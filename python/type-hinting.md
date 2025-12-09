# Python Type Hints Helper

> **Purpose**: Add practical type hints for safety and clarity  
> **Best For**: Copilot, ChatGPT, Claude, Agents  
> **Python Version**: 3.11+ (3.12+ for latest syntax)  
> **Last Updated**: 2025-12-09

---

## Mission

Help add **useful type hints** using modern Python 3.11+ syntax, Pydantic v2 for validation, and TypedDict for structured data. Focus on types that catch bugs and improve IDE support.

---

## Guard Clauses

**If no code provided:**
```
NO_ACTIONABLE_INPUT

Please provide Python code to add type hints to:
- Functions/methods
- Classes
- Data structures
```

**If code is already fully typed:**
```
ALREADY_TYPED

✅ Code is already fully typed.
- Function signatures: ✓
- Return types: ✓
- Class attributes: ✓

Consider running `mypy --strict` to verify type safety.
```

---

## Quick Context Checklist

```
☐ Code to type
☐ Python version (affects syntax)
☐ Strictness level (basic, moderate, strict)
☐ Framework constraints (Django, Pydantic, etc.)
```

> 📝 **Standard Context**: See [_common-sections.md](_common-sections.md) for full input checklist and severity levels.

---

## Copy-Paste Type Hinting Prompts

### Prompt: Add Type Hints
```text
Add comprehensive type hints to this code:

{{CODE}}

Use Python 3.11+ syntax:
- Built-in generics (list[str], dict[str, int])
- Union with | operator (str | None)
- Self for methods returning self
- TypedDict for dictionaries with known keys
- Literal for specific values

Make it pass mypy --strict.
```

### Prompt: Type a Class
```text
Add type hints to this class:

{{CODE}}

Include:
- __init__ parameters and return None
- All method signatures
- Class and instance attributes
- Property return types
- Generic type parameters if applicable

Use dataclass or Pydantic if appropriate.
```

### Prompt: Fix Type Errors
```text
Fix these mypy errors in this code:

Errors:
{{ERRORS}}

Code:
{{CODE}}

For each error:
1. Explain the issue
2. Show the fix
3. Note if it reveals a real bug

Provide the corrected code.
```

### Prompt: Type Stub Generation
```text
Generate type stubs (.pyi) for this module:

{{CODE}}

Create a .pyi file with:
- All public function signatures
- Class definitions with attributes
- Protocol definitions if needed
- Overloads for polymorphic functions

Follow typeshed conventions.
```

### Prompt: Add Protocols
```text
Define Protocol types for these duck-typed usages:

{{CODE}}

Create Protocol classes for:
- Structural typing (methods/attributes used)
- Runtime checkable where appropriate
- Generic protocols if needed

Replace Any with proper Protocols.
```

---

## Practical Type Hints Approach

### 1. **Bug Prevention**

- **None Handling**: Use `str | None` to show when values might be None
- **Basic Types**: Catch simple type errors like passing strings to math functions
- **Function Contracts**: Show what functions expect and return
- **Data Validation**: Use types to document expected data structures

### 2. **Better Development Experience**

- **IDE Help**: Get better autocomplete and error detection
- **Code Understanding**: Types help explain what code does
- **Refactoring Safety**: Catch issues when changing code
- **Self-Documentation**: Types serve as inline documentation

### 3. **Practical Benefits**

- **Catch Bugs Early**: Find issues before running code
- **Easier Maintenance**: Understand code when you come back to it
- **Team Collaboration**: Others can understand your code better
- **Gradual Adoption**: Add types incrementally where they help most

## Type Hints Guidelines

**Avoid:**

- Using `Any` everywhere (defeats the purpose of type hints)
- Making type annotations more complex than the actual code
- Adding types to every single variable (focus on function signatures)
- Ignoring type checker warnings without good reason
- Creating overly complex generic types for simple use cases
- Adding types that don't match what the code actually does

## Python Type Hints Report

Generate a **Practical Type Hints Analysis** and save it as a markdown file named `python-type-hints-analysis-[YYYY-MM-DD].md`:


## Report Format

Generate a comprehensive analysis and save as **two deliverables**:

### 1. Summary Report: `type-hinting-[YYYY-MM-DD].md`

```markdown
# Type Hinting

## Overview
- **Scope**: [What was analyzed]
- **Files Analyzed**: [Count]
- **Critical Issues**: [Count]
- **High Priority Items**: [Count]
- **Recommended Priority**: [Summary]

## Summary
[Brief overview of findings and recommended approach]

## Findings Summary
- Security: [Summary with count]
- Performance: [Summary with count]
- Code Quality: [Summary with count]
- Quality & Testing: [Summary with count]

## Prioritized Action Items
1. [Critical item with link to finding file]
2. [High priority item with link to finding file]
3. [Medium priority item with link to finding file]
...

## Success Metrics
- Security: Zero critical vulnerabilities
- Quality: Linting passes, complexity reduced
- Performance: Response times within targets
- Testing: 80%+ coverage for critical paths
```

