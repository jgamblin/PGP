# Modern Python Patterns — 2026 Development Guide

> **Purpose**: Cover Python 3.11+ features, modern patterns, and AI integration  
> **Best For**: Copilot, ChatGPT, Claude, Agents  
> **Python Version**: 3.11+ (3.12+ for latest features)  
> **Last Updated**: 2025-12-09

---

## Quick Context Checklist

```
☐ Python version (3.11+ required, 3.12+ recommended)
☐ Code to modernize or review
☐ Target patterns (async, pattern matching, type safety)
```

---

## Guard Clauses

**If no code provided:**
```
NO_ACTIONABLE_INPUT

Please provide Python code to analyze for modernization opportunities.
Include the current Python version target if known.
```

**If code is already modern:**
```
ALREADY_MODERN

✅ Code already uses modern Python patterns.
- Pattern matching: ✓
- Type hints: ✓
- Modern syntax: ✓

No modernization needed.
```

---

## Structural Pattern Matching (Python 3.10+)

### Basic Match Statement

```python
# Before: Nested if-elif chains
def handle_response(response):
    if response["status"] == "success":
        return response["data"]
    elif response["status"] == "error":
        return f"Error: {response['message']}"
    elif response["status"] == "pending":
        return "Processing..."
    else:
        return "Unknown status"

# After: Pattern matching
def handle_response(response: dict) -> str:
    match response:
        case {"status": "success", "data": data}:
            return data
        case {"status": "error", "message": msg}:
            return f"Error: {msg}"
        case {"status": "pending"}:
            return "Processing..."
        case _:
            return "Unknown status"
```

### Class Pattern Matching

```python
from dataclasses import dataclass
from typing import Literal

@dataclass
class Point:
    x: float
    y: float

@dataclass
class Circle:
    center: Point
    radius: float

@dataclass  
class Rectangle:
    top_left: Point
    width: float
    height: float

type Shape = Point | Circle | Rectangle

def describe_shape(shape: Shape) -> str:
    match shape:
        case Point(x=0, y=0):
            return "Origin"
        case Point(x=x, y=y):
            return f"Point at ({x}, {y})"
        case Circle(center=Point(x=0, y=0), radius=r):
            return f"Circle at origin with radius {r}"
        case Circle(center=c, radius=r):
            return f"Circle at {c} with radius {r}"
        case Rectangle(width=w, height=h) if w == h:
            return f"Square with side {w}"
        case Rectangle(width=w, height=h):
            return f"Rectangle {w}x{h}"
```

### Sequence Pattern Matching

```python
def process_command(args: list[str]) -> str:
    match args:
        case []:
            return "No command provided"
        case ["help"]:
            return "Available commands: help, version, run"
        case ["version"]:
            return "v1.0.0"
        case ["run", filename]:
            return f"Running {filename}"
        case ["run", filename, *flags]:
            return f"Running {filename} with flags: {flags}"
        case [cmd, *_]:
            return f"Unknown command: {cmd}"
```

---

## Exception Groups (Python 3.11+)

### Basic Exception Groups

```python
# Raising multiple exceptions together
def validate_user(data: dict) -> None:
    errors = []
    
    if not data.get("email"):
        errors.append(ValueError("Email is required"))
    if not data.get("password"):
        errors.append(ValueError("Password is required"))
    if len(data.get("password", "")) < 8:
        errors.append(ValueError("Password must be at least 8 characters"))
    
    if errors:
        raise ExceptionGroup("Validation failed", errors)

# Handling exception groups with except*
try:
    validate_user({"email": "", "password": "short"})
except* ValueError as eg:
    for error in eg.exceptions:
        print(f"Validation error: {error}")
```

### Concurrent Error Handling

```python
import asyncio

async def fetch_all(urls: list[str]) -> list[str]:
    """Fetch all URLs, collecting all errors."""
    async def fetch_one(url: str) -> str:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status != 200:
                    raise ConnectionError(f"Failed to fetch {url}: {response.status}")
                return await response.text()
    
    results = []
    errors = []
    
    async with asyncio.TaskGroup() as tg:
        tasks = [tg.create_task(fetch_one(url)) for url in urls]
    
    # TaskGroup raises ExceptionGroup if any task fails
    return [task.result() for task in tasks]

# Usage with except*
async def main():
    try:
        results = await fetch_all(["http://example.com", "http://invalid.url"])
    except* ConnectionError as eg:
        print(f"Some requests failed: {len(eg.exceptions)} errors")
        for error in eg.exceptions:
            print(f"  - {error}")
    except* Exception as eg:
        print(f"Unexpected errors: {eg.exceptions}")
```

