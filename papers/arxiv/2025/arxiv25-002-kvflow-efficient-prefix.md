---
id: arxiv25-002
title: "KVFlow: Efficient Prefix Caching for Accelerating LLM-Based Multi-Agent Workflows"
conference: arXiv 2025
date: 2025-07
authors:
  - name: "Zaifeng Pan"
    affiliation: ""
    is_industry: false
  - name: "Ajjkumar Patel"
    affiliation: ""
    is_industry: false
  - name: "Zhengding Hu"
    affiliation: ""
    is_industry: false
  - name: "Yipeng Shen"
    affiliation: ""
    is_industry: false
  - name: "Yue Guan"
    affiliation: ""
    is_industry: false
  - name: "Wan-Lu Li"
    affiliation: ""
    is_industry: false
  - name: "Lianhui Qin"
    affiliation: ""
    is_industry: false
  - name: "Yida Wang"
    affiliation: ""
    is_industry: false
  - name: "Yufei Ding"
    affiliation: ""
    is_industry: false
topics:
  - LLM Serving
  - Distributed Systems
tags: [kvflow, prefix-caching, multi-agent, workflow-aware]
arxiv: "2507.07400"
url: "https://arxiv.org/abs/2507.07400"
status: analyzed
---

# KVFlow: Efficient Prefix Caching for Accelerating LLM-Based Multi-Agent Workflows

**arXiv 2025** | arXiv: 2507.07400

## 摘要

Large language model (LLM) based agentic workflows have become a popular paradigm for coordinating multiple specialized agents to solve complex tasks. To improve serving efficiency, existing LLM systems employ prefix caching to reuse key-value (KV) tensors corresponding to agents' fixed prompts, thereby avoiding redundant computation across repeated invocations. However, current systems typically evict KV caches using a Least Recently Used (LRU) policy, which fails to anticipate future agent usage and often discards KV caches shortly before their reuse. This leads to frequent cache misses and substantial recomputation or swapping overhead. We present KVFlow, a workflow-aware KV cache management framework tailored for agentic workloads. KVFlow abstracts the agent execution schedule as an Agent Step Graph and assigns each agent a steps-to-execution value that estimates its temporal proximity to future activation. These values guide a fine-grained eviction policy at the KV node level, allowing KVFlow to preserve entries likely to be reused and efficiently manage shared prefixes in tree-structured caches. Moreover, KVFlow introduces a fully overlapped KV prefetching mechanism, which proactively loads required tensors from CPU to GPU in background threads for agents scheduled in the next step, thereby avoiding cache miss stalls during generation. Compared to SGLang with hierarchical radix cache, KVFlow achieves up to 1.83× speedup for single workflows with large prompts, and up to 2.19× speedup for scenarios with many concurrent workflows.

## 核心贡献

- 提出 KVFlow，workflow-aware KV cache 管理框架
- Agent Step Graph 抽象，为每个 agent 分配 steps-to-execution 值
- 细粒度 KV 节点级驱逐策略，保留即将被复用的条目
- 全重叠 KV 预取机制，后台线程提前加载张量
- 相比 SGLang 分层 radix 缓存：单工作流 1.83× 加速，多并发工作流 2.19× 加速

---
*导入自 net-research 数据库 | ID: arxiv25-002*
