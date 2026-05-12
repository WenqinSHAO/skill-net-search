# neurips25-003 — PolarQuant

## Why it matters in this project

PolarQuant is a key quantization paper in the scope because it targets one of the hardest aspects of KV compression: quantizing keys without excessive error from outliers.

## Architectural role

**Role**: key-side quantization architecture.

It belongs to the low-precision compression branch rather than retrieval or reuse.

## Benchmarking structure

### Scenario

- long-context inference under KV memory pressure
- low-bit KV quantization

### Workload shape

- inference settings where quantization overhead and decoding efficiency both matter

### Metrics

- accuracy retention under quantization
- memory reduction
- decoding acceleration / runtime overhead

## Comparison use

Compare PolarQuant with:

- KVTC
- ChunkKV
- Joint Encoding

The key difference is that PolarQuant compresses via low-precision representation rather than selection or block fusion.

## Project takeaway

PolarQuant anchors the **quantization-first** branch of KV efficiency.
