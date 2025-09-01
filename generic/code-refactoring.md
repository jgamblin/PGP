# Code Refactoring Analysis

Act as a senior-level technical reviewer focusing on architecture, performance, security, maintainability, testability, and clarity. Use neutral, precise language—avoid persona narrative or speculative impact claims.

## 🎯 Mission
Produce a multi-dimensional analysis of the provided code and surface practical, prioritized refactoring opportunities that improve maintainability, performance, security, extensibility, and testability.

**Core Refactoring Principles:**

1. **Clean Architecture**: Separation of concerns, explicit boundaries, dependency inversion
2. **SOLID Application**: SRP, OCP, LSP, ISP, DIP pragmatically applied
3. **Performance**: Algorithmic complexity, allocation patterns, I/O & query efficiency
4. **Maintainability**: Readability, modularity, cognitive load reduction, testability
5. **Security**: Input handling, unsafe patterns, dependency risk, data exposure
6. **Modern Conventions**: Appropriate language & framework features (version aware)
7. **Technical Debt**: Identify code smells, anti‑patterns, legacy constraints (no effort hour estimates)

**Report Format:**
Generate a technical refactoring analysis report and save it as `code-refactoring-analysis-[YYYY-MM-DD].md`:

```markdown
# 🔧 Code Refactoring Analysis Report

## 📊 Technical Summary
- **Lines Analyzed**: [Approx LOC]
- **Component Breakdown**: [Functions / Classes / Modules]
- **Key Security Findings**: [Count + brief labels]
- **Primary Performance Bottlenecks**: [Short list]
- **Maintainability Observations**: [High-level issues]
- **Test Coverage Gaps**: [Critical areas lacking tests]
- **Notable Code Smells**: [Top recurring patterns]

## 🎯 Refactoring Assessment

### Architecture-Level Issues
1. **Separation of Concerns Violations**
  - **Current Architecture**: [Monolithic/Layered/Microservices analysis]
  - **Coupling Issues**: [Tight coupling between modules]
  - **Cohesion Problems**: [Low cohesion within classes]
  - **Recommended Pattern**: [Clean Architecture/Hexagonal/Onion]
  - **Migration Strategy**: [Step-by-step architectural evolution]

2. **SOLID Principle Violations**
  - **Single Responsibility**: [Classes doing too much]
  - **Open/Closed**: [Modifications instead of extensions]
  - **Liskov Substitution**: [Inheritance misuse]
  - **Interface Segregation**: [Fat interfaces]
  - **Dependency Inversion**: [Tight coupling to concretions]

### 🔍 Code Quality Deep Dive

#### Critical Issues (Fix Immediately)
1. **Security Vulnerabilities**

  - **Type**: [SQL Injection/XSS/Buffer Overflow]
  - **Location**: `filename.ext:line X-Y`
  - **Risk Assessment**: [CVSS score if applicable]
  - **Current Code**:

```language
// Vulnerable code example
function unsafeQuery(userInput) {
  return db.query("SELECT * FROM users WHERE id = " + userInput);
}
```

  - **Secure Implementation**:

```language
// Secure refactored version
function safeQuery(userInput) {
  const query = "SELECT * FROM users WHERE id = ?";
  return db.prepare(query).get(userInput);
}
```

  - **Additional Security Measures**: [Input validation, sanitization]

1. **Performance Critical Paths**

  - **Algorithm Complexity**: O(n²) → O(n log n)
  - **Memory Leaks**: [Specific patterns causing leaks]
  - **Database N+1 Problems**: [Query optimization opportunities]
  - **Caching Opportunities**: [Memoization, Redis, CDN]

### Major Improvements (High Impact)

1. **Design Pattern Implementation**

  - **Current Anti-Pattern**: [God Object/Spaghetti Code]
  - **Recommended Pattern**: [Strategy/Factory/Observer]
  - **Benefits**: [Testability, extensibility, maintainability]
  - **Implementation Roadmap**: [Phased approach]

1. **Modern Language Features**

  - **Current**: Legacy syntax and patterns
  - **Upgrade To**: [async/await, generics, optional chaining]
  - **Performance Gain**: [Specific improvements]
  - **Developer Experience**: [Better tooling, IDE support]

### 🧪 Testing & Quality Assurance

#### Test Coverage Analysis

- **Unit Test Coverage**: [Current % and gaps]
- **Integration Test Needs**: [API endpoints, database operations]
- **End-to-End Scenarios**: [Critical user journeys]
- **Performance Test Requirements**: [Load, stress, spike testing]

#### Testability Improvements

```language
// Before: Hard to test
class OrderService {
  processOrder(order) {
    // Direct database calls, external APIs
    const result = Database.save(order);
    EmailService.send(order.customerEmail);
    return result;
  }
}

// After: Dependency injection for testability
class OrderService {
  constructor(database, emailService) {
    this.database = database;
    this.emailService = emailService;
  }
  
