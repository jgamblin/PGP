# AWS EC2 Deployment — Infrastructure Automation

> **Purpose**: Deploy applications to AWS EC2 with ARM-based instances  
> **Best For**: Copilot, ChatGPT, Claude, Agents  
> **Scope**: EC2, AMI selection, security groups, deployment scripts  
> **Last Updated**: 2025-12

---

## Mission

Help deploy applications to **AWS EC2** efficiently. Focus on ARM-based Graviton instances (t4g family) for better price-performance, with Debian/Ubuntu base images.

---

## Guard Clauses

**If no deployment requirements provided:**
```
NO_REQUIREMENTS_PROVIDED

Please share your deployment needs:
- Application type (web, API, worker)
- Expected traffic/load
- Budget constraints
- Region preference

I'll recommend the right EC2 setup.
```

**If setup looks good:**
```
SETUP_LOOKS_GOOD

✅ **Solid EC2 Configuration**

Your setup follows best practices:
- ARM instance (cost efficient) ✓
- Proper security groups ✓
- Appropriate instance size ✓

Minor suggestions (optional):
[list any refinements]
```

---

## Quick Context Checklist

```
☐ Application type and stack
☐ Traffic expectations
☐ Region requirements
☐ Budget constraints
☐ High availability needs
☐ Database requirements
```

---

## Copy-Paste Prompts

### Prompt: EC2 Setup Plan
```text
Create an EC2 deployment plan for:

Application: {{APP_DESCRIPTION}}
Stack: {{TECH_STACK}}
Expected traffic: {{TRAFFIC}}
Budget: {{BUDGET}}

Include:
1. Instance type recommendation (prefer t4g ARM)
2. AMI selection (Debian/Ubuntu)
3. Security group configuration
4. Storage requirements
5. Deployment script
```

### Prompt: Security Group Configuration
```text
Create security group rules for:

Application type: {{APP_TYPE}}
Needs: {{NEEDS}}

Consider:
- Minimal required ports
- SSH access restrictions
- Application ports
- HTTPS termination
```

### Prompt: Deployment Script
```text
Create a deployment script for EC2:

Application: {{APPLICATION}}
Instance: {{INSTANCE_TYPE}}
AMI: {{AMI}}

Include:
1. User data script for initial setup
2. Application deployment steps
3. systemd service configuration
4. Nginx/Caddy reverse proxy setup
```

### Prompt: Review EC2 Configuration
```text
Review this EC2 deployment configuration:

{{CONFIGURATION}}

Check for:
- Cost optimization (ARM instances)
- Security best practices
- Performance considerations
- Scalability options
```

---

## Instance Type Reference

### Recommended: ARM-Based (Graviton)

| Instance | vCPU | Memory | Use Case | Cost/hr* |
|----------|------|--------|----------|----------|
| t4g.nano | 2 | 0.5 GB | Dev/Test | ~$0.004 |
| t4g.micro | 2 | 1 GB | Light web | ~$0.008 |
| t4g.small | 2 | 2 GB | Small apps | ~$0.016 |
| t4g.medium | 2 | 4 GB | Medium apps | ~$0.034 |
| t4g.large | 2 | 8 GB | Production | ~$0.067 |
| t4g.xlarge | 4 | 16 GB | High traffic | ~$0.134 |

*Prices approximate, vary by region

### When to Use x86 (Intel/AMD)

| Scenario | Recommendation |
|----------|----------------|
| ARM-compatible app | Use t4g (40% cheaper) |
| Legacy x86 binaries | Use t3 |
| Specific software requirements | Check compatibility |

---

## AMI Selection

### Recommended Base Images

```bash
# Debian 12 ARM64 (preferred)
aws ec2 describe-images \
  --owners 136693071363 \
  --filters "Name=name,Values=debian-12-arm64-*" \
  --query 'sort_by(Images, &CreationDate)[-1].ImageId'

# Ubuntu 24.04 ARM64
aws ec2 describe-images \
  --owners 099720109477 \
  --filters "Name=name,Values=ubuntu/images/hvm-ssd/ubuntu-noble-24.04-arm64-server-*" \
  --query 'sort_by(Images, &CreationDate)[-1].ImageId'

# Amazon Linux 2023 ARM64
aws ec2 describe-images \
  --owners amazon \
  --filters "Name=name,Values=al2023-ami-*-arm64" \
  --query 'sort_by(Images, &CreationDate)[-1].ImageId'
```

### AMI Selection Table

| OS | ARM Support | Best For | Update Cadence |
|----|-------------|----------|----------------|
| Debian 12 | Excellent | Production servers | Stable |
| Ubuntu 24.04 | Excellent | General purpose | Regular |
| Amazon Linux 2023 | Excellent | AWS integration | Regular |

---

## Security Group Templates

### Web Application
```bash
# Create security group
aws ec2 create-security-group \
  --group-name web-app-sg \
  --description "Web application security group"

# Allow HTTPS
aws ec2 authorize-security-group-ingress \
  --group-name web-app-sg \
  --protocol tcp \
  --port 443 \
  --cidr 0.0.0.0/0

# Allow HTTP (redirect to HTTPS)
aws ec2 authorize-security-group-ingress \
  --group-name web-app-sg \
  --protocol tcp \
  --port 80 \
  --cidr 0.0.0.0/0

# Allow SSH (restrict to your IP)
aws ec2 authorize-security-group-ingress \
  --group-name web-app-sg \
  --protocol tcp \
  --port 22 \
  --cidr YOUR_IP/32
```

