---
id: nsdi26-056
title: "Matryoshka: Realizing Hyperscale Data Center Network Design for the AI Era"
conference: NSDI 2026
date: 2026-03
authors:
  - name: "Yan Cai,"
  - name: "Meta"
  - name: "Jialong Li,"
  - name: "Max Planck Institute for Informatics"
  - name: "Kutalmis Akpinar, Tianxiang Li, Hany Morsy, Jason Wilson, and Sunil Khaunte,"
  - name: "Meta"
topics:
  - Distributed Systems
tags:
  - distributed-systems
arxiv: ""
url: "https://www.usenix.org/conference/nsdi26/presentation/cai"
score: 8
status: analyzed
---

# Matryoshka: Realizing Hyperscale Data Center Network Design for the AI Era

**NSDI 2026** | Yan Cai,; Meta;; Jialong Li,; Max Planck Institute for Informatics;; Kutalmis Akpinar, Tianxiang Li, Hany Morsy, Jason Wilson, and Sunil Khaunte,; Met...


## 摘要

Over the past decade, data center networking (DCN) has undergone substantial transformation in terms of both scale and complexity. Developing a DCN entails multiple intricate steps, such as establishing physical connections, configuring logical network addressing, and defining high-level routing policies. While extensive work has focused on logical DCN design and physical deployment, a critical gap remains: materializing these designs into concrete switch configurations—a necessary step to realize the development procedure. This problem is especially acute in the AI era, as hyperscale, rapidly evolving, and highly heterogeneous AI-driven clusters place unprecedented demands on DCN design and implementation. This paper presents Matryoshka, Meta’s production-scale DCN design system that bridges this gap. Matryoshka employs an intent-based, model-driven approach to systematically compile high-level DCN design intents into working switch configurations. Operational for over six years, Matryoshka has supported orders-of-magnitude growth in Meta’s DCN infrastructure, guiding the design nearly 900 DCNs across 18 distinct types, including the latest 100K-GPU supercluster for AI training. We share our experience in building and operating Matryoshka, highlighting how it empowers the rapid design and evolution of AI clusters nowadays.

## 技术栈

System

## 核心贡献

_（待补充结构化分析）_

---

*导入自 NSDI2026 分析项目 | ID: nsdi26-056*
