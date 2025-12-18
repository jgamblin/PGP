# CI/CD Pipeline Analysis — DevOps Automation

> **Purpose**: Set up and optimize CI/CD pipelines  
> **Best For**: Copilot, ChatGPT, Claude, Agents  
> **Platforms**: GitHub Actions, GitLab CI, CircleCI, Jenkins  
> **Last Updated**: 2025-12

---

## Mission

Help set up, analyze, and optimize **CI/CD pipelines** for any project. Focus on security, speed, reliability, and developer experience.

---

## Guard Clauses

**If no pipeline config provided:**
```
NO_PIPELINE_CONFIG

Please provide CI/CD configuration to analyze:
- GitHub Actions workflow (.github/workflows/*.yml)
- GitLab CI config (.gitlab-ci.yml)
- Jenkinsfile or other CI config
- Or describe what you want to set up
```

**If pipeline looks good:**
```
PIPELINE_OPTIMIZED

✅ CI/CD pipeline analysis complete — no major issues.

Checks performed:
- Security: secrets handling, dependency scanning ✓
- Performance: caching, parallelization ✓
- Reliability: error handling, retries ✓
- Best practices: artifact management, notifications ✓

Pipeline is well-configured.
```

---

## Quick Context Checklist

```
☐ Current CI/CD config files
☐ Project language/framework
☐ Deployment target (cloud, container, serverless)
☐ Current pain points (slow builds, flaky tests)
```

---

## Copy-Paste CI/CD Prompts

### Prompt: Create GitHub Actions Workflow
```text
Create a GitHub Actions CI/CD workflow for:

Project type: {{PROJECT_TYPE}}
Language: {{LANGUAGE}}
Framework: {{FRAMEWORK}}

Include:
1. Lint and format check
2. Run tests with coverage
3. Security scanning
4. Build artifact
5. Deploy to {{TARGET}} (on main branch)

Use caching for dependencies. Support PR checks.
```

### Prompt: Optimize Pipeline Speed
```text
Optimize this CI/CD pipeline for speed:

{{PIPELINE_CONFIG}}

Current build time: {{CURRENT_TIME}}

Suggest:
1. Caching strategies
2. Parallelization opportunities
3. Unnecessary steps to remove
4. Matrix builds for multi-version testing
5. Conditional job execution

Target: Reduce build time by 50%+
```

### Prompt: Add Security Scanning
```text
Add security scanning to this pipeline:

{{PIPELINE_CONFIG}}

Add:
1. Dependency vulnerability scanning
2. SAST (Static Application Security Testing)
3. Secret detection
4. Container image scanning (if applicable)
5. SBOM generation

Use free/open-source tools where possible.
```

### Prompt: Fix Flaky Pipeline
```text
Debug this flaky CI/CD pipeline:

{{PIPELINE_CONFIG}}

Symptoms: {{SYMPTOMS}}
Failure rate: {{FAILURE_RATE}}

Identify:
1. Race conditions
2. Resource constraints
3. External dependency issues
4. Timeout problems
5. Order-dependent tests

Provide fixes with retry strategies.
```

### Prompt: Add Deployment Stage
```text
Add deployment to this pipeline:

{{PIPELINE_CONFIG}}

Deploy to: {{TARGET}}
Environment: {{ENVIRONMENT}}

Include:
1. Environment-specific configuration
2. Pre-deployment checks
3. Deployment strategy (rolling/blue-green/canary)
4. Post-deployment verification
5. Rollback capability

Use environment secrets securely.
```

---

## CI/CD Best Practices

### 1. **Pipeline Structure**

```yaml
# Recommended GitHub Actions structure
name: CI/CD

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Lint
        run: # linting commands

  test:
    runs-on: ubuntu-latest
    needs: lint  # Run after lint passes
    steps:
      - uses: actions/checkout@v4
      - name: Test
        run: # test commands

  build:
    runs-on: ubuntu-latest
    needs: test
    steps:
      - uses: actions/checkout@v4
      - name: Build
        run: # build commands

  deploy:
    runs-on: ubuntu-latest
    needs: build
    if: github.ref == 'refs/heads/main'
    steps:
      - name: Deploy
        run: # deploy commands
```

### 2. **Security Checklist**

- [ ] Secrets stored in CI/CD secrets manager (not in code)
- [ ] Least privilege for deployment credentials
- [ ] Dependency scanning enabled
- [ ] No sensitive data in logs
- [ ] Protected branches require CI pass
- [ ] Code signing for releases

### 3. **Performance Optimization**

| Technique | Impact | Implementation |
|-----------|--------|----------------|
| **Dependency caching** | High | Cache node_modules, .venv, etc. |
| **Parallelization** | High | Split tests, matrix builds |
| **Incremental builds** | Medium | Only rebuild changed components |
| **Artifact reuse** | Medium | Share build outputs between jobs |
| **Selective triggers** | Medium | Path filters, skip CI for docs |

### 4. **Common Tools by Language**

| Language | Lint | Test | Security |
|----------|------|------|----------|
| **JavaScript/TS** | ESLint, Prettier | Jest, Vitest | npm audit, Snyk |
| **Python** | Ruff | pytest | pip-audit, Bandit |
| **Go** | golangci-lint | go test | govulncheck, gosec |
| **Java** | Checkstyle, SpotBugs | JUnit | OWASP Dependency-Check |
| **Rust** | clippy, rustfmt | cargo test | cargo-audit |

---

## Report Format

### Pipeline Analysis Report: `ci-cd-analysis-[YYYY-MM-DD].md`

```markdown
# CI/CD Pipeline Analysis

## Summary
- **Platform**: [GitHub Actions/GitLab CI/etc.]
- **Build Time**: [Current average]
- **Reliability**: [Pass rate %]
- **Security Score**: [High/Medium/Low]

## Issues Found

| Issue | Severity | Impact | Fix |
|-------|----------|--------|-----|
| [Issue] | 🔴/🟠/🟡/🟢 | [Description] | [Solution] |

## Recommendations

### Immediate (This Week)
1. [High-impact fix]
2. [Security improvement]

### Short-term (This Month)
1. [Performance optimization]
2. [Reliability improvement]

### Long-term
1. [Architecture improvement]
2. [Advanced automation]

## Optimized Configuration
[Provide improved pipeline config]
```

---

## Severity Levels

| Level | Icon | Examples |
|-------|------|----------|
| **Critical** | 🔴 | Secrets exposed, no security scanning, broken deploys |
| **High** | �� | No caching, sequential when parallel possible, flaky tests |
| **Medium** | 🟡 | Missing notifications, no artifact retention policy |
| **Low** | 🟢 | Suboptimal caching, verbose logging |
