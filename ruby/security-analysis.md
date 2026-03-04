# Ruby/Rails Security Analysis

> **Purpose**: Comprehensive security audit for Ruby and Rails applications  
> **Best For**: Codex, Claude, ChatGPT, Copilot, Agents  
> **Scope**: OWASP Top 10, Rails security, authentication, authorization  
> **Last Updated**: 2026-03

---

## Mission

Help identify and fix **security vulnerabilities** in Ruby and Rails applications. Focus on common attack vectors, secure coding patterns, and Rails-specific security features.

---

## Guard Clauses

**If no code provided:**
```
NO_CODE_PROVIDED

Please provide Ruby/Rails code to analyze:
- Controllers, models, or views
- Authentication/authorization code
- API endpoints
- Configuration files
- Or describe the security concern

Include Rails version if relevant.
```

**If code appears secure:**
```
SECURITY_REVIEW_PASSED

✅ Security review complete — no critical issues found.

Checks performed:
- SQL injection: ✓ Protected
- XSS: ✓ Output escaped
- CSRF: ✓ Tokens validated
- Mass assignment: ✓ Strong parameters
- Authentication: ✓ Properly implemented
- Authorization: ✓ Access controlled

Recommendations for hardening:
[list any optional improvements]
```

---

## Quick Context Checklist

```
☐ Rails version
☐ Authentication solution (Devise, custom)
☐ Authorization solution (Pundit, CanCanCan)
☐ API authentication (JWT, API keys)
☐ User input sources
☐ Sensitive data handling
☐ Third-party integrations
☐ Deployment environment
```

---

## Copy-Paste Prompts

### Prompt: Full Security Audit
```text
Perform a security audit on this Rails code:

{{CODE}}

Rails version: {{VERSION}}
Authentication: {{AUTH_SOLUTION}}

Check for:
1. **Injection Attacks**
   - SQL injection
   - Command injection
   - LDAP injection

2. **Cross-Site Scripting (XSS)**
   - Reflected XSS
   - Stored XSS
   - DOM-based XSS

3. **Authentication Issues**
   - Weak passwords
   - Session management
   - Credential exposure

4. **Authorization Flaws**
   - Broken access control
   - IDOR vulnerabilities
   - Privilege escalation

5. **Data Protection**
   - Sensitive data exposure
   - Encryption at rest
   - Secure transmission

Provide severity ratings and fixes for each issue.
```

### Prompt: Review Authentication
```text
Review this authentication implementation:

{{CODE}}

Check for:
1. Password storage and hashing
2. Session management
3. Brute force protection
4. Password reset security
5. Multi-factor authentication
6. Remember me functionality
7. Logout implementation
```

### Prompt: Review Authorization
```text
Review this authorization implementation:

{{CODE}}

Authorization gem: {{PUNDIT_OR_CANCANCAN}}

Check for:
1. Policy/ability completeness
2. Default deny
3. IDOR vulnerabilities
4. Scope enforcement
5. Admin access controls
6. API authorization
```

### Prompt: API Security Review
```text
Review this API for security:

{{CODE}}

Authentication: {{JWT_OR_API_KEY}}

Check for:
1. Authentication mechanism
2. Rate limiting
3. Input validation
4. Output encoding
5. Error handling (no leaks)
6. CORS configuration
7. API versioning security
```

### Prompt: Fix Security Issue
```text
Fix this security vulnerability:

Code:
{{CODE}}

Vulnerability type: {{TYPE}}
Attack vector: {{VECTOR}}

Provide:
1. Secure implementation
2. Explanation of the fix
3. Additional hardening recommendations
4. Test cases for the fix
```

---

## SQL Injection

### Vulnerable Patterns

```ruby
# ❌ DANGEROUS: String interpolation
User.where("name = '#{params[:name]}'")
User.where("email LIKE '%#{params[:q]}%'")
Post.order("#{params[:sort]} #{params[:direction]}")

# ❌ DANGEROUS: Direct execution
ActiveRecord::Base.connection.execute(
  "SELECT * FROM users WHERE id = #{params[:id]}"
)

# ❌ DANGEROUS: find_by_sql with interpolation
User.find_by_sql("SELECT * FROM users WHERE name = '#{name}'")
```

### Secure Patterns

```ruby
# ✅ SAFE: Parameterized queries
User.where("name = ?", params[:name])
User.where(name: params[:name])
User.where("email LIKE ?", "%#{ActiveRecord::Base.sanitize_sql_like(params[:q])}%")

# ✅ SAFE: Whitelist for ordering
ALLOWED_SORT = %w[name email created_at].freeze
ALLOWED_DIR = %w[asc desc].freeze

sort = ALLOWED_SORT.include?(params[:sort]) ? params[:sort] : "created_at"
dir = ALLOWED_DIR.include?(params[:direction]) ? params[:direction] : "asc"
Post.order("#{sort} #{dir}")

# ✅ SAFE: Using Arel
Post.order(Post.arel_table[sort].send(dir))

# ✅ SAFE: Sanitized raw SQL
User.find_by_sql([
  "SELECT * FROM users WHERE name = ?",
  params[:name]
])
```

