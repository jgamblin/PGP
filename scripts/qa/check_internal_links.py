#!/usr/bin/env python3
"""Check local markdown links across repository markdown files."""

from __future__ import annotations

from pathlib import Path
import re
import sys

LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


def is_external(target: str) -> bool:
    lowered = target.lower()
    return lowered.startswith(("http://", "https://", "mailto:"))


def iter_markdown_files(root: Path) -> list[Path]:
    return sorted(p for p in root.rglob("*.md") if ".git" not in p.parts)


def normalize_target(raw_target: str) -> str:
    target = raw_target.strip()
    if target.startswith("<") and target.endswith(">"):
        target = target[1:-1]
    target = target.split("#", 1)[0]
    target = target.split("?", 1)[0]
    return target.strip()


def main() -> int:
    root = Path(__file__).resolve().parents[2]
    errors: list[str] = []

    for md_file in iter_markdown_files(root):
        rel = md_file.relative_to(root)
        in_fence = False

        with md_file.open("r", encoding="utf-8") as fh:
            for idx, raw in enumerate(fh, start=1):
                line = raw.rstrip("\n")
                if line.lstrip().startswith("```"):
                    in_fence = not in_fence
                    continue
                if in_fence:
                    continue

                for match in LINK_RE.finditer(line):
                    raw_target = match.group(1)
                    target = normalize_target(raw_target)
                    if not target or target.startswith("#") or is_external(target):
                        continue

                    resolved = (md_file.parent / target).resolve()
                    if not resolved.exists():
                        errors.append(f"{rel}:{idx} -> {raw_target}")

    print(f"Scanned markdown links in {len(iter_markdown_files(root))} markdown files.")
    if errors:
        print("Broken local links found:")
        for entry in errors:
            print(f"- {entry}")
        return 1

    print("Internal markdown link check passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
