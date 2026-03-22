#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

mdbook build "${ROOT_DIR}/en"
mdbook build "${ROOT_DIR}/tr"
cp "${ROOT_DIR}/site/index.html" "${ROOT_DIR}/dist/index.html"

printf 'Built English book at %s\n' "${ROOT_DIR}/dist/en"
printf 'Built Turkish book at %s\n' "${ROOT_DIR}/dist/tr"
