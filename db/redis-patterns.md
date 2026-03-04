# Redis — Caching & Data Structure Patterns

> **Purpose**: Production-ready Redis patterns for caching, pub/sub, and data structures  
> **Best For**: Codex, Claude, ChatGPT, Copilot, Agents  
> **Scope**: Caching strategies, data structures, pub/sub, Lua scripting, clustering  
> **Last Updated**: 2026-03

---

## Mission

Help design and implement **Redis solutions** for caching, session management, real-time features, and distributed systems. Focus on appropriate data structures, eviction policies, and high availability patterns.

---

## Guard Clauses

**If no Redis context provided:**
```
NO_REDIS_CONTEXT

Please provide context:
- Use case (caching, sessions, queues, etc.)
- Current data access patterns
- Performance requirements
- Language/framework in use
- Redis version and deployment

Include memory constraints if relevant.
```

**If Redis design is solid:**
```
REDIS_APPROVED

✅ Redis review complete — production ready.

Checks performed:
- Data structures: ✓ (appropriate for use case)
- Key design: ✓ (namespaced, consistent)
- TTL strategy: ✓ (prevents memory bloat)
- Serialization: ✓ (efficient format)

Design follows Redis best practices.
```

---

## Quick Context Checklist

```
☐ Redis version (6.x, 7.x)
☐ Use case (cache, session, queue, etc.)
☐ Expected data volume
☐ Memory constraints
☐ Persistence requirements (RDB/AOF)
☐ High availability needs
☐ Client library in use
☐ Performance requirements
```

---

## Copy-Paste Prompts

### Prompt: Design Redis Caching Strategy
```text
Design a Redis caching strategy for:

Application: {{APPLICATION}}
Data being cached: {{DATA_TYPE}}
Access patterns:
- Read frequency: {{READ_FREQ}}
- Write frequency: {{WRITE_FREQ}}
- Cache hit rate target: {{HIT_RATE}}

Current stack: {{TECH_STACK}}
Memory budget: {{MEMORY}}

Design should include:
1. Key naming convention
2. Data structure choice
3. TTL strategy
4. Invalidation approach
5. Cache-aside vs write-through
6. Example implementation code
```

### Prompt: Implement Real-Time Feature
```text
Implement a Redis-based solution for:

Feature: {{FEATURE}}
Requirements:
- Concurrent users: {{USERS}}
- Latency requirement: {{LATENCY}}
- Data consistency: {{CONSISTENCY}}

Language: {{LANGUAGE}}

Provide:
1. Redis commands/data structures
2. Client implementation code
3. Pub/Sub or Streams if needed
4. Error handling
5. Scaling considerations
```

### Prompt: Review Redis Usage
```text
Review this Redis implementation:

{{CODE_OR_COMMANDS}}

Current issues: {{ISSUES}}

Check for:
1. Key design (namespacing, sizing)
2. Data structure appropriateness
3. Memory efficiency
4. Connection management
5. Error handling
6. Race conditions
7. Scaling readiness
```

### Prompt: Design Rate Limiter
```text
Design a Redis rate limiter for:

API endpoint: {{ENDPOINT}}
Rate limits:
- Requests per second: {{RPS}}
- Burst allowance: {{BURST}}
- By: {{BY_KEY}} (IP, user, API key)

Requirements:
- Distributed (multiple servers)
- Accurate counting
- Low latency

Provide:
1. Algorithm choice (fixed window, sliding window, token bucket)
2. Redis commands/Lua script
3. Client implementation
4. Handling edge cases
```

---

## Data Structure Patterns

### Strings

```redis
# Basic key-value caching
SET user:1001:profile '{"name":"John","email":"john@ex.com"}' EX 3600
GET user:1001:profile

# Atomic counters
INCR page:views:homepage
INCRBY user:1001:points 100
INCRBYFLOAT product:99:rating 0.1

# Distributed locks
SET lock:order:12345 "server-1" NX EX 30
# Returns OK if acquired, nil if already locked

# Bit operations (user activity tracking)
SETBIT user:activity:2026-01-05 1001 1  # User 1001 active on date
GETBIT user:activity:2026-01-05 1001
BITCOUNT user:activity:2026-01-05        # Total active users
BITOP AND active:both day1 day2          # Users active both days
```

