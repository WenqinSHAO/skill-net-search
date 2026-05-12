# Architecture

## Core Architectural View

This project should analyze papers primarily by **what system boundary they move**, not by surface method labels alone.

The most useful architectural layers so far are:

### 1. Local KV memory management

Question:

- How is KV represented and allocated within a serving node?

Anchor:

- PagedAttention / vLLM

### 2. KV retrieval and selective movement

Question:

- When KV no longer fits in fast memory, how does the system decide what to fetch, retain, or evict?

Anchors:

- InfiniGen
- IceCache
- LouisKV
- TRIM-KV

### 3. Phase-disaggregated execution

Question:

- How does the architecture separate KV production and KV consumption across prefill and decode?

Anchors:

- DistServe
- Splitwise

### 4. KV-centric multi-tier serving platform

Question:

- How does the system organize compute, storage tiers, scheduling, and overload behavior around KV?

Anchors:

- Mooncake
- HCache
- Prefill-as-a-Service
- DualMap

### 5. Cross-request / cross-model KV reuse

Question:

- When can KV be reused as a transferable intermediate state rather than regenerated?

Anchors:

- LMCache
- KVShare
- SemShareKV
- DroidSpeak
- Q-KVComm

## Working Architectural Thesis

The field appears to evolve through successive enlargements of the KV boundary:

1. KV as a local memory-allocation problem
2. KV as a retrieval and movement problem
3. KV as a phase boundary between prefill and decode
4. KV as the center of a multi-tier serving platform
5. KV as a reusable interface across requests, workflows, and models

This thesis should be tested and refined as more per-paper notes are added.

## What To Watch For In Later Notes

For each new paper, ask:

1. What boundary does it move?
2. Does it reduce KV size, reduce KV movement, or redefine KV reuse?
3. Is it a local mechanism, a scheduler primitive, or a system architecture?
4. Which existing branch of the design space does it deepen, and which branch does it leave untouched?
