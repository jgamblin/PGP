# Common Sections Reference — Infrastructure

> **Purpose**: Shared boilerplate for all infrastructure prompts  
> **Best For**: Codex, Claude, ChatGPT, Copilot, Agents  
> **Scope**: Shared reference sections for infrastructure prompt workflows  
> **Last Updated**: 2026-03
> **Usage**: Reference this file instead of duplicating content  

---

## Quick Context Checklist

Use this condensed checklist instead of the full "Inputs Required" section:

```
☐ Cloud provider (AWS, GCP, Azure)
☐ Infrastructure tool (Terraform, Pulumi, CDK)
☐ Container orchestration (K8s, ECS, etc.)
☐ CI/CD platform (GitHub Actions, GitLab, etc.)
☐ Environment (dev, staging, production)
☐ Current infrastructure state
☐ Pain points or constraints
```

---

## Standard Guard Clauses

Include these at the top of analysis output to handle edge cases:

### No Input Provided
```
NO_ACTIONABLE_INPUT

Unable to proceed without infrastructure context. Please provide:
- Terraform/K8s manifests to analyze, OR
- Infrastructure configuration files, OR
- Description of desired infrastructure state

Example: "Review my Kubernetes deployment for security issues"
```

### Empty Diff / No Changes
```
NO_CHANGES_DETECTED

No infrastructure changes found.

Checked:
- Terraform plan shows no changes
- No modified YAML/HCL files detected

Next steps:
- Verify you're on the correct branch
- Ensure changes are committed
- Try: `terraform plan` to see pending changes
```

### Analysis Complete - No Issues
```
NO_ISSUES_FOUND

✅ Infrastructure review complete — production ready.

Summary:
- Resources reviewed: {{RESOURCE_COUNT}}
- Checks performed: {{CHECK_TYPES}}
- Result: Configuration meets best practices

Recommendation: Proceed with deployment.
```

### Analysis Complete - With Findings
```
ANALYSIS_COMPLETE

📋 Found {{ISSUE_COUNT}} items requiring attention.

Breakdown:
- 🔴 Critical: {{CRITICAL_COUNT}}
- 🟠 High: {{HIGH_COUNT}}
- 🟡 Medium: {{MEDIUM_COUNT}}
- 🟢 Low: {{LOW_COUNT}}

See detailed findings below.
```

---

## Severity Levels

Use consistent severity across all infrastructure prompts:

| Level | Label | Criteria | Action |
|-------|-------|----------|--------|
| 🔴 | **Critical** | Security vulnerability, data exposure, service outage risk | Fix immediately before deploy |
| 🟠 | **High** | Reliability issues, significant cost impact, compliance risk | Fix before production deploy |
| 🟡 | **Medium** | Best practice violations, minor performance issues | Should fix, can be follow-up |
| 🟢 | **Low** | Documentation, naming conventions, optimization | Optional, track for later |

---

## Standard Output Formats

### Infrastructure Issue Format

```markdown
### 🔴 [Issue Title]

**Resource:** `resource_type.resource_name`
**File:** `path/to/file.tf:42`

**Problem:**
[Description of what's wrong]

**Current Configuration:**
```hcl
# Current problematic configuration
```

**Suggested Fix:**
```hcl
# Improved configuration
```

**Impact:**
- Security: [impact]
- Cost: [impact]
- Reliability: [impact]
```

### Terraform Plan Format

```markdown
### Planned Changes

| Action | Resource | Details |
|--------|----------|---------|
| ➕ Create | `aws_instance.web` | New EC2 instance |
| 🔄 Update | `aws_security_group.web` | Add ingress rule |
| ➖ Destroy | `aws_eip.old` | No longer needed |

**Risk Assessment:** [Low/Medium/High]
**Estimated Cost Impact:** [Monthly change]
```

---

## Report Template

Use this structure for comprehensive infrastructure reviews:

```markdown
## Infrastructure Review Report

### Summary
| Metric | Value |
|--------|-------|
| Resources Reviewed | X |
| Issues Found | X |
| Critical | X |
| High | X |
| Medium | X |
| Low | X |

### Environment
- Cloud Provider: [AWS/GCP/Azure]
- IaC Tool: [Terraform/Pulumi/CDK]
- Region(s): [regions]
- Environment: [dev/staging/prod]

### Security Assessment
| Check | Status | Notes |
|-------|--------|-------|
| Encryption at rest | ✅/❌ | |
| Encryption in transit | ✅/❌ | |
| IAM least privilege | ✅/❌ | |
| Network segmentation | ✅/❌ | |
| Secrets management | ✅/❌ | |

### Reliability Assessment
| Check | Status | Notes |
|-------|--------|-------|
| High availability | ✅/❌ | |
| Auto-scaling | ✅/❌ | |
| Backup strategy | ✅/❌ | |
| Disaster recovery | ✅/❌ | |

### Cost Analysis
| Resource Type | Current | Optimized | Savings |
|--------------|---------|-----------|---------|
| | | | |

### Issues Found
[List issues by severity]

### Recommendations
1. [Priority action items]
```

---

## Cloud-Specific Patterns

### AWS