### API Server
```hcl
# Terraform example
resource "aws_security_group" "api" {
  name        = "api-server-sg"
  description = "API server security group"

  ingress {
    description = "HTTPS"
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    description = "SSH from bastion"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    security_groups = [aws_security_group.bastion.id]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}
```

---

## User Data Scripts

### Basic Web Server Setup
```bash
#!/bin/bash
set -e

# Update system
apt-get update && apt-get upgrade -y

# Install essentials
apt-get install -y \
  nginx \
  certbot \
  python3-certbot-nginx \
  fail2ban \
  ufw

# Configure firewall
ufw default deny incoming
ufw default allow outgoing
ufw allow ssh
ufw allow 'Nginx Full'
ufw --force enable

# Enable services
systemctl enable nginx fail2ban
systemctl start nginx fail2ban
```

### Application Server (Python/Node)
```bash
#!/bin/bash
set -e

# Update system
apt-get update && apt-get upgrade -y

# Install dependencies
apt-get install -y \
  python3 python3-pip python3-venv \
  nodejs npm \
  nginx \
  supervisor

# Create app user
useradd -m -s /bin/bash app

# Create app directory
mkdir -p /opt/app
chown app:app /opt/app

# Configure systemd service
cat > /etc/systemd/system/app.service << 'EOF'
[Unit]
Description=Application Service
After=network.target

[Service]
User=app
WorkingDirectory=/opt/app
ExecStart=/opt/app/venv/bin/python app.py
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
EOF

systemctl daemon-reload
systemctl enable app
```

---

## Deployment Scripts

### Full EC2 Launch Script
```bash
#!/bin/bash
set -e

# Configuration
INSTANCE_TYPE="t4g.small"
KEY_NAME="my-key"
SECURITY_GROUP="web-app-sg"
AMI_ID="ami-xxxxxxxxx"  # Debian 12 ARM64

# Launch instance
INSTANCE_ID=$(aws ec2 run-instances \
  --image-id $AMI_ID \
  --instance-type $INSTANCE_TYPE \
  --key-name $KEY_NAME \
  --security-groups $SECURITY_GROUP \
  --user-data file://user-data.sh \
  --tag-specifications 'ResourceType=instance,Tags=[{Key=Name,Value=web-app}]' \
  --query 'Instances[0].InstanceId' \
  --output text)

echo "Launched instance: $INSTANCE_ID"

# Wait for instance to be running
aws ec2 wait instance-running --instance-ids $INSTANCE_ID

# Get public IP
PUBLIC_IP=$(aws ec2 describe-instances \
  --instance-ids $INSTANCE_ID \
  --query 'Reservations[0].Instances[0].PublicIpAddress' \
  --output text)

echo "Instance running at: $PUBLIC_IP"
```

### Terraform Configuration
```hcl
# main.tf
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = var.region
}

resource "aws_instance" "web" {
  ami           = var.ami_id
  instance_type = "t4g.small"
  key_name      = var.key_name

  vpc_security_group_ids = [aws_security_group.web.id]

  user_data = file("user-data.sh")

  root_block_device {
    volume_size = 20
    volume_type = "gp3"
    encrypted   = true
  }

  tags = {
    Name        = "web-server"
    Environment = var.environment
  }
}

resource "aws_eip" "web" {
  instance = aws_instance.web.id
  domain   = "vpc"
}

output "public_ip" {
  value = aws_eip.web.public_ip
}
```

---

## Cost Optimization

### Savings Options

| Option | Savings | Commitment |
|--------|---------|------------|
| On-Demand | 0% | None |
| Spot Instances | 60-90% | Can be interrupted |
| Reserved (1yr) | ~40% | 1 year |
| Reserved (3yr) | ~60% | 3 years |
| Savings Plans | ~40% | 1-3 years |

### Cost-Saving Tips

```bash
# Use Spot Instances for non-critical workloads
aws ec2 run-instances \
  --instance-type t4g.small \
  --instance-market-options '{"MarketType":"spot"}'

# Enable detailed monitoring only if needed
# Use gp3 volumes instead of gp2 (cheaper + faster)
# Right-size instances based on actual usage
```

---

## Report Format

### Deployment Plan: `ec2-deployment-[YYYY-MM-DD].md`

```markdown
# EC2 Deployment Plan

## Application Overview
- **Name**: [Application name]
- **Stack**: [Tech stack]
- **Traffic**: [Expected load]

## Infrastructure

### Instance Configuration
- **Type**: t4g.small (ARM)
- **AMI**: Debian 12 ARM64
- **Region**: us-east-1
- **Storage**: 20GB gp3

### Security Groups
| Port | Protocol | Source | Purpose |
|------|----------|--------|---------|

### Estimated Costs
- Instance: $XX/month
- Storage: $XX/month
- Data transfer: $XX/month
- **Total**: $XX/month

## Deployment Steps
1. [ ] Create security groups
2. [ ] Launch EC2 instance
3. [ ] Configure application
4. [ ] Set up SSL/TLS
5. [ ] Configure monitoring

## Monitoring
- CloudWatch metrics
- Health checks
- Alerting rules
```

---

## Severity Guide

| Level | Icon | Examples |
|-------|------|----------|
| **Critical** | 🔴 | Open security groups, no encryption |
| **High** | 🟠 | Oversized instances, no backups |
| **Medium** | 🟡 | Missing monitoring, no auto-scaling |
| **Low** | 🟢 | Minor optimizations, tagging |