### Hashes

```redis
# Store objects (memory efficient)
HSET user:1001 name "John Doe" email "john@ex.com" points 500
HGET user:1001 email
HGETALL user:1001
HMGET user:1001 name email

# Partial updates
HINCRBY user:1001 points 50
HSET user:1001 last_login "2026-01-05T10:30:00Z"

# Scan large hashes
HSCAN user:1001 0 COUNT 100
```

### Lists

```redis
# Message queues (blocking)
LPUSH queue:emails '{"to":"user@ex.com","subject":"Welcome"}'
BRPOP queue:emails 30  # Block for 30 seconds

# Activity feed (capped)
LPUSH user:1001:feed '{"type":"like","post":123}'
LTRIM user:1001:feed 0 99  # Keep last 100 items
LRANGE user:1001:feed 0 9  # Get latest 10

# Reliable queue with backup
BRPOPLPUSH queue:tasks queue:processing 30
# On success: LREM queue:processing 1 task
# On failure: RPOPLPUSH queue:processing queue:tasks
```

### Sets

```redis
# Tags, categories, unique items
SADD product:99:tags "electronics" "wireless" "bluetooth"
SMEMBERS product:99:tags
SISMEMBER product:99:tags "wireless"

# Set operations
SADD user:1001:friends 2001 2002 2003
SADD user:2001:friends 1001 3001 3002
SINTER user:1001:friends user:2001:friends  # Mutual friends
SUNION user:1001:friends user:2001:friends  # All friends
SDIFF user:1001:friends user:2001:friends   # Only 1001's friends

# Random selection
SRANDMEMBER products:featured 5  # 5 random featured products
```

### Sorted Sets

```redis
# Leaderboards
ZADD game:leaderboard 1500 "player:1001"
ZADD game:leaderboard 2000 "player:1002"
ZINCRBY game:leaderboard 100 "player:1001"  # Add points
ZREVRANK game:leaderboard "player:1001"     # Rank (0-indexed)
ZREVRANGE game:leaderboard 0 9 WITHSCORES   # Top 10

# Time-based expiration (delayed jobs)
ZADD queue:delayed 1704470400 '{"job":"send_email","id":123}'
# Score = Unix timestamp when job should run
ZRANGEBYSCORE queue:delayed 0 1704470400 LIMIT 0 10

# Rate limiting (sliding window)
ZADD ratelimit:user:1001 1704470400.123 "req1"
ZREMRANGEBYSCORE ratelimit:user:1001 0 1704470340  # Remove >60s old
ZCARD ratelimit:user:1001  # Count requests in window

# Autocomplete
ZADD autocomplete:products 0 "iphone"
ZADD autocomplete:products 0 "ipad"
ZADD autocomplete:products 0 "ipod"
ZRANGEBYLEX autocomplete:products "[ip" "[ip\xff" LIMIT 0 10
```

### HyperLogLog

```redis
# Cardinality estimation (unique counts)
PFADD visitors:2026-01-05 "user1001" "user1002" "user1003"
PFCOUNT visitors:2026-01-05           # Approximate unique count

# Merge multiple days
PFMERGE visitors:week visitors:2026-01-01 visitors:2026-01-02 ...
PFCOUNT visitors:week

# Memory: ~12KB regardless of cardinality
# Accuracy: 0.81% standard error
```

### Streams

