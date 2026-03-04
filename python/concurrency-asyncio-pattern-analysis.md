# Python Async & Concurrency Helper

> **Purpose**: Write safe, efficient async and concurrent code  
> **Best For**: Codex, Claude, ChatGPT, Copilot, Agents  
> **Scope**: Python 3.11+ application development, tooling, and code quality  
> **Last Updated**: 2026-03
> **Python Version**: 3.11+ (TaskGroup, ExceptionGroup)  

---

## Mission

Help write **safe, efficient async code** using modern Python 3.11+ patterns like TaskGroup, ExceptionGroup, and asyncio.timeout.

---

## Guard Clauses

**If no code provided:**
```
NO_ACTIONABLE_INPUT

Please provide async/concurrent code to review:
- Async functions
- Concurrent operations
- Threading/multiprocessing code
```

**If async code is well-structured:**
```
ASYNC_CODE_CLEAN

✅ Async code looks good.
- TaskGroup usage: ✓
- Proper await: ✓
- Resource cleanup: ✓
- No blocking calls in async

Consider adding timeouts for external calls.
```

---

## Quick Context Checklist

```
☐ Async code to review
☐ Concurrency requirements
☐ External services called
☐ Performance requirements
```

> 📝 **Standard Context**: See [_common-sections.md](_common-sections.md) for full input checklist and severity levels.

---

## Copy-Paste Async Prompts

### Prompt: Review Async Code
```text
Review this async code for issues:

{{CODE}}

Check for:
1. Blocking calls in async functions (use run_in_executor)
2. Missing await keywords
3. Proper TaskGroup/gather usage
4. Resource cleanup (async context managers)
5. Exception handling in tasks
6. Timeout handling for external calls

Prioritize by severity.
```

### Prompt: Convert to Async
```text
Convert this synchronous code to async:

{{CODE}}

Use:
- async/await syntax
- aiohttp for HTTP (not requests)
- asyncpg/aiosqlite for database
- aiofiles for file I/O
- TaskGroup for concurrent operations (Python 3.11+)

Preserve functionality and error handling.
```

### Prompt: Add Concurrency
```text
Add concurrent execution to this code:

{{CODE}}

Requirements:
- Process {{ITEMS}} concurrently
- Limit to {{MAX_CONCURRENT}} simultaneous operations
- Handle errors without stopping other tasks
- Report progress

Use asyncio.Semaphore for rate limiting.
```

### Prompt: Fix Async Bug
```text
Debug this async code that's not working correctly:

{{CODE}}

Problem: {{DESCRIPTION}}

Check for common issues:
- Event loop already running
- Mixing sync/async incorrectly
- Race conditions
- Deadlocks
- Uncaught task exceptions
```

### Prompt: Add Timeout Handling
```text
Add proper timeout handling to this async code:

{{CODE}}

Implement:
- Per-operation timeouts
- Overall timeout for batch operations
- Graceful handling of TimeoutError
- Cleanup on timeout
- Retry logic (optional)

Use asyncio.timeout() (Python 3.11+).
```

---

## Practical Async Review

### 1. **Async Patterns**

- **Basic Async/Await**: Proper use of async functions and await
- **TaskGroup**: Python 3.11+ structured concurrency (preferred over gather)
- **Task Management**: Creating and managing concurrent tasks

### 2. **Safety & Reliability**

- **Resource Cleanup**: Properly closing connections and files
- **Exception Handling**: Catching and handling errors in async code
- **Deadlock Prevention**: Avoiding common async pitfalls

### 3. **Performance**

- **When to Use Async**: I/O-bound operations, not CPU-bound
- **Concurrency vs Parallelism**: Choosing the right approach
- **Common Bottlenecks**: Finding and fixing slow async operations

### 4. **Code Quality**

- **Code Clarity**: Readable async code, clear separation of concerns
- **Testing**: pytest-asyncio for async tests
- **Documentation**: Basic comments explaining async patterns

## What to Avoid

**Don't approve code with:**

- Resource leaks (unclosed connections, files)
- Unhandled exceptions in async functions
- Blocking operations in async code (use aiohttp instead of requests)
- Complex nested async patterns without clear purpose

## Async Code Review

Provide a **practical async code review** focusing on safety and performance:

# Python Async Code Review

## Quick Assessment

- **Async Pattern**: [async/await, asyncio.gather, etc.]
- **Safety Issues**: [Resource leaks, unhandled exceptions]
- **Performance**: [Bottlenecks, unnecessary blocking]
- **Code Quality**: [Readability, error handling]

## What's Working Well

- **Good Patterns**: [List effective async patterns found]
- **Proper Cleanup**: [Resources being closed correctly]
- **Error Handling**: [Good exception management]

## Issues to Fix

### Issue: [Brief description]

- **File**: `filename.py:line X`
- **Problem**: [What's wrong and why it matters]
- **Fix**: [Simple solution]
- **Example**:
```python
# Current (problematic)
[current code]

# Better approach
[improved code]
```

## Suggestions

### Quick Wins
- [Simple improvements that help immediately]
- [Better patterns to adopt]

### Performance
- [Ways to make async code faster]
- [When to use different concurrency approaches]

## Next Steps

1. [Most important fix]
2. [Second priority]
3. [Nice to have improvements]

## Checklist

- [ ] No resource leaks (connections, files closed)
- [ ] Proper error handling in async functions
- [ ] No blocking operations in async code
- [ ] Clear, readable async patterns

## Common Async Patterns

### Making HTTP Requests
```python
# Good - using aiohttp
import aiohttp

async def fetch_data(url):
 async with aiohttp.ClientSession() as session:
 async with session.get(url) as response:
 return await response.json()

# Avoid - blocking requests in async function
import requests # Don't do this in async code

async def bad_fetch(url):
 return requests.get(url).json() # Blocks the event loop!
```

### Running Multiple Tasks
```python
# Good - concurrent execution
import asyncio

async def process_urls(urls):
 tasks = [fetch_data(url) for url in urls]
 results = await asyncio.gather(*tasks)
 return results

# Less efficient - sequential
async def process_urls_slow(urls):
 results = []
 for url in urls:
 result = await fetch_data(url) # One at a time
 results.append(result)
 return results
```

### Proper Resource Cleanup
```python
# Good - ensures cleanup
async def read_file_async(filename):
 async with aiofiles.open(filename, 'r') as f:
 content = await f.read()
 return content # File automatically closed

# Risky - might leak resources
async def read_file_bad(filename):
 f = await aiofiles.open(filename, 'r')
 content = await f.read()
 await f.close() # What if an exception happens?
 return content
```

## Tooling & Automation

Use [_common-sections.md](_common-sections.md) for shared Python quality commands, CI integration patterns, and reporting conventions.

## Metrics & Validation

Use [_common-sections.md](_common-sections.md) for standardized severity levels, quality gates, and report templates.

## Follow-Up & Continuous Improvement

Use [_common-sections.md](_common-sections.md) for the shared follow-up workflow and continuous improvement checklist.
