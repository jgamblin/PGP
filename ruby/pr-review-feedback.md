# Ruby PR Review — Code Change Feedback

> **Purpose**: Review Ruby/Rails pull requests for quality and correctness  
> **Best For**: Copilot, ChatGPT, Claude, Agents  
> **Scope**: Ruby code changes, Rails patterns, RSpec tests  
> **Last Updated**: 2025-12

---

## Mission

Provide **constructive, actionable feedback** on Ruby code changes. Catch bugs, security issues, and ensure code quality before merge.

---

## Guard Clauses

**If no diff provided:**
```
NO_DIFF_PROVIDED

Please provide the PR changes to review:
- Run: git diff main...HEAD
- Or paste the changed code
- Include file paths for context
```

**If changes look good:**
```
LGTM

✅ **Approved to Merge**

Code review complete:
- Logic: Correct ✓
- Ruby style: Idiomatic ✓
- Security: No issues ✓
- Tests: Adequate ✓
- Performance: Acceptable ✓

Ship it! 🚀
```

---

## Quick Context Checklist

```
☐ PR diff (git diff main...HEAD)
☐ Changed files list
☐ PR description/intent
☐ Related tests
```

---

## Copy-Paste Prompts

### Prompt: Full PR Review
```text
Review this Ruby PR:

{{DIFF}}

Check:
1. 🔴 Security issues (SQL injection, mass assignment)
2. 🟠 Logic errors and bugs
3. 🟡 Ruby idioms and style
4. 🟢 Performance concerns
5. Test coverage

For each issue:
- File and line
- Severity
- Fix suggestion

Use GitHub suggestion blocks where helpful.
```

### Prompt: Rails-Specific Review
```text
Review this Rails PR:

{{DIFF}}

Focus on:
1. Controller actions (thin controllers?)
2. Model logic (validations, callbacks)
3. N+1 query risks
4. Strong parameters
5. Service object opportunities

Flag anti-patterns with fix suggestions.
```

### Prompt: Security Review
```text
Review this PR for security issues:

{{DIFF}}

Check:
1. SQL injection vulnerabilities
2. Mass assignment issues
3. Authentication/authorization gaps
4. Sensitive data exposure
5. CSRF protection

Flag all security concerns with severity.
```

### Prompt: Test Review
```text
Review the tests in this PR:

{{DIFF}}

Check:
1. Test coverage for new code
2. Edge cases tested
3. Test isolation
4. Factory usage
5. Assertion quality

Suggest missing test cases.
```

### Prompt: Quick Review
```text
Quick review this Ruby PR:

{{DIFF}}

Only flag:
- Bugs and logic errors
- Security vulnerabilities
- Obvious performance issues

Skip style nitpicks. Be concise.
```

---

## Review Checklist

### Ruby Code
- [ ] Uses Ruby idioms appropriately
- [ ] Methods are reasonably sized (<15 lines)
- [ ] Guard clauses instead of nested conditionals
- [ ] Proper error handling
- [ ] No unnecessary complexity

### Rails Code
- [ ] Controllers are thin
- [ ] Strong parameters used
- [ ] No N+1 query patterns
- [ ] Validations in models
- [ ] Scopes for reusable queries

### Security
- [ ] No SQL interpolation with user input
- [ ] Mass assignment protected
- [ ] Proper authorization checks
- [ ] Sensitive data not logged
- [ ] CSRF tokens not disabled

### Tests
- [ ] New functionality has tests
- [ ] Edge cases covered
- [ ] Tests are isolated
- [ ] Factories used over fixtures
- [ ] Assertions are meaningful

---

## Common Issues to Catch

### Security
```ruby
# ❌ SQL Injection
User.where("name = '#{params[:name]}'")

# ✅ Safe query
User.where(name: params[:name])

# ❌ Mass assignment vulnerability
User.create(params[:user])

# ✅ Strong parameters
User.create(user_params)
```

### N+1 Queries
```ruby
# ❌ N+1 query
@posts = Post.all
@posts.each { |post| puts post.author.name }

# ✅ Eager loading
@posts = Post.includes(:author).all
```

### Fat Controllers
```ruby
# ❌ Logic in controller
def create
  @user = User.new(user_params)
  if @user.save
    UserMailer.welcome(@user).deliver_later
    AuditLog.create(action: 'user_created', user: @user)
    # ... more logic
  end
end

# ✅ Extract to service
def create
  result = Users::CreateService.call(user_params)
  if result.success?
    redirect_to result.user
  else
    render :new, status: :unprocessable_entity
  end
end
```

### Ruby Style
```ruby
# ❌ Non-idiomatic
if user != nil && user.active? == true
  do_something
end

# ✅ Idiomatic
return unless user&.active?
do_something

# ❌ Manual iteration
result = []
items.each { |i| result << i.name if i.valid? }

# ✅ Enumerable
result = items.select(&:valid?).map(&:name)
```

---

## Feedback Format

### GitHub Suggestion Block
````markdown
**🟠 High: N+1 Query**

This will execute a query for each post's author:

```suggestion
  @posts = Post.includes(:author).where(published: true)
```

Use `includes` to eager load the association.
````

### Inline Comment Format
```markdown
**�� Critical: SQL Injection**

File: `app/models/user.rb`, line 15

User input should not be interpolated into SQL:

```ruby
# Current (vulnerable)
where("email LIKE '%#{term}%'")

# Fixed
where("email LIKE ?", "%#{term}%")
```
```

---

## Report Format

### PR Review: `pr-review-[branch]-[YYYY-MM-DD].md`

```markdown
# PR Review: [Branch Name]

## Summary
- **Files Changed**: [Count]
- **Lines Changed**: +[added] / -[removed]
- **Verdict**: Approved / Request Changes / Needs Discussion

## Security
| Issue | File | Line | Fix |
|-------|------|------|-----|

## Code Quality
| Issue | File | Line | Fix |
|-------|------|------|-----|

## Performance
| Issue | File | Line | Fix |
|-------|------|------|-----|

## Tests
| Issue | File | Line | Fix |
|-------|------|------|-----|

## What's Good
- [Positive observation 1]
- [Positive observation 2]

## Questions
- [Clarification needed]
```

---

## Severity Guide

| Level | Icon | Action | Examples |
|-------|------|--------|----------|
| **Critical** | 🔴 | Block merge | Security vulnerabilities, data loss |
| **High** | 🟠 | Should fix | N+1 queries, logic errors, missing validations |
| **Medium** | 🟡 | Consider | Non-idiomatic code, missing tests |
| **Low** | 🟢 | Optional | Style preferences, minor optimizations |
