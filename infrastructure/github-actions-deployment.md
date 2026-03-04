# GitHub Actions — CI/CD & Deployment Workflows

> **Purpose**: Production-ready GitHub Actions workflows for CI/CD  
> **Best For**: Codex, Claude, ChatGPT, Copilot, Agents  
> **Scope**: Testing, building, deploying, security scanning  
> **Last Updated**: 2026-03

---

## Mission

Help create **robust, secure, and efficient GitHub Actions workflows** for continuous integration and deployment. Focus on best practices for testing, building, and deploying applications safely.

---

## Guard Clauses

**If no workflow context provided:**
```
NO_WORKFLOW_CONTEXT

Please provide workflow context:
- Application type (web app, library, API, etc.)
- Language/framework
- Deployment target (AWS, GCP, Vercel, K8s, etc.)
- Or describe what you want to automate
```

**If workflow is well-configured:**
```
WORKFLOW_APPROVED

✅ GitHub Actions workflow review complete — production ready.

Checks performed:
- Security: ✓ (secrets management, permissions)
- Efficiency: ✓ (caching, parallelization)
- Reliability: ✓ (error handling, timeouts)
- Best practices: ✓ (pinned versions, reusable workflows)

Workflow follows GitHub Actions best practices.
```

---

## Quick Context Checklist

```
☐ Application type and language
☐ Testing requirements
☐ Build process
☐ Deployment target(s)
☐ Environment variables needed
☐ Secrets required
☐ Branch protection rules
☐ Required reviewers/approvals
```

---

## Copy-Paste Prompts

### Prompt: Generate CI/CD Workflow
```text
Generate a GitHub Actions workflow for:

Application: {{APP_TYPE}}
Language: {{LANGUAGE}}
Framework: {{FRAMEWORK}}

Requirements:
- Tests: {{TEST_FRAMEWORK}}
- Build: {{BUILD_COMMAND}}
- Deploy to: {{DEPLOY_TARGET}}
- Environments: {{ENVIRONMENTS}}

Generate complete workflow with:
1. CI pipeline (lint, test, build)
2. CD pipeline (deploy to environments)
3. Security scanning
4. Caching for dependencies
5. Environment protection rules
6. Rollback strategy

Follow best practices:
- Pin action versions with SHA
- Use OIDC for cloud auth
- Implement proper secret handling
- Add status checks
```

### Prompt: Review Workflow
```text
Review this GitHub Actions workflow:

{{WORKFLOW_YAML}}

Check for:
1. **Security**
   - Actions pinned to SHA
   - Minimal permissions
   - Secret exposure risks
   - Third-party action trust

2. **Efficiency**
   - Caching implemented
   - Parallel jobs where possible
   - Conditional execution
   - Artifact management

3. **Reliability**
   - Timeout settings
   - Error handling
   - Retry logic
   - Status reporting

4. **Maintainability**
   - Reusable workflows
   - Clear job naming
   - Documentation
   - DRY principles

Rate each: 🟢 Good | 🟡 Needs attention | 🔴 Critical issue
```

### Prompt: Multi-Environment Deployment
```text
Create deployment workflow for multiple environments:

Environments: {{ENVIRONMENTS}} (dev, staging, prod)
Deployment target: {{TARGET}}
Approval required: {{APPROVALS}}

Requirements:
- Automatic deploy to dev on merge to main
- Manual approval for staging/prod
- Environment-specific secrets
- Rollback capability
- Slack/Discord notifications

Generate:
1. Reusable deployment workflow
2. Environment-specific workflow files
3. Environment protection rules
4. Required secrets configuration
```

### Prompt: Monorepo Workflow
```text
Create workflows for monorepo:

Structure:
{{STRUCTURE}}

Requirements:
- Only run affected projects
- Shared dependencies caching
- Per-project versioning
- Coordinated releases

Generate:
1. Change detection workflow
2. Per-project CI workflows
3. Release workflow
4. Dependency update workflow
```

---

