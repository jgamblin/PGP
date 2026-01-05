# Observability & Logging — Structured Logging, Tracing, and Monitoring

> **Purpose**: Production-ready observability patterns and review  
> **Best For**: Copilot, ChatGPT, Claude, Agents  
> **Scope**: Structured logging, OpenTelemetry, metrics, distributed tracing, alerting  
> **Last Updated**: 2026-01

---

## Mission

Help design and implement **observability systems** that provide visibility into application behavior, enable debugging, and support incident response. Focus on structured logging, distributed tracing, metrics, and alerting patterns.

---

## Guard Clauses

**If no observability context provided:**
```
NO_OBSERVABILITY_CONTEXT

Please provide context:
- Application type (web, API, worker, etc.)
- Current logging approach
- Infrastructure (cloud, Kubernetes, etc.)
- Observability tools in use
- Pain points to address

Include log examples if reviewing current setup.
```

**If observability setup is solid:**
```
OBSERVABILITY_APPROVED

✅ Observability review complete — production ready.

Checks performed:
- Structured logging: ✓
- Correlation IDs: ✓
- Key metrics: ✓
- Distributed tracing: ✓
- Alert coverage: ✓

Setup follows observability best practices.
```

---

## Quick Context Checklist

```
☐ Application language/framework
☐ Deployment environment
☐ Current logging stack
☐ Tracing requirements
☐ Metrics storage (Prometheus, etc.)
☐ Log aggregation (ELK, Loki, etc.)
☐ Alerting system
☐ Compliance requirements (PII, etc.)
```

---

## Copy-Paste Prompts

### Prompt: Design Logging Strategy
```text
Design a logging strategy for:

Application: {{APPLICATION}}
Language/Framework: {{FRAMEWORK}}
Scale: {{REQUEST_VOLUME}}

Requirements:
- Debug capability: {{REQUIREMENTS}}
- Compliance: {{COMPLIANCE}}
- Retention: {{RETENTION}}

Provide:
1. Log levels and when to use each
2. Structured log format
3. Correlation ID propagation
4. Sensitive data handling
5. Example log statements
```

### Prompt: Review Logging Implementation
```text
Review this logging implementation:

{{CODE_OR_LOG_EXAMPLES}}

Check for:
1. **Structure**
   - JSON format
   - Consistent fields
   - Correlation IDs

2. **Content**
   - Appropriate log levels
   - Useful context
   - No sensitive data

3. **Performance**
   - Async logging
   - Appropriate verbosity
   - Sampling if needed
```

### Prompt: Design Distributed Tracing
```text
Design distributed tracing for:

Architecture: {{ARCHITECTURE}}
Services: {{SERVICE_LIST}}
Communication: {{SYNC_ASYNC}}

Requirements:
- Trace sampling rate: {{SAMPLING}}
- Span granularity: {{GRANULARITY}}
- Backend: {{JAEGER_ZIPKIN_ETC}}

Provide:
1. Instrumentation approach
2. Context propagation
3. Custom span attributes
4. Sampling strategy
5. Example traces
```

### Prompt: Design Metrics and Alerting
```text
Design metrics and alerting for:

Application: {{APPLICATION}}
SLOs: {{SLOS}}
Current pain points: {{ISSUES}}

Provide:
1. Key metrics (RED, USE)
2. Prometheus metric definitions
3. Grafana dashboard structure
4. Alert rules with thresholds
5. Runbook references
```

---

## Structured Logging

### Log Format Standard

```json
// Structured log entry
{
  // Required fields
  "timestamp": "2026-01-15T10:30:45.123Z",
  "level": "info",
  "message": "User login successful",
  
  // Correlation
  "trace_id": "abc123def456",
  "span_id": "789xyz",
  "request_id": "req-001",
  
  // Context
  "service": "auth-service",
  "environment": "production",
  "version": "1.2.3",
  "host": "auth-pod-xyz",
  
  // Event-specific
  "user_id": "user-123",
  "event": "user.login",
  "duration_ms": 45,
  
  // Error context (when applicable)
  "error": {
    "type": "AuthenticationError",
    "message": "Invalid credentials",
    "stack": "..."
  }
}
```

### Log Levels

