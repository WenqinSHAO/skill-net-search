---
id: arxiv23-001
title: "SGLang: Efficient Execution of Structured Language Model Programs"
conference: arXiv 2023
date: 2023-12
authors:
  - name: "Lianmin Zheng"
    affiliation: ""
    is_industry: false
  - name: "Liangsheng Yin"
    affiliation: ""
    is_industry: false
  - name: "Zhiqiang Xie"
    affiliation: ""
    is_industry: false
  - name: "Chuyue Sun"
    affiliation: ""
    is_industry: false
  - name: "Jeff Huang"
    affiliation: ""
    is_industry: false
  - name: "Cody Hao Yu"
    affiliation: ""
    is_industry: true
  - name: "Shiyi Cao"
    affiliation: ""
    is_industry: false
  - name: "Christos Kozyrakis"
    affiliation: ""
    is_industry: false
  - name: "Ion Stoica"
    affiliation: ""
    is_industry: false
  - name: "Joseph E. Gonzalez"
    affiliation: ""
    is_industry: false
  - name: "Clark Barrett"
    affiliation: ""
    is_industry: false
  - name: "Ying Sheng"
    affiliation: ""
    is_industry: false
topics:
  - LLM Serving
  - Distributed Systems
tags: [sglang, radix-attention, kv-cache, structured-programs]
arxiv: "2312.07104"
url: "https://arxiv.org/abs/2312.07104"
status: analyzed
---

# SGLang: Efficient Execution of Structured Language Model Programs

**arXiv 2023** | arXiv: 2312.07104

## 摘要

Large language models (LLMs) are increasingly used for complex tasks that require multiple generation calls, advanced prompting techniques, control flow, and structured inputs/outputs. However, efficient systems are lacking for programming and executing these applications. We introduce SGLang, a system for efficient execution of complex language model programs. SGLang consists of a frontend language and a runtime. The frontend simplifies programming with primitives for generation and parallelism control. The runtime accelerates execution with novel optimizations like RadixAttention for KV cache reuse and compressed finite state machines for faster structured output decoding. Experiments show that SGLang achieves up to 6.4× higher throughput compared to state-of-the-art inference systems on various large language and multi-modal models on tasks including agent control, logical reasoning, few-shot learning benchmarks, JSON decoding, retrieval-augmented generation pipelines, and multi-turn chat.

## 核心贡献

- 提出 SGLang 系统，包含前端语言和运行时
- RadixAttention：基于基树（radix tree）的 KV cache 复用机制
- 压缩有限状态机加速结构化输出解码
- 相比 SOTA 推理系统，吞吐量提升高达 6.4×
- 代码已开源：https://github.com/sgl-project/sglang

---
*导入自 net-research 数据库 | ID: arxiv23-001*
