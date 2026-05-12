---
id: arxiv26-002
title: "DualMap: Enabling Both Cache Affinity and Load Balancing for Distributed LLM Serving"
conference: arXiv 2026
date: 2026-02
authors:
  - name: "Ying Yuan"
    affiliation: ""
    is_industry: false
  - name: "Pengfei Zuo"
    affiliation: ""
    is_industry: false
  - name: "Bo Wang"
    affiliation: ""
    is_industry: false
  - name: "Zhangyu Chen"
    affiliation: ""
    is_industry: false
  - name: "Zhipeng Tan"
    affiliation: ""
    is_industry: false
  - name: "Zhou Yu"
    affiliation: ""
    is_industry: false
topics:
  - LLM Serving
  - Distributed Systems
tags: [dualmap, cache-affinity, load-balancing, distributed-serving]
arxiv: "2602.06502"
url: "https://arxiv.org/abs/2602.06502"
status: analyzed
---

# DualMap: Enabling Both Cache Affinity and Load Balancing for Distributed LLM Serving

**arXiv 2026** | arXiv: 2602.06502

## 摘要

In LLM serving, reusing the KV cache of prompts across requests is critical for reducing TTFT and serving costs. Cache-affinity scheduling, which co-locates requests with the same prompt prefix to maximize KV cache reuse, often conflicts with load-balancing scheduling that distributes requests evenly across compute instances. Existing schedulers fail to reconcile this trade-off as they operate within a single mapping space, typically applying cache-affinity routing to a subset of requests and load-balanced routing to the rest, without a unified solution to achieve both goals. To address this limitation, we propose DualMap, a dual-mapping scheduling strategy for distributed LLM serving that achieves both cache affinity and load balancing. Its key idea is to map each request to two candidate instances via two independent hash functions based on the request prompt, then intelligently select the better candidate based on current system states. This design increases the likelihood that requests with shared prefixes are co-located, while evenly dispersing distinct prefixes across the cluster via "the power of two choices". To make DualMap robust under dynamic and skewed real-world workloads, we incorporate three techniques: 1) SLO-aware request routing, which prioritizes cache affinity but switches to load-aware scheduling when TTFT exceeds the SLO, enhancing load balance without sacrificing cache reuse; 2) hotspot-aware rebalancing, which dynamically migrates requests from overloaded to underloaded instances, mitigating hotspots and rebalancing the system; 3) lightweight dual-hash-ring scaling, which leverages a dual-hash-ring mapping to support fast and low-overhead instance scaling without costly global remapping. Experiments on real-world workloads show that DualMap improves effective request capacity by up to 2.25× under the same TTFT SLO constraints compared with SOTA work.

## 核心贡献

- 提出 DualMap 双映射调度策略，同时实现 cache affinity 和 load balancing
- 通过两个独立 hash 函数将请求映射到两个候选实例，智能选择最优
- "the power of two choices" 设计：提高共享前缀请求共置概率，同时均匀分散不同前缀
- SLO-aware 请求路由：TTFT 超限时从 cache affinity 切换到 load-aware
- hotspot-aware 重平衡：动态迁移请求，缓解热点
- 轻量双哈希环扩容：支持快速、低开销的实例扩缩容
- 真实工作负载：相同 TTFT SLO 约束下，有效请求容量提升 up to 2.25×

---
*导入自 net-research 数据库 | ID: arxiv26-002*