## Workflow Templates

### Complete CI/CD Pipeline
```yaml
name: CI/CD Pipeline

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]
  workflow_dispatch:
    inputs:
      environment:
        description: 'Environment to deploy'
        required: true
        default: 'staging'
        type: choice
        options:
          - staging
          - production

concurrency:
  group: ${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: true

env:
  NODE_VERSION: '20'
  REGISTRY: ghcr.io
  IMAGE_NAME: ${{ github.repository }}

jobs:
  # ============================================
  # CI Jobs
  # ============================================
  
  lint:
    name: Lint
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@b4ffde65f46336ab88eb53be808477a3936bae11 # v4.1.1
      
      - name: Setup Node.js
        uses: actions/setup-node@60edb5dd545a775178f52524783378180af0d1f8 # v4.0.2
        with:
          node-version: ${{ env.NODE_VERSION }}
          cache: 'npm'
      
      - name: Install dependencies
        run: npm ci
      
      - name: Run linter
        run: npm run lint

  test:
    name: Test
    runs-on: ubuntu-latest
    services:
      postgres:
        image: postgres:16
        env:
          POSTGRES_PASSWORD: postgres
          POSTGRES_DB: test
        options: >-
          --health-cmd pg_isready
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5
        ports:
          - 5432:5432
    
    steps:
      - uses: actions/checkout@b4ffde65f46336ab88eb53be808477a3936bae11 # v4.1.1
      
      - name: Setup Node.js
        uses: actions/setup-node@60edb5dd545a775178f52524783378180af0d1f8 # v4.0.2
        with:
          node-version: ${{ env.NODE_VERSION }}
          cache: 'npm'
      
      - name: Install dependencies
        run: npm ci
      
      - name: Run tests
        run: npm test -- --coverage
        env:
          DATABASE_URL: postgresql://postgres:postgres@localhost:5432/test
      
      - name: Upload coverage
        uses: codecov/codecov-action@e28ff129e5465c2c0dcc6f003fc735cb6ae0c673 # v4.5.0
        with:
          token: ${{ secrets.CODECOV_TOKEN }}
          fail_ci_if_error: true

  security:
    name: Security Scan
    runs-on: ubuntu-latest
    permissions:
      security-events: write
    steps:
      - uses: actions/checkout@b4ffde65f46336ab88eb53be808477a3936bae11 # v4.1.1
      
      - name: Run Trivy vulnerability scanner
        uses: aquasecurity/trivy-action@062f2592684a31eb3aa050cc61e7ca1451cecd3d # v0.18.0
        with:
          scan-type: 'fs'
          format: 'sarif'
          output: 'trivy-results.sarif'
      
      - name: Upload Trivy scan results
        uses: github/codeql-action/upload-sarif@1b1aada464948af03b950897e5eb522f92603cc2 # v3.24.9
        with:
          sarif_file: 'trivy-results.sarif'

  build:
    name: Build
    runs-on: ubuntu-latest
    needs: [lint, test]
    permissions:
      contents: read
      packages: write
    outputs:
      image-tag: ${{ steps.meta.outputs.tags }}
      image-digest: ${{ steps.build.outputs.digest }}
    
    steps:
      - uses: actions/checkout@b4ffde65f46336ab88eb53be808477a3936bae11 # v4.1.1
      
      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@2b51285047da1547ffb1b2203d8be4c0af6b1f20 # v3.2.0
      
      - name: Login to Container Registry
        uses: docker/login-action@e92390c5fb421da1463c202d546fed0ec5c39f20 # v3.1.0
        with:
          registry: ${{ env.REGISTRY }}
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}
      
      - name: Extract metadata
        id: meta
        uses: docker/metadata-action@8e5442c4ef9f78752691e2d8f8d19755c6f78e81 # v5.5.1
        with:
          images: ${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}
          tags: |
            type=sha,prefix=
            type=ref,event=branch
            type=ref,event=pr
            type=semver,pattern={{version}}
      
      - name: Build and push
        id: build
        uses: docker/build-push-action@2cdde995de11925a030ce8070c3d77a52ffcf1c0 # v5.3.0
        with:
          context: .
          push: ${{ github.event_name != 'pull_request' }}
          tags: ${{ steps.meta.outputs.tags }}
          labels: ${{ steps.meta.outputs.labels }}
          cache-from: type=gha
          cache-to: type=gha,mode=max
          provenance: true
          sbom: true

  # ============================================
  # CD Jobs
  # ============================================
  
  deploy-staging:
    name: Deploy to Staging
    needs: [build, security]
    if: github.ref == 'refs/heads/main' && github.event_name == 'push'
    runs-on: ubuntu-latest
    environment:
      name: staging
      url: https://staging.example.com
    
    steps:
      - uses: actions/checkout@b4ffde65f46336ab88eb53be808477a3936bae11 # v4.1.1
      
      - name: Configure AWS credentials
        uses: aws-actions/configure-aws-credentials@e3dd6a429d7300a6a4c196c26e071d42e0343502 # v4.0.2
        with:
          role-to-assume: ${{ secrets.AWS_ROLE_ARN_STAGING }}
          aws-region: us-west-2
      
      - name: Deploy to ECS
        run: |
          aws ecs update-service \
            --cluster staging \
            --service app \
            --force-new-deployment

  deploy-production:
    name: Deploy to Production
    needs: [deploy-staging]
    if: github.event_name == 'workflow_dispatch' && inputs.environment == 'production'
    runs-on: ubuntu-latest
    environment:
      name: production
      url: https://example.com
    
    steps:
      - uses: actions/checkout@b4ffde65f46336ab88eb53be808477a3936bae11 # v4.1.1
      
      - name: Configure AWS credentials
        uses: aws-actions/configure-aws-credentials@e3dd6a429d7300a6a4c196c26e071d42e0343502 # v4.0.2
        with:
          role-to-assume: ${{ secrets.AWS_ROLE_ARN_PRODUCTION }}
          aws-region: us-west-2
      
      - name: Deploy to ECS
        run: |
          aws ecs update-service \
            --cluster production \
            --service app \
            --force-new-deployment
```

