# Monitoring & Observability

> **Purpose**: Production-grade monitoring, logging, and observability  
> **Best For**: Codex, Claude, ChatGPT, Copilot, Agents  
> **Scope**: Metrics, logging, tracing, alerting, dashboards  
> **Last Updated**: 2026-03

---

## Mission

Help design and implement **comprehensive observability solutions** for production systems. Focus on metrics, logging, distributed tracing, and actionable alerting using modern tools.

---

## Guard Clauses

**If no observability context provided:**
```
NO_OBSERVABILITY_CONTEXT

Please provide context:
- System type (web app, microservices, data pipeline, etc.)
- Scale (requests/sec, data volume)
- Current monitoring (if any)
- Cloud provider or self-hosted
- Or describe what you want to monitor
```

**If observability is well-configured:**
```
OBSERVABILITY_APPROVED

✅ Observability stack review complete — production ready.

Checks performed:
- Metrics: ✓ (collection, aggregation, retention)
- Logging: ✓ (structured, searchable, retained)
- Tracing: ✓ (distributed, sampled appropriately)
- Alerting: ✓ (actionable, not noisy)

Observability follows SRE best practices.
```

---

## Quick Context Checklist

```
☐ System architecture overview
☐ Current monitoring tools
☐ Key business metrics
☐ SLOs and SLIs defined
☐ Alert notification channels
☐ Retention requirements
☐ Compliance needs
☐ Budget constraints
```

---

## Copy-Paste Prompts

### Prompt: Design Observability Stack
```text
Design an observability stack for:

System: {{SYSTEM_TYPE}}
Scale: {{SCALE}}
Cloud: {{CLOUD_PROVIDER}}
Budget: {{BUDGET}}

Requirements:
- Metrics: {{METRICS_NEEDS}}
- Logging: {{LOGGING_NEEDS}}
- Tracing: {{TRACING_NEEDS}}

Generate:
1. Tool recommendations with justification
2. Architecture diagram
3. Data flow overview
4. Cost estimation
5. Implementation roadmap
```

### Prompt: SLO Definition
```text
Define SLOs for:

Service: {{SERVICE_NAME}}
Type: {{SERVICE_TYPE}}
Users: {{USER_COUNT}}
Current performance: {{BASELINE}}

Generate:
1. Recommended SLIs (latency, availability, error rate)
2. SLO targets with justification
3. Error budget calculation
4. Burn rate alert thresholds
5. Dashboard design
```

### Prompt: Review Monitoring
```text
Review this monitoring configuration:

{{CONFIG}}

Check for:
1. **Metrics**
   - Key metrics covered
   - Cardinality issues
   - Aggregation appropriate
   - Retention sufficient

2. **Logging**
   - Structured format
   - Log levels appropriate
   - PII handling
   - Correlation IDs

3. **Tracing**
   - Context propagation
   - Sampling strategy
   - Span coverage

4. **Alerting**
   - Actionable alerts
   - Runbook links
   - Escalation paths
   - Alert fatigue risk

Rate each: 🟢 Good | 🟡 Needs attention | 🔴 Critical gap
```

### Prompt: Alert Tuning
```text
Review and tune these alerts:

{{ALERTS}}

Historical data:
- False positive rate: {{FP_RATE}}
- Mean time to acknowledge: {{MTTA}}
- Alert frequency: {{FREQUENCY}}

Recommend:
1. Threshold adjustments
2. Alert consolidation
3. Severity reclassification
4. Missing alerts
5. Runbook improvements
```

---

## Prometheus Configuration

