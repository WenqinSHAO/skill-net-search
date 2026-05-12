---
id: fast25-001
title: "Mooncake: A KVCache-centric Disaggregated Architecture for LLM Serving"
conference: FAST 2025
date: 2025-02
authors:
  - name: "Ruoyu Qin"
    affiliation: "Moonshot AI; Tsinghua University"
    is_industry: true
  - name: "Zheming Li"
    affiliation: "Moonshot AI"
    is_industry: true
  - name: "Weiran He"
    affiliation: "Moonshot AI"
    is_industry: true
  - name: "Jialei Cui"
    affiliation: "Moonshot AI"
    is_industry: true
  - name: "Feng Ren"
    affiliation: "Tsinghua University"
    is_industry: false
  - name: "Mingxing Zhang"
    affiliation: "Tsinghua University"
    is_industry: false
  - name: "Yongwei Wu"
    affiliation: "Tsinghua University"
    is_industry: false
  - name: "Weimin Zheng"
    affiliation: "Tsinghua University"
    is_industry: false
  - name: "Xinran Xu"
    affiliation: "Moonshot AI"
    is_industry: true
topics:
  - LLM Serving
  - Distributed Systems
tags: [mooncake, kv-cache, disaggregation, distributed-serving]
arxiv: "2407.00079"
url: "https://www.usenix.org/conference/fast25/presentation/qin"
status: analyzed
---

# Mooncake: A KVCache-centric Disaggregated Architecture for LLM Serving

**FAST 2025 (Best Paper)** | arXiv: 2407.00079

## 摘要

Mooncake is the serving platform for Kimi, a leading LLM service provided by Moonshot AI. It features a KVCache-centric disaggregated architecture that separates the prefill and decoding clusters. It also leverages the underutilized CPU, DRAM, and SSD resources of the GPU cluster to implement a disaggregated cache of KVCache. The core of Mooncake is its KVCache-centric scheduler, which balances maximizing overall effective throughput while meeting latency-related Service Level Objectives (SLOs). Unlike traditional studies that assume all requests will be processed, Mooncake faces challenges due to highly overloaded scenarios. To mitigate these, we developed a prediction-based early rejection policy. Experiments show that Mooncake excels in long-context scenarios. Compared to the baseline method, Mooncake can achieve up to a 525% increase in throughput in certain simulated scenarios while adhering to SLOs. Under real workloads, Mooncake's innovative architecture enables Kimi to handle 75% more requests.

## 核心贡献

- **KVCache-centric 架构**：围绕 KV cache 设计整个 serving 平台
- **Prefill/Decode 分离**：prefill 集群和 decoding 集群分离部署
- **分层 KV 缓存**：利用 CPU DRAM、SSD 资源实现 disaggregated KV cache
- **KV-aware 调度器**：在满足 SLO 约束下最大化有效吞吐量
- **早期拒绝策略**：基于预测的过载保护机制
- **生产部署**：Kimi 使用，真实工作负载下处理 75% 更多请求
- FAST 2025 **最佳论文**

---
*导入自 net-research 数据库 | ID: fast25-001*
