#!/usr/bin/env python3
"""Validate required prompt metadata across all prompt files."""

from __future__ import annotations

from pathlib import Path
import re
import sys

PROMPT_DIRS = [
    "ai",
    "db",
    "frontend",
    "generic",
    "html",
    "infrastructure",
    "python",
    "ruby",
]
REQUIRED_KEYS = ("Purpose", "Best For", "Scope", "Last Updated")
LAST_UPDATED_RE = re.compile(r"^\d{4}-\d{2}$")
HEADER_RE = re.compile(r"^>\s+\*\*(.+?)\*\*:\s*(.*?)\s*$")


def iter_prompt_files(root: Path) -> list[Path]:
    files: list[Path] = []
    for rel in PROMPT_DIRS:
        files.extend(sorted((root / rel).glob("*.md")))
    return files


def parse_metadata(md_path: Path) -> dict[str, str]:
    meta: dict[str, str] = {}
    with md_path.open("r", encoding="utf-8") as fh:
        for raw in fh:
            line = raw.rstrip("\n")
            match = HEADER_RE.match(line)
            if match:
                key, value = match.groups()
                meta[key] = value
            # Metadata block always lives near the top.
            if line.startswith("---") and meta:
                break
    return meta


def main() -> int:
    root = Path(__file__).resolve().parents[2]
    files = iter_prompt_files(root)
    errors: list[str] = []

    for file_path in files:
        rel = file_path.relative_to(root)
        metadata = parse_metadata(file_path)
        for key in REQUIRED_KEYS:
            if key not in metadata:
                errors.append(f"{rel}: missing metadata '{key}'")
        if "Last Updated" in metadata and not LAST_UPDATED_RE.match(metadata["Last Updated"]):
            errors.append(
                f"{rel}: Last Updated value '{metadata['Last Updated']}' is not YYYY-MM"
            )

    print(f"Scanned {len(files)} prompt files.")
    if errors:
        print("Metadata validation failed:")
        for entry in errors:
            print(f"- {entry}")
        return 1

    print("Metadata validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