| Level | When to Use | Example |
|-------|-------------|---------|
| **ERROR** | Failures requiring attention | Database connection failed, Payment failed |
| **WARN** | Potential issues, degraded state | Rate limit approaching, Retry attempted |
| **INFO** | Significant business events | User registered, Order completed |
| **DEBUG** | Detailed diagnostic info | Query executed, Cache hit/miss |
| **TRACE** | Very detailed, high volume | Function entry/exit, Variable values |

### Language Examples

#### Python

```python
import structlog
import logging
from contextvars import ContextVar

# Context for correlation IDs
request_id_var: ContextVar[str] = ContextVar('request_id', default='')
trace_id_var: ContextVar[str] = ContextVar('trace_id', default='')

def add_context(logger, method_name, event_dict):
    """Add correlation IDs to all log entries"""
    event_dict['request_id'] = request_id_var.get()
    event_dict['trace_id'] = trace_id_var.get()
    return event_dict

# Configure structlog
structlog.configure(
    processors=[
        structlog.stdlib.filter_by_level,
        structlog.stdlib.add_logger_name,
        structlog.stdlib.add_log_level,
        structlog.stdlib.PositionalArgumentsFormatter(),
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.processors.StackInfoRenderer(),
        structlog.processors.format_exc_info,
        add_context,
        structlog.processors.UnicodeDecoder(),
        structlog.processors.JSONRenderer()
    ],
    wrapper_class=structlog.stdlib.BoundLogger,
    context_class=dict,
    logger_factory=structlog.stdlib.LoggerFactory(),
    cache_logger_on_first_use=True,
)

logger = structlog.get_logger()

# Usage
def process_order(order_id: str, user_id: str):
    log = logger.bind(order_id=order_id, user_id=user_id)
    
    log.info("processing_order_started")
    
    try:
        result = payment_service.charge(order_id)
        log.info(
            "payment_processed",
            amount=result.amount,
            payment_id=result.id,
            duration_ms=result.duration
        )
    except PaymentError as e:
        log.error(
            "payment_failed",
            error_type=type(e).__name__,
            error_message=str(e),
            exc_info=True
        )
        raise
```

#### Node.js/TypeScript

```typescript
import pino from 'pino';
import { AsyncLocalStorage } from 'async_hooks';

// Context storage for correlation IDs
const asyncLocalStorage = new AsyncLocalStorage<{
  requestId: string;
  traceId: string;
}>();

const logger = pino({
  level: process.env.LOG_LEVEL || 'info',
  formatters: {
    level: (label) => ({ level: label }),
  },
  timestamp: () => `,"timestamp":"${new Date().toISOString()}"`,
  mixin() {
    const store = asyncLocalStorage.getStore();
    return {
      service: 'order-service',
      environment: process.env.NODE_ENV,
      version: process.env.APP_VERSION,
      requestId: store?.requestId,
      traceId: store?.traceId,
    };
  },
});

// Express middleware
function requestLogger(req, res, next) {
  const requestId = req.headers['x-request-id'] || uuidv4();
  const traceId = req.headers['x-trace-id'] || uuidv4();
  
  asyncLocalStorage.run({ requestId, traceId }, () => {
    const start = Date.now();
    
    res.on('finish', () => {
      logger.info({
        event: 'http_request',
        method: req.method,
        path: req.path,
        statusCode: res.statusCode,
        durationMs: Date.now() - start,
        userAgent: req.headers['user-agent'],
      });
    });
    
    next();
  });
}

// Usage
async function processOrder(orderId: string, userId: string) {
  const log = logger.child({ orderId, userId });
  
  log.info({ event: 'order.processing.started' });
  
  try {
    const result = await paymentService.charge(orderId);
    log.info({
      event: 'payment.processed',
      amount: result.amount,
      paymentId: result.id,
      durationMs: result.duration,
    });
  } catch (error) {
    log.error({
      event: 'payment.failed',
      error: {
        type: error.constructor.name,
        message: error.message,
        stack: error.stack,
      },
    });
    throw error;
  }
}
```

#### Go

