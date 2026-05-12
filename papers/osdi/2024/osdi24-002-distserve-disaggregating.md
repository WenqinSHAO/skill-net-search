---
id: osdi24-002
title: "DistServe: Disaggregating Prefill and Decoding for Goodput-optimized Large Language Model Serving"
conference: OSDI 2024
date: 2024-07
authors:
  - name: "Yinmin Zhong"
    affiliation: "Peking University"
    is_industry: false
  - name: "Shengyu Liu"
    affiliation: "Peking University"
    is_industry: false
  - name: "Junda Chen"
    affiliation: "University of California San Diego"
    is_industry: false
  - name: "Jianbo Hu"
    affiliation: "Peking University"
    is_industry: false
  - name: "Yibo Zhu"
    affiliation: "StepFun"
    is_industry: true
  - name: "Xuanzhe Liu"
    affiliation: "Peking University"
    is_industry: false
  - name: "Xin Jin"
    affiliation: "Peking University"
    is_industry: false
  - name: "Hao Zhang"
    affiliation: "University of California San Diego"
    is_industry: false
topics:
  - LLM Serving
  - Distributed Systems
tags: [distllm, disaggregation, prefill-decode, goodput]
arxiv: "2401.09670"
url: "https://arxiv.org/abs/2401.09670"
status: analyzed
---

# DistServe: Disaggregating Prefill and Decoding for Goodput-optimized Large Language Model Serving

**OSDI 2024** | arXiv: 2401.09670

## 摘要

DistServe improves the performance of large language models (LLMs) serving by disaggregating the prefill and decoding computation. Existing LLM serving systems colocate the two phases and batch the computation of prefill and decoding across all users and requests. We find that this strategy not only leads to strong prefill-decoding interferences but also couples the resource allocation and parallelism plans for both phases. LLM applications often emphasize individual latency for each phase: time to first token (TTFT) for the prefill phase and time per output token (TPOT) of each request for the decoding phase. In the presence of stringent latency requirements, existing systems have to prioritize one latency over the other, or over-provision compute resources to meet both. DistServe assigns prefill and decoding computation to different GPUs, hence eliminating prefill-decoding interferences. Given the application's TTFT and TPOT requirements, DistServe co-optimizes the resource allocation and parallelism strategy tailored for each phase. DistServe also places the two phases according to the serving cluster's bandwidth to minimize the communication caused by disaggregation. As a result, DistServe significantly improves LLM serving performance in terms of the maximum rate that can be served within both TTFT and TPOT constraints on each GPU. Our evaluations show that on various popular LLMs, applications, and latency requirements, DistServe can serve 7.4x more requests or 12.6x tighter SLO, compared to state-of-the-art systems, while staying within latency constraints for > 90% of requests.

## 核心贡献

- 将 prefill 和 decoding 计算分配到不同 GPU，消除两阶段干扰
- 根据 TTFT 和 TPOT 需求，为每阶段协同优化资源分配和并行策略
- 根据集群带宽放置两阶段，最小化 disaggregation 带来的通信开销
- 相比 SOTA 系统，可服务 7.4× 更多请求或 12.6× 更紧 SLO
- 在 > 90% 请求满足延迟约束的同时显著提升性能

---
*导入自 net-research 数据库 | ID: osdi24-002*