---

## Cross-Site Scripting (XSS)

### Vulnerable Patterns

```erb
<%# ❌ DANGEROUS: raw/html_safe on user input %>
<%= raw @user.bio %>
<%= @user.bio.html_safe %>
<%= sanitize(@user.content, tags: %w[script]) %>

<%# ❌ DANGEROUS: Unescaped in JavaScript %>
<script>
  var name = '<%= @user.name %>';  // XSS if name contains quotes
  var data = <%= @data.to_json %>;  // Unsafe without escaping
</script>

<%# ❌ DANGEROUS: href with user input %>
<a href="<%= @link.url %>">Click</a>  // javascript: URLs
```

### Secure Patterns

```erb
<%# ✅ SAFE: Default escaping (Rails does this automatically) %>
<%= @user.name %>
<%= @user.bio %>

<%# ✅ SAFE: Sanitize with allowed tags %>
<%= sanitize @user.bio, tags: %w[p br strong em], attributes: %w[class] %>

<%# ✅ SAFE: JavaScript escaping %>
<script>
  var name = <%= @user.name.to_json %>;
  var data = <%= json_escape(@data.to_json) %>;
</script>

<%# ✅ SAFE: Content Security Policy %>
<%= javascript_tag nonce: true do %>
  // Script with CSP nonce
<% end %>

<%# ✅ SAFE: URL validation %>
<% if @link.url.start_with?("https://", "http://", "/") %>
  <a href="<%= @link.url %>">Click</a>
<% end %>
```

### Content Security Policy

```ruby
# config/initializers/content_security_policy.rb
Rails.application.configure do
  config.content_security_policy do |policy|
    policy.default_src :self
    policy.font_src    :self, :https, :data
    policy.img_src     :self, :https, :data
    policy.object_src  :none
    policy.script_src  :self, :https
    policy.style_src   :self, :https, :unsafe_inline
    
    # Specify URI for violation reports
    policy.report_uri "/csp-violation-report"
  end
  
  # Generate nonce for scripts
  config.content_security_policy_nonce_generator = ->(request) {
    SecureRandom.base64(16)
  }
  
  config.content_security_policy_nonce_directives = %w[script-src]
end
```

---

## CSRF Protection

### Proper CSRF Configuration

```ruby
# app/controllers/application_controller.rb
class ApplicationController < ActionController::Base
  # Enable CSRF protection
  protect_from_forgery with: :exception
  
  # For APIs, use null_session instead
  # protect_from_forgery with: :null_session
end

# For specific controllers that need different handling
class ApiController < ApplicationController
  protect_from_forgery with: :null_session
  before_action :authenticate_api_token!
end
```

### CSRF in JavaScript/Turbo

```erb
<%# Ensure CSRF token is available %>
<%= csrf_meta_tags %>

<%# For fetch requests %>
<script>
  const csrfToken = document.querySelector('meta[name="csrf-token"]').content;
  
  fetch('/api/resource', {
    method: 'POST',
    headers: {
      'X-CSRF-Token': csrfToken,
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(data)
  });
</script>
```

---

## Authentication Security

### Secure Password Handling

```ruby
# ✅ Use has_secure_password
class User < ApplicationRecord
  has_secure_password
  
  # Password requirements
  validates :password, length: { minimum: 12 },
                       format: { 
                         with: /\A(?=.*[a-z])(?=.*[A-Z])(?=.*\d)/,
                         message: "must include uppercase, lowercase, and number"
                       },
                       if: :password_required?
  
  private
  
  def password_required?
    new_record? || password.present?
  end
end

# ✅ Secure password reset
class PasswordResetsController < ApplicationController
  def create
    user = User.find_by(email: params[:email].downcase)
    
    # Always show same message (prevent enumeration)
    if user
      user.generate_password_reset_token!
      PasswordMailer.reset(user).deliver_later
    end
    
    flash[:notice] = "If that email exists, you will receive reset instructions."
    redirect_to root_path
  end
  
  def update
    user = User.find_by_password_reset_token(params[:token])
    
    if user&.password_reset_valid? && user.update(password_params)
      user.clear_password_reset_token!
      sign_in(user)
      redirect_to root_path, notice: "Password updated!"
    else
      flash[:error] = "Invalid or expired reset token"
      redirect_to new_password_reset_path
    end
  end
end
```

### Session Security

