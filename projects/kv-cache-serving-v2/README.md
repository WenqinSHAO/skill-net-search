# KV Cache Serving & Sharing v2

## Intent

This project studies how KV cache management changes the design space of LLM inference systems.

The main goal is not to collect every remotely related paper. The goal is to understand:

- how systems place, move, compress, evict, or reuse KV state
- which techniques operate at the tensor/block level versus the serving-system level
- where the main tradeoffs are across latency, memory footprint, throughput, and quality

## Scope

In scope:

- KV cache reuse and sharing across requests, sessions, models, or agents
- KV cache compression, coding, quantization, and eviction
- tiered memory, swapping, and disaggregated KV architectures
- serving-system mechanisms that directly expose or depend on KV behavior

Borderline but often useful:

- scheduling work that is only interesting because of KV constraints
- long-context methods that materially change KV footprint or access pattern

Out of scope by default:

- generic transformer efficiency papers with no meaningful KV angle
- broad agent-system papers unless KV state is central to the design
- general network or systems papers without a clear connection to KV-backed LLM serving

## Seed Paper Set

The list below is the starting set carried over from the earlier pilot. It is a seed set, not a final canonical scope.

### Core systems and architectures

- `sosp23-001` PagedAttention
- `arxiv23-002` CacheGen
- `isca24-001` Splitwise
- `osdi24-001` InfiniGen
- `osdi24-002` DistServe
- `fast25-001` Mooncake
- `eurosys25-001` HCache
- `atc25-001` KVCache in the Wild
- `nsdi26-008` DroidSpeak

### Reuse and sharing

- `arxiv25-001` LMCache
- `arxiv25-002` KVFlow
- `arxiv25-003` Tokencake
- `arxiv25-004` KVShare
- `arxiv25-005` SemShareKV
- `arxiv-2501` Q-KVComm

### Compression, eviction, and storage efficiency

- `iclr26-001` KVTC
- `iclr26-002` IceCache
- `iclr26-004` LouisKV
- `iclr26-005` TRIM-KV / Cache What Lasts
- `neurips25-003` PolarQuant
- `neurips25-006` Ada-KV
- `neurips25-007` KeyDiff
- `neurips25-008` HiFC
- `neurips25-011` ChunkKV
- `arxiv26-003` Joint Encoding of KV-Cache Blocks

### Related serving context

- `arxiv26-001` Prefill-as-a-Service
- `arxiv26-002` DualMap
- `sigcomm25-003` SCX
- `nsdi26-020` JITServe
- `nsdi26-038` FlexLLM
- `nsdi26-049` Seshat
- `nsdi26-061` Agentix

## Why These Papers

- The first group anchors the end-to-end system designs.
- The second group isolates reuse and communication of KV state.
- The third group captures memory-pressure responses: compression, quantization, eviction, retrieval, tiering, and storage.
- The fourth group helps explain when KV behavior is first-order for serving policy, prefill service design, or distributed cache placement rather than a local optimization.

## Open Curation Questions

- Which long-context or attention papers are truly in scope versus merely adjacent?
- Should multi-agent KV communication be treated as a subtopic of reuse, or as a separate communication layer?
- Which papers are best viewed as production serving systems versus mechanism papers?

## Working Rule

This `v2` space is the clean project surface for future work. The earlier `kv-cache-serving` project is preserved only as raw source material.
