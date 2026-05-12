# neurips25-006 — Ada-KV

## Why it matters in this project

Ada-KV is one of the core eviction papers because it moves beyond uniform token/head treatment and allocates budget adaptively.

## Architectural role

**Role**: adaptive-budget eviction architecture.

Its contribution is not retrieval or compression coding, but deciding where scarce KV budget should go across attention structure.

## Benchmarking structure

### Scenario

- long-sequence inference under fixed KV budget

### Workload shape

- question-aware and question-agnostic settings
- LongBench and Ruler-style benchmark suites

### Metrics

- generation quality under eviction
- robustness across budget settings
- gains over prior eviction methods

## Comparison use

Compare Ada-KV with:

- KeyDiff
- TRIM-KV

It should not be judged mainly against retrieval systems on speedup.

## Project takeaway

Ada-KV sharpens the idea that **budget allocation itself is an architectural choice inside eviction systems**.
