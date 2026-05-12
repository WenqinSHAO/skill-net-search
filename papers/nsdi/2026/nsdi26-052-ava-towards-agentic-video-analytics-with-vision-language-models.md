---
id: nsdi26-052
title: "AVA: Towards Agentic Video Analytics with Vision Language Models"
conference: NSDI 2026
date: 2026-03
authors:
  - name: "Yuxuan Yan,"
  - name: "Zhejiang University"
  - name: "Shiqi Jiang,"
  - name: "Microsoft Research"
  - name: "Ting Cao,"
  - name: "Tsinghua University"
topics:
  - Distributed Systems
tags:
  - distributed-systems
arxiv: ""
url: "https://www.usenix.org/conference/nsdi26/presentation/yan"
score: 8
status: analyzed
---

# AVA: Towards Agentic Video Analytics with Vision Language Models

**NSDI 2026** | Yuxuan Yan,; Zhejiang University;; Shiqi Jiang,; Microsoft Research;; Ting Cao,; Tsinghua University;; Yifan Yang,; Microsoft Research;; Qianqian Yang...


## 摘要

AI-driven video analytics has become increasingly important across diverse domains. However, existing systems are often constrained to specific, predefined tasks, limiting their adaptability in open-ended analytical scenarios. The recent emergence of Vision Language Models (VLMs) as transformative technologies offers significant potential for enabling open-ended video understanding, reasoning, and analytics. Nevertheless, their limited context windows present challenges when processing ultra-long video content, which is prevalent in real-world applications. To address this, we introduce AVA, a VLM-powered system designed for open-ended, advanced video analytics. AVA incorporates two key innovations: (1) the near real-time construction of Event Knowledge Graphs (EKGs) for efficient indexing of long or continuous video streams, and (2) an agentic retrieval-generation mechanism that leverages EKGs to handle complex and diverse queries. Comprehensive evaluations on public benchmarks, LVBench and VideoMME-Long, demonstrate that AVA achieves state-of-the-art performance, attaining 62.3% and 64.1% accuracy, respectively, significantly surpassing existing VLM and video Retrieval-Augmented Generation (RAG) systems. Furthermore, to evaluate video analytics in ultra-long and open-world video scenarios, we introduce a new benchmark, AVA-100. This benchmark comprises 8 videos, each exceeding 10 hours in duration, along with 120 manually annotated, diverse, and complex question-answer pairs. On AVA-100, AVA achieves top-tier performance with an accuracy of 75.8%. The source code of AVA is available at https://github.com/I-ESC/Project-Ava . The AVA-100 benchmark could be accessed at https://huggingface.co/datasets/iesc/Ava-100 .

## 技术栈

AI

## 核心贡献

_（待补充结构化分析）_

---

*导入自 NSDI2026 分析项目 | ID: nsdi26-052*
