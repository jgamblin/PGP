# PR Review Feedback — Code Review Assistant

> **Purpose**: Provide constructive, actionable PR reviews  
> **Best For**: Copilot, ChatGPT, Claude, Agents  
> **Languages**: Any  
> **Last Updated**: 2025-12

---

## Mission

Help review **pull requests** with constructive, actionable feedback. Focus on catching bugs, security issues, and maintainability problems while being respectful and helpful.

---

## Guard Clauses

**If no diff provided:**
```
NO_DIFF_PROVIDED

Please provide the PR diff to review:
- Run: git diff main...HEAD
- Or paste the changed code
- Include file paths for context
```

**If PR looks good:**
```
LGTM

✅ **Approved to Merge**

Code review complete — no blocking issues.

Checks performed:
- Security: no vulnerabilities ✓
- Logic: no bugs found ✓
- Performance: no issues ✓
- Style: follows conventions ✓

Ship it! 🚀
```

---

## Quick Context Checklist

```
☐ PR diff (git diff main...HEAD)
☐ Changed files list
☐ PR description/intent
☐ Language and framework context
```

---

## Copy-Paste PR Review Prompts

### Prompt: Full PR Review
```text
Review this PR:

{{DIFF}}

Check for:
1. 🔴 Security issues (injection, auth, secrets)
2. 🟠 Bugs and logic errors
3. 🟡 Performance problems
4. 🟢 Code style and best practices

For each issue provide:
- File and line number
- Severity level
- Specific fix suggestion
- Brief explanation

Use GitHub suggestion blocks where possible.
```

### Prompt: Security-Focused Review
```text
Security review for this PR:

{{DIFF}}

Focus on:
- SQL/command injection
- Authentication/authorization
- Input validation
- Secret handling
- CSRF/XSS risks

Flag all security concerns with severity.
```

### Prompt: Quick Review
```text
Quick review this small PR:

{{DIFF}}

Only flag:
- Bugs that will break in production
- Security vulnerabilities
- Obvious performance issues

Skip style nits. Be concise.
```

### Prompt: Review Tests
```text
Review the tests in this PR:

{{DIFF}}

Check:
1. Do tests cover the new functionality?
2. Are edge cases tested?
3. Are assertions meaningful?
4. Could tests give false positives?
5. Is test code maintainable?

Suggest missing test cases.
```

### Prompt: Generate PR Description
```text
Generate a PR description for this diff:

{{DIFF}}

Include:
1. Summary (what and why)
2. Changes made (bullet points)
3. Testing done
4. Breaking changes (if any)
5. Related issues

Keep it concise but complete.
```

---

## Review Guidelines

### 1. **What to Look For**

| Category | Examples | Severity |
|----------|----------|----------|
| **Security** | Injection, auth bypass, secrets | 🔴 Critical |
| **Bugs** | Logic errors, null refs, race conditions | 🟠 High |
| **Performance** | N+1 queries, memory leaks, blocking | 🟡 Medium |
| **Maintainability** | Complexity, duplication, naming | �� Low |

### 2. **Feedback Format**

Use GitHub suggestion blocks for concrete fixes:

````markdown
**🟠 High: Potential null reference**

`user` could be null if not found. Add a check:

```suggestion
const user = await findUser(id);
if (!user) {
  throw new NotFoundError('User not found');
}
return user.name;
```
````

### 3. **Review Checklist**

- [ ] Code does what PR description says
- [ ] No obvious bugs or logic errors
- [ ] Security considerations addressed
- [ ] Error handling present
- [ ] Tests added/updated
- [ ] No unnecessary complexity
- [ ] Naming is clear and consistent

### 4. **Tone Guide**

| Instead of | Say |
|------------|-----|
| "This is wrong" | "This might cause X issue because..." |
| "Why did you..." | "Consider doing X instead for..." |
| "This is bad" | "This could be improved by..." |
| "You need to" | "We should..." |

---

## Common Issues to Catch

### Security
```
- SQL queries built with string concatenation
- User input not validated/sanitized
- Hardcoded credentials or API keys
- Missing authentication/authorization
- Sensitive data in logs
```

### Bugs
```
- Off-by-one errors
- Null/undefined not handled
- Race conditions
- Resource leaks (connections, files)
- Error conditions not handled
```

### Performance
```
- N+1 database queries
- Missing indexes on queries
- Large data loaded into memory
- Synchronous blocking operations
- Missing caching opportunities
```

---

## Report Format

### PR Review: `pr-review-[YYYY-MM-DD].md`

```markdown
# PR Review

## Summary
- **PR**: [Title/Number]
- **Files Changed**: [Count]
- **Verdict**: Approved / Request Changes / Needs Discussion

## Findings

### 🔴 Critical (Must Fix)
| Issue | Location | Fix |
|-------|----------|-----|

### �� High (Should Fix)
| Issue | Location | Fix |
|-------|----------|-----|

### 🟡 Medium (Consider)
| Issue | Location | Suggestion |
|-------|----------|------------|

### 🟢 Low (Optional)
| Issue | Location | Note |
|-------|----------|------|

## Positive Feedback
- [What was done well]

## Questions
- [Clarifications needed]
```

---

## Severity Guide

| Level | Icon | Action | Examples |
|-------|------|--------|----------|
| **Critical** | 🔴 | Block merge | Security holes, data loss, crashes |
| **High** | 🟠 | Should fix | Bugs in main paths, missing validation |
| **Medium** | 🟡 | Consider fixing | Code smells, minor performance |
| **Low** | 🟢 | Optional | Style, minor improvements |

---

## Tips for Better Reviews

1. **Review in context**: Understand what the PR is trying to do
2. **Be specific**: Point to exact lines, suggest exact fixes
3. **Explain why**: Help the author learn, not just fix
4. **Prioritize**: Not all issues are equally important
5. **Be kind**: There's a person on the other side
6. **Acknowledge good work**: Positive feedback matters too