```go
package main

import (
    "context"
    "go.uber.org/zap"
    "go.uber.org/zap/zapcore"
)

type contextKey string

const (
    requestIDKey contextKey = "request_id"
    traceIDKey   contextKey = "trace_id"
)

func NewLogger() *zap.Logger {
    config := zap.NewProductionConfig()
    config.EncoderConfig.TimeKey = "timestamp"
    config.EncoderConfig.EncodeTime = zapcore.ISO8601TimeEncoder
    
    logger, _ := config.Build(
        zap.Fields(
            zap.String("service", "order-service"),
            zap.String("environment", os.Getenv("ENV")),
            zap.String("version", os.Getenv("VERSION")),
        ),
    )
    return logger
}

func LoggerFromContext(ctx context.Context, logger *zap.Logger) *zap.Logger {
    requestID, _ := ctx.Value(requestIDKey).(string)
    traceID, _ := ctx.Value(traceIDKey).(string)
    
    return logger.With(
        zap.String("request_id", requestID),
        zap.String("trace_id", traceID),
    )
}

// Usage
func ProcessOrder(ctx context.Context, orderID, userID string) error {
    log := LoggerFromContext(ctx, logger).With(
        zap.String("order_id", orderID),
        zap.String("user_id", userID),
    )
    
    log.Info("processing order started",
        zap.String("event", "order.processing.started"),
    )
    
    result, err := paymentService.Charge(ctx, orderID)
    if err != nil {
        log.Error("payment failed",
            zap.String("event", "payment.failed"),
            zap.Error(err),
        )
        return err
    }
    
    log.Info("payment processed",
        zap.String("event", "payment.processed"),
        zap.Float64("amount", result.Amount),
        zap.String("payment_id", result.ID),
        zap.Int64("duration_ms", result.DurationMs),
    )
    
    return nil
}
```

---

## Correlation IDs

### Propagation Pattern

```
┌─────────────────────────────────────────────────────────────────┐
│                        Request Flow                              │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Client                                                          │
│    │                                                             │
│    │ X-Request-ID: req-001                                       │
│    │ X-Trace-ID: trace-abc                                       │
│    ▼                                                             │
│  ┌─────────────┐                                                 │
│  │ API Gateway │ ─── logs with trace-abc ───                     │
│  └─────────────┘                                                 │
│    │                                                             │
│    │ X-Request-ID: req-001                                       │
│    │ X-Trace-ID: trace-abc                                       │
│    ▼                                                             │
│  ┌─────────────┐                                                 │
│  │ Auth Service│ ─── logs with trace-abc ───                     │
│  └─────────────┘                                                 │
│    │                                                             │
│    │ X-Request-ID: req-001                                       │
│    │ X-Trace-ID: trace-abc                                       │
│    ▼                                                             │
│  ┌─────────────┐      ┌─────────────┐                           │
│  │Order Service│ ───► │Payment Svc  │ ─── logs with trace-abc   │
│  └─────────────┘      └─────────────┘                           │
│         │                                                        │
│         │ Message Queue (trace-abc in headers)                   │
│         ▼                                                        │
│  ┌─────────────┐                                                 │
│  │ Email Svc   │ ─── logs with trace-abc ───                     │
│  └─────────────┘                                                 │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### HTTP Header Propagation

```python
# Outgoing HTTP requests
import httpx

class TracedHTTPClient:
    def __init__(self, base_url: str):
        self.client = httpx.AsyncClient(base_url=base_url)
    
    async def request(self, method: str, path: str, **kwargs):
        headers = kwargs.pop('headers', {})
        
        # Propagate correlation IDs
        headers['X-Request-ID'] = request_id_var.get()
        headers['X-Trace-ID'] = trace_id_var.get()
        
        # OpenTelemetry compatible
        headers['traceparent'] = f"00-{trace_id_var.get()}-{span_id_var.get()}-01"
        
        return await self.client.request(method, path, headers=headers, **kwargs)
```

### Message Queue Propagation

```python
# Publishing with correlation
async def publish_event(event: dict, routing_key: str):
    headers = {
        'x-request-id': request_id_var.get(),
        'x-trace-id': trace_id_var.get(),
        'x-correlation-id': correlation_id_var.get(),
    }
    
    await channel.basic_publish(
        exchange='events',
        routing_key=routing_key,
        body=json.dumps(event),
        properties=pika.BasicProperties(headers=headers)
    )

