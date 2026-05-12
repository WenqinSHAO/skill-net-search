---
id: nsdi26-004
title: "SYMI: Efficient Mixture-of-Experts Training via Model and Optimizer State Decoupling"
conference: NSDI 2026
date: 2026-03
authors:
  - name: "Athinagoras Skiadopoulos,"
  - name: "Stanford University"
  - name: "Mark Zhao,"
  - name: "University of Colorado Boulder"
  - name: "Swapnil Gandhi,"
  - name: "Stanford University and NVIDIA"
topics:
  - Distributed Systems
tags:
  - distributed-systems
arxiv: ""
url: "https://www.usenix.org/conference/nsdi26/presentation/skiadopoulos"
score: 8
status: analyzed
---

# SYMI: Efficient Mixture-of-Experts Training via Model and Optimizer State Decoupling

**NSDI 2026** | Athinagoras Skiadopoulos,; Stanford University;; Mark Zhao,; University of Colorado Boulder;; Swapnil Gandhi,; Stanford University and NVIDIA;; Thomas...


## 摘要

Mixture-of-Experts (MoE) models have become a widely-adopted solution to continue scaling model sizes without a corresponding linear increase in compute. During MoE model training, each input token is dynamically routed to a subset of experts—sparsely-activated feed-forward networks—within each transformer layer. The distribution of tokens assigned to each expert varies widely and rapidly over the course of training. To handle the wide load imbalance across experts, current systems are forced to either drop tokens assigned to popular experts, degrading convergence, or frequently rebalance resources allocated to each expert based on popularity, incurring high state migration overheads. To break this performance-accuracy tradeoff, we introduce SYMI, an adaptive MoE training system. The key insight of SYMI is to decouple the placement of expert parameters from their large optimizer state. SYMI statically partitions the optimizer of each expert across all training nodes. Meanwhile, SYMI dynamically adjusts the placement of expert parameters by repurposing existing weight updates, avoiding migration overheads. In doing so, SYMI right-sizes the GPU resources allocated to each expert, on a per-iteration basis, with minimal overhead. Compared to state-of-the-art MoE training systems, DeepSpeed and FlexMoE, SYMI is able to achieve a 30.5% and 25.9% faster time-to-convergence, respectively.

## 技术栈

System

## 核心贡献

_（待补充结构化分析）_

---

*导入自 NSDI2026 分析项目 | ID: nsdi26-004*
