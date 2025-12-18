# Generic Development Prompts — Index

> **Purpose**: Universal prompts for any programming language or framework  
> **Best For**: Copilot, ChatGPT, Claude, Agents  
> **Languages**: Any  
> **Last Updated**: 2025-12

---

## Prompt File Index

| File | Purpose | Use When |
|------|---------|----------|
| [ci-cd-pipeline-analysis.md](ci-cd-pipeline-analysis.md) | CI/CD pipeline setup and optimization | Setting up or improving build pipelines |
| [code-refactoring.md](code-refactoring.md) | Code quality improvements | Cleaning up or restructuring code |
| [copilot-instructions.md](copilot-instructions.md) | AI assistant configuration | Customizing Copilot/AI behavior |
| [do-next.md](do-next.md) | Project re-engagement planning | Returning to a project after a break |
| [documentation-generation.md](documentation-generation.md) | Documentation creation | Writing READMEs, API docs, guides |
| [pr-review-feedback.md](pr-review-feedback.md) | Pull request code review | Reviewing PRs for quality |
| [project-repo.md](project-repo.md) | Repository setup | Starting new projects |
| [security-analysis.md](security-analysis.md) | Security vulnerability scanning | Finding and fixing security issues |
| [system-design-architecture-review.md](system-design-architecture-review.md) | Architecture evaluation | Reviewing system design |

---

## Quick Context Checklist

For any generic prompt, provide:

```
☐ Code/files to analyze
☐ Language and framework
☐ Current issues or pain points
☐ Constraints (time, compatibility, etc.)
```

---

## Copy-Paste Quick Prompts

### Prompt: General Code Review
```text
Review this code for issues:

{{CODE}}

Language: {{LANGUAGE}}

Check for:
1. Bugs and logic errors
2. Security vulnerabilities
3. Performance problems
4. Code quality issues
5. Missing error handling

Output severity as: 🔴 Critical | 🟠 High | 🟡 Medium | 🟢 Low
```

### Prompt: Quick Refactor
```text
Refactor this code for clarity:

{{CODE}}

Goals:
- Improve readability
- Reduce complexity
- Follow {{LANGUAGE}} best practices
- Add error handling if missing

Show the improved version with comments explaining changes.
```

### Prompt: Generate Documentation
```text
Generate documentation for this code:

{{CODE}}

Create:
1. Function/method docstrings
2. Usage examples
3. Parameter descriptions
4. Return value documentation
```

### Prompt: Debug Help
```text
Help debug this issue:

Code:
{{CODE}}

Error/Problem:
{{ERROR}}

Expected behavior: {{EXPECTED}}
Actual behavior: {{ACTUAL}}

Identify the root cause and provide a fix.
```

### Prompt: What Should I Do Next?
```text
Analyze this project and suggest next steps:

Project structure:
{{STRUCTURE}}

Recent changes:
{{RECENT_COMMITS}}

Current issues:
{{ISSUES}}

Suggest prioritized action items for the next work session.
```

---

## Severity Levels

| Level | Icon | Description |
|-------|------|-------------|
| **Critical** | 🔴 | Security vulnerability, data loss risk, system crash |
| **High** | 🟠 | Bug in main functionality, performance issue |
| **Medium** | 🟡 | Code quality issue, missing tests |
| **Low** | 🟢 | Style improvement, optimization opportunity |

---

## Workflow Examples

### Starting a New Project
1. Use [project-repo.md](project-repo.md) for structure setup
2. Use [documentation-generation.md](documentation-generation.md) for README
3. Use [ci-cd-pipeline-analysis.md](ci-cd-pipeline-analysis.md) for CI setup

### Code Review Workflow
1. Use [pr-review-feedback.md](pr-review-feedback.md) for PR review
2. Use [security-analysis.md](security-analysis.md) for security check
3. Use [code-refactoring.md](code-refactoring.md) for improvements

### Returning to a Project
1. Use [do-next.md](do-next.md) for project assessment
2. Use [code-refactoring.md](code-refactoring.md) for cleanup
3. Use [documentation-generation.md](documentation-generation.md) to update docs
