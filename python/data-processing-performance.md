# Python Data Processing Performance Optimization

> **Purpose**: Maximize data processing speed with measurable benchmarks  
> **Best For**: Codex, Claude, ChatGPT, Copilot, Agents  
> **Scope**: Python 3.11+ application development, tooling, and code quality  
> **Last Updated**: 2026-03
> **Python Version**: 3.11+ (3.12+ for free-threading)  

---

## Mission

Optimize Python data processing pipelines for **maximum performance** while establishing **measurable benchmarks** to validate improvements. Every optimization must be justified with before/after metrics.

---

## Guard Clauses

**If no code provided:**
```
NO_ACTIONABLE_INPUT

Please provide data processing code to optimize:
- Python scripts or modules
- Current execution times or benchmarks
- Input data characteristics (size, format, volume)
- Performance targets or constraints
```

**If code is already optimized:**
```
NO_OPTIMIZATION_NEEDED

✅ Code is already well-optimized.
- Vectorized operations: ✓
- Memory-efficient: ✓
- I/O optimized: ✓
- Parallelized where beneficial: ✓

Current benchmarks appear optimal for the data characteristics.
Consider profiling to confirm no hidden bottlenecks.
```

---

## Quick Context Checklist

```
☐ Code to optimize
☐ Current execution time / benchmarks
☐ Data volume (rows, file sizes, memory usage)
☐ Input/output formats (CSV, Parquet, JSON, etc.)
☐ Hardware constraints (CPU cores, RAM, GPU)
☐ Acceptable tradeoffs (memory vs speed, readability vs performance)
```

> 📝 **Standard Context**: See [_common-sections.md](_common-sections.md) for full input checklist and severity levels.

---

## Copy-Paste Performance Prompts

### Prompt: Profile and Benchmark Code
```text
Profile this data processing code and establish baseline benchmarks:

{{CODE}}

Data characteristics:
- Input size: {{SIZE}}
- Format: {{FORMAT}}

Provide:
1. Line-by-line profiling (cProfile/line_profiler results)
2. Memory profiling (peak usage, allocations)
3. I/O timing breakdown
4. Bottleneck identification with percentage of total time
5. Baseline benchmark table for future comparison

Use this benchmarking template:
| Metric | Baseline | Target | Method |
|--------|----------|--------|--------|
| Execution time | X sec | ? | timeit |
| Memory peak | X MB | ? | tracemalloc |
| Throughput | X rows/sec | ? | calculated |
```

### Prompt: Vectorize with NumPy/Pandas
```text
Convert this loop-based code to vectorized operations:

{{CODE}}

Requirements:
- Replace Python loops with NumPy/Pandas vectorized operations
- Eliminate row-by-row iteration
- Use broadcasting where applicable
- Maintain numerical precision

Provide before/after benchmarks showing speedup factor.
```

### Prompt: Optimize Pandas Operations
```text
Optimize this Pandas code for large datasets:

{{CODE}}

Dataset size: {{ROWS}} rows, {{COLS}} columns

Apply:
1. Use appropriate dtypes (category, int32 vs int64, etc.)
2. Replace apply() with vectorized alternatives
3. Use query() instead of boolean indexing for complex filters
4. Optimize groupby operations (sort=False, observed=True)
5. Use inplace operations where safe
6. Consider chunked processing if memory-constrained

Show memory reduction and speedup metrics.
```

### Prompt: Parallelize Processing
```text
Add parallel processing to this data pipeline:

{{CODE}}

Environment:
- CPU cores: {{CORES}}
- Data volume: {{SIZE}}
- I/O bound or CPU bound: {{TYPE}}

Implement appropriate parallelization:
- multiprocessing.Pool for CPU-bound work
- concurrent.futures for mixed workloads  
- asyncio for I/O-bound operations
- joblib for scikit-learn compatible code
- Dask for out-of-memory datasets

Include:
- Optimal worker count determination
- Chunk size optimization
- Error handling across workers
- Progress reporting
- Benchmark comparison: serial vs parallel
```

### Prompt: Optimize File I/O
```text
Optimize file I/O in this data processing code:

{{CODE}}

Current file operations:
- Format: {{FORMAT}}
- Total size: {{SIZE}}
- Read pattern: {{PATTERN}} (full/streaming/random)

Optimize for:
1. File format (CSV → Parquet/Feather for columnar)
2. Compression (snappy, zstd, lz4)
3. Chunked reading for large files
4. Memory-mapped files where appropriate
5. Buffered I/O configuration
6. Async I/O for multiple files

Provide I/O time comparison table.
```

