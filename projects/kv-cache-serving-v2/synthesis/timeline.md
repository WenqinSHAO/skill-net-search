# Timeline

## 2023

- Early serving work establishes KV memory as the operational bottleneck rather than a hidden implementation detail.
- Cache-oriented execution and memory-management ideas begin to show up as system primitives.

## 2024

- Disaggregated and phase-splitting serving designs make KV placement a system-level concern.
- The design space shifts from “fit on one GPU” to “where should KV live and when should it move?”

## 2025

- The field expands rapidly along multiple fronts:
  - eviction
  - compression
  - quantization
  - sharing
  - tiered storage
- A key question emerges: are these competing alternatives, or composable building blocks?

## 2026

- The problem becomes more explicit in project and production terms:
  - cross-model sharing
  - queueing and stability under KV constraints
  - serving policy under uncertain or changing workload information

## Working Questions

- Which step changed the field most: disaggregation, compression, or reuse?
- Which 2025 ideas survive as primitives in 2026 systems?
- Where does multi-agent KV communication belong in this timeline?
