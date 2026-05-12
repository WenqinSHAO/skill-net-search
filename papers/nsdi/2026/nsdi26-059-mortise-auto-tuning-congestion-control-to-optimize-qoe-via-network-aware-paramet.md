---
id: nsdi26-059
title: "Mortise: Auto-tuning Congestion Control to Optimize QoE via Network-Aware Parameter Optimization"
conference: NSDI 2026
date: 2026-03
authors:
  - name: "Yixin Shen,"
  - name: "Tsinghua University, Bytedance Inc., and Zhongguancun Laboratory"
  - name: "Ruihua Chen,"
  - name: "Tsinghua University"
  - name: "Bo Wang,"
  - name: "Tsinghua University and Zhongguancun Laboratory"
topics:
  - Distributed Systems
tags:
  - distributed-systems
arxiv: ""
url: "https://www.usenix.org/conference/nsdi26/presentation/shen-yixin"
score: 8
status: analyzed
---

# Mortise: Auto-tuning Congestion Control to Optimize QoE via Network-Aware Parameter Optimization

**NSDI 2026** | Yixin Shen,; Tsinghua University, Bytedance Inc., and Zhongguancun Laboratory;; Ruihua Chen,; Tsinghua University;; Bo Wang,; Tsinghua University and ...


## 摘要

Congestion control algorithms (CCAs) critically shape the tradeoff among throughput, latency, and loss, directly impacting user Quality of Experience (QoE). However, most existing CCAs use static, heuristically chosen parameter settings that fail to adapt to dynamic network states, resulting in suboptimal QoE. Our key observation is that the optimal CCA parameter configuration depends on real-time network states. To bridge this gap, we propose Mortise, a real-time, network-aware adaptation framework that dynamically tunes rule-based CCA parameters to maximize QoE. To address the challenges in modeling the complex parameter-QoE relationship, Mortise introduces a QoS tradeoff proxy to decompose parameter optimization into two steps: it first infers the application's preferred QoS tradeoff from real-time QoE gradients and then derives the corresponding parameter settings via control-theoretic analysis. Implemented atop TCP and evaluated in both emulated and production environments, Mortise outperforms state-of-the-art solutions, enhancing the QoE of file downloading service by up to 73% and QoE of video streaming service by up to 167% in real-world scenarios, with minimal deployment overhead.

## 技术栈

Algorithm

## 核心贡献

_（待补充结构化分析）_

---

*导入自 NSDI2026 分析项目 | ID: nsdi26-059*