---

## TaskGroup (Python 3.11+)

### Basic TaskGroup Usage

```python
import asyncio

async def process_items(items: list[str]) -> list[str]:
    """Process items concurrently with proper error handling."""
    
    async def process_one(item: str) -> str:
        await asyncio.sleep(0.1)  # Simulate work
        return f"processed: {item}"
    
    results = []
    
    async with asyncio.TaskGroup() as tg:
        tasks = [tg.create_task(process_one(item)) for item in items]
    
    # All tasks completed successfully (or ExceptionGroup raised)
    return [task.result() for task in tasks]
```

### TaskGroup with Timeout

```python
async def fetch_with_timeout(urls: list[str], timeout: float = 5.0) -> list[str]:
    """Fetch URLs with overall timeout."""
    
    async def fetch_one(url: str) -> str:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                return await response.text()
    
    try:
        async with asyncio.timeout(timeout):
            async with asyncio.TaskGroup() as tg:
                tasks = [tg.create_task(fetch_one(url)) for url in urls]
            return [task.result() for task in tasks]
    except TimeoutError:
        raise TimeoutError(f"Fetching {len(urls)} URLs exceeded {timeout}s timeout")
```

---

## Type Parameter Syntax (Python 3.12+)

### New Generic Syntax

```python
# Before (Python 3.11 and earlier)
from typing import TypeVar, Generic

T = TypeVar("T")
K = TypeVar("K")
V = TypeVar("V")

class Stack(Generic[T]):
    def __init__(self) -> None:
        self._items: list[T] = []
    
    def push(self, item: T) -> None:
        self._items.append(item)
    
    def pop(self) -> T:
        return self._items.pop()

# After (Python 3.12+)
class Stack[T]:
    def __init__(self) -> None:
        self._items: list[T] = []
    
    def push(self, item: T) -> None:
        self._items.append(item)
    
    def pop(self) -> T:
        return self._items.pop()
```

### Generic Functions

```python
# Before
from typing import TypeVar

T = TypeVar("T")

def first(items: list[T]) -> T | None:
    return items[0] if items else None

# After (Python 3.12+)
def first[T](items: list[T]) -> T | None:
    return items[0] if items else None
```

### Bounded Type Parameters

```python
from typing import Protocol

class Comparable(Protocol):
    def __lt__(self, other: Self) -> bool: ...

# Python 3.12+ syntax
def max_item[T: Comparable](items: list[T]) -> T:
    return max(items)

# With constraints
def process[T: (str, bytes)](data: T) -> T:
    return data.strip()
```

---

## Type Aliases (Python 3.12+)

```python
# Before
from typing import TypeAlias, Union

UserId: TypeAlias = int
JsonValue: TypeAlias = Union[str, int, float, bool, None, list["JsonValue"], dict[str, "JsonValue"]]

# After (Python 3.12+)
type UserId = int
type JsonValue = str | int | float | bool | None | list[JsonValue] | dict[str, JsonValue]

# Generic type aliases
type ListOrSet[T] = list[T] | set[T]
type Mapper[K, V] = dict[K, V] | Callable[[K], V]
```

---

## PEP 723: Inline Script Metadata

For single-file scripts with dependencies:

```python
# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "requests>=2.31.0",
#   "rich>=13.0.0",
# ]
# ///

"""
Single-file script with embedded dependencies.
Run with: uv run script.py
"""

import requests
from rich import print

def main():
    response = requests.get("https://api.github.com")
    print(f"[green]GitHub API Status: {response.status_code}[/green]")

if __name__ == "__main__":
    main()
```

Run with:
```bash
# uv automatically reads inline metadata and installs deps
uv run script.py

# Or with pipx
pipx run script.py
```

---

