# Python Code Refactoring Analysis

> **Purpose**: Improve code quality and structure  
> **Best For**: Copilot, ChatGPT, Claude, Agents  
> **Python Version**: 3.11+  
> **Last Updated**: 2025-12-09

---

## Mission

Analyze code to identify practical improvements using modern Pythonic patterns, type hints, and clean code principles.

---

## Guard Clauses

**If no code provided:**
```
NO_ACTIONABLE_INPUT

Please provide Python code to refactor:
- Source files or code snippets
- Specific improvement goals
- Constraints (backward compatibility, etc.)
```

**If code is already clean:**
```
NO_REFACTORING_NEEDED

✅ Code is already well-structured.
- Follows PEP 8: ✓
- Type hints present: ✓
- Functions focused: ✓
- No obvious improvements needed

Consider adding property-based tests for additional confidence.
```

---

## Quick Context Checklist

```
☐ Code to refactor
☐ Current pain points
☐ Constraints (performance, compatibility)
☐ Target patterns or style
```

> 📝 **Standard Context**: See [_common-sections.md](_common-sections.md) for full input checklist and severity levels.

---

## Copy-Paste Refactoring Prompts

### Prompt: General Code Review
```text
Review this Python code for refactoring opportunities:

{{CODE}}

Identify:
1. Code smells (duplication, long functions, deep nesting)
2. PEP 8 violations
3. Missing type hints
4. Opportunities for Python 3.11+ features
5. Performance improvements

Prioritize by impact. Show before/after for top 3 issues.
```

### Prompt: Extract Functions
```text
This function is too long. Extract smaller, focused functions:

{{CODE}}

Goals:
- Each function does one thing
- Functions are under 20 lines
- Clear, descriptive names
- Proper parameter passing (no global state)

Show the refactored code with all extracted functions.
```

### Prompt: Modernize Legacy Code
```text
Modernize this Python code for 3.11+:

{{CODE}}

Update to use:
- Type hints (PEP 484, 585, 604)
- Pattern matching (match/case) where appropriate
- Dataclasses or Pydantic models
- f-strings instead of .format()
- Walrus operator where it improves clarity
- pathlib instead of os.path

Preserve functionality. Show complete updated code.
```

### Prompt: Improve Error Handling
```text
Improve error handling in this code:

{{CODE}}

Fix:
- Bare except clauses
- Generic Exception catches
- Missing error context
- Silent failures

Add:
- Specific exception types
- Helpful error messages
- Proper logging
- Graceful degradation
```

### Prompt: Reduce Complexity
```text
Reduce cyclomatic complexity in this code:

{{CODE}}

Apply:
- Early returns (guard clauses)
- Dictionary dispatch instead of if/elif chains
- Extract conditional logic to functions
- Use itertools/comprehensions where clearer

Target: No function over complexity 10.
```

---

**Report Format:**
Generate a practical code improvement report and save it as a markdown file named `python-refactoring-analysis-[YYYY-MM-DD].md`:


## Report Format

Generate a comprehensive analysis and save as **two deliverables**:

### 1. Summary Report: `code-refactoring-[YYYY-MM-DD].md`