```redis
# Event streaming
XADD orders:stream * customer_id 1001 product_id 99 quantity 2
# Returns: "1704470400123-0" (ID)

# Read new entries
XREAD COUNT 10 BLOCK 5000 STREAMS orders:stream $

# Consumer groups (distributed processing)
XGROUP CREATE orders:stream order-processors $ MKSTREAM

# Consumer reads
XREADGROUP GROUP order-processors consumer-1 COUNT 1 BLOCK 5000 STREAMS orders:stream >

# Acknowledge processing
XACK orders:stream order-processors 1704470400123-0

# Check pending (unacknowledged)
XPENDING orders:stream order-processors

# Claim abandoned messages
XCLAIM orders:stream order-processors consumer-2 60000 1704470400123-0
```

---

## Caching Patterns

### Cache-Aside (Lazy Loading)

```python
# Python example
import json
import redis

r = redis.Redis()

def get_user(user_id: int) -> dict:
    cache_key = f"user:{user_id}"
    
    # Try cache first
    cached = r.get(cache_key)
    if cached:
        return json.loads(cached)
    
    # Cache miss - load from DB
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        # Store in cache with TTL
        r.setex(cache_key, 3600, json.dumps(user.to_dict()))
    
    return user.to_dict() if user else None

def update_user(user_id: int, data: dict):
    # Update DB
    db.query(User).filter(User.id == user_id).update(data)
    db.commit()
    
    # Invalidate cache
    r.delete(f"user:{user_id}")
```

### Write-Through

```python
def update_user(user_id: int, data: dict):
    # Update DB
    user = db.query(User).filter(User.id == user_id).first()
    for key, value in data.items():
        setattr(user, key, value)
    db.commit()
    
    # Update cache immediately
    cache_key = f"user:{user_id}"
    r.setex(cache_key, 3600, json.dumps(user.to_dict()))
    return user
```

### Write-Behind (Write-Back)

```python
def update_user_async(user_id: int, data: dict):
    cache_key = f"user:{user_id}"
    
    # Update cache immediately
    cached = r.get(cache_key)
    if cached:
        user_data = json.loads(cached)
        user_data.update(data)
        r.setex(cache_key, 3600, json.dumps(user_data))
    
    # Queue DB write for later (batch processing)
    r.lpush("queue:user_updates", json.dumps({
        "user_id": user_id,
        "data": data,
        "timestamp": time.time()
    }))
```

### Refresh-Ahead

```python
def get_user_with_refresh(user_id: int) -> dict:
    cache_key = f"user:{user_id}"
    ttl_key = f"user:{user_id}:refresh"
    
    cached = r.get(cache_key)
    if cached:
        user_data = json.loads(cached)
        
        # Check if refresh needed (TTL below threshold)
        if not r.exists(ttl_key):
            # Trigger async refresh
            refresh_cache_async.delay(user_id)
            # Set short TTL to prevent multiple refreshes
            r.setex(ttl_key, 60, "1")
        
        return user_data
    
    # Cache miss - sync load
    return get_user(user_id)
```

---

## Key Design Best Practices

### Naming Convention

```redis
# Pattern: {object-type}:{id}:{sub-object}
# Use colons as separators

# ✅ Good key names
user:1001:profile
user:1001:settings
order:12345:items
session:abc123def456
cache:api:users:list:page:1
ratelimit:ip:192.168.1.1
lock:order:12345

# ❌ Bad key names
user_1001_profile      # Underscores (inconsistent)
USER:1001:PROFILE      # Mixed case
u:1001:p               # Too abbreviated
```

### Key Expiration Strategies

```python
# Spread TTL to prevent thundering herd
import random

def cache_with_jitter(key: str, value: str, base_ttl: int):
    # Add 0-10% jitter
    jitter = random.randint(0, base_ttl // 10)
    ttl = base_ttl + jitter
    r.setex(key, ttl, value)

# Soft vs hard expiration
def get_with_soft_expiry(key: str, soft_ttl: int, hard_ttl: int):
    """
    soft_ttl: When to start background refresh
    hard_ttl: Actual key expiration
    """
    pipe = r.pipeline()
    pipe.get(key)
    pipe.ttl(key)
    value, ttl = pipe.execute()
    
    if value and ttl < hard_ttl - soft_ttl:
        # Trigger background refresh
        refresh_async.delay(key)
    
    return value
```

