# RSpec Test Generation — Ruby/Rails Testing

> **Purpose**: Generate RSpec tests for Ruby and Rails applications  
> **Best For**: Copilot, ChatGPT, Claude, Agents  
> **Scope**: RSpec, FactoryBot, model/request/feature specs  
> **Last Updated**: 2025-12

---

## Mission

Generate **practical, maintainable RSpec tests** that catch bugs, document behavior, and give confidence when making changes.

---

## Guard Clauses

**If no code provided:**
```
NO_CODE_PROVIDED

Please share Ruby code to test:
- Class or module
- Rails model, controller, or service
- Or describe what needs testing

I'll generate appropriate RSpec specs.
```

**If tests already comprehensive:**
```
TESTS_LOOK_GOOD

✅ **Well-Tested Code**

Test coverage is comprehensive:
- Happy paths covered ✓
- Edge cases tested ✓
- Error conditions handled ✓
- Tests are isolated ✓

Minor suggestions (optional):
[list any additional cases]
```

---

## Quick Context Checklist

```
☐ Code to test
☐ Test type (model, request, feature, unit)
☐ Existing test setup (factories, shared examples)
☐ Framework (Rails, pure Ruby)
☐ Special testing needs (external APIs, jobs)
```

---

## Copy-Paste Prompts

### Prompt: Generate Model Specs
```text
Generate RSpec model specs for:

{{MODEL_CODE}}

Include tests for:
1. Validations (presence, format, uniqueness)
2. Associations
3. Scopes
4. Instance methods
5. Class methods
6. Callbacks (if any)

Use FactoryBot for test data.
```

### Prompt: Generate Request Specs
```text
Generate RSpec request specs for:

{{CONTROLLER_CODE}}

Test each action:
1. Successful responses (200, 201)
2. Error responses (400, 401, 404, 422)
3. Authorization (if applicable)
4. Response body structure
5. Side effects (database changes, jobs)
```

### Prompt: Generate Service Specs
```text
Generate RSpec specs for this service object:

{{SERVICE_CODE}}

Test:
1. Success case with valid input
2. Failure cases with invalid input
3. Edge cases
4. Return value structure
5. Side effects
```

### Prompt: Add Missing Tests
```text
Review this code and existing tests:

Code:
{{CODE}}

Existing tests:
{{TESTS}}

Identify and generate tests for:
1. Untested code paths
2. Missing edge cases
3. Error conditions
4. Boundary conditions
```

---

## RSpec Setup

### Gemfile
```ruby
group :development, :test do
  gem 'rspec-rails', '~> 6.1'
  gem 'factory_bot_rails', '~> 6.4'
  gem 'faker', '~> 3.2'
end

group :test do
  gem 'shoulda-matchers', '~> 5.3'
  gem 'simplecov', '~> 0.22', require: false
  gem 'webmock', '~> 3.19'
  gem 'vcr', '~> 6.2'
end
```

### spec/rails_helper.rb
```ruby
require 'spec_helper'
ENV['RAILS_ENV'] ||= 'test'
require_relative '../config/environment'
abort("Database not in test mode!") if Rails.env.production?
require 'rspec/rails'

Dir[Rails.root.join('spec/support/**/*.rb')].each { |f| require f }

RSpec.configure do |config|
  config.fixture_path = Rails.root.join('spec/fixtures')
  config.use_transactional_fixtures = true
  config.infer_spec_type_from_file_location!
  config.filter_rails_from_backtrace!
  
  config.include FactoryBot::Syntax::Methods
end

Shoulda::Matchers.configure do |config|
  config.integrate do |with|
    with.test_framework :rspec
    with.library :rails
  end
end
```

---

## Test Patterns

### Model Spec
```ruby
# spec/models/user_spec.rb
RSpec.describe User, type: :model do
  describe 'validations' do
    it { is_expected.to validate_presence_of(:email) }
    it { is_expected.to validate_uniqueness_of(:email).case_insensitive }
    it { is_expected.to validate_length_of(:name).is_at_most(100) }
  end

  describe 'associations' do
    it { is_expected.to have_many(:posts).dependent(:destroy) }
    it { is_expected.to belong_to(:organization).optional }
  end

  describe 'scopes' do
    describe '.active' do
      let!(:active_user) { create(:user, active: true) }
      let!(:inactive_user) { create(:user, active: false) }

      it 'returns only active users' do
        expect(described_class.active).to eq([active_user])
      end
    end
  end

  describe '#full_name' do
    let(:user) { build(:user, first_name: 'John', last_name: 'Doe') }

    it 'returns combined first and last name' do
      expect(user.full_name).to eq('John Doe')
    end
  end
end
```