```markdown
# Code Refactoring

## Overview
- **Scope**: [What was analyzed]
- **Files Analyzed**: [Count]
- **Critical Issues**: [Count]
- **High Priority Items**: [Count]
- **Recommended Priority**: [Summary]

## Summary
[Brief overview of findings]

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

### 2. Per-Finding Details: `code-refactoring-[YYYY-MM-DD]/`

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
# Code Improvement Report


## Inputs Required

To provide effective guidance, please provide:

**Git Context**:
- Current branch name: `git branch --show-current`
- Changed files: `git diff main...HEAD --name-only`
- Detailed changes: `git diff main...HEAD`

**Code Artifacts**:
- Source files to review (specific files or directories)
- Existing tests (if any)
- Configuration files (linting, formatting, build tools)
- README or documentation describing the codebase

**Runtime Context**:
- Python version and environment
- Frameworks or libraries in use
- Current pain points or known issues
- Performance metrics (if available)

**Constraints**:
- Project urgency level
- Any compliance or security requirements

## Python Refactoring Focus

Before providing recommendations, I will:

1. **Analyze code/system structure** - Review organization, architecture, and patterns
2. **Identify issues** - Code smells, anti-patterns, technical debt
3. **Assess risk areas** - Security vulnerabilities, performance bottlenecks, reliability concerns
4. **Evaluate quality** - Code quality, testing, documentation status
5. **Consider context** - Project size, team experience, time constraints
6. **Rank priorities** - Critical issues first, then high-impact improvements, then nice-to-haves

**Clarifying Questions** (if needed):
- What specific areas are causing the most problems?
- What are the most critical user workflows or features?
- What's the expected lifespan and scale of this project?
- Are there any known issues or technical debt to address?

## Recommended Plan

Based on the analysis, I will provide a prioritized action plan:

1. **Address Critical Issues**
   - Fix security vulnerabilities and data safety issues
   - Resolve blocking bugs or system failures
   - **Success indicators**: Zero critical vulnerabilities, system stability restored

2. **Improve Code Quality**
   - Improve code clarity and structure
   - Enhance testing and reliability
   - **Success indicators**: Code quality scores improved, complexity reduced

3. **Enhance Quality & Maintainability**
   - Improve code clarity and organization
   - Add or improve test coverage
   - Update documentation
   - **Success indicators**: Code quality metrics improved, tests passing, docs up-to-date

4. **Optimize Performance** (if applicable)
   - Address performance bottlenecks
   - Improve resource usage
   - **Success indicators**: Performance metrics meet targets

5. **Ensure Long-term Sustainability**
   - Set up automation and tooling
   - Document architectural decisions
   - **Success indicators**: CI/CD pipeline working, team productivity improved

## Project Health Check
- **Code Quality Score**: [X/100 based on readability and structure]
- **Lines of Code**: [Total LOC count]
- **Functions/Classes**: [Breakdown by type]
- **Time to Fix**: [Estimated hours for improvements]
- **Security Notes**: [Basic security considerations]
- **Performance**: [Simple bottlenecks identified]
- **Maintainability**: [How easy is it to change?]
- **Testing Gaps**: [Areas that need tests]

## Code Improvement Assessment

### Structure & Organization
1. **Code Organization**
 - **Current Structure**: [How files and functions are organized]
 - **Coupling Issues**: [Functions/classes too tightly connected]
 - **Clarity Problems**: [Hard to understand parts]
 - **Suggested Pattern**: [Simple, clear organization]
 - **Improvement Steps**: [Easy changes to make it better]

2. **Design Principles**
 - **Single Purpose**: [Functions doing too many things]
 - **Easy to Extend**: [Hard to add new features]
 - **Clear Interfaces**: [Confusing function signatures]
 - **Dependencies**: [Too many interconnected parts]

### Code Quality Review

#### Top Priority Issues
1. **Security Concerns**
 - **Type**: [SQL Injection/XSS/Buffer Overflow]
 - **Location**: `filename.ext:line X-Y`
 - **Risk Assessment**: [CVSS score if applicable]
 - **Current Code**:
 ```python
 # Vulnerable code example
 def unsafe_query(user_input):
 query = f"SELECT * FROM users WHERE id = {user_input}"
 return db.execute(query).fetchall()
 ```
 - **Secure Implementation**:
 ```python
 # Secure refactored version
 from sqlalchemy import text

 def safe_query(user_input: int) -> List[User]:
 query = text("SELECT * FROM users WHERE id = :user_id")
 return db.execute(query, {"user_id": user_input}).fetchall()
 ```
 - **Additional Security Measures**: [Input validation, sanitization]

2. **Performance Issues**
 - **Slow Algorithms**: [Simple optimizations available]
 - **Memory Usage**: [Patterns using too much memory]
 - **Database Queries**: [N+1 problems and slow queries]
 - **Caching**: [Simple caching opportunities]

#### Quick Wins (High Impact)
1. **List Comprehensions and Generator Expressions**
 - **Current Issue**: Explicit loops for simple transformations
 - **Simple Fix**: Use list comprehensions or generator expressions
 - **Example**:
 ```python
 # Before: Explicit loop
 results = []
 for item in items:
 if item.is_active:
 results.append(item.name.upper())

 # After: List comprehension
 results = [item.name.upper() for item in items if item.is_active]

 # For large datasets: Generator expression
 results = (item.name.upper() for item in items if item.is_active)
 ```
 - **Benefits**: More readable, often faster, more Pythonic

2. **Dataclasses Instead of Simple Classes**
 - **Current Issue**: Boilerplate code for simple data containers
 - **Simple Fix**: Replace with dataclasses or NamedTuples
 - **Example**:
 ```python
 # Before: Manual class with boilerplate
 class User:
 def __init__(self, name, email, age):
 self.name = name
 self.email = email
 self.age = age

 def __repr__(self):
 return f"User(name='{self.name}', email='{self.email}', age={self.age})"

 # After: Dataclass
 from dataclasses import dataclass

 @dataclass
 class User:
 name: str
 email: str
 age: int
 ```
 - **Benefits**: Less code, automatic __repr__, type hints, equality methods

3. **Context Managers for Resource Handling**
 - **Current Issue**: Manual resource management and cleanup
 - **Simple Fix**: Use `with` statements and context managers
 - **Example**:
 ```python
 # Before: Manual file handling
 file = open('data.txt', 'r')
 try:
 content = file.read()
 process_content(content)
 finally:
 file.close()

 # After: Context manager
 with open('data.txt', 'r') as file:
 content = file.read()
 process_content(content)

 # Custom context manager for database connections
 from contextlib import contextmanager

 @contextmanager
 def database_transaction():
 conn = get_connection()
 trans = conn.begin()
 try:
 yield conn
 trans.commit()
 except Exception:
 trans.rollback()
 raise
 finally:
 conn.close()
 ```
 - **Benefits**: Guaranteed cleanup, exception safety, cleaner code

4. **Modern Python Features**
 - **f-strings**: Replace `.format()` and `%` formatting
 - **Type hints**: Add basic type annotations
 - **Pathlib**: Replace `os.path` operations
 - **Example**:
 ```python
 # Before: Old string formatting
 message = "Hello {}, you have {} messages".format(user.name, count)

 # After: f-strings
 message = f"Hello {user.name}, you have {count} messages"

 # Before: os.path
 import os
 file_path = os.path.join(base_dir, 'data', 'file.txt')

 # After: pathlib
 from pathlib import Path
 file_path = Path(base_dir) / 'data' / 'file.txt'
 ```

### Testing & Quality

#### Test Coverage Check
- **Unit Tests**: [Current coverage and missing areas]
- **Integration Tests**: [API and database testing needs]
- **Key Scenarios**: [Important user flows to test]
- **Performance Tests**: [Basic load testing if needed]

#### Python-Specific Testability Improvements
```python
# Before: Hard to test - tightly coupled
class OrderService:
 def process_order(self, order):
 # Direct database calls, external APIs
 result = Database.save(order)
 EmailService.send(order.customer_email)
 PaymentGateway.charge(order.total)
 return result

