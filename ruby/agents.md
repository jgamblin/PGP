# agents.md – Ruby/Rails Prompts

## Purpose
This folder contains Ruby and Rails prompt templates for code review, ActiveRecord performance, transaction safety, service object refactoring, security, and test coverage. Designed for use by AI agents, Copilot coding agent, or LLM-powered tools to deliver actionable, context-aware improvements for Ruby projects.

## Agent Usage Scenarios
- Automated Rails code review (N+1, transaction safety, strong params)
- Generating technical reports for PRs, refactors, or test coverage audits
- Suggesting incremental, dependency-safe code improvements
- Identifying security risks and missing specs

## How Agents Should Use These Prompts
1. Select the prompt matching the code context (e.g. rubocop-compliance.md for style).
2. Follow the report structure and severity ranking in the prompt.
3. Output findings in ranked order (Critical/High/Medium/Low).
4. Prefer minimal, dependency-safe diffs for code changes.
5. Use unified diff format for patches; avoid unrelated rewrites.
6. For tests, generate RSpec code focused on new/changed logic.
7. Ask for clarification if Rails version, DB, or project structure is unclear.

## Best Practices
- Flag N+1 risks, transaction gaps, and missing strong params.
- Validate all suggestions against the provided code context.
- Do not fabricate build/test steps; these prompts are for analysis and review only.
- Encourage incremental improvement: report → patch → test → validate.

## Example Agent Workflow
1. Run code-refactoring.md or rubocop-compliance.md on selected files.
2. Output a technical report with ranked findings.
3. Generate a minimal patch for top performance or safety issue.
4. Propose RSpec tests for new/changed logic.
5. Summarize risk and rollback steps.

---
For other domains, see agents.md in the generic, python, or html folders.
