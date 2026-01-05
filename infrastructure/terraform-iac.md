# Terraform & Infrastructure as Code — IaC Patterns

> **Purpose**: Production-ready Terraform configurations and IaC best practices  
> **Best For**: Copilot, ChatGPT, Claude, Agents  
> **Scope**: Terraform, OpenTofu, multi-cloud infrastructure  
> **Last Updated**: 2026-01

---

## Mission

Help create **maintainable, secure, and scalable Infrastructure as Code** using Terraform. Focus on modular design, state management, and multi-environment patterns that work in real production scenarios.

---

## Guard Clauses

**If no infrastructure context provided:**
```
NO_INFRA_CONTEXT

Please provide infrastructure context:
- Cloud provider(s) (AWS, GCP, Azure, etc.)
- Resources to provision
- Environment requirements (dev/staging/prod)
- Or describe your infrastructure needs
```

**If configuration follows best practices:**
```
TERRAFORM_APPROVED

✅ Terraform configuration review complete — production ready.

Checks performed:
- Module structure: ✓ (proper organization)
- State management: ✓ (remote backend configured)
- Variables: ✓ (validated and documented)
- Security: ✓ (no hardcoded secrets, least privilege)
- Naming: ✓ (consistent conventions)

Configuration follows Terraform best practices.
```

---

## Quick Context Checklist

```
☐ Cloud provider(s)
☐ Resources to provision
☐ Environment (dev/staging/prod)
☐ State backend (S3, GCS, Azure Blob, etc.)
☐ Existing infrastructure to import
☐ Team size and workflow
☐ CI/CD integration needs
```

---

## Copy-Paste Prompts

### Prompt: Generate Terraform Configuration
```text
Generate Terraform configuration for:

Cloud: {{PROVIDER}} (AWS/GCP/Azure)
Resources: {{RESOURCES}}
Environment: {{ENV}}

Requirements:
- Region: {{REGION}}
- Naming convention: {{CONVENTION}}
- Tags required: {{TAGS}}
- Network: {{VPC_CIDR}} (or use existing: {{VPC_ID}})

Generate:
1. Provider configuration with version constraints
2. Backend configuration ({{BACKEND_TYPE}})
3. Variables with validation and descriptions
4. Main resource definitions
5. Outputs for important values
6. terraform.tfvars.example

Follow best practices:
- Use data sources for existing resources
- Implement proper tagging strategy
- Use locals for computed values
- Add lifecycle rules where appropriate
```

### Prompt: Review Terraform Code
```text
Review this Terraform configuration:

{{TERRAFORM_CODE}}

Check for:
1. **Structure & Organization**
   - Proper file organization
   - Module usage and composition
   - Variable and output definitions

2. **Security**
   - No hardcoded secrets
   - Least privilege IAM policies
   - Encryption enabled where applicable
   - Security groups properly scoped

3. **Reliability**
   - Resource dependencies explicit
   - Lifecycle rules for stateful resources
   - Prevent accidental destruction

4. **Maintainability**
   - Consistent naming conventions
   - Proper documentation
   - Variable validation
   - Sensible defaults

5. **Cost Optimization**
   - Right-sized resources
   - Spot/preemptible where applicable
   - Resource scheduling

Rate each: 🟢 Good | 🟡 Needs attention | 🔴 Critical issue
```

### Prompt: Create Reusable Module
```text
Create a reusable Terraform module for:

Purpose: {{MODULE_PURPOSE}}
Provider: {{PROVIDER}}

Module should support:
- Multiple environments via variables
- Optional features via feature flags
- Sensible defaults with override capability
- Proper output values for composition

Generate module structure:
```
modules/{{MODULE_NAME}}/
├── main.tf
├── variables.tf
├── outputs.tf
├── versions.tf
├── README.md
└── examples/
    └── basic/
        ├── main.tf
        └── terraform.tfvars
```

Include:
- Complete variable documentation
- Input validation where appropriate
- Example usage
- README with requirements and examples
```