## Result Type Pattern

Explicit error handling without exceptions:

```python
from __future__ import annotations
from dataclasses import dataclass
from typing import Generic, TypeVar, Callable

T = TypeVar("T")
E = TypeVar("E")

@dataclass(frozen=True, slots=True)
class Ok(Generic[T]):
    value: T
    
    def is_ok(self) -> bool:
        return True
    
    def is_err(self) -> bool:
        return False
    
    def unwrap(self) -> T:
        return self.value
    
    def unwrap_or(self, default: T) -> T:
        return self.value
    
    def map[U](self, fn: Callable[[T], U]) -> Result[U, E]:
        return Ok(fn(self.value))

@dataclass(frozen=True, slots=True)
class Err(Generic[E]):
    error: E
    
    def is_ok(self) -> bool:
        return False
    
    def is_err(self) -> bool:
        return True
    
    def unwrap(self) -> T:
        raise ValueError(f"Called unwrap on Err: {self.error}")
    
    def unwrap_or(self, default: T) -> T:
        return default
    
    def map[U](self, fn: Callable[[T], U]) -> Result[U, E]:
        return self  # type: ignore

type Result[T, E] = Ok[T] | Err[E]

# Usage
def parse_int(s: str) -> Result[int, str]:
    try:
        return Ok(int(s))
    except ValueError:
        return Err(f"Cannot parse '{s}' as integer")

def divide(a: int, b: int) -> Result[float, str]:
    if b == 0:
        return Err("Division by zero")
    return Ok(a / b)

# Chaining
result = parse_int("42").map(lambda x: x * 2)
match result:
    case Ok(value):
        print(f"Success: {value}")
    case Err(error):
        print(f"Error: {error}")
```

---

## Structured Logging

Modern logging with context:

```python
import logging
import json
from datetime import datetime, UTC
from typing import Any

class StructuredFormatter(logging.Formatter):
    """JSON formatter for structured logging."""
    
    def format(self, record: logging.LogRecord) -> str:
        log_data = {
            "timestamp": datetime.now(UTC).isoformat(),
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage(),
        }
        
        # Add extra fields
        if hasattr(record, "extra"):
            log_data.update(record.extra)
        
        # Add exception info
        if record.exc_info:
            log_data["exception"] = self.formatException(record.exc_info)
        
        return json.dumps(log_data)

def get_logger(name: str) -> logging.Logger:
    """Get a configured structured logger."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    
    handler = logging.StreamHandler()
    handler.setFormatter(StructuredFormatter())
    logger.addHandler(handler)
    
    return logger

# Usage
logger = get_logger(__name__)

def process_request(request_id: str, user_id: int) -> None:
    logger.info(
        "Processing request",
        extra={"request_id": request_id, "user_id": user_id}
    )
```

---

## AI/LLM Integration Patterns

### Structured Output with Pydantic

```python
from pydantic import BaseModel, Field
from openai import OpenAI

class CodeReviewFinding(BaseModel):
    """Structured finding from AI code review."""
    severity: str = Field(description="critical, high, medium, or low")
    file: str = Field(description="File path")
    line_start: int = Field(description="Starting line number")
    line_end: int = Field(description="Ending line number")
    issue: str = Field(description="Description of the issue")
    suggestion: str = Field(description="How to fix it")

class CodeReviewResult(BaseModel):
    """Complete code review result."""
    findings: list[CodeReviewFinding]
    summary: str
    approved: bool

def ai_code_review(code: str) -> CodeReviewResult:
    """Get structured code review from AI."""
    client = OpenAI()
    
    completion = client.beta.chat.completions.parse(
        model="gpt-4o-2024-08-06",
        messages=[
            {"role": "system", "content": "You are a senior Python code reviewer."},
            {"role": "user", "content": f"Review this code:\n\n{code}"}
        ],
        response_format=CodeReviewResult,
    )
    
    return completion.choices[0].message.parsed
```

### Instructor Library Pattern

