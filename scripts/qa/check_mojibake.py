#!/usr/bin/env python3
"""Fail when replacement-character mojibake exists in markdown files."""

from __future__ import annotations

from pathlib import Path


def iter_markdown_files(root: Path) -> list[Path]:
    return sorted(p for p in root.rglob("*.md") if ".git" not in p.parts)


def main() -> int:
    root = Path(__file__).resolve().parents[2]
    offenders: list[str] = []

    for md_file in iter_markdown_files(root):
        rel = md_file.relative_to(root)
        with md_file.open("r", encoding="utf-8") as fh:
            for idx, line in enumerate(fh, start=1):
                if "\ufffd" in line:
                    offenders.append(f"{rel}:{idx}")

    print(f"Scanned {len(iter_markdown_files(root))} markdown files.")
    if offenders:
        print("Replacement-character mojibake found:")
        for entry in offenders:
            print(f"- {entry}")
        return 1

    print("No mojibake found.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
