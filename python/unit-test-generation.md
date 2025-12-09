# Python Testing Helper

> **Purpose**: Generate and improve Python tests  
> **Best For**: Copilot, ChatGPT, Claude, Agents  
> **Python Version**: 3.11+  
> **Last Updated**: 2025-12-09

---

## Mission

Help create **reliable, well-tested code** using pytest, hypothesis for property testing, and modern async testing patterns.

---

## Guard Clauses

**If no code provided:**
```
NO_ACTIONABLE_INPUT

Please provide Python code to generate tests for:
- Function or class to test
- Expected behavior description
- Edge cases to consider
```

**If code already has good coverage:**
```
TESTS_ADEQUATE

✅ Test coverage appears adequate.
- Happy path: ✓
- Edge cases: ✓
- Error handling: ✓

Consider adding property-based tests with hypothesis for additional confidence.
```

---

## Quick Context Checklist

```
☐ Code to test
☐ Existing tests (if any)
☐ Test framework (pytest recommended)
☐ Special requirements (async, database, mocking)
```


> 📝 **Standard Context**: See [_common-sections.md](_common-sections.md) for full input checklist and severity levels.

---

## Copy-Paste Testing Prompts

### Prompt: Generate Basic Tests
```text
Generate pytest tests for this code:

{{CODE}}

Include:
1. Happy path test (expected usage)
2. Edge cases (empty, None, boundaries)
3. Error conditions (invalid input, exceptions)
4. Use @pytest.mark.parametrize for multiple inputs

Output complete, runnable test file with docstrings.
```

### Prompt: Generate Property-Based Tests
```text
Generate hypothesis property-based tests for this code:

{{CODE}}

Use hypothesis to test:
1. Properties that should always hold
2. Invariants the function maintains
3. Round-trip behaviors (serialize/deserialize)
4. Commutative/associative properties if applicable

Include appropriate @given strategies.
```

### Prompt: Generate Async Tests
```text
Generate pytest-asyncio tests for this async code:

{{CODE}}

Include:
1. Basic async function tests
2. Concurrent execution tests
3. Timeout handling tests
4. Exception propagation tests
5. Use async fixtures where needed

Mark tests with @pytest.mark.asyncio.
```

### Prompt: Generate API Tests
```text
Generate tests for this FastAPI/Flask endpoint:

{{CODE}}

Include:
1. Successful request tests
2. Validation error tests (400)
3. Authentication tests (401/403)
4. Not found tests (404)
5. Use TestClient or pytest fixtures

Test both response status and body content.
```

### Prompt: Improve Test Coverage
```text
Analyze this code and existing tests:

Code:
{{CODE}}

Existing Tests:
{{TESTS}}

Identify:
1. Untested code paths
2. Missing edge cases
3. Uncovered error conditions
4. Integration points without tests

Generate additional tests to improve coverage.
```

---

## Practical Testing Approach

### 1. **Bug Prevention**

- **Key Functionality**: Test the most important parts of your code
- **Edge Cases**: Test boundary conditions and error scenarios
- **Error Handling**: Make sure errors are handled gracefully
- **Business Logic**: Verify your core logic works correctly

### 2. **Confidence & Speed**

- **Regression Prevention**: Catch when changes break existing functionality
- **Quick Feedback**: Fast tests that run quickly during development
- **API Testing**: Test your endpoints and integrations
- **Basic Security**: Test for obvious security issues

### 3. **Maintainability**

- **Simple Tests**: Easy to understand and modify
- **Clear Examples**: Tests that show how code should work
- **Safe Refactoring**: Change code confidently knowing tests will catch issues
- **Easy Debugging**: Tests help pinpoint where problems occur

## Testing Guidelines

**Avoid:**

- Tests that don't actually verify anything useful
- Focusing only on coverage numbers instead of meaningful tests
- Tests that break when you make small, safe changes
- Tests that take forever to run
- Skipping tests for important user workflows
- Writing tests without understanding what could go wrong

## Python Testing Report

Generate a **Practical Testing Analysis Report** and save it as a markdown file named `python-test-analysis-[YYYY-MM-DD].md`:


## Report Format

Generate a comprehensive analysis and save as **two deliverables**:

### 1. Summary Report: `unit-test-generation-[YYYY-MM-DD].md`