### 2. Per-Finding Details: `type-hinting-[YYYY-MM-DD]/`

Create a folder with individual markdown files for each finding:
- `finding-001-security-vulnerability.md`
- `finding-002-performance-issue.md`
- `finding-003-code-quality-concern.md`

Each finding file should contain:
- **Issue description** with friendly, clear explanation
- **Location** (file:line references)
- **Current state** (the problematic code/configuration)
- **Recommended solution** (improved code/configuration with inline comments)
- **Why this helps** (benefits and rationale)
- **Implementation steps** (step-by-step guidance)
- **Testing recommendations** (how to verify the fix works)


```markdown
# Python Type Hints Analysis Report

## Type Hints Status
- **Current Coverage**: [X% of functions have type hints]
- **Bug Prevention**: [Types catching X common errors]
- **Code Clarity**: [How much clearer the code is with types]
- **IDE Support**: [Better autocomplete and error detection]
- **Maintenance**: [Easier to understand and modify code]
- **Team Help**: [Others can understand your code better]

## Function Analysis

### Function: `function_name(param1, param2)`
- **Location**: `filename.py:line X`
- **Importance**: [Critical/Important/Nice to have]
- **Current Types**: [X% of parameters typed, return type present/missing]
- **Risk Level**: [High/Medium/Low - likelihood of type-related bugs]
- **Complexity**: [Simple/Complex - how hard it is to add types]
- **Usage**: [How often this function is called] interface classification]

**Advanced Parameter Type Intelligence:**
- `param1`: [Current: Any → Target: CustomerData, Domain context: User identification, Validation: UUID format, Security: PII handling]
- `param2`: [Current: None → Target: Optional[datetime], Performance: Cached computation, Error handling: Timezone-aware defaults]
- `*args`: [Missing → Target: *args: Unpack[Tuple[str, ...]], Usage pattern: Variable message components]
- `**kwargs`: [Missing → Target: **kwargs: TypedDict specifications, API evolution: Backward compatibility]

**Return Type Domain Logic Analysis:**
- **Current State**: [Untyped → 45% of returns cause downstream type errors]
- **Domain Semantics**: [ProcessedResult with success/failure indicators and error context]
- **Error Modeling**: [Result[T, E] pattern for explicit error handling]
- **Performance Characteristics**: [Lazy evaluation types, memory usage optimization]

## Production-Grade Type Safety Implementation

### For `function_name()` - Production-Ready Type Safety:
```python
from __future__ import annotations

from typing import (
 TYPE_CHECKING, TypeVar, Generic, Protocol, 
 Literal, NewType, Final, ClassVar, overload
)
from typing_extensions import TypedDict, NotRequired
from datetime import datetime
from decimal import Decimal
from uuid import UUID

if TYPE_CHECKING:
 from mypy_extensions import TypedDict

# Domain-specific type definitions
CustomerID = NewType('CustomerID', UUID)
ProcessingResult = TypeVar('ProcessingResult', bound='BaseProcessingResult')

class CustomerData(TypedDict):
 """Type-safe customer data structure with domain validation."""
 customer_id: CustomerID
 email: str # Validated email format
 consent_data: ConsentFlags
 processing_timestamp: NotRequired[datetime] # Optional for backward compatibility

class ConsentFlags(TypedDict, total=False):
 """GDPR compliance consent tracking."""
 marketing: bool
 analytics: bool
 data_processing: bool

class ProcessingError(Protocol):
 """Error interface for type-safe error handling."""
 code: str
 message: str
 recovery_suggestions: list[str]

def function_name(
 customer_data: CustomerData,
 processing_time: datetime | None = None,
 *, # Force keyword-only arguments for API evolution
 validation_level: Literal['basic', 'strict', 'extended'] = 'basic',
 **config: Unpack[ProcessingConfig]
) -> Result[ProcessedCustomer, ProcessingError]:
 """Process customer data with comprehensive type safety.

 Type Safety Features:
 - Prevents None dereference through Optional handling
 - Validates domain constraints through NewType
 - Ensures API contract compliance through Protocol
 - Enables safe refactoring through precise return types
 """
 # Implementation with comprehensive type checking
 if not isinstance(customer_data.get('customer_id'), UUID):
 return Err(ValidationError(
 code='invalid_customer_id',
 message='Customer ID must be valid UUID',
 recovery_suggestions=['Check UUID format', 'Validate input source']
 ))

 # Type-safe processing logic
 processed: ProcessedCustomer = ProcessedCustomer(
 customer_id=customer_data['customer_id'],
 processing_timestamp=processing_time or datetime.now(UTC),
 validation_passed=True
 )

 return Ok(processed)
