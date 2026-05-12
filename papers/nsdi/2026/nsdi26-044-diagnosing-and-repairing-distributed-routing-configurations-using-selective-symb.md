---
id: nsdi26-044
title: "Diagnosing and Repairing Distributed Routing Configurations Using Selective Symbolic Simulation"
conference: NSDI 2026
date: 2026-03
authors:
  - name: "Rulan Yang, Gao Han, Hanyang Shao, Xiaoqiang Zheng, Xing Fang, Ziyi Wang, and Lizhao You,"
  - name: "Xiamen University"
  - name: "Ruiting Zhou,"
  - name: "Southeast University"
  - name: "Linghe Kong,"
  - name: "Shanghai Jiao Tong University"
topics:
  - Distributed Systems
tags:
  - distributed-systems
arxiv: ""
url: "https://www.usenix.org/conference/nsdi26/presentation/yang"
score: 8
status: analyzed
---

# Diagnosing and Repairing Distributed Routing Configurations Using Selective Symbolic Simulation

**NSDI 2026** | Rulan Yang, Gao Han, Hanyang Shao, Xiaoqiang Zheng, Xing Fang, Ziyi Wang, and Lizhao You,; Xiamen University;; Ruiting Zhou,; Southeast University;; L...


## 摘要

Although substantial progress has been made in automatically verifying whether distributed routing configurations comply with certain intents, diagnosing and repairing configuration errors remains manual and time-consuming. To fill this gap, we propose S2Sim, a novel system for automatic routing configuration diagnosis and repair. Our key insight is that by deriving a set of contracts that guarantees an intent-compliant variant of the erroneous configuration, we can systematically check for all contract violations in the configuration via symbolic simulation to pinpoint and repair the errors. S2Sim also introduces a series of extensions to support complex configurations (e.g., ACL, route aggregation and multi-path routing), networks (e.g., underlay and overlay networks), and intents (e.g., k-link failure tolerance). We fully implement S2Sim and evaluate its performance using real configurations from two major providers and synthesized configurations composed from their real errors and real-world topologies with different scales O(10) to O(1000). Results show that S2Sim accurately and efficiently diagnoses and repairs real configuration errors (i.e., up to 20 seconds in real networks of O(100) nodes and up to 15 minutes in synthesized networks of O(1000) nodes).

## 技术栈

System

## 核心贡献

_（待补充结构化分析）_

---

*导入自 NSDI2026 分析项目 | ID: nsdi26-044*