```ruby
# config/initializers/session_store.rb
Rails.application.config.session_store :cookie_store,
  key: '_myapp_session',
  secure: Rails.env.production?,
  httponly: true,
  same_site: :lax,
  expire_after: 24.hours

# Regenerate session on login (prevent fixation)
class SessionsController < ApplicationController
  def create
    user = User.authenticate(params[:email], params[:password])
    
    if user
      reset_session  # Prevent session fixation
      session[:user_id] = user.id
      session[:created_at] = Time.current
      redirect_to dashboard_path
    else
      # Use generic message (prevent enumeration)
      flash[:error] = "Invalid email or password"
      render :new
    end
  end
  
  def destroy
    reset_session
    redirect_to root_path
  end
end

# Session timeout check
class ApplicationController < ActionController::Base
  before_action :check_session_timeout
  
  private
  
  def check_session_timeout
    if session[:created_at] && session[:created_at] < 24.hours.ago
      reset_session
      redirect_to login_path, alert: "Session expired. Please log in again."
    end
  end
end
```

### Brute Force Protection

```ruby
# Using Rack::Attack
# config/initializers/rack_attack.rb
class Rack::Attack
  # Throttle login attempts by IP
  throttle("logins/ip", limit: 5, period: 20.seconds) do |req|
    req.ip if req.path == "/login" && req.post?
  end
  
  # Throttle login attempts by email
  throttle("logins/email", limit: 5, period: 60.seconds) do |req|
    if req.path == "/login" && req.post?
      req.params.dig("user", "email")&.downcase
    end
  end
  
  # Block suspicious requests
  blocklist("block bad IPs") do |req|
    Blocklist.blocked?(req.ip)
  end
  
  # Custom response
  self.throttled_responder = ->(env) {
    retry_after = (env["rack.attack.match_data"] || {})[:period]
    [
      429,
      { "Content-Type" => "application/json", "Retry-After" => retry_after.to_s },
      [{ error: "Rate limit exceeded" }.to_json]
    ]
  }
end
```

---

## Authorization Security

### Pundit Patterns

```ruby
# app/policies/application_policy.rb
class ApplicationPolicy
  attr_reader :user, :record

  def initialize(user, record)
    @user = user
    @record = record
  end

  # Default deny all
  def index?
    false
  end

  def show?
    false
  end

  def create?
    false
  end

  def update?
    false
  end

  def destroy?
    false
  end

  class Scope
    attr_reader :user, :scope

    def initialize(user, scope)
      @user = user
      @scope = scope
    end

    def resolve
      raise NotImplementedError, "Define resolve in #{self.class}"
    end
  end
end

# app/policies/post_policy.rb
class PostPolicy < ApplicationPolicy
  def show?
    record.published? || record.user == user || user&.admin?
  end
  
  def update?
    record.user == user || user&.admin?
  end
  
  def destroy?
    record.user == user || user&.admin?
  end
  
  class Scope < ApplicationPolicy::Scope
    def resolve
      if user&.admin?
        scope.all
      elsif user
        scope.where(published: true).or(scope.where(user: user))
      else
        scope.where(published: true)
      end
    end
  end
end

# Controller usage
class PostsController < ApplicationController
  def show
    @post = Post.find(params[:id])
    authorize @post
  end
  
  def index
    @posts = policy_scope(Post)
  end
end
```

### Preventing IDOR

```ruby
# ❌ VULNERABLE: Direct ID lookup
class DocumentsController < ApplicationController
  def show
    @document = Document.find(params[:id])  # Any user can access any document!
  end
end

# ✅ SECURE: Scoped queries
class DocumentsController < ApplicationController
  def show
    @document = current_user.documents.find(params[:id])
  end
  
  # Or with authorization
  def show
    @document = Document.find(params[:id])
    authorize @document
  end
end

# ✅ SECURE: Using UUIDs instead of sequential IDs
class Document < ApplicationRecord
  # Use UUID primary key (harder to enumerate)
  # In migration: create_table :documents, id: :uuid
end
```

---

## Mass Assignment Protection

### Strong Parameters

```ruby
class UsersController < ApplicationController
  def create
    @user = User.new(user_params)
    # ...
  end
  
  def update
    @user = current_user
    @user.update(user_params)
    # ...
  end
  
  private
  
  def user_params
    # Whitelist allowed attributes
    params.require(:user).permit(:name, :email, :avatar)
  end
  
  # Different params for admin
  def admin_user_params
    params.require(:user).permit(:name, :email, :role, :admin, :verified)
  end
end

# ❌ DANGEROUS: Never do this
params.require(:user).permit!  # Allows ALL attributes
User.new(params[:user])        # No protection
```

### Nested Attributes

```ruby
class OrdersController < ApplicationController
  private
  
  def order_params
    params.require(:order).permit(
      :customer_name,
      :shipping_address,
      # Nested attributes - be explicit
      line_items_attributes: [:id, :product_id, :quantity, :_destroy]
    )
  end
end
```

---

## Sensitive Data Protection

