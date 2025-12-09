# Python Code Review Helper

> **Purpose**: Review PRs and provide actionable feedback  
> **Best For**: Copilot, ChatGPT, Claude, Agents  
> **Python Version**: 3.11+  
> **Last Updated**: 2025-12-09

---

## Mission

Provide **practical code review feedback** that catches bugs, security issues, and suggests improvements with specific code suggestions.

---

## Guard Clauses

**If no diff provided:**
```
NO_ACTIONABLE_DIFF

No code changes detected. Please provide:
- `git diff main...HEAD` output, OR
- Specific files to review, OR
- Code snippets to analyze
```

**If PR looks good:**
```
✅ **LGTM — Approved to Merge**

Nice work! This PR is ready to ship.

**Technical Checklist**
- [x] No security regressions
- [x] Query performance acceptable
- [x] Error handling covers expected failures
- [x] Type hints on public interfaces

**What I Liked**
- [Specific positive observation]
- [Another specific positive]

Merging! 🚀
```

---

## Quick Context Checklist

```
☐ Branch: `git branch --show-current`
☐ Diff: `git diff main...HEAD`
☐ Changed files: `git diff main...HEAD --name-only`
☐ Framework context if relevant
```

> 📝 **Standard Context**: See [_common-sections.md](_common-sections.md) for severity levels and output formats.

---

## Copy-Paste PR Review Prompts

### Prompt: Full PR Review
```text
Review this PR:

{{DIFF}}

Check for:
1. 🔴 Security issues (injection, auth, secrets)
2. 🟠 Bugs and logic errors
3. 🟡 Performance problems (N+1, memory)
4. 🟢 Code style and best practices

For each issue:
- File and line number
- Severity level
- GitHub suggestion block with fix
- Brief explanation
```

### Prompt: Security-Focused Review
```text
Security review for this PR:

{{DIFF}}

Focus on:
- SQL/command injection
- Authentication/authorization
- Input validation
- Secret handling
- Dependency vulnerabilities

Flag all security concerns with severity.
```

### Prompt: Quick Review
```text
Quick review of this diff:

{{DIFF}}

Only flag:
- Bugs that will break in production
- Security vulnerabilities
- Obvious performance issues

Skip style nits. Be concise.
```

### Prompt: Generate PR Description
```text
Generate a PR description for this diff:

{{DIFF}}

Include:
1. Summary (what and why)
2. Changes made (bullet points)
3. Testing done
4. Breaking changes (if any)
5. Related issues
```

### Prompt: Review Test Coverage
```text
Review test coverage for this PR:

Code changes:
{{CODE}}

Test changes:
{{TESTS}}

Identify:
- Untested code paths
- Missing edge case tests
- Weak assertions
- Suggest specific tests to add
```

---

## Practical Code Review Approach

### 1. **Security & Safety**
- **Basic Security**: SQL injection prevention, input validation, secure defaults
- **Framework Safety**: Proper Django/FastAPI security practices, CSRF protection
- **Dependencies**: Check for known vulnerabilities in packages
- **Secrets**: No hardcoded passwords or API keys in code

### 2. **Performance & Efficiency**
- **Simple Optimizations**: Obvious performance improvements, efficient algorithms
- **Database Queries**: Avoid N+1 problems, use proper ORM patterns
- **Memory Usage**: Efficient data structures, avoid memory leaks
- **Async Patterns**: Proper async/await usage when beneficial

### 3. **Code Organization & Clarity**
- **Readability**: Clear naming, logical structure, easy to follow
- **Separation**: Functions do one thing, classes have clear purposes
- **Dependencies**: Reasonable coupling, clear interfaces
- **Patterns**: Use appropriate patterns, avoid overengineering

### 4. **Testing & Reliability**
- **Test Coverage**: Key functionality is tested, edge cases considered
- **Error Handling**: Graceful failure, helpful error messages
- **Documentation**: Important functions have docstrings, README is updated
- **Maintainability**: Code is easy to change and extend

## Review Guidelines
**Avoid:**
- Nitpicking minor style issues while missing real problems
- Giving vague feedback without specific suggestions
- Ignoring obvious performance or security issues
- Focusing on theoretical problems instead of practical concerns
- Assuming tests are good just because they exist