```python
import instructor
from pydantic import BaseModel
from openai import OpenAI

class ExtractedData(BaseModel):
    name: str
    age: int
    occupation: str

# Patch OpenAI client with instructor
client = instructor.from_openai(OpenAI())

def extract_person_data(text: str) -> ExtractedData:
    """Extract structured data from text."""
    return client.chat.completions.create(
        model="gpt-4o-mini",
        response_model=ExtractedData,
        messages=[
            {"role": "user", "content": f"Extract person data from: {text}"}
        ]
    )
```

### MCP (Model Context Protocol) Tool

```python
from mcp.server import Server
from mcp.types import Tool, TextContent

server = Server("python-tools")

@server.tool()
async def analyze_python(code: str) -> list[TextContent]:
    """Analyze Python code for issues.
    
    Args:
        code: Python source code to analyze
    """
    # Run ruff on the code
    import subprocess
    import tempfile
    
    with tempfile.NamedTemporaryFile(suffix=".py", delete=False) as f:
        f.write(code.encode())
        f.flush()
        
        result = subprocess.run(
            ["ruff", "check", f.name, "--output-format=json"],
            capture_output=True,
            text=True
        )
    
    return [TextContent(type="text", text=result.stdout or "No issues found")]

if __name__ == "__main__":
    import asyncio
    asyncio.run(server.run())
```

---

## Copy-Paste Prompts

### Prompt: Modernize Python Code
```text
Modernize this Python code to use 3.12+ features:

{{CODE}}

Apply these patterns where appropriate:
1. Structural pattern matching (match/case)
2. New type parameter syntax (def func[T]())
3. Type aliases (type X = ...)
4. Exception groups (except*)
5. TaskGroup for async concurrency
6. f-string improvements

Output:
- Modernized code with comments explaining changes
- List of patterns applied
- Any compatibility notes for older Python versions
```

### Prompt: Add Result Type Error Handling
```text
Refactor this code to use Result type pattern instead of exceptions:

{{CODE}}

Requirements:
1. Create appropriate Ok/Err types
2. Replace try/except with Result returns
3. Use pattern matching for Result handling
4. Preserve all error information
5. Add type hints throughout

Output the refactored code with inline comments.
```

### Prompt: Convert to Async with TaskGroup
```text
Convert this synchronous code to async using TaskGroup:

{{CODE}}

Requirements:
1. Use asyncio.TaskGroup for concurrent operations
2. Handle errors with ExceptionGroup
3. Add proper timeout handling
4. Include type hints
5. Follow modern async patterns

Output the async version with comments explaining the conversion.
```

### Prompt: Add Structured Logging
```text
Add structured logging to this code:

{{CODE}}

Requirements:
1. Use JSON-formatted log output
2. Add contextual fields (request_id, user_id, etc.)
3. Use appropriate log levels
4. Include timing for slow operations
5. Don't log sensitive data (passwords, tokens)

Output the code with logging added and explanation of log points.
```

### Prompt: Create Pydantic Models for AI Output
```text
Create Pydantic models to structure AI responses for this use case:

{{USE_CASE_DESCRIPTION}}

Requirements:
1. Use Pydantic v2 syntax
2. Add Field descriptions for AI guidance
3. Include validation where appropriate
4. Make models composable/nestable
5. Add example values

Output:
- Pydantic model definitions
- Example usage with OpenAI/Instructor
- Sample expected output
```

---

## Output Format

### Modernization Report
```markdown
# Python Modernization Report

## Summary
- **Current Python target**: 3.X
- **Recommended target**: 3.12+
- **Patterns applicable**: X of Y

## Changes Applied

### Pattern: [Name]
- **Location**: `file.py:lines`
- **Before**: [Old pattern]
- **After**: [New pattern]
- **Benefit**: [Why it's better]

## Compatibility Notes
- [Any breaking changes or version requirements]
```

### JSON Output (For Agents)
```json
{
  "analysis_type": "modernization",
  "python_version_current": "3.9",
  "python_version_recommended": "3.12",
  "patterns_found": [
    {
      "pattern": "match_statement",
      "file": "handlers.py",
      "line_start": 45,
      "line_end": 67,
      "current_code": "if-elif chain",
      "suggested_code": "match/case"
    }
  ],
  "total_improvements": 5,
  "breaking_changes": false
}
```

---

*For shared boilerplate and tool configuration, see [Common Sections](./_common-sections.md)*