### Prompt: Memory Optimization
```text
Reduce memory usage in this data processing code:

{{CODE}}

Current memory profile:
- Peak usage: {{PEAK_MB}} MB
- Dataset size: {{ROWS}} rows
- Target: {{TARGET_MB}} MB or lower

Apply:
1. Generator/iterator patterns instead of lists
2. dtype optimization (downcast numerics, categoricals)
3. Chunked processing
4. del + gc.collect() for intermediate results
5. __slots__ for custom classes
6. Memory-efficient data structures (arrays vs lists)
7. Copy-on-write (pandas 2.0+)

Show memory profile before/after with tracemalloc.
```

### Prompt: Use Polars Instead of Pandas
```text
Convert this Pandas code to Polars for better performance:

{{CODE}}

Focus on:
1. Lazy evaluation with scan_* and collect()
2. Expression-based API (no apply())
3. Parallel execution (automatic in Polars)
4. Streaming for large datasets
5. Efficient string operations

Provide:
- Equivalent Polars code
- API mapping for common operations
- Benchmark comparison (Pandas vs Polars)
- Memory usage comparison
```

### Prompt: GPU Acceleration
```text
Add GPU acceleration to this data processing code:

{{CODE}}

GPU environment:
- GPU: {{GPU_MODEL}}
- VRAM: {{VRAM_GB}} GB
- Framework preference: {{CUDF/RAPIDS/CUPY/NUMBA}}

Implement:
1. Data transfer optimization (minimize CPU↔GPU copies)
2. Batch sizing for VRAM constraints
3. Fallback for non-GPU environments
4. Mixed precision where applicable

Benchmark: CPU baseline vs GPU accelerated.
```

### Prompt: Optimize with Cython/Numba
```text
Accelerate this computation-heavy code with Cython or Numba:

{{CODE}}

Hot path analysis: {{DESCRIPTION}}

For Numba (@jit):
- Identify nopython-compatible code
- Add type hints for better compilation
- Use parallel=True for loop parallelization
- Apply @vectorize for ufuncs

For Cython:
- Add static type declarations
- Use memoryviews for arrays
- Disable bounds checking in hot loops
- Release GIL for parallel sections

Provide compilation instructions and benchmark comparison.
```

### Prompt: End-to-End Pipeline Optimization
```text
Optimize this complete data processing pipeline:

{{CODE}}

Pipeline stages:
1. Data ingestion: {{INGESTION_DETAILS}}
2. Transformation: {{TRANSFORM_DETAILS}}
3. Aggregation: {{AGG_DETAILS}}
4. Output: {{OUTPUT_DETAILS}}

Total data volume: {{VOLUME}}
Current runtime: {{CURRENT_TIME}}
Target runtime: {{TARGET_TIME}}

Provide:
1. Stage-by-stage profiling and bottleneck analysis
2. Optimizations for each stage
3. Data flow optimization (minimize copies, lazy evaluation)
4. Caching strategy for repeated operations
5. Complete optimized pipeline
6. Benchmark table showing improvement per stage
```

---

## Benchmarking Framework

### Standard Benchmark Template

Always measure and report using this structure:

```python
"""
Performance Benchmark Report
============================
Date: {{DATE}}
Code Version: {{VERSION}}
Hardware: {{CPU}}, {{RAM}} GB RAM, {{GPU if applicable}}
Python: {{VERSION}}
Key Libraries: {{LIBRARY_VERSIONS}}

Data Characteristics:
- Input size: {{SIZE}}
- Format: {{FORMAT}}
- Complexity: {{DESCRIPTION}}

Results:
| Stage | Baseline | Optimized | Speedup | Memory Δ |
|-------|----------|-----------|---------|----------|
| Load  | X.XX s   | X.XX s    | X.Xx    | -XX%     |
| Process| X.XX s  | X.XX s    | X.Xx    | -XX%     |
| Save  | X.XX s   | X.XX s    | X.Xx    | -XX%     |
| Total | X.XX s   | X.XX s    | X.Xx    | -XX%     |

Methodology:
- Runs: 5 (median reported)
- Warmup: 1 run discarded
- Environment: Fresh process, no competing workloads
"""
```

### Benchmarking Code Snippets

```python
# Timing with context manager
import time
from contextlib import contextmanager

@contextmanager
def timer(name: str = "Operation"):
    start = time.perf_counter()
    yield
    elapsed = time.perf_counter() - start
    print(f"{name}: {elapsed:.4f} seconds")

# Memory profiling
import tracemalloc

def profile_memory(func):
    """Decorator to profile memory usage."""
    def wrapper(*args, **kwargs):
        tracemalloc.start()
        result = func(*args, **kwargs)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        print(f"Current: {current / 1024 / 1024:.2f} MB")
        print(f"Peak: {peak / 1024 / 1024:.2f} MB")
        return result
    return wrapper

# Comparative benchmarking
import timeit

def benchmark_comparison(baseline_func, optimized_func, data, runs=5):
    """Compare two implementations."""
    baseline_time = timeit.timeit(
        lambda: baseline_func(data), number=runs
    ) / runs
    
    optimized_time = timeit.timeit(
        lambda: optimized_func(data), number=runs
    ) / runs
    
    speedup = baseline_time / optimized_time
    print(f"Baseline: {baseline_time:.4f}s")
    print(f"Optimized: {optimized_time:.4f}s")
    print(f"Speedup: {speedup:.2f}x")
    return speedup
```

