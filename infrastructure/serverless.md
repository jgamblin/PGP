# Serverless — Functions & Edge Computing

> **Purpose**: Serverless application development and deployment patterns  
> **Best For**: Copilot, ChatGPT, Claude, Agents  
> **Scope**: AWS Lambda, Vercel, Cloudflare Workers, edge functions  
> **Last Updated**: 2026-01

---

## Mission

Help build **production-ready serverless applications** with proper architecture, cold start optimization, and deployment patterns. Focus on practical solutions across major serverless platforms.

---

## Guard Clauses

**If no serverless context provided:**
```
NO_SERVERLESS_CONTEXT

Please provide serverless context:
- Platform (AWS Lambda, Vercel, Cloudflare Workers, etc.)
- Use case (API, event processing, scheduled tasks, etc.)
- Language/runtime
- Or describe what you're building
```

**If configuration is optimized:**
```
SERVERLESS_OPTIMIZED

✅ Serverless configuration review complete — production ready.

Checks performed:
- Function size: ✓ (optimized bundle)
- Memory/timeout: ✓ (appropriate settings)
- Cold starts: ✓ (mitigated where needed)
- Error handling: ✓ (proper retries and DLQ)
- Security: ✓ (least privilege, secrets management)

Configuration follows serverless best practices.
```

---

## Quick Context Checklist

```
☐ Serverless platform
☐ Use case (API, events, scheduled)
☐ Language and runtime version
☐ Expected traffic patterns
☐ Latency requirements
☐ External dependencies (DB, APIs)
☐ Deployment method (SAM, Serverless Framework, CDK)
```

---

## Copy-Paste Prompts

### Prompt: Design Serverless Architecture
```text
Design serverless architecture for:

Use case: {{USE_CASE}}
Platform: {{PLATFORM}}
Expected traffic: {{TRAFFIC}}

Requirements:
- Latency: {{LATENCY_REQUIREMENT}}
- Availability: {{AVAILABILITY}}
- Data storage: {{STORAGE}}
- External integrations: {{INTEGRATIONS}}

Generate:
1. Architecture diagram (Mermaid)
2. Function breakdown with responsibilities
3. Event flow between components
4. Data storage strategy
5. Error handling approach
6. Cost estimate

Consider:
- Cold start impact
- Concurrency limits
- Idempotency requirements
- Observability needs
```

### Prompt: AWS Lambda Function Review
```text
Review this AWS Lambda function:

{{CODE}}

Configuration:
- Runtime: {{RUNTIME}}
- Memory: {{MEMORY}}
- Timeout: {{TIMEOUT}}
- Trigger: {{TRIGGER}}

Check for:
1. **Performance**
   - Cold start optimization
   - Connection reuse
   - Bundle size
   - Memory vs CPU balance

2. **Reliability**
   - Error handling
   - Retry logic
   - Idempotency
   - Timeout handling

3. **Security**
   - IAM permissions (least privilege)
   - Input validation
   - Secret management
   - VPC configuration (if needed)

4. **Observability**
   - Structured logging
   - Metrics
   - Tracing (X-Ray)

5. **Cost**
   - Right-sized memory
   - Execution time optimization
   - Unnecessary invocations

Provide optimized code and configuration.
```

### Prompt: Cloudflare Worker Development
```text
Create a Cloudflare Worker for:

Purpose: {{PURPOSE}}
Routes: {{ROUTES}}

Requirements:
- KV storage: {{KV_NEEDS}}
- D1 database: {{D1_NEEDS}}
- R2 storage: {{R2_NEEDS}}
- External APIs: {{APIS}}

Generate:
1. Worker code with proper error handling
2. wrangler.toml configuration
3. Type definitions (if TypeScript)
4. Test examples
5. Deployment instructions

Optimize for:
- Sub-50ms response times
- Edge caching strategies
- Global distribution
```

