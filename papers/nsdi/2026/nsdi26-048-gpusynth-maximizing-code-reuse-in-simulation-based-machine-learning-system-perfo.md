---
id: nsdi26-048
title: "GPUSynth: Maximizing Code Reuse in Simulation-Based Machine Learning System Performance Estimation"
conference: NSDI 2026
date: 2026-03
authors:
  - name: "Jianxing Qin, Jingrong Chen, and Xinhao Kong,"
  - name: "Duke University"
  - name: "Yongji Wu,"
  - name: "UC Berkeley"
  - name: "Tianjun Yuan,"
  - name: "Duke University"
topics:
  - Distributed Systems
tags:
  - distributed-systems
arxiv: ""
url: "https://www.usenix.org/conference/nsdi26/presentation/qin"
score: 8
status: analyzed
---

# GPUSynth: Maximizing Code Reuse in Simulation-Based Machine Learning System Performance Estimation

**NSDI 2026** | Jianxing Qin, Jingrong Chen, and Xinhao Kong,; Duke University;; Yongji Wu,; UC Berkeley;; Tianjun Yuan,; Duke University;; Liang Luo,; Meta AI;; Zhao...


## 摘要

Modern machine learning (ML) training workloads place substantial demands on both computational and communication resources. Consequently, accurate performance estimation has become increasingly critical for guiding system design decisions, such as the selection of parallelization strategies, cluster configurations, and hardware provisioning. Existing simulation-based performance estimation requires reimplementing the ML framework in a simulator, which demands significant manual effort and is hard to maintain as ML frameworks evolve rapidly. This paper introduces Phantora, a hybrid GPU cluster simulator designed for performance estimation of ML training workloads. Phantora executes unmodified ML frameworks as is within a distributed, containerized environment. Each container emulates the behavior of a GPU server in a large-scale cluster, while Phantora intercepts and simulates GPU- and communication-related operations to provide high-fidelity performance estimation. We call this approach hybrid simulation of ML systems, in contrast to traditional methods that simulate static workloads. The primary advantage of hybrid simulation is that it allows direct reuse of ML framework source code in simulation, avoiding the need for reimplementation. Our evaluation shows that Phantora provides accuracy comparable to static workload simulation while supporting three state-of-the-art LLM training frameworks out-of-the-box. In addition, Phantora operates on a single GPU, eliminating the need for the resource-intensive trace collection and workload extraction steps required by traditional trace-based simulators. Phantora is open-sourced at https://github.com/QDelta/Phantora.

## 技术栈

System

## 核心贡献

_（待补充结构化分析）_

---

*导入自 NSDI2026 分析项目 | ID: nsdi26-048*