# After: Dependency injection with protocols
from typing import Protocol
from dataclasses import dataclass
from abc import ABC, abstractmethod

class DatabaseProtocol(Protocol):
 def save(self, order: Order) -> OrderResult: ...

class EmailServiceProtocol(Protocol):
 async def send(self, email: str) -> None: ...

class PaymentProtocol(Protocol):
 def charge(self, amount: float) -> PaymentResult: ...

@dataclass
class OrderService:
 database: DatabaseProtocol
 email_service: EmailServiceProtocol
 payment_service: PaymentProtocol

 async def process_order(self, order: Order) -> OrderResult:
 # Easy to test with mocks
 result = await self.database.save(order)
 await self.email_service.send(order.customer_email)
 payment_result = self.payment_service.charge(order.total)
 return OrderResult(result, payment_result)

# Test example
import pytest
from unittest.mock import Mock, AsyncMock

@pytest.mark.asyncio
async def test_process_order():
 # Arrange
 mock_db = Mock()
 mock_email = AsyncMock()
 mock_payment = Mock()

 service = OrderService(mock_db, mock_email, mock_payment)
 order = Order(customer_email="test@example.com", total=100.0)

 # Act
 result = await service.process_order(order)

 # Assert
 mock_db.save.assert_called_once_with(order)
 mock_email.send.assert_called_once_with("test@example.com")
 mock_payment.charge.assert_called_once_with(100.0)