### Basic Setup
```yaml
# prometheus.yml
global:
  scrape_interval: 15s
  evaluation_interval: 15s
  external_labels:
    cluster: production
    env: prod

alerting:
  alertmanagers:
    - static_configs:
        - targets:
            - alertmanager:9093

rule_files:
  - /etc/prometheus/rules/*.yml

scrape_configs:
  - job_name: prometheus
    static_configs:
      - targets: ['localhost:9090']

  - job_name: kubernetes-pods
    kubernetes_sd_configs:
      - role: pod
    relabel_configs:
      - source_labels: [__meta_kubernetes_pod_annotation_prometheus_io_scrape]
        action: keep
        regex: true
      - source_labels: [__meta_kubernetes_pod_annotation_prometheus_io_path]
        action: replace
        target_label: __metrics_path__
        regex: (.+)
      - source_labels: [__address__, __meta_kubernetes_pod_annotation_prometheus_io_port]
        action: replace
        regex: ([^:]+)(?::\d+)?;(\d+)
        replacement: $1:$2
        target_label: __address__
```

### Recording Rules
```yaml
# recording-rules.yml
groups:
  - name: slo_rules
    interval: 30s
    rules:
      # Request rate
      - record: job:http_requests:rate5m
        expr: sum(rate(http_requests_total[5m])) by (job)
      
      # Error rate
      - record: job:http_errors:rate5m
        expr: sum(rate(http_requests_total{status=~"5.."}[5m])) by (job)
      
      # Error ratio
      - record: job:http_error_ratio:rate5m
        expr: |
          job:http_errors:rate5m / job:http_requests:rate5m
      
      # Latency percentiles
      - record: job:http_latency:p50
        expr: histogram_quantile(0.5, sum(rate(http_request_duration_seconds_bucket[5m])) by (job, le))
      
      - record: job:http_latency:p95
        expr: histogram_quantile(0.95, sum(rate(http_request_duration_seconds_bucket[5m])) by (job, le))
      
      - record: job:http_latency:p99
        expr: histogram_quantile(0.99, sum(rate(http_request_duration_seconds_bucket[5m])) by (job, le))

  - name: resource_rules
    rules:
      # CPU utilization
      - record: instance:cpu_utilization:ratio
        expr: |
          1 - avg(rate(node_cpu_seconds_total{mode="idle"}[5m])) by (instance)
      
      # Memory utilization
      - record: instance:memory_utilization:ratio
        expr: |
          1 - (node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes)
```

### Alert Rules
```yaml
# alerts.yml
groups:
  - name: slo_alerts
    rules:
      # High error rate
      - alert: HighErrorRate
        expr: job:http_error_ratio:rate5m > 0.01
        for: 5m
        labels:
          severity: warning
        annotations:
          summary: "High error rate on {{ $labels.job }}"
          description: "Error rate is {{ $value | humanizePercentage }}"
          runbook: https://runbooks.example.com/high-error-rate
      
      # Critical error rate
      - alert: CriticalErrorRate
        expr: job:http_error_ratio:rate5m > 0.05
        for: 2m
        labels:
          severity: critical
        annotations:
          summary: "Critical error rate on {{ $labels.job }}"
          description: "Error rate is {{ $value | humanizePercentage }}"
          runbook: https://runbooks.example.com/critical-error-rate

      # High latency
      - alert: HighLatencyP95
        expr: job:http_latency:p95 > 0.5
        for: 5m
        labels:
          severity: warning
        annotations:
          summary: "High p95 latency on {{ $labels.job }}"
          description: "P95 latency is {{ $value | humanizeDuration }}"

      # Error budget burn rate (fast burn)
      - alert: ErrorBudgetFastBurn
        expr: |
          (
            job:http_error_ratio:rate5m > (14.4 * 0.001)
            and
            job:http_error_ratio:rate1h > (14.4 * 0.001)
          )
        for: 2m
        labels:
          severity: critical
          page: true
        annotations:
          summary: "Fast error budget burn on {{ $labels.job }}"
          description: "At current rate, error budget will be exhausted in < 2 hours"

  - name: infrastructure_alerts
    rules:
      - alert: HighCPU
        expr: instance:cpu_utilization:ratio > 0.8
        for: 15m
        labels:
          severity: warning
        annotations:
          summary: "High CPU on {{ $labels.instance }}"
          description: "CPU at {{ $value | humanizePercentage }}"
      
      - alert: HighMemory
        expr: instance:memory_utilization:ratio > 0.9
        for: 5m
        labels:
          severity: warning
        annotations:
          summary: "High memory on {{ $labels.instance }}"
          description: "Memory at {{ $value | humanizePercentage }}"
      
      - alert: DiskSpaceLow
        expr: |
          (node_filesystem_avail_bytes{mountpoint="/"} / node_filesystem_size_bytes{mountpoint="/"}) < 0.1
        for: 5m
        labels:
          severity: critical
        annotations:
          summary: "Low disk space on {{ $labels.instance }}"
          description: "Disk space is {{ $value | humanizePercentage }} available"
```

