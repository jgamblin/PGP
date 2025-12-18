# Project Repository Setup — New Project Scaffolding

> **Purpose**: Bootstrap new projects with best practices  
> **Best For**: Copilot, ChatGPT, Claude, Agents  
> **Languages**: Any  
> **Last Updated**: 2025-12

---

## Mission

Help **set up new projects** with proper structure, configuration, documentation, and tooling. Create a solid foundation that scales.

---

## Guard Clauses

**If no project type specified:**
```
PROJECT_TYPE_REQUIRED

What kind of project are you creating?

Common types:
- Web app (React, Vue, Next.js, etc.)
- API/Backend (Express, FastAPI, Rails, etc.)
- CLI tool
- Library/Package
- Microservice
- Monorepo

Please specify the type and language/framework.
```

**If project already exists:**
```
PROJECT_EXISTS

Detected existing project structure.

Would you like to:
1. Add missing configurations
2. Update existing setup
3. Start fresh (will overwrite)

Please clarify intent.
```

---

## Quick Context Checklist

```
☐ Project name
☐ Language/framework choice
☐ Project type (app, library, CLI)
☐ Team size (solo, small, large)
☐ Deployment target (Vercel, AWS, Docker)
```

---

## Copy-Paste Project Prompts

### Prompt: Create New Project
```text
Set up a new [LANGUAGE/FRAMEWORK] project for [PURPOSE].

Include:
1. Standard directory structure
2. Package manager config (dependencies, scripts)
3. Linter and formatter setup
4. Git configuration (.gitignore, hooks)
5. README with setup instructions
6. Basic CI/CD workflow

Make it production-ready from day one.
```

### Prompt: Add Configuration Files
```text
Add standard configuration files to this [LANGUAGE] project:

Current structure:
[PASTE TREE OUTPUT]

Add:
- Linting config
- Formatting config
- Editor config
- Git hooks (pre-commit)
- Environment file template

Follow community standards.
```

### Prompt: Create README
```text
Generate a professional README for this project:

Project: [NAME]
Purpose: [DESCRIPTION]
Language: [LANG]
Framework: [FRAMEWORK]

Include:
1. Project overview
2. Features
3. Installation steps
4. Usage examples
5. Configuration
6. Contributing guidelines
7. License
```

### Prompt: Setup CI/CD
```text
Create CI/CD workflows for this [LANGUAGE] project:

Repository: [GITHUB/GITLAB]
Deployment: [TARGET]

Include:
- Test workflow (on PR)
- Build and deploy (on merge to main)
- Security scanning
- Code coverage reporting

Use [GITHUB ACTIONS / GITLAB CI].
```

### Prompt: Monorepo Setup
```text
Convert this project to a monorepo structure:

Current apps/packages:
- [LIST THEM]

Use [TURBOREPO / NX / PNPM WORKSPACES].

Include:
- Shared configs
- Dependency management
- Build orchestration
- Per-package scripts
```

---

## Project Structure Templates

### Web Application
```
project/
├── src/
│   ├── components/    # UI components
│   ├── pages/         # Route pages
│   ├── hooks/         # Custom hooks
│   ├── utils/         # Helpers
│   ├── services/      # API clients
│   └── types/         # Type definitions
├── public/            # Static assets
├── tests/             # Test files
├── .github/           # CI/CD workflows
├── package.json
├── tsconfig.json
├── .eslintrc.js
├── .prettierrc
├── .gitignore
└── README.md
```

### API/Backend
```
project/
├── src/
│   ├── routes/        # API endpoints
│   ├── controllers/   # Request handlers
│   ├── services/      # Business logic
│   ├── models/        # Data models
│   ├── middleware/    # Express/Fastify middleware
│   ├── utils/         # Helpers
│   └── config/        # Configuration
├── tests/
├── migrations/        # Database migrations
├── scripts/           # Utility scripts
├── .github/
├── Dockerfile
├── docker-compose.yml
├── package.json
└── README.md
```

