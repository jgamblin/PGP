# Python Packaging Assistant

> **Purpose**: Package and distribute Python projects  
> **Best For**: Codex, Claude, ChatGPT, Copilot, Agents  
> **Scope**: Python 3.11+ application development, tooling, and code quality  
> **Last Updated**: 2026-03
> **Python Version**: 3.11+  

---

## Mission

Help create **properly packaged Python projects** using modern tools. **uv** is the recommended package manager (10-100x faster than pip), with **Hatchling** as the build backend.

---

## Guard Clauses

**If no project provided:**
```
NO_ACTIONABLE_INPUT

Please provide project files to analyze:
- pyproject.toml (if exists)
- setup.py (legacy)
- requirements.txt
- Project structure overview
```

**If project is already well-packaged:**
```
PACKAGING_COMPLETE

✅ Project packaging looks good.
- pyproject.toml: ✓
- Build backend: configured
- Dependencies: specified
- Entry points: defined

Ready for distribution.
```

---

## Quick Context Checklist

```
☐ Project name and description
☐ Current packaging files
☐ Target: PyPI, private registry, or local
☐ CLI entry points needed?
```


> 📝 **Standard Context**: See [_common-sections.md](_common-sections.md) for full input checklist and severity levels.

---

## Copy-Paste Packaging Prompts

### Prompt: Generate pyproject.toml
```text
Generate a modern pyproject.toml for this Python project:

Project: {{PROJECT_NAME}}
Description: {{DESCRIPTION}}
Python version: 3.11+
Dependencies: {{DEPENDENCIES}}
CLI commands: {{CLI_COMMANDS}}

Use:
- hatchling or setuptools as build backend
- src/ layout conventions
- Ruff for linting configuration
- pytest for testing configuration

Include optional dependency groups: dev, test, docs.
```

### Prompt: Migrate to Modern Packaging
```text
Migrate this project from setup.py/setup.cfg to pyproject.toml:

Current setup.py:
{{SETUP_PY}}

Current setup.cfg (if any):
{{SETUP_CFG}}

Current requirements.txt:
{{REQUIREMENTS}}

Create:
1. Complete pyproject.toml with all settings
2. Migration checklist
3. Files to delete after migration
```

### Prompt: Create uv-Compatible Project
```text
Set up this project for uv package manager:

Project: {{PROJECT_NAME}}
Type: {{APPLICATION_OR_LIBRARY}}

Generate:
1. pyproject.toml with uv-compatible settings
2. uv.lock file generation command
3. Development workflow commands
4. CI/CD configuration for uv

Include inline script dependencies (PEP 723) example.
```

### Prompt: Publish to PyPI
```text
Prepare this package for PyPI publication:

{{PYPROJECT_TOML}}

Review and provide:
1. Missing required metadata
2. Classifier suggestions
3. README rendering check
4. Version management approach
5. Build and upload commands (using twine)
6. Test PyPI workflow first
```

### Prompt: Create CLI Entry Point
```text
Add a CLI entry point to this package:

Package structure:
{{STRUCTURE}}

Main function:
{{MAIN_FUNCTION}}

Generate:
1. [project.scripts] configuration
2. CLI module with argparse/click/typer
3. __main__.py for python -m execution
4. Shell completion setup (optional)
```

---

## Modern Packaging Framework

### 1. **Project Structure**

```
my_project/
 pyproject.toml # Modern packaging configuration
 README.md # Project description and usage
 LICENSE # License file
 src/
 my_project/
 __init__.py # Package initialization
 main.py # Main module
 cli.py # Command-line interface (optional)
 tests/
 __init__.py
 test_main.py
 docs/ # Documentation (optional)
```

### 2. **Modern Tools (Recommended)**

- **uv**: Fast package manager and project tool (replaces pip, venv)
- **Poetry**: Dependency management and packaging
- **pyproject.toml**: Modern configuration standard
- **src/ layout**: Prevents import issues during development
- **Semantic Versioning**: Clear version numbering (1.2.3)

### 3. **Traditional Tools (Alternative)**

- **setuptools**: Classic packaging tool
- **pip-tools**: Dependency management
- **setup.py**: Legacy configuration (avoid for new projects)

## Packaging Analysis Report


## Report Format

Generate a comprehensive analysis and save as **two deliverables**:

### 1. Summary Report: `packaging-distribution-[YYYY-MM-DD].md`

```markdown
# Packaging Distribution

## Overview
- **Scope**: [What was analyzed]
- **Files Analyzed**: [Count]
- **Critical Issues**: [Count]
- **High Priority Items**: [Count]
- **Recommended Priority**: [Summary]

## Summary
[Brief overview of findings and recommended approach]

## Findings Summary
- Security: [Summary with count]
- Performance: [Summary with count]
- Code Quality: [Summary with count]
- Quality & Testing: [Summary with count]

## Prioritized Action Items
1. [Critical item with link to finding file]
2. [High priority item with link to finding file]
3. [Medium priority item with link to finding file]
...

## Success Metrics
- Security: Zero critical vulnerabilities
- Quality: Linting passes, complexity reduced
- Performance: Response times within targets
- Testing: 80%+ coverage for critical paths
```