---

## Performance Optimization Hierarchy

Apply optimizations in this order (highest impact first):

### 1. 🔴 Algorithm & Data Structure (10-1000x improvement)
- Choose O(n) over O(n²) algorithms
- Use appropriate data structures (sets for lookup, deque for queues)
- Implement early termination and pruning

### 2. 🟠 Vectorization (10-100x improvement)
- Replace Python loops with NumPy/Pandas operations
- Use broadcasting instead of iteration
- Leverage SIMD operations

### 3. 🟡 I/O Optimization (2-50x improvement)
- Use columnar formats (Parquet, Feather) over CSV
- Enable compression (snappy, zstd)
- Batch I/O operations
- Use memory-mapped files

### 4. 🟢 Parallelization (2-Nx improvement, N = cores)
- multiprocessing for CPU-bound work
- asyncio for I/O-bound work
- Dask/Ray for distributed processing

### 5. 🔵 Low-Level Optimization (1.5-10x improvement)
- Numba JIT compilation
- Cython for hot paths
- GPU acceleration (CuPy, RAPIDS)

### 6. ⚪ Micro-Optimizations (1.1-1.5x improvement)
- List comprehensions over map/filter
- Local variable caching
- String interning
- __slots__ for classes

---

## Common Anti-Patterns & Fixes

### Anti-Pattern 1: Row-by-Row DataFrame Iteration

```python
# ❌ SLOW: Iterating with iterrows()
for idx, row in df.iterrows():
    df.loc[idx, 'new_col'] = row['a'] + row['b']

# ✅ FAST: Vectorized operation
df['new_col'] = df['a'] + df['b']
# Speedup: 100-1000x
```

### Anti-Pattern 2: Repeated DataFrame Appends

```python
# ❌ SLOW: Growing DataFrame in loop
result = pd.DataFrame()
for chunk in chunks:
    result = pd.concat([result, process(chunk)])

# ✅ FAST: Collect then concat once
results = [process(chunk) for chunk in chunks]
result = pd.concat(results, ignore_index=True)
# Speedup: 10-100x
```

### Anti-Pattern 3: Using apply() for Vectorizable Operations

```python
# ❌ SLOW: apply() with lambda
df['upper'] = df['name'].apply(lambda x: x.upper())

# ✅ FAST: Vectorized string method
df['upper'] = df['name'].str.upper()
# Speedup: 5-20x
```

### Anti-Pattern 4: Inefficient Data Types

```python
# ❌ WASTEFUL: Default int64/float64
df = pd.read_csv('data.csv')  # All columns as int64/float64

# ✅ EFFICIENT: Optimized dtypes
df = pd.read_csv('data.csv', dtype={
    'id': 'int32',
    'category': 'category',
    'value': 'float32',
    'flag': 'bool'
})
# Memory reduction: 50-75%
```

### Anti-Pattern 5: Loading Full File When Streaming Works

```python
# ❌ MEMORY HOG: Load entire file
df = pd.read_csv('huge_file.csv')
result = df.groupby('category').sum()

# ✅ MEMORY EFFICIENT: Chunked processing
chunks = pd.read_csv('huge_file.csv', chunksize=100_000)
result = pd.concat([
    chunk.groupby('category').sum() 
    for chunk in chunks
]).groupby(level=0).sum()
# Memory reduction: 90%+
```

### Anti-Pattern 6: Repeated Filtering

```python
# ❌ SLOW: Multiple filter passes
active = df[df['status'] == 'active']
recent = active[active['date'] > cutoff]
high_value = recent[recent['value'] > 1000]

# ✅ FAST: Single combined filter
result = df.query(
    "status == 'active' and date > @cutoff and value > 1000"
)
# Speedup: 2-5x
```

---

## Library Performance Comparison

| Task | Pandas | Polars | DuckDB | Speedup |
|------|--------|--------|--------|---------|
| CSV read (1GB) | 45s | 8s | 6s | 7x |
| GroupBy agg | 12s | 0.8s | 0.5s | 24x |
| Join (10M rows) | 8s | 0.6s | 0.4s | 20x |
| Filter | 2s | 0.1s | 0.1s | 20x |
| Memory (1GB CSV) | 4GB | 1.2GB | 0.8GB | 5x |

