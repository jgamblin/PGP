# Ruby Project Repository — Setup & Structure

> **Purpose**: Set up and organize Ruby/Rails project repositories  
> **Best For**: Copilot, ChatGPT, Claude, Agents  
> **Scope**: Project structure, configuration, tooling  
> **Last Updated**: 2025-12

---

## Mission

Help users **create well-structured Ruby projects** with proper configuration, tooling, and best practices from the start.

---

## Guard Clauses

**If no project context:**
```
NO_PROJECT_CONTEXT

To help set up your Ruby project, I need:
- Project type (gem, Rails app, API, CLI)
- Ruby version
- Key features/dependencies
- Team size (solo, small team)

Or describe what you're building.
```

**If project is well-structured:**
```
PROJECT_LOOKS_GOOD

✅ **Well-Structured Ruby Project**

Your project follows best practices:
- Clear directory structure ✓
- Proper configuration files ✓
- Testing setup complete ✓
- Documentation present ✓

Minor suggestions (optional):
[list any refinements]
```

---

## Quick Context Checklist

```
☐ Project type (gem, Rails, Sinatra, CLI)
☐ Ruby version
☐ Database (if applicable)
☐ Key features
☐ Testing framework preference
```

---

## Copy-Paste Prompts

### Prompt: Analyze Project Structure
```text
Analyze this Ruby project structure:

{{TREE_OUTPUT}}

Evaluate:
1. Directory organization
2. Configuration completeness
3. Testing setup
4. Documentation
5. Missing essential files

Recommend improvements.
```

### Prompt: Create New Project
```text
Set up a new Ruby project:

Type: {{PROJECT_TYPE}}
Ruby: {{RUBY_VERSION}}
Features: {{FEATURES}}
Database: {{DATABASE}}

Include:
- Directory structure
- Gemfile with essentials
- Configuration files
- Testing setup
- CI configuration
- README template
```

### Prompt: Add Tooling
```text
Add development tooling to my Ruby project:

Current setup:
{{CURRENT_STRUCTURE}}

Add:
- RuboCop configuration
- RSpec setup
- CI/CD pipeline
- Pre-commit hooks
- Code coverage
```

### Prompt: Rails API Setup
```text
Set up a new Rails API project:

Ruby: {{RUBY_VERSION}}
Rails: {{RAILS_VERSION}}
Database: {{DATABASE}}
Authentication: {{AUTH_METHOD}}

Include:
- API-only configuration
- Serializer setup
- Authentication
- Versioning strategy
- Docker setup
```

---

## Project Structures

### Ruby Gem
```
my_gem/
├── lib/
│   ├── my_gem.rb              # Main entry point
│   └── my_gem/
│       ├── version.rb         # Version constant
│       ├── configuration.rb   # Config module
│       └── client.rb          # Main class
├── spec/
│   ├── spec_helper.rb
│   ├── my_gem_spec.rb
│   └── my_gem/
│       └── client_spec.rb
├── .github/
│   └── workflows/
│       └── ci.yml
├── .rubocop.yml
├── .rspec
├── Gemfile
├── my_gem.gemspec
├── LICENSE
├── README.md
└── CHANGELOG.md
```

### Rails Application
```
my_app/
├── app/
│   ├── controllers/
│   │   └── application_controller.rb
│   ├── models/
│   │   └── application_record.rb
│   ├── services/              # Service objects
│   │   └── base_service.rb
│   ├── serializers/           # JSON serializers
│   └── jobs/
├── config/
│   ├── application.rb
│   ├── database.yml
│   ├── routes.rb
│   └── initializers/
├── db/
│   ├── migrate/
│   └── seeds.rb
├── spec/
│   ├── rails_helper.rb
│   ├── spec_helper.rb
│   ├── factories/
│   ├── models/
│   ├── requests/
│   └── services/
├── .github/
│   └── workflows/
│       └── ci.yml
├── .rubocop.yml
├── .rspec
├── Dockerfile
├── docker-compose.yml
├── Gemfile
└── README.md
```

### CLI Application
```
my_cli/
├── lib/
│   ├── my_cli.rb
│   └── my_cli/
│       ├── cli.rb            # Thor/OptionParser setup
│       ├── commands/
│       │   ├── base.rb
│       │   └── generate.rb
│       └── version.rb
├── exe/
│   └── my_cli                # Executable
├── spec/
│   ├── spec_helper.rb
│   └── my_cli/
│       └── cli_spec.rb
├── .rubocop.yml
├── Gemfile
├── my_cli.gemspec
└── README.md
```

---

## Essential Configuration Files

### .ruby-version
```
3.3.0
```