---

## OpenTelemetry Configuration

### Collector Config
```yaml
# otel-collector.yaml
receivers:
  otlp:
    protocols:
      grpc:
        endpoint: 0.0.0.0:4317
      http:
        endpoint: 0.0.0.0:4318
  
  prometheus:
    config:
      scrape_configs:
        - job_name: otel-collector
          scrape_interval: 10s
          static_configs:
            - targets: ['localhost:8888']

processors:
  batch:
    timeout: 1s
    send_batch_size: 1024
  
  memory_limiter:
    check_interval: 1s
    limit_mib: 2000
    spike_limit_mib: 400
  
  attributes:
    actions:
      - key: environment
        value: production
        action: upsert

  tail_sampling:
    decision_wait: 10s
    num_traces: 100
    expected_new_traces_per_sec: 100
    policies:
      - name: errors
        type: status_code
        status_code: {status_codes: [ERROR]}
      - name: slow-traces
        type: latency
        latency: {threshold_ms: 1000}
      - name: probabilistic
        type: probabilistic
        probabilistic: {sampling_percentage: 10}

exporters:
  otlphttp:
    endpoint: https://otel.example.com
    headers:
      Authorization: Bearer ${OTEL_TOKEN}
  
  prometheus:
    endpoint: 0.0.0.0:8889
    namespace: app
  
  loki:
    endpoint: http://loki:3100/loki/api/v1/push
    labels:
      resource:
        service.name: "service_name"

service:
  pipelines:
    traces:
      receivers: [otlp]
      processors: [memory_limiter, tail_sampling, batch]
      exporters: [otlphttp]
    
    metrics:
      receivers: [otlp, prometheus]
      processors: [memory_limiter, batch]
      exporters: [prometheus, otlphttp]
    
    logs:
      receivers: [otlp]
      processors: [memory_limiter, attributes, batch]
      exporters: [loki]
```