## Report Format

Generate a comprehensive analysis and save as **three deliverables**:

### 1. Summary Report: `pr-review-feedback-[YYYY-MM-DD].md`

```markdown
# Pr Review Feedback

## Overview
- **Files Analyzed**: [Count]
- **Critical Issues**: [Count]
- **Suggestions**: [Count]

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

## Next Steps
- Address any critical security issues first
- Consider performance and quality improvements
- Add tests for important functionality
```

### 2. Per-Finding Details: `pr-review-feedback-[YYYY-MM-DD]/`

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

### 3. Quick Approval Comment: `pr-approval-comment-[YYYY-MM-DD].md`

**ONLY generate this file if there are NO critical issues** (security vulnerabilities, data loss risks, blocking bugs).

If the PR passes review, create a short, copy-paste ready approval message:

```markdown
✅ **LGTM — Approved to Merge**

Nice work! This PR is ready to ship. I verified the following:

**Technical Checklist**
- [ ] No security regressions (auth, input validation, secrets)
- [ ] Query performance acceptable (no N+1, bounded result sets)
- [ ] Error handling covers expected failure modes
- [ ] Test coverage on critical paths
- [ ] Type hints present on public interfaces

**What I Liked**
- [Specific positive: e.g., "Clean separation between data access and business logic"]
- [Specific positive: e.g., "Good use of context managers for resource cleanup"]

**Follow-Up Items** *(non-blocking, track separately)*
| Item | File | Tracking |
|------|------|----------|
| [Brief description] | `path/file.py` | Issue #XX or next sprint |

---
Thanks for the solid contribution — merging! 🚀
```

**Guidelines for Approval Comment:**
- Maximum 25 lines
- Only create if PR can be safely merged (no critical security/data/blocking issues)
- Complete the technical checklist with checks for items verified
- Include 2–3 specific positive observations (avoid generic praise)
- List non-blocking follow-ups in a table with file refs and tracking links
- Friendly, collegial tone — celebrate good engineering

---

### Alternative Format (if detailed findings used)

```markdown
# Code Review Analysis

## Review Summary
- **Security Check**: [Any security concerns found?]
- **Code Quality**: [Overall quality rating and main issues]
- **Performance**: [Any performance concerns or improvements]
- **Testing**: [Are the changes properly tested?]

## Issues Found

### Security Concerns

#### Issue: [Type of security issue found]
- **File**: `path/to/file.py:line X-Y`
- **Risk Level**: High/Medium/Low
- **Problem**: [What could go wrong]
- **Impact**: [What happens if exploited]

**Current Code:**
```python
# Code that has the security issue
def unsafe_function(user_input):
 query = f"SELECT * FROM users WHERE id = {user_input}"
 return db.execute(query).fetchall()
```

**Better Approach:**
```python
# Safer way to write this
def safe_function(user_input: int) -> List[User]:
 """Get user data safely."""
 # Validate input first
 if not isinstance(user_input, int) or user_input <= 0:
 raise ValueError("Invalid user ID")

 # Use parameterized query
 query = "SELECT * FROM users WHERE id = %s"
 return db.execute(query, (user_input,)).fetchall()
```

**Why This is Better:**
- Prevents SQL injection attacks
- Validates input before using it
- Clear error messages for invalid input

## Git Analysis Steps

### Review Changed Files
```bash
# Check what branch you're on
git branch --show-current

# See what Python files changed
git diff main...HEAD --name-only | grep '\.py$'

# Look at the actual changes
git diff main...HEAD

# Check if dependencies changed
git diff main...HEAD requirements.txt setup.py pyproject.toml
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


## Quality Guidelines

### Security
- No critical vulnerabilities or hardcoded secrets
- Input validation for user data
- Safe handling of sensitive information

### Code Quality
- Linting passes (ruff, black)
- Functions are focused and readable
- No significant code duplication

### Testing
- Important functionality has tests
- Edge cases are considered
- Tests verify behavior, not implementation

### Documentation
- Complex logic is explained
- README updated if needed



## After the Review

1. **Run tests** to make sure nothing broke
2. **Fix critical issues first** (security, bugs)
3. **Consider other suggestions** as time permits
4. **Update docs** if you made significant changes
