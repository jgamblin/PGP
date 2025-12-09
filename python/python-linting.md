# Python Code Style Assistant

> **Purpose**: Code formatting, linting, and style enforcement  
> **Best For**: Copilot, ChatGPT, Claude, Agents  
> **Python Version**: 3.11+  
> **Last Updated**: 2025-12-09

---

## Mission

Help write **clean, readable Python code** using modern tools. Ruff replaces Flake8, isort, Black, and more in a single fast tool.

---

## Guard Clauses

**If no code provided:**
```
NO_ACTIONABLE_INPUT

Please provide Python code to analyze for style issues.
```

**If code passes all checks:**
```
NO_STYLE_ISSUES

✅ Code passes all style checks.
- Formatting: ✓
- Imports: ✓
- Linting: ✓

No changes needed.
```

---

## Quick Context Checklist

```
☐ Code to check
☐ Python version (3.11+ recommended)
☐ Existing style config (pyproject.toml, ruff.toml)
```


> 📝 **Standard Context**: See [_common-sections.md](_common-sections.md) for full input checklist and severity levels.

---

## Copy-Paste Linting Prompts

### Prompt: Configure Ruff
```text
Configure Ruff for this project:

{{PYPROJECT_TOML}}

Set up:
1. Line length: 88 (Black-compatible)
2. Target Python: 3.11+
3. Enable recommended rules (E, F, I, UP, B, SIM)
4. Configure per-file ignores for tests
5. isort-compatible import sorting

Add to pyproject.toml [tool.ruff] section.
```

### Prompt: Fix Linting Errors
```text
Fix these Ruff/linting errors:

Errors:
{{ERRORS}}

Code:
{{CODE}}

For each error:
1. Explain what's wrong
2. Show the fix
3. Note if it's auto-fixable

Apply fixes and show corrected code.
```

### Prompt: Migrate to Ruff
```text
Migrate this project from legacy tools to Ruff:

Current config:
{{CONFIG}}

Tools to replace:
- flake8 → Ruff linter
- isort → Ruff isort rules
- black → Ruff formatter
- pyupgrade → Ruff UP rules
- autoflake → Ruff F rules

Generate new pyproject.toml sections and files to delete.
```

### Prompt: Add Type Checking
```text
Add mypy configuration to this project:

{{PYPROJECT_TOML}}

Configure:
1. Strict mode settings
2. Per-module overrides for gradual adoption
3. Ignore patterns for tests/migrations
4. Integration with pre-commit

Add to pyproject.toml [tool.mypy] section.
```

### Prompt: Review Code Style
```text
Review this code for style issues:

{{CODE}}

Check against:
- PEP 8 guidelines
- Modern Python idioms (3.11+)
- Type hint completeness
- Docstring presence
- Import organization

Provide specific fixes, not just rule names.
```

---

## Modern Code Style Framework

### 1. **Ruff - The Modern All-in-One Tool (Recommended)**

- **Speed**: 10-100x faster than Flake8, isort, and other tools combined
- **Comprehensive**: Replaces Flake8, isort, pydocstyle, pyupgrade, and more
- **Easy Setup**: Single tool configuration in pyproject.toml
- **Auto-fix**: Automatically fixes many issues (like isort + autoflake)
- **Compatible**: Drop-in replacement for existing Flake8 workflows

### 2. **Ruff Formatter (Replaces Black)**

- **Black-compatible**: Same output as Black
- **Integrated**: Part of the Ruff tool
- **Fast**: Formats code automatically without separate tool

### 3. **Traditional Tools (Legacy - Avoid)**

- **Flake8**: Style checking (replaced by Ruff)
- **isort**: Import sorting (replaced by Ruff)
- **Black**: Formatting (replaced by Ruff formatter)
- **pyupgrade**: Syntax modernization (replaced by Ruff)
- **autoflake**: Remove unused imports (replaced by Ruff)

### 4. **Code Quality Principles**

- **Readability First**: Style should improve code understanding
- **Consistency**: Same patterns throughout the project
- **Automation**: Let tools handle formatting, focus on logic
- **Modern Python**: Use current Python features and syntax
- **Team Friendly**: Easy for others to read and contribute

## What to Avoid

**Don't be overly strict about:**

- Minor whitespace issues that don't affect readability
- Very long lines that are clear and readable
- Import order when it doesn't impact functionality
- Docstring formatting for simple, obvious functions

## Code Style Review

Provide a **practical code style review** focusing on readability and consistency:

# Python Code Style Review

## Style Assessment

- **Overall Consistency**: [Good/Needs work/Mixed]
- **Readability**: [Clear/Confusing/Needs improvement]
- **Tool Compatibility**: [Black/Flake8 compatible or issues found]
- **Import Organization**: [Well organized/Needs sorting/Mixed]

## Good Style Practices Found

- **Consistent Naming**: [Good variable and function names]
- **Clear Structure**: [Well-organized code blocks]
- **Readable Formatting**: [Good use of whitespace and line breaks]

## Style Improvements

### Issue: [Brief description]

