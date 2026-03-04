# Docker Configuration Audit — Review & Validation

> **Purpose**: Audit and validate Docker configurations for production readiness  
> **Best For**: Codex, Claude, ChatGPT, Copilot, Agents  
> **Scope**: Dockerfile review, Compose validation, security audit, best practices  
> **Last Updated**: 2026-03

---

## Mission

Help audit and validate **existing Docker configurations** to ensure they follow best practices, are secure, efficient, and production-ready. Focus on identifying issues in Dockerfiles, docker-compose files, and overall container architecture.

---

## Guard Clauses

**If no Docker configuration provided:**
```
NO_DOCKER_CONFIG_PROVIDED

Please provide Docker configuration to audit:
- Dockerfile(s)
- docker-compose.yml
- .dockerignore
- Or describe your container setup
```

**If configuration looks good:**
```
DOCKER_CONFIG_APPROVED

✅ Docker configuration audit complete — production ready.

Checks performed:
- Security: ✓ (non-root, no secrets, minimal attack surface)
- Efficiency: ✓ (multi-stage, proper caching, slim base)
- Reliability: ✓ (health checks, restart policies, dependencies)
- Best practices: ✓ (labels, .dockerignore, version pinning)

Configuration follows Docker best practices.
```

---

## Quick Context Checklist

```
☐ Dockerfile(s) to review
☐ docker-compose.yml (if applicable)
☐ .dockerignore file
☐ Environment (dev/staging/prod)
☐ Deployment target (local, Kubernetes, ECS, etc.)
☐ Security requirements
```

---

## Copy-Paste Audit Prompts

### Prompt: Full Docker Audit
```text
Audit this Docker configuration for production readiness:

Dockerfile:
{{DOCKERFILE}}

docker-compose.yml:
{{COMPOSE_FILE}}

.dockerignore:
{{DOCKERIGNORE}}

Environment: {{ENVIRONMENT}}

Check for:
1. **Security Issues**
   - Running as root
   - Secrets in image/compose
   - Exposed sensitive ports
   - Privileged mode usage
   - Missing security options

2. **Efficiency Issues**
   - Large image size
   - Poor layer caching
   - Unnecessary dependencies
   - Missing multi-stage build
   - Alpine vs Debian choice

3. **Reliability Issues**
   - Missing health checks
   - No restart policies
   - Improper dependency order
   - Missing resource limits
   - Volume persistence issues

4. **Best Practice Violations**
   - Using :latest tags
   - Missing labels
   - No .dockerignore
   - ADD instead of COPY
   - Multiple processes per container

Rate each issue: 🔴 Critical | 🟠 High | 🟡 Medium | 🟢 Low

Output as `DOCKER_CONFIG_APPROVED` if no significant issues found.
```

### Prompt: Dockerfile Review
```text
Review this Dockerfile for issues:

{{DOCKERFILE}}

Target environment: {{ENVIRONMENT}}

Check:
1. Base image choice and version pinning
2. Multi-stage build usage
3. Layer ordering and caching
4. Non-root user configuration
5. Package installation (no-install-recommends, cleanup)
6. COPY vs ADD usage
7. Health check presence
8. Exposed ports
9. Entry point and CMD configuration
10. Build arguments and secrets handling

Provide fixed Dockerfile if issues found.
```

### Prompt: Docker Compose Review
```text
Review this docker-compose.yml for issues:

{{COMPOSE_FILE}}

Check:
1. **Service Configuration**
   - Image version pinning
   - Build context and caching
   - Port mappings (host exposure)
   - Environment variable handling
   
2. **Dependencies**
   - depends_on with conditions
   - Health check configuration
   - Startup order correctness
   
3. **Resources**
   - Memory limits
   - CPU limits
   - Restart policies
   
4. **Networking**
   - Network isolation
   - Exposed vs internal ports
   - DNS configuration
   
5. **Volumes**
   - Named vs bind mounts
   - Data persistence
   - Permission issues
   
6. **Security**
   - Secrets management
   - Read-only filesystems
   - Capability dropping

Provide fixed compose file if issues found.
```

### Prompt: Security-Focused Audit
```text
Security audit this Docker configuration:

{{DOCKERFILE_AND_COMPOSE}}

Check for vulnerabilities:
1. **Image Security**
   - Base image vulnerabilities (outdated?)
   - Running as root user
   - Unnecessary packages installed
   - Secrets baked into image
   
2. **Runtime Security**
   - Privileged mode
   - Excessive capabilities
   - Host network/PID/IPC usage
   - Writable root filesystem
   
3. **Secrets Management**
   - Hardcoded passwords
   - API keys in environment
   - Secrets in build args
   - Proper secrets mounting
   
4. **Network Security**
   - Unnecessary port exposure
   - Internal vs external networks
   - TLS configuration
   
5. **Resource Limits**
   - Memory limits (prevent DoS)
   - CPU limits
   - PID limits

Output security score: 🟢 Secure | 🟡 Needs Work | 🔴 Vulnerable
```

