---
id: arxiv25-008
title: "Sparse Attention Across Multiple-Context KV Cache"
conference: "arXiv 2025"
date: "2025-03"
authors:
  - name: "Ziyi Cao"
    affiliation: ""
    is_industry: false
  - name: "Qingyi Si"
    affiliation: ""
    is_industry: false
  - name: "Jingbin Zhang"
    affiliation: ""
    is_industry: false
  - name: "Bingquan Liu"
    affiliation: ""
    is_industry: false
topics:
  - LLM Serving
  - Learning-based Systems
tags:
  - llm-serving
  - learning-based-systems
arxiv: "2508.11661"
url: "https://ojs.aaai.org/index.php/AAAI/article/view/40266"
status: analyzed
---
# Sparse Attention Across Multiple-Context KV Cache

## 摘要

Reusing historical KV cache has become a mainstream approach for improving long-sequence inference efficiency, and sparse attention can further enhance throughput by selecting the most relevant KV cache. Existing methods, however, are limited to single-context scenarios with causal-attention dependencies. In retrieval-augmented generation, each document context is computed and stored independently as multiple-context KV cache, lacking cross-attention between contexts. SamKV is the first exploration of attention sparsification for multiple-context KV cache. It accounts for complementary information from other contexts when sparsifying one context and then locally recomputes the sparsified information. Experiments show that SamKV compresses sequence length to 15% without accuracy degradation compared with full-recomputation baselines, significantly improving throughput in multi-context RAG scenarios.

## Problem

[(待补充)]

## Method

[(待补充)]

## Evaluation

[(待补充)]

## Limitations

[(待补充)]