### Request Spec
```ruby
# spec/requests/posts_spec.rb
RSpec.describe 'Posts API', type: :request do
  let(:user) { create(:user) }
  let(:headers) { { 'Authorization' => "Bearer #{user.token}" } }

  describe 'GET /api/posts' do
    let!(:posts) { create_list(:post, 3, user: user) }

    it 'returns all posts' do
      get '/api/posts', headers: headers

      expect(response).to have_http_status(:ok)
      expect(json_response['data'].size).to eq(3)
    end

    context 'without authentication' do
      it 'returns unauthorized' do
        get '/api/posts'

        expect(response).to have_http_status(:unauthorized)
      end
    end
  end

  describe 'POST /api/posts' do
    let(:valid_params) { { post: { title: 'New Post', body: 'Content' } } }

    it 'creates a new post' do
      expect {
        post '/api/posts', params: valid_params, headers: headers
      }.to change(Post, :count).by(1)

      expect(response).to have_http_status(:created)
    end

    context 'with invalid params' do
      let(:invalid_params) { { post: { title: '' } } }

      it 'returns validation errors' do
        post '/api/posts', params: invalid_params, headers: headers

        expect(response).to have_http_status(:unprocessable_entity)
        expect(json_response['errors']).to include("Title can't be blank")
      end
    end
  end
end
```

### Service Spec
```ruby
# spec/services/users/create_service_spec.rb
RSpec.describe Users::CreateService do
  describe '#call' do
    subject(:service) { described_class.new(params) }

    context 'with valid params' do
      let(:params) { { email: 'test@example.com', name: 'Test User' } }

      it 'creates a user' do
        expect { service.call }.to change(User, :count).by(1)
      end

      it 'returns success result' do
        result = service.call

        expect(result).to be_success
        expect(result.user).to be_persisted
      end

      it 'sends welcome email' do
        expect { service.call }
          .to have_enqueued_mail(UserMailer, :welcome)
      end
    end

    context 'with invalid params' do
      let(:params) { { email: '', name: '' } }

      it 'does not create a user' do
        expect { service.call }.not_to change(User, :count)
      end

      it 'returns failure result with errors' do
        result = service.call

        expect(result).to be_failure
        expect(result.errors).to include("Email can't be blank")
      end
    end

    context 'with duplicate email' do
      let(:params) { { email: 'existing@example.com', name: 'Test' } }

      before { create(:user, email: 'existing@example.com') }

      it 'returns failure with duplicate error' do
        result = service.call

        expect(result).to be_failure
        expect(result.errors).to include('Email has already been taken')
      end
    end
  end
end
```

### Factory Example
```ruby
# spec/factories/users.rb
FactoryBot.define do
  factory :user do
    email { Faker::Internet.unique.email }
    name { Faker::Name.name }
    password { 'password123' }
    active { true }

    trait :inactive do
      active { false }
    end

    trait :admin do
      role { 'admin' }
    end

    trait :with_posts do
      transient do
        posts_count { 3 }
      end

      after(:create) do |user, evaluator|
        create_list(:post, evaluator.posts_count, user: user)
      end
    end
  end
end
```

---

## Testing Patterns Reference

| What to Test | Pattern |
|-------------|---------|
| Validations | `validate_presence_of`, `validate_uniqueness_of` |
| Associations | `have_many`, `belong_to`, `have_one` |
| Scopes | Create test data, verify returned records |
| Methods | Call method, verify return value |
| API endpoints | Request specs with response assertions |
| Services | Test success/failure, side effects |
| Jobs | `have_enqueued_job`, perform_now tests |
| Mailers | `have_enqueued_mail`, mail content tests |

---

## Report Format

### Test Coverage: `test-coverage-[YYYY-MM-DD].md`

```markdown
# Test Coverage Report

## Summary
- **Specs Generated**: [Count]
- **Coverage Type**: [Model/Request/Service]
- **Test Categories**: [List]

## Generated Specs

### Models
| Model | Tests | Status |
|-------|-------|--------|

### Services
| Service | Tests | Status |
|---------|-------|--------|

### Requests
| Endpoint | Tests | Status |
|----------|-------|--------|

## Missing Coverage
- [ ] Edge case: [description]
- [ ] Error condition: [description]

## Notes
[Any special considerations]
```

---

## Severity Guide

| Level | Icon | Examples |
|-------|------|----------|
| **Critical** | 🔴 | No tests for core functionality |
| **High** | 🟠 | Missing error case tests, untested validations |
| **Medium** | 🟡 | Missing edge cases, incomplete coverage |
| **Low** | 🟢 | Additional scenarios, refactoring tests |