### Prompt: Vercel Serverless Functions
```text
Create Vercel serverless functions for:

Framework: {{FRAMEWORK}} (Next.js, SvelteKit, etc.)
Routes: {{ROUTES}}

Requirements:
- Database: {{DATABASE}}
- Authentication: {{AUTH}}
- File uploads: {{UPLOADS}}

Generate:
1. API route handlers
2. Middleware configuration
3. Edge vs Node.js runtime selection
4. Environment variable setup
5. vercel.json configuration

Consider:
- Edge runtime for low latency
- Streaming responses
- ISR/SSG where applicable
```

### Prompt: Event-Driven Architecture
```text
Design event-driven serverless system:

Events: {{EVENT_TYPES}}
Producers: {{PRODUCERS}}
Consumers: {{CONSUMERS}}

Requirements:
- Ordering: {{ORDERING_NEEDS}}
- Exactly-once: {{DELIVERY_GUARANTEE}}
- Throughput: {{THROUGHPUT}}

Generate:
1. Event schema definitions
2. Event bus/queue configuration
3. Consumer function patterns
4. Dead letter queue handling
5. Replay strategy
6. Monitoring approach
```

### Prompt: Cold Start Optimization
```text
Optimize cold starts for this Lambda:

{{CODE}}

Current metrics:
- Cold start duration: {{COLD_START_MS}}
- Warm invocation: {{WARM_MS}}
- Memory: {{MEMORY}}
- Bundle size: {{SIZE}}

Analyze and optimize:
1. Bundle size reduction
2. Lazy loading opportunities
3. SDK initialization
4. Connection pooling
5. Provisioned concurrency need
6. SnapStart eligibility (Java)

Provide optimized code and configuration.
```

---

## AWS Lambda Patterns

### Optimized Handler Structure
```python
# Python Lambda with connection reuse
import json
import boto3
from functools import lru_cache

# Initialize outside handler (reused across invocations)
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('my-table')

@lru_cache(maxsize=1)
def get_secret():
    """Cache secrets for warm invocations."""
    client = boto3.client('secretsmanager')
    response = client.get_secret_value(SecretId='my-secret')
    return json.loads(response['SecretString'])

def handler(event, context):
    """Main handler - keep lightweight."""
    try:
        # Input validation
        body = json.loads(event.get('body', '{}'))
        
        # Business logic
        result = process_request(body)
        
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'X-Request-Id': context.aws_request_id
            },
            'body': json.dumps(result)
        }
    except ValidationError as e:
        return {'statusCode': 400, 'body': json.dumps({'error': str(e)})}
    except Exception as e:
        print(f'Error: {e}')  # CloudWatch Logs
        return {'statusCode': 500, 'body': json.dumps({'error': 'Internal error'})}
```

```typescript
// TypeScript Lambda with Powertools
import { Logger, Tracer, Metrics } from '@aws-lambda-powertools/';
import { APIGatewayProxyHandler } from 'aws-lambda';

const logger = new Logger();
const tracer = new Tracer();
const metrics = new Metrics();

// Connection reuse
import { DynamoDBClient } from '@aws-sdk/client-dynamodb';
const client = new DynamoDBClient({});

export const handler: APIGatewayProxyHandler = async (event, context) => {
  // Add correlation IDs
  logger.addContext(context);
  
  const segment = tracer.getSegment();
  
  try {
    logger.info('Processing request', { path: event.path });
    
    const result = await processRequest(event);
    
    metrics.addMetric('SuccessfulRequests', 1);
    
    return {
      statusCode: 200,
      body: JSON.stringify(result),
    };
  } catch (error) {
    logger.error('Request failed', { error });
    metrics.addMetric('FailedRequests', 1);
    throw error;
  }
};
```

