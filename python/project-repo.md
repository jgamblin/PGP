# Python Project Setup Assistant

> **Purpose**: Create well-organized Python projects  
> **Best For**: Copilot, ChatGPT, Claude, Agents  
> **Python Version**: 3.11+  
> **Last Updated**: 2025-12-09

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

Recommended tools and commands for Python development:

### Analysis & Quality Tools
```bash
# Python code quality
ruff check .
black --check .
mypy .

# Testing
pytest --cov=. --cov-report=term-missing

# Security
bandit -r .
pip-audit
```

### Git Analysis
```bash
# Review changes
git diff main...HEAD --stat
git log --oneline -10

# Identify changed files
git diff main...HEAD --name-only
```

### CI/CD Integration
Recommend adding these to your development workflow:
```bash
# Pre-commit hooks
pre-commit run ruff --all-files
pre-commit run black --all-files
pre-commit run mypy --all-files
```

### Pre-commit Hooks (Recommended)
```bash
# Install pre-commit framework
pip install pre-commit  # or brew install pre-commit

# Set up hooks
pre-commit install
pre-commit run --all-files
```


## Metrics & Validation

Define clear success criteria for outcomes:

### Quality Guidelines
- **Security**: Zero critical vulnerabilities, zero hardcoded secrets
- **Code Quality**: Ruff and Black passes with minimal warnings
- **Complexity**: Cyclomatic complexity <10 per function/method
- **Duplication**: No code blocks duplicated more than twice
- **Documentation**: Public APIs and complex logic documented

### Testing Thresholds
- **Critical paths**: 80% test coverage
- **All tests pass**: No failing tests without corresponding code changes
- **Test quality**: Tests verify behavior, not implementation details
- **Edge cases**: Error conditions and boundary cases tested

### Performance Benchmarks (if applicable)
- **No regressions**: Performance metrics maintained or improved
- **Response times**: Within acceptable thresholds for user-facing operations
- **Resource usage**: Memory and CPU usage within reasonable bounds
- **Scalability**: System handles expected load

### Operational Readiness
- **Documentation**: README, API docs, and runbooks up-to-date
- **Monitoring**: Key metrics and errors are observable
- **Deployment**: Automated deployment process works reliably



## Follow-Up & Continuous Improvement

### Feedback Loop
After implementing changes:

1. **Verify improvements**
   - Run all tests to ensure nothing broke
   - Check that metrics improved (quality scores, performance)
   - Gather feedback from team members or users
   - Validate that issues are actually resolved

2. **Monitor impact**
   - Track if bugs decreased in modified areas
   - Measure if development velocity improved
   - Note if system reliability increased
   - Observe user satisfaction changes

3. **Document learnings**
   - Update team standards based on findings
   - Create architecture decision records (ADRs) for significant changes
   - Share successful patterns and approaches
   - Update documentation with new practices

### When to Get Team Input
When to discuss with your teammates:
- **Breaking changes needed**: Discuss with the team before making major changes
- **Performance degradation**: Roll back and investigate if metrics worsen significantly
- **Test coverage drops**: Pause changes to add tests first
- **Security concerns**: Pair with a teammate on authentication, authorization, or data handling code
- **Team confusion**: Provide additional documentation, pairing, or training

### Continuous Improvement
- Schedule regular reviews (weekly/monthly/quarterly based on project activity)
- Gradually increase quality standards as codebase improves
- Celebrate wins and improvements with the team
- Keep improvements incremental and sustainable
- Build a culture of quality and continuous learning

### Process Optimization
Based on findings, consider updating:
- **Coding standards**: Add patterns that prevent common issues
- **Review checklists**: Include checks for identified problem areas
- **CI/CD pipelines**: Add automated checks for recurring issues
- **Documentation templates**: Standardize important documentation
- **Team practices**: Share knowledge and establish better workflows
