# Security Analysis Assistant

> **Purpose**: Identify and fix security vulnerabilities across any codebase  
> **Best For**: Copilot, ChatGPT, Claude, Agents  
> **Languages**: Any (JavaScript, Python, Go, Rust, Java, etc.)  
> **Last Updated**: 2025-12

---

## Mission

Help identify and fix **security vulnerabilities** in applications across any language or framework. Focus on practical, actionable findings that prevent real-world attacks.

---

## Guard Clauses

**If no code provided:**
```
NO_ACTIONABLE_INPUT

Please provide code or configuration to analyze:
- Source files
- Dependency manifests (package.json, requirements.txt, go.mod, etc.)
- Infrastructure configs (Dockerfile, terraform, k8s manifests)
- Specific security concerns
```

**If no security issues found:**
```
NO_SECURITY_ISSUES

✅ Security scan complete — no vulnerabilities detected.

Checks performed:
- Injection attacks: ✓
- Hardcoded secrets: ✓  
- Unsafe deserialization: ✓
- Vulnerable dependencies: ✓
- Authentication/authorization: ✓
- Cryptographic issues: ✓

Code appears secure for the analyzed scope.
```

---

## Quick Context Checklist

```
☐ Code to scan
☐ Dependencies (package.json, go.mod, Cargo.toml, etc.)
☐ Framework (React, Express, Django, Spring, etc.)
☐ Deployment environment (cloud, container, serverless)
☐ Compliance requirements (PCI, HIPAA, SOC2, etc.)
```

---

## Copy-Paste Security Prompts

### Prompt: Quick Security Scan
```text
Security scan this code:

{{CODE}}

Language: {{LANGUAGE}}

Check for:
1. Injection attacks (SQL, command, LDAP, XPath)
2. Hardcoded secrets (API keys, passwords, tokens)
3. Unsafe deserialization
4. Path traversal vulnerabilities
5. SSRF/CSRF risks
6. Insecure cryptography
7. Authentication/authorization flaws

Output severity as: 🔴 Critical | 🟠 High | 🟡 Medium | 🟢 Low

If clean: output `NO_SECURITY_ISSUES`
```

### Prompt: Dependency Audit
```text
Audit these dependencies for security vulnerabilities:

{{DEPENDENCY_FILE}}

Check for:
1. Known CVEs in any package
2. Outdated packages with security fixes available
3. Typosquatting/suspicious package names
4. Overly permissive version ranges
5. Unmaintained packages (no updates in 2+ years)

Output as table:
| Package | Version | Issue | Severity | CVE | Action |
```

### Prompt: Secrets Detection
```text
Scan this code/config for exposed secrets:

{{CODE}}

Look for:
1. API keys and tokens
2. Database credentials
3. Private keys and certificates
4. OAuth/JWT secrets
5. Cloud provider credentials (AWS, GCP, Azure)
6. Webhook URLs with tokens

For each finding, suggest how to externalize to environment variables or secret manager.
```

### Prompt: Auth/Authz Review
```text
Review this authentication/authorization code:

{{CODE}}

Check for:
1. Password storage (bcrypt/argon2/scrypt, not MD5/SHA1)
2. Token validation (expiry, signature, audience)
3. Session management (secure cookies, regeneration)
4. Privilege escalation vectors
5. IDOR (Insecure Direct Object Reference)
6. Rate limiting on auth endpoints
7. Multi-factor authentication implementation

Output findings with severity and specific fixes.
```

### Prompt: Infrastructure Security Review
```text
Review this infrastructure configuration:

{{CONFIG}}

Type: {{DOCKERFILE/TERRAFORM/K8S/CLOUDFORMATION}}

Check for:
1. Containers running as root
2. Overly permissive IAM/RBAC policies
3. Unencrypted data at rest/in transit
4. Public exposure of internal services
5. Missing network segmentation
6. Insecure default configurations
7. Missing resource limits

Output findings with remediation steps.
```

### Prompt: API Security Review
```text
Review this API endpoint for security:

{{CODE}}

Check for:
1. Input validation and sanitization
2. Authentication requirements
3. Authorization checks
4. Rate limiting
5. Response data exposure (over-fetching)
6. CORS configuration
7. Error message information leakage

Output findings with secure code examples.
```

### Prompt: AI/LLM Security Check
```text
Review this AI/LLM integration code for security:

{{CODE}}

Check for:
1. Prompt injection vulnerabilities
2. Sensitive data in prompts (PII, credentials)
3. Output sanitization before rendering
4. API key exposure
5. Rate limiting and cost controls
6. Model output validation
7. Jailbreak prevention measures

Critical for modern AI-integrated applications.
```

---

## Security Analysis Framework

### 1. **OWASP Top 10 Coverage**

| Category | Description | What to Check |
|----------|-------------|---------------|
| **A01: Broken Access Control** | Authorization failures | IDOR, privilege escalation, missing authz checks |
| **A02: Cryptographic Failures** | Data exposure | Weak encryption, plaintext secrets, bad TLS |
| **A03: Injection** | Untrusted data execution | SQL, NoSQL, OS command, LDAP injection |
| **A04: Insecure Design** | Architecture flaws | Missing threat modeling, unsafe patterns |
| **A05: Security Misconfiguration** | Bad defaults | Verbose errors, unnecessary features, weak headers |
| **A06: Vulnerable Components** | Outdated deps | Known CVEs, unmaintained packages |
| **A07: Auth Failures** | Identity issues | Weak passwords, session fixation, credential stuffing |
| **A08: Data Integrity Failures** | Untrusted data | Insecure deserialization, unsigned updates |
| **A09: Logging Failures** | Missing visibility | No audit logs, sensitive data in logs |
| **A10: SSRF** | Server-side requests | Unvalidated URLs, internal service access |

