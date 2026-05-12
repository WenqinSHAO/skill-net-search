---
id: arxiv25-003
title: "Tokencake: A KV-Cache-centric Serving Framework for LLM-based Multi-Agent Applications"
conference: arXiv 2025
date: 2025-10
authors:
  - name: "Zhuohang Bian"
    affiliation: ""
    is_industry: false
  - name: "Feiyang Wu"
    affiliation: ""
    is_industry: false
  - name: "Teng Ma"
    affiliation: ""
    is_industry: false
  - name: "Youwei Zhuo"
    affiliation: ""
    is_industry: false
topics:
  - LLM Serving
  - Distributed Systems
tags: [tokencake, kv-cache, multi-agent, agent-serving]
arxiv: "2510.18586"
url: "https://arxiv.org/abs/2510.18586"
status: analyzed
---

# Tokencake: A KV-Cache-centric Serving Framework for LLM-based Multi-Agent Applications

**arXiv 2025** | arXiv: 2510.18586

## 摘要

Large Language Models (LLMs) are increasingly deployed in complex multi-agent applications that use external function calls. This workload creates severe performance challenges for the KV Cache: space contention leads to the eviction of critical agents' caches and time underutilization leaves the cache of agents stalled on long-running tool calls idling in GPU memory. We present Tokencake, a KV-Cache-centric serving framework that co-optimizes scheduling and memory management with an agent-aware design. Tokencake's Space Scheduler uses dynamic memory partitioning to shield critical agents from contention, while its Time Scheduler employs a proactive offload and predictive upload mechanism to repurpose GPU memory during function call stalls. Our evaluation on representative multi-agent benchmarks shows that Tokencake can reduce end-to-end latency by over 47.06%, improve effective GPU memory utilization by up to 16.9% compared to vLLM.

## 核心贡献

- 提出 Tokencake，KV-Cache-centric 的多 Agent 服务框架
- Space Scheduler：动态内存分区，保护关键 agent 免受竞争
- Time Scheduler：主动 offload + 预测性 upload，利用 tool call 暂停期
- 相比 vLLM：端到端延迟降低 > 47%，GPU 内存利用率提升 up to 16.9%
- 针对有外部函数调用的多 agent 工作负载优化

---
*导入自 net-research 数据库 | ID: arxiv25-003*
