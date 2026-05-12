# Research Program

## Core Question

How do current systems push KV reuse beyond exact prefix reuse, and when is the storage-for-computation trade actually favorable?

## Main Workstreams

### 1. Reuse-contract ladder

Map the field by what contract each system is willing to support:

- exact prefix reuse
- approximate cross-request reuse
- semantic reuse
- cross-model reuse
- agent/protocol-level exchange

The point is to identify where the compatibility boundary moves and what new infrastructure each move requires.

### 2. Storage-for-computation economics

For each main reuse style, ask:

- what compute is avoided?
- what storage footprint is added?
- what transfer path is required?
- what latency is saved?
- what quality risk is introduced?

This should not rely on one vague “reuse is good” claim. It needs an explicit cost model.

### 3. Beyond-prefix mechanisms

Identify the main tricks people use to go beyond exact prefix reuse:

- approximate matching
- semantic matching
- selective recomputation
- clustering / centroiding
- sparse-attention-guided cache reuse
- workflow- or program-level reuse planning

### 4. Cross-model and multi-agent state sharing

Study when reusable KV stops being a cache and starts behaving like an intermediate representation:

- across model variants
- across different models
- across agents in larger programs

### 5. Future interaction with sparse attention

Test the hypothesis that newer sparse-attention or structured-sparsity designs make reusable KV more attractive by:

- making retained state smaller
- exposing stronger locality
- making reusable state more structured
- widening the set of contexts that can share internal state

## Deliverables

1. A narrow landscape of beyond-prefix KV reuse systems.
2. A storage-versus-computation tradeoff framework.
3. A comparison of exact, approximate, semantic, cross-model, and agent-level reuse.
4. A forward-looking note on sparse attention and reusable model-native state.
