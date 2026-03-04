# Execution Pattern (Terminal-First)

## Standard Sequence
1. Inspect repository shape and changed files.
2. Select one primary prompt path and one optional supporting prompt.
3. Implement minimal, high-impact changes first.
4. Run validations relevant to the touched areas.
5. Summarize outcomes with file references and remaining risks.

## Context Checklist
- Branch and diff scope.
- Relevant runtime/toolchain versions.
- Target constraints (security, performance, compatibility).
- Expected deliverable format.

## Validation Checklist
- Run `bash scripts/qa/run_docs_qa.sh` for documentation and prompt changes.
- Confirm no broken internal links or metadata regressions.
- Confirm compatibility paths are preserved when touching `html/` content.
