# HTML/CSS Project Repository — Setup & Standards

> **Purpose**: Analyze and set up frontend project repositories  
> **Best For**: Codex, Claude, ChatGPT, Copilot, Agents  
> **Scope**: HTML, CSS, Static Sites, Component Libraries  
> **Last Updated**: 2026-03

---

> **Legacy Path Notice**: `html/` is maintained for backward compatibility. For stack-first guidance, also use [frontend/agents.md](../frontend/agents.md). 
> **Migration Map**: [docs/compat/html-to-frontend-map.md](../docs/compat/html-to-frontend-map.md)

## Mission

Help users **understand, set up, and improve** frontend project structure. Provide standards, configuration, and onboarding guidance for HTML/CSS projects.

---

## Guard Clauses

**If no project provided:**
```
NO_PROJECT_CONTEXT

To analyze your project, please share:
- Project type (static site, component library, etc.)
- Build tools used (if any)
- Team size and skill level
- Main technology (HTML, CSS, Sass, Tailwind, etc.)

Or paste your current directory structure.
```

**If project is well-organized:**
```
PROJECT_LOOKS_GOOD

✅ **Well-Structured Frontend Project**

Your project follows good practices:
- Clear folder organization ✓
- Consistent naming conventions ✓
- Proper configuration files ✓
- Documentation present ✓

Consider these minor improvements:
[list any optional enhancements]
```

---

## Quick Context Checklist

```
☐ Directory structure (tree or ls -la)
☐ Package.json or build config
☐ README content
☐ CSS approach (plain, Sass, Tailwind, etc.)
☐ Team standards (if any)
```

---

## Copy-Paste Prompts

### Prompt: Analyze Project Structure
```text
Analyze this frontend project structure:

{{TREE_OUTPUT}}

Evaluate:
1. Folder organization
2. File naming conventions
3. Asset organization
4. CSS architecture
5. Component structure

Recommend improvements with specific folder/file changes.
```

### Prompt: Generate Project Setup
```text
Create a frontend project structure for:

Project: {{PROJECT_TYPE}}
CSS Approach: {{CSS_METHOD}}
Components: {{COMPONENT_STYLE}}
Tools: {{BUILD_TOOLS}}

Include:
- Folder structure
- Essential config files
- README template
- CSS organization
- Component file templates
```

### Prompt: Improve Existing Project
```text
Here's my current frontend project:

{{CURRENT_STRUCTURE}}

Problems I'm facing:
{{PROBLEMS}}

Suggest:
1. Reorganization steps
2. Files to add/remove
3. Naming convention updates
4. Configuration improvements
```

### Prompt: Create Onboarding Guide
```text
Create a developer onboarding guide for this frontend project:

{{PROJECT_STRUCTURE}}

Include:
1. Project overview
2. Setup instructions
3. Folder structure explanation
4. CSS conventions
5. Component creation guide
6. Common tasks
```

### Prompt: Generate Configuration
```text
Generate configuration files for a frontend project:

Build: {{BUILD_TOOL}}
CSS: {{CSS_PREPROCESSOR}}
Linting: {{LINTING_NEEDS}}
Browser support: {{BROWSERS}}

Create:
- Build configuration
- CSS linting rules
- Editor config
- Git ignore
```

---

## Recommended Project Structures

### Static Site
```
project/
├── index.html
├── about.html
├── contact.html
├── assets/
│   ├── css/
│   │   ├── main.css
│   │   └── components/
│   │       ├── header.css
│   │       ├── footer.css
│   │       └── cards.css
│   ├── js/
│   │   └── main.js
│   ├── images/
│   │   ├── icons/
│   │   └── photos/
│   └── fonts/
├── README.md
└── .gitignore
```

### Component Library
```
component-library/
├── src/
│   ├── components/
│   │   ├── button/
│   │   │   ├── button.html
│   │   │   ├── button.css
│   │   │   └── README.md
│   │   ├── card/
│   │   ├── form/
│   │   └── navigation/
│   ├── tokens/
│   │   ├── colors.css
│   │   ├── spacing.css
│   │   └── typography.css
│   └── utilities/
│       └── helpers.css
├── docs/
│   ├── getting-started.md
│   └── components.md
├── dist/
├── package.json
└── README.md
```

### Sass Project
```
sass-project/
├── src/
│   ├── scss/
│   │   ├── main.scss
│   │   ├── base/
│   │   │   ├── _reset.scss
│   │   │   ├── _typography.scss
│   │   │   └── _variables.scss
│   │   ├── components/
│   │   │   ├── _buttons.scss
│   │   │   ├── _cards.scss
│   │   │   └── _forms.scss
│   │   ├── layout/
│   │   │   ├── _header.scss
│   │   │   ├── _footer.scss
│   │   │   └── _grid.scss
│   │   └── pages/
│   │       ├── _home.scss
│   │       └── _about.scss
│   └── html/
│       └── index.html
├── dist/
│   ├── css/
│   └── index.html
├── package.json
└── README.md
```