### 2. **Security Tools by Language**

| Language | Static Analysis | Dependency Scan | Secrets Detection |
|----------|-----------------|-----------------|-------------------|
| **JavaScript/TS** | ESLint security plugin, Semgrep | npm audit, Snyk | GitLeaks, TruffleHog |
| **Python** | Ruff (S rules), Bandit, Semgrep | pip-audit, Safety | GitLeaks, detect-secrets |
| **Go** | gosec, Semgrep | govulncheck | GitLeaks, TruffleHog |
| **Java** | SpotBugs, Semgrep | OWASP Dependency-Check | GitLeaks |
| **Rust** | cargo-audit, Semgrep | cargo-deny | GitLeaks |
| **C/C++** | Semgrep, cppcheck | - | GitLeaks |
| **Any** | Semgrep, CodeQL | Snyk, Dependabot | GitLeaks, TruffleHog |

### 3. **Common Vulnerability Patterns**

#### Injection Attacks
```
❌ VULNERABLE
query = "SELECT * FROM users WHERE id = " + userId
os.system("convert " + filename + " output.jpg")

✅ SECURE  
query = "SELECT * FROM users WHERE id = ?" // parameterized
subprocess.run(["convert", filename, "output.jpg"]) // no shell
```

#### Hardcoded Secrets
```
❌ VULNERABLE
apiKey = "sk-1234567890abcdef"
dbPassword = "supersecret123"

✅ SECURE
apiKey = os.environ["API_KEY"]
dbPassword = getSecret("db-password")  // from secret manager
```

#### Insecure Cryptography
```
❌ VULNERABLE
hashlib.md5(password)  // weak hash
DES.encrypt(data)       // weak cipher

✅ SECURE
bcrypt.hash(password)   // strong password hash
AES-256-GCM.encrypt(data)  // authenticated encryption
```

---

## Report Format

Generate a comprehensive security analysis and save as **two deliverables**:

### 1. Summary Report: `security-analysis-[YYYY-MM-DD].md`

```markdown
# Security Analysis Report

## Executive Summary
- **Overall Risk Level**: [Critical/High/Medium/Low]
- **Critical Vulnerabilities**: [Count]
- **High Priority Issues**: [Count]
- **Medium/Low Issues**: [Count]
- **Scope**: [What was analyzed]

## Risk Matrix

| Severity | Count | Examples |
|----------|-------|----------|
| 🔴 Critical | X | [Brief description] |
| 🟠 High | X | [Brief description] |
| 🟡 Medium | X | [Brief description] |
| 🟢 Low | X | [Brief description] |

## Top Priority Fixes
1. [Critical issue - link to detailed finding]
2. [High priority issue - link to detailed finding]
3. [Next priority - link to detailed finding]

## Dependency Vulnerabilities
| Package | Version | CVE | Severity | Fix Version |
|---------|---------|-----|----------|-------------|

## Recommendations
- **Immediate**: [Actions for critical/high issues]
- **Short-term**: [Actions for medium issues]
- **Long-term**: [Security improvements]

## Compliance Notes
- [Relevant compliance implications]
```

### 2. Per-Finding Details: `security-analysis-[YYYY-MM-DD]/`

Create individual files for each finding:

```markdown
# Finding: [Vulnerability Name]

## Summary
- **Severity**: 🔴 Critical / 🟠 High / 🟡 Medium / 🟢 Low
- **Category**: [OWASP category]
- **Location**: `file.ext:line`
- **CWE**: [CWE-XXX if applicable]

## Description
[Clear explanation of the vulnerability and why it's dangerous]

## Vulnerable Code
```language
// Current insecure implementation
[code snippet]
```

## Secure Fix
```language
// Remediated implementation with comments
[fixed code snippet]
```

## Attack Scenario
[How an attacker could exploit this]

## Verification Steps
1. [How to verify the fix works]
2. [Test cases to add]

## References
- [Link to relevant documentation]
- [OWASP reference]
```

---

## Severity Classification

| Level | Icon | Criteria | Response Time |
|-------|------|----------|---------------|
| **Critical** | 🔴 | Actively exploitable, data breach risk, RCE | Immediate |
| **High** | 🟠 | Significant risk, requires specific conditions | 24-48 hours |
| **Medium** | 🟡 | Limited impact, defense in depth issue | 1-2 weeks |
| **Low** | 🟢 | Best practice, minimal risk | Next sprint |

---

## Security Review Checklist

### Input Handling
- [ ] All user input validated and sanitized
- [ ] Parameterized queries for database operations
- [ ] File uploads restricted by type and size
- [ ] URL/redirect validation

### Authentication
- [ ] Strong password hashing (bcrypt/argon2)
- [ ] Secure session management
- [ ] MFA available for sensitive operations
- [ ] Account lockout after failed attempts

### Authorization
- [ ] Role-based access control implemented
- [ ] Resource ownership verified
- [ ] No IDOR vulnerabilities
- [ ] Principle of least privilege applied

### Data Protection
- [ ] Sensitive data encrypted at rest
- [ ] TLS 1.2+ for data in transit
- [ ] No secrets in code or logs
- [ ] PII handling compliant with regulations

### Infrastructure
- [ ] Security headers configured (CSP, HSTS, etc.)
- [ ] Dependencies up to date
- [ ] Containers not running as root
- [ ] Network segmentation in place

### Logging & Monitoring
- [ ] Security events logged
- [ ] No sensitive data in logs
- [ ] Alerting for suspicious activity
- [ ] Audit trail for compliance
