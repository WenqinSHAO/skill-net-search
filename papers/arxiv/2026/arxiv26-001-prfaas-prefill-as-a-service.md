---
id: arxiv26-001
title: "Prefill-as-a-Service: KVCache of Next-Generation Models Could Go Cross-Datacenter"
conference: arXiv 2026
date: 2026-04
authors:
  - name: "Ruoyu Qin"
    affiliation: ""
    is_industry: true
  - name: "Weiran He"
    affiliation: ""
    is_industry: false
  - name: "Yaoyu Wang"
    affiliation: ""
    is_industry: false
  - name: "Zheming Li"
    affiliation: ""
    is_industry: false
  - name: "Xinran Xu"
    affiliation: ""
    is_industry: true
  - name: "Yongwei Wu"
    affiliation: ""
    is_industry: false
  - name: "Weimin Zheng"
    affiliation: ""
    is_industry: false
  - name: "Mingxing Zhang"
    affiliation: ""
    is_industry: false
topics:
  - LLM Serving
  - Distributed Systems
tags: [prfaas, prefill-as-a-service, disaggregation, cross-datacenter]
arxiv: "2604.15039"
url: "https://arxiv.org/abs/2604.15039"
status: analyzed
---

# Prefill-as-a-Service: KVCache of Next-Generation Models Could Go Cross-Datacenter

**arXiv 2026** | arXiv: 2604.15039

## 摘要

Prefill-decode (PD) disaggregation has become the standard architecture for large-scale LLM serving, but in practice its deployment boundary is still determined by KVCache transfer. In conventional dense-attention models, prefill generates huge KVCache traffics that keep prefill and decode tightly coupled within a single high-bandwidth network domain, limiting heterogeneous deployment and resource elasticity. Recent hybrid-attention architectures substantially reduce KVCache size, making cross-cluster KVCache transport increasingly plausible. However, smaller KVCache alone does not make heterogeneous cross-datacenter PD serving practical: real workloads remain bursty, request lengths are highly skewed, prefix caches are unevenly distributed, and inter-cluster bandwidth fluctuates. A naive design that fully externalizes prefill can therefore still suffer from congestion, unstable queueing, and poor utilization. We present Prefill-as-a-Service (PrfaaS), a cross-datacenter serving architecture that selectively offloads long-context prefill to standalone, compute-dense prefill clusters and transfers the resulting KVCache over commodity Ethernet to local PD clusters for decode. Rather than treating reduced KVCache as sufficient, PrfaaS combines model-side KV efficiency with system-side selective offloading, bandwidth-aware scheduling, and cache-aware request placement. This design removes the requirement that heterogeneous accelerators share the same low-latency RDMA fabric, enabling independent scaling of prefill and decode capacity across loosely coupled clusters. In a case study using an internal 1T-parameter hybrid model, a PrfaaS-augmented heterogeneous deployment achieves 54% higher serving throughput and 64% lower P90 TTFT than a homogeneous PD baseline, with approximately 15% throughput gain at equal cost, while consuming only modest cross-datacenter bandwidth.

## 核心贡献

- 提出 Prefill-as-a-Service (PrfaaS)，跨数据中心 serving 架构
- 将长上下文 prefill 卸载到独立的计算密集 prefill 集群
- 通过普通 Ethernet（非 RDMA）传输 KVCache
- 结合模型侧 KV 效率与系统侧选择性卸载、带宽感知调度
- 解除异构加速器共享同一低延迟 RDMA 网络的要求
- 1T 参数混合模型案例：54% 更高吞吐量 + 64% 更低 P90 TTFT

---
*导入自 net-research 数据库 | ID: arxiv26-001*
