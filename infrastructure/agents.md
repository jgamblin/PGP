# Infrastructure Agents — AI Development Instructions

> **Purpose**: Agent instructions for infrastructure-related development tasks  
> **Best For**: Copilot, Cursor, Windsurf, Claude Agents  
> **Scope**: Kubernetes, Terraform, Docker, CI/CD, serverless, monitoring  
> **Last Updated**: 2026-01

---

## Overview

This file contains instructions for AI coding agents working on infrastructure-related tasks. Agents should follow these guidelines when working with containers, orchestration, infrastructure as code, CI/CD pipelines, and monitoring systems.

---

## Core Principles

### 1. Security First
- **Never expose secrets in code or logs**
- Use secret management (Vault, AWS Secrets Manager, K8s Secrets)
- Apply principle of least privilege
- Scan images and dependencies for vulnerabilities

### 2. Infrastructure as Code
- All infrastructure should be version controlled
- Prefer declarative over imperative
- Use modules/templates for reusability
- Document infrastructure decisions

### 3. Reliability
- Design for failure (redundancy, health checks)
- Implement proper monitoring and alerting
- Use rolling deployments with rollback capability
- Test disaster recovery procedures

---

## Agent Capabilities

### Kubernetes Tasks

When asked to work with Kubernetes:

```markdown
1. **Understand the context**
   - What namespace/cluster?
   - What workload type (Deployment, StatefulSet, Job)?
   - What are the resource requirements?
   - Are there existing patterns to follow?

2. **Apply best practices**
   - Use resource limits and requests
   - Configure health probes (liveness, readiness, startup)
   - Use ConfigMaps/Secrets for configuration
   - Apply appropriate security contexts

3. **Consider operations**
   - How will this be deployed (Helm, Kustomize, raw YAML)?
   - What monitoring/logging is needed?
   - How will updates be rolled out?
   - What's the rollback strategy?
```

### Terraform Tasks

When asked to work with Terraform:

```markdown
1. **Structure properly**
   - Use consistent file organization (main.tf, variables.tf, outputs.tf)
   - Create reusable modules
   - Use workspaces or separate state files for environments
   - Document variables and outputs

2. **State management**
   - Use remote state (S3, GCS, Terraform Cloud)
   - Enable state locking
   - Plan state migrations carefully
   - Never commit state files

3. **Security considerations**
   - Use data sources for sensitive values
   - Implement proper IAM policies
   - Enable encryption at rest
   - Use security groups/firewalls appropriately
```

### Docker Tasks

When asked to work with Docker:

```markdown
1. **Image optimization**
   - Use multi-stage builds
   - Choose appropriate base images (distroless, Alpine, slim)
   - Order layers for cache efficiency
   - Minimize image size

2. **Security hardening**
   - Run as non-root user
   - Use specific image tags (not :latest)
   - Scan for vulnerabilities
   - Remove unnecessary tools/packages

3. **Compose patterns**
   - Use networks for service isolation
   - Configure health checks
   - Use volumes appropriately
   - Handle secrets properly
```

### CI/CD Tasks

When asked to work with CI/CD:

```markdown
1. **Pipeline design**
   - Keep pipelines fast (parallelization, caching)
   - Fail fast on errors
   - Use matrix builds for multiple versions
   - Separate build, test, and deploy stages

2. **Security**
   - Use OIDC for cloud authentication (not long-lived keys)
   - Scan dependencies and code
   - Protect deployment secrets
   - Require approvals for production

3. **Best practices**
   - Pin action/image versions
   - Use reusable workflows
   - Implement proper tagging strategy
   - Configure appropriate timeouts
```

---

## Platform-Specific Guidelines

### Kubernetes

```yaml
# Always include these in Deployments
spec:
  replicas: 3  # HA by default
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 1
      maxUnavailable: 0
  template:
    spec:
      securityContext:
        runAsNonRoot: true
        runAsUser: 1000
        fsGroup: 1000
      containers:
        - name: app
          resources:
            requests:
              cpu: 100m
              memory: 128Mi
            limits:
              cpu: 500m
              memory: 512Mi
          livenessProbe:
            httpGet:
              path: /health
              port: 8080
            initialDelaySeconds: 10
            periodSeconds: 10
          readinessProbe:
            httpGet:
              path: /ready
              port: 8080
            initialDelaySeconds: 5
            periodSeconds: 5
```

### Terraform (AWS)

```hcl
# Standard module structure
terraform {
  required_version = ">= 1.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
  
  backend "s3" {
    bucket         = "terraform-state-bucket"
    key            = "project/terraform.tfstate"
    region         = "us-east-1"
    encrypt        = true
    dynamodb_table = "terraform-locks"
  }
}

# Always tag resources
locals {
  common_tags = {
    Environment = var.environment
    Project     = var.project_name
    ManagedBy   = "terraform"
    Owner       = var.owner
  }
}
```