# Consuming with correlation
async def consume_event(message):
    headers = message.properties.headers or {}
    
    # Restore context
    request_id_var.set(headers.get('x-request-id', str(uuid4())))
    trace_id_var.set(headers.get('x-trace-id', str(uuid4())))
    
    logger.info("processing_message", 
        queue=message.routing_key,
        message_id=message.message_id
    )
```

---

## OpenTelemetry

### Setup

```python
# Python OpenTelemetry setup
from opentelemetry import trace, metrics
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.exporter.otlp.proto.grpc.metric_exporter import OTLPMetricExporter
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry.instrumentation.httpx import HTTPXClientInstrumentor
from opentelemetry.instrumentation.sqlalchemy import SQLAlchemyInstrumentor

def setup_telemetry(service_name: str):
    # Tracing
    trace_provider = TracerProvider(
        resource=Resource.create({
            "service.name": service_name,
            "service.version": os.getenv("VERSION", "unknown"),
            "deployment.environment": os.getenv("ENV", "development"),
        })
    )
    
    trace_provider.add_span_processor(
        BatchSpanProcessor(OTLPSpanExporter())
    )
    trace.set_tracer_provider(trace_provider)
    
    # Metrics
    metric_provider = MeterProvider(
        resource=Resource.create({"service.name": service_name})
    )
    metrics.set_meter_provider(metric_provider)
    
    # Auto-instrumentation
    FastAPIInstrumentor.instrument()
    HTTPXClientInstrumentor().instrument()
    SQLAlchemyInstrumentor().instrument()

# Custom spans
tracer = trace.get_tracer(__name__)

async def process_order(order_id: str):
    with tracer.start_as_current_span("process_order") as span:
        span.set_attribute("order.id", order_id)
        
        with tracer.start_as_current_span("validate_order"):
            validate(order_id)
        
        with tracer.start_as_current_span("charge_payment") as payment_span:
            result = await charge_payment(order_id)
            payment_span.set_attribute("payment.amount", result.amount)
            payment_span.set_attribute("payment.id", result.id)
        
        span.add_event("order_completed", {"status": "success"})
```

### Span Attributes

```python
# Standard semantic conventions
span.set_attribute("http.method", "POST")
span.set_attribute("http.url", "/api/orders")
span.set_attribute("http.status_code", 201)
span.set_attribute("http.user_agent", request.headers.get("user-agent"))

span.set_attribute("db.system", "postgresql")
span.set_attribute("db.statement", "SELECT * FROM users WHERE id = $1")
span.set_attribute("db.operation", "SELECT")

span.set_attribute("messaging.system", "rabbitmq")
span.set_attribute("messaging.destination", "orders.created")
span.set_attribute("messaging.operation", "publish")

# Custom attributes
span.set_attribute("user.id", user_id)
span.set_attribute("order.id", order_id)
span.set_attribute("order.total", order.total)
```

---

## Metrics

### RED Method (Request-oriented)

```python
from prometheus_client import Counter, Histogram, Gauge

# Rate: Requests per second
http_requests_total = Counter(
    'http_requests_total',
    'Total HTTP requests',
    ['method', 'endpoint', 'status']
)

# Errors: Failed requests per second
http_request_errors_total = Counter(
    'http_request_errors_total',
    'Total HTTP request errors',
    ['method', 'endpoint', 'error_type']
)

# Duration: Request latency
http_request_duration_seconds = Histogram(
    'http_request_duration_seconds',
    'HTTP request latency',
    ['method', 'endpoint'],
    buckets=[.005, .01, .025, .05, .1, .25, .5, 1, 2.5, 5, 10]
)

# Middleware
@app.middleware("http")
async def metrics_middleware(request: Request, call_next):
    start = time.time()
    
    try:
        response = await call_next(request)
        
        http_requests_total.labels(
            method=request.method,
            endpoint=request.url.path,
            status=response.status_code
        ).inc()
        
        return response
    except Exception as e:
        http_request_errors_total.labels(
            method=request.method,
            endpoint=request.url.path,
            error_type=type(e).__name__
        ).inc()
        raise
    finally:
        http_request_duration_seconds.labels(
            method=request.method,
            endpoint=request.url.path
        ).observe(time.time() - start)
