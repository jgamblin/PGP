# Service Objects & Domain Logic — Rails Architecture

> **Purpose**: Extract business logic from controllers/models into service objects  
> **Best For**: Copilot, ChatGPT, Claude, Agents  
> **Scope**: Service objects, form objects, domain logic patterns  
> **Last Updated**: 2025-12

---

## Mission

Help refactor **fat controllers and models** into clean, testable service objects. Apply separation of concerns and improve Rails architecture.

---

## Guard Clauses

**If no code provided:**
```
NO_CODE_PROVIDED

Please share Rails code to refactor:
- Fat controller action
- Complex model method
- Or describe the business logic

I'll suggest service object extraction.
```

**If code is already clean:**
```
CODE_LOOKS_GOOD

✅ **Clean Architecture**

Code follows good patterns:
- Single responsibility ✓
- Testable ✓
- Controllers are thin ✓
- Models are focused ✓

Minor suggestions (optional):
[list any refinements]
```

---

## Quick Context Checklist

```
☐ Controller or model code to refactor
☐ Business logic description
☐ Current pain points
☐ Related models/services
☐ Testing requirements
```

---

## Copy-Paste Prompts

### Prompt: Extract Service Object
```text
Extract this controller logic into a service object:

{{CONTROLLER_CODE}}

Requirements:
1. Create service with single public method
2. Return result object (success/failure)
3. Handle errors gracefully
4. Make it testable

Include the RSpec spec.
```

### Prompt: Refactor Fat Controller
```text
This controller is too fat. Refactor it:

{{CONTROLLER_CODE}}

Goals:
- Extract business logic to services
- Keep controller to HTTP concerns only
- Maintain same behavior
- Improve testability
```

### Prompt: Create Form Object
```text
Create a form object for this complex form:

{{FORM_REQUIREMENTS}}

Related models: {{MODELS}}

Include:
- Validations
- Attribute handling
- Save method
- Error handling
```

### Prompt: Domain Logic Organization
```text
Help organize domain logic for this feature:

{{FEATURE_DESCRIPTION}}

Current code:
{{CODE}}

Suggest:
1. Service object structure
2. Where each piece of logic belongs
3. How services interact
4. Testing strategy
```

---

## When to Use Service Objects

### Signs You Need a Service Object

| Sign | Example |
|------|---------|
| Controller > 10 lines | Complex `create` action |
| Multiple model operations | Create user + send email + log |
| External API calls | Payment processing |
| Complex conditionals | Business rules |
| Hard to test | Logic buried in controller |
| Reusable logic | Same flow in multiple places |

### Signs to Keep in Model

| Keep in Model | Example |
|--------------|---------|
| Validations | `validates :email, presence: true` |
| Associations | `has_many :posts` |
| Simple scopes | `scope :active, -> { where(active: true) }` |
| Attribute logic | `def full_name` |

---

## Service Object Patterns

### Basic Service Object
```ruby
# app/services/users/create_service.rb
module Users
  class CreateService
    def initialize(params)
      @params = params
    end

    def call
      user = User.new(@params)
      
      if user.save
        send_welcome_email(user)
        Result.success(user: user)
      else
        Result.failure(errors: user.errors.full_messages)
      end
    end

    private

    def send_welcome_email(user)
      UserMailer.welcome(user).deliver_later
    end
  end
end

# Usage in controller
def create
  result = Users::CreateService.new(user_params).call

  if result.success?
    redirect_to result.user
  else
    @errors = result.errors
    render :new, status: :unprocessable_entity
  end
end
```

### Result Object
```ruby
# app/services/result.rb
class Result
  attr_reader :data, :errors

  def initialize(success:, data: {}, errors: [])
    @success = success
    @data = data
    @errors = errors
  end

  def self.success(data = {})
    new(success: true, data: data)
  end

  def self.failure(errors: [], data: {})
    new(success: false, errors: Array(errors), data: data)
  end

  def success?
    @success
  end

  def failure?
    !@success
  end

  def method_missing(method, *args)
    data[method] || data[method.to_s] || super
  end

  def respond_to_missing?(method, include_private = false)
    data.key?(method) || data.key?(method.to_s) || super
  end
end
```

### Service with Dependencies
```ruby
# app/services/orders/process_service.rb
module Orders
  class ProcessService
    def initialize(order, payment_gateway: PaymentGateway.new)
      @order = order
      @payment_gateway = payment_gateway
    end

    def call
      return Result.failure(errors: ['Order invalid']) unless @order.valid?

      ActiveRecord::Base.transaction do
        charge_payment
        update_inventory
        send_confirmation
        Result.success(order: @order)
      end
    rescue PaymentError => e
      Result.failure(errors: [e.message])
    end

    private

    def charge_payment
      @payment_gateway.charge(@order.total, @order.payment_method)
    end

    def update_inventory
      @order.line_items.each do |item|
        item.product.decrement!(:stock, item.quantity)
      end
    end

    def send_confirmation
      OrderMailer.confirmation(@order).deliver_later
    end
  end
end
```

