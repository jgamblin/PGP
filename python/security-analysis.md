# Python Security Analysis Assistant

> **Purpose**: Identify and fix security vulnerabilities  
> **Best For**: Copilot, ChatGPT, Claude, Agents  
> **Python Version**: 3.11+  
> **Last Updated**: 2025-12-09

---

## Mission

Help identify and fix **security vulnerabilities** in Python applications. Use Ruff's security rules (S prefix) and pip-audit for comprehensive coverage.

---

## Guard Clauses

**If no code provided:**
```
NO_ACTIONABLE_INPUT

Please provide Python code or dependencies to analyze:
- Source files
- requirements.txt / pyproject.toml
- Specific security concerns
```

**If no security issues found:**
```
NO_SECURITY_ISSUES

✅ Security scan complete — no vulnerabilities detected.

Checks performed:
- SQL/Command injection: ✓
- Hardcoded secrets: ✓
- Unsafe deserialization: ✓
- Vulnerable dependencies: ✓
- Path traversal: ✓

Code appears secure for the analyzed scope.
```

---

## Quick Context Checklist

```
☐ Code to scan
☐ Dependencies (requirements.txt, pyproject.toml)
☐ Framework (Django, Flask, FastAPI)
☐ Deployment environment (cloud, container, etc.)
```


> 📝 **Standard Context**: See [_common-sections.md](_common-sections.md) for full input checklist and severity levels.

---

## Copy-Paste Security Prompts

### Prompt: Quick Security Scan
```text
Security scan this Python code:

{{CODE}}

Check for:
1. SQL/command injection
2. Hardcoded secrets (API keys, passwords)
3. Unsafe deserialization (pickle, yaml.load)
4. Path traversal vulnerabilities
5. SSRF risks
6. Insecure cryptography

Output severity as: 🔴 Critical | 🟠 High | 🟡 Medium | 🟢 Low

If clean: output `NO_SECURITY_ISSUES`
```

### Prompt: Dependency Audit
```text
Audit these Python dependencies for security:

{{REQUIREMENTS_TXT or PYPROJECT_TOML}}

Check for:
1. Known CVEs in any package
2. Outdated packages with security fixes
3. Typosquatting/suspicious package names
4. Overly permissive version ranges

Output as table:
| Package | Version | Issue | Severity | Action |
```

### Prompt: Secure Code Refactor
```text
Refactor this code to be secure:

{{CODE}}

Apply:
1. Parameterized queries (not f-strings)
2. Input validation with Pydantic
3. Secrets from environment variables
4. Safe file path handling with pathlib
5. Proper error messages (no stack traces to users)

Output the secure version with inline comments explaining changes.
```

### Prompt: Auth/Authz Review
```text
Review this authentication/authorization code:

{{CODE}}

Check for:
1. Password hashing (bcrypt/argon2, not MD5/SHA1)
2. Token validation (expiry, signature)
3. Session management issues
4. Privilege escalation vectors
5. Rate limiting on auth endpoints

Output findings with severity and specific fixes.
```

### Prompt: AI/LLM Security Check
```text
Review this AI/LLM integration code for security:

{{CODE}}

Check for:
1. Prompt injection vulnerabilities
2. Sensitive data in prompts
3. Output sanitization
4. API key exposure
5. Rate limiting and cost controls
6. Model output validation

This is critical for 2026 AI-integrated applications.
```

---

## Security Analysis Framework

### 1. **Common Python Security Issues**

- **Injection Attacks**: SQL injection, command injection, code injection
- **Input Validation**: Unvalidated user input and data sanitization
- **Authentication/Authorization**: Weak authentication and access controls
- **Cryptography**: Weak encryption, poor key management, insecure hashing
- **Dependencies**: Vulnerable third-party packages
- **Configuration**: Insecure defaults and exposed secrets

### 2. **Security Tools (2026 Stack)**

```bash
# All-in-one with Ruff (includes bandit rules)
ruff check --select=S .

# Dependency audit
pip-audit

# Advanced static analysis
semgrep --config=p/python
```

### 3. **Secure Development Practices**

- **Input Sanitization**: Validate and sanitize all user inputs
- **Parameterized Queries**: Prevent SQL injection attacks
- **Secure Headers**: Implement proper HTTP security headers
- **Error Handling**: Don't expose sensitive information in errors
- **Logging Security**: Log security events without exposing secrets

## Security Analysis Report


## Report Format

Generate a comprehensive analysis and save as **two deliverables**:

### 1. Summary Report: `security-analysis-[YYYY-MM-DD].md`

