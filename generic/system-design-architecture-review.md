# System Design & Architecture Review — Technical Evaluation

> **Purpose**: Evaluate and improve system architecture  
> **Best For**: Copilot, ChatGPT, Claude, Agents  
> **Scope**: Any scale system  
> **Last Updated**: 2025-12

---

## Mission

Help **review and design system architectures** that are scalable, maintainable, and resilient. Identify bottlenecks, single points of failure, and opportunities for improvement.

---

## Guard Clauses

**If no system description provided:**
```
SYSTEM_DESCRIPTION_REQUIRED

Please provide:
1. System overview (what does it do?)
2. Current architecture diagram or description
3. Scale requirements (users, requests/sec, data volume)
4. Pain points or specific concerns

Even a rough sketch or text description helps.
```

**If simple CRUD app:**
```
SIMPLE_SYSTEM

This appears to be a straightforward CRUD application.

Standard recommendations apply:
- Use a relational database (PostgreSQL)
- Add caching layer if needed (Redis)
- Deploy behind a load balancer
- Standard REST or GraphQL API

No complex architecture patterns needed at this scale.
Want me to focus on something specific instead?
```

---

## Quick Context Checklist

```
☐ System purpose and requirements
☐ Current architecture (diagram or description)
☐ Scale requirements (users, RPS, data)
☐ Tech stack in use
☐ Known pain points
☐ Budget/team constraints
```

---

## Copy-Paste Architecture Prompts

### Prompt: Architecture Review
```text
Review this system architecture:

[PASTE ARCHITECTURE DESCRIPTION OR DIAGRAM]

Current scale: [USERS/RPS/DATA VOLUME]
Expected growth: [NEXT 1-2 YEARS]

Analyze:
1. Scalability bottlenecks
2. Single points of failure
3. Data flow issues
4. Security concerns
5. Cost optimization opportunities

Provide specific recommendations with priority.
```

### Prompt: Design New System
```text
Design a system for:

Purpose: [WHAT IT DOES]
Users: [EXPECTED SCALE]
Requirements:
- [KEY REQUIREMENT 1]
- [KEY REQUIREMENT 2]
- [KEY REQUIREMENT 3]

Constraints:
- Budget: [HIGH/MEDIUM/LOW]
- Team size: [NUMBER]
- Timeline: [MONTHS]

Provide:
1. High-level architecture
2. Component breakdown
3. Technology recommendations
4. Data flow diagram
5. Deployment strategy
```

### Prompt: Scale Existing System
```text
Help scale this system:

Current state:
- [CURRENT ARCHITECTURE]
- [CURRENT LOAD]
- [CURRENT PAIN POINTS]

Target:
- [10X / 100X / 1000X] current load
- [SPECIFIC REQUIREMENTS]

What changes are needed? Prioritize by impact and effort.
```

### Prompt: Database Design
```text
Design the database schema for:

System: [DESCRIPTION]
Main entities: [LIST]
Access patterns:
- [READ-HEAVY / WRITE-HEAVY / BALANCED]
- [COMMON QUERIES]

Requirements:
- [CONSISTENCY / AVAILABILITY PREFERENCE]
- [EXPECTED DATA VOLUME]

Recommend:
1. Database choice (SQL vs NoSQL)
2. Schema design
3. Indexing strategy
4. Scaling approach
```

### Prompt: Microservices Breakdown
```text
Help break this monolith into microservices:

Current monolith:
[DESCRIPTION OF MODULES/FEATURES]

Pain points:
- [WHY BREAK IT UP]

Team structure:
- [NUMBER OF TEAMS]

Propose:
1. Service boundaries
2. Communication patterns (sync/async)
3. Data ownership
4. Migration strategy
5. Shared infrastructure needs
```

---

## Architecture Patterns Reference

### Scalability Patterns

| Pattern | Use When | Trade-offs |
|---------|----------|------------|
| **Horizontal Scaling** | Stateless services | Requires load balancing |
| **Vertical Scaling** | Quick fix, DB scaling | Has limits, costly |
| **Caching** | Read-heavy, repeated queries | Cache invalidation |
| **CDN** | Static content, global users | Cost at scale |
| **Database Sharding** | Massive data, write-heavy | Complexity, cross-shard queries |
| **Read Replicas** | Read-heavy workloads | Replication lag |
| **Event-Driven** | Async processing, decoupling | Eventual consistency |
| **CQRS** | Different read/write patterns | Complexity |

### Reliability Patterns

| Pattern | Purpose | When to Use |
|---------|---------|-------------|
| **Load Balancer** | Distribute traffic | Multiple instances |
| **Circuit Breaker** | Prevent cascade failures | External dependencies |
| **Retry with Backoff** | Handle transient failures | Network calls |
| **Health Checks** | Detect failures | All services |
| **Graceful Degradation** | Maintain partial service | Non-critical features |
| **Bulkhead** | Isolate failures | Multi-tenant, critical paths |

### Data Patterns

