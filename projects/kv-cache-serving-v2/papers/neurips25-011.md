# neurips25-011 — ChunkKV

## Why it matters in this project

ChunkKV matters because it attacks compression at the semantic-chunk level rather than the isolated-token level.

## Architectural role

**Role**: semantic-unit KV compression architecture.

It is an important counterpoint to token-wise eviction and quantization papers.

## Benchmarking structure

### Scenario

- long-context inference under aggressive compression

### Workload shape

- LongBench
- Needle-In-A-Haystack
- GSM8K
- JailbreakV

### Metrics

- accuracy / precision under compression
- throughput improvement via layer-wise index reuse
- compression-ratio-matched comparisons

## Comparison use

Compare ChunkKV with:

- KVTC
- PolarQuant
- TRIM-KV

It occupies the semantic-preservation branch rather than pure low-bit or pure retention.

## Project takeaway

ChunkKV suggests that preserving the right **semantic unit** may matter more than preserving the right isolated token.
