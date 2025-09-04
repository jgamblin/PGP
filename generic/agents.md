# agents.md – Generic Prompts

## Purpose
This folder contains universal, language-agnostic prompt templates for code analysis, refactoring, documentation, and review. These are designed for use by AI agents, Copilot coding agent, or any LLM-powered tool to deliver high-signal, actionable feedback across any codebase.

## Agent Usage Scenarios
- Automated code review (security, performance, architecture)
- Generating technical reports for PRs or refactor proposals
- Repository health audits and documentation scaffolding
- Suggesting incremental, low-risk code improvements

## How Agents Should Use These Prompts
1. Select the most relevant prompt for the code context (e.g. code-refactoring.md for refactor analysis).
2. Follow the report structure and severity taxonomy provided in the prompt.
3. Always output findings in ranked order (Critical/High/Medium/Low).
4. Prefer minimal diffs and actionable suggestions over broad rewrites.
5. When generating patches, use unified diff format and include only necessary changes.
6. For documentation, follow the provided scaffolding and update only missing or outdated sections.
7. Ask for clarification if code context or project structure is ambiguous.

## Best Practices
- Maintain a neutral, technical tone—avoid speculation or business impact claims.
- Use explicit headings and consistent formatting for all reports.
- Validate all suggestions against the provided code context.
- Do not fabricate build/test steps; these prompts are for analysis and review only.
- Encourage incremental improvement: report → patch → test → validate.

## Example Agent Workflow
1. Run code-refactoring.md on selected files.
2. Output a technical report with ranked findings.
3. Generate a minimal patch for the top issue.
4. Propose targeted tests for new/changed logic.
5. Summarize risk and rollback steps.

---
For more domain-specific instructions, see the agents.md in the python, html, or ruby folders.