### Python Instrumentation
```python
# observability.py
import logging
from opentelemetry import trace, metrics
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.exporter.otlp.proto.grpc.metric_exporter import OTLPMetricExporter
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry.instrumentation.httpx import HTTPXClientInstrumentor
from opentelemetry.instrumentation.sqlalchemy import SQLAlchemyInstrumentor
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.metrics.export import PeriodicExportingMetricReader
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.semconv.resource import ResourceAttributes


def setup_observability(service_name: str, version: str) -> None:
    """Initialize OpenTelemetry instrumentation."""
    resource = Resource.create({
        ResourceAttributes.SERVICE_NAME: service_name,
        ResourceAttributes.SERVICE_VERSION: version,
        ResourceAttributes.DEPLOYMENT_ENVIRONMENT: "production",
    })
    
    # Tracing
    tracer_provider = TracerProvider(resource=resource)
    tracer_provider.add_span_processor(
        BatchSpanProcessor(OTLPSpanExporter())
    )
    trace.set_tracer_provider(tracer_provider)
    
    # Metrics
    metric_reader = PeriodicExportingMetricReader(
        OTLPMetricExporter(),
        export_interval_millis=60000,
    )
    meter_provider = MeterProvider(
        resource=resource,
        metric_readers=[metric_reader],
    )
    metrics.set_meter_provider(meter_provider)
    
    # Auto-instrumentation
    FastAPIInstrumentor.instrument()
    HTTPXClientInstrumentor.instrument()
    SQLAlchemyInstrumentor().instrument()


# Custom metrics
meter = metrics.get_meter(__name__)

request_counter = meter.create_counter(
    "app.requests",
    description="Number of requests",
    unit="1",
)

request_duration = meter.create_histogram(
    "app.request.duration",
    description="Request duration in seconds",
    unit="s",
)

active_connections = meter.create_up_down_counter(
    "app.connections.active",
    description="Number of active connections",
    unit="1",
)


# Custom spans
tracer = trace.get_tracer(__name__)

async def process_order(order_id: str) -> dict:
    with tracer.start_as_current_span("process_order") as span:
        span.set_attribute("order.id", order_id)
        
        # Nested span
        with tracer.start_as_current_span("validate_order"):
            # validation logic
            pass
        
        with tracer.start_as_current_span("charge_payment"):
            # payment logic
            pass
        
        return {"status": "completed"}
```

### Node.js Instrumentation
```typescript
// observability.ts
import { NodeSDK } from '@opentelemetry/sdk-node';
import { OTLPTraceExporter } from '@opentelemetry/exporter-trace-otlp-grpc';
import { OTLPMetricExporter } from '@opentelemetry/exporter-metrics-otlp-grpc';
import { PeriodicExportingMetricReader } from '@opentelemetry/sdk-metrics';
import { getNodeAutoInstrumentations } from '@opentelemetry/auto-instrumentations-node';
import { Resource } from '@opentelemetry/resources';
import { SemanticResourceAttributes } from '@opentelemetry/semantic-conventions';

const resource = new Resource({
  [SemanticResourceAttributes.SERVICE_NAME]: process.env.SERVICE_NAME,
  [SemanticResourceAttributes.SERVICE_VERSION]: process.env.SERVICE_VERSION,
  [SemanticResourceAttributes.DEPLOYMENT_ENVIRONMENT]: process.env.NODE_ENV,
});

const sdk = new NodeSDK({
  resource,
  traceExporter: new OTLPTraceExporter({
    url: process.env.OTEL_EXPORTER_OTLP_ENDPOINT,
  }),
  metricReader: new PeriodicExportingMetricReader({
    exporter: new OTLPMetricExporter({
      url: process.env.OTEL_EXPORTER_OTLP_ENDPOINT,
    }),
    exportIntervalMillis: 60000,
  }),
  instrumentations: [
    getNodeAutoInstrumentations({
      '@opentelemetry/instrumentation-fs': { enabled: false },
    }),
  ],
});

sdk.start();

process.on('SIGTERM', () => {
  sdk.shutdown()
    .then(() => console.log('SDK shut down'))
    .catch((error) => console.error('Error shutting down SDK', error))
    .finally(() => process.exit(0));
});
```

---

## Structured Logging

### Python with structlog
```python
# logging_config.py
import logging
import structlog
from opentelemetry import trace


def add_trace_context(logger, method_name, event_dict):
    """Add trace context to log entries."""
    span = trace.get_current_span()
    if span.is_recording():
        ctx = span.get_span_context()
        event_dict["trace_id"] = format(ctx.trace_id, "032x")
        event_dict["span_id"] = format(ctx.span_id, "016x")
    return event_dict


def setup_logging(log_level: str = "INFO") -> None:
    """Configure structured logging with JSON output."""
    structlog.configure(
        processors=[
            structlog.contextvars.merge_contextvars,
            structlog.processors.add_log_level,
            structlog.processors.TimeStamper(fmt="iso"),
            add_trace_context,
            structlog.processors.StackInfoRenderer(),
            structlog.processors.format_exc_info,
            structlog.processors.JSONRenderer(),
        ],
        wrapper_class=structlog.make_filtering_bound_logger(
            getattr(logging, log_level)
        ),
        context_class=dict,
        logger_factory=structlog.PrintLoggerFactory(),
        cache_logger_on_first_use=True,
    )


# Usage
logger = structlog.get_logger()

logger.info(
    "order_processed",
    order_id="12345",
    customer_id="67890",
    total=99.99,
    items=3,
)

# With context binding
log = logger.bind(request_id="abc123")
log.info("starting_request")
log.info("processing_data")
log.info("request_complete", duration_ms=150)
```

