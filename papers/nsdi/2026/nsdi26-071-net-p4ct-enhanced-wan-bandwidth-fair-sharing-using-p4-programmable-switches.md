---
id: nsdi26-071
title: "Net-P4ct: Enhanced WAN Bandwidth Fair Sharing Using P4 Programmable Switches"
conference: NSDI 2026
date: 2026-03
authors:
  - name: "Haoran Chen and Mingwei Cui,"
  - name: "Bytedance"
  - name: "Yihan Zou, Yihang Miao, Suhan Jiang, Damu Ding, Lirong Lai, Ming Gao, Rui Jiang, Shengyuan He, Anjian Chen, Jiaming Shi, Junjie Wan, Yandong Duan, Ruomin Fang, Hongyu Wu, and Yongping Tang,"
  - name: "ByteDance"
  - name: "Qiao Kang,"
  - name: "unaffiliated"
topics:
  - Distributed Systems
tags:
  - distributed-systems
arxiv: ""
url: "https://www.usenix.org/conference/nsdi26/presentation/chen"
score: 8
status: analyzed
---

# Net-P4ct: Enhanced WAN Bandwidth Fair Sharing Using P4 Programmable Switches

**NSDI 2026** | Haoran Chen and Mingwei Cui,; Bytedance;; Yihan Zou, Yihang Miao, Suhan Jiang, Damu Ding, Lirong Lai, Ming Gao, Rui Jiang, Shengyuan He, Anjian Chen, ...


## 摘要

At growing internet companies like ByteDance, Wide Area Network (WAN) bandwidth sharing across diverse services with varying SLO requirements is a fundamental challenge. Conventional host-based enforcement systems, where agents identify and throttle traffic at the server end, face practical challenges such as "blind spot" traffic, kernel-dependent operational complexity, and significant server resource overhead. To address these issues, we present Net-P4ct, an in-network bandwidth enforcement system using P4 programmable switches. Net-P4ct improves both bandwidth guarantees and fair sharing by shifting dynamic QoS control into the switch data plane. Specifically, it achieves broader traffic coverage by combining host-side traffic tagging with a P4-switch pipeline, where service classification and QoS class assignment are performed. Based on observed traffic metrics, a centralized control plane determines real-time policy updates according to the max-min fair bandwidth allocation. We demonstrate the system's benefits including improved bandwidth utilization, reduced operational complexity, and lower per-byte processing cost. Net-P4ct has been deployed in ByteDance's production WAN for nearly a year, and we hope to share our experience with the community.

## 技术栈

Hardware

## 核心贡献

_（待补充结构化分析）_

---

*导入自 NSDI2026 分析项目 | ID: nsdi26-071*