### Prompt: Multi-Environment Setup
```text
Design multi-environment Terraform structure:

Environments: {{ENVIRONMENTS}} (dev, staging, prod)
Shared resources: {{SHARED}}
Per-environment resources: {{PER_ENV}}

Requirements:
- Minimize code duplication
- Environment-specific variables
- Shared modules
- State isolation per environment
- Easy promotion between environments

Generate:
1. Directory structure
2. Backend configuration per environment
3. Shared modules
4. Environment-specific tfvars
5. Workspace vs directory strategy recommendation
```

### Prompt: State Migration
```text
Plan Terraform state migration:

Current state: {{CURRENT_STATE}}
Target state: {{TARGET_STATE}}

Migration type:
- [ ] Local to remote backend
- [ ] Between remote backends
- [ ] Monolith to modules
- [ ] Import existing resources

Generate:
1. Pre-migration checklist
2. Backup procedures
3. Migration commands
4. Validation steps
5. Rollback plan
```

### Prompt: Import Existing Resources
```text
Import existing {{PROVIDER}} resources into Terraform:

Resources to import:
{{RESOURCE_LIST}}

For each resource:
1. Generate terraform import command
2. Create matching resource block
3. Run terraform plan to verify
4. Identify drift from actual state

Generate import script and resource definitions.
```

---

## Project Structure

### Recommended Layout
```
infrastructure/
├── modules/                    # Reusable modules
│   ├── networking/
│   │   ├── main.tf
│   │   ├── variables.tf
│   │   ├── outputs.tf
│   │   └── versions.tf
│   ├── compute/
│   └── database/
├── environments/               # Environment-specific configs
│   ├── dev/
│   │   ├── main.tf
│   │   ├── backend.tf
│   │   ├── variables.tf
│   │   ├── terraform.tfvars
│   │   └── outputs.tf
│   ├── staging/
│   └── prod/
├── shared/                     # Shared resources (DNS, etc.)
└── scripts/
    ├── init.sh
    └── plan.sh
```

### Alternative: Terragrunt Layout
```
infrastructure/
├── terragrunt.hcl              # Root config
├── modules/                    # Reusable modules
├── environments/
│   ├── dev/
│   │   ├── terragrunt.hcl
│   │   ├── networking/
│   │   │   └── terragrunt.hcl
│   │   └── app/
│   │       └── terragrunt.hcl
│   ├── staging/
│   └── prod/
└── _envcommon/                 # Shared terragrunt configs
```

---

## Provider Configuration

### AWS Provider
```hcl
terraform {
  required_version = ">= 1.6.0"
  
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
  
  backend "s3" {
    bucket         = "company-terraform-state"
    key            = "env/dev/terraform.tfstate"
    region         = "us-west-2"
    encrypt        = true
    dynamodb_table = "terraform-state-lock"
  }
}

provider "aws" {
  region = var.aws_region
  
  default_tags {
    tags = {
      Environment = var.environment
      Project     = var.project_name
      ManagedBy   = "terraform"
      Owner       = var.owner
    }
  }
}
```

### GCP Provider
```hcl
terraform {
  required_version = ">= 1.6.0"
  
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 5.0"
    }
  }
  
  backend "gcs" {
    bucket = "company-terraform-state"
    prefix = "env/dev"
  }
}

provider "google" {
  project = var.gcp_project
  region  = var.gcp_region
}
```

### Azure Provider
```hcl
terraform {
  required_version = ">= 1.6.0"
  
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 3.0"
    }
  }
  
  backend "azurerm" {
    resource_group_name  = "terraform-state-rg"
    storage_account_name = "companyterraformstate"
    container_name       = "tfstate"
    key                  = "dev.terraform.tfstate"
  }
}

provider "azurerm" {
  features {}
}
```

---

## Variables Best Practices

### Variable Definition with Validation
```hcl
variable "environment" {
  description = "Deployment environment (dev, staging, prod)"
  type        = string
  
  validation {
    condition     = contains(["dev", "staging", "prod"], var.environment)
    error_message = "Environment must be dev, staging, or prod."
  }
}

variable "instance_type" {
  description = "EC2 instance type"
  type        = string
  default     = "t3.micro"
  
  validation {
    condition     = can(regex("^t3\\.|^t4g\\.|^m5\\.|^m6i\\.", var.instance_type))
    error_message = "Instance type must be t3, t4g, m5, or m6i family."
  }
}

variable "allowed_cidr_blocks" {
  description = "CIDR blocks allowed to access the resources"
  type        = list(string)
  default     = []
  
  validation {
    condition = alltrue([
      for cidr in var.allowed_cidr_blocks : can(cidrhost(cidr, 0))
    ])
    error_message = "All elements must be valid CIDR blocks."
  }
}

variable "tags" {
  description = "Additional tags to apply to resources"
  type        = map(string)
  default     = {}
}
```