### Log Aggregation with Loki
```yaml
# promtail.yaml
server:
  http_listen_port: 9080
  grpc_listen_port: 0

positions:
  filename: /tmp/positions.yaml

clients:
  - url: http://loki:3100/loki/api/v1/push

scrape_configs:
  - job_name: kubernetes-pods
    kubernetes_sd_configs:
      - role: pod
    
    pipeline_stages:
      - json:
          expressions:
            level: level
            trace_id: trace_id
            span_id: span_id
            message: event
      
      - labels:
          level:
          trace_id:
      
      - timestamp:
          source: timestamp
          format: RFC3339Nano
    
    relabel_configs:
      - source_labels: [__meta_kubernetes_pod_label_app]
        target_label: app
      - source_labels: [__meta_kubernetes_namespace]
        target_label: namespace
      - source_labels: [__meta_kubernetes_pod_name]
        target_label: pod
```

---

## Grafana Dashboards

### SLO Dashboard (JSON)
```json
{
  "title": "Service SLOs",
  "panels": [
    {
      "title": "Availability SLO",
      "type": "gauge",
      "targets": [
        {
          "expr": "1 - (sum(increase(http_requests_total{status=~\"5..\"}[30d])) / sum(increase(http_requests_total[30d])))",
          "legendFormat": "Availability"
        }
      ],
      "fieldConfig": {
        "defaults": {
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {"color": "red", "value": 0},
              {"color": "yellow", "value": 0.99},
              {"color": "green", "value": 0.999}
            ]
          },
          "unit": "percentunit",
          "min": 0.9,
          "max": 1
        }
      }
    },
    {
      "title": "Error Budget Remaining",
      "type": "stat",
      "targets": [
        {
          "expr": "(1 - 0.999) - (sum(increase(http_requests_total{status=~\"5..\"}[30d])) / sum(increase(http_requests_total[30d])))",
          "legendFormat": "Error Budget"
        }
      ],
      "fieldConfig": {
        "defaults": {
          "unit": "percentunit",
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {"color": "red", "value": 0},
              {"color": "yellow", "value": 0.25},
              {"color": "green", "value": 0.5}
            ]
          }
        }
      }
    },
    {
      "title": "Request Rate",
      "type": "graph",
      "targets": [
        {
          "expr": "sum(rate(http_requests_total[5m]))",
          "legendFormat": "Total RPS"
        },
        {
          "expr": "sum(rate(http_requests_total{status=~\"5..\"}[5m]))",
          "legendFormat": "Error RPS"
        }
      ]
    },
    {
      "title": "Latency Distribution",
      "type": "heatmap",
      "targets": [
        {
          "expr": "sum(rate(http_request_duration_seconds_bucket[5m])) by (le)",
          "legendFormat": "{{le}}"
        }
      ]
    }
  ]
}
```

