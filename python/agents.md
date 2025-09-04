# agents.md – Python Prompts

## Purpose
This folder contains Python-specific prompt templates for code analysis, refactoring, type safety, async/concurrency, ORM optimization, and test coverage. Designed for use by AI agents, Copilot coding agent, or LLM-powered tools to deliver actionable, context-aware improvements for Python projects.

## Agent Usage Scenarios
- Automated Python code review (type hints, async correctness, security)
- Generating technical reports for PRs, refactors, or test coverage audits
- Suggesting incremental type adoption and mypy/pyright compliance
- Identifying performance bottlenecks and unsafe patterns

## How Agents Should Use These Prompts
1. Select the prompt matching the code context (e.g. type-hinting.md for type safety).
2. Follow the report structure and severity ranking in the prompt.
3. Output findings in ranked order (Critical/High/Medium/Low).
4. Prefer minimal, dependency-safe diffs for code changes.
5. Use unified diff format for patches; avoid unrelated rewrites.
6. For tests, generate pytest-style code focused on new/changed logic.
7. Ask for clarification if Python version, framework, or project structure is unclear.

## Best Practices
- Use explicit, modern type hints and static analysis tools.
- Flag blocking calls in async code and unsafe DB/ORM patterns.
- Validate all suggestions against the provided code context.
- Do not fabricate build/test steps; these prompts are for analysis and review only.
- Encourage incremental improvement: report → patch → test → validate.

## Example Agent Workflow
1. Run type-hinting.md on selected files.
2. Output a technical report with ranked findings.
3. Generate a minimal patch for top type safety or performance issue.
4. Propose pytest tests for new/changed logic.
5. Summarize risk and rollback steps.

---
For generic or other language instructions, see agents.md in the generic, html, or ruby folders.
