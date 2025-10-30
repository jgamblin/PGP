# Python Development Assistant Guide

This guide helps you use the normalized Python prompts effectively for personal projects and POC development. Copy this into your actual Python project and adapt it to your specific needs.

Purpose: Coordinate code improvements, testing, and quality checks using the practical Python prompts in this collection.

---

## Summary

To provide guidance, please provide:

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
- Team collaboration preferences
- Deployment environment
- Any compliance or security requirements

## Situation Assessment

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

## Focus Areas for Personal Projects
1. **Code Quality**: Clean, readable code that works correctly
2. **Basic Testing**: Cover the important functions and edge cases
3. **Type Hints**: Add helpful type annotations for clarity
4. **Performance**: Fix obvious bottlenecks and inefficiencies
5. **Documentation**: Clear README and function documentation
6. **Style**: Consistent formatting with Flake8 and Black

---
## Simple Project Structure
```
my_project/
 src/ # Your main code
 my_project/
 __init__.py
 main.py
 utils.py
 tests/ # Test files
 test_main.py
 test_utils.py
 requirements.txt # Dependencies
 README.md # Project documentation
 .flake8 # Style configuration
```
Optional: `pyproject.toml`, `.pre-commit-config.yaml`, `docs/`

---
## Quick Code Review Prompt
```
Use the Python Code Review Assistant to review this code:
[paste your code or file]

Focus on:
- Code correctness and potential bugs
- Readability and maintainability
- Basic performance issues
- Missing error handling
- Simple improvements

Provide practical suggestions with examples.
```

Follow-ups:
- "Show mypy error elimination order (highest leverage first)."
- "Generate diff adding only return type hints to public functions in file X." 
- "List unawaited async calls or blocking sync calls inside async funcs." 

---
## Adding Type Hints
```
Use the Python Type Hints Assistant to add type annotations:
[paste your function or class]

Start with:
1. Function parameters and return types
2. Class attributes
3. Complex data structures (dicts, lists)

Focus on helpful annotations that catch common bugs.
```

---
## Performance Check
```
Use the Python Async & Concurrency Assistant for async code:
[paste your async code]

Or use the Database & ORM Assistant for database code:
[paste your models or queries]

Look for:
- Slow loops or inefficient algorithms
- Database N+1 query problems
- Blocking operations in async code
- Memory usage issues
```

---
## Adding Tests
```
Use the Python Testing Assistant to create tests:
[paste your function or class]

Create tests for:
- Normal operation (happy path)
- Edge cases and error conditions
- Different input types
- Important business logic

Provide pytest examples that are easy to run.
```

---
## Basic Security Check
```
Use the Python Code Review Assistant to check for security issues:
[paste your code]

Look for:
- User input validation
- SQL injection risks
- File path traversal
- Unsafe deserialization
- Missing error handling

Provide safer alternatives with examples.
``` 

---
## Better Logging
```
Use the Python Code Helper to improve logging:
[paste your code with print statements or poor error handling]

Replace:
- print() statements with proper logging
- Bare except clauses with specific exceptions
- Silent failures with informative error messages

Show practical logging examples.
```

---
## Improvement Workflow
1. **Code Review**: Use Code Review Assistant for overall assessment
2. **Fix Issues**: Use Code Helper to clean up identified problems
3. **Add Tests**: Use Testing Assistant for important functions
4. **Type Hints**: Use Type Hints Assistant for better IDE support
5. **Style**: Use Code Style Assistant for consistent formatting
6. **Documentation**: Use Documentation Assistant for README and docstrings

---
## Final Check
- [ ] Code runs without errors
- [ ] Tests pass (if you have them)
- [ ] Flake8 style check passes
- [ ] Functions have clear names and docstrings
- [ ] No obvious security issues
- [ ] README explains how to use the project 

---
## Making Changes
```
When asking for code improvements:
- Request specific, small changes
- Ask for before/after examples
- Focus on one issue at a time
- Test changes before applying more
```

---
## Getting Better Responses
If suggestions are too vague, ask for:
```
- Specific code examples
- Step-by-step instructions
- Explanation of why the change helps
- Simple examples I can copy and modify
```

---
## Example Improvement Session
```
1. Code review: "What can be improved in this file?"
2. Fix issues: "Help me clean up this function"
3. Add tests: "Create tests for this function"
4. Add types: "Add type hints to this code"
5. Document: "Write a docstring for this function"
6. Style: "Check the formatting of this file"
```

---
## Project Setup
```
Use the Python Project Setup Assistant to:
- Create a good project structure
- Set up requirements.txt or pyproject.toml
- Configure Flake8, Black, and pytest
- Create a helpful README template

Start with: "Help me set up a new Python project for [describe your project]"
```

---
## Before You're Done
- [ ] Does the code do what you intended?
- [ ] Are there tests for the important parts?
- [ ] Is the code readable and well-organized?
- [ ] Does it handle errors gracefully?
- [ ] Is the README up to date?
- [ ] Can someone else understand and use your code? 

---
## Using This Guide
Copy this guide into your actual Python project and adapt it to your needs. Replace examples with your specific project details.

Focus on small, practical improvements that make your code better step by step.




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
