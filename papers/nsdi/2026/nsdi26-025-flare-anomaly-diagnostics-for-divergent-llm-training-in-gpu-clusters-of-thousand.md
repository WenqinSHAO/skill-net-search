---
id: nsdi26-025
title: "Flare: Anomaly Diagnostics for Divergent LLM Training in GPU Clusters of Thousand-Plus Scale"
conference: NSDI 2026
date: 2026-03
authors:
  - name: "Weihao Cui,"
  - name: "Shanghai Jiao Tong University"
  - name: "Ji Zhang,"
  - name: "Ant Group"
  - name: "Han Zhao,"
  - name: "Shanghai Jiao Tong University"
topics:
  - Distributed Systems
tags:
  - distributed-systems
arxiv: ""
url: "https://www.usenix.org/conference/nsdi26/presentation/cui"
score: 8
status: analyzed
---

# Flare: Anomaly Diagnostics for Divergent LLM Training in GPU Clusters of Thousand-Plus Scale

**NSDI 2026** | Weihao Cui,; Shanghai Jiao Tong University;; Ji Zhang,; Ant Group;; Han Zhao,; Shanghai Jiao Tong University;; Chao Liu and Jian Sha,; Ant Group;; Qua...


## 摘要

The rapid proliferation of large language models has driven the need for efficient GPU training clusters. However, it is challenging due to the frequent occurrence of training anomalies. Since existing diagnostic tools are narrowly tailored to specific issues, there are gaps in their ability to address anomalies spanning the entire training stack. In response, we introduce Flare, a diagnostic framework designed for distributed LLM training at scale. Flare first integrates a lightweight tracing daemon for full-stack and backend-extensible tracing. Additionally, it features a diagnostic engine that automatically diagnoses anomalies, with a focus on performance regressions. The deployment of Flare across 6,000 GPUs has demonstrated significant improvements in pinpointing deficiencies in real-world scenarios, with continuous operation for over eight months.

## 技术栈

System

## 核心贡献

_（待补充结构化分析）_

---

*导入自 NSDI2026 分析项目 | ID: nsdi26-025*
