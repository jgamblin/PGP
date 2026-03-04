#!/usr/bin/env bash
set -euo pipefail

repo_root=$(cd "$(dirname "$0")/../.." && pwd)
cd "$repo_root"

python3 scripts/qa/validate_metadata.py
python3 scripts/qa/check_internal_links.py
python3 scripts/qa/check_mojibake.py
