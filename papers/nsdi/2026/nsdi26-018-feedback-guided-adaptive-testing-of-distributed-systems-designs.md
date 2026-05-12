---
id: nsdi26-018
title: "Feedback-guided Adaptive Testing of Distributed Systems Designs"
conference: NSDI 2026
date: 2026-03
authors:
  - name: "Ao Li,"
  - name: "Carnegie Mellon University"
  - name: "Ankush Desai,"
  - name: "Amazon Web Services"
  - name: "Rohan Padhye,"
  - name: "Carnegie Mellon University"
topics:
  - Distributed Systems
tags:
  - distributed-systems
arxiv: ""
url: "https://www.usenix.org/conference/nsdi26/presentation/li"
score: 8
status: analyzed
---

# Feedback-guided Adaptive Testing of Distributed Systems Designs

**NSDI 2026** | Ao Li,; Carnegie Mellon University;; Ankush Desai,; Amazon Web Services;; Rohan Padhye,; Carnegie Mellon University


## 摘要

Validating distributed systems for correctness poses significant challenges. Practitioners often rely on formal models of core system designs, which are then tested by exploring possible component interactions. Unfortunately, standard testing approaches based on random sampling of the state space are inefficient and prone to missing subtle bugs, as they lack guidance from the system's behavior. To address this, we present Fest, a new testing system for formal models of distributed systems. Fest incorporates feedback-guided adaptive schedule generation, drawing inspiration from grey-box fuzzing, to steer exploration towards maximizing behavioral coverage and uncovering bugs more effectively. Our implementation in the P programming framework demonstrates significant improvements across 94 distributed system model configurations: up to 41× (1.5× average) improvement in behavioral coverage, 278× (15× average) improvement in scenario coverage, and 33% more bugs detected compared to existing methods. These results highlight Fest's effectiveness in ensuring the robustness of distributed systems through improved testing efficiency.

## 技术栈

Algorithm

## 核心贡献

_（待补充结构化分析）_

---

*导入自 NSDI2026 分析项目 | ID: nsdi26-018*
