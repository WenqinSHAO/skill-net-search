---
id: nsdi26-049
title: "Seshat: Workload Characterization and Generation of Large Language Model Serving in Production"
conference: NSDI 2026
date: 2026-03
authors:
  - name: "Yuxing Xiang,"
  - name: "Peking University"
  - name: "Xue Li and Kun Qian,"
  - name: "Alibaba Group"
  - name: "Yan Zhang,"
  - name: "Peking University"
topics:
  - Distributed Systems
tags:
  - distributed-systems
arxiv: ""
url: "https://www.usenix.org/conference/nsdi26/presentation/xiang-servegen"
score: 8
status: analyzed
---

# Seshat: Workload Characterization and Generation of Large Language Model Serving in Production

**NSDI 2026** | Yuxing Xiang,; Peking University;; Xue Li and Kun Qian,; Alibaba Group;; Yan Zhang,; Peking University;; Wenyuan Yu and Ennan Zhai,; Alibaba Group;; X...


## 摘要

With the widespread adoption of Large Language Models (LLMs), serving LLM inference requests has become an increasingly important task, attracting active research advancements. Practical workloads play an essential role in this process: they are critical for motivating and benchmarking serving techniques and systems. However, the existing understanding of real-world LLM serving workloads is limited due to the lack of a comprehensive workload characterization. Prior analyses remain insufficient in scale and scope, thus failing to fully capture intricate workload characteristics. In this paper, we fill the gap with an in-depth characterization of LLM serving workloads collected from our worldwide cloud inference serving service, covering not only language models but also emerging multimodal and reasoning models, and unveiling important new findings in each case. Moreover, based on our findings, we propose ServeGen, a principled framework for generating realistic LLM serving workloads by composing them on a per-client basis. A practical use case in production validates that ServeGen avoids 50% under-provisioning compared to naive workload generation, demonstrating ServeGen's advantage in performance benchmarking. ServeGen is available at https://github.com/alibaba/ServeGen.

## 技术栈

Measurement

## 核心贡献

_（待补充结构化分析）_

---

*导入自 NSDI2026 分析项目 | ID: nsdi26-049*