```markdown
# Security Analysis

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

### 2. Per-Finding Details: `security-analysis-[YYYY-MM-DD]/`

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
# Python Security Analysis

## Security Assessment
- **Overall Risk Level**: [Low/Medium/High based on findings]
- **Critical Issues**: [Number of critical security vulnerabilities]
- **High Priority Fixes**: [Issues that need immediate attention]
- **Dependencies**: [Vulnerable packages and versions]
- **Code Coverage**: [Percentage of code analyzed]

## Critical Security Issues

### 1. SQL Injection Vulnerabilities
- **Location**: `filename.py:line X`
- **Risk Level**: Critical
- **Description**: User input directly concatenated into SQL queries
- **Current Code**:
```python
# VULNERABLE - Never do this
def get_user(user_id):
 query = f"SELECT * FROM users WHERE id = {user_id}"
 return db.execute(query).fetchone()
```
- **Secure Fix**:
```python
# SECURE - Use parameterized queries
def get_user(user_id: int) -> Optional[User]:
 query = "SELECT * FROM users WHERE id = ?"
 return db.execute(query, (user_id,)).fetchone()

# Or with SQLAlchemy
def get_user(user_id: int) -> Optional[User]:
 return session.query(User).filter(User.id == user_id).first()
```
- **Impact**: Attackers could access, modify, or delete database data
- **Priority**: Fix immediately

### 2. Command Injection
- **Location**: `filename.py:line Y`
- **Risk Level**: Critical
- **Description**: User input passed to shell commands without sanitization
- **Current Code**:
```python
# VULNERABLE - Command injection risk
import subprocess
def process_file(filename):
 subprocess.run(f"convert {filename} output.jpg", shell=True)
```
- **Secure Fix**:
```python
# SECURE - Use subprocess with argument list
import subprocess
from pathlib import Path

def process_file(filename: str):
 # Validate filename
 if not Path(filename).exists():
 raise ValueError("File does not exist")

 # Use argument list instead of shell=True
 subprocess.run(["convert", filename, "output.jpg"], check=True)
```

### 3. Insecure Cryptography
- **Location**: `filename.py:line Z`
- **Risk Level**: High
- **Description**: Using weak hashing algorithms or insecure random generation
- **Current Code**:
```python
# VULNERABLE - Weak hashing
import hashlib
import random

def hash_password(password):
 return hashlib.md5(password.encode()).hexdigest()

def generate_token():
 return str(random.randint(1000000, 9999999))
```
- **Secure Fix**:
```python
# SECURE - Strong hashing and random generation
import hashlib
import secrets
import bcrypt

def hash_password(password: str) -> str:
 # Use bcrypt for password hashing
 salt = bcrypt.gensalt()
 return bcrypt.hashpw(password.encode('utf-8'), salt).decode('utf-8')

def verify_password(password: str, hashed: str) -> bool:
 return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))

def generate_secure_token(length: int = 32) -> str:
 return secrets.token_urlsafe(length)
