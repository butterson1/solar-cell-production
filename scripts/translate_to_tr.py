#!/usr/bin/env python3

from __future__ import annotations

import argparse
import json
import re
import shutil
import time
import urllib.parse
import urllib.request
from pathlib import Path

import tomllib


ROOT = Path(__file__).resolve().parent.parent
EN_SRC = ROOT / "en" / "src"
TR_SRC = ROOT / "tr" / "src"
API = "https://translate.googleapis.com/translate_a/single?client=gtx&sl=en&tl=tr&dt=t&q="

PLACEHOLDER_RE = re.compile(r"__PH_\d+__")
SEP = "__TRSEP__"

GLOSSARY = [
    ("Solar cell", "Güneş hücresi"),
    ("solar cell", "güneş hücresi"),
    ("Solar cells", "Güneş hücreleri"),
    ("solar cells", "güneş hücreleri"),
    ("solar panel", "güneş paneli"),
    ("Solar panel", "Güneş paneli"),
    ("solar panels", "güneş panelleri"),
    ("Solar panels", "Güneş panelleri"),
    ("module", "modül"),
    ("Module", "Modül"),
    ("modules", "modüller"),
    ("Module-level", "Modül düzeyinde"),
    ("photovoltaic", "fotovoltaik"),
    ("Photovoltaic", "Fotovoltaik"),
    ("wafer", "wafer"),
    ("Wafer", "Wafer"),
    ("junction box", "bağlantı kutusu"),
    ("Junction box", "Bağlantı kutusu"),
    ("encapsulant", "enkapsülant"),
    ("Encapsulant", "Enkapsülant"),
    ("backsheet", "arka tabaka"),
    ("Backsheet", "Arka tabaka"),
    ("fill factor", "dolum faktörü"),
    ("Fill factor", "Dolum faktörü"),
    ("single-axis tracker", "tek eksenli takip sistemi"),
    ("single-axis trackers", "tek eksenli takip sistemleri"),
    ("grid-connected", "şebekeye bağlı"),
    ("hot spot", "sıcak nokta"),
    ("hotspot", "sıcak nokta"),
    ("TOPCon", "TOPCon"),
    ("PERC", "PERC"),
    ("HJT", "HJT"),
    ("CdTe", "CdTe"),
    ("CIGS", "CIGS"),
    ("AM1.5", "AM1.5"),
]


def call_translate(text: str) -> str:
    url = API + urllib.parse.quote(text)
    for attempt in range(4):
        try:
            with urllib.request.urlopen(url, timeout=30) as response:
                data = json.loads(response.read().decode("utf-8"))
            return "".join(part[0] for part in data[0])
        except Exception:
            if attempt == 3:
                raise
            time.sleep(1.5 * (attempt + 1))
    raise RuntimeError("unreachable")


def apply_glossary(text: str) -> str:
    for src, dst in GLOSSARY:
        text = text.replace(src, dst)
    text = text.replace("Güneş Pili", "Güneş Hücresi")
    text = text.replace("güneş pili", "güneş hücresi")
    text = text.replace("fotovoltaik etki", "fotovoltaik etki")
    text = text.replace("güneş modülü", "güneş modülü")
    text = text.replace("akışın", "akımın")
    text = text.replace("şebekeye", "şebekeye")
    return text


def protect(text: str) -> tuple[str, dict[str, str]]:
    placeholders: dict[str, str] = {}

    def repl(match: re.Match[str]) -> str:
        token = f"__PH_{len(placeholders)}__"
        placeholders[token] = match.group(0)
        return token

    patterns = [
        r"`[^`]+`",
        r"\{\{#quiz [^}]+\}\}",
        r"https?://\S+",
        r"\b[A-Z]{2,}(?:[A-Z0-9-]{0,})\b",
    ]
    protected = text
    for pattern in patterns:
        protected = re.sub(pattern, repl, protected)
    return protected, placeholders


def restore(text: str, placeholders: dict[str, str]) -> str:
    for token, value in placeholders.items():
        text = text.replace(token, value)
    return text


def translate_text(text: str) -> str:
    if not re.search(r"[A-Za-z]", text):
        return text
    protected, placeholders = protect(text)
    translated = call_translate(protected)
    translated = restore(translated, placeholders)
    return apply_glossary(translated)


def translate_batch(items: list[str]) -> list[str]:
    if not items:
        return []
    if len(items) == 1:
        return [translate_text(items[0])]

    protected_items = []
    placeholder_maps = []
    for item in items:
        protected, placeholders = protect(item)
        protected_items.append(protected)
        placeholder_maps.append(placeholders)

    translated_blob = call_translate(f"\n{SEP}\n".join(protected_items))
    translated_parts = translated_blob.split(f"\n{SEP}\n")
    if len(translated_parts) != len(items):
        return [translate_text(item) for item in items]

    output = []
    for translated, placeholders in zip(translated_parts, placeholder_maps):
        restored = restore(translated, placeholders)
        output.append(apply_glossary(restored))
    return output


