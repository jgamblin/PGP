# Background Jobs — Sidekiq, Solid Queue & Active Job

> **Purpose**: Production-ready background job patterns and best practices  
> **Best For**: Copilot, ChatGPT, Claude, Agents  
> **Scope**: Sidekiq, Solid Queue, Active Job, queues, retries, scheduling  
> **Last Updated**: 2026-01

---

## Mission

Help build **reliable, scalable background processing** for Rails applications. Focus on job design, error handling, queue management, and production operations.

---

## Guard Clauses

**If no job context provided:**
```
NO_JOB_CONTEXT

Please provide context:
- Task to run in background
- Current implementation (if refactoring)
- Volume/frequency expectations
- Error handling requirements
- Or describe the async operation needed

Include queue backend (Sidekiq, Solid Queue, etc.)
```

**If job implementation is solid:**
```
JOB_APPROVED

✅ Background job review complete — production ready.

Checks performed:
- Design: ✓ (idempotent, small batches)
- Error handling: ✓ (retries, dead letter)
- Performance: ✓ (efficient queries, memory)
- Monitoring: ✓ (logging, metrics)

Job follows background processing best practices.
```

---

## Quick Context Checklist

```
☐ Queue backend (Sidekiq, Solid Queue)
☐ Job purpose and trigger
☐ Expected volume/frequency
☐ Data dependencies
☐ Error handling needs
☐ Retry requirements
☐ Timeout constraints
☐ Monitoring setup
```

---

## Copy-Paste Prompts

### Prompt: Create Background Job
```text
Create a background job for:

Task: {{TASK_DESCRIPTION}}
Trigger: {{TRIGGER}}
Queue backend: {{SIDEKIQ_OR_SOLID_QUEUE}}

Requirements:
- Arguments: {{ARGUMENTS}}
- Retry policy: {{RETRIES}}
- Queue priority: {{PRIORITY}}
- Timeout: {{TIMEOUT}}

Provide:
1. Job class
2. Enqueue examples
3. Error handling
4. Tests
```

### Prompt: Review Background Job
```text
Review this background job:

{{JOB_CODE}}

Check for:
1. **Idempotency**
   - Safe to run multiple times
   - Handles duplicate executions

2. **Arguments**
   - Serializable
   - Minimal data (IDs vs objects)

3. **Error Handling**
   - Retry configuration
   - Dead letter queue
   - Error reporting

4. **Performance**
   - Batch processing
   - Memory efficiency
   - Query optimization

5. **Operations**
   - Logging
   - Monitoring hooks
   - Timeout handling
```

### Prompt: Convert to Background Job
```text
Convert this synchronous code to a background job:

{{CODE}}

Context: {{WHY_ASYNC}}
Queue backend: {{BACKEND}}

Requirements:
- Maintain functionality
- Handle partial failures
- Add proper error handling
- Ensure idempotency
```

### Prompt: Design Job Pipeline
```text
Design a job pipeline for:

Workflow: {{WORKFLOW_DESCRIPTION}}
Steps:
1. {{STEP_1}}
2. {{STEP_2}}
3. {{STEP_3}}

Requirements:
- Sequential vs parallel execution
- Error handling between steps
- Progress tracking
- Rollback strategy
```

---

## Active Job Basics

### Simple Job

```ruby
# app/jobs/send_welcome_email_job.rb
class SendWelcomeEmailJob < ApplicationJob
  queue_as :default
  
  # Retry configuration
  retry_on ActiveRecord::RecordNotFound, wait: 5.seconds, attempts: 3
  discard_on ActiveJob::DeserializationError
  
  def perform(user_id)
    user = User.find(user_id)
    UserMailer.welcome(user).deliver_now
  end
end

# Enqueue
SendWelcomeEmailJob.perform_later(user.id)

# Enqueue with delay
SendWelcomeEmailJob.set(wait: 1.hour).perform_later(user.id)

# Enqueue at specific time
SendWelcomeEmailJob.set(wait_until: Date.tomorrow.noon).perform_later(user.id)
```

### Job with Options