### Python CI Workflow
```yaml
name: Python CI

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: ['3.11', '3.12']
    
    steps:
      - uses: actions/checkout@b4ffde65f46336ab88eb53be808477a3936bae11 # v4.1.1
      
      - name: Install uv
        uses: astral-sh/setup-uv@v1
      
      - name: Set up Python ${{ matrix.python-version }}
        run: uv python install ${{ matrix.python-version }}
      
      - name: Install dependencies
        run: uv sync --all-extras --dev
      
      - name: Run linting
        run: uv run ruff check .
      
      - name: Run type checking
        run: uv run mypy .
      
      - name: Run tests
        run: uv run pytest --cov --cov-report=xml
      
      - name: Upload coverage
        uses: codecov/codecov-action@e28ff129e5465c2c0dcc6f003fc735cb6ae0c673 # v4.5.0
        if: matrix.python-version == '3.12'
```

### Kubernetes Deployment
```yaml
name: Deploy to Kubernetes

on:
  workflow_call:
    inputs:
      environment:
        required: true
        type: string
      image-tag:
        required: true
        type: string
    secrets:
      KUBE_CONFIG:
        required: true

jobs:
  deploy:
    runs-on: ubuntu-latest
    environment: ${{ inputs.environment }}
    
    steps:
      - uses: actions/checkout@b4ffde65f46336ab88eb53be808477a3936bae11 # v4.1.1
      
      - name: Set up kubectl
        uses: azure/setup-kubectl@3e0aec4d80787158d308d7b364cb1b702e7feb7f # v4.0.0
      
      - name: Configure kubeconfig
        run: |
          mkdir -p ~/.kube
          echo "${{ secrets.KUBE_CONFIG }}" | base64 -d > ~/.kube/config
      
      - name: Deploy with Helm
        run: |
          helm upgrade --install app ./charts/app \
            --namespace ${{ inputs.environment }} \
            --set image.tag=${{ inputs.image-tag }} \
            --values ./charts/app/values-${{ inputs.environment }}.yaml \
            --wait \
            --timeout 10m
      
      - name: Verify deployment
        run: |
          kubectl rollout status deployment/app -n ${{ inputs.environment }}
```