### Credential Storage

```ruby
# ✅ Use Rails credentials
# Edit: rails credentials:edit

# config/credentials.yml.enc
aws:
  access_key_id: xxx
  secret_access_key: xxx
stripe:
  secret_key: xxx

# Access in code
Rails.application.credentials.aws[:access_key_id]
Rails.application.credentials.dig(:stripe, :secret_key)

# Environment-specific credentials
# rails credentials:edit --environment production
Rails.application.credentials.stripe[:secret_key]
```

### Filtering Sensitive Parameters

```ruby
# config/initializers/filter_parameter_logging.rb
Rails.application.config.filter_parameters += [
  :password,
  :password_confirmation,
  :credit_card,
  :ssn,
  :social_security,
  :secret,
  :token,
  :api_key,
  :access_token,
  :refresh_token
]

# Also filter in exception tracking
Sentry.init do |config|
  config.before_send = ->(event, hint) {
    event.request.data = "[FILTERED]" if event.request&.data
    event
  }
end
```

### Encryption at Rest

```ruby
# Rails 7+ encrypted attributes
class User < ApplicationRecord
  encrypts :ssn
  encrypts :medical_notes, deterministic: true  # Allows querying
end

# Custom encryption for older Rails
class User < ApplicationRecord
  attr_encrypted :ssn, key: Rails.application.credentials.encryption_key
end
```

---

## Security Headers

```ruby
# config/initializers/secure_headers.rb
# Using secure_headers gem

SecureHeaders::Configuration.default do |config|
  config.x_frame_options = "DENY"
  config.x_content_type_options = "nosniff"
  config.x_xss_protection = "1; mode=block"
  config.x_download_options = "noopen"
  config.x_permitted_cross_domain_policies = "none"
  config.referrer_policy = %w[strict-origin-when-cross-origin]
  
  config.csp = {
    default_src: %w['self'],
    script_src: %w['self'],
    style_src: %w['self' 'unsafe-inline'],
    img_src: %w['self' data: https:],
    font_src: %w['self'],
    connect_src: %w['self'],
    frame_ancestors: %w['none'],
    form_action: %w['self'],
    base_uri: %w['self']
  }
  
  config.hsts = "max-age=31536000; includeSubDomains"
end
```

---

## Security Checklist

```
Authentication:
☐ Strong password requirements
☐ Secure password storage (bcrypt)
☐ Session regeneration on login
☐ Session timeout
☐ Brute force protection
☐ Secure password reset flow

Authorization:
☐ Default deny policies
☐ Scoped queries (prevent IDOR)
☐ Admin actions protected
☐ API endpoints authorized

Input Validation:
☐ Strong parameters
☐ Input sanitization
☐ File upload validation
☐ SQL parameterization

Output Encoding:
☐ XSS prevention (auto-escaping)
☐ JSON encoding
☐ Content-Type headers

Configuration:
☐ CSRF protection enabled
☐ Security headers set
☐ Secrets in credentials
☐ SSL enforced
☐ Cookie security flags
```

---

## Severity Guide

| Severity | Vulnerability | Impact |
|----------|---------------|--------|
| 🔴 Critical | SQL injection | Full database access |
| 🔴 Critical | Command injection | Server compromise |
| 🔴 Critical | Authentication bypass | Account takeover |
| 🔴 Critical | Insecure deserialization | Remote code execution |
| 🟠 High | XSS (stored) | Session hijacking |
| 🟠 High | IDOR | Unauthorized data access |
| 🟠 High | CSRF | Unauthorized actions |
| 🟡 Medium | XSS (reflected) | Phishing |
| 🟡 Medium | Information disclosure | Reconnaissance |
| 🟢 Low | Missing security headers | Defense in depth |

---

## Report Template

```markdown
## Security Audit Report

### Application
- Rails version: [version]
- Ruby version: [version]
- Authentication: [solution]
- Authorization: [solution]

### Findings Summary
| Severity | Count |
|----------|-------|
| 🔴 Critical | |
| 🟠 High | |
| 🟡 Medium | |
| 🟢 Low | |

### Detailed Findings

#### [Severity] [Vulnerability Name]
- **Location**: [file:line]
- **Description**: [what was found]
- **Impact**: [potential damage]
- **Reproduction**: [steps]
- **Recommendation**: [fix]
- **Code Example**:
```ruby
# Vulnerable
...

# Fixed
...
```

### Recommendations
1. [Priority] [Recommendation]
   - Effort: [low/medium/high]
   - Impact: [description]
```

---

## Related Prompts

- [../python/security-analysis.md](../python/security-analysis.md) — Python security patterns
- [../generic/security-analysis.md](../generic/security-analysis.md) — General security
- [rails-active-record-performance-audit.md](rails-active-record-performance-audit.md) — Safe query patterns

---

*Last updated: 2026-01*
