# Documentation Generation — Clear & Useful Docs

> **Purpose**: Create clear, useful documentation  
> **Best For**: Copilot, ChatGPT, Claude, Agents  
> **Languages**: Any  
> **Last Updated**: 2025-12

---

## Mission

Help create **clear, useful documentation** that makes code easier to understand and use. Focus on practical docs that people actually read.

---

## Guard Clauses

**If no code/project provided:**
```
NO_CONTENT_TO_DOCUMENT

Please provide content to document:
- Source code files
- API endpoints
- Project structure
- Or describe what needs documentation
```

**If documentation is complete:**
```
DOCUMENTATION_COMPLETE

✅ Documentation review complete — looks good.

Checks performed:
- README present and clear: ✓
- API documented: ✓
- Setup instructions: ✓
- Examples included: ✓

Documentation is comprehensive.
```

---

## Quick Context Checklist

```
☐ Code/project to document
☐ Target audience (developers, users, both)
☐ Documentation style (technical, friendly, brief)
☐ Output format (Markdown, JSDoc, docstrings)
```

---

## Copy-Paste Documentation Prompts

### Prompt: Generate README
```text
Generate a README.md for this project:

Project name: {{NAME}}
Purpose: {{PURPOSE}}
Language: {{LANGUAGE}}
Main features: {{FEATURES}}

Include:
1. Title and description
2. Installation instructions
3. Quick start example
4. Configuration options
5. API reference (brief)
6. Contributing guidelines
7. License

Keep it concise but complete.
```

### Prompt: Add Code Documentation
```text
Add documentation to this code:

{{CODE}}

Language: {{LANGUAGE}}
Style: {{DOCSTRING_STYLE}}

For each function/class include:
- Brief description
- Parameters with types
- Return value
- Example usage (for public APIs)
- Exceptions/errors raised

Match existing project style.
```

### Prompt: Document API Endpoint
```text
Document this API endpoint:

{{CODE}}

Create documentation including:
1. Endpoint URL and method
2. Request parameters/body
3. Response format with examples
4. Error responses
5. Authentication requirements
6. Rate limits (if any)
7. Example curl/fetch request
```

### Prompt: Create Setup Guide
```text
Create a setup/installation guide for:

{{PROJECT_STRUCTURE}}

Include:
1. Prerequisites (language, tools, accounts)
2. Clone/download instructions
3. Dependency installation
4. Environment configuration
5. Database setup (if applicable)
6. Running the application
7. Verifying it works
8. Common issues and fixes
```

### Prompt: Write Changelog Entry
```text
Write a changelog entry for these changes:

{{CHANGES}}

Version: {{VERSION}}

Use Keep a Changelog format:
- Added: new features
- Changed: changes in existing functionality
- Deprecated: soon-to-be removed
- Removed: removed features
- Fixed: bug fixes
- Security: vulnerability fixes
```

### Prompt: Generate API Reference
```text
Generate API reference documentation:

{{CODE}}

Format: Markdown tables

For each public function/method:
| Function | Parameters | Returns | Description |

Include:
- Type information
- Default values
- Required vs optional
- Brief examples
```

---

## Documentation Templates

### 1. **README Template**

```markdown
# Project Name

Brief description of what this project does.

## Features

- Feature 1
- Feature 2
- Feature 3

## Installation

```bash
# Installation command
npm install project-name
```

## Quick Start

```javascript
// Minimal example
import { thing } from 'project-name';
const result = thing.doSomething();
```

## Configuration

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `option1` | string | `"default"` | What it does |

## API Reference

See [API.md](./docs/API.md) for full documentation.

## Contributing

See [CONTRIBUTING.md](./CONTRIBUTING.md).

## License

MIT
```

### 2. **Function Documentation**

```python
# Python (Google style)
def process_data(data: list[dict], options: Options | None = None) -> Result:
    """Process input data and return results.

    Args:
        data: List of data dictionaries to process.
        options: Optional configuration options.

    Returns:
        Result object containing processed data.

    Raises:
        ValueError: If data is empty or malformed.
        ProcessingError: If processing fails.

    Example:
        >>> result = process_data([{"id": 1}])
        >>> print(result.count)
        1
    """
```

```javascript
// JavaScript (JSDoc)
/**
 * Process input data and return results.
 * @param {Object[]} data - Array of data objects to process.
 * @param {Options} [options] - Optional configuration.
 * @returns {Result} Processed result object.
 * @throws {Error} If data is empty or malformed.
 * @example
 * const result = processData([{ id: 1 }]);
 * console.log(result.count); // 1
 */
function processData(data, options) { }
```

### 3. **API Endpoint Documentation**

```markdown
## POST /api/users

Create a new user account.

### Request

```json
{
  "email": "user@example.com",
  "password": "securepassword",
  "name": "John Doe"
}
```

### Response

**Success (201)**
```json
{
  "id": "abc123",
  "email": "user@example.com",
  "name": "John Doe",
  "createdAt": "2025-01-01T00:00:00Z"
}
```

**Error (400)**
```json
{
  "error": "validation_error",
  "message": "Email already exists"
}
```

### Authentication

Requires API key in header: `Authorization: Bearer <token>`
```

---

## Documentation Best Practices

### 1. **Writing Guidelines**

| Do | Don't |
|----|-------|
| Use active voice | Use passive voice |
| Be concise | Write walls of text |
| Include examples | Only describe abstractly |
| Keep up to date | Let docs get stale |
| Write for your audience | Use jargon unnecessarily |

### 2. **What to Document**

| Priority | What | Why |
|----------|------|-----|
| **High** | Setup/Installation | Gets people started |
| **High** | Public API | How to use your code |
| **High** | Configuration | How to customize |
| **Medium** | Architecture | How it works |
| **Medium** | Contributing | How to help |
| **Low** | Internal details | Usually not needed |

### 3. **Documentation Audit Checklist**

- [ ] README exists and is current
- [ ] Installation works as documented
- [ ] Examples run without errors
- [ ] All public APIs documented
- [ ] Configuration options listed
- [ ] Error messages explained
- [ ] Changelog maintained

---

## Report Format

### Documentation Report: `docs-[YYYY-MM-DD].md`

```markdown
# Documentation Assessment

## Summary
- **Project**: [Name]
- **Coverage**: [% of public APIs documented]
- **Quality**: [Good/Needs Work/Missing]

## Current State
- README: [✓/✗]
- API Docs: [✓/✗]
- Setup Guide: [✓/✗]
- Examples: [✓/✗]
- Changelog: [✓/✗]

## Gaps Found

| Missing | Priority | Effort |
|---------|----------|--------|
| [Item] | High/Med/Low | Hours |

## Generated Documentation
[Include generated docs here]

## Recommendations
1. [First priority]
2. [Second priority]
```

---

## Tips for Good Documentation

1. **Write for the reader**: Consider what they need to know, not what you want to say
2. **Start with examples**: Show, don't just tell
3. **Keep it updated**: Outdated docs are worse than no docs
4. **Test your docs**: Try following your own instructions
5. **Get feedback**: Ask someone to read it and identify confusion
