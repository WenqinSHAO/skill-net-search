# Reuse And Sharing

## Why This Comparison Matters

This branch is central to the project because it makes the storage-versus-computation trade explicit.

All five papers ask some version of the same strategic question:

- when is it better to preserve and reuse prior KV state rather than recompute it?

But they answer it at different system boundaries:

- `arxiv25-001` LMCache turns KV into an external reusable service layer.
- `arxiv25-004` KVShare allows approximate reuse across requests in multi-tenant serving.
- `arxiv25-005` SemShareKV pushes reuse further by using semantic similarity rather than exact or near-exact prefix identity.
- `nsdi26-008` DroidSpeak extends reuse across different models with selective recomputation.
- `arxiv-2501` Q-KVComm goes even further and treats KV as a communication representation between agents.

So the comparison is not just about reuse quality. It is about what level of the serving stack is being redefined:

- cache layer
- tenant-sharing layer
- semantic matching layer
- cross-model interface
- inter-agent protocol

That is why this branch links directly back to serving infrastructure rather than standing alone as an algorithm family.

## Common Problem Frame

The shared pressure behind this line is straightforward:

- prefill is expensive
- overlapping context appears repeatedly
- full recomputation wastes compute and latency budget
- storing everything blindly creates its own infrastructure burden

So reuse systems must decide:

1. what counts as a reusable state boundary
2. how exact that boundary must be
3. when recomputation is still necessary
4. how the serving system stores, routes, and exposes reusable state

This is why reuse is a systems contract, not just a matching trick.

## Architectural Progression

### LMCache: external reusable KV infrastructure

LMCache is the cleanest infrastructure-first paper in the branch.

Its main move is:

- move KV outside GPU-local engine state
- allow reuse across queries
- allow reuse across engines and execution paths

This is important because it says the main problem is not merely finding a reuse opportunity. It is creating a serving substrate where reusable KV can persist and be accessed across inference engines.

Best read:

- a reusable KV service-layer architecture
- infrastructure for cross-query and cross-engine reuse

### KVShare: approximate reuse under serving pressure

KVShare adds a more aggressive reuse contract.

Its main move is:

- do not require exact prefix identity
- allow approximate reuse across requests
- explicitly manage quality risk and selective recomputation

Compared with LMCache, KVShare is less about building the external cache substrate and more about widening what the service counts as a reusable hit under multi-tenant TTFT pressure.

Best read:

- a serving-oriented approximate reuse paper
- a system that trades some recomputation and quality control for broader reuse coverage

### SemShareKV: semantic similarity as the reuse boundary

SemShareKV pushes this line further by changing the notion of compatibility itself.

Its main move is:

- find semantically similar prompts rather than exact or mostly exact ones
- use fuzzy matching and positional handling to recover reusable state

Compared with KVShare, the key difference is that the reuse boundary is no longer mostly prefix-structural. It becomes similarity-search-driven.

Best read:

- a semantic reuse expansion paper
- a system that treats KV sharing partly as a retrieval/matching problem

### DroidSpeak: cross-model reusable intermediate state

DroidSpeak changes the branch qualitatively.

Its main move is:

- allow one model to reuse another model’s KV
- preserve quality with selective layer recomputation
- make reuse viable across cooperating models with shared architecture

Compared with SemShareKV or KVShare, the question is no longer only whether two requests are similar enough. The question becomes whether two executions from different models are compatible enough for partial state reuse.

Best read:

- a cross-model reuse architecture
- a paper that turns KV into an inter-model serving interface

### Q-KVComm: reuse becomes communication protocol

Q-KVComm pushes the strongest version of the idea.

Its main move is:

- transmit compressed KV-style internal representations between agents
- treat internal state as a communication medium rather than only a saved cache

Compared with DroidSpeak, the system focus shifts:

- DroidSpeak is still primarily about serving efficiency through shared state
- Q-KVComm is about replacing or augmenting text-based agent communication with representation exchange

Best read:

- a protocol-level paper
- an early signal that KV may become a shared representation beyond serving internals

## Benchmark Regime

This branch is comparable only if the source of the reuse opportunity is made explicit.

### Shared comparison axes

- TTFT reduction
- throughput gain
- compute saved through avoided prefill
- quality degradation after reuse
- storage or transfer overhead

