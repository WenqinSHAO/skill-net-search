# neurips25-007 — KeyDiff

## Why it matters in this project

KeyDiff matters as a training-free eviction baseline centered on key similarity rather than learned gating or heavy orchestration.

## Architectural role

**Role**: key-similarity-based eviction architecture.

It is a lightweight alternative in the retention branch and helps define what a simpler, training-free eviction system looks like.

## Benchmarking structure

### Scenario

- long-context inference in resource-constrained environments

### Workload shape

- long prompts under strict memory constraints

### Metrics

- quality under eviction
- feasibility in constrained memory
- comparison to other training-free eviction methods

## Comparison use

Compare KeyDiff with:

- Ada-KV
- TRIM-KV

The useful distinction is:

- similarity-based heuristic
- adaptive analytical allocation
- learned retention

## Project takeaway

KeyDiff is useful because it anchors the low-complexity end of the eviction design space.