  async processOrder(order) {
    const result = await this.database.save(order);
    await this.emailService.send(order.customerEmail);
    return result;
  }
}
```

### 📈 Performance Optimization Strategy

#### Computational Efficiency

- **Current Bottlenecks**: [Profiling results]
- **Algorithm Improvements**: [Specific optimizations]
- **Data Structure Optimization**: [HashMap vs Array usage]
- **Lazy Loading Opportunities**: [Deferred computation]

#### Memory Management

- **Memory Footprint**: [Current vs. optimized]
- **Garbage Collection Impact**: [Allocation patterns]
- **Memory Leaks**: [Event listeners, closures]
- **Object Pooling**: [Reusable object strategies]

### 🛡️ Security Hardening Plan

#### Input Validation & Sanitization

- **Injection Vulnerabilities**: [SQL, NoSQL, Command]
- **Cross-Site Scripting (XSS)**: [Stored, reflected, DOM-based]
- **Authentication Weaknesses**: [Password policies, MFA]
- **Authorization Flaws**: [RBAC, ABAC implementation]

#### Secure Coding Practices

- **Error Handling**: [Information disclosure prevention]
- **Logging Security**: [Sensitive data in logs]
- **Cryptography**: [Encryption at rest and in transit]
- **Dependency Vulnerabilities**: [Outdated packages]

## 📋 Immediate Action Plan

### 🚀 Implementation Tasks (Prioritized)

1. Remediate critical security vulnerabilities
2. Resolve highest-impact performance bottlenecks
3. Isolate and refactor violation clusters (SRP / boundary breaches)
4. Introduce/expand test coverage for critical paths & risky refactors
5. Add structured logging, metrics, and basic tracing at key seams
6. Capture architectural decisions (ADR) & update high-level diagrams

### 📊 Execution Strategy

- **Parallel Streams**: Security remediation & performance profiling may proceed concurrently
- **Ordering**: Stabilize (security + correctness) → optimize → restructure
- **Testing**: Add / adjust tests before deeper structural changes
- **Documentation**: Record boundary shifts and new contracts as they land
- **Risk Control**: Use feature flags / incremental merges for larger refactors

## 🎖️ Success Indicators

### Baseline (Capture Before Changes)

- **Cyclomatic Complexity (avg / hotspots)**: [Value]
- **Code Duplication (approx)**: [%]
- **Key Smell Instances**: [Counts by type]
- **Bug Density (if available)**: [Value]
- **Incident MTTR (if applicable)**: [Value]

### Target Improvement Goals

- **Security**: No known critical vulnerabilities
- **Performance**: [Target latency / throughput thresholds]
- **Complexity**: Reduce hotspot functions below agreed threshold
- **Duplication**: Lower structural duplication below target %
- **Smells**: Eliminate critical & major categories
- **Test Coverage**: Cover critical logic paths & previously untested branches
- **Documentation**: Current high-level architecture & module contracts updated

### Expected Benefits

- **Security**: Reduced exposure surface & clearer trust boundaries
- **Performance**: Lower latency / reduced resource usage
- **Maintainability**: Lower cognitive load & clearer ownership zones
- **Stability**: Fewer crash / failure vectors in critical paths
- **Confidence**: Tests + ADRs support safe iteration

## ⚠️ Risk Assessment & Mitigation

### Breaking Change Analysis

- **API Changes**: [Backward compatibility impact]
- **Database Schema**: [Migration requirements]
- **Third-party Dependencies**: [Version compatibility]
- **Performance Regression**: [Monitoring strategy]

### Rollback Strategy

- **Feature Flags**: [Gradual rollout capability]
- **Database Migrations**: [Reversible changes]
- **Deployment Pipeline**: [Blue-green deployment]
- **Monitoring**: [Real-time health checks]

### Team Readiness

- **Skill Gap Analysis**: [Training requirements]
- **Code Review Process**: [Quality gates]
- **Documentation Updates**: [Knowledge transfer]
- **Pair Programming**: [Knowledge sharing sessions]

**Analysis Scope & Context Intelligence:**

- **Micro-Analysis**: Current selection or function under cursor
- **File-Level Analysis**: Complete file with all dependencies
- **Module-Level Analysis**: Related files and their interactions
- **System-Level Analysis**: Architecture patterns across entire codebase
- **Cross-Cutting Concerns**: Security, performance, and maintainability across all layers

**Advanced Context Awareness:**

- **Framework Detection**: [React/Angular/Vue, Spring/Django/Express]
- **Architecture Pattern**: [MVC, MVP, MVVM, Clean Architecture, Microservices]
- **Database Integration**: [ORM patterns, query optimization, connection pooling]
- **API Design**: [REST, GraphQL, gRPC compliance and best practices]
- **Build Tools**: [Webpack, Vite, Maven, Gradle configuration impact]
- **CI/CD Pipeline**: [Integration with automated testing and deployment]

**Smart Configuration & Adaptation:**

- **Language Version**: [Auto-detect and recommend latest stable features]
- **Framework Version**: [Compatibility analysis and upgrade recommendations]
- **Performance Profile**: [Web app/Mobile/Real-time system considerations]
- **Team Size**: [Code organization for small vs large teams]
- **Deployment Environment**: [Cloud-native vs on-premise optimizations]
- **Compliance Requirements**: [GDPR, HIPAA, SOX, PCI-DSS impact on code structure]

**Industry-Specific Adaptations:**

- **Fintech**: [PCI compliance, transaction integrity, audit trails]
- **Healthcare**: [HIPAA compliance, data privacy, security protocols]
- **E-commerce**: [Performance optimization, scalability patterns]
- **Gaming**: [Real-time performance, memory optimization]
- **IoT/Embedded**: [Resource constraints, power efficiency]

**Modern Development Practices Integration:**

- **DevOps Alignment**: [Infrastructure as code compatibility]
- **Observability**: [Logging, monitoring, tracing integration points]
- **Security DevOps**: [SAST/DAST integration, vulnerability scanning]
- **Documentation as Code**: [API docs, architecture diagrams generation]
- **Feature Flags**: [Progressive deployment and A/B testing support]

**Interactive Follow-up:**
After generating the report, ask: "Which area would you like to tackle first: security remediation, performance optimization, architectural restructuring, or test coverage expansion?"