### Critical benchmark differences

LMCache emphasizes:

- cross-query prefix reuse
- cross-engine operation
- persistent external KV footprint

KVShare emphasizes:

- multi-tenant serving
- long-context requests
- TTFT and throughput under approximate reuse

SemShareKV emphasizes:

- semantically similar prompts with lexical variation
- speedup and memory reduction
- output-quality degradation under fuzzy reuse

DroidSpeak emphasizes:

- multi-model or compound-AI settings
- throughput and prefill speedup
- quality under selective recomputation

Q-KVComm emphasizes:

- multi-agent communication tasks
- compression ratio
- semantic fidelity and task robustness

This means the branch is not one benchmark family. It spans at least three:

1. serving reuse across requests
2. serving reuse across models
3. representation exchange across agents

## Comparative Judgment

### What LMCache gets right

- makes KV reuse an infrastructure concern rather than an engine-local optimization
- creates the cleanest bridge between cache persistence and serving systems
- highlights that reuse needs a service substrate, not just a matching policy

Main limitation:

- broader reuse contracts still have to be layered on top of it

### What KVShare adds

- expands reuse beyond exact matches
- directly engages the serving pressure behind reuse, especially TTFT in multi-tenant settings
- makes selective recomputation part of the reuse contract

Main limitation:

- still lives mainly in the request-serving world rather than cross-model or agent-level reuse

### What SemShareKV adds

- widens the reuse boundary from lexical/prefix overlap to semantic similarity
- shows that reuse can be phrased as a similarity-search problem
- increases the possible hit rate where exact reuse is too restrictive

Main limitation:

- quality assurance becomes harder because compatibility is less structural and more inferred

### What DroidSpeak adds

- changes reuse from cross-request to cross-model
- makes selective recomputation the key bridge between incompatible and compatible state
- suggests that KV can serve as an inter-model intermediate representation

Main limitation:

- depends on stronger architectural compatibility assumptions across models

### What Q-KVComm adds

- pushes KV beyond cache reuse into agent communication
- reframes the reuse question as "should models exchange internal state rather than regenerated text?"
- signals the most speculative and forward-looking part of the branch

Main limitation:

- it is only partly comparable to serving papers because the objective shifts from serving efficiency to communication efficiency and semantic fidelity

## Serving-Infrastructure View

Your framing is exactly the right one: reuse is not a standalone algorithmic trick.

The branch only becomes important because it interacts with serving infrastructure in at least four ways:

1. **State persistence**
   - reusable KV must exist outside one ephemeral execution path
2. **Routing and locality**
   - the system must bring related requests, models, or agents into contact with the reusable state
3. **Compatibility control**
   - the system needs rules for exact reuse, approximate reuse, or partial recomputation
4. **Operational accounting**
   - the system must decide when extra storage and transfer are cheaper than repeated compute

That is why LMCache and DroidSpeak feel architecturally central: both force the serving stack to expose reusable state as infrastructure, not just exploit it opportunistically inside one kernel path.

## Productization View

If the question is "which idea looks most productizable now?" the answer is stratified.

For same-request-family or same-engine serving:

- LMCache is the most direct infrastructure template

For multi-tenant serving with strong TTFT pressure:

- KVShare is the strongest practical comparison point

For broader semantic reuse:

- SemShareKV is attractive but carries more matching and quality-risk burden

For compound systems with cooperating models:

- DroidSpeak is the most strategically important, because it suggests a new serving interface rather than just a larger cache

For agent-to-agent representation exchange:

- Q-KVComm is the most speculative; it is better read as a forward signal than an immediate serving blueprint

## Project Takeaway

This line of work establishes the third central claim of the project:

**KV reuse is really a question of where the system is willing to substitute stored intermediate state for repeated computation.**

The progression can be read as:

1. preserve KV outside the local engine
2. widen the conditions for reuse across requests
3. widen them again through semantic similarity
4. treat KV as a reusable interface across models
5. potentially treat KV as an inter-agent communication medium

That makes this branch the bridge between classic serving infrastructure and the more speculative future of compound and agentic systems. It is not a side algorithm line. It is one of the clearest places where storage, scheduling, compatibility, and compute substitution meet.
