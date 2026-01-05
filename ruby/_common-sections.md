# Common Sections Reference — Ruby

> **Purpose**: Shared boilerplate for all Ruby/Rails prompts  
> **Usage**: Reference this file instead of duplicating content  
> **Last Updated**: 2026-01

---

## Quick Context Checklist

Use this condensed checklist instead of the full "Inputs Required" section:

```
☐ Branch: `git branch --show-current`
☐ Changes: `git diff main...HEAD --name-only`
☐ Diff: `git diff main...HEAD`
☐ Ruby version (3.2+ recommended)
☐ Rails version (if applicable)
☐ Key gems in use
☐ Pain points or constraints
```

---

## Standard Guard Clauses

Include these at the top of analysis output to handle edge cases:

### No Input Provided
```
NO_ACTIONABLE_INPUT

Unable to proceed without source material. Please provide:
- Ruby file(s) to analyze, OR
- Code pasted directly in the message, OR
- Repository URL with specific files to review

Example: "Review app/models/user.rb for N+1 queries"
```

### Empty Diff / No Changes
```
NO_CHANGES_DETECTED

No code changes found between branches.

Checked:
- `git diff main...HEAD` returned empty
- No modified Ruby files detected

Next steps:
- Verify you're on the correct branch
- Ensure changes are committed
- Try: `git status` to see uncommitted changes
```

### Analysis Complete - No Issues
```
NO_ISSUES_FOUND

✅ Analysis complete — no significant issues detected.

Summary:
- Files scanned: {{FILE_COUNT}}
- Checks performed: {{CHECK_TYPES}}
- Result: Code meets quality standards

Recommendation: Proceed with confidence.
```

### Analysis Complete - With Findings
```
ANALYSIS_COMPLETE

📋 Found {{ISSUE_COUNT}} items requiring attention.

Breakdown:
- 🔴 Critical: {{CRITICAL_COUNT}}
- 🟠 High: {{HIGH_COUNT}}
- 🟡 Medium: {{MEDIUM_COUNT}}
- 🟢 Low: {{LOW_COUNT}}

See detailed findings below.
```

---

## Severity Levels

Use consistent severity across all prompts:

| Level | Label | Criteria | Action |
|-------|-------|----------|--------|
| 🔴 | **Critical** | Security vulnerability, data loss risk, system crash | Fix immediately before merge |
| 🟠 | **High** | Bugs, significant performance issues, breaking changes | Fix before merge |
| 🟡 | **Medium** | Code quality, minor performance, maintainability | Should fix, can be follow-up |
| 🟢 | **Low** | Style, minor improvements, nice-to-haves | Optional, track for later |

---

## Standard Output Formats

### Code Issue Format

```markdown
### 🔴 [Issue Title]

**Location:** `path/to/file.rb:42`

**Problem:**
[Description of what's wrong]

**Current Code:**
```ruby
# Current problematic implementation
```

**Suggested Fix:**
```ruby
# Improved implementation
```

**Why This Matters:**
[Impact on security/performance/maintainability]
```

### Code Diff Format

For suggesting changes, use GitHub-compatible diff:

```diff
# path/to/file.rb
- old_code_line
+ new_code_line
```

---

## Report Template

Use this structure for comprehensive reviews:

```markdown
## Ruby Code Review Report

### Summary
| Metric | Value |
|--------|-------|
| Files Reviewed | X |
| Issues Found | X |
| Critical | X |
| High | X |
| Medium | X |
| Low | X |

### Environment
- Ruby: [version]
- Rails: [version if applicable]
- Key Gems: [relevant gems]

### Critical Issues
[List critical issues]

### High Priority Issues
[List high priority issues]

### Medium Priority Issues
[List medium priority issues]

### Low Priority Issues
[List low priority issues]

### Recommendations
1. [Priority action items]
```

---

## Ruby Version Patterns

### Ruby 3.2+ Features to Prefer

```ruby
# Pattern matching (3.0+)
case response
in { status: 200, body: }
  process(body)
in { status: 404 }
  handle_not_found
in { status: 500.. }
  handle_error
end

# Endless methods (3.0+)
def full_name = "#{first_name} #{last_name}"

# Data classes (3.2+)
User = Data.define(:name, :email) do
  def display = "#{name} <#{email}>"
end

# Anonymous block arguments (3.1+)
users.map { _1.name.upcase }
```