- **File**: `filename.py:line X`
- **Current**: [What needs fixing]
- **Better**: [Improved version]
- **Why**: [Brief explanation of benefit]

**Example:**
```python
# Current style
def calculate_total(items,tax_rate,discount=0):
 result=sum([item['price']for item in items])
 return result*(1+tax_rate)*(1-discount)

# Improved style
def calculate_total(items, tax_rate, discount=0):
 """Calculate total price with tax and discount applied."""
 subtotal = sum(item['price'] for item in items)
 return subtotal * (1 + tax_rate) * (1 - discount)
```

## Modern Tools Setup

### Option 1: Ruff + Black (Recommended)

#### Ruff Configuration (pyproject.toml)
```toml
[tool.ruff]
# Enable pycodestyle (`E`) and Pyflakes (`F`) codes by default.
select = ["E", "F", "I", "N", "UP", "YTT", "S", "BLE", "B", "A", "COM", "C4", "DTZ", "T10", "EM", "EXE", "ISC", "ICN", "G", "INP", "PIE", "T20", "PYI", "PT", "Q", "RSE", "RET", "SLF", "SIM", "TID", "TCH", "ARG", "PTH", "ERA", "PD", "PGH", "PL", "TRY", "NPY", "RUF"]
ignore = ["E501"] # Line too long (handled by Black)

# Same as Black.
line-length = 88

# Allow unused variables when underscore-prefixed.
dummy-variable-rgx = "^(_+|(_+[a-zA-Z0-9_]*[a-zA-Z0-9]+?))$"

# Assume Python 3.8+.
target-version = "py38"

[tool.ruff.mccabe]
# Unlike Flake8, default to a complexity level of 10.
max-complexity = 10

[tool.ruff.isort]
# Use Black-compatible import sorting
profile = "black"
```

#### Black Configuration (pyproject.toml)
```toml
[tool.black]
line-length = 88
target-version = ['py38']
include = '\.pyi?$'
```

### Option 2: Traditional Setup (Flake8 + isort)

#### Flake8 Configuration (.flake8)
```ini
[flake8]
max-line-length = 88
extend-ignore = 
 E203, # whitespace before ':'
 E501, # line too long (handled by Black)
 W503, # line break before binary operator
exclude = 
 .git,
 __pycache__,
 .venv,
 migrations/
```

#### isort Configuration (pyproject.toml)
```toml
[tool.isort]
profile = "black"
multi_line_output = 3
line_length = 88
```

## Quick Setup and Usage

### Modern Approach: Ruff + Black
```bash
# Install tools
pip install ruff black

# Format code with Black
black your_file.py

# Check and auto-fix with Ruff
ruff check your_file.py --fix

# Check without fixing
ruff check your_file.py
```

### Traditional Approach: Flake8 + isort + Black
```bash
# Install tools
pip install flake8 isort black

# Format code
black your_file.py

# Sort imports
isort your_file.py

# Check style
flake8 your_file.py
```

### Pre-commit Setup (Recommended)
```yaml
# .pre-commit-config.yaml
repos:
 - repo: https://github.com/psf/black
 rev: 23.9.1
 hooks:
 - id: black
 - repo: https://github.com/astral-sh/ruff-pre-commit
 rev: v0.1.0
 hooks:
 - id: ruff
 args: [--fix, --exit-non-zero-on-fix]
```

```bash
pip install pre-commit
pre-commit install
```

## Code Style Checklist

### Formatting (Automated by Black)
- [ ] Consistent indentation (4 spaces)
- [ ] Proper spacing around operators
- [ ] Reasonable line lengths (88 characters)
- [ ] Consistent string quote style

### Code Quality (Checked by Ruff/Flake8)
- [ ] Clear variable and function names (snake_case)
- [ ] Organized imports (standard, third-party, local)
- [ ] No unused imports or variables
- [ ] Modern Python syntax (f-strings, type hints)
- [ ] Helpful comments where needed

### Best Practices
- [ ] Functions have single responsibility
- [ ] Meaningful variable names (not `x`, `data`, `temp`)
- [ ] Type hints for function parameters and returns
- [ ] Docstrings for public functions and classes

## Style Tips

### Good Naming
```python
# Good
user_count = len(users)
is_valid = check_email(email)
process_payment(amount, card_info)

# Avoid
n = len(users)
flag = check_email(email)
do_stuff(x, y)
```

### Clear Structure
```python
# Good - clear separation
def calculate_discount(price, customer_type):
 if customer_type == 'premium':
 return price * 0.1
 elif customer_type == 'regular':
 return price * 0.05
 else:
 return 0

# Harder to read - cramped
def calculate_discount(price,customer_type):
 if customer_type=='premium':return price*0.1
 elif customer_type=='regular':return price*0.05
 else:return 0
```

### Useful Comments
```python
# Good - explains why
# Use exponential backoff to handle API rate limits
time.sleep(2 ** retry_count)

# Less helpful - explains what
# Sleep for 2 to the power of retry_count seconds
time.sleep(2 ** retry_count)
```



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

### Deployment Readiness
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
