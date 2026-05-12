---
id: eurosys25-002
title: "CacheBlend: Fast Large Language Model Serving for RAG with Cached Knowledge Fusion"
conference: EuroSys 2025
date: 2025-05
authors:
  - name: "Jiayi Yao"
    affiliation: ""
    is_industry: false
  - name: "Hanchen Li"
    affiliation: ""
    is_industry: false
  - name: "Yuhan Liu"
    affiliation: ""
    is_industry: false
  - name: "Siddhant Ray"
    affiliation: ""
    is_industry: false
  - name: "Yihua Cheng"
    affiliation: ""
    is_industry: false
  - name: "Qizheng Zhang"
    affiliation: ""
    is_industry: false
  - name: "Kuntai Du"
    affiliation: ""
    is_industry: false
  - name: "Shan Lu"
    affiliation: ""
    is_industry: false
  - name: "Junchen Jiang"
    affiliation: ""
    is_industry: false
topics:
  - LLM Serving
  - Distributed Systems
tags: [cacheblend, rag, kv-cache, knowledge-fusion]
arxiv: "2405.16444"
url: "https://arxiv.org/abs/2405.16444"
status: analyzed
---

# CacheBlend: Fast Large Language Model Serving for RAG with Cached Knowledge Fusion

**EuroSys 2025** | arXiv: 2405.16444

## 摘要

Large language models (LLMs) often incorporate multiple text chunks in their inputs to provide the necessary contexts. To speed up the prefill of the long LLM inputs, one can pre-compute the KV cache of a text and re-use the KV cache when the context is reused as the prefix of another LLM input. However, the reused text chunks are not always the input prefix, which makes precomputed KV caches not directly usable since they ignore the text's cross-attention with the preceding texts. Thus, the benefits of reusing KV caches remain largely unrealized. This paper tackles just one challenge: when an LLM input contains multiple text chunks, how to quickly combine their precomputed KV caches in order to achieve the same generation quality as the expensive full prefill (i.e., without reusing KV cache)? This challenge naturally arises in retrieval-augmented generation (RAG) where the input is supplemented with multiple retrieved texts as the context. We present CacheBlend, a scheme that reuses the precomputed KV caches, regardless prefix or not, and selectively recomputes the KV values of a small subset of tokens to partially update each reused KV cache. In the meantime, the small extra delay for recomputing some tokens can be pipelined with the retrieval of KV caches within the same job, allowing CacheBlend to store KV caches in slower devices with more storage capacity while retrieving them without increasing the inference delay. By comparing CacheBlend with the state-of-the-art KV cache reusing schemes on three open-source LLMs of various sizes and four popular benchmark datasets of different tasks, we show that CacheBlend reduces time-to-first-token (TTFT) by 2.2-3.3x and increases the inference throughput by 2.8-5x from full KV recompute without compromising generation quality.

## 核心贡献

- 提出 CacheBlend，支持非前缀 KV cache 复用（特别适用于 RAG 场景）
- 选择性重计算少量 token 的 KV 值，部分更新复用的 KV cache
- 重计算延迟可与 KV cache 检索流水线化，允许使用更慢但更大容量的存储
- TTFT 降低 2.2-3.3×，推理吞吐量提升 2.8-5×
- 不损失生成质量
- 代码已开源

---
*导入自 net-research 数据库 | ID: eurosys25-002*