### SAM Template
```yaml
AWSTemplateFormatVersion: '2010-09-09'
Transform: AWS::Serverless-2016-10-31
Description: Serverless API

Globals:
  Function:
    Runtime: python3.12
    MemorySize: 256
    Timeout: 30
    Tracing: Active
    Environment:
      Variables:
        LOG_LEVEL: INFO
        POWERTOOLS_SERVICE_NAME: my-service

Resources:
  ApiFunction:
    Type: AWS::Serverless::Function
    Properties:
      FunctionName: !Sub ${AWS::StackName}-api
      Handler: app.handler
      CodeUri: src/
      Description: API handler
      Architectures:
        - arm64  # Graviton2 - better price/performance
      Events:
        Api:
          Type: Api
          Properties:
            Path: /{proxy+}
            Method: ANY
      Policies:
        - DynamoDBCrudPolicy:
            TableName: !Ref DataTable
      Environment:
        Variables:
          TABLE_NAME: !Ref DataTable
    Metadata:
      BuildMethod: esbuild  # For Node.js
      BuildProperties:
        Minify: true
        Target: es2022

  DataTable:
    Type: AWS::DynamoDB::Table
    Properties:
      TableName: !Sub ${AWS::StackName}-data
      BillingMode: PAY_PER_REQUEST
      AttributeDefinitions:
        - AttributeName: pk
          AttributeType: S
        - AttributeName: sk
          AttributeType: S
      KeySchema:
        - AttributeName: pk
          KeyType: HASH
        - AttributeName: sk
          KeyType: RANGE

Outputs:
  ApiEndpoint:
    Value: !Sub https://${ServerlessRestApi}.execute-api.${AWS::Region}.amazonaws.com/Prod/
```

---

## Cloudflare Workers

### Basic Worker
```typescript
// src/index.ts
export interface Env {
  MY_KV: KVNamespace;
  DB: D1Database;
  BUCKET: R2Bucket;
  API_KEY: string;
}

export default {
  async fetch(request: Request, env: Env, ctx: ExecutionContext): Promise<Response> {
    const url = new URL(request.url);
    
    // Simple router
    switch (url.pathname) {
      case '/api/data':
        return handleData(request, env);
      case '/api/upload':
        return handleUpload(request, env);
      default:
        return new Response('Not Found', { status: 404 });
    }
  },
  
  // Scheduled tasks
  async scheduled(event: ScheduledEvent, env: Env, ctx: ExecutionContext) {
    ctx.waitUntil(processScheduledTask(env));
  },
};

async function handleData(request: Request, env: Env): Promise<Response> {
  // Check cache first
  const cacheKey = new URL(request.url).pathname;
  const cached = await env.MY_KV.get(cacheKey);
  
  if (cached) {
    return new Response(cached, {
      headers: { 'Content-Type': 'application/json', 'X-Cache': 'HIT' },
    });
  }
  
  // Query D1
  const { results } = await env.DB.prepare(
    'SELECT * FROM items WHERE active = ?'
  ).bind(1).all();
  
  const response = JSON.stringify(results);
  
  // Cache for 5 minutes
  await env.MY_KV.put(cacheKey, response, { expirationTtl: 300 });
  
  return new Response(response, {
    headers: { 'Content-Type': 'application/json', 'X-Cache': 'MISS' },
  });
}
```

### wrangler.toml
```toml
name = "my-worker"
main = "src/index.ts"
compatibility_date = "2024-01-01"

# KV Namespace
[[kv_namespaces]]
binding = "MY_KV"
id = "xxx"

# D1 Database
[[d1_databases]]
binding = "DB"
database_name = "my-db"
database_id = "xxx"

# R2 Bucket
[[r2_buckets]]
binding = "BUCKET"
bucket_name = "my-bucket"

# Environment variables (secrets via wrangler secret)
[vars]
ENVIRONMENT = "production"

# Routes
[triggers]
crons = ["0 * * * *"]  # Every hour

# Custom domains
routes = [
  { pattern = "api.example.com/*", custom_domain = true }
]
```

---

## Vercel Edge Functions

