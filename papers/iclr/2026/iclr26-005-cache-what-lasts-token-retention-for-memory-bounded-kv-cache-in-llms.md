---
id: iclr26-005
title: "Cache What Lasts: Token Retention for Memory-Bounded KV Cache in LLMs"
conference: "ICLR 2026"
date: "2026-03"
authors:
  - name: "Ngoc Bui"
    affiliation: ""
    is_industry: false
  - name: "Shubham Sharma"
    affiliation: ""
    is_industry: false
  - name: "Simran Lamba"
    affiliation: ""
    is_industry: false
  - name: "Saumitra Mishra"
    affiliation: ""
    is_industry: false
  - name: "Rex Ying"
    affiliation: ""
    is_industry: false
topics:
  - LLM Serving
  - Caching
tags:
  - llm-serving
  - caching
arxiv: ""
url: "https://openreview.net/forum?id=qCaq3jGb0S"
status: analyzed
---
# Cache What Lasts: Token Retention for Memory-Bounded KV Cache in LLMs

## 摘要

Memory and computation remain core bottlenecks in long-horizon LLM inference due to the quadratic cost of self-attention and the ever-growing key-value (KV) cache. Existing strategies for memory-bounded inference, such as quantization, offloading, or heuristic KV eviction, either incur high orchestration costs or rely on unreliable attention-based proxies of importance. We propose TRIM-KV, a novel approach that learns each token’s intrinsic importance at creation time via a lightweight retention gate. Each gate predicts a scalar retention score that decays over time, reflecting the long-term utility of the token for a specific layer and head. Tokens with low scores are evicted when the memory budget is exceeded, ensuring that the cache always contains the most critical tokens. TRIM-KV is trained efficiently through distillation from a frozen LLM combined with a capacity loss, requiring only gate fine-tuning and adding negligible inference overhead. Across mathematical reasoning (GSM8K, MATH-500, AIME24), procedural generation (LongProc), conversational long-memory benchmarks (LongMemEval), and long-context understanding (LongBenchV2 and SCBench), TRIM-KV consistently outperforms strong eviction and learnable retrieval baselines, especially in low-memory regimes. Remarkably, it even surpasses full-cache models in some settings, showing that selective retention can serve as a form of regularization, suppressing noise from uninformative tokens. Qualitative analyses further reveal that learned retention scores align with human intuition, naturally recovering heuristics such as sink tokens, sliding windows, and gist compression without explicit design. Beyond efficiency, retention scores provide insights into layer- and head-specific roles, suggesting a new path toward LLM interpretability.

## Problem

[(待补充)]

## Method

[(待补充)]

## Evaluation

[(待补充)]

## Limitations

[(待补充)]