### Prompt: Performance Optimization
```text
Optimize this Docker configuration for performance:

{{DOCKERFILE}}

Current image size: {{SIZE}}
Build time: {{BUILD_TIME}}

Analyze:
1. **Image Size Reduction**
   - Base image choice
   - Multi-stage opportunities
   - Layer consolidation
   - Dependency pruning
   - Static binary options (Go, Rust)
   
2. **Build Speed**
   - Layer caching order
   - Parallel build stages
   - BuildKit features
   - Dependency caching
   
3. **Runtime Performance**
   - Startup time
   - Memory footprint
   - Process management
   - Health check efficiency

Provide optimized Dockerfile with size/time estimates.
```

### Prompt: Compose Service Architecture
```text
Review the service architecture in this compose file:

{{COMPOSE_FILE}}

Evaluate:
1. **Service Separation**
   - Single responsibility per container
   - Proper microservice boundaries
   - Shared vs dedicated databases
   
2. **Scaling Readiness**
   - Stateless services
   - Session handling
   - Database connections
   - Load balancing needs
   
3. **Development vs Production**
   - Environment-specific overrides
   - Volume mounting strategy
   - Debug vs production settings
   
4. **Logging & Monitoring**
   - Log driver configuration
   - Centralized logging setup
   - Metrics exposure
   
5. **Backup & Recovery**
   - Data volume strategy
   - Backup procedures
   - Disaster recovery

Provide architecture recommendations.
```

---

## Audit Checklists

### Dockerfile Checklist
```text
Base Image:
☐ Using official image
☐ Specific version tag (not :latest)
☐ Slim/minimal variant for production
☐ Appropriate for architecture (ARM/AMD)

Build Process:
☐ Multi-stage build (if applicable)
☐ Proper layer ordering (least→most changing)
☐ Dependencies before source code
☐ Combined RUN commands where logical
☐ Cache mounts for package managers

Security:
☐ Non-root USER directive
☐ No secrets in build args
☐ No hardcoded credentials
☐ Minimal packages (--no-install-recommends)
☐ Package cache cleaned (rm -rf /var/lib/apt/lists/*)

Runtime:
☐ WORKDIR set
☐ EXPOSE for documentation
☐ HEALTHCHECK defined
☐ Appropriate ENTRYPOINT/CMD
☐ Signal handling (exec form, tini)

Metadata:
☐ LABEL with maintainer
☐ LABEL with version
☐ Clear comments for complex steps
```

### Docker Compose Checklist
```text
Services:
☐ All images version pinned
☐ Build context minimal
☐ Health checks for all services
☐ Restart policies defined
☐ Resource limits set

Dependencies:
☐ depends_on with condition: service_healthy
☐ Correct startup order
☐ No circular dependencies

Networking:
☐ Custom networks defined
☐ Only necessary ports exposed to host
☐ Internal services not exposed

Volumes:
☐ Named volumes for persistent data
☐ Bind mounts only for development
☐ No sensitive data in bind mounts

Environment:
☐ Using env_file for secrets
☐ No hardcoded passwords
☐ Appropriate defaults

Production:
☐ No development tools in prod compose
☐ Logging configured
☐ Proper scale settings
```

---

## Common Issues & Fixes

### Dockerfile Issues

| Issue | Bad | Good |
|-------|-----|------|
| Latest tag | `FROM node:latest` | `FROM node:22-slim-bookworm` |
| Running as root | No USER directive | `USER app` |
| Poor caching | COPY . . first | COPY package*.json first |
| Large image | Full base image | Multi-stage + slim base |
| Secrets in build | `ARG PASSWORD` | Use secrets mount |
| No health check | Missing HEALTHCHECK | Add HEALTHCHECK directive |
| ADD for local files | `ADD . .` | `COPY . .` |
| Shell form | `CMD npm start` | `CMD ["npm", "start"]` |

### Docker Compose Issues

| Issue | Bad | Good |
|-------|-----|------|
| No version pin | `image: postgres` | `image: postgres:16-bookworm` |
| Simple depends_on | `depends_on: [db]` | `depends_on: db: condition: service_healthy` |
| Host port exposure | `ports: ["5432:5432"]` | `expose: ["5432"]` (internal only) |
| No health check | Missing healthcheck | Add healthcheck with test |
| Hardcoded secrets | `PASSWORD=secret` | Use env_file or secrets |
| No restart policy | Missing restart | `restart: unless-stopped` |
| No resource limits | Missing limits | Add memory/cpu limits |
| Bind mount in prod | `volumes: [./data:/data]` | Named volume |

---

## Security Hardening

### Dockerfile Security
```dockerfile
# Pin specific versions
FROM python:3.12.1-slim-bookworm@sha256:abc123...

# Create non-root user
RUN groupadd --gid 1000 app && \
    useradd --uid 1000 --gid 1000 --shell /bin/bash app

# Install only what's needed
RUN apt-get update && apt-get install -y --no-install-recommends \
    required-package \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean

# Use secrets for build-time secrets (BuildKit)
RUN --mount=type=secret,id=npmrc,target=/root/.npmrc npm ci

# Set filesystem permissions
COPY --chown=app:app . .

# Switch to non-root
USER app

# Read-only root filesystem compatibility
ENV HOME=/tmp
```

