# agents.md – Frontend/HTML Prompts

## Purpose
This folder contains frontend prompt templates for accessibility, semantic markup, performance (Core Web Vitals), CSS architecture, and code review. Designed for use by AI agents, Copilot coding agent, or LLM-powered tools to deliver actionable, standards-compliant improvements for web projects.

## Agent Usage Scenarios
- Automated accessibility audits (WCAG 2.2, ARIA, keyboard navigation)
- Semantic HTML and CSS architecture review (BEM, utility-first)
- Performance analysis (LCP, CLS, INP) and optimization suggestions
- Generating technical reports for PRs or refactor proposals

## How Agents Should Use These Prompts
1. Select the prompt matching the code context (e.g. accessibility-check.md for a11y).
2. Follow the report structure and severity ranking in the prompt.
3. Output findings in ranked order (Critical/High/Medium/Low) with WCAG references.
4. Prefer minimal, semantic diffs for code changes; avoid broad rewrites.
5. Use unified diff format for patches; preserve existing spacing and comments.
6. For tests, generate code for keyboard navigation, ARIA state, and conditional rendering.
7. Ask for clarification if framework, design system, or project structure is unclear.

## Best Practices
- Always audit landmarks, heading hierarchy, and ARIA before suggesting changes.
- Validate all suggestions against the provided code context.
- Do not fabricate build/test steps; these prompts are for analysis and review only.
- Encourage incremental improvement: report → patch → test → validate.

## Example Agent Workflow
1. Run accessibility-check.md on selected files.
2. Output a technical report with ranked findings and WCAG refs.
3. Generate a minimal patch for top accessibility or semantic issue.
4. Propose tests for keyboard navigation and ARIA state.
5. Summarize risk and rollback steps.

---
For other domains, see agents.md in the generic, python, or ruby folders.