```markdown
# Unit Test Generation

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

### 2. Per-Finding Details: `unit-test-generation-[YYYY-MM-DD]/`

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
# Python Testing Analysis Report

## Key Function Testing Needs

### Function: `function_name()`

- **Location**: `filename.py:line X`
- **Importance**: [Critical/Important/Nice to have]
- **How Often Used**: [Frequently/Sometimes/Rarely]
- **What Breaks If It Fails**: [User can't log in, data gets corrupted, etc.]
- **Current Tests**: [X% covered, what's missing]
- **Known Issues**: [Bugs found before, tricky edge cases]
- **Performance**: [Fast/slow, memory usage if relevant]
- **Security Notes**: [Input validation, auth checks, sensitive data]
- **Special Requirements**: [Any compliance or business rules to test]

## Test Strategy

### Important Tests to Write
1. **Test**: `test_user_login_success`
 - **Purpose**: Make sure users can log in properly
 - **Scenario**: Valid user credentials and successful login
 - **What to Check**: User gets logged in, session created, redirected correctly
 - **Performance**: <200ms execution time under load

2. **Test**: `test_user_login_failure_scenarios`
 - **Purpose**: Handle login errors properly
 - **Scenarios**: Wrong password, non-existent user, account locked
 - **What to Check**: Appropriate error messages, no sensitive info leaked

3. **Test**: `test_user_login_security`
 - **Purpose**: Basic security checks
 - **Scenarios**: SQL injection attempts, rate limiting
 - **What to Check**: Attacks are blocked, no crashes or data leaks

### Edge Cases & Error Scenarios
1. **Boundary Testing**
 - **Empty Values**: `None`, `""`, `[]`, `{}` handled properly
 - **Limits**: Max users, memory usage, timeouts
 - **Bad Data**: Corrupted input, malformed JSON, encoding problems
 - **Concurrency**: Multiple users at once, data conflicts

2. **Common Failures**
 - **Network Issues**: Connection timeouts, API failures
 - **Database Problems**: Connection errors, transaction failures
 - **External Services**: Third-party API downtime, rate limits
 - **Resource Issues**: Memory problems, slow responses

### Integration Testing

- **User Workflows**: Complete user journeys work end-to-end
- **API Testing**: Your endpoints work with other services
- **Security Testing**: Auth and permissions work correctly
- **Performance Testing**: App handles expected load

## Test Examples

### Test File: `test_user_service.py` - Basic Test Suite
```python
"""Tests for user service functionality.

Basic tests to make sure user operations work correctly
and catch bugs before they cause problems.
"""
import pytest
from unittest.mock import Mock, patch
from datetime import datetime

class TestUserService:
 """Test user service operations."""

 @pytest.fixture
 def sample_user_data(self):
 """Sample user data for testing."""
 return {
 "email": "test@example.com",
 "name": "Test User",
 "password": "secure_password123"
 }

 @pytest.fixture
 def mock_database(self):
 """Mock database for testing."""
 with patch('user_service.database') as mock_db:
 mock_db.save_user.return_value = {
 'id': 123,
 'email': 'test@example.com',
 'created_at': datetime.now()
 }
 yield mock_db

 def test_create_user_success(self, sample_user_data, mock_database):
 """Test creating a new user successfully."""
 # Arrange
 service = UserService(database=mock_database)

 # Act
 result = service.create_user(sample_user_data)

 # Assert - Check it worked
 assert result["success"] == True
 assert result["user_id"] is not None
 assert result["email"] == sample_user_data["email"]

 # Check database was called
 mock_database.save_user.assert_called_once()

 # Check password was hashed (not stored in plain text)
 saved_data = mock_database.save_user.call_args[0][0]
 assert saved_data["password"] != sample_user_data["password"]

 def test_create_user_with_invalid_email(self, mock_database):
 """Test creating user with invalid email."""
 # Arrange
 service = UserService(database=mock_database)
 invalid_data = {
 "email": "not-an-email",
 "name": "Test User",
 "password": "secure_password123"
 }

 # Act
 result = service.create_user(invalid_data)

 # Assert - Should fail gracefully
 assert result["success"] == False
 assert "email" in result["error"].lower()

 # Database should not be called
 mock_database.save_user.assert_not_called()

 def test_create_user_database_error(self, sample_user_data, mock_database):
 """Test handling database errors."""
 # Arrange
 service = UserService(database=mock_database)
 mock_database.save_user.side_effect = DatabaseError("Connection failed")

 # Act
 result = service.create_user(sample_user_data)

 # Assert - Should handle error gracefully
 assert result["success"] == False
 assert "error" in result
 assert "Connection failed" not in result["error"] # Don't expose internal errors

 # Should provide user-friendly message
 assert "try again" in result["error"].lower() or "temporarily unavailable" in result["error"].lower()
