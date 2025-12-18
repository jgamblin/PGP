# Docker Containerization — Container Best Practices

> **Purpose**: Build efficient, secure Docker containers  
> **Best For**: Copilot, ChatGPT, Claude, Agents  
> **Scope**: Dockerfiles, multi-stage builds, compose, security  
> **Last Updated**: 2025-12

---

## Mission

Help create **production-ready Docker containers**. Focus on multi-stage builds, Debian/Ubuntu base images, security best practices, and efficient caching.

---

## Guard Clauses

**If no application details provided:**
```
NO_DETAILS_PROVIDED

Please share your application details:
- Language/framework (Python, Node, Go, etc.)
- Dependencies
- Build requirements
- Runtime needs

I'll create an optimized Dockerfile.
```

**If Dockerfile looks good:**
```
DOCKERFILE_LOOKS_GOOD

✅ **Solid Container Configuration**

Your Dockerfile follows best practices:
- Multi-stage build ✓
- Non-root user ✓
- Minimal base image ✓
- Proper caching ✓

Minor suggestions (optional):
[list any refinements]
```

---

## Quick Context Checklist

```
☐ Application language/framework
☐ Build dependencies vs runtime
☐ Exposed ports
☐ Environment variables needed
☐ Volume/data requirements
☐ Health check endpoint
```

---

## Copy-Paste Prompts

### Prompt: Create Dockerfile
```text
Create a production Dockerfile for:

Language: {{LANGUAGE}}
Framework: {{FRAMEWORK}}
Build command: {{BUILD_COMMAND}}
Start command: {{START_COMMAND}}

Requirements:
1. Multi-stage build
2. Debian/Ubuntu base image
3. Non-root user
4. Proper layer caching
5. Health check
```

### Prompt: Optimize Dockerfile
```text
Optimize this Dockerfile for production:

{{DOCKERFILE}}

Focus on:
- Reducing image size
- Improving build cache
- Security hardening
- Multi-stage if beneficial
```

### Prompt: Docker Compose Setup
```text
Create a docker-compose.yml for:

Services: {{SERVICES}}
Databases: {{DATABASES}}
Requirements: {{REQUIREMENTS}}

Include:
- Health checks
- Volume mounts
- Environment variables
- Network configuration
```

### Prompt: Review Docker Configuration
```text
Review this Docker configuration for issues:

{{DOCKERFILE_OR_COMPOSE}}

Check for:
- Security vulnerabilities
- Build efficiency
- Best practices
- Production readiness
```

---

## Base Image Selection

### Recommended Base Images

| Language | Base Image | Size | Notes |
|----------|------------|------|-------|
| Python | `python:3.12-slim-bookworm` | ~150MB | Debian-based |
| Node.js | `node:22-slim-bookworm` | ~200MB | Debian-based |
| Go | `golang:1.22` → `debian:bookworm-slim` | ~80MB | Multi-stage |
| Ruby | `ruby:3.3-slim-bookworm` | ~200MB | Debian-based |
| Java | `eclipse-temurin:21-jre-jammy` | ~250MB | Ubuntu-based |
| Rust | `rust:1.75` → `debian:bookworm-slim` | ~80MB | Multi-stage |
| Generic | `debian:bookworm-slim` | ~80MB | Minimal |

### Image Variants

| Variant | Use Case | Example |
|---------|----------|---------|
| `-slim` | Production (recommended) | `python:3.12-slim-bookworm` |
| `-bookworm` | Full Debian 12 | `python:3.12-bookworm` |
| `-alpine` | Smallest (compatibility issues) | `python:3.12-alpine` |

---

## Multi-Stage Build Patterns

### Python Application
```dockerfile
# Build stage
FROM python:3.12-slim-bookworm AS builder

WORKDIR /app

# Install build dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# Production stage
FROM python:3.12-slim-bookworm

WORKDIR /app

# Create non-root user
RUN useradd --create-home --shell /bin/bash app

# Copy installed packages
COPY --from=builder /install /usr/local

# Copy application
COPY --chown=app:app . .

USER app

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8000/health')"

CMD ["python", "-m", "gunicorn", "app:app", "--bind", "0.0.0.0:8000"]
```

### Node.js Application
```dockerfile
# Build stage
FROM node:22-slim-bookworm AS builder

WORKDIR /app

# Install dependencies
COPY package*.json ./
RUN npm ci --only=production

# Build if needed
COPY . .
RUN npm run build

# Production stage
FROM node:22-slim-bookworm

WORKDIR /app

# Create non-root user
RUN useradd --create-home --shell /bin/bash app

# Copy built application
COPY --from=builder --chown=app:app /app/dist ./dist
COPY --from=builder --chown=app:app /app/node_modules ./node_modules
COPY --from=builder --chown=app:app /app/package*.json ./

USER app

EXPOSE 3000

HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD node -e "require('http').get('http://localhost:3000/health', (r) => process.exit(r.statusCode === 200 ? 0 : 1))"

CMD ["node", "dist/index.js"]
```

### Go Application
```dockerfile
# Build stage
FROM golang:1.22-bookworm AS builder

WORKDIR /app

# Download dependencies
COPY go.mod go.sum ./
RUN go mod download

# Build binary
COPY . .
RUN CGO_ENABLED=0 GOOS=linux go build -ldflags="-w -s" -o /app/server

# Production stage
FROM debian:bookworm-slim

WORKDIR /app

# Install CA certificates for HTTPS
RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Create non-root user
RUN useradd --create-home --shell /bin/bash app

# Copy binary
COPY --from=builder --chown=app:app /app/server .

USER app

EXPOSE 8080

HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD ["/app/server", "health"]

CMD ["./server"]
```

