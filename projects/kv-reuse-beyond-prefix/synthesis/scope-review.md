# Scope Review

## Initial Narrow Scope

This project is intentionally narrower than `kv-cache-serving-v2`.

The center of gravity is:

- how reuse goes beyond exact prefix reuse
- how storage is traded for avoided computation
- what serving infrastructure is required to make that trade practical
- whether sparse or structured attention makes broader reuse more plausible

## Imported First Batch

The first focused import batch added:

- `arxiv25-006` PRKV
- `arxiv25-007` CentroidKV
- `arxiv25-008` SamKV
- `arxiv25-010` NOSA
- `arxiv26-004` HySparse

These additions matter because they extend the project in two directions:

1. they widen beyond-prefix or structure-aware reuse through clustering, hybrid selection, or multiple-context sparse attention
2. they provide the first concrete bridge between sparse attention and KV sharing

## What Now Looks Strong Enough

The project now has enough shared-DB coverage to support a first serious narrative on:

- exact prefix reuse as infrastructure
- approximate and semantic reuse
- cross-model reuse
- agent-level representation exchange
- sparse-attention-guided or clustering-guided reuse extensions

## What Still Needs Fresh Search

### 1. Better economic evidence

We still need primary-source or current-market evidence for:

- storage-tier cost
- bandwidth and latency by tier
- when reuse stops paying for itself

### 2. Broader heterogeneous-model reuse

The current repo is still stronger on:

- same-architecture cross-model reuse

than on:

- truly heterogeneous model-family reuse

### 3. Boundary cases

We may still want one or two strong counterpoints where:

- sparse attention reduces the need for reuse instead of encouraging it
- compression wins more cleanly than reuse