### Tailwind Project
```
tailwind-project/
├── src/
│   ├── index.html
│   ├── pages/
│   │   └── about.html
│   ├── components/
│   │   └── partials/
│   └── input.css
├── dist/
│   ├── output.css
│   └── index.html
├── tailwind.config.js
├── postcss.config.js
├── package.json
└── README.md
```

---

## Essential Configuration Files

### .gitignore
```gitignore
# Dependencies
node_modules/

# Build output
dist/
build/

# Editor
.vscode/
.idea/
*.swp

# OS
.DS_Store
Thumbs.db

# Logs
*.log
npm-debug.log*

# Compiled CSS
*.css.map
```

### .editorconfig
```ini
root = true

[*]
indent_style = space
indent_size = 2
end_of_line = lf
charset = utf-8
trim_trailing_whitespace = true
insert_final_newline = true

[*.md]
trim_trailing_whitespace = false

[*.{html,css,scss}]
indent_size = 2
```

### .stylelintrc.json
```json
{
  "extends": ["stylelint-config-standard"],
  "rules": {
    "selector-class-pattern": "^[a-z][a-z0-9]*(?:-[a-z0-9]+)*(?:__[a-z0-9]+(?:-[a-z0-9]+)*)?(?:--[a-z0-9]+(?:-[a-z0-9]+)*)?$",
    "declaration-block-no-redundant-longhand-properties": true,
    "shorthand-property-no-redundant-values": true,
    "color-named": "never",
    "max-nesting-depth": 3
  }
}
```

### package.json (Basic)
```json
{
  "name": "frontend-project",
  "version": "1.0.0",
  "description": "Frontend project",
  "scripts": {
    "start": "npx serve",
    "lint:css": "stylelint 'src/**/*.css'",
    "format": "prettier --write 'src/**/*.{html,css}'"
  },
  "devDependencies": {
    "stylelint": "^15.0.0",
    "stylelint-config-standard": "^34.0.0",
    "prettier": "^3.0.0"
  }
}
```

---

## README Template

```markdown
# Project Name

Brief description of the project.

## Quick Start

```bash
# Clone the repository
git clone [repo-url]
cd [project-name]

# Install dependencies (if any)
npm install

# Start development server
npm start
```

## Project Structure

```
src/
├── css/          # Stylesheets
├── js/           # JavaScript files
├── images/       # Image assets
└── index.html    # Main entry point
```

## CSS Architecture

This project uses [BEM/Tailwind/SCSS] for styling.

### Naming Convention
- Components: `.component-name`
- Elements: `.component-name__element`
- Modifiers: `.component-name--modifier`

### File Organization
- `base/` - Reset, typography, variables
- `components/` - Reusable UI components
- `layout/` - Page structure (header, footer)
- `pages/` - Page-specific styles

## Browser Support

- Chrome (last 2 versions)
- Firefox (last 2 versions)
- Safari (last 2 versions)
- Edge (last 2 versions)

## Contributing

1. Create a feature branch
2. Follow the CSS naming conventions
3. Test across browsers
4. Submit a PR

## License

MIT
```

---

## Report Format

### Repository Analysis: `repo-analysis-[YYYY-MM-DD].md`

```markdown
# Repository Analysis: [Project Name]

## Overview
- **Project Type**: [Static Site / Component Library / etc.]
- **Tech Stack**: [HTML, CSS, Sass, etc.]
- **Build Tools**: [None / Vite / Webpack / etc.]
- **Overall Health**: [Score /10]

## Structure Analysis
| Aspect | Status | Notes |
|--------|--------|-------|
| Folder Organization | ✅/⚠️/❌ | |
| Naming Conventions | ✅/⚠️/❌ | |
| CSS Architecture | ✅/⚠️/❌ | |
| Documentation | ✅/⚠️/❌ | |
| Configuration | ✅/⚠️/❌ | |

## Recommendations

### High Priority
1. [Issue] - [Fix]

### Medium Priority
1. [Issue] - [Fix]

### Nice to Have
1. [Improvement]

## Suggested Structure
[Include improved folder structure]

## Next Steps
1. [Action item]
2. [Action item]
```

---

## Severity Guide

| Level | Icon | Action | Examples |
|-------|------|--------|----------|
| **Critical** | 🔴 | Fix now | No CSS organization, missing config |
| **High** | 🟠 | Fix soon | Inconsistent naming, no documentation |
| **Medium** | 🟡 | Plan fix | Missing linting, suboptimal structure |
| **Low** | 🟢 | Consider | Optional improvements |

---

## Common Issues & Fixes

| Issue | Problem | Solution |
|-------|---------|----------|
| Flat CSS | All styles in one file | Split by component/page |
| No variables | Hardcoded values | Use CSS custom properties |
| No documentation | Team confusion | Add README and comments |
| Mixed naming | Inconsistent classes | Adopt BEM or utility classes |
| No linting | Style inconsistency | Add Stylelint config |
| Missing gitignore | Tracked junk files | Add proper .gitignore |