```

### USE Method (Resource-oriented)

```python
# Utilization: % of resource capacity used
db_connection_pool_utilization = Gauge(
    'db_connection_pool_utilization',
    'Database connection pool utilization',
    ['pool_name']
)

# Saturation: Queue depth / work waiting
task_queue_depth = Gauge(
    'task_queue_depth',
    'Number of tasks waiting in queue',
    ['queue_name']
)

# Errors: Resource errors
db_connection_errors_total = Counter(
    'db_connection_errors_total',
    'Database connection errors',
    ['error_type']
)
```

### Business Metrics

```python
# Business KPIs
orders_total = Counter(
    'orders_total',
    'Total orders placed',
    ['status', 'payment_method']
)

order_value_dollars = Histogram(
    'order_value_dollars',
    'Order value distribution',
    buckets=[10, 25, 50, 100, 250, 500, 1000]
)

active_users = Gauge(
    'active_users',
    'Currently active users'
)

# Usage
orders_total.labels(status='completed', payment_method='credit_card').inc()
order_value_dollars.observe(order.total)
active_users.set(get_active_user_count())
```

### Prometheus Recording Rules

```yaml
# prometheus-rules.yaml
groups:
  - name: http_metrics
    rules:
      # Request rate (per second)
      - record: http_requests:rate5m
        expr: rate(http_requests_total[5m])
      
      # Error rate
      - record: http_errors:rate5m
        expr: rate(http_request_errors_total[5m])
      
      # Error ratio
      - record: http_error_ratio:rate5m
        expr: |
          http_errors:rate5m / http_requests:rate5m
      
      # P99 latency
      - record: http_latency:p99
        expr: |
          histogram_quantile(0.99, 
            rate(http_request_duration_seconds_bucket[5m]))
      
      # Apdex score (threshold: 0.5s)
      - record: http_apdex:rate5m
        expr: |
          (
            sum(rate(http_request_duration_seconds_bucket{le="0.5"}[5m]))
            + sum(rate(http_request_duration_seconds_bucket{le="2.0"}[5m])) / 2
          ) / sum(rate(http_request_duration_seconds_count[5m]))
```

---

## Alerting

### Alert Rules

```yaml
# alerting-rules.yaml
groups:
  - name: service_alerts
    rules:
      # High error rate
      - alert: HighErrorRate
        expr: http_error_ratio:rate5m > 0.01
        for: 5m
        labels:
          severity: critical
        annotations:
          summary: "High error rate on {{ $labels.service }}"
          description: "Error rate is {{ $value | humanizePercentage }} (threshold: 1%)"
          runbook_url: "https://runbooks.example.com/high-error-rate"
      
      # High latency
      - alert: HighLatency
        expr: http_latency:p99 > 1
        for: 5m
        labels:
          severity: warning
        annotations:
          summary: "High latency on {{ $labels.service }}"
          description: "P99 latency is {{ $value | humanizeDuration }}"
          runbook_url: "https://runbooks.example.com/high-latency"
      
      # Low request rate (potential outage)
      - alert: LowRequestRate
        expr: http_requests:rate5m < 10
        for: 5m
        labels:
          severity: warning
        annotations:
          summary: "Abnormally low traffic on {{ $labels.service }}"
          description: "Request rate is {{ $value }}/s"
      
      # Database connection pool exhaustion
      - alert: DBPoolExhaustion
        expr: db_connection_pool_utilization > 0.9
        for: 5m
        labels:
          severity: critical
        annotations:
          summary: "Database connection pool nearly exhausted"
          description: "Pool utilization at {{ $value | humanizePercentage }}"
      
      # SLO burn rate
      - alert: SLOBurnRateHigh
        expr: |
          (
            http_error_ratio:rate1h > (14.4 * 0.001)
            and
            http_error_ratio:rate5m > (14.4 * 0.001)
          )
          or
          (
            http_error_ratio:rate6h > (6 * 0.001)
            and
            http_error_ratio:rate30m > (6 * 0.001)
          )
        for: 2m
        labels:
          severity: critical
        annotations:
          summary: "SLO burn rate too high"
          description: "Burning error budget faster than expected"
