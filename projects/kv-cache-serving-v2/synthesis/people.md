# People

## Goal

Identify who is repeatedly driving the field:

- by defining the right problem early
- by building foundational mechanisms
- by connecting system design to real deployment constraints

This section is worth doing, but it needs a stricter method than the earlier synthesis layers because the current shared paper database still has sparse affiliation fields. That means the first version should separate:

- what the current local DB can support directly
- what will require explicit enrichment from paper frontmatter or official pages

## What To Track

For each author or institution cluster, ask:

1. Which branch do they influence most?
2. Are they early problem definers, mechanism builders, or platform builders?
3. Do they repeatedly publish in one coherent line, or make one isolated contribution?
4. Are they shaping academic benchmarks or real production practices?

## Current Limitation

Many shared paper records have author names but missing affiliations.

That means:

- author-level recurrence can be tracked now
- affiliation-level claims are still weak
- institution clustering should remain provisional until the metadata is enriched

So the right next step is not to force a polished people ranking. It is to prepare a disciplined extraction method.

The project is now past that earlier placeholder stage. A first evidence-based map is possible, but only if we keep a strict distinction between:

- recurring author lines that are directly visible in the scoped papers
- institution clusters that are verified from source pages
- weaker hypotheses that still need more metadata enrichment

## Extraction Method

For each in-scope paper, capture:

1. authors
2. affiliations
3. whether the work is mainly:
   - problem-definition
   - mechanism design
   - system architecture
   - production/deployment
4. which branch of the architecture map it influences most

Then build two views:

- recurring authors across branches
- recurring institutions across contribution styles

## Verified Recurring Author Lines

### 1. The UChicago LMCache / model-native-state line

This is currently the clearest recurring author cluster in scope.

Repeatedly visible names include:

- `Yuhan Liu`
- `Yihua Cheng`
- `Jiayi Yao`
- `Kuntai Du`
- `Yuyang Huang`
- `Junchen Jiang`
- often with `Shan Lu`

Directly visible in the current local DB:

- `CacheGen`
- `LMCache`
- `DroidSpeak`
- related neighboring work such as `CacheBlend`

Contribution style:

- turning KV from local cache state into reusable or transferable system state
- strong emphasis on compression/streaming, external cache layers, and cross-model reuse

Interpretation:

- this is one of the most coherent author lines in the project
- it is not one isolated paper; it is a sustained program around model-native state reuse and movement

### 2. The Microsoft efficient-AI / disaggregation line

This line is anchored by recurring Microsoft systems researchers, especially:

- `Esha Choukse`
- `Madan Musuvathi`
- plus recurring collaborators such as `Chaojie Zhang`, `Íñigo Goiri`, `Saeed Maleki`, and `Ricardo Bianchini`

Directly visible in scope:

- `Splitwise`
- `DroidSpeak`

Contribution style:

- cross-stack efficient AI systems
- phase disaggregation
- efficient model communication and reuse at deployment scale

Interpretation:

- this line is less about one narrow KV mechanism and more about repeatedly redefining the systems boundary around inference efficiency

### 3. The Peking University DistServe line

This is the clearest phase-disaggregation author cluster in the current project.

Core recurring names:

- `Yinmin Zhong`
- `Xuanzhe Liu`
- `Xin Jin`

Directly visible in scope:

- `DistServe`
- plus neighboring disaggregation/distributed-inference work in the broader local DB

Contribution style:

- service decomposition under TTFT/TPOT pressure
- bandwidth-aware phase placement
- strong systems framing around distributed inference architecture

Interpretation:

- this line looks like one of the field’s strongest academic centers for phase-aware LLM serving architecture

### 4. The Tsinghua / Moonshot platform line

Core recurring names in scope:

- `Mingxing Zhang`
- `Yongwei Wu`
- `Weimin Zheng`

with deployment-facing coauthors from `Moonshot AI`.

Directly visible in scope:

- `Mooncake`
- `Prefill-as-a-Service`

Contribution style:

- production-oriented KV-centric platform design
- disaggregated serving with strong operational grounding

Interpretation:

- this line is especially important because it closes the gap between architecture paper and deployed serving platform

## Verified Institution Clusters

### University of Chicago

Verified from departmental pages and project pages.

Current role in this project:

- strongest recurring line on KV as reusable, transferable, and externally managed state
- especially strong in:
  - KV compression/streaming
  - cross-query reuse
  - external cache layers
  - cross-model reuse

Best read:

- one of the clearest drivers of the "model-native state" view of KV

### Microsoft Research / Azure Research

Verified from Microsoft Research pages.

Current role in this project:

- cross-stack efficient AI systems
- phase splitting and deployment architecture
- newer reuse and communication work around multiple-model inference

Best read:

- one of the strongest industrial problem-defining groups in this space

### Peking University

Verified from USENIX/author pages for `DistServe`.

Current role in this project:

- strong academic center for disaggregated LLM serving architecture
- especially phase-aware service decomposition under latency constraints

Best read:

- a major academic driver of the prefill/decode disaggregation story

### Tsinghua University + Moonshot AI

Verified from FAST and Tsinghua sources for `Mooncake`, plus related scoped papers.

Current role in this project:

- KV-centric serving platform design
- strong productization signal
- tighter integration between architecture and deployment reality

Best read:

- a high-signal joint academia/industry line for platform-scale KV serving

## Provisional Institution Clusters

### Platform / production-oriented systems

Likely institutions to track:

- industrial serving teams
- cloud providers
- labs tied to deployed serving platforms

Questions:

- who is turning KV ideas into operational architecture?

### Foundational systems / architecture groups

Likely institutions to track:

- systems groups producing PagedAttention, DistServe, Mooncake-like work

Questions:

- who repeatedly shifts the architectural boundary of the field?

### Compression / retention / long-context mechanism groups

Questions:

- who repeatedly defines benchmark-driving KV compression or eviction ideas?

### Agentic / workflow-aware groups

Questions:

- who is reframing KV around programs, workflows, and cross-model communication?

## Contribution-Style Reading

The current evidence suggests four contribution styles that matter more than raw paper count.

### 1. Problem definers and boundary shifters

These are the people and labs that repeatedly expose a new systems boundary:

- `Splitwise`
- `DistServe`
- `Mooncake`
- `Prefill-as-a-Service`

This cluster matters because it decides where the field should look next, not just how to optimize a fixed interface.

### 2. Model-native state builders

These are the lines that repeatedly treat KV as transferable or reusable intermediate state:

- `CacheGen`
- `LMCache`
- `DroidSpeak`

This is currently the most coherent recurring author program in the scope.

### 3. Reuse-compatibility expanders

These are the papers that widen what counts as reusable state:

- `KVShare`
- `SemShareKV`
- `DroidSpeak`
- `Q-KVComm`

Here the important contribution is not only efficiency, but changing the compatibility contract itself.

### 4. Memory-budget mechanism builders

These are mostly individual-paper or looser clusters rather than one dominant recurring-author program in the current scope:

- `Ada-KV`
- `KeyDiff`
- `TRIM-KV`
- `PolarQuant`
- `ChunkKV`
- `KVTC`

Interpretation:

- this branch is rich methodologically
- but, based on the current scope, it has fewer clearly recurring people/labs than the disaggregation and reuse branches

## Output We Eventually Want

- author clusters by branch
- institution clusters by contribution style
- a shortlist of people/labs who consistently identify the next important problem early

## Current Shortlist

If the question is who looks especially important under the current evidence, the strongest shortlists are:

- for **phase disaggregation and serving architecture**:
  - the `DistServe` line at Peking University
  - the `Splitwise` / `DroidSpeak` Microsoft efficient-AI line
  - the `Mooncake` Tsinghua + Moonshot line

- for **model-native state reuse as a sustained research program**:
  - the `CacheGen` / `LMCache` / `DroidSpeak` line centered around UChicago

- for **speculative future direction toward protocol-level KV use**:
  - `DroidSpeak`
  - `Q-KVComm`
  - adjacent workflow papers like `Agentix`

## Remaining Gaps

This people map is now meaningful, but it is still incomplete.

The main remaining weaknesses are:

- some affiliation fields in the shared DB are still blank
- the retention/compression branch needs more direct institution enrichment
- some newer arXiv papers in the scope have only partial metadata

So the right standard is:

- strong on recurring lines and major institution clusters
- cautious on exact lab rankings beyond the best-supported groups above