### Locals for Computed Values
```hcl
locals {
  # Combine default and custom tags
  common_tags = merge(
    {
      Environment = var.environment
      Project     = var.project_name
      ManagedBy   = "terraform"
    },
    var.tags
  )
  
  # Naming convention
  name_prefix = "${var.project_name}-${var.environment}"
  
  # Environment-specific settings
  is_production = var.environment == "prod"
  
  instance_count = local.is_production ? 3 : 1
  
  # Computed CIDR blocks
  private_subnets = [
    for i, az in var.availability_zones :
    cidrsubnet(var.vpc_cidr, 4, i)
  ]
}
```

---

## Resource Patterns

### Prevent Accidental Destruction
```hcl
resource "aws_db_instance" "main" {
  identifier = "${local.name_prefix}-db"
  # ... other config
  
  lifecycle {
    prevent_destroy = true
  }
}

resource "aws_s3_bucket" "important" {
  bucket = "${local.name_prefix}-data"
  
  lifecycle {
    prevent_destroy = true
  }
}
```

### Create Before Destroy
```hcl
resource "aws_instance" "web" {
  ami           = var.ami_id
  instance_type = var.instance_type
  
  lifecycle {
    create_before_destroy = true
  }
}
```

### Ignore Changes
```hcl
resource "aws_autoscaling_group" "main" {
  name                = "${local.name_prefix}-asg"
  desired_capacity    = var.desired_capacity
  min_size            = var.min_size
  max_size            = var.max_size
  
  # Ignore changes made by autoscaling
  lifecycle {
    ignore_changes = [desired_capacity]
  }
}
```

### Conditional Resource Creation
```hcl
resource "aws_cloudwatch_log_group" "main" {
  count = var.enable_logging ? 1 : 0
  
  name              = "/app/${local.name_prefix}"
  retention_in_days = var.log_retention_days
}

# Reference with conditional
resource "aws_ecs_task_definition" "main" {
  # ...
  
  dynamic "log_configuration" {
    for_each = var.enable_logging ? [1] : []
    content {
      log_driver = "awslogs"
      options = {
        awslogs-group  = aws_cloudwatch_log_group.main[0].name
        awslogs-region = var.aws_region
      }
    }
  }
}
```

### Dynamic Blocks
```hcl
resource "aws_security_group" "main" {
  name        = "${local.name_prefix}-sg"
  description = "Security group for ${var.project_name}"
  vpc_id      = var.vpc_id
  
  dynamic "ingress" {
    for_each = var.ingress_rules
    content {
      from_port   = ingress.value.from_port
      to_port     = ingress.value.to_port
      protocol    = ingress.value.protocol
      cidr_blocks = ingress.value.cidr_blocks
      description = ingress.value.description
    }
  }
  
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
  
  tags = local.common_tags
}
```

---

## State Management

### Remote State Data Source
```hcl
# Reference state from another configuration
data "terraform_remote_state" "networking" {
  backend = "s3"
  config = {
    bucket = "company-terraform-state"
    key    = "env/${var.environment}/networking/terraform.tfstate"
    region = "us-west-2"
  }
}

# Use outputs from remote state
resource "aws_instance" "web" {
  subnet_id = data.terraform_remote_state.networking.outputs.private_subnet_ids[0]
  # ...
}
```

### State Locking (DynamoDB for AWS)
```hcl
# Create state locking table (run once)
resource "aws_dynamodb_table" "terraform_locks" {
  name         = "terraform-state-lock"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "LockID"
  
  attribute {
    name = "LockID"
    type = "S"
  }
  
  tags = {
    Name      = "Terraform State Lock"
    ManagedBy = "terraform"
  }
}
```

---

## CI/CD Integration