---

## Rate Limiting

### Fixed Window

```python
def is_rate_limited_fixed(user_id: str, limit: int = 100, window: int = 60) -> bool:
    key = f"ratelimit:fixed:{user_id}:{int(time.time()) // window}"
    
    current = r.incr(key)
    if current == 1:
        r.expire(key, window)
    
    return current > limit
```

### Sliding Window (Lua Script)

```lua
-- sliding_window.lua
local key = KEYS[1]
local now = tonumber(ARGV[1])
local window = tonumber(ARGV[2])
local limit = tonumber(ARGV[3])

-- Remove old entries
redis.call('ZREMRANGEBYSCORE', key, 0, now - window)

-- Count current requests
local count = redis.call('ZCARD', key)

if count < limit then
    -- Add new request
    redis.call('ZADD', key, now, now .. '-' .. math.random())
    redis.call('EXPIRE', key, window)
    return 0  -- Not limited
else
    return 1  -- Rate limited
end
```

```python
# Python client
SLIDING_WINDOW_SCRIPT = """..."""
sliding_window = r.register_script(SLIDING_WINDOW_SCRIPT)

def is_rate_limited_sliding(user_id: str, limit: int = 100, window: int = 60) -> bool:
    key = f"ratelimit:sliding:{user_id}"
    now = time.time()
    return sliding_window(keys=[key], args=[now, window, limit]) == 1
```

### Token Bucket (Lua Script)

```lua
-- token_bucket.lua
local key = KEYS[1]
local capacity = tonumber(ARGV[1])
local rate = tonumber(ARGV[2])  -- tokens per second
local now = tonumber(ARGV[3])
local requested = tonumber(ARGV[4])

local bucket = redis.call('HMGET', key, 'tokens', 'last_update')
local tokens = tonumber(bucket[1]) or capacity
local last_update = tonumber(bucket[2]) or now

-- Add tokens based on time elapsed
local elapsed = now - last_update
tokens = math.min(capacity, tokens + (elapsed * rate))

if tokens >= requested then
    tokens = tokens - requested
    redis.call('HMSET', key, 'tokens', tokens, 'last_update', now)
    redis.call('EXPIRE', key, capacity / rate * 2)
    return 1  -- Allowed
else
    redis.call('HMSET', key, 'tokens', tokens, 'last_update', now)
    redis.call('EXPIRE', key, capacity / rate * 2)
    return 0  -- Denied
end
```

---

## Distributed Locking

### Simple Lock (SET NX)

```python
import uuid
import time

class RedisLock:
    def __init__(self, redis_client, name: str, timeout: int = 10):
        self.redis = redis_client
        self.name = f"lock:{name}"
        self.timeout = timeout
        self.token = str(uuid.uuid4())
    
    def acquire(self, blocking: bool = True, blocking_timeout: int = 10) -> bool:
        start = time.time()
        while True:
            if self.redis.set(self.name, self.token, nx=True, ex=self.timeout):
                return True
            
            if not blocking:
                return False
            
            if time.time() - start > blocking_timeout:
                return False
            
            time.sleep(0.1)
    
    def release(self) -> bool:
        # Only release if we own the lock
        script = """
        if redis.call('get', KEYS[1]) == ARGV[1] then
            return redis.call('del', KEYS[1])
        else
            return 0
        end
        """
        return self.redis.eval(script, 1, self.name, self.token)
    
    def __enter__(self):
        if not self.acquire():
            raise Exception("Could not acquire lock")
        return self
    
    def __exit__(self, *args):
        self.release()

# Usage
with RedisLock(r, "order:12345") as lock:
    # Critical section
    process_order(12345)
```

### Redlock (Multi-Instance)