### Docker Compose Security
```yaml
services:
  app:
    image: myapp:1.0.0
    read_only: true  # Read-only root filesystem
    security_opt:
      - no-new-privileges:true  # Prevent privilege escalation
    cap_drop:
      - ALL  # Drop all capabilities
    cap_add:
      - NET_BIND_SERVICE  # Add only what's needed
    tmpfs:
      - /tmp  # Writable temp directory
    secrets:
      - db_password
    deploy:
      resources:
        limits:
          memory: 512M
          cpus: '0.5'

secrets:
  db_password:
    file: ./secrets/db_password.txt  # Or external: true for swarm
```

---

## Resource Limits Reference

### Memory Limits
```yaml
services:
  app:
    deploy:
      resources:
        limits:
          memory: 512M      # Hard limit
        reservations:
          memory: 256M      # Guaranteed minimum
    # For docker-compose (non-swarm)
    mem_limit: 512m
    mem_reservation: 256m
```

### CPU Limits
```yaml
services:
  app:
    deploy:
      resources:
        limits:
          cpus: '0.5'       # 50% of one CPU
        reservations:
          cpus: '0.25'      # Guaranteed minimum
    # For docker-compose (non-swarm)
    cpus: 0.5
```

### Recommended Limits by Service Type
| Service Type | Memory | CPU | Notes |
|--------------|--------|-----|-------|
| Web app (Node/Python) | 256M-512M | 0.25-0.5 | Adjust for load |
| Database (PostgreSQL) | 512M-2G | 0.5-2 | Depends on data size |
| Cache (Redis) | 128M-512M | 0.25 | Based on cache size |
| Queue worker | 256M-512M | 0.25-0.5 | Based on job complexity |
| Static server (nginx) | 64M-128M | 0.1-0.25 | Very lightweight |

---

## Report Template

```markdown
# Docker Configuration Audit Report

**Date**: {{DATE}}
**Environment**: {{ENVIRONMENT}}
**Auditor**: {{AUDITOR}}

## Summary

| Category | Status | Issues |
|----------|--------|--------|
| Security | 🟢/🟡/🔴 | {{COUNT}} |
| Efficiency | 🟢/🟡/🔴 | {{COUNT}} |
| Reliability | 🟢/🟡/🔴 | {{COUNT}} |
| Best Practices | 🟢/🟡/🔴 | {{COUNT}} |

**Overall Score**: {{SCORE}}/100

## Critical Issues (Fix Immediately)

| Issue | Location | Risk | Fix |
|-------|----------|------|-----|

## High Priority Issues

| Issue | Location | Risk | Fix |
|-------|----------|------|-----|

## Medium/Low Priority

| Issue | Location | Recommendation |
|-------|----------|----------------|

## Dockerfile Analysis

- **Base Image**: {{IMAGE}}
- **Final Size**: {{SIZE}}
- **Layers**: {{COUNT}}
- **Non-root User**: ✅/❌
- **Health Check**: ✅/❌
- **Multi-stage**: ✅/❌

## Compose Analysis

- **Services**: {{COUNT}}
- **Networks**: {{NETWORKS}}
- **Volumes**: {{VOLUMES}}
- **All Health Checks**: ✅/❌
- **Resource Limits**: ✅/❌
- **Secrets Management**: ✅/❌

## Recommended Changes

### Dockerfile
```dockerfile
{{FIXED_DOCKERFILE}}
```

### docker-compose.yml
```yaml
{{FIXED_COMPOSE}}
```

## Validation Commands

```bash
# Test build
docker build -t myapp:test .

# Scan for vulnerabilities
docker scout cves myapp:test

# Test compose
docker compose config
docker compose up -d
docker compose ps
```
```

---

## Severity Guide

| Level | Icon | Examples |
|-------|------|----------|
| **Critical** | 🔴 | Running as root, secrets in image, privileged mode, no resource limits in prod |
| **High** | 🟠 | :latest tags, no health checks, exposed database ports, missing restart policy |
| **Medium** | 🟡 | Large image size, poor caching, missing .dockerignore, shell form CMD |
| **Low** | 🟢 | Missing labels, suboptimal base image, minor ordering issues |

---

## Quick Validation Commands

```bash
# Validate Dockerfile syntax
docker build --check .

# Validate compose file
docker compose config

# Check image for vulnerabilities
docker scout cves myimage:tag
trivy image myimage:tag

# Analyze image layers
docker history myimage:tag
dive myimage:tag

# Check running container security
docker inspect --format='{{.Config.User}}' container_name
docker inspect --format='{{.HostConfig.Privileged}}' container_name

# Test health check
docker inspect --format='{{.State.Health.Status}}' container_name
```