```

## Test Implementation Roadmap

### Phase 1: Critical Path Protection (Week 1-2, 32-48 hours)

1. [ ] **Core Functionality Testing**
 - **Implementation**: 100% coverage of transaction processing, user authentication, data validation
 - **Success Metric**: Zero critical path failures in production

2. [ ] **Security & Compliance Testing**
 - **Implementation**: Input validation, encryption, audit trail testing
 - **Coverage**: PCI-DSS, GDPR, SOX compliance validation

### Phase 2: System Reliability & Performance (Week 3-4, 24-36 hours)

1. [ ] **Performance & Load Testing**
 - **Target**: Maintain <200ms response time under 10x load
 - **Implementation**: Stress testing, memory profiling, database performance

2. [ ] **Integration & Contract Testing**
 - **Target**: 99.9% uptime through comprehensive integration validation
 - **Implementation**: API contract testing, third-party service mocking

### Phase 3: Advanced Quality Engineering (Week 5-6, 20-28 hours)

1. [ ] **Chaos Engineering & Resilience Testing**
 - **Implementation**: Network partitions, service failures, resource exhaustion
 - **Coverage**: Validate graceful degradation under adverse conditions

## Test Engineering Success Metrics

- **Production Incident Reduction**: 90% decrease in test-preventable bugs
- **Deployment Velocity**: 60% faster releases through comprehensive test automation
- **System Reliability**: 99.95% uptime through robust testing
- **Development Confidence**: 95% of changes deployed without rollback
- **Quality Assurance**: 100% audit success rate through automated validation

**Test Scope:**

- **Current Selection**: Generate tests for the currently selected function/class
- **Current File**: Create comprehensive test suite for the active Python file
- **Cursor Context**: Test the function/method containing the cursor
- **Related Files**: Include integration tests for imported modules visible in workspace

**IDE Integration:**

- Auto-detect testing framework from project dependencies (pytest.ini, setup.py, requirements.txt)
- Use existing import statements to understand dependencies and mock requirements
- Analyze function signatures and type hints for comprehensive parameter testing
- Reference related test files in workspace to maintain consistency
- Detect database models and API calls for integration test suggestions

**Smart Configuration:**

- Framework: [Auto-detect from project structure and existing test files]
- Dependencies: [Auto-identify external services, APIs, and databases from imports]
- Performance testing: [Include for functions with loops, file I/O, or network calls]
- Coverage analysis: [Focus on critical business logic and complex algorithms]

## Advanced Python Test Intelligence Engine

**Test Strategy Analysis:**

- **Risk Assessment**: Analysis of critical untested code paths
- **Performance Critical Path Detection**: Automated identification of SLA-impacting functions
- **Security Testing Requirements**: PCI-DSS, GDPR, HIPAA compliance validation needs
- **Integration Complexity Analysis**: Third-party service dependency mapping
- **Test Data Management**: Production-representative test data generation
- **Chaos Engineering Integration**: Failure mode testing and resilience validation

**Smart Test Configuration Engine:**

- **Framework Optimization**: pytest vs unittest selection based on project complexity
- **Test Environment Scaling**: Docker containerization, database seeding, service mocking
- **CI/CD Integration**: Automated test execution, coverage reporting, quality gates
- **Performance Benchmarking**: Automated performance regression detection
- **Test Maintenance**: Automated test update detection and refactoring suggestions
- **Coverage Analysis**: Business-critical path prioritization over line coverage metrics

## Interactive Excellence Protocol

**Upon analysis completion:**
"I've identified [X] critical testing gaps in [specific function] which currently has [coverage %] test coverage. The highest-risk areas include [specific risks]. Implementing comprehensive tests will prevent [Y]% of potential failures and improve system reliability. Shall I provide the exact test implementation for these critical functions?"

## Test Engineering Excellence Validation

**Quality Checklist:**

- Critical execution paths protected with comprehensive test coverage
- Performance requirements validated through load and stress testing
- Security and compliance requirements verified through automated testing
- Error handling and recovery strategies thoroughly validated
- Integration points tested with realistic failure scenarios
- Impact assessed through risk-based testing approach
- Deployment confidence enabled through comprehensive test automation
- Test maintenance strategy ensuring long-term sustainability

**Quality Guidelines:**

- **Critical Path Coverage**: 100% coverage of mission-critical code paths
- **Performance Assurance**: SLA compliance validated through automated testing
- **Quality Engineering**: Tests serve as living documentation and executable specifications
- **Continuous Improvement**: Test metrics drive ongoing quality improvements




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