```

## Security Audit Findings

### Input Validation Issues
- [ ] User inputs not validated or sanitized
- [ ] File uploads without type/size restrictions
- [ ] URL parameters used without validation
- [ ] Form data processed without CSRF protection

### Authentication & Authorization
- [ ] Weak password requirements
- [ ] No rate limiting on login attempts
- [ ] Session management issues
- [ ] Missing access control checks

### Configuration Security
- [ ] Secrets hardcoded in source code
- [ ] Debug mode enabled in production
- [ ] Insecure default configurations
- [ ] Missing security headers

### Dependency Vulnerabilities
- [ ] Outdated packages with known vulnerabilities
- [ ] Packages from untrusted sources
- [ ] Unnecessary dependencies increasing attack surface

## Security Implementation Plan

### Phase 1: Critical Fixes (Immediate - 4-8 hours)

1. **Fix Injection Vulnerabilities**
 ```python
 # Install secure database library
 pip install sqlalchemy

 # Replace string concatenation with parameterized queries
 from sqlalchemy import text

 def safe_query(user_input: str):
 query = text("SELECT * FROM users WHERE name = :name")
 return db.execute(query, {"name": user_input}).fetchall()
 ```

2. **Secure Input Validation**
 ```python
 from typing import Optional
 import re
 from html import escape

 def validate_email(email: str) -> bool:
 pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
 return bool(re.match(pattern, email))

 def sanitize_input(user_input: str) -> str:
 # Remove potentially dangerous characters
 sanitized = re.sub(r'[<>"\']', '', user_input)
 return escape(sanitized)

 def validate_file_upload(filename: str, max_size: int = 5_000_000) -> bool:
 allowed_extensions = {'.jpg', '.jpeg', '.png', '.gif', '.pdf', '.txt'}
 file_path = Path(filename)

 # Check extension
 if file_path.suffix.lower() not in allowed_extensions:
 raise ValueError("File type not allowed")

 # Check size
 if file_path.stat().st_size > max_size:
 raise ValueError("File too large")

 return True
 ```

3. **Secure Configuration Management**
 ```python
 import os
 from pathlib import Path
 from typing import Optional

 class SecurityConfig:
 """Secure configuration management."""

 def __init__(self):
 self.secret_key = self._get_secret_key()
 self.database_url = self._get_database_url()
 self.debug = self._get_debug_mode()

 def _get_secret_key(self) -> str:
 key = os.getenv('SECRET_KEY')
 if not key:
 raise ValueError("SECRET_KEY environment variable required")
 if len(key) < 32:
 raise ValueError("SECRET_KEY must be at least 32 characters")
 return key

 def _get_database_url(self) -> str:
 url = os.getenv('DATABASE_URL')
 if not url:
 raise ValueError("DATABASE_URL environment variable required")
 return url

 def _get_debug_mode(self) -> bool:
 # Never enable debug in production
 return os.getenv('ENVIRONMENT', 'production').lower() == 'development'

 # Usage
 config = SecurityConfig()
 ```

### Phase 2: Authentication & Authorization (8-12 hours)

1. **Secure Authentication System**
 ```python
 import jwt
 import bcrypt
 from datetime import datetime, timedelta
 from typing import Optional, Dict, Any

 class AuthManager:
 """Secure authentication manager."""

 def __init__(self, secret_key: str):
 self.secret_key = secret_key
 self.algorithm = 'HS256'
 self.token_expiry = timedelta(hours=24)

 def hash_password(self, password: str) -> str:
 """Hash password securely."""
 if len(password) < 8:
 raise ValueError("Password must be at least 8 characters")

 salt = bcrypt.gensalt()
 return bcrypt.hashpw(password.encode('utf-8'), salt).decode('utf-8')

 def verify_password(self, password: str, hashed: str) -> bool:
 """Verify password against hash."""
 return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))

 def create_token(self, user_id: str, permissions: list = None) -> str:
 """Create JWT token."""
 payload = {
 'user_id': user_id,
 'permissions': permissions or [],
 'exp': datetime.utcnow() + self.token_expiry,
 'iat': datetime.utcnow()
 }
 return jwt.encode(payload, self.secret_key, algorithm=self.algorithm)

 def verify_token(self, token: str) -> Optional[Dict[Any, Any]]:
 """Verify and decode JWT token."""
 try:
 payload = jwt.decode(token, self.secret_key, algorithms=[self.algorithm])
 return payload
 except jwt.ExpiredSignatureError:
 return None
 except jwt.InvalidTokenError:
 return None

 # Rate limiting for login attempts
 from collections import defaultdict
 import time

 class RateLimiter:
 """Simple rate limiter for login attempts."""

 def __init__(self, max_attempts: int = 5, window_minutes: int = 15):
 self.max_attempts = max_attempts
 self.window_seconds = window_minutes * 60
 self.attempts = defaultdict(list)

 def is_allowed(self, identifier: str) -> bool:
 """Check if request is allowed."""
 now = time.time()

 # Clean old attempts
 self.attempts[identifier] = [
 attempt for attempt in self.attempts[identifier]
 if now - attempt < self.window_seconds
 ]

 # Check if under limit
 if len(self.attempts[identifier]) >= self.max_attempts:
 return False

 # Record attempt
 self.attempts[identifier].append(now)
 return True
 ```

2. **Authorization Decorators**
 ```python
 from functools import wraps
 from flask import request, jsonify, g

 def require_auth(f):
 """Decorator to require authentication."""
 @wraps(f)
 def decorated_function(*args, **kwargs):
 token = request.headers.get('Authorization')
 if not token:
 return jsonify({'error': 'No token provided'}), 401

 if token.startswith('Bearer '):
 token = token[7:]

 payload = auth_manager.verify_token(token)
 if not payload:
 return jsonify({'error': 'Invalid token'}), 401

 g.current_user = payload
 return f(*args, **kwargs)
 return decorated_function

 def require_permission(permission: str):
 """Decorator to require specific permission."""
 def decorator(f):
 @wraps(f)
 def decorated_function(*args, **kwargs):
 if not hasattr(g, 'current_user'):
 return jsonify({'error': 'Authentication required'}), 401

 user_permissions = g.current_user.get('permissions', [])
 if permission not in user_permissions:
 return jsonify({'error': 'Insufficient permissions'}), 403

 return f(*args, **kwargs)
 return decorated_function
 return decorator

 # Usage
 @app.route('/admin/users')
 @require_auth
 @require_permission('admin')
 def admin_users():
 return jsonify({'users': get_all_users()})
 ```

### Phase 3: Security Monitoring (4-6 hours)

1. **Security Event Logging**
 ```python
 import logging
 from datetime import datetime
 from typing import Optional

 # Configure security logger
 security_logger = logging.getLogger('security')
 security_handler = logging.FileHandler('security.log')
 security_formatter = logging.Formatter(
 '%(asctime)s - SECURITY - %(levelname)s - %(message)s'
 )
 security_handler.setFormatter(security_formatter)
 security_logger.addHandler(security_handler)
 security_logger.setLevel(logging.INFO)

 def log_security_event(event_type: str, user_id: Optional[str] = None, 
 ip_address: Optional[str] = None, **details):
 """Log security-related events."""
 event_data = {
 'event_type': event_type,
 'user_id': user_id,
 'ip_address': ip_address,
 'timestamp': datetime.utcnow().isoformat(),
 **details
 }

 security_logger.info(f"Security event: {event_type}", extra=event_data)

 # Usage examples
 def login_attempt(username: str, success: bool, ip_address: str):
 log_security_event(
 'login_attempt',
 user_id=username,
 ip_address=ip_address,
 success=success
 )

 def data_access(user_id: str, resource: str, action: str):
 log_security_event(
 'data_access',
 user_id=user_id,
 resource=resource,
 action=action
 )
 ```

2. **Automated Security Scanning**
 ```bash
 # Install security tools
 pip install bandit safety pip-audit

 # Create security check script
 #!/bin/bash
 echo "Running security analysis..."

 # Check code for security issues
 bandit -r . -f json -o bandit-report.json

 # Check dependencies for vulnerabilities
 safety check --json --output safety-report.json

 # Audit packages
 pip-audit --format=json --output=audit-report.json

 echo "Security analysis complete. Check reports for issues."
 ```
```

