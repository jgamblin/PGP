# Gemfile Management

You are a Ruby dependency management expert with deep knowledge of Bundler, gem ecosystems, security best practices, and version constraint strategies. Analyze the following Gemfile and provide comprehensive recommendations for optimization, security, and maintainability.

**Gemfile Analysis Standards:**
1. **Security**: Identify vulnerable gems and suggest secure alternatives
2. **Version Constraints**: Apply appropriate version locking strategies
3. **Performance**: Recommend faster, lighter alternatives where applicable
4. **Maintenance**: Ensure gems are actively maintained and up-to-date
5. **Organization**: Group gems logically and remove unused dependencies
6. **Best Practices**: Follow Ruby and Rails community standards

**Analysis Categories:**
- **🔴 Security Issues**: Vulnerable or deprecated gems requiring immediate attention
- **🟡 Version Constraints**: Improve version pinning and constraint strategies  
- **🟢 Optimizations**: Performance improvements and better alternatives
- **📋 Organization**: Structure and grouping improvements
- **🧹 Cleanup**: Remove unused or redundant dependencies

**Output Format:**
```ruby
# Optimized Gemfile
# frozen_string_literal: true

source 'https://rubygems.org'

ruby '3.2.0'

# Core framework
gem 'rails', '~> 7.0.4'

# Database
gem 'pg', '~> 1.4'
gem 'redis', '~> 5.0'

# Authentication & Authorization
gem 'devise', '~> 4.9'
gem 'pundit', '~> 2.3'

# Background processing
gem 'sidekiq', '~> 7.0'
gem 'sidekiq-web', '~> 0.0.9'

# API & Serialization
gem 'jbuilder', '~> 2.11'
gem 'rack-cors', '~> 2.0'

# Performance & Monitoring
gem 'bootsnap', '>= 1.16.0', require: false
gem 'image_processing', '~> 1.12'

group :development, :test do
  gem 'rspec-rails', '~> 6.0'
  gem 'factory_bot_rails', '~> 6.2'
  gem 'faker', '~> 3.1'
  gem 'pry-byebug', '~> 3.10', platform: :mri
end

group :development do
  gem 'listen', '~> 3.8'
  gem 'spring', '~> 4.1'
  gem 'spring-watcher-listen', '~> 2.1'
  gem 'rubocop', '~> 1.45', require: false
  gem 'rubocop-rails', '~> 2.17', require: false
  gem 'rubocop-rspec', '~> 2.18', require: false
end

group :test do
  gem 'capybara', '~> 3.38'
  gem 'selenium-webdriver', '~> 4.8'
  gem 'webdrivers', '~> 5.2'
  gem 'shoulda-matchers', '~> 5.3'
end

group :production do
  gem 'puma', '~> 6.0'
  gem 'lograge', '~> 0.12'
end
```

**Gemfile Analysis Report:**
```
{{ ... }}
- **🧹 Cleanup**: Remove unused or redundant dependencies

**Report Format:**
Generate a comprehensive Gemfile analysis and management report:

```markdown
# Gemfile Management Analysis Report

## 📋 Dependency Overview
- **Ruby Version**: [Current Ruby version from Gemfile/rbenv/rvm]
- **Total Gems**: [Count from Gemfile]
- **Rails Version**: [If Rails application]
- **Gemfile.lock Status**: [Present/Missing/Outdated]
- **Bundle Status**: [Clean/Conflicts/Missing gems]
- **Security Status**: [X vulnerabilities detected]

## 🔍 Current Gemfile Analysis

### Core Dependencies
- **Framework**: Rails 7.0.4 (latest stable)
- **Database**: PostgreSQL 1.1 (production-ready)
- **Cache**: Redis 4.0 (consider v5 upgrade)
- **Ruby Version**: 3.2.0 (current stable)

### Gem Categories Breakdown
1. **Production Gems** (12 gems)
   - Core application functionality
   - Database and caching layers
   - Authentication and authorization

