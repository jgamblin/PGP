# Python Assistant Prompts

> **Purpose**: Index of all Python development prompts  
> **Best For**: Copilot, ChatGPT, Claude, Agents  
> **Python Version**: 3.11+  
> **Last Updated**: 2025-12-09

---

## Quick Start

Choose the assistant that matches your task:

| Task | File | Description |
|------|------|-------------|
| **New Project** | [project-repo.md](project-repo.md) | Initialize project structure and tooling |
| **Code Review** | [pr-review-feedback.md](pr-review-feedback.md) | PR review, refactoring, quality checks |
| **Refactoring** | [code-refactoring.md](code-refactoring.md) | Improve code structure and patterns |
| **Testing** | [unit-test-generation.md](unit-test-generation.md) | pytest, coverage, property testing |
| **Type Safety** | [type-hinting.md](type-hinting.md) | Type hints, Pydantic, validation |
| **Security** | [security-analysis.md](security-analysis.md) | Vulnerability scanning, secure patterns |
| **Documentation** | [documentation-generation.md](documentation-generation.md) | Docstrings, API docs, README |
| **CLI Apps** | [cli-application-development.md](cli-application-development.md) | Click, Typer, Rich terminal UIs |
| **Database** | [database-schema-orm-optimization.md](database-schema-orm-optimization.md) | SQLAlchemy, database patterns |
| **Error Handling** | [logging-error-handling.md](logging-error-handling.md) | Logging, exceptions, Result types |
| **Packaging** | [packaging-distribution.md](packaging-distribution.md) | uv, PyPI, distribution |
| **Modern Patterns** | [modern-patterns.md](modern-patterns.md) | Python 3.11+ features, async, AI |
| **Async** | [concurrency-asyncio-pattern-analysis.md](concurrency-asyncio-pattern-analysis.md) | Async/await patterns |
| **Linting** | [python-linting.md](python-linting.md) | Ruff, code style |

---

## Shared Resources

- **[_common-sections.md](_common-sections.md)** — Shared boilerplate, tool configs, guard clauses

---

## Quick Context Checklist

Copy this into any prompt:

```
☐ Branch: `git branch --show-current`
☐ Changes: `git diff main...HEAD --name-only`
☐ Python: 3.11+ / 3.12+
☐ Frameworks: [Django/Flask/FastAPI/none]
☐ Pain points: [specific issues]
```

---

## Guard Clauses

All prompts handle these edge cases:

| Situation | Response Token |
|-----------|----------------|
| No input provided | `NO_ACTIONABLE_INPUT` |
| Empty diff | `NO_CHANGES_DETECTED` |
| Analysis clean | `NO_ISSUES_FOUND` |
| Issues found | `ANALYSIS_COMPLETE` |

See [_common-sections.md](_common-sections.md) for full templates.

---

## 2026 Tool Stack

```bash
# Package management (10-100x faster than pip)
uv pip install package-name

# Linting + formatting (replaces flake8, isort, black)
ruff check --fix . && ruff format .

# Type checking
mypy src/

# Testing
pytest --cov=src

# Security
pip-audit && ruff check --select=S .
```

---

## Severity Levels

Use consistent severity across all analyses:

| Level | When to Use |
|-------|-------------|
| 🔴 **Critical** | Security vulnerability, data loss, crashes |
| 🟠 **High** | Bugs, performance issues, breaking changes |
| 🟡 **Medium** | Code quality, maintainability issues |
| 🟢 **Low** | Style, minor improvements |

---

## Copy-Paste Prompts

### Quick Code Review
```text
Review this Python code for issues:

{{CODE}}

Check: security, performance, code quality, testing gaps.
Output severity as: 🔴 Critical, 🟠 High, 🟡 Medium, 🟢 Low

If no issues: output `NO_ISSUES_FOUND`
```

### Quick Refactor
```text
Refactor this Python code to be more Pythonic:

{{CODE}}

Apply:
- List/dict comprehensions where clearer
- Context managers for resources
- f-strings for formatting
- Type hints on function signatures
- Dataclasses for data containers

Show before/after with explanations.
```

### Quick Type Hints
```text
Add type hints to this Python code:

{{CODE}}

Requirements:
- All function parameters and returns
- Use modern syntax (X | None, not Optional[X])
- Use collections.abc for generic types
- Add Literal for string constants

If already fully typed: output `ALREADY_TYPED`
```

### Quick Security Scan
```text
Security scan this Python code:

{{CODE}}

Check for:
- SQL/command injection
- Hardcoded secrets
- Unsafe deserialization
- Path traversal

Output as: 🔴 Critical | 🟠 High | 🟡 Medium | 🟢 Low

If clean: output `NO_SECURITY_ISSUES`
```

### Quick Test Generation
```text
Generate pytest tests for this code:

{{CODE}}

Include:
- Happy path tests
- Edge cases (empty, None, boundaries)
- Error conditions
- Use @pytest.mark.parametrize for variants

Output ready-to-run test code.
```

---

## How to Use These Prompts

1. Choose the assistant that matches your needs
2. Copy the relevant prompt
3. Replace `{{PLACEHOLDERS}}` with your actual content
4. Paste into Copilot, ChatGPT, Claude, or your agent system

---

## Workflow Examples

### New Feature Development
1. [project-repo.md](project-repo.md) — Set up project if new
2. Write feature code
3. [type-hinting.md](type-hinting.md) — Add type hints
4. [unit-test-generation.md](unit-test-generation.md) — Write tests
5. [pr-review-feedback.md](pr-review-feedback.md) — Self-review before PR

### PR Review
1. [pr-review-feedback.md](pr-review-feedback.md) — Full review with suggestions
2. Check [security-analysis.md](security-analysis.md) for sensitive changes
3. Verify [unit-test-generation.md](unit-test-generation.md) coverage

### Modernization
1. [modern-patterns.md](modern-patterns.md) — Apply 3.11+ features
2. [type-hinting.md](type-hinting.md) — Add comprehensive types
3. [logging-error-handling.md](logging-error-handling.md) — Structured logging

---

*For tool configurations and shared sections, see [_common-sections.md](_common-sections.md)*
