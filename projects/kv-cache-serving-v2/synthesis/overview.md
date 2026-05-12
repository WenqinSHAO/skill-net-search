# Overview

## Project Question

What is the emerging architecture of KV-aware LLM serving systems, and how do different papers intervene on the same bottleneck from different layers of the stack?

## Provisional Categories

### 1. Reuse and sharing

- Reuse existing KV state across requests or workflows
- Share KV across models, agents, or tenants
- Reduce repeated prefill cost

Examples:

- LMCache
- KVFlow
- Tokencake
- KVShare
- SemShareKV
- DroidSpeak
- Q-KVComm

### 2. Compression and eviction

- Compress KV footprint directly
- Decide which KV state to keep or drop under budget
- Trade off memory against quality or recomputation

Examples:

- KVTC
- IceCache
- PolarQuant
- Ada-KV
- KeyDiff
- ChunkKV
- Joint Encoding of KV-Cache Blocks

### 3. Tiered memory and disaggregation

- Push KV beyond local GPU memory
- Swap KV across CPU, flash, or remote memory
- Separate compute and KV residence

Examples:

- DistServe
- Mooncake
- HCache
- HiFC

### 4. Serving policies shaped by KV constraints

- Scheduling or placement that only makes sense once KV becomes a first-class resource
- System behavior driven by KV locality, occupancy, or load imbalance

Examples:

- JITServe
- FlexLLM
- Seshat
- Agentix

## Current Hypothesis

The literature seems to be moving from local KV optimizations toward explicit KV-aware system design:

1. First, reduce memory waste.
2. Then, externalize KV into tiers or services.
3. Then, treat KV as a reusable and shareable state object across workflows.

This needs to be sharpened with per-paper notes and a cleaner timeline.