### Form Object
```ruby
# app/forms/registration_form.rb
class RegistrationForm
  include ActiveModel::Model
  include ActiveModel::Attributes

  attribute :email, :string
  attribute :password, :string
  attribute :company_name, :string
  attribute :plan, :string

  validates :email, presence: true, format: { with: URI::MailTo::EMAIL_REGEXP }
  validates :password, presence: true, length: { minimum: 8 }
  validates :company_name, presence: true
  validates :plan, inclusion: { in: %w[basic pro enterprise] }

  def save
    return false unless valid?

    ActiveRecord::Base.transaction do
      create_company
      create_user
      create_subscription
      true
    end
  rescue ActiveRecord::RecordInvalid => e
    errors.add(:base, e.message)
    false
  end

  def user
    @user
  end

  private

  def create_company
    @company = Company.create!(name: company_name)
  end

  def create_user
    @user = @company.users.create!(email: email, password: password)
  end

  def create_subscription
    @company.create_subscription!(plan: plan)
  end
end
```

---

## Controller Refactoring

### Before: Fat Controller
```ruby
# ❌ Too much logic in controller
class OrdersController < ApplicationController
  def create
    @order = current_user.orders.new(order_params)
    
    if @order.save
      @order.line_items.each do |item|
        product = item.product
        product.stock -= item.quantity
        product.save!
      end
      
      payment = PaymentGateway.charge(
        amount: @order.total,
        card: params[:card_token]
      )
      
      if payment.success?
        @order.update!(payment_id: payment.id, status: 'paid')
        OrderMailer.confirmation(@order).deliver_later
        redirect_to @order, notice: 'Order placed!'
      else
        @order.destroy
        flash[:error] = payment.error_message
        render :new
      end
    else
      render :new
    end
  end
end
```

### After: Clean Controller + Service
```ruby
# ✅ Thin controller
class OrdersController < ApplicationController
  def create
    result = Orders::CreateService.new(
      user: current_user,
      params: order_params,
      card_token: params[:card_token]
    ).call

    if result.success?
      redirect_to result.order, notice: 'Order placed!'
    else
      @order = result.order
      @errors = result.errors
      render :new, status: :unprocessable_entity
    end
  end
end

# ✅ Service handles business logic
module Orders
  class CreateService
    def initialize(user:, params:, card_token:)
      @user = user
      @params = params
      @card_token = card_token
    end

    def call
      @order = @user.orders.new(@params)
      
      return Result.failure(order: @order, errors: @order.errors.full_messages) unless @order.save

      process_order
    end

    private

    def process_order
      ActiveRecord::Base.transaction do
        update_inventory
        process_payment
        send_confirmation
        Result.success(order: @order)
      end
    rescue PaymentError => e
      @order.destroy
      Result.failure(order: @order, errors: [e.message])
    end

    def update_inventory
      InventoryService.new(@order).decrement
    end

    def process_payment
      payment = PaymentGateway.charge(amount: @order.total, card: @card_token)
      raise PaymentError, payment.error_message unless payment.success?
      @order.update!(payment_id: payment.id, status: 'paid')
    end

    def send_confirmation
      OrderMailer.confirmation(@order).deliver_later
    end
  end
end
```

---

## Directory Structure

```
app/
├── services/
│   ├── result.rb              # Shared result object
│   ├── base_service.rb        # Optional base class
│   ├── users/
│   │   ├── create_service.rb
│   │   ├── update_service.rb
│   │   └── delete_service.rb
│   ├── orders/
│   │   ├── create_service.rb
│   │   └── process_service.rb
│   └── payments/
│       └── charge_service.rb
├── forms/
│   ├── registration_form.rb
│   └── checkout_form.rb
└── queries/
    └── users/
        └── search_query.rb
```

---

## Report Format

### Refactoring Plan: `refactoring-[YYYY-MM-DD].md`

```markdown
# Service Object Refactoring Plan

## Current State
- **Controllers**: [Fat/Clean]
- **Models**: [Fat/Clean]
- **Business Logic Location**: [Scattered/Organized]

## Extractions Needed

| Location | Logic | Service Name |
|----------|-------|--------------|

## Priority Order
1. [Highest complexity]
2. [Most reused]
3. [Hardest to test]

## Implementation Plan
1. Create Result class
2. Extract [Service 1]
3. Extract [Service 2]
4. Add specs

## Testing Strategy
- Unit test each service
- Integration test controller
- Keep existing behavior
```

---

## Severity Guide

| Level | Icon | Examples |
|-------|------|----------|
| **Critical** | 🔴 | Untestable logic, God objects |
| **High** | 🟠 | Fat controllers, complex model methods |
| **Medium** | 🟡 | Duplicated logic, missing services |
| **Low** | 🟢 | Minor extractions, optional cleanup |