```ruby
class ProcessOrderJob < ApplicationJob
  queue_as :critical
  
  # Custom queue based on arguments
  queue_as do
    if arguments.first.priority == "high"
      :critical
    else
      :default
    end
  end
  
  # Retry configuration
  retry_on StandardError, wait: :polynomially_longer, attempts: 5
  retry_on Timeout::Error, wait: 1.minute, attempts: 10
  discard_on OrderAlreadyProcessedError
  
  # Callbacks
  before_perform :validate_order
  after_perform :notify_completion
  around_perform :track_timing
  
  def perform(order_id, options = {})
    @order = Order.find(order_id)
    @options = options
    
    OrderProcessor.new(@order).process
  end
  
  private
  
  def validate_order
    raise OrderAlreadyProcessedError if @order&.processed?
  end
  
  def notify_completion
    OrderNotifier.completed(@order).deliver_later
  end
  
  def track_timing
    start_time = Time.current
    yield
    duration = Time.current - start_time
    
    Rails.logger.info("ProcessOrderJob completed in #{duration}s")
    StatsD.timing("jobs.process_order.duration", duration)
  end
end
```

### Idempotent Job Pattern

```ruby
class ImportDataJob < ApplicationJob
  queue_as :imports
  
  def perform(import_id)
    import = Import.find(import_id)
    
    # Idempotency check
    return if import.completed?
    
    # Use database lock to prevent concurrent execution
    import.with_lock do
      return if import.completed?
      
      import.update!(status: :processing)
      
      begin
        process_import(import)
        import.update!(status: :completed, completed_at: Time.current)
      rescue => e
        import.update!(status: :failed, error_message: e.message)
        raise
      end
    end
  end
  
  private
  
  def process_import(import)
    import.rows.find_each do |row|
      # Skip already processed rows (idempotent)
      next if row.processed?
      
      process_row(row)
      row.update!(processed: true)
    end
  end
end
```

---

## Sidekiq

### Sidekiq Worker

```ruby
# app/sidekiq/hard_worker.rb (or app/workers/)
class HardWorker
  include Sidekiq::Worker
  
  # Sidekiq-specific options
  sidekiq_options queue: :critical,
                  retry: 5,
                  backtrace: true,
                  lock: :until_executed  # sidekiq-unique-jobs
  
  # Custom retry delays
  sidekiq_retry_in do |count, exception|
    case exception
    when RateLimitError
      60 * (count + 1)  # Linear backoff
    else
      (count ** 4) + 15  # Exponential backoff
    end
  end
  
  def perform(user_id, action)
    user = User.find(user_id)
    
    case action
    when "sync"
      UserSyncService.new(user).call
    when "cleanup"
      UserCleanupService.new(user).call
    end
  end
end

# Enqueue
HardWorker.perform_async(user.id, "sync")
HardWorker.perform_in(1.hour, user.id, "cleanup")
HardWorker.perform_at(Time.current + 1.day, user.id, "sync")
```

### Sidekiq Batches (Pro)

```ruby
class BatchImportJob
  include Sidekiq::Worker
  
  def perform(file_id)
    file = ImportFile.find(file_id)
    
    batch = Sidekiq::Batch.new
    batch.description = "Import #{file.name}"
    batch.on(:success, ImportCallbacks, file_id: file_id)
    batch.on(:death, ImportCallbacks, file_id: file_id)
    
    batch.jobs do
      file.chunks.each do |chunk|
        ProcessChunkJob.perform_async(chunk.id)
      end
    end
  end
end

class ImportCallbacks
  def on_success(status, options)
    file = ImportFile.find(options["file_id"])
    file.update!(status: :completed)
    ImportMailer.success(file).deliver_later
  end
  
  def on_death(status, options)
    file = ImportFile.find(options["file_id"])
    file.update!(status: :failed)
    ImportMailer.failure(file).deliver_later
  end
end
```

### Sidekiq Configuration

```ruby
# config/initializers/sidekiq.rb
Sidekiq.configure_server do |config|
  config.redis = { url: ENV["REDIS_URL"], network_timeout: 5 }
  
  # Server middleware
  config.server_middleware do |chain|
    chain.add Sidekiq::Middleware::Server::RetryJobs
  end
  
  # Death handler
  config.death_handlers << ->(job, ex) do
    ErrorReporter.report(ex, job: job)
  end
end

Sidekiq.configure_client do |config|
  config.redis = { url: ENV["REDIS_URL"], network_timeout: 5 }
end

# config/sidekiq.yml
:concurrency: 10
:timeout: 25

:queues:
  - [critical, 4]
  - [default, 2]
  - [low, 1]

# Schedule (requires sidekiq-cron or sidekiq-scheduler)
:schedule:
  cleanup_job:
    cron: "0 3 * * *"
    class: CleanupJob
    queue: low
```

