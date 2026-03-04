---
name: claudeai-pgp
description: Route work to the correct Pretty Good Prompts (PGP) document and produce structured, artifact-oriented outputs for Claude workflows. Use when tasks in this repository (or repositories consuming these prompts) require high-quality analysis, modernization planning, documentation updates, or implementation guidance across AI, frontend, backend, infra, database, Python, Ruby, or HTML domains.
---

# ClaudeAI PGP

## Overview
Use this skill to pick the right PGP prompt, structure outputs for clarity, and keep repository documentation and guidance internally consistent.

## Workflow
1. Select the best prompt path with [references/prompt-routing.md](references/prompt-routing.md).
2. Build a concise context summary before recommendations.
3. Produce structured artifacts with explicit sections, priorities, and acceptance criteria.
4. Validate documentation integrity and metadata before final delivery:
   - `bash scripts/qa/run_docs_qa.sh`
5. Align prompt edits with [../../docs/prompt-standards.md](../../docs/prompt-standards.md).

## Decision Rules
- Choose one primary domain prompt and only add secondary prompts when they materially improve quality.
- Keep outputs decision-complete: no hidden assumptions, no missing acceptance criteria.
- For compatibility migrations, preserve existing paths and provide explicit forward links.

## Artifact Contract
- Findings first for review/audit requests.
- Implementation plan must include interfaces changed, tests, and defaults.
- Documentation outputs must include exact file targets.

## References
- [references/prompt-routing.md](references/prompt-routing.md)
- [references/artifact-pattern.md](references/artifact-pattern.md)
- [../../docs/prompt-standards.md](../../docs/prompt-standards.md)