```

#### Python Testing Patterns
```python
# Use pytest fixtures for common test data
@pytest.fixture
def sample_user():
 return User(name="John Doe", email="john@example.com", age=30)

# Use parametrize for multiple test cases
@pytest.mark.parametrize("input_value,expected", [
 ("hello", "HELLO"),
 ("world", "WORLD"),
 ("", ""),
])
def test_uppercase(input_value, expected):
 assert uppercase(input_value) == expected

# Use context managers for testing exceptions
def test_invalid_email():
 with pytest.raises(ValidationError, match="Invalid email format"):
 validate_email("invalid-email")
```

### Performance Optimization Strategy

#### Computational Efficiency
- **Current Bottlenecks**: [Profiling results]
- **Algorithm Improvements**: [Specific optimizations]
- **Data Structure Optimization**: [HashMap vs Array usage]
- **Lazy Loading Opportunities**: [Deferred computation]

#### Memory Management
- **Memory Footprint**: [Current vs. optimized]
- **Garbage Collection Impact**: [Allocation patterns]
- **Memory Leaks**: [Event listeners, closures]
- **Object Pooling**: [Reusable object strategies]

### Security Hardening Plan

#### Input Validation & Sanitization
- **Injection Vulnerabilities**: [SQL, NoSQL, Command]
- **Cross-Site Scripting (XSS)**: [Stored, reflected, DOM-based]
- **Authentication Weaknesses**: [Password policies, MFA]
- **Authorization Flaws**: [RBAC, ABAC implementation]

#### Secure Coding Practices
- **Error Handling**: [Information disclosure prevention]
- **Logging Security**: [Sensitive data in logs]
- **Cryptography**: [Encryption at rest and in transit]
- **Dependency Vulnerabilities**: [Outdated packages]

## Action Plan

### Fix First (High Priority)
1. [ ] **Security Issues**
 - Add input validation
 - Fix SQL injection risks
 - Update vulnerable packages
 - **Why**: Prevent security problems
 - **Time**: 4-8 hours

2. [ ] **Performance Problems**
 - Fix slow database queries
 - Optimize memory usage
 - Add simple caching
 - **Why**: Make the app faster
 - **Time**: 6-12 hours

3. [ ] **Code Organization**
 - Break up large functions
 - Separate concerns better
 - Clean up messy parts
 - **Why**: Easier to understand and change
 - **Time**: 8-16 hours

4. [ ] **Code Quality**
 - Fix obvious code smells
 - Add type hints
 - Improve naming
 - **Why**: Cleaner, more maintainable code
 - **Time**: 6-12 hours

5. [ ] **Modern Python Patterns**
 - Replace loops with comprehensions where appropriate
 - Use dataclasses for simple data containers
 - Implement context managers for resource handling
 - Add f-strings, type hints, and pathlib
 - Consider async/await for I/O operations
 - **Why**: More Pythonic, readable, and maintainable code
 - **Time**: 4-8 hours

6. [ ] **Basic Testing**
 - Add tests for key functions
 - Test important user flows
 - Set up pytest properly
 - **Why**: Catch bugs before they happen
 - **Time**: 8-16 hours

7. [ ] **Documentation**
 - Add docstrings to key functions
 - Write a basic README
 - Document any tricky parts
 - **Why**: Help future you (and others)
 - **Time**: 3-6 hours

### How to Approach This
- **Start Simple**: Fix security issues first, then performance
- **Small Steps**: Make one change at a time and test it
- **Test as You Go**: Add tests while you refactor
- **Document Changes**: Keep notes on what you changed and why
- **Total Time**: 39-78 hours (incrementally of focused work)
- **Approach**: Work on it bit by bit in your spare time

## Success Measures

### Before Changes
- **Code Complexity**: [How complex is it now?]
- **Duplicate Code**: [How much code is repeated?]
- **Bug Count**: [Known issues]
- **Test Coverage**: [How much is tested?]

### Goals After Improvements
- **Security**: No obvious security holes
- **Performance**: Reasonable response times for your use case
- **Complexity**: Functions that are easy to understand
- **Duplication**: Minimal repeated code
- **Testing**: Key functionality is tested
- **Documentation**: Important parts are documented

### Expected Benefits
- **Security**: Basic protection against common issues
- **Speed**: Noticeably faster performance
- **Maintainability**: Much easier to make changes
- **Confidence**: You can modify code without breaking things
- **Stability**: Fewer unexpected crashes or bugs
- **Understanding**: New contributors can figure out the code

## Things to Watch Out For

### Potential Issues
- **Breaking Changes**: [Will this break existing functionality?]
- **Database Changes**: [Do you need to migrate data?]
- **Dependencies**: [Will updating packages cause issues?]
- **Performance**: [Could changes make things slower?]

### Safety Net
- **Backups**: Make sure you can revert changes
- **Testing**: Test changes in a safe environment first
- **Small Steps**: Make one change at a time
- **Version Control**: Commit frequently with good messages

### Getting Help
- **Documentation**: Read the docs for libraries you're using
- **Community**: Ask questions on Stack Overflow or Reddit
- **Code Review**: Have someone else look at important changes
- **Learning**: Take time to understand new patterns before using them
```

