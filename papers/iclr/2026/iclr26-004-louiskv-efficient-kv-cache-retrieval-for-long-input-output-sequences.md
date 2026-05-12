---
id: iclr26-004
title: "LouisKV: Efficient KV Cache Retrieval for Long Input-Output Sequences"
conference: "ICLR 2026"
date: "2026-03"
authors:
  - name: "Wenbo Wu"
    affiliation: ""
    is_industry: false
  - name: "Qingyi Si"
    affiliation: ""
    is_industry: false
  - name: "Xiurui Pan"
    affiliation: ""
    is_industry: false
  - name: "Ye Wang"
    affiliation: ""
    is_industry: false
  - name: "Jie Zhang"
    affiliation: ""
    is_industry: false
topics:
  - LLM Serving
  - Caching
  - Distributed Systems
tags:
  - llm-serving
  - caching
  - distributed-systems
arxiv: ""
url: "https://openreview.net/forum?id=6RJ8fZwm4P"
status: analyzed
---
# LouisKV: Efficient KV Cache Retrieval for Long Input-Output Sequences

## 摘要

While Key-Value (KV) cache succeeds in reducing redundant computations in auto-regressive models, it introduces significant memory overhead, limiting its practical deployment in long-sequence scenarios. Existing KV retrieval methods attempt to mitigate this by dynamically retaining only a subset of KV entries on the GPU. However, they still suffer from notable efficiency and accuracy bottlenecks due to per-token retrieval and coarse-grained page-level KV management strategy, especially in long-output reasoning scenarios. With the emergence of large reasoning models, efficiently handling such scenarios has become increasingly important. To address this issue, we present two key observations: (1) critical KVs exhibit strong temporal locality during decoding, and (2) these KVs exhibit distinct distribution patterns across the input prompt and the generated output. Building on these observations, we propose LouisKV, an efficient KV cache retrieval framework designed for various long-sequence scenarios. Specifically, LouisKV introduces a semantic-aware retrieval strategy that leverages temporal locality to trigger retrieval only at semantic boundaries, drastically reducing computation and data transfer overhead. LouisKV also designs a decoupled, fine-grained management scheme that tailors differentiated strategies for input and output sequences to create retrieval units that better match the model's attention patterns, thereby enabling the precise identification of critical KVs. Furthermore, to boost system efficiency, LouisKV incorporates several kernel-level optimizations, including custom Triton and CUDA kernels to accelerate the KV clustering and retrieval. Evaluation results show that LouisKV achieves up to 4.7× speedup over state-of-the-art KV retrieval methods while maintaining near-lossless accuracy across diverse long-sequence tasks, including long-input short-output, short-input long-output, and long-input long-output scenarios.

## Problem

[(待补充)]

## Method

[(待补充)]

## Evaluation

[(待补充)]

## Limitations

[(待补充)]
