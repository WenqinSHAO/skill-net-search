---
id: arxiv25-004
title: "KVShare: An LLM Service System with Efficient and Effective Multi-Tenant KV Cache Reuse"
conference: arXiv 2025
date: 2025-03
authors:
  - name: "Huan Yang"
    affiliation: ""
    is_industry: false
  - name: "Renji Zhang"
    affiliation: ""
    is_industry: false
  - name: "Mingzhe Huang"
    affiliation: ""
    is_industry: false
  - name: "Weijun Wang"
    affiliation: ""
    is_industry: false
  - name: "Yin Tang"
    affiliation: ""
    is_industry: false
  - name: "Yuanchun Li"
    affiliation: ""
    is_industry: false
  - name: "Yunxin Liu"
    affiliation: ""
    is_industry: false
  - name: "Deyu Zhang"
    affiliation: ""
    is_industry: false
topics:
  - LLM Serving
  - Distributed Systems
tags: [kvshare, multi-tenant, kv-cache-reuse]
arxiv: "2503.16525"
url: "https://arxiv.org/abs/2503.16525"
status: analyzed
---

# KVShare: An LLM Service System with Efficient and Effective Multi-Tenant KV Cache Reuse

**arXiv 2025** | arXiv: 2503.16525

## 摘要

Recent advances in long-text understanding have pushed the context length of large language models (LLMs) up to one million tokens. It boosts LLMs's accuracy and reasoning capacity but causes exorbitant computational costs and unsatisfactory Time to First Token (TTFT). KV cache reuse, which reuses the exact same KV cache of prefixes and templates or shares similar ones but with extra selective recomputation, offers a promising way to tackle this issue. However, prior studies overlook the cross-request KV reuse and the attention deviations introduced by new tokens during the decoding stage. In this paper, we present a KV cache management module that shares the KV cache across requests under multi-tenant scenarios without sacrificing model accuracy. Our system, KVShare, enables accurate and efficient LLM serving by 1) a Dual-Stage High Deviation algorithm (DHD) that conditionally selects a small portion of KV cache to be recomputed during both prefill and decode phases, and 2) a cache-aware scheduler that prioritizes requests based on their KV cache hit rates and orchestrates continuous batching to achieve enhanced system efficiency and faster TTFT. Multi-task experiments conducted on models such as Qwen2.5-7B,Llama3.1-8B and Yi1.5-9B demonstrate that KVShare reduces TTFT by up to 9.39x and increases 1.2x of the throughput compared to the full KV recompute. Moreover, KVShare achieves 20.38% boost in terms of accuracy compared to SOTA methods.

## 核心贡献

- 提出 KVShare，支持多租户场景下的跨请求 KV cache 复用
- Dual-Stage High Deviation (DHD) 算法：选择性重计算少量 KV cache
- cache-aware 调度器：基于 KV cache 命中率优先级排序
- TTFT 降低 up to 9.39×，吞吐量提升 1.2×
- 相比 SOTA 方法，准确率提升 20.38%

---
*导入自 net-research 数据库 | ID: arxiv25-003*
