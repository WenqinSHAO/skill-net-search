---
id: sosp23-001
title: "Efficient Memory Management for Large Language Model Serving with PagedAttention"
conference: SOSP 2023
date: 2023-10
authors:
  - name: "Woosuk Kwon"
    affiliation: ""
    is_industry: true
  - name: "Zhuohan Li"
    affiliation: ""
    is_industry: true
  - name: "Siyuan Zhuang"
    affiliation: ""
    is_industry: false
  - name: "Ying Sheng"
    affiliation: ""
    is_industry: false
  - name: "Lianmin Zheng"
    affiliation: ""
    is_industry: false
  - name: "Cody Hao Yu"
    affiliation: ""
    is_industry: true
  - name: "Joseph E. Gonzalez"
    affiliation: ""
    is_industry: false
  - name: "Hao Zhang"
    affiliation: ""
    is_industry: false
  - name: "Ion Stoica"
    affiliation: ""
    is_industry: false
topics:
  - LLM Serving
  - Distributed Systems
tags: [llm-serving, pagedattention, vllm, kv-cache, memory-management]
arxiv: "2309.06180"
url: "https://arxiv.org/abs/2309.06180"
status: analyzed
---

# Efficient Memory Management for Large Language Model Serving with PagedAttention

**SOSP 2023** | arXiv: 2309.06180

## 摘要

High throughput serving of large language models (LLMs) requires batching sufficiently many requests at a time. However, existing systems struggle because the key-value cache (KV cache) memory for each request is huge and grows and shrinks dynamically. When managed inefficiently, this memory can be significantly wasted by fragmentation and redundant duplication, limiting the batch size. To address this problem, we propose PagedAttention, an attention algorithm inspired by the classical virtual memory and paging techniques in operating systems. On top of it, we build vLLM, an LLM serving system that achieves (1) near-zero waste in KV cache memory and (2) flexible sharing of KV cache within and across requests to further reduce memory usage. Our evaluations show that vLLM improves the throughput of popular LLMs by 2-4× with the same level of latency compared to the state-of-the-art systems, such as FasterTransformer and Orca. The improvement is more pronounced with longer sequences, larger models, and more complex decoding algorithms.

## 核心贡献

- 提出 PagedAttention，将操作系统的虚拟内存分页思想引入 KV cache 管理
- 构建 vLLM 系统，实现近零 KV cache 内存浪费
- 支持请求内和跨请求的 KV cache 灵活共享
- 相比 SOTA 系统，吞吐量提升 2-4×
- 代码已开源：https://github.com/vllm-project/vllm

---
*导入自 net-research 数据库 | ID: sosp23-001*
