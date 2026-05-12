---
id: arxiv25-005
title: "SemShareKV: Efficient KVCache Sharing for Semantically Similar Prompts via Token-Level LSH Matching"
conference: arXiv 2025
date: 2025-09
authors:
  - name: "Xinye Zhao"
    affiliation: ""
    is_industry: false
  - name: "Spyridon Mastorakis"
    affiliation: ""
    is_industry: false
topics:
  - LLM Serving
  - Distributed Systems
tags: [semsharekv, semantic-similarity, kv-cache-sharing, lsh]
arxiv: "2509.24832"
url: "https://arxiv.org/abs/2509.24832"
status: analyzed
---

# SemShareKV: Efficient KVCache Sharing for Semantically Similar Prompts via Token-Level LSH Matching

**arXiv 2025** | arXiv: 2509.24832

## 摘要

As large language models (LLMs) continue to scale, the memory footprint of key-value (KV) caches during inference has become a significant bottleneck. Existing approaches primarily focus on compressing KV caches within a single prompt or reusing shared prefixes or frequently ocurred text segments across prompts. However, such strategies are limited in scenarios where prompts are semantically similar but lexically different, which frequently occurs in tasks such as multi-document summarization and conversational agents. We propose \textit{SemShareKV}, a KV cache sharing and compression framework that accelerates LLM inference by reusing KVCache in semantically similar prompts. Instead of relying on exact token matches, SemShareKV applies fuzzy token matching using locality-sensitive hashing (LSH) on token embeddings and incorporates Rotary Position Embedding (RoPE) to better preserve positional information. By selectively reusing relevant key-value pairs from a reference prompt's cache, SemShareKV reduces redundant computation while maintaining output quality. Experiments on diverse summarization datasets show up to 6.25$\times$ speedup and 42\% lower GPU memory usage with 5k tokens input, with negligible quality degradation. These results highlight the potential of semantic-aware cache sharing for efficient LLM inference.

## 核心贡献

- 提出 SemShareKV，基于语义相似性的 KV cache 共享框架
- 使用局部敏感哈希（LSH）进行 token 级模糊匹配
- 结合 RoPE 位置编码更好地保留位置信息
- 相比精确 token 匹配，支持语义相似但词汇不同的 prompt 复用
- 最高 6.25× 加速，GPU 内存降低 42%（5k tokens 输入）
- 生成质量损失可忽略

---
*导入自 net-research 数据库 | ID: arxiv25-004*