### .rubocop.yml
```yaml
require:
  - rubocop-rails
  - rubocop-rspec

AllCops:
  TargetRubyVersion: 3.3
  NewCops: enable
  Exclude:
    - 'db/schema.rb'
    - 'bin/*'
    - 'vendor/**/*'
    - 'node_modules/**/*'

Style/Documentation:
  Enabled: false

Style/FrozenStringLiteralComment:
  Enabled: true

Metrics/BlockLength:
  Exclude:
    - 'spec/**/*'
    - 'config/routes.rb'

Metrics/MethodLength:
  Max: 15

Layout/LineLength:
  Max: 120
```

### .rspec
```
--require spec_helper
--format documentation
--color
```

### spec/spec_helper.rb
```ruby
# frozen_string_literal: true

require 'simplecov'
SimpleCov.start do
  add_filter '/spec/'
  add_group 'Models', 'app/models'
  add_group 'Services', 'app/services'
end

RSpec.configure do |config|
  config.expect_with :rspec do |expectations|
    expectations.include_chain_clauses_in_custom_matcher_descriptions = true
  end

  config.mock_with :rspec do |mocks|
    mocks.verify_partial_doubles = true
  end

  config.shared_context_metadata_behavior = :apply_to_host_groups
  config.filter_run_when_matching :focus
  config.disable_monkey_patching!
  config.order = :random
  Kernel.srand config.seed
end
```

### .github/workflows/ci.yml
```yaml
name: CI

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    
    services:
      postgres:
        image: postgres:15
        env:
          POSTGRES_PASSWORD: postgres
        ports:
          - 5432:5432
        options: >-
          --health-cmd pg_isready
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5

    steps:
      - uses: actions/checkout@v4
      
      - uses: ruby/setup-ruby@v1
        with:
          ruby-version: '3.3'
          bundler-cache: true
      
      - name: Setup database
        env:
          RAILS_ENV: test
          DATABASE_URL: postgres://postgres:postgres@localhost:5432/test
        run: |
          bundle exec rails db:create
          bundle exec rails db:schema:load
      
      - name: Run tests
        env:
          RAILS_ENV: test
          DATABASE_URL: postgres://postgres:postgres@localhost:5432/test
        run: bundle exec rspec
      
      - name: Run linter
        run: bundle exec rubocop

  security:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: ruby/setup-ruby@v1
        with:
          ruby-version: '3.3'
          bundler-cache: true
      - run: bundle exec bundler-audit check --update
      - run: bundle exec brakeman -q
```

### Dockerfile
```dockerfile
FROM ruby:3.3-slim

RUN apt-get update -qq && \
    apt-get install -y build-essential libpq-dev && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY Gemfile Gemfile.lock ./
RUN bundle install --jobs 4 --retry 3

COPY . .

EXPOSE 3000
CMD ["bundle", "exec", "rails", "server", "-b", "0.0.0.0"]
```

### docker-compose.yml
```yaml
version: '3.8'

services:
  app:
    build: .
    ports:
      - "3000:3000"
    environment:
      - DATABASE_URL=postgres://postgres:postgres@db:5432/app_development
      - REDIS_URL=redis://redis:6379/0
    depends_on:
      - db
      - redis
    volumes:
      - .:/app
      - bundle:/usr/local/bundle

  db:
    image: postgres:15
    environment:
      POSTGRES_PASSWORD: postgres
    volumes:
      - postgres_data:/var/lib/postgresql/data

  redis:
    image: redis:7

volumes:
  postgres_data:
  bundle:
```

---

## Report Format

### Project Analysis: `project-analysis-[YYYY-MM-DD].md`

```markdown
# Project Analysis

## Overview
- **Type**: [Gem/Rails/CLI]
- **Ruby Version**: [Version]
- **Health Score**: [X/10]

## Structure Analysis
| Aspect | Status | Notes |
|--------|--------|-------|
| Directory Layout | ✅/⚠️/❌ | |
| Configuration | ✅/⚠️/❌ | |
| Testing | ✅/⚠️/❌ | |
| CI/CD | ✅/⚠️/❌ | |
| Documentation | ✅/⚠️/❌ | |

## Missing Files
- [ ] .rubocop.yml
- [ ] CI configuration
- [ ] README sections

## Recommendations
1. [Priority fix]
2. [Should add]
3. [Nice to have]
```

---

## Severity Guide

| Level | Icon | Examples |
|-------|------|----------|
| **Critical** | 🔴 | No tests, security config missing |
| **High** | 🟠 | Missing CI, no linting |
| **Medium** | 🟡 | Incomplete docs, config improvements |
| **Low** | 🟢 | Style preferences, optional tooling |
