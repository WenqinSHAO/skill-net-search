# KV Reuse Beyond Prefix Analysis

## Thesis

The most useful way to understand this project is:

**KV reuse stops being “prefix caching” and becomes a real systems design space once the system is willing to preserve, transport, approximate, or reinterpret model-native state in order to avoid future computation.**

That design space now spans:

- exact prefix reuse as infrastructure
- approximate cross-request reuse
- semantic reuse
- app-logic-guided modular or plan-level reuse
- structured retained-state reuse
- cross-model reuse
- multi-context sparse reuse
- inter-agent representation exchange

The central trade is always the same:

- keep more state
- move more state
- avoid more compute

The difficult part is that these three do not scale together cleanly.

## A Working Sizing Model

For this project, it helps to make the object concrete.

At a high level, KV-cache footprint scales roughly with:

`KV bytes ~= 2 x L x H_kv x d_head x T x b`

Where:

- `L` is the number of transformer layers
- `H_kv` is the number of KV heads
- `d_head` is the head dimension
- `T` is the number of cached tokens
- `b` is bytes per element
- the factor `2` is for keys and values

This is only a project-level sizing abstraction, but it already explains why KV reuse became a first-class systems issue:

- storage grows linearly with token count
- long prompts and long agent trajectories produce large persistent state quickly
- the value of reuse rises with saved prefill, but so does the cost of retaining and moving that state

The second useful abstraction is a break-even rule:

`reuse is worthwhile when compute_saved > storage_cost + transfer_cost + lookup_cost + repair_cost + quality_risk_cost`

Everything in the current scope is a way of changing one side of that inequality:

- exact-cache systems reduce `lookup_cost` and `transfer_cost`
- approximate or semantic systems increase `compute_saved` by widening hits, but add `repair_cost` and `quality_risk_cost`
- sparse-attention systems reduce the retained-state term itself
- app-logic-guided systems improve the hit rate by carving out higher-value reusable boundaries

## 1. Reuse Contract Ladder

The cleanest structure for the field is not by venue or by algorithm family. It is by **reuse contract**.

### Level 1. Exact reusable cache infrastructure

Representative papers:

- `CacheGen`
- `HCache`
- `LMCache`

Contract:

- the reused object is still exact or nearly exact historical state
- the main systems work is persistence and transfer

What changes here is not compatibility but infrastructure. The system turns KV into a reusable external resource instead of an ephemeral GPU-local artifact.

Main benefits:

- high correctness confidence
- direct compute savings under repeated prefixes or repeated sessions

Main costs:

- persistent storage footprint
- transfer overhead
- orchestration complexity across engines or devices

Best fit:

- repeated or multi-turn enterprise workloads
- settings with high exact-prefix recurrence

Quantitative anchors:

- `LMCache` reports up to `15x` throughput improvement with vLLM on workloads such as multi-round QA and document analysis.
- `CacheGen` is important less for the absolute peak number and more for showing that stale or externalized KV can be compressed and streamed rather than recomputed blindly.

Architectural design:

- the cache object is still exact model-native state
- `LMCache` makes this operational by separating the cache layer from the inference engine via a connector plus a control API
- the system then supports both prefix reuse and prefill/decode disaggregation, so the same stored object can serve either repeated requests or split execution paths

Benchmark regime:

- these papers are most convincing on repeated-prefix or repeated-session workloads
- the key metrics are `TTFT`, throughput, cache-hit ratio, and transfer overhead
- `LMCache` is especially valuable because it also reports deployment-side observations such as remote-fetch delay and context truncation cutting hit rate roughly in half

### Level 2. Approximate request-level reuse

Representative paper:

- `KVShare`

Contract:

- reuse can happen without exact identity
- the system tolerates bounded approximation and selective recomputation

This is the first clear step beyond classic prefix caching at the serving layer.

Main benefits:

- higher reuse opportunity rate
- stronger TTFT savings in multi-tenant settings

Main costs:

- quality-risk management
- more complex correctness boundaries
- extra control logic around recomputation

Best fit:

- multi-tenant serving with repeated but not identical long contexts

Quantitative anchors:

- `KVShare` reports up to `9.39x` TTFT reduction, about `1.2x` throughput improvement over full recomputation, and `20.38%` accuracy improvement over prior approximate-reuse baselines.

Architectural design:

- `KVShare` explicitly splits the repair problem into a prefill-side and decode-side selective recomputation problem
- its `Dual-Stage High Deviation` logic identifies the small subset of reused state whose deviation matters enough to recompute
- the cache-aware scheduler then turns reuse opportunity into system throughput by prioritizing high-hit requests inside continuous batching

Benchmark regime:

- the relevant scenario is multi-tenant long-context serving rather than single-user repeated chat
- the paper evaluates across models including `Qwen2.5-7B`, `Llama3.1-8B`, and `Yi1.5-9B`
- the right comparison axis later is not only speedup, but whether the quality loss under approximate reuse stays bounded as context diverges

### Level 3. Semantic reuse

Representative paper:

- `SemShareKV`

Contract:

- prompts can be lexically different but semantically similar enough to share state

This is a stronger move than approximate prefix reuse because the compatibility boundary becomes inference-driven rather than largely structural.

Main benefits:

- much wider reuse surface
- reuse can occur even when token sequences diverge materially

Main costs:

- matching complexity
- less transparent quality guarantees
- greater risk of compatibility mistakes

Best fit:

- summary, conversation, or templated reasoning workloads with recurring semantic patterns

Quantitative anchors:

- `SemShareKV` reports up to `6.25x` speedup and `42%` lower GPU memory usage at `5k` input tokens with negligible quality degradation on summarization-style tasks.

Architectural design:

- the reuse contract changes at the matching layer rather than at the storage tier
- `SemShareKV` uses token-level `LSH` over token embeddings and then repairs positional ambiguity with `RoPE` awareness
- the critical design choice is that reuse is built on approximate token correspondence, not exact substring identity

Benchmark regime:

- the paper is strongest on summarization-style workloads where prompts differ lexically but share semantic structure
- the most important metrics are speedup, memory reduction, and downstream quality preservation under approximate semantic matching

### Level 4. App-logic-guided modular or plan-level reuse

Representative papers:

- `Prompt Cache`
- `Cost-Efficient Serving of LLM Agents via Test-Time Plan Caching`
- `Don't Break the Cache`

Contract:

- the application or framework explicitly exposes reusable structure before the runtime ever sees tokens as an undifferentiated stream

The key insight is that some of the best cache boundaries are visible from application logic:

- stable system prompts
- prompt templates
- tool schemas
- shared retrieved documents
- reusable intermediate plans
- intermediate artifacts consumed by multiple downstream steps

This is different from pure runtime KV reuse because the framework may know which context pieces are:

- stable
- high-value
- widely referenced
- worth persisting even if they are not the whole prefix

Main benefits:

- higher-confidence reusable boundaries
- less need for purely heuristic similarity matching
- possible separation between stable and dynamic context segments

Main costs:

- requires framework or application cooperation
- can miss opportunities not visible in app logic
- some cached artifacts are plans or prompt modules, not raw KV objects

Best fit:

- agent frameworks
- tool-heavy workflows
- applications with stable templates and repeated intermediate reasoning scaffolds

Quantitative anchors:

- `Prompt Cache` reports TTFT improvements ranging from about `8x` on GPU inference to about `60x` on CPU inference for long prompts such as document QA and recommendation settings.
- `Cost-Efficient Serving of LLM Agents via Test-Time Plan Caching` reports `46.62%` average cost reduction across several real-world agentic applications while maintaining task performance.
- `Don't Break the Cache` evaluates more than `500` agent sessions with `10,000`-token system prompts and reports `45-80%` API-cost reduction plus `13-31%` TTFT improvement, while also showing that naive full-context caching can hurt latency.

Architectural design:

- `Prompt Cache` treats a prompt as a composition of reusable modules rather than one flat token stream
- in project-level notation, if a prompt is `P = [m1, m2, ..., mk, x_dynamic]`, the runtime can reuse cached attention states for the stable modules `m_i` and prefill only the uncached or dynamic tail
- `Test-Time Plan Caching` shifts the reusable object above raw KV into plan templates and adapted execution traces
- `Don't Break the Cache` matters because it compares cache boundaries directly: full history, system prompt only, or system-plus-stable-scaffold with dynamic tool outputs excluded