def translate_markdown_line(line: str) -> str:
    stripped = line.strip()
    if not stripped:
        return line
    if stripped.startswith("{{#quiz "):
        return line
    if stripped == "---":
        return line

    match = re.match(r"^(\s*#+\s+)(.*)$", line)
    if match:
        return match.group(1) + translate_text(match.group(2))

    match = re.match(r"^(\s*[-*]\s+)\[(.+)\]\((.+)\)\s*$", line)
    if match:
        return f"{match.group(1)}[{translate_text(match.group(2))}]({match.group(3)})"

    match = re.match(r"^(\s*)\[(.+)\]\((.+)\)\s*$", line)
    if match:
        return f"{match.group(1)}[{translate_text(match.group(2))}]({match.group(3)})"

    match = re.match(r"^(\s*\d+\.\s+)(.*)$", line)
    if match:
        return match.group(1) + translate_text(match.group(2))

    match = re.match(r"^(\s*[-*]\s+)(.*)$", line)
    if match:
        return match.group(1) + translate_text(match.group(2))

    return translate_text(line)


def translate_markdown_file(src: Path, dst: Path) -> None:
    blocks = src.read_text(encoding="utf-8").split("\n\n")
    translated_blocks: list[str] = []
    pending: list[str] = []
    pending_indexes: list[int] = []

    def flush() -> None:
        nonlocal pending, pending_indexes
        if not pending:
            return
        for idx, translated in zip(pending_indexes, translate_batch(pending)):
            translated_blocks[idx] = translated
        pending = []
        pending_indexes = []

    for block in blocks:
        translated_blocks.append(block)
        idx = len(translated_blocks) - 1
        stripped = block.strip()
        if not stripped or stripped == "---" or stripped.startswith("{{#quiz "):
            continue
        if "\n" in block and all(line.lstrip().startswith(("- [", "#", "##", "###")) for line in block.splitlines() if line.strip()):
            translated_blocks[idx] = "\n".join(translate_markdown_line(line) for line in block.splitlines())
            continue
        if len(block) < 2600:
            pending.append(block)
            pending_indexes.append(idx)
            if sum(len(item) for item in pending) > 6000 or len(pending) >= 6:
                flush()
            continue
        translated_blocks[idx] = translate_text(block)

    flush()
    dst.write_text("\n\n".join(translated_blocks).rstrip() + "\n", encoding="utf-8")


def translate_value(value):
    if isinstance(value, list):
        if value and all(isinstance(item, str) for item in value):
            return translate_batch(value)
        return [translate_value(item) for item in value]
    if isinstance(value, dict):
        translated = {}
        batch_keys = [key for key, item in value.items() if isinstance(item, str)]
        if batch_keys:
            translated_values = translate_batch([value[key] for key in batch_keys])
            for key, translated_value in zip(batch_keys, translated_values):
                translated[key] = translated_value
        for key, item in value.items():
            if key in translated:
                continue
            translated[key] = translate_value(item)
        return translated
    if isinstance(value, str):
        return translate_text(value)
    return value


def toml_string(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def write_quiz_file(data: dict, dst: Path) -> None:
    lines: list[str] = []
    for question in data["questions"]:
        lines.append("[[questions]]")
        lines.append(f'type = "{question["type"]}"')
        if "prompt" in question:
            prompt = question["prompt"]
            if "prompt" in prompt:
                lines.append(f"prompt.prompt = {toml_string(prompt['prompt'])}")
            if "distractors" in prompt:
                lines.append("prompt.distractors = [")
                for item in prompt["distractors"]:
                    lines.append(f"  {toml_string(item)},")
                lines.append("]")
        if "answer" in question:
            answer = question["answer"]
            if "answer" in answer:
                lines.append(f"answer.answer = {toml_string(answer['answer'])}")
            if "alternatives" in answer:
                lines.append("answer.alternatives = [")
                for item in answer["alternatives"]:
                    lines.append(f"  {toml_string(item)},")
                lines.append("]")
        if "alternatives" in question:
            lines.append("alternatives = [")
            for item in question["alternatives"]:
                lines.append(f"  {toml_string(item)},")
            lines.append("]")
        if "context" in question:
            lines.append(f"context = {toml_string(question['context'])}")
        if "id" in question:
            lines.append(f'id = "{question["id"]}"')
        lines.append("")
    dst.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def translate_quiz_file(src: Path, dst: Path) -> None:
    data = tomllib.loads(src.read_text(encoding="utf-8"))
    translated = translate_value(data)
    for question, original in zip(translated["questions"], data["questions"]):
        question["type"] = original["type"]
        question["id"] = original["id"]
    write_quiz_file(translated, dst)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--force", action="store_true", help="Replace an existing Turkish source tree.")
    args = parser.parse_args()

    if TR_SRC.exists():
        if not args.force:
            raise SystemExit("tr/src already exists. Re-run with --force to overwrite it.")
        shutil.rmtree(TR_SRC)

    shutil.copytree(EN_SRC, TR_SRC)

    for path in sorted(TR_SRC.rglob("*.md")):
        relative = path.relative_to(TR_SRC)
        print(f"md   {relative}")
        translate_markdown_file(EN_SRC / relative, path)

    for path in sorted(TR_SRC.joinpath("quizzes").glob("*.toml")):
        relative = path.relative_to(TR_SRC)
        print(f"quiz {relative}")
        translate_quiz_file(EN_SRC / relative, path)


if __name__ == "__main__":
    main()