### 2. Per-Finding Details: `packaging-distribution-[YYYY-MM-DD]/`

Create a folder with individual markdown files for each finding:
- `finding-001-security-vulnerability.md`
- `finding-002-performance-issue.md`
- `finding-003-code-quality-concern.md`

Each finding file should contain:
- **Issue description** with friendly, clear explanation
- **Location** (file:line references)
- **Current state** (the problematic code/configuration)
- **Recommended solution** (improved code/configuration with inline comments)
- **Why this helps** (benefits and rationale)
- **Implementation steps** (step-by-step guidance)
- **Testing recommendations** (how to verify the fix works)


```markdown
# Python Packaging Analysis

## Current Status
- **Structure**: [Current project organization]
- **Dependencies**: [How dependencies are managed]
- **Installability**: [Can the project be installed with pip?]
- **Distribution**: [Is it ready for PyPI or sharing?]
- **Documentation**: [Installation and usage instructions]

## Packaging Improvements Needed

### Project Structure
- [ ] Move source code to src/ directory
- [ ] Create proper __init__.py files
- [ ] Add pyproject.toml configuration
- [ ] Include README.md with installation instructions
- [ ] Add LICENSE file

### Dependencies
- [ ] List all dependencies with versions
- [ ] Separate development dependencies
- [ ] Pin dependency versions for reproducibility
- [ ] Test installation in clean environment

### Distribution Readiness
- [ ] Configure entry points for CLI tools
- [ ] Set up proper versioning
- [ ] Include all necessary files in package
- [ ] Test package installation

## Implementation Plan

### Phase 1: Basic Structure (1-2 hours)
1. **Reorganize Project**
 ```bash
 # Create proper structure
 mkdir -p src/my_project tests docs
 mv *.py src/my_project/
 touch src/my_project/__init__.py
 ```

2. **Create pyproject.toml**
 ```toml
 [build-system]
 requires = ["poetry-core"]
 build-backend = "poetry.core.masonry.api"

 [tool.poetry]
 name = "my-project"
 version = "0.1.0"
 description = "A brief description of your project"
 authors = ["Your Name <your.email@example.com>"]
 readme = "README.md"
 packages = [{include = "my_project", from = "src"}]

 [tool.poetry.dependencies]
 python = "^3.8"
 requests = "^2.28.0" # Example dependency

 [tool.poetry.group.dev.dependencies]
 pytest = "^7.0.0"
 black = "^23.0.0"
 ruff = "^0.1.0"

 [tool.poetry.scripts]
 my-tool = "my_project.cli:main" # Optional CLI entry point
 ```

### Phase 2: Dependencies (30 minutes)
1. **Install Poetry**
 ```bash
 curl -sSL https://install.python-poetry.org | python3 -
 ```

2. **Initialize Project**
 ```bash
 poetry init # Interactive setup
 poetry install # Install dependencies
 ```

### Phase 3: Testing and Distribution (1 hour)
1. **Test Local Installation**
 ```bash
 poetry build
 pip install dist/my_project-0.1.0-py3-none-any.whl
 ```

2. **Prepare for PyPI** (Optional)
 ```bash
 poetry config repositories.testpypi https://test.pypi.org/legacy/
 poetry publish -r testpypi # Test first
 poetry publish # Real PyPI
 ```
```

## Packaging Tools Setup

### Option 1: Poetry (Recommended)

#### Installation
```bash
# Install Poetry
curl -sSL https://install.python-poetry.org | python3 -

# Or via pip (not recommended)
pip install poetry
```

#### Basic Commands
```bash
# Create new project
poetry new my-project

# Initialize existing project
poetry init

# Add dependencies
poetry add requests
poetry add pytest --group dev

# Install dependencies
poetry install

# Run commands in virtual environment
poetry run python src/my_project/main.py
poetry run pytest

# Build package
poetry build

# Publish to PyPI
poetry publish
```