### Reusable Workflow
```yaml
# .github/workflows/reusable-deploy.yml
name: Reusable Deploy

on:
  workflow_call:
    inputs:
      environment:
        required: true
        type: string
      version:
        required: true
        type: string
    secrets:
      AWS_ROLE_ARN:
        required: true
    outputs:
      deploy-url:
        value: ${{ jobs.deploy.outputs.url }}

jobs:
  deploy:
    runs-on: ubuntu-latest
    environment: ${{ inputs.environment }}
    outputs:
      url: ${{ steps.deploy.outputs.url }}
    
    steps:
      - uses: actions/checkout@b4ffde65f46336ab88eb53be808477a3936bae11 # v4.1.1
      
      - name: Configure AWS credentials
        uses: aws-actions/configure-aws-credentials@e3dd6a429d7300a6a4c196c26e071d42e0343502 # v4.0.2
        with:
          role-to-assume: ${{ secrets.AWS_ROLE_ARN }}
          aws-region: us-west-2
      
      - name: Deploy
        id: deploy
        run: |
          # Deploy logic here
          echo "url=https://${{ inputs.environment }}.example.com" >> $GITHUB_OUTPUT
```

---

## Security Best Practices

### OIDC Authentication (No Long-Lived Secrets)
```yaml
# AWS
- name: Configure AWS credentials
  uses: aws-actions/configure-aws-credentials@v4
  with:
    role-to-assume: arn:aws:iam::123456789:role/github-actions
    aws-region: us-west-2

# GCP
- name: Authenticate to Google Cloud
  uses: google-github-actions/auth@v2
  with:
    workload_identity_provider: projects/123456/locations/global/workloadIdentityPools/github/providers/github
    service_account: github-actions@project.iam.gserviceaccount.com

# Azure
- name: Azure Login
  uses: azure/login@v2
  with:
    client-id: ${{ secrets.AZURE_CLIENT_ID }}
    tenant-id: ${{ secrets.AZURE_TENANT_ID }}
    subscription-id: ${{ secrets.AZURE_SUBSCRIPTION_ID }}
```

### Minimal Permissions
```yaml
# Default minimal permissions
permissions:
  contents: read

jobs:
  build:
    runs-on: ubuntu-latest
    permissions:
      contents: read
      packages: write  # Only for jobs that need it
```

### Pin Actions to SHA
```yaml
# ❌ Don't use tags (can be moved)
- uses: actions/checkout@v4

# ✅ Pin to commit SHA
- uses: actions/checkout@b4ffde65f46336ab88eb53be808477a3936bae11 # v4.1.1
```

### Secret Scanning
```yaml
- name: Check for secrets
  uses: trufflesecurity/trufflehog@main
  with:
    path: ./
    base: ${{ github.event.repository.default_branch }}
    head: HEAD
```

---

## Caching Strategies

### Node.js
```yaml
- uses: actions/setup-node@v4
  with:
    node-version: '20'
    cache: 'npm'  # Built-in caching
```

### Python with uv
```yaml
- name: Install uv
  uses: astral-sh/setup-uv@v1
  with:
    enable-cache: true
```

### Docker Layers
```yaml
- uses: docker/build-push-action@v5
  with:
    cache-from: type=gha
    cache-to: type=gha,mode=max
```

### Custom Cache
```yaml
- name: Cache dependencies
  uses: actions/cache@v4
  with:
    path: |
      ~/.cache/pip
      ~/.local/share/virtualenvs
    key: ${{ runner.os }}-deps-${{ hashFiles('**/requirements.txt') }}
    restore-keys: |
      ${{ runner.os }}-deps-
```