### Docker

```dockerfile
# Multi-stage production Dockerfile
FROM node:20-slim AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production

FROM gcr.io/distroless/nodejs20-debian12
WORKDIR /app
COPY --from=builder /app/node_modules ./node_modules
COPY . .
USER nonroot:nonroot
EXPOSE 3000
CMD ["server.js"]
```

### GitHub Actions

```yaml
# Standard workflow patterns
name: CI/CD

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

permissions:
  contents: read
  id-token: write  # For OIDC

jobs:
  build:
    runs-on: ubuntu-latest
    timeout-minutes: 15
    steps:
      - uses: actions/checkout@v4
      
      - name: Setup Node
        uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: 'npm'
      
      - name: Install
        run: npm ci
      
      - name: Test
        run: npm test
      
      - name: Build
        run: npm run build
```

---

## Response Patterns

### When Creating Infrastructure

```markdown
## Infrastructure: [Component Name]

### Overview
- Purpose: [what this creates]
- Provider: [AWS/GCP/Azure/etc]
- Components: [list of resources]

### Prerequisites
- [Prerequisite 1]
- [Prerequisite 2]

### Configuration
```hcl/yaml
[Configuration code]
```

### Variables
| Variable | Type | Description | Default |
|----------|------|-------------|---------|
| | | | |

### Outputs
| Output | Description |
|--------|-------------|
| | |

### Security Considerations
- [Security item 1]
- [Security item 2]
```

### When Reviewing Infrastructure

```markdown
## Infrastructure Review

### Scope
- Files reviewed: [list]
- Platform: [K8s/Terraform/Docker/etc]

### Security Assessment
| Area | Status | Notes |
|------|--------|-------|
| Secrets management | | |
| Network security | | |
| IAM/RBAC | | |
| Encryption | | |

### Reliability Assessment
| Area | Status | Notes |
|------|--------|-------|
| High availability | | |
| Health checks | | |
| Resource limits | | |
| Rollback capability | | |

### Issues Found
1. [Severity] Issue description
   - Location:
   - Impact:
   - Fix:

### Recommendations
1. [Priority] Recommendation
   - Benefit:
   - Implementation:
```

### When Debugging Infrastructure

```markdown
## Debugging: [Issue Description]

### Symptoms
- [Observed behavior]

### Investigation Steps
1. [Step 1 and findings]
2. [Step 2 and findings]

### Root Cause
[Explanation of root cause]

### Resolution
```bash/yaml
[Commands or config changes]
```

### Prevention
- [How to prevent recurrence]
```

---

## Common Patterns

### High Availability

```markdown
When designing for HA:
- Use multiple replicas (3+ for quorum-based systems)
- Spread across availability zones
- Implement proper health checks
- Configure anti-affinity rules
- Use load balancers with health checks
- Plan for graceful degradation
```

### Zero-Downtime Deployments

```markdown
When implementing zero-downtime deploys:
- Use rolling updates with maxUnavailable: 0
- Ensure readiness probes are configured
- Handle connection draining
- Make database changes backward compatible
- Test rollback procedures
- Use blue-green or canary for critical services
```

### Cost Optimization

```markdown
When optimizing costs:
- Right-size resources based on metrics
- Use spot/preemptible instances where appropriate
- Implement autoscaling
- Clean up unused resources
- Use reserved capacity for predictable workloads
- Tag resources for cost allocation
```

---

## Integration with Other Prompts

Reference these related prompts for specific tasks:

| Task | Prompt |
|------|--------|
| Kubernetes patterns | [kubernetes.md](kubernetes.md) |
| Terraform IaC | [terraform-iac.md](terraform-iac.md) |
| Docker configuration | [docker-containerization.md](docker-containerization.md) |
| Docker audits | [docker-configuration-audit.md](docker-configuration-audit.md) |
| CI/CD pipelines | [github-actions-deployment.md](github-actions-deployment.md) |
| Serverless patterns | [serverless.md](serverless.md) |
| Monitoring setup | [monitoring-observability.md](monitoring-observability.md) |

---

## Quality Checklist

Before completing any infrastructure task, verify:

```markdown
- [ ] Security best practices applied
- [ ] Secrets not exposed in code
- [ ] Resource limits configured
- [ ] Health checks implemented
- [ ] Logging and monitoring configured
- [ ] Rollback strategy documented
- [ ] Cost implications considered
- [ ] Documentation updated
- [ ] Changes tested in non-production
- [ ] Peer review completed
```

---

*Last updated: 2026-01*
