---
id: isca24-001
title: "Splitwise: Efficient generative LLM inference using phase splitting"
conference: ISCA 2024
date: 2024-06
authors:
  - name: "Pratyush Patel"
    affiliation: "University of Washington"
    is_industry: false
  - name: "Esha Choukse"
    affiliation: "Microsoft"
    is_industry: true
  - name: "Chaojie Zhang"
    affiliation: "Microsoft"
    is_industry: true
  - name: "Aashaka Shah"
    affiliation: "Microsoft"
    is_industry: true
  - name: "Íñigo Goiri"
    affiliation: "Microsoft"
    is_industry: true
  - name: "Saeed Maleki"
    affiliation: "Microsoft"
    is_industry: true
  - name: "Ricardo Bianchini"
    affiliation: "Microsoft"
    is_industry: true
topics:
  - LLM Serving
  - Distributed Systems
tags: [splitwise, phase-splitting, prefill-decode, disaggregation]
arxiv: "2311.18677"
url: "https://arxiv.org/abs/2311.18677"
status: analyzed
---

# Splitwise: Efficient generative LLM inference using phase splitting

**ISCA 2024** | arXiv: 2311.18677

## 摘要

Recent innovations in generative large language models (LLMs) have made their applications and use-cases ubiquitous. This has led to large-scale deployments of these models, using complex, expensive, and power-hungry AI accelerators, most commonly GPUs. These developments make LLM inference efficiency an important challenge. Based on our extensive characterization, we find that there are two main phases during an LLM inference request: a compute-intensive prompt computation, and a memory-intensive token generation, each with distinct latency, throughput, memory, and power characteristics. Despite state-of-the-art batching and scheduling, the token generation phase underutilizes compute resources. Specifically, unlike compute-intensive prompt computation phases, token generation phases do not require the compute capability of the latest GPUs, and can be run with lower power and cost.

With Splitwise, we propose splitting the two phases of a LLM inference request on to separate machines. This allows us to use hardware that is well-suited for each phase, and provision resources independently per phase. However, splitting an inference request across machines requires state transfer from the machine running prompt computation over to the machine generating tokens. We implement and optimize this state transfer using the fast back-plane interconnects available in today's GPU clusters.

We use the Splitwise technique to design LLM inference clusters using the same or different types of machines for the prompt computation and token generation phases. Our clusters are optimized for three key objectives: throughput, cost, and power. In particular, we show that we can achieve 1.4× higher throughput at 20% lower cost than current designs. Alternatively, we can achieve 2.35× more throughput with the same cost and power budgets.

## 核心贡献

- 将 LLM 推理拆分为计算密集的 prefill 和内存带宽密集的 decode 两阶段
- 两阶段分配到不同机器，使用硬件更匹配每个阶段的需求
- 利用 GPU 集群的高速背板互连优化状态传输
- 1.4× 更高吞吐量 + 20% 更低成本，或 2.35× 更高吞吐量（同成本/功耗）
- 为 throughput、cost、power 三个目标优化集群设计

---
*导入自 net-research 数据库 | ID: isca24-001*