### Next.js API Route (Edge)
```typescript
// app/api/data/route.ts
import { NextRequest, NextResponse } from 'next/server';

export const runtime = 'edge';  // Use edge runtime

export async function GET(request: NextRequest) {
  const { searchParams } = new URL(request.url);
  const id = searchParams.get('id');
  
  // Use edge-compatible fetch
  const data = await fetch(`https://api.example.com/data/${id}`, {
    headers: {
      'Authorization': `Bearer ${process.env.API_KEY}`,
    },
    next: { revalidate: 60 },  // Cache for 60 seconds
  });
  
  if (!data.ok) {
    return NextResponse.json(
      { error: 'Failed to fetch data' },
      { status: data.status }
    );
  }
  
  return NextResponse.json(await data.json());
}

export async function POST(request: NextRequest) {
  const body = await request.json();
  
  // Validate input
  if (!body.name) {
    return NextResponse.json(
      { error: 'Name is required' },
      { status: 400 }
    );
  }
  
  // Process request
  const result = await processData(body);
  
  return NextResponse.json(result, { status: 201 });
}
```

### Middleware (Edge)
```typescript
// middleware.ts
import { NextResponse } from 'next/server';
import type { NextRequest } from 'next/server';

export function middleware(request: NextRequest) {
  // Rate limiting with edge KV
  const ip = request.ip ?? '127.0.0.1';
  
  // Auth check
  const token = request.headers.get('authorization');
  if (!token && request.nextUrl.pathname.startsWith('/api/protected')) {
    return NextResponse.json(
      { error: 'Unauthorized' },
      { status: 401 }
    );
  }
  
  // Add headers
  const response = NextResponse.next();
  response.headers.set('X-Request-Id', crypto.randomUUID());
  
  return response;
}

export const config = {
  matcher: '/api/:path*',
};
```

---

## Event Processing Patterns

### SQS Consumer
```python
import json
from typing import Any

def handler(event: dict, context: Any) -> dict:
    """Process SQS messages with partial batch response."""
    batch_item_failures = []
    
    for record in event['Records']:
        try:
            message = json.loads(record['body'])
            process_message(message)
        except Exception as e:
            print(f"Error processing message {record['messageId']}: {e}")
            batch_item_failures.append({
                'itemIdentifier': record['messageId']
            })
    
    return {
        'batchItemFailures': batch_item_failures
    }

def process_message(message: dict) -> None:
    """Process individual message - implement idempotency."""
    message_id = message['id']
    
    # Check if already processed (idempotency)
    if is_processed(message_id):
        print(f"Message {message_id} already processed, skipping")
        return
    
    # Process
    do_work(message)
    
    # Mark as processed
    mark_processed(message_id)
```

### EventBridge Pattern
```yaml
# SAM template for EventBridge
Resources:
  OrderEventRule:
    Type: AWS::Events::Rule
    Properties:
      EventBusName: !Ref OrderEventBus
      EventPattern:
        source:
          - orders
        detail-type:
          - OrderCreated
          - OrderUpdated
      Targets:
        - Id: ProcessOrderFunction
          Arn: !GetAtt ProcessOrderFunction.Arn
          DeadLetterConfig:
            Arn: !GetAtt OrderDLQ.Arn
          RetryPolicy:
            MaximumRetryAttempts: 3
            MaximumEventAgeInSeconds: 3600
```

---

## Cost Optimization

### Memory vs Duration Trade-off
```
| Memory | CPU     | Cost/ms | Typical Use Case          |
|--------|---------|---------|---------------------------|
| 128MB  | Minimal | Lowest  | Simple transformations    |
| 256MB  | 0.167   | Low     | API handlers, light I/O   |
| 512MB  | 0.333   | Medium  | DB queries, file processing|
| 1024MB | 0.667   | Medium  | Image processing, parsing |
| 2048MB | 1.333   | Higher  | ML inference, heavy compute|
| 3008MB | 2.0     | High    | Max single-core performance|
```

### Power Tuning
```bash
# Use AWS Lambda Power Tuning to find optimal memory
# https://github.com/alexcasalboni/aws-lambda-power-tuning

