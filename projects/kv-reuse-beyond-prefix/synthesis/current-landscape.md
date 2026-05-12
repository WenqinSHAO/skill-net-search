# Current Landscape

## What The Repo Already Covers Well

The current shared DB and `kv-cache-serving-v2` already cover the core reuse progression well enough to start this project.

### 1. Exact reuse becomes infrastructure

Current anchors:

- `CacheGen`
- `HCache`
- `LMCache`

These papers establish that reusable KV is not just a cache-hit optimization. It often requires:

- persistence outside GPU-local execution
- explicit transfer paths
- orchestration across engines or serving boundaries

### 2. Reuse expands beyond exact prefix identity

Current anchors:

- `KVShare`
- `SemShareKV`

These papers already give the project a clean first comparison:

- exact or near-exact reuse
- approximate reuse with quality control
- semantic reuse via fuzzy matching

### 3. Reuse expands beyond one request / one model

Current anchors:

- `DroidSpeak`
- `Q-KVComm`
- `Agentix`

These papers are important because they begin to treat KV as:

- reusable across models
- reusable across workflow stages
- potentially usable as an inter-agent representation

### 4. Reuse depends on serving infrastructure

Current anchors:

- `Mooncake`
- `DualMap`
- `JITServe`

These are not pure reuse papers, but they matter because they expose the operational side of reuse:

- where the state lives
- how requests are routed toward it
- when extra storage and transfer are cheaper than extra compute

## What The Repo Does Not Yet Cover Well Enough

The current repo is still weaker on two fronts, though the first batch has improved the first gap substantially.

### 1. Sparse-attention or clustering methods that directly widen reuse

Now imported into the shared DB:

- `PRKV`
- `CentroidKV`
- `SamKV`
- `HySparse`
- `NOSA`

Why they matter here:

- `PRKV` and `CentroidKV` widen reuse or selective reuse through structured clustering or hybrid selection
- `SamKV` studies sparse attention over multiple-context KV caches, which is directly relevant to beyond-prefix reuse in RAG-like settings
- `HySparse` and `NOSA` suggest that newer sparse-attention designs may make reusable KV cheaper or more structured

### 2. Explicit cost-model evidence

The current project explains reuse architecture well, but it does not yet quantify:

- storage cost per GB across tiers
- transfer cost and latency per tier
- the compute cost actually avoided by reuse
- when storage inflation makes aggressive reuse less attractive

That needs a separate evidence pass.

### 3. Truly heterogeneous cross-model reuse

The repo now covers:

- same-engine or same-service reuse
- approximate and semantic reuse
- cross-model reuse among architecture-compatible models
- agent-level representation exchange

What it still does not cover well is reuse across more heterogeneous model families where compatibility is weaker and recomputation burden is more complex.