---

## Solid Queue (Rails 8+)

### Basic Setup

```ruby
# config/application.rb
config.active_job.queue_adapter = :solid_queue

# db/migrate/create_solid_queue_tables.rb
# Run: rails solid_queue:install:migrations
```

### Solid Queue Job

```ruby
class ProcessPaymentJob < ApplicationJob
  queue_as :payments
  limits_concurrency to: 1, key: ->(order_id) { "order-#{order_id}" }
  
  # Solid Queue specific
  retry_on StandardError, wait: :polynomially_longer, attempts: 5
  
  def perform(order_id)
    order = Order.find(order_id)
    PaymentProcessor.process(order)
  end
end
```

### Solid Queue Configuration

```yaml
# config/solid_queue.yml
default: &default
  dispatchers:
    - polling_interval: 1
      batch_size: 500
  workers:
    - queues: "*"
      threads: 5
      polling_interval: 0.1

development:
  <<: *default

production:
  dispatchers:
    - polling_interval: 1
      batch_size: 500
  workers:
    - queues: [critical]
      threads: 5
      polling_interval: 0.1
    - queues: [default, low]
      threads: 3
      polling_interval: 0.5
```

### Solid Queue Recurring Jobs

```yaml
# config/recurring.yml
production:
  daily_cleanup:
    class: CleanupJob
    schedule: every day at 3am
    
  hourly_sync:
    class: SyncJob
    schedule: every hour
    
  weekly_report:
    class: WeeklyReportJob
    schedule: every monday at 9am
    args:
      - report_type: summary
```

---

## Job Patterns

### Bulk Operations

```ruby
class BulkEmailJob < ApplicationJob
  queue_as :bulk
  
  BATCH_SIZE = 100
  
  def perform(campaign_id, offset = 0)
    campaign = Campaign.find(campaign_id)
    subscribers = campaign.subscribers.offset(offset).limit(BATCH_SIZE)
    
    return if subscribers.empty?
    
    # Process batch
    subscribers.each do |subscriber|
      CampaignMailer.send_campaign(campaign, subscriber).deliver_now
    end
    
    # Enqueue next batch
    if subscribers.size == BATCH_SIZE
      self.class.perform_later(campaign_id, offset + BATCH_SIZE)
    else
      campaign.update!(status: :completed)
    end
  end
end

# Or use find_each for memory efficiency
class ProcessAllUsersJob < ApplicationJob
  def perform
    User.active.find_each(batch_size: 500) do |user|
      ProcessUserJob.perform_later(user.id)
    end
  end
end
```

### Job with Progress Tracking

```ruby
class LongRunningJob < ApplicationJob
  queue_as :long_running
  
  def perform(task_id)
    task = Task.find(task_id)
    items = task.items
    total = items.count
    
    task.update!(status: :processing, progress: 0)
    
    items.each_with_index do |item, index|
      process_item(item)
      
      # Update progress every 10 items
      if (index + 1) % 10 == 0
        progress = ((index + 1).to_f / total * 100).round
        task.update!(progress: progress)
        
        # Broadcast progress via Turbo Streams
        task.broadcast_replace_to(
          task.user,
          target: "task_#{task.id}_progress",
          partial: "tasks/progress",
          locals: { task: task }
        )
      end
    end
    
    task.update!(status: :completed, progress: 100)
  end
end
```

### Job Chains / Workflows

```ruby
# Sequential job chain
class OrderWorkflow
  def self.start(order_id)
    ValidateOrderJob
      .set(wait: 0)
      .perform_later(order_id)
  end
end

class ValidateOrderJob < ApplicationJob
  def perform(order_id)
    order = Order.find(order_id)
    
    if OrderValidator.valid?(order)
      ProcessPaymentJob.perform_later(order_id)
    else
      order.update!(status: :invalid)
    end
  end
end

class ProcessPaymentJob < ApplicationJob
  def perform(order_id)
    order = Order.find(order_id)
    
    if PaymentProcessor.charge(order)
      FulfillOrderJob.perform_later(order_id)
    else
      order.update!(status: :payment_failed)
    end
  end
end

class FulfillOrderJob < ApplicationJob
  def perform(order_id)
    order = Order.find(order_id)
    FulfillmentService.fulfill(order)
    SendConfirmationJob.perform_later(order_id)
  end
end
```