# Input payload
{
  "lambdaARN": "arn:aws:lambda:us-east-1:xxx:function:my-function",
  "powerValues": [128, 256, 512, 1024, 2048],
  "num": 50,
  "payload": "{\"test\": true}"
}
```

---

## Observability

### Structured Logging
```python
import json
import os

def log(level: str, message: str, **kwargs):
    """Structured logging for CloudWatch Logs Insights."""
    print(json.dumps({
        'level': level,
        'message': message,
        'service': os.environ.get('SERVICE_NAME', 'unknown'),
        'function': os.environ.get('AWS_LAMBDA_FUNCTION_NAME'),
        'request_id': os.environ.get('_X_AMZN_REQUEST_ID'),
        **kwargs
    }))

# Usage
log('INFO', 'Processing order', order_id='123', customer_id='456')
log('ERROR', 'Payment failed', order_id='123', error='Card declined')
```

### CloudWatch Insights Queries
```
# Find slow invocations
fields @timestamp, @requestId, @duration
| filter @duration > 1000
| sort @duration desc
| limit 20

# Error analysis
fields @timestamp, @message
| filter @message like /ERROR/
| stats count() by bin(1h)

# Cold starts
filter @type = "REPORT"
| fields @requestId, @duration, @billedDuration, @memorySize, @maxMemoryUsed
| filter @initDuration > 0
| stats count() as coldStarts, avg(@initDuration) as avgColdStart by bin(1h)
```

---

## Report Template

```markdown
# Serverless Review — {{FUNCTION_NAME}}

**Date**: {{DATE}}
**Platform**: {{PLATFORM}}
**Runtime**: {{RUNTIME}}

## Summary

| Category | Status | Issues |
|----------|--------|--------|
| Performance | 🟢/🟡/🔴 | {{COUNT}} |
| Reliability | 🟢/🟡/🔴 | {{COUNT}} |
| Security | 🟢/🟡/🔴 | {{COUNT}} |
| Cost | 🟢/🟡/🔴 | {{COUNT}} |

## Metrics

| Metric | Current | Recommended |
|--------|---------|-------------|
| Memory | {{MEM}} | {{REC_MEM}} |
| Timeout | {{TIMEOUT}} | {{REC_TIMEOUT}} |
| Cold Start | {{COLD}} | < 500ms |
| Bundle Size | {{SIZE}} | < 5MB |

## Issues & Recommendations
{{RECOMMENDATIONS}}

## Optimized Code
{{OPTIMIZED_CODE}}
```

---

## Best Practices

### General
- Keep functions focused (single responsibility)
- Initialize SDK clients outside handler
- Use environment variables for configuration
- Implement idempotency for event processing
- Set appropriate timeout (not too long, not too short)

### Performance
- Right-size memory (affects CPU too)
- Minimize bundle size
- Use arm64 architecture where available
- Consider provisioned concurrency for latency-sensitive
- Lazy load heavy dependencies

### Security
- Least privilege IAM permissions
- Use Secrets Manager/Parameter Store for secrets
- Validate all inputs
- Enable VPC only when necessary (adds cold start)
- Use function URLs with IAM auth when appropriate

### Cost
- Avoid over-provisioning memory
- Use reserved concurrency to limit scale
- Consider Graviton2/arm64 (20% cheaper)
- Batch operations where possible
- Use EventBridge Scheduler instead of CloudWatch Events

---

## Severity Guide

| Level | Icon | Examples |
|-------|------|----------|
| **Critical** | 🔴 | Hardcoded secrets, excessive IAM permissions, no error handling |
| **High** | 🟠 | No DLQ for async, missing timeouts, cold start > 3s |
| **Medium** | 🟡 | Suboptimal memory, missing structured logging |
| **Low** | 🟢 | Minor optimization opportunities |
