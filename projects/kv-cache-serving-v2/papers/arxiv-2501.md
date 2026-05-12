# arxiv-2501 — Q-KVComm

## Why it matters in this project

Q-KVComm matters because it extends the project from reuse for serving efficiency into KV as an agent-to-agent communication representation.

## Architectural role

**Role**: representation-based communication protocol for agents.

Architecturally, it is not merely a cache-sharing optimization inside a serving engine. It proposes that agents may exchange compressed KV representations directly instead of raw text.

## Benchmarking structure

### Scenario

- multi-agent LLM communication
- cross-agent transmission of internal representations

### Workload shape

- conversational QA
- multi-hop reasoning
- heterogeneous or different-sized models

### Metrics

- compression ratio
- semantic fidelity / coherence quality
- robustness across model sizes and task types

## Comparison use

Compare Q-KVComm with:

- DroidSpeak
- KVShare
- SemShareKV

The key distinction is:

- KV reused for serving
- KV transmitted as communication

## Project takeaway

Q-KVComm supports the strongest version of the project’s reuse thesis:

**KV may become an inter-agent medium, not only an inference cache.**