### Throttled Job

```ruby
class RateLimitedApiJob < ApplicationJob
  queue_as :api_calls
  
  # Limit to 10 per minute
  RATE_LIMIT = 10
  RATE_PERIOD = 60.seconds
  
  retry_on RateLimitError, wait: RATE_PERIOD, attempts: 5
  
  def perform(resource_id)
    if rate_limited?
      raise RateLimitError, "Rate limit exceeded"
    end
    
    increment_counter
    ApiClient.fetch(resource_id)
  end
  
  private
  
  def rate_limited?
    current_count >= RATE_LIMIT
  end
  
  def current_count
    Rails.cache.read(rate_limit_key) || 0
  end
  
  def increment_counter
    Rails.cache.increment(rate_limit_key, 1, expires_in: RATE_PERIOD)
  end
  
  def rate_limit_key
    "rate_limit:#{self.class.name}:#{Time.current.beginning_of_minute.to_i}"
  end
end
```

### Timeout Handling

```ruby
class TimeoutSafeJob < ApplicationJob
  queue_as :default
  
  # Global timeout
  TIMEOUT = 5.minutes
  
  def perform(task_id)
    Timeout.timeout(TIMEOUT) do
      process_task(task_id)
    end
  rescue Timeout::Error
    handle_timeout(task_id)
    raise  # Re-raise for retry handling
  end
  
  private
  
  def process_task(task_id)
    task = Task.find(task_id)
    # Long running operation
  end
  
  def handle_timeout(task_id)
    Rails.logger.error("TimeoutSafeJob timed out for task #{task_id}")
    Task.find(task_id).update!(status: :timeout)
  end
end
```

---

## Error Handling

### Comprehensive Error Handling

```ruby
class RobustJob < ApplicationJob
  queue_as :default
  
  # Specific error handling
  retry_on ActiveRecord::Deadlocked, wait: 5.seconds, attempts: 3
  retry_on Net::OpenTimeout, wait: :polynomially_longer, attempts: 5
  retry_on Faraday::TimeoutError, wait: 10.seconds, attempts: 3
  
  # Discard unrecoverable errors
  discard_on ActiveRecord::RecordNotFound
  discard_on ArgumentError
  
  # Custom error handling
  rescue_from CustomError do |exception|
    handle_custom_error(exception)
  end
  
  around_perform do |job, block|
    block.call
  rescue StandardError => e
    # Log and report before retry
    Rails.logger.error("Job failed: #{e.message}")
    ErrorReporter.report(e, job_class: self.class.name, arguments: arguments)
    raise
  end
  
  def perform(record_id)
    # Job logic
  end
  
  private
  
  def handle_custom_error(exception)
    Rails.logger.warn("CustomError handled: #{exception.message}")
    # Don't re-raise, job completes successfully
  end
end
```

### Dead Letter Queue

```ruby
# config/initializers/sidekiq.rb
Sidekiq.configure_server do |config|
  config.death_handlers << ->(job, exception) do
    # Store failed job for analysis
    DeadJob.create!(
      job_class: job["class"],
      args: job["args"],
      error_class: exception.class.name,
      error_message: exception.message,
      backtrace: exception.backtrace&.first(10),
      failed_at: Time.current
    )
    
    # Alert on critical jobs
    if job["queue"] == "critical"
      SlackNotifier.alert("Critical job failed: #{job['class']}")
    end
  end
end
```

---

## Testing

### Testing Active Jobs

```ruby
# test/jobs/send_welcome_email_job_test.rb
require "test_helper"

class SendWelcomeEmailJobTest < ActiveJob::TestCase
  test "sends welcome email" do
    user = users(:one)
    
    assert_emails 1 do
      SendWelcomeEmailJob.perform_now(user.id)
    end
  end
  
  test "enqueues job" do
    user = users(:one)
    
    assert_enqueued_with(job: SendWelcomeEmailJob, args: [user.id]) do
      SendWelcomeEmailJob.perform_later(user.id)
    end
  end
  
  test "retries on record not found" do
    assert_raises ActiveRecord::RecordNotFound do
      SendWelcomeEmailJob.perform_now(999999)
    end
  end
  
  test "enqueues in correct queue" do
    assert_enqueued_jobs 1, only: SendWelcomeEmailJob, queue: :mailers do
      SendWelcomeEmailJob.perform_later(1)
    end
  end
end
```