### Rails 7+ Features to Prefer

```ruby
# Hotwire/Turbo patterns
turbo_stream.replace @post
turbo_stream.append "posts", partial: "posts/post", locals: { post: @post }

# Strict loading (prevent N+1)
class Post < ApplicationRecord
  self.strict_loading_by_default = true
end

# Async queries
users = User.where(active: true).load_async
posts = Post.recent.load_async
# ... other work ...
users.each { |u| process(u) }  # waits for query if not done

# Solid Queue / Active Job patterns
class ProcessOrderJob < ApplicationJob
  queue_as :critical
  retry_on StandardError, wait: :exponentially_longer, attempts: 5
  
  def perform(order_id)
    # ...
  end
end
```

---

## Common Code Smells

### N+1 Queries
```ruby
# ❌ Bad
users.each { |u| puts u.posts.count }

# ✅ Good
users.includes(:posts).each { |u| puts u.posts.size }
```

### Fat Controllers
```ruby
# ❌ Bad - logic in controller
def create
  @user = User.new(user_params)
  @user.status = calculate_status(params)
  notify_admin if @user.premium?
  # ...
end

# ✅ Good - extract to service
def create
  result = Users::CreateService.call(user_params)
  # ...
end
```

### Missing Validations
```ruby
# ❌ Bad - validate in controller/service
def create
  return error unless params[:email].match?(EMAIL_REGEX)
  User.create!(params)
end

# ✅ Good - validate in model
class User < ApplicationRecord
  validates :email, presence: true, format: { with: URI::MailTo::EMAIL_REGEXP }
end
```

---

## Gem Recommendations

### Essential Development Gems

```ruby
# Gemfile
group :development, :test do
  gem "rspec-rails"
  gem "factory_bot_rails"
  gem "faker"
  gem "rubocop-rails", require: false
  gem "rubocop-rspec", require: false
  gem "rubocop-performance", require: false
  gem "bullet"  # N+1 detection
  gem "brakeman", require: false  # Security scanning
end

group :development do
  gem "annotate"
  gem "better_errors"
  gem "binding_of_caller"
end
```

### Modern Alternatives

| Old Gem | Modern Alternative | Notes |
|---------|-------------------|-------|
| Devise | Rodauth | More secure, modular |
| Sidekiq (paid) | Solid Queue | Built into Rails 8 |
| Webpacker | Vite Ruby, Propshaft | Simpler, faster |
| CarrierWave | Active Storage | Built into Rails |
| Paperclip | Active Storage | Built into Rails |

---

## Testing Standards

### RSpec Structure

```ruby
RSpec.describe User, type: :model do
  describe "validations" do
    it { is_expected.to validate_presence_of(:email) }
  end
  
  describe "#full_name" do
    subject { user.full_name }
    
    let(:user) { build(:user, first_name: "John", last_name: "Doe") }
    
    it { is_expected.to eq("John Doe") }
  end
  
  describe ".active" do
    it "returns only active users" do
      active = create(:user, status: :active)
      _inactive = create(:user, status: :inactive)
      
      expect(described_class.active).to contain_exactly(active)
    end
  end
end
```

### Factory Patterns

```ruby
FactoryBot.define do
  factory :user do
    sequence(:email) { |n| "user#{n}@example.com" }
    first_name { Faker::Name.first_name }
    last_name { Faker::Name.last_name }
    
    trait :admin do
      role { :admin }
    end
    
    trait :with_posts do
      transient do
        posts_count { 3 }
      end
      
      after(:create) do |user, evaluator|
        create_list(:post, evaluator.posts_count, author: user)
      end
    end
  end
end
```

---

## Performance Baselines

| Metric | Target | Concern |
|--------|--------|---------|
| Page load | < 200ms | > 500ms |
| API response | < 100ms | > 300ms |
| Background job | < 30s | > 60s |
| Database query | < 50ms | > 200ms |
| N+1 queries | 0 | Any |
| Memory per request | < 50MB | > 100MB |

---

*Last updated: 2026-01*