## Security Tools Setup

### Bandit Configuration
```yaml
# .bandit
skips: ['B101'] # Skip assert_used test
exclude_dirs: ['tests', 'venv']
```

### Pre-commit Security Hooks
```yaml
# .pre-commit-config.yaml
repos:
 - repo: https://github.com/PyCQA/bandit
 rev: 1.7.5
 hooks:
 - id: bandit
 args: ['-c', '.bandit']
 - repo: https://github.com/gitguardian/ggshield
 rev: v1.25.0
 hooks:
 - id: ggshield
 language: python
 stages: [commit]
```

## Security Checklist

### Code Security
- [ ] No SQL injection vulnerabilities
- [ ] No command injection risks
- [ ] Input validation on all user inputs
- [ ] Secure cryptographic practices
- [ ] No hardcoded secrets or credentials
- [ ] Proper error handling (no information disclosure)

### Authentication & Authorization
- [ ] Strong password requirements
- [ ] Secure session management
- [ ] Rate limiting on authentication endpoints
- [ ] Proper access control checks
- [ ] Multi-factor authentication (where appropriate)

### Configuration Security
- [ ] Environment variables for sensitive configuration
- [ ] Debug mode disabled in production
- [ ] Secure HTTP headers implemented
- [ ] HTTPS enforced
- [ ] Security logging enabled

### Dependencies
- [ ] All packages up to date
- [ ] No known vulnerable dependencies
- [ ] Minimal dependency footprint
- [ ] Dependencies from trusted sources only

## Interactive Security Workflow

**After analyzing your code, I'll:**

1. **Scan for Vulnerabilities**: Use automated tools to find security issues
2. **Prioritize Fixes**: Rank issues by severity and impact
3. **Provide Solutions**: Give specific code fixes for each vulnerability
4. **Implement Monitoring**: Set up security logging and monitoring

**Next Steps:**
"I've found [X] security issues in your code, including [Y] critical vulnerabilities. The highest priority fix is [specific issue] because [reason]. Shall I help you implement the secure solution?"

## Success Metrics

### Before Security Hardening
- Potential SQL injection vulnerabilities
- Weak authentication mechanisms
- No input validation
- Secrets in source code
- No security monitoring

### After Security Implementation
- All injection vulnerabilities fixed
- Strong authentication and authorization
- Comprehensive input validation
- Secure configuration management
- Active security monitoring and logging
- Regular security scanning in CI/CD

**Upon completion, I'll help you:**
- Fix all identified security vulnerabilities
- Implement secure coding practices
- Set up automated security scanning
- Create security monitoring and logging
- Establish ongoing security maintenance

Let me know about your application and I'll help you identify and fix security vulnerabilities to protect against common attacks!




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