Benchmark regime:

- the right workloads are long-horizon agent sessions, tool-using applications, and repeated execution scaffolds rather than classic long-document benchmarks
- the decisive metrics are no longer just `TTFT` and throughput; they also include API cost, session-level latency, and whether dynamic tool outputs poison the cache boundary

### Level 5. Structured retained-state reuse

Representative papers:

- `PRKV`
- `CentroidKV`

Contract:

- the system still retains or recovers prior state, but it changes the unit of reusable access
- reuse is improved through better page structure or clustering, not only through better request matching

These papers matter because they widen the reuse story without requiring semantic prompt matching or cross-model compatibility. They improve how retained state itself can be reused.

Main benefits:

- better compute savings from retained-state reuse under large KV footprints
- lower storage or access overhead through structure-aware retained-state handling

Main costs:

- approximation or clustering fidelity loss
- added machinery in access structure or cluster maintenance

Best fit:

- long-context serving where full retained state exists but must be made cheaper to reuse

Quantitative anchors:

- `PRKV` reports up to `6.75x` speedup over prior KV-retrieval methods by jointly improving selection and page-level transfer structure.
- `CentroidKV` reports up to `75%` KV-memory reduction, up to `1.92x` decoding acceleration, and up to `4x` serving-throughput improvement while preserving comparable performance.

Architectural design:

- `PRKV` changes the reuse unit from raw token positions to a better-structured page abstraction
- the point is not merely offloading; it is to make retrieval granularity closer to the actually useful reuse granularity
- `CentroidKV` moves further by clustering similar KV entries into centroids, so the stored object itself becomes approximate and compressed

Benchmark regime:

- these papers should be compared on long-context decoding workloads where the full retained state exists but direct reuse is too expensive
- later comparison should separate:
  - retrieval-structure wins (`PRKV`)
  - approximation-through-clustering wins (`CentroidKV`)

### Level 6. Multi-context sparse reuse

Representative paper:

- `SamKV`

Contract:

- the reused object is not a single causal prefix stream
- it is a set of independently computed context caches
- sparse selection plus local recomputation provides the bridge

This is highly relevant for RAG and multi-context inference. It is one of the clearest ways the field moves beyond single-prefix assumptions.

Main benefits:

- much more realistic for retrieval-augmented systems
- can retain multi-context benefits without full recomputation

Main costs:

- local recomputation is still necessary
- the cross-context selection logic is more involved
- retained-state footprint can still be large if sparsification is weak

Best fit:

- RAG or tool-driven systems with many independent context fragments

Quantitative anchors:

- `SamKV` reports compressing effective sequence length to about `15%` of the original without accuracy degradation relative to full-recomputation baselines in multi-context RAG scenarios.

Architectural design:

- `SamKV` assumes each retrieved context can already have its own cache
- reuse then becomes a sparse selection problem over multiple existing caches, with local recomputation filling in the missing interactions
- this is important because it maps more closely to realistic RAG or tool pipelines than single-prefix papers do

Benchmark regime:

- the core scenario is multi-context RAG rather than monolithic long documents
- the key metrics are effective sequence compression, retained accuracy, and the amount of local repair compute still required after sparse reuse

### Level 7. Cross-model reuse

Representative papers:

- `DroidSpeak`
- `LRAgent`

Contract:

- reusable KV can cross model boundaries as long as compatibility is strong enough
- selective recomputation or adapter-aware decomposition repairs the incompatibility gap

This is the strongest deployed-systems signal that KV might be more than a per-model cache.

Main benefits:

- avoids repeated prefill across cooperating models
- creates a stronger storage-for-computation trade because one preserved state can serve more than one model execution

Main costs:

- compatibility restrictions
- selective recomputation burden
- stronger serving-system coordination requirements

Best fit:

- compound systems with multiple architecture-compatible model variants
- multi-LoRA agent systems with shared backbones

Quantitative anchors:

- `DroidSpeak` reports up to `4x` throughput improvement and about `3.1x` faster prefill with negligible loss on F1, Rouge-L, or code-similarity metrics.
- `LRAgent` does not present one single headline ratio in the abstract, but architecturally it aims to approach the throughput and TTFT of fully shared caching while preserving the accuracy of the non-shared baseline.

Architectural design:

- `DroidSpeak` uses selective layer recomputation: reuse most layers from a source model and recompute only the incompatible subset
- a useful project-level abstraction is: if `L` layers exist and only `R` layers need repair, saved prefill work scales roughly with `(L - R) / L`, subject to transfer overhead
- `LRAgent` makes the compatibility contract even more explicit by decomposing cache state into a shared backbone component plus an adapter-specific low-rank component
- in project-level notation: `KV_agent ~= KV_base + Delta_KV_lora`, where the base is shared and only the low-rank delta remains agent-specific

Benchmark regime:

- `DroidSpeak` is validated on cross-model pairs with shared architecture and reports both throughput and quality metrics
- `LRAgent` belongs in multi-LoRA agent settings where role diversity exists but most weights still come from the same backbone

### Level 8. Agent/protocol-level representation exchange

Representative papers:

- `Q-KVComm`
- partially `Agentix` as a workflow context signal

Contract:

- internal representations, not raw text alone, become the object exchanged between agents

This is the most speculative stage in the current scope, but it matters because it changes the meaning of reuse entirely.

Main benefits:

- potentially very large avoided recomputation
- richer state transmission than natural-language serialization

Main costs:

- semantic fidelity risk
- protocol and interoperability complexity
- unclear near-term production path

Best fit:

- tightly managed multi-agent systems where representation exchange can be controlled end to end

Quantitative anchors:

- `Q-KVComm` is best read through its communication-side metrics: compression ratio, semantic fidelity, and robustness across model sizes and multi-hop tasks, rather than only TTFT or throughput.

## 2. How Current Systems Maximize The Storage-For-Computation Trade

There are five main strategies visible in the current scope.

### Why benchmark geometry matters

Many of the headline numbers in this space are not directly comparable because the papers operate in different workload geometries:

- repeated exact prefixes
- semantically similar but lexically different prompts
- multi-tenant long-context serving
- multi-context RAG
- cross-model or multi-agent pipelines
- sparse-attention decoding with offloadable state

That means later comparisons should always track at least four benchmarking dimensions:

- **scenario**: repeated chat, document QA, summarization, RAG, agent workflow, or multi-model serving
- **workload shape**: long input, long output, or both
- **metric family**: `TTFT`, decode throughput, end-to-end latency, API cost, memory footprint, or output quality
- **reuse burden**: exact hit, approximate match, semantic match, sparse selection, or repaired cross-model reuse

### A. Preserve exact state outside the fast path

Papers:

- `CacheGen`
- `HCache`
- `LMCache`

Idea:

- keep exact or near-exact state available outside GPU-local execution
- pay storage and transfer to avoid repeated prefill

This is the most infrastructure-like form of reuse.

Architectural design:

- `LMCache` is especially important because it separates KV persistence from the inference engine through a connector plus control API, and supports both prefix reuse and prefill/decode disaggregation.

Benchmark shape:

- repeated or multi-round workloads such as document analysis and QA
- the paper is useful because it ties systems design to real deployment constraints rather than only synthetic long-context tests

### B. Widen the set of compatible reuse opportunities

Papers:

- `KVShare`
- `SemShareKV`
- `DroidSpeak`
- `LRAgent`

Idea:

- if exact recurrence is too rare, widen compatibility through approximation, semantics, or partial repair

This increases the potential compute saved, but correctness becomes less automatic.

Architectural design:

- `KVShare` uses dual-stage high-deviation selection and selective recomputation.
- `LRAgent` splits the reusable state into a shared backbone-induced component and an adapter-dependent low-rank component.

Benchmark shape:

- `KVShare` is mainly a long-context multi-tenant serving paper
- `SemShareKV` is mainly a semantic-neighbor summarization paper
- `DroidSpeak` and `LRAgent` are multi-model or multi-agent compatibility papers

This is why a single “reuse speedup” ranking would be misleading.

### C. Make retained state cheaper or more reusable structurally

Papers:

- `PRKV`
- `CentroidKV`
- `SamKV`

Idea:

- the system can still save compute by preserving state, but the retained object must be restructured so it remains economically reusable

This is an important middle ground because it does not require the strongest compatibility claims.

Architectural design:

- `PRKV` improves the page as the access unit.
- `CentroidKV` uses chunked similarity matching and centroid merging.
- `SamKV` sparsifies over multiple context caches and then locally repairs the dropped information.

### D. Co-design attention and reusable state

Papers:

- `NOSA`
- `HySparse`

Idea:

- rather than treat reuse as an after-the-fact service optimization, redesign the attention pattern so retained state becomes cheaper, more structured, or more shareable

This is the most important future-facing branch in the project.

Quantitative anchors:

- `NOSA` reports up to `2.3x` decoding-throughput improvement over a vanilla trainable sparse-attention baseline while preserving near-lossless performance.
- `HySparse` reports nearly `10x` KV-cache reduction in its `80B` MoE setting, where only `5` of `49` layers use full attention.

Architectural design:

- `NOSA` keeps the sparse-attention computation native to training, then adds locality constraints that make the resulting accesses offloadable in deployment
- `HySparse` interleaves sparse layers with full-attention oracle layers, so sparse layers can inherit token selection and reuse the preceding full layer's KV

Benchmark shape:

- `NOSA` is a decoding-throughput story under trainable sparse attention
- `HySparse` is both a memory and compute story, especially in large-model settings where the sparse/full alternation changes the retained-state burden materially

### E. Use application logic to expose better cache boundaries

Papers:

- `Prompt Cache`
- `Cost-Efficient Serving of LLM Agents via Test-Time Plan Caching`
- `Don't Break the Cache`

Idea:

- instead of waiting for the runtime to infer reuse opportunities from token similarity alone, let the application or framework expose stable modules and reusable intermediate artifacts directly

This is important because it changes the unit of reuse from:

- whatever the runtime happens to see

to:

- what the application already knows is stable or repeatedly useful

## 3. Is Reuse Worthwhile When Storage Gets Expensive?

This is the most important question in the project that is **not yet fully answered**.

What the current papers already support:

- reuse can save substantial prefill computation
- reuse can reduce TTFT materially
- reuse often requires persistent state outside GPU memory
- reuse frequently shifts the bottleneck from compute to storage/transfer/control overhead
- agentic workloads make the usefulness of caching highly dependent on whether stable and dynamic context are separated cleanly

What the current project still lacks:

- one explicit common cost model

The answer clearly depends on tier.

## 3.1 A Concrete Cost Proxy

The repo still does not have a perfect deployment-cost model, but the public-cloud pricing surface is already strong enough to establish one useful proxy:

- **GPU/HBM is an opportunity-cost tier, not a storage-priced tier.**
  - AWS `p5.4xlarge` exposes `80 GB` of H100 HBM3 and `p5.48xlarge` exposes `640 GB` of HBM3 across 8 GPUs.
- **Memory-tier persistence is expensive but directly usable.**
  - Google Cloud lists memory-optimized memory at about `$0.0051` per GiB-hour, which is about `$3.67` per GiB-month.
- **Block storage is dramatically cheaper than live memory, but not free once performance is provisioned.**
  - AWS gp3 pricing examples use about `$0.08` per GB-month, with included baseline `3,000` IOPS and `125 MB/s`, and additional charges of about `$0.005` per provisioned IOPS-month and `$0.06` per provisioned MB/s-month.
- **Object storage is cheaper still.**
  - Google Cloud Standard Storage starts around `$0.020-0.026` per GB-month, depending on region or multi-region choice.

That implies a rough public-cloud ratio:

- memory-optimized DRAM-like persistence at about `$3.67/GiB-month`
- gp3-like block persistence at about `$0.08/GB-month`
- object storage at about `$0.02-0.026/GB-month`

So a very rough order-of-magnitude comparison is:

- DRAM-like persistence is about `46x` more expensive per GiB-month than gp3-like block storage
- and about `140x-180x` more expensive per GiB-month than commodity object storage

This is not a complete cost model for KV reuse, but it is already enough to make one conclusion hard to avoid:

- if reuse requires long-lived large KV footprints, the system is strongly pushed toward lower tiers
- once it moves there, transfer cost and locality often dominate

## 3.2 A Better Economic Decision Rule

The right decision is not “storage is cheap” or “storage is expensive.” It is:

`value_of_saved_prefill_and_decode > carrying_cost_of_state + movement_cost + miss_and_repair_penalty`

For an approximate engineering template:

`net_value ~= p_hit x C_saved - C_store - p_fetch x C_transfer - p_miss x C_fallback - C_control - C_quality`

Where:

- `p_hit` is the probability the retained state is actually reusable
- `C_saved` is the compute and latency value avoided when the hit works
- `C_store` is the cost of retaining the object in some tier for its lifetime
- `p_fetch x C_transfer` captures how often the system must move that state across PCIe, host memory, NVMe, or network
- `p_miss x C_fallback` captures the cost when the system stores state but still ends up recomputing
- `C_control` covers matching, lookup, scheduling, and orchestration
- `C_quality` captures quality loss, repair compute, or safety margin for approximate reuse

This template helps explain the papers:

- `LMCache` tries to reduce `C_transfer` and `C_control`
- `KVShare` and `SemShareKV` try to increase `p_hit`
- `PRKV` and `CentroidKV` try to reduce `C_store` and `C_transfer` for retained state
- `DroidSpeak` and `LRAgent` increase `C_quality` and `C_control`, but can make `C_saved` much larger
- `Prompt Cache` and plan caching often win by raising `p_hit` sharply on the stable parts of agent workflows

This is also the best answer so far to the “storage price is soaring” concern:

- rising storage price hurts indiscriminate long-lived retention
- but it does not kill reuse uniformly
- it pushes the field toward higher-value cache boundaries, better locality, smaller retained objects, and stronger admission control

### Tier A. GPU / HBM

Pros:

- best access performance
- lowest latency for live decode use

Cons:

- highest effective price
- strongest capacity pressure

Interpretation:

- exact long-lived persistence here is rarely scalable
- reuse usually needs lower tiers if the state lifetime is not very short

Concrete implication:

- the economic burden of using HBM as a persistence tier is usually the foregone value of GPU capacity, not a tidy storage line item

### Tier B. Host DRAM

Pros:

- lower cost than HBM
- still reasonable latency and bandwidth

Cons:

- transfer to GPU remains expensive enough to matter
- cluster-wide persistence is still non-trivial

Interpretation:

- often the first practical persistence tier for reusable KV

Concrete implication:

- DRAM-like tiers are plausible when recurrence is high and latency sensitivity is strong, but they are expensive enough that “cache everything indefinitely” is rarely a good idea

### Tier C. Local NVMe / SSD

Pros:

- much cheaper storage
- large retained-state capacity

Cons:

- transfer overhead and locality become dominant concerns

Interpretation:

- worthwhile only when reuse recurrence is strong enough or when cheaper persistent retention beats expensive recomputation clearly enough

Concrete implication:

- the storage line item is low enough to be attractive, but sustained provisioned throughput or high random-access demand can erode the advantage quickly

### Tier D. Remote / distributed storage

Pros:

- largest persistence surface
- natural fit for cross-engine or cross-service reuse

Cons:

- highest transfer and orchestration burden
- stronger locality, routing, and admission-control requirements

Interpretation:

- only worthwhile when reuse probability and compute avoided are sufficiently high, or when the serving system can route aggressively toward retained state

Concrete implication:

- object-store-like persistence is attractive for very cheap long-lived retention, but only if the system can avoid paying too often in retrieval latency, transfer, and cache misses

### Current project judgment

The current evidence suggests:

- exact reuse is most attractive when recurrence is high and state can be retained in DRAM-like tiers with good locality
- approximate and semantic reuse are only worthwhile when the additional compatibility surface outweighs the cost of extra matching, transfer, and quality risk
- cross-model reuse is only worthwhile when the saved prefill is large enough and compatibility is strong enough to keep repair cost low
- app-level modularization can make caching more worthwhile by isolating stable high-value context from dynamic cache-breaking context
- sparse-attention-enabled reuse may become attractive precisely because it reduces how much state must be retained or moved