**Recommendation**: For datasets > 100MB, consider Polars or DuckDB.

---

## Report Format

Generate a comprehensive analysis and save as **two deliverables**:

### 1. Summary Report: `data-performance-[YYYY-MM-DD].md`

```markdown
# Data Processing Performance Analysis

## Overview
- **Scope**: [What was analyzed]
- **Dataset**: [Size, format, characteristics]
- **Baseline Runtime**: [Current time]
- **Optimized Runtime**: [New time]
- **Total Speedup**: [X.Xx]
- **Memory Reduction**: [XX%]

## Executive Summary
[2-3 sentence summary of findings and impact]

## Benchmark Results

### Before Optimization
| Stage | Time | Memory | Throughput |
|-------|------|--------|------------|
| ... | ... | ... | ... |
| **Total** | **X.XX s** | **XXX MB** | **X rows/s** |

### After Optimization
| Stage | Time | Memory | Throughput | Improvement |
|-------|------|--------|------------|-------------|
| ... | ... | ... | ... | ... |
| **Total** | **X.XX s** | **XXX MB** | **X rows/s** | **X.Xx** |

## Optimizations Applied
1. [Optimization with quantified impact]
2. [Optimization with quantified impact]
3. ...

## Prioritized Remaining Opportunities
- 🔴 [High-impact opportunity not yet implemented]
- 🟡 [Medium-impact opportunity]
- 🟢 [Low-impact opportunity]

## Reproducibility
- Python version: X.XX
- Key libraries: pandas==X.X, numpy==X.X, ...
- Hardware: [specs]
- Benchmark command: `python benchmark.py --runs 5`
```

### 2. Per-Optimization Details: `data-performance-[YYYY-MM-DD]/`

Create a folder with individual files:
- `optimization-001-vectorization.md`
- `optimization-002-io-format.md`
- `optimization-003-parallelization.md`

Each file should contain:
- **What was changed** with code diff
- **Why it's faster** (technical explanation)
- **Measured improvement** (benchmark data)
- **Trade-offs** (if any)
- **How to verify** (reproducible benchmark)

---

## Success Metrics

| Metric | Target | How to Measure |
|--------|--------|----------------|
| Speedup | ≥ 2x improvement | timeit comparison |
| Memory | ≤ 50% of baseline | tracemalloc peak |
| Throughput | ≥ 2x rows/second | calculated |
| Reproducibility | < 5% variance | 5-run std dev |
| Code Quality | Passes linting | ruff check |

---

## Tool Recommendations

### Profiling
- **cProfile**: Built-in, good overview
- **line_profiler**: Line-by-line timing
- **py-spy**: Sampling profiler, low overhead
- **Scalene**: CPU, memory, and GPU profiling

### Benchmarking
- **timeit**: Quick timing
- **pytest-benchmark**: Integration with tests
- **asv (airspeed velocity)**: Track performance over time

### Memory
- **tracemalloc**: Built-in memory tracking
- **memory_profiler**: Line-by-line memory
- **memray**: Modern memory profiler with flamegraphs

### Visualization
- **snakeviz**: Interactive cProfile visualization
- **flamegraph**: CPU profiling visualization
- **memray flamegraph**: Memory flamegraphs

---

## Quick Reference: Modern High-Performance Stack

```python
# 2026 recommended stack for data processing

# Fast DataFrame operations
import polars as pl  # or pandas 2.0+ with PyArrow backend

# Numerical computing
import numpy as np
from numba import jit, prange  # JIT compilation

# Parallel processing
from concurrent.futures import ProcessPoolExecutor
import multiprocessing as mp

# Async I/O
import asyncio
import aiofiles

# File formats
import pyarrow.parquet as pq  # Parquet I/O
import pyarrow.feather as feather  # Feather I/O

# Progress tracking
from tqdm import tqdm

# Profiling
import cProfile
import tracemalloc
from line_profiler import profile
```

---

## Severity Levels

| Level | Label | Criteria | Action |
|-------|-------|----------|--------|
| 🔴 | **Critical** | >10x slower than optimal, blocks processing | Fix immediately |
| 🟠 | **High** | 2-10x slower, significant resource waste | Fix before production |
| 🟡 | **Medium** | 1.5-2x slower, noticeable impact | Should fix |
| 🟢 | **Low** | <1.5x slower, minor optimization | Optional, document |

---

## Related Prompts

- [concurrency-asyncio-pattern-analysis.md](concurrency-asyncio-pattern-analysis.md) — Async patterns
- [code-refactoring.md](code-refactoring.md) — General code improvement
- [modern-patterns.md](modern-patterns.md) — Python 3.11+ features