| Pattern | Use Case | Considerations |
|---------|----------|----------------|
| **Event Sourcing** | Audit trail, rebuild state | Storage growth |
| **Saga** | Distributed transactions | Compensation logic |
| **Outbox** | Reliable messaging | Additional table |
| **Change Data Capture** | Sync between systems | Infra overhead |

---

## Common Architectures

### Three-Tier Web App
```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   Client    │────▶│   Server    │────▶│  Database   │
│   (React)   │     │  (Node/API) │     │ (PostgreSQL)│
└─────────────┘     └─────────────┘     └─────────────┘
```
**Best for**: Small-medium apps, < 10K concurrent users

### Scaled Web App
```
                    ┌─────────────┐
                    │     CDN     │
                    └──────┬──────┘
                           │
┌─────────────┐     ┌──────▼──────┐
│   Client    │────▶│    Load     │
└─────────────┘     │   Balancer  │
                    └──────┬──────┘
                           │
              ┌────────────┼────────────┐
              │            │            │
        ┌─────▼─────┐┌─────▼─────┐┌─────▼─────┐
        │  Server 1 ││  Server 2 ││  Server N │
        └─────┬─────┘└─────┬─────┘└─────┬─────┘
              │            │            │
              └────────────┼────────────┘
                           │
                    ┌──────▼──────┐     ┌───────────┐
                    │    Cache    │────▶│  Database │
                    │   (Redis)   │     │ (Primary) │
                    └─────────────┘     └─────┬─────┘
                                              │
                                        ┌─────▼─────┐
                                        │  Replica  │
                                        └───────────┘
```
**Best for**: Medium-large apps, 10K-100K+ concurrent users

### Event-Driven Microservices
```
┌──────────┐     ┌──────────┐     ┌──────────┐
│ Service A│────▶│  Message │────▶│ Service B│
└──────────┘     │   Queue  │     └──────────┘
                 │ (Kafka)  │
┌──────────┐     │          │     ┌──────────┐
│ Service C│────▶│          │────▶│ Service D│
└──────────┘     └──────────┘     └──────────┘
```
**Best for**: Large systems, independent scaling, async workflows

---

## Evaluation Checklist

### Scalability
- [ ] Can handle 10X current load?
- [ ] Stateless services (easy horizontal scaling)?
- [ ] Database can scale (sharding, read replicas)?
- [ ] Caching strategy in place?
- [ ] CDN for static content?

### Reliability
- [ ] No single points of failure?
- [ ] Health checks on all services?
- [ ] Circuit breakers for external calls?
- [ ] Graceful degradation possible?
- [ ] Disaster recovery plan?

### Maintainability
- [ ] Clear service boundaries?
- [ ] Well-documented APIs?
- [ ] Monitoring and alerting?
- [ ] Deployment automation?
- [ ] Reasonable complexity for team?

### Security
- [ ] Authentication/authorization?
- [ ] Data encryption (transit + rest)?
- [ ] Network segmentation?
- [ ] Secret management?
- [ ] Input validation everywhere?

### Cost
- [ ] Right-sized infrastructure?
- [ ] Auto-scaling configured?
- [ ] Reserved instances for steady load?
- [ ] Unused resources identified?

---

## Report Format

### Architecture Review: `arch-review-[YYYY-MM-DD].md`

```markdown
# Architecture Review

## System Overview
- **Purpose**: [What the system does]
- **Scale**: [Current users/RPS/data]
- **Tech Stack**: [Key technologies]

## Current Architecture
[Diagram or description]

## Findings

### 🔴 Critical Issues
| Issue | Impact | Recommendation |
|-------|--------|----------------|

### �� High Priority
| Issue | Impact | Recommendation |
|-------|--------|----------------|

### 🟡 Medium Priority
| Issue | Impact | Recommendation |
|-------|--------|----------------|

### 🟢 Improvements
| Area | Suggestion | Benefit |
|------|------------|---------|

## Recommended Architecture
[Proposed changes with diagram]

## Migration Path
1. [Phase 1 - Quick wins]
2. [Phase 2 - Core changes]
3. [Phase 3 - Optimization]

## Estimated Effort
| Change | Effort | Priority |
|--------|--------|----------|
```

---

## Severity Guide

| Level | Icon | Impact | Examples |
|-------|------|--------|----------|
| **Critical** | 🔴 | System failure risk | SPOF, no backups, security hole |
| **High** | 🟠 | Performance/reliability | Bottleneck, missing monitoring |
| **Medium** | 🟡 | Technical debt | Tight coupling, missing docs |
| **Low** | 🟢 | Optimization | Cost savings, minor improvements |

---

## Questions to Ask

### Understanding the System
1. What problem does this system solve?
2. Who are the users? How many?
3. What are the critical paths?
4. What data is most important?

### Scale Requirements
1. Current load vs expected growth?
2. Peak traffic patterns?
3. Latency requirements?
4. Data retention needs?

### Constraints
1. Budget limitations?
2. Team expertise?
3. Existing infrastructure?
4. Compliance requirements?