The stronger economic reading is:

- exact prefix caching remains attractive when recurrence is high and the cache object is stable
- approximate and semantic reuse only remain worthwhile if they raise `p_hit` faster than they increase `C_control` and `C_quality`
- agent and cross-model reuse justify themselves only when the avoided prefill is very large or shared many times downstream
- sparse attention helps most when it shrinks the object enough that lower-tier storage and transfer become tolerable again

This still needs a more quantitative follow-up. Right now it is a strong qualitative judgment, not a finished cost model.

## 4. How Reuse Goes Beyond Prefix

The new project’s most important result so far is that “beyond prefix reuse” is not one move. It is several distinct moves.

### A. Approximate prefix neighborhood reuse

- `KVShare`

### B. Semantic similarity reuse

- `SemShareKV`

### C. Context-engineered prompt modules or plan reuse

- `Prompt Cache`
- `Cost-Efficient Serving of LLM Agents via Test-Time Plan Caching`
- `Don't Break the Cache`

### D. Structure-aware retained-state reuse

- `PRKV`
- `CentroidKV`

### E. Multi-context sparse reuse

- `SamKV`

### F. Cross-model partial state reuse

- `DroidSpeak`
- `LRAgent`

### G. Intra-model architectural sharing

- `HySparse`

### H. Protocol-level representation sharing

- `Q-KVComm`

That list is useful because each move has a different failure mode:

- approximation error
- semantic mismatch
- poor modular partitioning between stable and dynamic context
- cluster/centroid fidelity loss
- missing cross-context information
- cross-model incompatibility
- architectural coupling constraints
- semantic-fidelity loss in representation exchange

## 5. Context Engineering As A Reuse Signal

This is the most useful new extension beyond the original plan.

The current papers suggest that application-level context engineering may provide stronger reuse signals than model/runtime-only logic.

### What Prompt Cache adds

`Prompt Cache` is the cleanest early example.

It explicitly treats:

- system messages
- prompt templates
- reusable document context

as modular prompt segments whose attention states can be precomputed and reused.

This matters because it says:

- not all reusable boundaries need to be discovered by semantic matching
- some are explicit in application structure

### What Don't Break the Cache adds

`Don't Break the Cache` is important because it evaluates agentic prompt caching strategies directly and distinguishes:

- full context caching
- system-prompt-only caching
- caching that excludes dynamic tool results

This is highly relevant to the project because it shows that:

- cacheability depends on context composition
- dynamic tool outputs may break cacheability even when system prompts and scaffold text stay stable

### What Test-Time Plan Caching adds

`Cost-Efficient Serving of LLM Agents via Test-Time Plan Caching` is not a KV-cache paper in the narrow sense, but it is very relevant conceptually.

It suggests that some of the highest-value reusable objects in agent systems are not prompt segments alone, but:

- reusable plans
- structured intermediate reasoning templates

This raises an important possibility for the project:

- the best storage-for-computation trade may sometimes come from caching above raw KV, at the plan or execution-template level

### What LRAgent adds

`LRAgent` strengthens the connection between agent structure and KV reuse.

In multi-LoRA agent systems:

- role specialization is explicit at the application level
- most of the backbone-induced state remains shared
- only lightweight adapter-specific state needs to differ

This is an especially important example because app-level role structure directly shapes what KV can be shared.

### Current project judgment

The interplay between context engineering and KV reuse is real and should stay inside this project.

The most plausible pattern is:

1. application logic identifies stable or repeatedly consumed context pieces
2. serving/runtime layers turn those pieces into reusable KV or reusable higher-level artifacts
3. approximate, semantic, sparse, or cross-model methods widen reuse beyond the exact boundaries that app logic exposes

That means context engineering is not a separate topic. It is an upstream generator of better reuse boundaries.

## 6. Sparse Attention And Computational Sparsity

This is the newest and least stabilized part of the project, but it is already promising.

### What the current evidence suggests

`SamKV`, `NOSA`, and `HySparse` jointly suggest two distinct futures.

#### Future A. Sparse attention encourages reuse

How:

- smaller retained state
- stronger locality
- more structured selected tokens
- easier offloadability
- more explicit sharing between architectural components