```

### Alert Labels and Routing

```yaml
# alertmanager.yaml
route:
  group_by: ['alertname', 'service']
  group_wait: 30s
  group_interval: 5m
  repeat_interval: 4h
  receiver: 'default'
  routes:
    - match:
        severity: critical
      receiver: 'pagerduty-critical'
      continue: true
    
    - match:
        severity: warning
      receiver: 'slack-warnings'
    
    - match:
        team: payments
      receiver: 'payments-team'

receivers:
  - name: 'default'
    slack_configs:
      - channel: '#alerts'
        send_resolved: true
  
  - name: 'pagerduty-critical'
    pagerduty_configs:
      - service_key: '{{ .SecretPagerDutyKey }}'
        severity: critical
  
  - name: 'slack-warnings'
    slack_configs:
      - channel: '#alerts-warnings'
```

---

## Dashboards

### Service Dashboard Template

```
┌─────────────────────────────────────────────────────────────┐
│                    Service: order-service                    │
│  Environment: production    Version: 1.2.3    Pods: 5       │
├─────────────────────────────────────────────────────────────┤
│  SLI Summary (Last 7 days)                                  │
│  ┌─────────────┬─────────────┬─────────────┐                │
│  │ Availability│ Latency P99 │ Error Budget│                │
│  │   99.95%    │   245ms     │   68% left  │                │
│  └─────────────┴─────────────┴─────────────┘                │
├─────────────────────────────────────────────────────────────┤
│  Request Rate                    Error Rate                  │
│  ┌─────────────────────┐        ┌─────────────────────┐     │
│  │ ▄▄▄█████▄▄▄▄█▄▄▄▄▄ │        │ ▁▁▂▁▁▁▁▁▁█▁▁▁▁▁▁▁ │     │
│  │ 1.2k req/s         │        │ 0.02%              │     │
│  └─────────────────────┘        └─────────────────────┘     │
├─────────────────────────────────────────────────────────────┤
│  Latency Distribution            Status Codes               │
│  ┌─────────────────────┐        ┌─────────────────────┐     │
│  │ P50: 45ms           │        │ 2xx: 98.5%         │     │
│  │ P90: 120ms          │        │ 4xx: 1.2%          │     │
│  │ P99: 245ms          │        │ 5xx: 0.3%          │     │
│  └─────────────────────┘        └─────────────────────┘     │
├─────────────────────────────────────────────────────────────┤
│  Top Endpoints by Latency        Recent Errors              │
│  ┌─────────────────────┐        ┌─────────────────────┐     │
│  │ POST /orders: 340ms │        │ 10:45 PaymentError │     │
│  │ GET /users: 85ms    │        │ 10:42 Timeout      │     │
│  │ GET /products: 65ms │        │ 10:38 ValidationErr│     │
│  └─────────────────────┘        └─────────────────────┘     │
└─────────────────────────────────────────────────────────────┘
```

### Grafana Dashboard JSON

```json
{
  "title": "Service Overview",
  "panels": [
    {
      "title": "Request Rate",
      "type": "timeseries",
      "targets": [
        {
          "expr": "sum(rate(http_requests_total{service=\"$service\"}[5m]))",
          "legendFormat": "Requests/s"
        }
      ]
    },
    {
      "title": "Error Rate",
      "type": "timeseries",
      "targets": [
        {
          "expr": "sum(rate(http_request_errors_total{service=\"$service\"}[5m])) / sum(rate(http_requests_total{service=\"$service\"}[5m])) * 100",
          "legendFormat": "Error %"
        }
      ],
      "thresholds": {
        "mode": "absolute",
        "steps": [
          { "value": 0, "color": "green" },
          { "value": 1, "color": "yellow" },
          { "value": 5, "color": "red" }
        ]
      }
    },
    {
      "title": "Latency Percentiles",
      "type": "timeseries",
      "targets": [
        {
          "expr": "histogram_quantile(0.50, rate(http_request_duration_seconds_bucket{service=\"$service\"}[5m]))",
          "legendFormat": "P50"
        },
        {
          "expr": "histogram_quantile(0.90, rate(http_request_duration_seconds_bucket{service=\"$service\"}[5m]))",
          "legendFormat": "P90"
        },
        {
          "expr": "histogram_quantile(0.99, rate(http_request_duration_seconds_bucket{service=\"$service\"}[5m]))",
          "legendFormat": "P99"
        }
      ]
    }
  ],
  "templating": {
    "list": [
      {
        "name": "service",
        "type": "query",
        "query": "label_values(http_requests_total, service)"
      }
    ]
  }
}
```

---

## Sensitive Data Handling

### PII Redaction

```python
import re
from typing import Any