```

## Type Safety Implementation Roadmap

### Phase 1: Start with the Basics (Week 1)

1. **Key Functions First**
 - **Target**: Add types to your most important functions
 - **Focus**: Main business logic, API endpoints, data processing
 - **Success**: Catch obvious type errors before running code
 - **Tool**: Basic mypy checking

2. **Data Structures**
 - **Target**: Type your main data classes and dictionaries
 - **Focus**: User data, API responses, configuration objects
 - **Success**: Clear documentation of data shapes
 - **Tool**: dataclasses with type hints

### Phase 2: Developer Experience Enhancement (Week 3-4, 20-28 hours)

1. **IDE Intelligence Optimization**
 - **Team Velocity**: 40% faster development through enhanced autocomplete
 - **Implementation**: Rich generic types, TypedDict, and Protocol usage
 - **Refactoring Safety**: Large-scale changes with static analysis confidence

2. **Domain-Specific Type Systems**
 - **Technical Value**: Prevent invalid domain state transitions
 - **Implementation**: NewType, Literal types, and domain validation
 - **Quality Improvement**: Self-documenting domain logic through types

### Phase 3: Advanced Types (Week 4-5)

5. **Generic Patterns**
 - **Target**: Add types to reusable components
 - **Focus**: Utility functions, common patterns, shared code
 - **Success**: Reusable code with clear type contracts
 - **Tool**: Basic generics like List[T], Dict[str, T]

6. **Async Functions**
 - **Target**: Type your async/await code
 - **Focus**: Async functions, coroutines, async generators
 - **Success**: Clear async function signatures
 - **Tool**: Awaitable, Coroutine type hints

## Type Safety Success Metrics

- **Runtime Error Reduction**: 85% decrease in type-related production incidents
- **Development Velocity**: 40% faster feature development through type intelligence
- **Code Quality**: 60% improvement in maintainability index
- **Refactoring Confidence**: 95% successful large-scale code changes
- **API Reliability**: 99.9% uptime through comprehensive interface validation
- **Team Onboarding**: 65% faster new developer productivity

## Action Plan

1. [ ] **High Priority**: Add return type annotations to public functions
2. [ ] **Medium Priority**: Annotate function parameters
3. [ ] **Low Priority**: Add type hints to private methods
4. [ ] **Cleanup**: Update imports and use modern syntax

## mypy Configuration

```ini
# Recommended mypy.ini settings
[mypy]
python_version = 3.9
warn_return_any = True
warn_unused_configs = True
disallow_untyped_defs = True
```

## Type Coverage Metrics

- **Annotated Functions**: [X%]
- **mypy Score**: [Pass/Fail with error count]

- **Estimated Effort**: [Hours to complete]

```text

**Type Annotation Scope:**
- **Current Selection**: Add type hints to the currently selected function/class
- **Current File**: Analyze and annotate all functions/methods in the active file
- **Cursor Context**: Focus on the function/method containing the cursor
- **Import Dependencies**: Include necessary typing imports at the file top

**IDE Integration:**
- Auto-detect Python version from project settings (pyproject.toml, setup.py)
- Use existing import statements to infer available types
- Analyze function usage patterns across the workspace to determine precise types
- Reference related files to understand custom type definitions and protocols
- Maintain consistency with existing type annotation patterns in the codebase

**Smart Type Analysis:**
- Python version: [Auto-detect from project configuration or IDE settings]
- Type syntax: [Use modern syntax (3.10+) if supported, fallback to older syntax]
- Runtime checking: [Include if TYPE_CHECKING imports are already present]
- Mypy compliance: [Add configuration based on existing mypy.ini or pyproject.toml]