### RSpec Testing

```ruby
# spec/jobs/process_order_job_spec.rb
require "rails_helper"

RSpec.describe ProcessOrderJob, type: :job do
  describe "#perform" do
    let(:order) { create(:order) }
    
    it "processes the order" do
      expect(OrderProcessor).to receive(:new).with(order).and_call_original
      
      described_class.perform_now(order.id)
      
      expect(order.reload).to be_processed
    end
    
    context "when order not found" do
      it "raises and retries" do
        expect {
          described_class.perform_now(999999)
        }.to raise_error(ActiveRecord::RecordNotFound)
      end
    end
    
    context "when order already processed" do
      let(:order) { create(:order, :processed) }
      
      it "discards the job" do
        expect(OrderProcessor).not_to receive(:new)
        
        described_class.perform_now(order.id)
      end
    end
  end
  
  describe "queue" do
    it "uses critical queue for high priority" do
      order = create(:order, priority: "high")
      
      expect {
        described_class.perform_later(order.id)
      }.to have_enqueued_job.on_queue("critical")
    end
  end
end
```

---

## Monitoring

### Logging Best Practices

```ruby
class MonitoredJob < ApplicationJob
  around_perform do |job, block|
    job_info = {
      class: self.class.name,
      job_id: job_id,
      arguments: arguments,
      queue: queue_name
    }
    
    Rails.logger.info("Job started", job_info)
    start_time = Process.clock_gettime(Process::CLOCK_MONOTONIC)
    
    block.call
    
    duration = Process.clock_gettime(Process::CLOCK_MONOTONIC) - start_time
    Rails.logger.info("Job completed", job_info.merge(duration: duration))
    
  rescue => e
    Rails.logger.error("Job failed", job_info.merge(
      error: e.class.name,
      message: e.message
    ))
    raise
  end
end
```

### Metrics Collection

```ruby
class InstrumentedJob < ApplicationJob
  around_perform do |job, block|
    tags = {
      job_class: self.class.name,
      queue: queue_name
    }
    
    StatsD.increment("jobs.started", tags: tags)
    
    start_time = Time.current
    begin
      block.call
      StatsD.increment("jobs.completed", tags: tags)
    rescue => e
      StatsD.increment("jobs.failed", tags: tags.merge(error: e.class.name))
      raise
    ensure
      duration = Time.current - start_time
      StatsD.timing("jobs.duration", duration * 1000, tags: tags)
    end
  end
end
```

---

## Severity Guide

| Severity | Issue | Impact |
|----------|-------|--------|
| 🔴 Critical | Non-idempotent jobs | Data corruption |
| 🔴 Critical | No retry configuration | Lost jobs |
| 🔴 Critical | Passing AR objects (not IDs) | Serialization failures |
| 🟠 High | No error reporting | Silent failures |
| 🟠 High | Missing timeouts | Queue blockage |
| 🟡 Medium | No progress tracking | Poor visibility |
| 🟡 Medium | Inefficient batching | Memory issues |
| 🟢 Low | Missing logging | Debugging difficulty |

---

## Report Template

```markdown
## Background Job Review

### Job: [name]
- Queue: [queue name]
- Trigger: [how it's enqueued]
- Frequency: [expected volume]

### Assessment
| Criteria | Status | Notes |
|----------|--------|-------|
| Idempotent | | |
| Error handling | | |
| Retry config | | |
| Timeout | | |
| Monitoring | | |
| Testing | | |

### Issues Found
1. [Severity] Issue
   - Impact:
   - Fix:

### Recommendations
1. [Priority] Recommendation
   - Benefit:
```

---

## Related Prompts

- [rails-active-record-performance-audit.md](rails-active-record-performance-audit.md) — Query optimization
- [rspec-test-generation.md](rspec-test-generation.md) — Testing patterns
- [service-object-domain-logic-refactoring.md](service-object-domain-logic-refactoring.md) — Service objects

---

*Last updated: 2026-01*