REDACTION_PATTERNS = [
    (r'\b[\w.-]+@[\w.-]+\.\w+\b', '[EMAIL_REDACTED]'),
    (r'\b\d{3}-\d{2}-\d{4}\b', '[SSN_REDACTED]'),
    (r'\b\d{16}\b', '[CARD_REDACTED]'),
    (r'"password"\s*:\s*"[^"]*"', '"password": "[REDACTED]"'),
    (r'"api_key"\s*:\s*"[^"]*"', '"api_key": "[REDACTED]"'),
    (r'Bearer\s+[\w-]+\.[\w-]+\.[\w-]+', 'Bearer [TOKEN_REDACTED]'),
]

def redact_sensitive_data(data: Any) -> Any:
    """Recursively redact sensitive data from log entries"""
    if isinstance(data, str):
        for pattern, replacement in REDACTION_PATTERNS:
            data = re.sub(pattern, replacement, data)
        return data
    
    if isinstance(data, dict):
        return {k: redact_sensitive_data(v) for k, v in data.items()}
    
    if isinstance(data, list):
        return [redact_sensitive_data(item) for item in data]
    
    return data

# Add as structlog processor
def redact_processor(logger, method_name, event_dict):
    return redact_sensitive_data(event_dict)
```

### Field-Level Encryption

```python
from cryptography.fernet import Fernet

class SecureLogger:
    def __init__(self, key: bytes):
        self.fernet = Fernet(key)
        self.sensitive_fields = {'email', 'phone', 'address'}
    
    def log(self, level: str, message: str, **kwargs):
        encrypted_kwargs = {}
        for key, value in kwargs.items():
            if key in self.sensitive_fields:
                encrypted_kwargs[f"{key}_encrypted"] = self.fernet.encrypt(
                    str(value).encode()
                ).decode()
            else:
                encrypted_kwargs[key] = value
        
        logger.log(level, message, **encrypted_kwargs)
```

---

## Severity Guide

| Severity | Issue | Impact |
|----------|-------|--------|
| 🔴 Critical | No error logging | Blind to failures |
| 🔴 Critical | PII in logs | Compliance violation |
| 🔴 Critical | No correlation IDs | Can't trace requests |
| 🟠 High | Missing key metrics | Can't measure SLOs |
| 🟠 High | No alerts configured | Delayed incident response |
| 🟡 Medium | Unstructured logs | Difficult to query |
| 🟡 Medium | Missing context | Hard to debug |
| 🟢 Low | No log sampling | High costs at scale |

---

## Report Template

```markdown
## Observability Review

### Current State
- Logging: [structured/unstructured]
- Tracing: [yes/no, tool]
- Metrics: [yes/no, tool]
- Alerting: [yes/no, tool]

### Logging Assessment
| Aspect | Status | Notes |
|--------|--------|-------|
| Structured format | | |
| Log levels | | |
| Correlation IDs | | |
| Context richness | | |
| PII handling | | |

### Metrics Coverage
| Metric Type | Covered | Missing |
|-------------|---------|---------|
| Request rate | | |
| Error rate | | |
| Latency | | |
| Saturation | | |
| Business metrics | | |

### Alerting Coverage
| SLI | Alert | Threshold | Status |
|-----|-------|-----------|--------|
| | | | |

### Recommendations
1. [Priority] Recommendation
   - Current gap:
   - Implementation:
   - Expected benefit:
```

---

## Related Prompts

- [api-design.md](api-design.md) — API patterns
- [security-analysis.md](security-analysis.md) — Security logging
- [monitoring-observability.md](../infrastructure/monitoring-observability.md) — Infrastructure monitoring

---

*Last updated: 2026-01*
