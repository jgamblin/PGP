---
name: codex-pgp
description: Route work to the correct Pretty Good Prompts (PGP) document and execute terminal-first implementation workflows. Use when operating in this repository (or a repo consuming these prompts) for modernization, code review, refactoring, infrastructure, database, Python, Ruby, frontend, HTML/CSS, or AI/LLM tasks that need a precise prompt selection and execution path.
---

# Codex PGP

## Overview
Use this skill to select the best PGP prompt file for the task, gather the required repository context, and produce implementation-ready outputs with clear validation steps.

## Workflow
1. Classify the request by domain and intent using [references/prompt-routing.md](references/prompt-routing.md).
2. Gather minimum context before proposing changes: changed files, constraints, stack versions, and expected output format.
3. Apply prompt guidance from the selected file and keep outputs concise, action-oriented, and reproducible.
4. Enforce repository quality checks before finalizing changes:
   - `bash scripts/qa/run_docs_qa.sh`
5. If the task affects docs or prompt quality, align with [../../docs/prompt-standards.md](../../docs/prompt-standards.md).

## Decision Rules
- Prefer domain-specific prompts over generic ones when both apply.
- Use `generic/` prompts when tasks span multiple stacks or are architecture/process focused.
- Keep `html/` references backward-safe and cross-link to `frontend/` guidance when modern equivalents exist.
- For review tasks, prioritize defects and risks first, then remediation order.

## Output Contract
- Start with key findings or implementation outcome.
- Include exact file paths and verification commands.
- List unresolved risks or assumptions explicitly.

## References
- [references/prompt-routing.md](references/prompt-routing.md)
- [references/execution-pattern.md](references/execution-pattern.md)
- [../../docs/prompt-standards.md](../../docs/prompt-standards.md)