### Infrastructure Dashboard
```json
{
  "title": "Infrastructure Health",
  "panels": [
    {
      "title": "CPU Usage by Node",
      "type": "timeseries",
      "targets": [
        {
          "expr": "100 * (1 - avg(rate(node_cpu_seconds_total{mode=\"idle\"}[5m])) by (instance))",
          "legendFormat": "{{instance}}"
        }
      ],
      "fieldConfig": {
        "defaults": {
          "unit": "percent",
          "thresholds": {
            "steps": [
              {"color": "green", "value": 0},
              {"color": "yellow", "value": 70},
              {"color": "red", "value": 85}
            ]
          }
        }
      }
    },
    {
      "title": "Memory Usage",
      "type": "timeseries",
      "targets": [
        {
          "expr": "100 * (1 - (node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes))",
          "legendFormat": "{{instance}}"
        }
      ]
    },
    {
      "title": "Disk I/O",
      "type": "timeseries",
      "targets": [
        {
          "expr": "rate(node_disk_read_bytes_total[5m])",
          "legendFormat": "Read - {{device}}"
        },
        {
          "expr": "rate(node_disk_written_bytes_total[5m])",
          "legendFormat": "Write - {{device}}"
        }
      ]
    },
    {
      "title": "Network Traffic",
      "type": "timeseries",
      "targets": [
        {
          "expr": "rate(node_network_receive_bytes_total{device!~\"lo|veth.*\"}[5m])",
          "legendFormat": "RX - {{device}}"
        },
        {
          "expr": "rate(node_network_transmit_bytes_total{device!~\"lo|veth.*\"}[5m])",
          "legendFormat": "TX - {{device}}"
        }
      ]
    }
  ]
}
```

---

## Alertmanager Configuration

```yaml
# alertmanager.yml
global:
  resolve_timeout: 5m
  slack_api_url: ${SLACK_WEBHOOK_URL}

route:
  receiver: default
  group_by: [alertname, cluster, service]
  group_wait: 30s
  group_interval: 5m
  repeat_interval: 4h
  routes:
    - match:
        severity: critical
      receiver: pagerduty
      continue: true
    
    - match:
        severity: critical
      receiver: slack-critical
    
    - match:
        severity: warning
      receiver: slack-warnings

receivers:
  - name: default
    slack_configs:
      - channel: '#alerts'
        title: '{{ .GroupLabels.alertname }}'
        text: '{{ range .Alerts }}{{ .Annotations.description }}{{ end }}'

  - name: slack-critical
    slack_configs:
      - channel: '#alerts-critical'
        title: '🚨 {{ .GroupLabels.alertname }}'
        color: danger
        text: |
          {{ range .Alerts }}
          *Alert:* {{ .Annotations.summary }}
          *Description:* {{ .Annotations.description }}
          *Runbook:* {{ .Annotations.runbook }}
          {{ end }}

  - name: slack-warnings
    slack_configs:
      - channel: '#alerts'
        title: '⚠️ {{ .GroupLabels.alertname }}'
        color: warning

  - name: pagerduty
    pagerduty_configs:
      - service_key: ${PAGERDUTY_SERVICE_KEY}
        severity: critical
        description: '{{ .GroupLabels.alertname }}'

inhibit_rules:
  - source_match:
      severity: critical
    target_match:
      severity: warning
    equal: [alertname, cluster, service]
```

---

## SLO Framework

### Defining SLOs
```yaml
# slo.yaml
service: api-gateway
slos:
  - name: availability
    description: "API should be available 99.9% of the time"
    sli:
      type: availability
      metric: |
        sum(rate(http_requests_total{status!~"5.."}[{{window}}]))
        /
        sum(rate(http_requests_total[{{window}}]))
    target: 0.999
    window: 30d
    
  - name: latency-p99
    description: "99th percentile latency should be under 500ms"
    sli:
      type: latency
      metric: |
        histogram_quantile(0.99, 
          sum(rate(http_request_duration_seconds_bucket[{{window}}])) by (le)
        )
    target: 0.5  # 500ms
    window: 30d
    
  - name: throughput
    description: "System should handle at least 1000 RPS"
    sli:
      type: throughput
      metric: sum(rate(http_requests_total[5m]))
    target: 1000
    window: 5m

error_budget:
  monthly_budget_minutes: 43.2  # 99.9% over 30 days
  burn_rate_alerts:
    - name: fast_burn
      short_window: 5m
      long_window: 1h
      burn_rate: 14.4
      severity: critical
    - name: slow_burn
      short_window: 30m
      long_window: 6h
      burn_rate: 6
      severity: warning
```