```python
# For high availability across multiple Redis instances
from redlock import Redlock

dlm = Redlock([
    {"host": "redis1", "port": 6379},
    {"host": "redis2", "port": 6379},
    {"host": "redis3", "port": 6379},
])

lock = dlm.lock("resource_name", 1000)  # 1000ms
if lock:
    try:
        # Critical section
        process_resource()
    finally:
        dlm.unlock(lock)
```

---

## Pub/Sub Patterns

### Basic Pub/Sub

```python
# Publisher
def publish_event(channel: str, event: dict):
    r.publish(channel, json.dumps(event))

# Subscriber
def subscribe_events(channels: list):
    pubsub = r.pubsub()
    pubsub.subscribe(channels)
    
    for message in pubsub.listen():
        if message["type"] == "message":
            event = json.loads(message["data"])
            handle_event(message["channel"], event)

# Pattern subscription
def subscribe_pattern(pattern: str):
    pubsub = r.pubsub()
    pubsub.psubscribe(pattern)  # e.g., "orders:*"
    
    for message in pubsub.listen():
        if message["type"] == "pmessage":
            handle_event(message["channel"], json.loads(message["data"]))
```

### Reliable Messaging with Streams

```python
# Producer
def produce_event(stream: str, event: dict) -> str:
    return r.xadd(stream, event, maxlen=10000)

# Consumer with group
class StreamConsumer:
    def __init__(self, stream: str, group: str, consumer: str):
        self.stream = stream
        self.group = group
        self.consumer = consumer
        self._ensure_group()
    
    def _ensure_group(self):
        try:
            r.xgroup_create(self.stream, self.group, "$", mkstream=True)
        except redis.ResponseError as e:
            if "BUSYGROUP" not in str(e):
                raise
    
    def consume(self, count: int = 10, block: int = 5000):
        messages = r.xreadgroup(
            self.group, self.consumer,
            {self.stream: ">"},
            count=count, block=block
        )
        
        for stream_name, entries in messages or []:
            for entry_id, data in entries:
                yield entry_id, data
    
    def ack(self, entry_id: str):
        r.xack(self.stream, self.group, entry_id)
    
    def recover_pending(self, min_idle: int = 60000):
        """Claim messages that haven't been acked"""
        pending = r.xpending_range(
            self.stream, self.group,
            min="-", max="+", count=10
        )
        
        for entry in pending:
            if entry["time_since_delivered"] > min_idle:
                r.xclaim(
                    self.stream, self.group, self.consumer,
                    min_idle, [entry["message_id"]]
                )
```

---

## Lua Scripting

### Atomic Operations

```lua
-- atomic_increment_if.lua
-- Increment only if value below threshold
local key = KEYS[1]
local threshold = tonumber(ARGV[1])
local increment = tonumber(ARGV[2])

local current = tonumber(redis.call('GET', key) or 0)

if current + increment <= threshold then
    return redis.call('INCRBY', key, increment)
else
    return -1  -- Would exceed threshold
end
```

```lua
-- transfer_balance.lua
-- Atomic balance transfer
local from_key = KEYS[1]
local to_key = KEYS[2]
local amount = tonumber(ARGV[1])

local from_balance = tonumber(redis.call('GET', from_key) or 0)

if from_balance >= amount then
    redis.call('DECRBY', from_key, amount)
    redis.call('INCRBY', to_key, amount)
    return 1  -- Success
else
    return 0  -- Insufficient balance
end
```

### Complex Data Operations

```lua
-- leaderboard_update.lua
-- Update score and return new rank
local leaderboard = KEYS[1]
local player = ARGV[1]
local score_delta = tonumber(ARGV[2])

-- Update score
local new_score = redis.call('ZINCRBY', leaderboard, score_delta, player)

-- Get rank (0-indexed, reversed for high-to-low)
local rank = redis.call('ZREVRANK', leaderboard, player)

return {new_score, rank}
```