This is the picture supported by:

- `NOSA`
- `HySparse`
- partially `SamKV`

#### Future B. Sparse attention reduces the need for reuse

How:

- if the active state is already much smaller and attention cost is already reduced, the marginal value of long-lived retained-state reuse can shrink

This possibility is not yet strongly contradicted by the current scope. It remains an important open question.

### Current project judgment

The most likely answer is not one-sided.

Sparse attention probably:

- reduces the need for brute-force persistence of full KV
- but increases the practicality of more structured, more selective, and more architecture-aware reuse

That makes sparse attention less a replacement for reuse than a change in what kind of reuse becomes economically sensible.

## 7. Cross-Model And Agent-Level Reuse

This branch is still evidence-thin compared with request-level reuse, but it is where the project is most forward-looking.

### Cross-model reuse

`DroidSpeak` and `LRAgent` are the strongest current signals.

Main lesson:

- KV can cross model boundaries when compatibility is strong enough
- selective recomputation or low-rank decomposition is the repair mechanism

This suggests the future competition may not only be over better caches, but over better **compatibility contracts**.

### Agent-level reuse

`Q-KVComm` is the clearest signal here.

Main lesson:

- models may exchange internal compressed representations directly
- reuse then becomes part of communication, not only caching

This is speculative, but it is a meaningful direction rather than a random edge case.

## 8. Current Best Answers To The Project Questions

### How do people maximize the trade?

By:

- externalizing exact state
- widening compatibility
- restructuring retained state
- co-designing attention and reusable state
- using application logic to expose better cache boundaries

### Is it worthwhile when storage is expensive?

Sometimes, but only when:

- recurrence is strong enough
- retained state is local enough
- transfer is cheap enough
- compute avoided is large enough
- quality risk is controlled tightly enough

This answer is still not quantitative enough.

### How does reuse go beyond prefix?

Through:

- approximation
- semantics
- context-engineered prompt modules and reusable plans
- clustering
- multi-context sparse selection
- cross-model compatibility
- intra-model sharing
- inter-agent representation exchange

### What are the tradeoffs?

- quality degradation
- compatibility constraints
- transfer overhead
- persistent-state cost
- orchestration burden
- application/framework integration burden

### How do people share across models and agents?

- cross-model reuse uses selective recomputation as repair
- agent-level exchange treats internal state as a communication object

### Does context engineering help?

Yes, likely in two ways:

- it exposes stable prompt modules such as system prompts and reusable scaffolds
- it identifies high-value intermediate artifacts that downstream agent steps or sibling agents are likely to consume

The strongest current caveat is that some of these reusable objects sit above raw KV. So the project should distinguish:

- app-level reusable objects
- runtime-level reusable KV state

while still analyzing their interaction together.

### What does the future look like?

Most likely:

- less brute-force full-state retention
- more structured, sparse, clustered, or compatibility-aware retained-state reuse
- more co-design between model architecture and serving infrastructure
- more app-level control over what gets preserved
- a gradual shift from cache object to reusable intermediate representation

## 9. What Still Needs Search

Only four search gaps still look worth spending time on.

### 1. Better storage-cost evidence

This is the biggest remaining weakness.

Need:

- current tier cost assumptions
- bandwidth and latency assumptions
- any primary-source system cost discussions from production papers

### 2. Stronger heterogeneous-model reuse evidence

Need:

- at least one convincing paper or system direction beyond same-architecture or fine-tuned-variant reuse

### 3. One or two boundary-case sparse-attention papers

Need:

- better evidence on whether sparsity mostly reduces the need for reuse or actually strengthens reusable-state architectures

### 4. One or two stronger app-logic / context-engineering papers

Need:

- better evidence on how frameworks explicitly partition stable versus dynamic context
- stronger links from reusable plans, prompts, or intermediate artifacts down to KV or prompt-cache economics

## Bottom Line

The current state of the project supports one strong conclusion:

**The most important development is not just that people can reuse KV beyond exact prefixes. It is that the field is building a ladder of broader reuse contracts, and application-level context engineering may help decide which boundaries are worth preserving before the runtime ever starts approximating them.**

That is the core story this project should keep testing and refining.
