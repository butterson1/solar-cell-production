# pv.bayram.cloud mdBook

This repository now contains two mdBook builds from the same source repo:

- `en/`: English source book
- `tr/`: Turkish source book

Both books are built into separate output directories:

- `dist/en/`
- `dist/tr/`

## Build

Build both books and a simple root language selector:

```bash
./scripts/build-all.sh
```

Build a single language directly with mdBook:

```bash
mdbook build en
mdbook build tr
```

## Turkish source regeneration

The Turkish source tree can be regenerated from the English source with:

```bash
./scripts/translate_to_tr.py --force
```

This copies `en/src/` to `tr/src/`, translates markdown chapters and quiz text, and preserves quiz assets and IDs.

## Deploy under `/en` and `/tr`

After `./scripts/build-all.sh`, publish:

- `dist/en/` to the server path served at `/en/`
- `dist/tr/` to the server path served at `/tr/`
- optional: `dist/index.html` at `/` for a language chooser

Example sync pattern:

```bash
rsync -av --delete dist/en/ user@host:/var/www/pv/en/
rsync -av --delete dist/tr/ user@host:/var/www/pv/tr/
rsync -av dist/index.html user@host:/var/www/pv/index.html
```
