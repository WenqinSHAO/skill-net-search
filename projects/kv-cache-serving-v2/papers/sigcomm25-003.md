# sigcomm25-003 — SCX

## Why it matters in this project

SCX matters because it brings confidentiality into the KV-serving design space while still treating KV encoding as a systems primitive.

## Architectural role

**Role**: stateless secure KV encoding layer for cloud-scale serving.

It is not only a security add-on. It changes how intermediate KV state can be externalized and served under confidentiality constraints.

## Benchmarking structure

### Scenario

- cloud-scale confidential transformer serving

### Workload shape

- serving where intermediate KV state cannot be trusted as plain internal memory

### Metrics

- serving overhead under secure encoding
- scalability under confidential serving assumptions

## Comparison use

Compare SCX with:

- LMCache
- CacheGen
- KVTC

The key question is what changes when encoded/externalized KV must also remain confidential.

## Project takeaway

SCX is useful because it reminds the project that once KV becomes infrastructure, **security properties become architectural properties too**.
