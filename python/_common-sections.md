# Common Sections Reference

> **Purpose**: Shared boilerplate for all Python prompts  
> **Usage**: Reference this file instead of duplicating content  
> **Last Updated**: 2025-12-09

---

## Quick Context Checklist

Use this condensed checklist instead of the full "Inputs Required" section:

```
☐ Branch: `git branch --show-current`
☐ Changes: `git diff main...HEAD --name-only`
☐ Diff: `git diff main...HEAD`
☐ Python version (3.11+ recommended)
☐ Frameworks/libraries in use
☐ Pain points or constraints
```

---

## Standard Guard Clauses

Include these at the top of analysis output to handle edge cases:

### No Input Provided
```
NO_ACTIONABLE_INPUT

Unable to proceed without source material. Please provide:
- Python file(s) to analyze, OR
- Code pasted directly in the message, OR
- Repository URL with specific files to review

Example: "Review src/api/handlers.py for security issues"
```

### Empty Diff / No Changes
```
NO_CHANGES_DETECTED

No code changes found between branches.

Checked:
- `git diff main...HEAD` returned empty
- No modified Python files detected

Next steps:
- Verify you're on the correct branch
- Ensure changes are committed
- Try: `git status` to see uncommitted changes
```

### Analysis Complete - No Issues
```
NO_ISSUES_FOUND

✅ Analysis complete — no significant issues detected.

Summary:
- Files scanned: {{FILE_COUNT}}
- Checks performed: {{CHECK_TYPES}}
- Result: Code meets quality standards

Recommendation: Proceed with confidence.
```

### Analysis Complete - With Findings
```
ANALYSIS_COMPLETE

📋 Found {{ISSUE_COUNT}} items requiring attention.

Breakdown:
- 🔴 Critical: {{CRITICAL_COUNT}}
- 🟠 High: {{HIGH_COUNT}}
- 🟡 Medium: {{MEDIUM_COUNT}}
- 🟢 Low: {{LOW_COUNT}}

See detailed findings below.
```

---

## Severity Levels

Use consistent severity across all prompts:

| Level | Label | Criteria | Action |
|-------|-------|----------|--------|
| 🔴 | **Critical** | Security vulnerability, data loss risk, system crash | Fix immediately before merge |
| 🟠 | **High** | Bugs, significant performance issues, breaking changes | Fix before merge |
| 🟡 | **Medium** | Code quality, minor performance, maintainability | Should fix, can be follow-up |
| 🟢 | **Low** | Style, minor improvements, nice-to-haves | Optional, track for later |

---

## Standard Output Formats

### Markdown Report (Default)
```markdown
# [Analysis Type] Report

## Overview
- **Files Analyzed**: {{COUNT}}
- **Critical Issues**: {{COUNT}}
- **Recommendations**: {{COUNT}}

## Findings

### Finding 1: [Title]
- **Severity**: 🔴 Critical
- **Location**: `path/file.py:42-56`
- **Issue**: [Description]
- **Fix**: [Solution with code example]

## Summary
[Brief conclusion and next steps]
```

### JSON Output (For Agents)
```json
{
  "analysis_type": "security|performance|quality",
  "files_analyzed": 0,
  "findings": [
    {
      "id": "F001",
      "severity": "critical|high|medium|low",
      "title": "Issue title",
      "file": "path/file.py",
      "line_start": 42,
      "line_end": 56,
      "description": "What's wrong",
      "suggestion": "How to fix",
      "code_before": "problematic code",
      "code_after": "fixed code"
    }
  ],
  "summary": {
    "critical": 0,
    "high": 0,
    "medium": 0,
    "low": 0
  },
  "actionable": true
}
```

---

## 2026 Python Tool Stack

### Package Management
```bash
# Primary: uv (10-100x faster than pip)
uv pip install package-name
uv venv .venv
uv pip compile requirements.in -o requirements.txt

# Alternative: Poetry (if already in use)
poetry add package-name
```

### Code Quality (Single Tool)
```bash
# Ruff replaces: flake8, isort, pyupgrade, autoflake, bandit
uv pip install ruff
ruff check .          # Lint
ruff check --fix .    # Auto-fix
ruff format .         # Format (replaces Black)
```

### Type Checking
```bash
# Primary: mypy
uv pip install mypy
mypy src/

# Alternative: pyright (faster, stricter)
uv pip install pyright
pyright src/
```

### Testing
```bash
# pytest + plugins
uv pip install pytest pytest-cov pytest-asyncio hypothesis
pytest --cov=src --cov-report=term-missing
```

### Security
```bash
# Dependency audit
uv pip install pip-audit
pip-audit

# Static analysis (included in Ruff with S rules)
ruff check --select=S .
```

---

## Standard pyproject.toml Configuration

```toml
[project]
name = "your-project"
version = "0.1.0"
description = "Project description"
readme = "README.md"
requires-python = ">=3.11"
dependencies = []

[project.optional-dependencies]
dev = [
    "ruff>=0.8.0",
    "mypy>=1.13.0",
    "pytest>=8.0.0",
    "pytest-cov>=6.0.0",
]

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.ruff]
target-version = "py311"
line-length = 88
src = ["src"]

[tool.ruff.lint]
select = [
    "E",    # pycodestyle errors
    "W",    # pycodestyle warnings
    "F",    # Pyflakes
    "I",    # isort
    "B",    # flake8-bugbear
    "C4",   # flake8-comprehensions
    "UP",   # pyupgrade
    "S",    # flake8-bandit (security)
    "PTH",  # flake8-use-pathlib
    "RUF",  # Ruff-specific rules
]
ignore = ["E501"]  # Line too long (handled by formatter)

[tool.ruff.format]
docstring-code-format = true

[tool.mypy]
python_version = "3.11"
strict = true
warn_return_any = true
warn_unused_configs = true

[tool.pytest.ini_options]
testpaths = ["tests"]
asyncio_mode = "auto"
addopts = "-ra -q --cov=src"
```

---

## Pre-commit Configuration

```yaml
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.8.0
    hooks:
      - id: ruff
        args: [--fix]
      - id: ruff-format

  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v1.13.0
    hooks:
      - id: mypy
        additional_dependencies: []

  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v5.0.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
      - id: check-added-large-files
```

---

## Quick Reference Commands

```bash
# Project setup
uv venv .venv && source .venv/bin/activate
uv pip install -e ".[dev]"
pre-commit install

# Daily workflow
ruff check --fix . && ruff format .
mypy src/
pytest

# Before commit
pre-commit run --all-files

# Security check
pip-audit
ruff check --select=S .

# Update dependencies
uv pip compile requirements.in -o requirements.txt --upgrade
```

---

*This file is referenced by all Python prompts. Update here to apply changes everywhere.*
