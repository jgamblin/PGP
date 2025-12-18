# AI Assistant Instructions — Copilot Configuration

> **Purpose**: Configure AI coding assistants for optimal output  
> **Best For**: GitHub Copilot, ChatGPT, Claude, Cursor  
> **Languages**: Any  
> **Last Updated**: 2025-12

---

## Mission

Help configure and use **AI coding assistants** effectively. Create custom instructions that produce consistent, high-quality code matching your project's style and requirements.

---

## Guard Clauses

**If no context provided:**
```
NO_PROJECT_CONTEXT

Please provide project context for AI configuration:
- Project type and language
- Coding standards/style guide
- Framework and libraries used
- Specific requirements or constraints
```

**If already well-configured:**
```
AI_CONFIG_COMPLETE

✅ AI assistant configuration looks good.

Current setup:
- Project context: defined ✓
- Code style: specified ✓
- Output format: clear ✓
- Constraints: documented ✓

Ready for AI-assisted development.
```

---

## Quick Context Checklist

```
☐ Project language and framework
☐ Code style preferences
☐ Testing requirements
☐ Documentation standards
```

---

## Copy-Paste AI Configuration Prompts

### Prompt: Create Custom Instructions
```text
Create custom AI assistant instructions for this project:

Project: {{PROJECT_NAME}}
Language: {{LANGUAGE}}
Framework: {{FRAMEWORK}}
Style guide: {{STYLE_GUIDE}}

Generate instructions that ensure AI:
1. Follows our code style
2. Uses correct imports/dependencies
3. Includes proper error handling
4. Adds appropriate documentation
5. Writes testable code

Format for .github/copilot-instructions.md
```

### Prompt: Code Generation Guidelines
```text
When generating code for this project:

{{PROJECT_CONTEXT}}

Always:
- Use {{LANGUAGE_VERSION}} syntax
- Follow {{STYLE_GUIDE}} conventions
- Include type hints/annotations
- Add error handling
- Write docstrings/comments for complex logic

Never:
- Use deprecated APIs
- Include hardcoded credentials
- Skip input validation
- Ignore edge cases
```

### Prompt: Review AI-Generated Code
```text
Review this AI-generated code for quality:

{{CODE}}

Check for:
1. Correctness (does it do what was asked?)
2. Security issues
3. Performance problems
4. Style violations
5. Missing error handling
6. Edge cases not handled

Suggest improvements or approve.
```

### Prompt: Improve AI Prompts
```text
Improve this prompt for better AI output:

Original prompt:
{{PROMPT}}

Current output issues:
{{ISSUES}}

Rewrite the prompt to:
1. Be more specific
2. Include examples
3. Specify output format
4. Add constraints
5. Handle edge cases
```

### Prompt: Create Code Template
```text
Create a code template for AI to follow:

Use case: {{USE_CASE}}
Language: {{LANGUAGE}}

Include:
- Standard imports
- Function/class structure
- Error handling pattern
- Documentation format
- Test structure

Show example implementation.
```

---

## AI Configuration Best Practices

### 1. **Project-Level Instructions**

Create `.github/copilot-instructions.md`:

```markdown
# Copilot Instructions for [Project Name]

## Language & Style
- Language: [e.g., TypeScript 5.0+, Python 3.11+]
- Style: [e.g., Airbnb, PEP 8, Google]
- Formatter: [e.g., Prettier, Ruff, gofmt]

## Code Patterns
- Error handling: [pattern description]
- Logging: [library and format]
- Testing: [framework and approach]

## Do's
- Always include type annotations
- Use async/await for I/O operations
- Write descriptive variable names
- Add JSDoc/docstrings for public APIs

## Don'ts
- Don't use `any` type without justification
- Don't catch generic exceptions silently
- Don't hardcode configuration values
- Don't skip input validation
```

### 2. **Effective Prompting Patterns**

| Pattern | Example | Use When |
|---------|---------|----------|
| **Specific** | "Create a retry decorator with exponential backoff, max 3 retries" | You know exactly what you want |
| **Contextual** | "In our Express app with Prisma, add a user endpoint" | Building on existing code |
| **Constrained** | "Under 20 lines, no external deps, ES6 only" | Need focused output |
| **Examples** | "Like this existing function: [code]" | Want consistent style |

### 3. **Output Format Control**

```text
# Request specific output
"Generate as:
1. Function implementation
2. Unit tests (pytest)
3. Usage example
4. Docstring

Use this format:
```python
def function_name(...):
    '''Docstring here'''
    ...
```"
```

### 4. **Common Configuration by Language**

#### JavaScript/TypeScript
```markdown
- Use ESM imports, not CommonJS
- Prefer const, avoid let, never var
- Use async/await, not callbacks
- Include JSDoc for public functions
- Use strict TypeScript (no any)
```

#### Python
```markdown
- Python 3.11+ syntax
- Type hints on all functions
- Google-style docstrings
- Use pathlib, not os.path
- Prefer dataclasses or Pydantic
```

#### Go
```markdown
- Follow Effective Go guidelines
- Handle all errors explicitly
- Use context for cancellation
- Add godoc comments
- Use interfaces for testing
```

---

## Report Format

### AI Configuration Report: `ai-config-[YYYY-MM-DD].md`

```markdown
# AI Assistant Configuration

## Project Setup
- **Project**: [Name]
- **Language**: [Language + Version]
- **Framework**: [Framework]

## Custom Instructions
[Generated copilot-instructions.md content]

## Prompt Templates

### Feature Implementation
```text
[Template]
```

### Bug Fix
```text
[Template]
```

### Test Generation
```text
[Template]
```

## Quality Checklist
- [ ] Style guide documented
- [ ] Error patterns defined
- [ ] Test requirements specified
- [ ] Security constraints listed
```

---

## Tips for Better AI Output

1. **Be Specific**: "Add login endpoint" → "Add POST /api/auth/login with JWT, rate limiting, and password hashing"

2. **Provide Context**: Include relevant existing code, types, or interfaces

3. **Specify Constraints**: Mention performance requirements, compatibility needs

4. **Request Format**: Ask for specific output structure (function, class, module)

5. **Iterate**: Refine output with follow-up prompts

6. **Verify**: Always review AI-generated code for correctness and security