---

## Docker Compose Templates

### Web Application Stack
```yaml
# docker-compose.yml
services:
  app:
    build:
      context: .
      dockerfile: Dockerfile
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=postgresql://postgres:postgres@db:5432/app
      - REDIS_URL=redis://redis:6379
    depends_on:
      db:
        condition: service_healthy
      redis:
        condition: service_healthy
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8000/health"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 10s
    restart: unless-stopped

  db:
    image: postgres:16-bookworm
    volumes:
      - postgres_data:/var/lib/postgresql/data
    environment:
      - POSTGRES_DB=app
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=postgres
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 10s
      timeout: 5s
      retries: 5
    restart: unless-stopped

  redis:
    image: redis:7-bookworm
    volumes:
      - redis_data:/data
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 10s
      timeout: 5s
      retries: 5
    restart: unless-stopped

volumes:
  postgres_data:
  redis_data:
```

### Development with Hot Reload
```yaml
# docker-compose.dev.yml
services:
  app:
    build:
      context: .
      dockerfile: Dockerfile.dev
    ports:
      - "8000:8000"
    volumes:
      - .:/app
      - /app/node_modules  # Preserve node_modules
    environment:
      - NODE_ENV=development
    command: npm run dev
```

---

## Security Best Practices

### Dockerfile Security Checklist

```dockerfile
# ✅ Use specific version tags
FROM python:3.12-slim-bookworm

# ✅ Run as non-root user
RUN useradd --create-home --shell /bin/bash app
USER app

# ✅ Don't store secrets in image
# Use environment variables or secrets management

# ✅ Minimize installed packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    required-package \
    && rm -rf /var/lib/apt/lists/*

# ✅ Use COPY instead of ADD
COPY . .

# ✅ Set read-only filesystem if possible
# docker run --read-only

# ✅ Drop capabilities
# docker run --cap-drop=ALL
```

### Security Scanning
```bash
# Scan image for vulnerabilities
docker scout cves myimage:latest

# Alternative with Trivy
trivy image myimage:latest

# Build with security scanning
docker build --sbom=true --provenance=true -t myimage .
```

---

## Build Optimization

### Layer Caching Strategy
```dockerfile
# ✅ Order from least to most frequently changing

# 1. Base image and system packages (rarely change)
FROM python:3.12-slim-bookworm
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# 2. Dependencies (change occasionally)
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 3. Application code (changes frequently)
COPY . .

# 4. Build step
RUN python -m compileall .
```

### .dockerignore
```gitignore
# .dockerignore
.git
.gitignore
README.md
LICENSE
.env
.env.*
docker-compose*.yml
Dockerfile*
.dockerignore

# Language specific
__pycache__
*.pyc
.pytest_cache
.mypy_cache
node_modules
.npm
dist
build
target
*.log
```

---

## Useful Commands

### Build Commands
```bash
# Build with tag
docker build -t myapp:latest .

# Build for specific platform (ARM)
docker build --platform linux/arm64 -t myapp:arm64 .

# Build with no cache
docker build --no-cache -t myapp:latest .

# Multi-platform build
docker buildx build --platform linux/amd64,linux/arm64 -t myapp:latest --push .
```

### Debug Commands
```bash
# Run shell in container
docker run -it --rm myapp:latest /bin/bash

# View image layers
docker history myapp:latest

# Inspect image
docker inspect myapp:latest

# Check image size
docker images myapp:latest
```

### Cleanup Commands
```bash
# Remove unused images
docker image prune -a

# Remove all stopped containers
docker container prune

# Remove everything unused
docker system prune -a --volumes
```

---

## Report Format

### Container Review: `docker-review-[YYYY-MM-DD].md`

```markdown
# Docker Configuration Review

## Image Analysis
- **Base Image**: [Image name]
- **Final Size**: [Size]
- **Layers**: [Count]
- **Build Time**: [Duration]

## Security Assessment

| Check | Status |
|-------|--------|
| Non-root user | ✅/❌ |
| Specific version tags | ✅/❌ |
| No secrets in image | ✅/❌ |
| Minimal packages | ✅/❌ |
| Health check | ✅/❌ |

## Optimization Opportunities

| Issue | Impact | Fix |
|-------|--------|-----|

## Recommendations
1. [Priority 1]
2. [Priority 2]
3. [Priority 3]
```

---

## Common Issues & Fixes

| Issue | Cause | Fix |
|-------|-------|-----|
| Large image size | Too many layers, dev deps | Multi-stage build, slim base |
| Slow builds | Poor cache usage | Order COPY statements properly |
| Permission errors | Root vs non-root | Add USER directive |
| Missing CA certs | Stripped image | Install ca-certificates |
| Build fails on ARM | x86 binaries | Use multi-arch images |

---

## Severity Guide

| Level | Icon | Examples |
|-------|------|----------|
| **Critical** | 🔴 | Root user, secrets in image, no health check |
| **High** | 🟠 | Latest tags, oversized images, dev dependencies |
| **Medium** | 🟡 | Poor caching, missing .dockerignore |
| **Low** | 🟢 | Minor optimizations, labeling |
