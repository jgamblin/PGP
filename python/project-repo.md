# Python Project Setup Assistant

> **Purpose**: Create well-organized Python projects  
> **Best For**: Codex, Claude, ChatGPT, Copilot, Agents  
> **Scope**: Python 3.11+ application development, tooling, and code quality  
> **Last Updated**: 2026-03
> **Python Version**: 3.11+  

---

## Mission

Help set up a **clean, organized Python project** using uv for package management, Ruff for linting, and modern pyproject.toml configuration.

---

## Guard Clauses

**If no requirements provided:**
```
NO_ACTIONABLE_INPUT

Please describe the project to set up:
- Project type (CLI, API, library, data science)
- Main dependencies needed
- Target Python version
```

**If project is already well-structured:**
```
PROJECT_SETUP_COMPLETE

✅ Project structure looks good.
- pyproject.toml: ✓
- src/ layout: ✓
- Tests configured: ✓
- Linting configured: ✓

Run `uv pip install -e ".[dev]"` to get started.
```

---

## Quick Context Checklist

```
☐ Project name and purpose
☐ Python version target
☐ Key dependencies
☐ Project type (CLI, API, library)
```

> 📝 **Standard Context**: See [_common-sections.md](_common-sections.md) for full input checklist and severity levels.

---

## Copy-Paste Project Setup Prompts

### Prompt: Create New Project
```text
Set up a new Python project:

Name: {{PROJECT_NAME}}
Type: {{TYPE}} (CLI/API/Library)
Python: 3.11+

Generate:
1. pyproject.toml with uv/hatch
2. src/{{package}}/ layout
3. tests/ structure with pytest
4. .gitignore for Python
5. README.md template
6. Basic GitHub Actions CI

Use modern tools: Ruff, pytest, mypy.
```

### Prompt: Audit Project Structure
```text
Audit this project structure:

{{STRUCTURE}}

Check for:
1. Modern packaging (pyproject.toml vs setup.py)
2. src/ layout vs flat layout
3. Test organization
4. Missing standard files (LICENSE, README, .gitignore)
5. Outdated tooling

Provide specific recommendations.
```

### Prompt: Add CI/CD
```text
Add GitHub Actions CI to this project:

{{PYPROJECT_TOML}}

Create workflow that:
1. Tests on Python 3.11, 3.12, 3.13
2. Runs Ruff linting
3. Runs mypy type checking
4. Runs pytest with coverage
5. Publishes to PyPI on release (optional)

Use uv for fast dependency installation.
```

### Prompt: Modernize Legacy Project
```text
Modernize this legacy Python project:

Current structure:
{{STRUCTURE}}

Current setup.py:
{{SETUP_PY}}

Migrate to:
1. pyproject.toml with modern build backend
2. src/ layout
3. Ruff (replace flake8/isort/black)
4. Modern pytest configuration
5. GitHub Actions CI

Provide migration steps and new files.
```

### Prompt: Add Pre-commit Hooks
```text
Add pre-commit hooks to this project:

{{PYPROJECT_TOML}}

Configure hooks for:
1. Ruff (linting + formatting)
2. mypy type checking
3. pytest (optional, fast tests only)
4. Conventional commit messages
5. Secrets detection

Generate .pre-commit-config.yaml.
```

---

## Project Setup Framework

### 1. **Python Foundation Structure**
- **Package Organization**: src/ layout with __init__.py files
- **Virtual Environment**: uv or venv for dependency isolation
- **Dependencies**: pyproject.toml with dependency groups
- **Python Versions**: Support for 3.11+ with CI matrix testing

### 2. **Code Quality Tools**
- **Ruff**: All-in-one linting and formatting (replaces flake8, isort, black)
- **Type Checking**: mypy or pyright for catching type-related bugs
- **Testing**: pytest for simple, effective testing

### 3. **Development Tools**
- **Pre-commit**: Code quality checks before commits
- **Virtual Environment**: Keep dependencies isolated
- **CI/CD**: GitHub Actions for automated testing

### 4. **Framework Integration**
- **Web Frameworks**: FastAPI, Django, or Flask specific configurations
- **Data Science**: Jupyter notebooks, data directories, and analysis workflows
- **CLI Applications**: Typer or Click command-line interface setup
- **Package Distribution**: PyPI publishing and versioning strategies

## Negative Constraints
**Do NOT:**
- Mix different dependency management systems (choose one: pip, Poetry, or pipenv)
- Include unnecessary framework dependencies for simple projects
- Set overly strict linting rules that impede development velocity
- Create complex directory structures for small libraries or scripts