```python
# Python client
leaderboard_update = r.register_script("""
local leaderboard = KEYS[1]
local player = ARGV[1]
local score_delta = tonumber(ARGV[2])
local new_score = redis.call('ZINCRBY', leaderboard, score_delta, player)
local rank = redis.call('ZREVRANK', leaderboard, player)
return {new_score, rank}
""")

def update_player_score(player_id: str, points: int) -> tuple:
    result = leaderboard_update(
        keys=["game:leaderboard"],
        args=[f"player:{player_id}", points]
    )
    return float(result[0]), int(result[1])
```

---

## High Availability

### Redis Sentinel

```python
from redis.sentinel import Sentinel

sentinel = Sentinel([
    ('sentinel1', 26379),
    ('sentinel2', 26379),
    ('sentinel3', 26379),
], socket_timeout=0.5)

# Get master
master = sentinel.master_for('mymaster', socket_timeout=0.5)
master.set('key', 'value')

# Get replica for reads
replica = sentinel.slave_for('mymaster', socket_timeout=0.5)
replica.get('key')
```

### Redis Cluster

```python
from redis.cluster import RedisCluster

rc = RedisCluster(
    host='cluster-node-1',
    port=6379,
    decode_responses=True
)

# Cluster handles key distribution automatically
rc.set('user:1001', 'data')
rc.get('user:1001')

# Use hash tags for related keys on same node
rc.set('{user:1001}:profile', '...')
rc.set('{user:1001}:settings', '...')
# Both keys go to same slot due to {user:1001}
```

---

## Memory Optimization

### Memory Analysis

```redis
# Check memory usage
MEMORY USAGE user:1001
MEMORY DOCTOR
INFO memory

# Analyze key patterns
DEBUG OBJECT user:1001
OBJECT ENCODING user:1001
```

### Optimization Techniques

```redis
# Use hashes for small objects (ziplist encoding)
# Up to hash-max-ziplist-entries (512 default)
HSET user:1001 name "John" email "john@ex.com" points 500

# Use shorter keys in high-volume scenarios
# u:1001 vs user:1001

# Use appropriate encoding
CONFIG SET hash-max-ziplist-entries 512
CONFIG SET hash-max-ziplist-value 64
CONFIG SET list-max-ziplist-size -2
CONFIG SET zset-max-ziplist-entries 128

# Eviction policies
CONFIG SET maxmemory 2gb
CONFIG SET maxmemory-policy allkeys-lru  # Or volatile-lru, allkeys-lfu
```

---

## Severity Guide

| Severity | Issue | Impact |
|----------|-------|--------|
| 🔴 Critical | No TTL on cache keys | Memory exhaustion |
| 🔴 Critical | Blocking operations in main thread | Application hangs |
| 🔴 Critical | Storing sensitive data without encryption | Security breach |
| 🟠 High | Large keys (>1MB) | Network/memory issues |
| 🟠 High | Hot keys (single key high traffic) | Node overload |
| 🟡 Medium | Inefficient data structure choice | Memory waste |
| 🟡 Medium | Missing connection pooling | Connection overhead |
| 🟢 Low | Non-namespaced keys | Maintenance difficulty |

---

## Report Template

```markdown
## Redis Review

### Environment
- Redis version: [version]
- Deployment: [standalone/sentinel/cluster]
- Memory: [used/available]
- Keys: [count]

### Usage Analysis
| Pattern | Count | Memory | TTL | Status |
|---------|-------|--------|-----|--------|
| | | | | |

### Data Structure Assessment
| Key Pattern | Structure | Encoding | Appropriate |
|-------------|-----------|----------|-------------|
| | | | |

### Issues Found
1. [Severity] Issue description
   - Key pattern:
   - Impact:
   - Recommendation:

### Recommendations
1. [Priority] Recommendation
   - Benefit:
   - Implementation:
```

---

## Related Prompts

- [nosql-mongodb.md](nosql-mongodb.md) — MongoDB patterns
- [postgresql-optimization.md](postgresql-optimization.md) — PostgreSQL optimization
- [api-design.md](../generic/api-design.md) — API caching strategies

---

*Last updated: 2026-01*