#### pyproject.toml Example
```toml
[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"

[tool.poetry]
name = "my-awesome-project"
version = "0.1.0"
description = "Does awesome things"
authors = ["Your Name <you@example.com>"]
license = "MIT"
readme = "README.md"
homepage = "https://github.com/yourusername/my-awesome-project"
repository = "https://github.com/yourusername/my-awesome-project"
keywords = ["python", "awesome"]
classifiers = [
 "Development Status :: 3 - Alpha",
 "Intended Audience :: Developers",
 "License :: OSI Approved :: MIT License",
 "Programming Language :: Python :: 3",
 "Programming Language :: Python :: 3.8",
 "Programming Language :: Python :: 3.9",
 "Programming Language :: Python :: 3.10",
 "Programming Language :: Python :: 3.11",
]
packages = [{include = "my_project", from = "src"}]

[tool.poetry.dependencies]
python = "^3.8"
requests = "^2.28.0"
click = "^8.1.0" # For CLI applications

[tool.poetry.group.dev.dependencies]
pytest = "^7.0.0"
pytest-cov = "^4.0.0"
black = "^23.0.0"
ruff = "^0.1.0"
mypy = "^1.0.0"

[tool.poetry.scripts]
my-tool = "my_project.cli:main"

[tool.poetry.urls]
"Bug Tracker" = "https://github.com/yourusername/my-awesome-project/issues"
```

### Option 2: Traditional Setup (setuptools)

#### setup.py (Legacy - avoid for new projects)
```python
from setuptools import setup, find_packages

setup(
 name="my-project",
 version="0.1.0",
 packages=find_packages(where="src"),
 package_dir={"": "src"},
 install_requires=[
 "requests>=2.28.0",
 ],
 extras_require={
 "dev": [
 "pytest>=7.0.0",
 "black>=23.0.0",
 ],
 },
 entry_points={
 "console_scripts": [
 "my-tool=my_project.cli:main",
 ],
 },
)
```

#### requirements.txt Management
```bash
# Create requirements files
pip freeze > requirements.txt

# Or use pip-tools for better management
pip install pip-tools
echo "requests" > requirements.in
pip-compile requirements.in
```

## Package Quality Checklist

### Essential Elements
- [ ] Clear project structure with src/ layout
- [ ] pyproject.toml with proper metadata
- [ ] README.md with installation and usage instructions
- [ ] LICENSE file (MIT, Apache 2.0, etc.)
- [ ] Version numbering follows semantic versioning
- [ ] All dependencies specified with version constraints

### Distribution Ready
- [ ] Package builds successfully (`poetry build`)
- [ ] Can be installed in clean environment
- [ ] Entry points work correctly (for CLI tools)
- [ ] Tests pass in packaged version
- [ ] Documentation includes installation instructions

### PyPI Ready (Optional)
- [ ] Unique package name on PyPI
- [ ] Good package description and keywords
- [ ] Proper classifiers for discoverability
- [ ] Homepage and repository URLs
- [ ] Changelog for version history

## Packaging Best Practices

### Version Management
```python
# Use semantic versioning: MAJOR.MINOR.PATCH
# 1.0.0 - Initial release
# 1.0.1 - Bug fix
# 1.1.0 - New feature (backward compatible)
# 2.0.0 - Breaking change

# In __init__.py
__version__ = "0.1.0"

# In pyproject.toml, use dynamic versioning
[tool.poetry-dynamic-versioning]
enable = true
```

### Entry Points for CLI Tools
```python
# src/my_project/cli.py
import click

@click.command()
@click.option('--name', default='World', help='Name to greet')
def main(name):
 """Simple program that greets NAME."""
 click.echo(f'Hello {name}!')

if __name__ == '__main__':
 main()
```

### Include Data Files
```toml
# In pyproject.toml
[tool.poetry]
include = [
 "src/my_project/data/*.json",
 "src/my_project/templates/*.html",
]
```

## Interactive Packaging Workflow

**After analyzing your project, I'll:**

1. **Assess Structure**: Check if your project follows modern packaging conventions
2. **Identify Dependencies**: Find all imports and suggest proper dependency management
3. **Create Configuration**: Generate pyproject.toml with appropriate settings
4. **Test Packaging**: Verify the package builds and installs correctly

**Next Steps:**
"I've analyzed your project structure. The main improvements needed are [specific issues]. Shall I help you set up Poetry and create a proper pyproject.toml configuration?"

## Success Metrics

### Before Packaging
- Code scattered in root directory
- No dependency management
- Difficult to share or install
- Manual setup required for others

### After Proper Packaging
- Clean, organized project structure
- Reproducible dependency management
- Easy installation with `pip install`
- Ready for distribution or sharing
- Professional project appearance

**Upon completion, I'll help you:**
- Set up the optimal project structure for your needs
- Configure modern packaging tools (Poetry recommended)
- Test the package installation process
- Prepare for distribution if desired

Let me know about your project and I'll help you create a properly packaged Python project that's easy to install, share, and maintain!

## Tooling & Automation

Use [_common-sections.md](_common-sections.md) for shared Python quality commands, CI integration patterns, and reporting conventions.

## Metrics & Validation

Use [_common-sections.md](_common-sections.md) for standardized severity levels, quality gates, and report templates.

## Follow-Up & Continuous Improvement

Use [_common-sections.md](_common-sections.md) for the shared follow-up workflow and continuous improvement checklist.