## Python Project Analysis Report

Please provide the following information about your Python project:

```
# Python Repository Setup Requirements
Project Name: [Enter project name]
Project Type: [web app, CLI tool, library, data science, API, etc.]
Python Version: [3.8+, 3.9+, 3.10+, etc.]
Framework: [Django, Flask, FastAPI, none, etc.]
Team Size: [number of developers]
Deployment Target: [Docker, cloud, PyPI, none]
```

## Python Repository Assessment & Setup Plan

Based on your project requirements, I'll analyze and create:

### Essential Python Structure
```
python-project/
 README.md # Project overview with installation instructions
 pyproject.toml # Modern Python project configuration (Poetry/PEP 621)
 requirements.txt # or Pipfile/poetry.lock
 .python-version # Python version specification (pyenv)
 .gitignore # Python-specific exclusions
 .github/
 workflows/
 python-app.yml # GitHub Actions CI/CD
 src/
 your_package/
 __init__.py
 main.py
 modules/
 tests/
 __init__.py
 conftest.py # pytest configuration
 test_*.py
 docs/
 conf.py # Sphinx configuration
 index.rst
 scripts/
 setup_dev.py # Development setup script
```

### Python Configuration Files
- **.pre-commit-config.yaml**: Code quality automation
- **tox.ini**: Multi-environment testing
- **setup.cfg**: Tool configurations (flake8, mypy, etc.)
- **.coveragerc**: Code coverage configuration
- **Dockerfile**: Containerization (if applicable)

## Implementation Tasks

1. Set up Python package structure with proper __init__.py files
2. Configure dependency management (Poetry/pip/pipenv)
3. Set up code quality tools (Black, isort, flake8/ruff, mypy)
4. Configure pytest with fixtures and coverage reporting
5. Set up pre-commit hooks for automated code quality
6. Create CI/CD pipeline with Python-specific testing

## Python Setup Quality Metrics

### Standards Compliance Framework
- **PEP Compliance**: PEP 8 style, PEP 517/518 build system, PEP 621 metadata
- **Code Quality**: Black formatting, isort imports, type hints coverage >80%
- **Testing Infrastructure**: pytest with >85% coverage, parametrized tests
- **Documentation**: Sphinx docs with Google/NumPy docstring style

### Success Metrics
- **Developer Setup**: `git clone && make install` gets developers running in <5 minutes
- **Code Quality**: 100% Black/isort compliance, mypy type checking passes
- **Test Reliability**: All tests pass across Python 3.8+ versions
- **CI/CD Speed**: Full test suite completes in <10 minutes

## Python Context Intelligence

**Python Project Detection:**
- **Framework Requirements**: Django (models, migrations), Flask (blueprints), FastAPI (routers)
- **Package Type**: Library (setup.py, __init__.py), Application (entry points), CLI (click)
- **Data Science**: Jupyter notebooks, data/, requirements for pandas/numpy/scipy
- **Async Support**: asyncio patterns, async testing with pytest-asyncio
- **Database Integration**: SQLAlchemy, Django ORM, or database-specific drivers

**Python Environment Setup:**
- **Virtual Environment**: Poetry for dependency management and packaging
- **Development Tools**: Black, isort, mypy, flake8/ruff, pytest
- **Pre-commit Hooks**: Automated linting and formatting
- **Type Checking**: mypy configuration with strict mode options

## Interactive Python Setup Protocol

After analyzing your Python project requirements, I'll provide:

1. ** Python Structure**: Package organization with __init__.py files
2. ** Dependency Management**: Poetry/pip setup with dev dependencies
3. ** Development Tools**: Linting, formatting, and type checking configuration
4. ** Testing Setup**: pytest configuration with fixtures and coverage
5. ** Automation**: Pre-commit hooks and CI/CD workflows

**Follow-up Question:**
> *"Would you like me to help you set up the basic Python package structure first, or would you prefer to focus on configuring the development tools like Black, mypy, and pytest?"*

Ready to create a professional Python project with modern tooling and best practices?

## Tooling & Automation

Use [_common-sections.md](_common-sections.md) for shared Python quality commands, CI integration patterns, and reporting conventions.

## Metrics & Validation

Use [_common-sections.md](_common-sections.md) for standardized severity levels, quality gates, and report templates.

## Follow-Up & Continuous Improvement

Use [_common-sections.md](_common-sections.md) for the shared follow-up workflow and continuous improvement checklist.
