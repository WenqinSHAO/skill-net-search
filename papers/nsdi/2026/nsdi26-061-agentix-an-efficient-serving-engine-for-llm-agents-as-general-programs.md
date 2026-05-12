---
id: nsdi26-061
title: "Agentix: An Efficient Serving Engine for LLM Agents as General Programs"
conference: NSDI 2026
date: 2026-03
authors:
  - name: "Michael Luo,"
  - name: "University of California, Berkeley, and Google DeepMind"
  - name: "Xiaoxiang Shi,"
  - name: "Shanghai Jiao Tong University"
  - name: "Colin Cai, Tianjun Zhang, Justin Wong, and Yichuan Wang,"
  - name: "University of California, Berkeley"
topics:
  - Distributed Systems
tags:
  - distributed-systems
arxiv: ""
url: "https://www.usenix.org/conference/nsdi26/presentation/luo"
score: 8
status: analyzed
---

# Agentix: An Efficient Serving Engine for LLM Agents as General Programs

**NSDI 2026** | Michael Luo,; University of California, Berkeley, and Google DeepMind;; Xiaoxiang Shi,; Shanghai Jiao Tong University;; Colin Cai, Tianjun Zhang, Just...


## 摘要

Large language model (LLM) applications are evolving beyond simple chatbots into dynamic, general-purpose agentic programs, which scale LLM calls and output tokens to help AI agents reason, explore, and solve complex tasks. However, existing LLM serving systems ignore dependencies between programs and calls, missing significant opportunities for optimization. Our analysis reveals that programs submitted to LLM serving engines experience long cumulative wait times, primarily due to head-of-line blocking at both the individual LLM request and the program. To address this, we introduce Agentix, an LLM serving system that treats programs as first-class citizens to minimize their end-to-end latencies. Agentix intercepts LLM calls submitted by programs, enriching schedulers with program-level context. We propose two scheduling algorithms—for single-threaded and distributed programs—that preempt and prioritize LLM calls based on their programs' previously completed calls. Our evaluation demonstrates that across diverse LLMs and agentic workloads, Agentix improves throughput of programs by 4-15× at the same latency compared to state-of-the-art systems, such as vLLM.

## 技术栈

System

## 核心贡献

_（待补充结构化分析）_

---

*导入自 NSDI2026 分析项目 | ID: nsdi26-061*