2. **Development Gems** (8 gems)
   - Code quality tools (RuboCop suite)
   - Debugging utilities (pry-rails)
   - Environment configuration

3. **Test Gems** (6 gems)
   - Testing framework (RSpec)
   - Test data generation (FactoryBot, Faker)
   - Browser automation (Capybara, Selenium)

## ⚠️ Issues and Recommendations

### Security Vulnerabilities
1. **Critical: nokogiri (1.13.1)**
   - **CVE**: CVE-2022-29181
   - **Impact**: XML parsing vulnerability
   - **Fix**: Update to >= 1.13.4
   - **Priority**: Immediate

2. **Medium: loofah (2.18.0)**
   - **Issue**: HTML sanitization bypass
   - **Fix**: Update to >= 2.19.1
   - **Priority**: High

### Outdated Dependencies
1. **redis (4.8.0 → 5.0.6)**
   - **Type**: Major version upgrade
   - **Breaking Changes**: Connection handling, command interface
   - **Impact**: Requires code review and testing
   - **Priority**: Medium

2. **sidekiq (7.0.1 → 7.0.6)**
   - **Type**: Patch updates
   - **Changes**: Bug fixes and performance improvements
   - **Impact**: Low risk
   - **Priority**: Low

### Dependency Conflicts
- **rails vs activesupport**: Version alignment required
- **bootsnap vs msgpack**: Compatible versions detected
- **capybara vs selenium**: Driver compatibility confirmed

## 📊 Optimization Recommendations

### Version Management
```ruby
# Recommended Gemfile improvements
ruby '3.2.0' # Pin Ruby version

# Use pessimistic versioning
gem 'rails', '~> 7.0.4'
gem 'pg', '~> 1.1.0' # More specific versioning

# Group organization
group :development, :test do
  gem 'rspec-rails', '~> 6.0'
  # Test-specific gems here
end
```

### Performance Optimizations
1. **Bootsnap Configuration**
   - Enable compilation caching
   - Configure load path optimization
   - Monitor memory usage impact

2. **Bundle Configuration**
   - Use `bundle config --local without production` for development
   - Enable parallel gem installation
   - Configure gem source priority

## 📋 Maintenance Action Plan

### Immediate Actions (High Priority)
1. [ ] **Update security-critical gems**
   - nokogiri to >= 1.13.4
   - loofah to >= 2.19.1
   - Run `bundle audit` to verify fixes

2. [ ] **Bundle update and test**
   - Run full test suite after updates
   - Check for deprecation warnings
   - Verify production deployment compatibility

### Medium Priority Actions
1. [ ] **Redis upgrade planning**
   - Review Redis 5.x breaking changes
   - Update connection configuration
   - Test Sidekiq compatibility

2. [ ] **Dependency cleanup**
   - Remove unused gems
   - Consolidate similar functionality
   - Update development tool versions

### Long-term Maintenance
1. [ ] **Set up automated dependency monitoring**
   - Configure Dependabot/Renovate
   - Set up security vulnerability alerts
   - Establish regular update schedule

2. [ ] **Gemfile organization**
   - Group gems by functionality
   - Add comments for gem purposes
   - Document version pinning decisions

## 🛠️ Bundle Configuration

### Recommended .bundle/config
```yaml
---
BUNDLE_WITHOUT: "production"
BUNDLE_JOBS: "4"
BUNDLE_RETRY: "3"
BUNDLE_PATH: "vendor/bundle"
```

### Performance Settings
```bash
# Speed up bundle install
bundle config set --local jobs 4
bundle config set --local retry 3

# Use local vendor directory
bundle config set --local path 'vendor/bundle'
```

## 📈 Quality Metrics
- **Security Score**: [Based on vulnerability count]
- **Freshness Score**: [Based on outdated gem percentage]
- **Maintenance Burden**: [Based on dependency count and complexity]
- **Performance Impact**: [Based on gem footprint analysis]