```hcl
# Standard AWS resource patterns

# Always use encryption
resource "aws_s3_bucket" "example" {
  bucket = "my-bucket"
}

resource "aws_s3_bucket_server_side_encryption_configuration" "example" {
  bucket = aws_s3_bucket.example.id
  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "aws:kms"
    }
  }
}

# Always block public access
resource "aws_s3_bucket_public_access_block" "example" {
  bucket                  = aws_s3_bucket.example.id
  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}

# IAM least privilege
resource "aws_iam_policy" "example" {
  name = "minimal-policy"
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Action = [
          "s3:GetObject",
          "s3:PutObject"
        ]
        Resource = "${aws_s3_bucket.example.arn}/*"
      }
    ]
  })
}
```

### GCP

```hcl
# Standard GCP resource patterns

# Use workload identity
resource "google_service_account" "example" {
  account_id   = "example-sa"
  display_name = "Example Service Account"
}

resource "google_project_iam_member" "example" {
  project = var.project_id
  role    = "roles/storage.objectViewer"  # Least privilege
  member  = "serviceAccount:${google_service_account.example.email}"
}

# Enable audit logging
resource "google_project_iam_audit_config" "example" {
  project = var.project_id
  service = "allServices"
  
  audit_log_config {
    log_type = "ADMIN_READ"
  }
  audit_log_config {
    log_type = "DATA_READ"
  }
}
```

### Azure

```hcl
# Standard Azure resource patterns

# Use managed identities
resource "azurerm_user_assigned_identity" "example" {
  resource_group_name = azurerm_resource_group.example.name
  location            = azurerm_resource_group.example.location
  name                = "example-identity"
}

# Enable encryption
resource "azurerm_storage_account" "example" {
  name                     = "examplestorageacct"
  resource_group_name      = azurerm_resource_group.example.name
  location                 = azurerm_resource_group.example.location
  account_tier             = "Standard"
  account_replication_type = "GRS"
  
  min_tls_version                 = "TLS1_2"
  enable_https_traffic_only       = true
  allow_nested_items_to_be_public = false
  
  identity {
    type = "UserAssigned"
    identity_ids = [azurerm_user_assigned_identity.example.id]
  }
}
```

---

## Kubernetes Patterns

### Pod Security

```yaml
# Standard security context
apiVersion: v1
kind: Pod
spec:
  securityContext:
    runAsNonRoot: true
    runAsUser: 1000
    fsGroup: 1000
    seccompProfile:
      type: RuntimeDefault
  containers:
    - name: app
      securityContext:
        allowPrivilegeEscalation: false
        readOnlyRootFilesystem: true
        capabilities:
          drop:
            - ALL
```

### Resource Management

```yaml
# Always set resource requests and limits
resources:
  requests:
    cpu: 100m
    memory: 128Mi
  limits:
    cpu: 500m
    memory: 512Mi
```

### Health Checks

```yaml
# Always configure probes
livenessProbe:
  httpGet:
    path: /health
    port: 8080
  initialDelaySeconds: 10
  periodSeconds: 10
  timeoutSeconds: 5
  failureThreshold: 3

readinessProbe:
  httpGet:
    path: /ready
    port: 8080
  initialDelaySeconds: 5
  periodSeconds: 5
  timeoutSeconds: 3
  failureThreshold: 3

startupProbe:
  httpGet:
    path: /health
    port: 8080
  initialDelaySeconds: 0
  periodSeconds: 10
  timeoutSeconds: 5
  failureThreshold: 30
```

---

## CI/CD Patterns

### GitHub Actions

```yaml
# Standard workflow patterns
name: Deploy

on:
  push:
    branches: [main]

permissions:
  contents: read
  id-token: write  # OIDC

jobs:
  deploy:
    runs-on: ubuntu-latest
    timeout-minutes: 30
    environment: production
    
    steps:
      - uses: actions/checkout@v4
      
      - name: Configure AWS Credentials
        uses: aws-actions/configure-aws-credentials@v4
        with:
          role-to-assume: ${{ secrets.AWS_ROLE_ARN }}
          aws-region: us-east-1
      
      - name: Deploy
        run: |
          terraform init
          terraform apply -auto-approve
```

---

## Security Checklist

Every infrastructure review should check:

```markdown
- [ ] No secrets in code (use secret management)
- [ ] Encryption at rest enabled
- [ ] Encryption in transit (TLS 1.2+)
- [ ] IAM follows least privilege
- [ ] Network properly segmented
- [ ] Logging enabled
- [ ] Monitoring configured
- [ ] Backup strategy in place
- [ ] Firewall rules minimal
- [ ] Public access blocked where appropriate
```

---

## Cost Optimization Checklist

```markdown
- [ ] Right-sized instances
- [ ] Auto-scaling configured
- [ ] Spot/preemptible instances where appropriate
- [ ] Reserved capacity for steady-state
- [ ] Unused resources cleaned up
- [ ] Data lifecycle policies set
- [ ] Cross-region transfer minimized
- [ ] Resources tagged for cost allocation
```

---

## Reliability Checklist

```markdown
- [ ] Multi-AZ deployment
- [ ] Health checks configured
- [ ] Auto-healing enabled
- [ ] Graceful shutdown handling
- [ ] Circuit breakers implemented
- [ ] Retry logic with backoff
- [ ] Chaos testing performed
- [ ] Runbooks documented
```

---

*Last updated: 2026-01*
