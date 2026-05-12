# neurips25-008 — HiFC

## Why it matters in this project

HiFC matters because it brings flash/SSD into the KV memory hierarchy without relying on host DRAM as the main expansion path.

## Architectural role

**Role**: flash-based KV swapping architecture.

It is a memory-tier paper, but with a very concrete systems angle:

- direct SSD-to-GPU data path
- reduced dependence on expensive DRAM pools

## Benchmarking structure

### Scenario

- long-context inference whose KV footprint exceeds GPU memory
- DRAM-free or DRAM-minimized swapping

### Workload shape

- long-context workloads such as NarrativeQA
- sustained swapping under load

### Metrics

- inference throughput
- cost of memory expansion
- latency stability under load
- durability/endurance implications for SSD regions

## Comparison use

Compare HiFC with:

- IceCache
- HCache
- Mooncake

The main axis is storage tier and transfer path, not semantic reuse.

## Project takeaway

HiFC shows that KV-serving architecture can also be a **storage-systems problem**, not only an inference-scheduler problem.