### GitHub Actions Workflow
```yaml
name: Terraform

on:
  push:
    branches: [main]
    paths: ['infrastructure/**']
  pull_request:
    branches: [main]
    paths: ['infrastructure/**']

env:
  TF_VERSION: '1.6.0'
  AWS_REGION: 'us-west-2'

jobs:
  terraform:
    runs-on: ubuntu-latest
    defaults:
      run:
        working-directory: infrastructure/environments/dev
    
    steps:
      - uses: actions/checkout@v4
      
      - name: Setup Terraform
        uses: hashicorp/setup-terraform@v3
        with:
          terraform_version: ${{ env.TF_VERSION }}
      
      - name: Configure AWS Credentials
        uses: aws-actions/configure-aws-credentials@v4
        with:
          role-to-assume: ${{ secrets.AWS_ROLE_ARN }}
          aws-region: ${{ env.AWS_REGION }}
      
      - name: Terraform Format
        run: terraform fmt -check -recursive
      
      - name: Terraform Init
        run: terraform init
      
      - name: Terraform Validate
        run: terraform validate
      
      - name: Terraform Plan
        run: terraform plan -out=tfplan
        
      - name: Terraform Apply
        if: github.ref == 'refs/heads/main' && github.event_name == 'push'
        run: terraform apply -auto-approve tfplan
```

---

## Security Best Practices

### Sensitive Variables
```hcl
variable "database_password" {
  description = "Database master password"
  type        = string
  sensitive   = true
}

# Use in resource
resource "aws_db_instance" "main" {
  password = var.database_password
  # Password won't show in logs or plan output
}
```

### IAM Least Privilege
```hcl
# Specific permissions instead of wildcards
data "aws_iam_policy_document" "app" {
  statement {
    effect = "Allow"
    actions = [
      "s3:GetObject",
      "s3:PutObject",
    ]
    resources = [
      "${aws_s3_bucket.app.arn}/*"
    ]
  }
  
  statement {
    effect = "Allow"
    actions = [
      "s3:ListBucket",
    ]
    resources = [
      aws_s3_bucket.app.arn
    ]
  }
}
```

### Encryption
```hcl
resource "aws_s3_bucket" "main" {
  bucket = "${local.name_prefix}-data"
}

resource "aws_s3_bucket_server_side_encryption_configuration" "main" {
  bucket = aws_s3_bucket.main.id
  
  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm     = "aws:kms"
      kms_master_key_id = aws_kms_key.main.arn
    }
  }
}
```

---

## Report Template

```markdown
# Terraform Review — {{PROJECT}}

**Date**: {{DATE}}
**Environment**: {{ENV}}
**Provider**: {{PROVIDER}}

## Summary

| Category | Status | Issues |
|----------|--------|--------|
| Structure | 🟢/🟡/🔴 | {{COUNT}} |
| Security | 🟢/🟡/🔴 | {{COUNT}} |
| Reliability | 🟢/🟡/🔴 | {{COUNT}} |
| Maintainability | 🟢/🟡/🔴 | {{COUNT}} |

## Critical Issues
{{CRITICAL_ISSUES}}

## Recommendations
{{RECOMMENDATIONS}}

## Corrected Configuration
{{CORRECTED_HCL}}
```

---

## Best Practices Checklist

### Structure
- [ ] Logical file organization (main.tf, variables.tf, outputs.tf)
- [ ] Reusable modules for common patterns
- [ ] Consistent naming conventions
- [ ] Proper use of locals for computed values

### Security
- [ ] No hardcoded secrets (use variables + secret management)
- [ ] Sensitive variables marked as sensitive
- [ ] Least privilege IAM policies
- [ ] Encryption enabled for data at rest

### Reliability
- [ ] Remote state with locking
- [ ] State file encryption
- [ ] prevent_destroy for critical resources
- [ ] Explicit resource dependencies

### Operations
- [ ] terraform fmt applied
- [ ] terraform validate passes
- [ ] Meaningful output values
- [ ] Documentation in README

---

## Severity Guide

| Level | Icon | Examples |
|-------|------|----------|
| **Critical** | 🔴 | Hardcoded secrets, no state locking, wildcard IAM permissions |
| **High** | 🟠 | No encryption, missing prevent_destroy, no variable validation |
| **Medium** | 🟡 | Inconsistent naming, missing tags, no documentation |
| **Low** | 🟢 | Formatting issues, suboptimal structure |