---

## Runbook Template

```markdown
# Runbook: {{ALERT_NAME}}

## Overview
**Severity**: {{SEVERITY}}
**Service**: {{SERVICE}}
**SLO Impact**: {{SLO_IMPACT}}

## Alert Condition
```promql
{{ALERT_QUERY}}
```

## Impact
{{BUSINESS_IMPACT}}

## Quick Actions

### 1. Verify the Alert
```bash
# Check current value
curl -s "http://prometheus:9090/api/v1/query?query={{QUERY}}" | jq

# Check recent history
curl -s "http://prometheus:9090/api/v1/query_range?query={{QUERY}}&start={{START}}&end={{END}}&step=1m" | jq
```

### 2. Check Service Health
```bash
# Check pods
kubectl get pods -l app={{SERVICE}} -n {{NAMESPACE}}

# Check recent logs
kubectl logs -l app={{SERVICE}} -n {{NAMESPACE}} --tail=100 --since=10m

# Check events
kubectl get events -n {{NAMESPACE}} --sort-by='.lastTimestamp'
```

### 3. Immediate Mitigation
{{MITIGATION_STEPS}}

## Root Cause Investigation
{{INVESTIGATION_STEPS}}

## Escalation
- L1: {{L1_CONTACT}}
- L2: {{L2_CONTACT}}
- L3: {{L3_CONTACT}}

## Post-Incident
- [ ] Update monitoring if needed
- [ ] Create follow-up ticket
- [ ] Update this runbook
```

---

## Report Template

```markdown
# Observability Review — {{SERVICE}}

**Date**: {{DATE}}
**Reviewer**: {{REVIEWER}}

## Summary

| Category | Status | Coverage |
|----------|--------|----------|
| Metrics | 🟢/🟡/🔴 | {{PERCENT}}% |
| Logging | 🟢/🟡/🔴 | {{PERCENT}}% |
| Tracing | 🟢/🟡/🔴 | {{PERCENT}}% |
| Alerting | 🟢/🟡/🔴 | {{PERCENT}}% |
| Dashboards | 🟢/🟡/🔴 | {{PERCENT}}% |

## SLO Status
{{SLO_STATUS}}

## Gaps Identified
{{GAPS}}

## Recommendations
{{RECOMMENDATIONS}}

## Implementation Plan
{{PLAN}}
```

---

## Best Practices Checklist

### Metrics
- [ ] USE method for resources (Utilization, Saturation, Errors)
- [ ] RED method for services (Rate, Errors, Duration)
- [ ] Business metrics tracked
- [ ] Cardinality controlled
- [ ] Proper aggregation rules

### Logging
- [ ] Structured JSON format
- [ ] Correlation IDs present
- [ ] Log levels appropriate
- [ ] PII redacted
- [ ] Retention policy defined

### Tracing
- [ ] All services instrumented
- [ ] Context propagation working
- [ ] Sampling rate appropriate
- [ ] Custom spans for business logic
- [ ] Baggage items when needed

### Alerting
- [ ] SLO-based alerts
- [ ] Runbooks linked
- [ ] Severity levels defined
- [ ] Escalation paths clear
- [ ] Alert fatigue managed

---

## Severity Guide

| Level | Icon | Examples |
|-------|------|----------|
| **Critical** | 🔴 | No metrics, no alerting, data loss risk |
| **High** | 🟠 | Missing SLOs, no distributed tracing |
| **Medium** | 🟡 | Unstructured logs, noisy alerts |
| **Low** | 🟢 | Dashboard improvements, minor gaps |