**Analysis Scope & Context Intelligence:**
- **Micro-Analysis**: Current selection or function under cursor
- **File-Level Analysis**: Complete file with all dependencies
- **Module-Level Analysis**: Related files and their interactions
- **System-Level Analysis**: Architecture patterns across entire codebase
- **Cross-Cutting Concerns**: Security, performance, and maintainability across all layers

**Advanced Python Context Awareness:**
- **Framework Detection**: [Django, Flask, FastAPI, Starlette, Tornado, Quart]
- **Architecture Pattern**: [Django MVT, Flask blueprints, FastAPI dependency injection, Clean Architecture]
- **Database Integration**: [Django ORM, SQLAlchemy, asyncpg, PyMongo optimization patterns]
- **API Design**: [Django REST Framework, Flask-RESTful, FastAPI automatic docs, GraphQL with Strawberry]
- **Build Tools**: [Poetry, pip-tools, setuptools, wheel, Docker multi-stage builds]
- **CI/CD Pipeline**: [pytest, tox, GitHub Actions, GitLab CI, pre-commit hooks]

**Smart Python Configuration & Adaptation:**
- **Python Version**: [Auto-detect 3.8+ features, recommend 3.11+ for performance]
- **Framework Version**: [Django 4.x LTS, Flask 2.x, FastAPI 0.95+, compatibility analysis]
- **Performance Profile**: [ASGI vs WSGI, asyncio patterns, multiprocessing considerations]
- **Package Management**: [Poetry vs pip-tools, virtual environment strategies]
- **Deployment Environment**: [Docker, Kubernetes, serverless (AWS Lambda), PaaS optimization]
- **Compliance Requirements**: [Data privacy with Django, HIPAA-compliant logging, audit trails]

**Industry-Specific Adaptations:**
- **Fintech**: [PCI compliance, transaction integrity, audit trails]
- **Healthcare**: [HIPAA compliance, data privacy, security protocols]
- **E-commerce**: [Performance optimization, scalability patterns]
- **Gaming**: [Real-time performance, memory optimization]
- **IoT/Embedded**: [Resource constraints, power efficiency]

**Modern Development Practices Integration:**
- **DevOps Alignment**: [Infrastructure as code compatibility]
- **Observability**: [Logging, monitoring, tracing integration points]
- **Security DevOps**: [SAST/DAST integration, vulnerability scanning]
- **Documentation as Code**: [API docs, architecture diagrams generation]
- **Feature Flags**: [Progressive deployment and A/B testing support]

**Next Steps:**
After generating the report, ask: "Which area would you like to tackle first - security fixes, performance improvements, or code organization? I can help you implement the changes step by step."




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