### Python Package
```
project/
├── src/
│   └── package_name/
│       ├── __init__.py
│       ├── main.py
│       └── utils.py
├── tests/
│   ├── __init__.py
│   └── test_main.py
├── docs/
├── .github/
├── pyproject.toml
├── setup.py
├── requirements.txt
├── .pre-commit-config.yaml
├── .gitignore
└── README.md
```

### CLI Tool
```
project/
├── src/
│   ├── cli.py         # Entry point
│   ├── commands/      # Subcommands
│   └── utils/
├── tests/
├── pyproject.toml     # or package.json
├── .github/
├── .gitignore
├── LICENSE
└── README.md
```

---

## Essential Configuration Files

### .gitignore Template
```gitignore
# Dependencies
node_modules/
vendor/
.venv/
__pycache__/

# Build outputs
dist/
build/
*.egg-info/

# Environment
.env
.env.local
*.env

# IDE
.idea/
.vscode/
*.swp

# OS
.DS_Store
Thumbs.db

# Logs
*.log
logs/

# Test/Coverage
coverage/
.pytest_cache/
.nyc_output/
```

### EditorConfig
```ini
# .editorconfig
root = true

[*]
indent_style = space
indent_size = 2
end_of_line = lf
charset = utf-8
trim_trailing_whitespace = true
insert_final_newline = true

[*.{py,rs}]
indent_size = 4

[*.md]
trim_trailing_whitespace = false
```

### Pre-commit Hooks
```yaml
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.5.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
      - id: check-json
      - id: check-added-large-files
```

---

## README Template

```markdown
# Project Name

Brief description of what this project does.

## Features

- Feature 1
- Feature 2
- Feature 3

## Installation

\`\`\`bash
# Clone the repository
git clone https://github.com/user/project.git
cd project

# Install dependencies
npm install  # or pip install -r requirements.txt

# Set up environment
cp .env.example .env
# Edit .env with your values
\`\`\`

## Usage

\`\`\`bash
# Development
npm run dev

# Production
npm run build
npm start
\`\`\`

## Configuration

| Variable | Description | Default |
|----------|-------------|---------|
| `PORT` | Server port | `3000` |
| `DATABASE_URL` | Database connection | Required |

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

MIT
```

---

## Report Format

### Project Setup: `project-setup-[name].md`

```markdown
# Project Setup Report

## Project Info
- **Name**: [Project Name]
- **Type**: [Web App / API / CLI / Library]
- **Language**: [Language/Framework]
- **Created**: [Date]

## Structure Created
[Tree output of created structure]

## Configuration Files
| File | Purpose | Status |
|------|---------|--------|
| package.json | Dependencies | ✅ Created |
| tsconfig.json | TypeScript | ✅ Created |
| .eslintrc | Linting | ✅ Created |
| .prettierrc | Formatting | ✅ Created |
| .gitignore | Git ignores | ✅ Created |

## Scripts Available
| Command | Description |
|---------|-------------|
| `npm run dev` | Start development |
| `npm run build` | Production build |
| `npm test` | Run tests |
| `npm run lint` | Run linter |

## Next Steps
1. [ ] Install dependencies: `npm install`
2. [ ] Configure environment: `cp .env.example .env`
3. [ ] Start development: `npm run dev`
```

---

## Severity Levels

| Level | Icon | Meaning | Example |
|-------|------|---------|---------|
| **Critical** | 🔴 | Missing required config | No package.json |
| **High** | 🟠 | Missing important setup | No .gitignore |
| **Medium** | 🟡 | Missing recommended | No linter config |
| **Low** | 🟢 | Nice to have | No EditorConfig |

---

## Best Practices Checklist

### Security
- [ ] `.env` files in `.gitignore`
- [ ] No secrets in code
- [ ] Dependency lock files committed
- [ ] Security scanning in CI

### Quality
- [ ] Linter configured
- [ ] Formatter configured
- [ ] Pre-commit hooks
- [ ] Tests directory created

### Documentation
- [ ] README with setup instructions
- [ ] Contributing guidelines
- [ ] License file
- [ ] Changelog

### CI/CD
- [ ] Test workflow
- [ ] Build workflow
- [ ] Deploy workflow
- [ ] Branch protection