---

## Matrix Strategies

### Multi-Platform Build
```yaml
jobs:
  build:
    strategy:
      matrix:
        os: [ubuntu-latest, macos-latest, windows-latest]
        node: [18, 20, 22]
        exclude:
          - os: windows-latest
            node: 18
    runs-on: ${{ matrix.os }}
    steps:
      - uses: actions/setup-node@v4
        with:
          node-version: ${{ matrix.node }}
```

### Dynamic Matrix
```yaml
jobs:
  prepare:
    runs-on: ubuntu-latest
    outputs:
      matrix: ${{ steps.set-matrix.outputs.matrix }}
    steps:
      - id: set-matrix
        run: |
          echo "matrix=$(cat matrix.json)" >> $GITHUB_OUTPUT

  build:
    needs: prepare
    strategy:
      matrix: ${{ fromJson(needs.prepare.outputs.matrix) }}
```

---

## Notifications

### Slack Notification
```yaml
- name: Notify Slack
  if: always()
  uses: slackapi/slack-github-action@v1
  with:
    payload: |
      {
        "text": "Deployment ${{ job.status }}",
        "blocks": [
          {
            "type": "section",
            "text": {
              "type": "mrkdwn",
              "text": "*${{ github.repository }}*\nDeployment to ${{ inputs.environment }} ${{ job.status }}"
            }
          }
        ]
      }
  env:
    SLACK_WEBHOOK_URL: ${{ secrets.SLACK_WEBHOOK }}
```

### GitHub Deployment Status
```yaml
- name: Create deployment
  uses: chrnorm/deployment-action@v2
  id: deployment
  with:
    token: ${{ secrets.GITHUB_TOKEN }}
    environment: ${{ inputs.environment }}

- name: Update deployment status
  if: always()
  uses: chrnorm/deployment-status@v2
  with:
    token: ${{ secrets.GITHUB_TOKEN }}
    deployment-id: ${{ steps.deployment.outputs.deployment_id }}
    state: ${{ job.status }}
```

---

## Report Template

```markdown
# GitHub Actions Workflow Review — {{REPO}}

**Date**: {{DATE}}
**Workflows**: {{WORKFLOW_COUNT}}

## Summary

| Category | Status | Issues |
|----------|--------|--------|
| Security | 🟢/🟡/🔴 | {{COUNT}} |
| Efficiency | 🟢/🟡/🔴 | {{COUNT}} |
| Reliability | 🟢/🟡/🔴 | {{COUNT}} |
| Maintainability | 🟢/🟡/🔴 | {{COUNT}} |

## Security Issues
{{SECURITY_ISSUES}}

## Optimization Opportunities
{{OPTIMIZATIONS}}

## Recommended Changes
{{RECOMMENDATIONS}}
```

---

## Best Practices Checklist

### Security
- [ ] Actions pinned to SHA (not tags)
- [ ] Minimal permissions per job
- [ ] OIDC for cloud authentication
- [ ] Secrets not exposed in logs
- [ ] Third-party actions audited

### Efficiency
- [ ] Caching enabled
- [ ] Parallel jobs where possible
- [ ] Conditional execution
- [ ] Concurrency limits set

### Reliability
- [ ] Timeouts configured
- [ ] Retry on failure for flaky tests
- [ ] Status checks required
- [ ] Rollback strategy defined

### Maintainability
- [ ] Reusable workflows used
- [ ] Clear job/step naming
- [ ] Environment variables centralized
- [ ] Documentation included

---

## Severity Guide

| Level | Icon | Examples |
|-------|------|----------|
| **Critical** | 🔴 | Unpinned actions, secrets in logs, excessive permissions |
| **High** | 🟠 | No OIDC auth, missing security scans, no status checks |
| **Medium** | 🟡 | No caching, sequential jobs that could parallel |
| **Low** | 🟢 | Minor naming issues, missing comments |