```

## Advanced Python Type Intelligence Engine

**Type Analysis:**

- **Domain Modeling**: Finance/healthcare/e-commerce specific type patterns
- **Performance-Critical Path Analysis**: High-throughput service type optimization
- **API Surface Type Design**: External interface contract validation
- **Framework Integration**: Django/Flask/FastAPI specific type patterns
- **Database Integration**: SQLAlchemy/Django ORM type safety patterns
- **Async Pattern Analysis**: Comprehensive async/await type safety

**Smart Type System Configuration:**

- **Python Version Optimization**: Leverage latest typing features while maintaining compatibility
- **mypy Configuration**: Strict mode enablement with context-appropriate exceptions
- **IDE Integration**: PyCharm/VSCode optimal type intelligence configuration
- **CI/CD Integration**: Automated type checking with performance benchmarking
- **Team Skill Assessment**: Type system complexity calibrated to team expertise
- **Migration Strategy**: Gradual type adoption without disrupting development velocity

## Interactive Excellence Protocol

**Upon analysis completion:**
"I've identified [X] critical type safety gaps that could prevent production incidents and improve developer velocity by [Z]%. The highest-impact improvement is [specific function] which handles [critical process] and currently lacks type safety for [X] daily operations. Implementing comprehensive type annotations here will prevent [Y]% of runtime errors and enable measurable reliability gains. Shall I provide the exact type implementation that will transform this function into a type-safe, self-documenting API?"

## Type Safety Excellence Validation

**Type Safety Quality Checklist:**

- Runtime error prevention through comprehensive null safety
- Domain constraints enforced through type system
- API contracts validated through Protocol and TypedDict usage
- Performance implications analyzed and optimized
- IDE intelligence maximized through rich type annotations
- Refactoring safety enabled through precise type definitions
- Team velocity enhanced through self-documenting type contracts
- Error reduction impact quantified through metrics

**Quality Guidelines:**

- **Zero Runtime Type Errors**: 100% elimination of TypeError/AttributeError in typed code
- **Complete API Contracts**: All public interfaces fully typed with Protocol validation
- **Domain Accuracy**: Types accurately represent domain constraints and workflows
- **Performance Optimization**: Type system enhances rather than hinders system performance




## Tooling & Automation

Recommended tools and commands for Python development:

### Analysis & Quality Tools
```bash
# Python code quality
ruff check .
black --check .
mypy .

# Testing
pytest --cov=. --cov-report=term-missing

# Security
bandit -r .
pip-audit
```

### Git Analysis
```bash
# Review changes
git diff main...HEAD --stat
git log --oneline -10

# Identify changed files
git diff main...HEAD --name-only
```

### CI/CD Integration
Recommend adding these to your development workflow:
```bash
# Pre-commit hooks
pre-commit run ruff --all-files
pre-commit run black --all-files
pre-commit run mypy --all-files
```

### Pre-commit Hooks (Recommended)
```bash
# Install pre-commit framework
pip install pre-commit  # or brew install pre-commit

# Set up hooks
pre-commit install
pre-commit run --all-files
```


## Metrics & Validation

Define clear success criteria for outcomes:

### Quality Guidelines
- **Security**: Zero critical vulnerabilities, zero hardcoded secrets
- **Code Quality**: Ruff and Black passes with minimal warnings
- **Complexity**: Cyclomatic complexity <10 per function/method
- **Duplication**: No code blocks duplicated more than twice
- **Documentation**: Public APIs and complex logic documented

### Testing Thresholds
- **Critical paths**: 80% test coverage
- **All tests pass**: No failing tests without corresponding code changes
- **Test quality**: Tests verify behavior, not implementation details
- **Edge cases**: Error conditions and boundary cases tested

### Performance Benchmarks (if applicable)
- **No regressions**: Performance metrics maintained or improved
- **Response times**: Within acceptable thresholds for user-facing operations
- **Resource usage**: Memory and CPU usage within reasonable bounds
- **Scalability**: System handles expected load

### Deployment Readiness
- **Documentation**: README, API docs, and runbooks up-to-date
- **Monitoring**: Key metrics and errors are observable
- **Deployment**: Automated deployment process works reliably



## Follow-Up & Continuous Improvement

### Feedback Loop
After implementing changes:

1. **Verify improvements**
   - Run all tests to ensure nothing broke
   - Check that metrics improved (quality scores, performance)
   - Gather feedback from team members or users
   - Validate that issues are actually resolved

2. **Monitor impact**
   - Track if bugs decreased in modified areas
   - Measure if development velocity improved
   - Note if system reliability increased
   - Observe user satisfaction changes

3. **Document learnings**
   - Update team standards based on findings
   - Create architecture decision records (ADRs) for significant changes
   - Share successful patterns and approaches
   - Update documentation with new practices

### When to Get Team Input
When to discuss with your teammates:
- **Breaking changes needed**: Discuss with the team before making major changes
- **Performance degradation**: Roll back and investigate if metrics worsen significantly
- **Test coverage drops**: Pause changes to add tests first
- **Security concerns**: Pair with a teammate on authentication, authorization, or data handling code
- **Team confusion**: Provide additional documentation, pairing, or training

### Continuous Improvement
- Schedule regular reviews (weekly/monthly/quarterly based on project activity)
- Gradually increase quality standards as codebase improves
- Celebrate wins and improvements with the team
- Keep improvements incremental and sustainable
- Build a culture of quality and continuous learning

### Process Optimization
Based on findings, consider updating:
- **Coding standards**: Add patterns that prevent common issues
- **Review checklists**: Include checks for identified problem areas
- **CI/CD pipelines**: Add automated checks for recurring issues
- **Documentation templates**: Standardize important documentation
- **Team practices**: Share knowledge and establish better workflows
