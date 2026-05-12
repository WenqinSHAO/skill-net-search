---
id: nsdi26-058
title: "Predict, Prune, Play: Efficient Video Playback Optimization Under Device Diversity and Drift"
conference: NSDI 2026
date: 2026-03
authors:
  - name: "Harsha Sharma,"
  - name: "Massachusetts Institute of Technology and Amazon"
  - name: "Pouya Hamadanian and Arash Nasr-Esfahany,"
  - name: "Massachusetts Institute of Technology"
  - name: "Zahaib Akhtar,"
  - name: "Amazon and North Carolina State University"
topics:
  - Distributed Systems
tags:
  - distributed-systems
arxiv: ""
url: "https://www.usenix.org/conference/nsdi26/presentation/sharma"
score: 8
status: analyzed
---

# Predict, Prune, Play: Efficient Video Playback Optimization Under Device Diversity and Drift

**NSDI 2026** | Harsha Sharma,; Massachusetts Institute of Technology and Amazon;; Pouya Hamadanian and Arash Nasr-Esfahany,; Massachusetts Institute of Technology;; ...


## 摘要

Video-streaming platforms tune dozens of playback parameters across thousands of client devices. Our measurements from Amazon Prime Video show that device-specific tuning can enhance stream quality. Yet traditional tuning techniques like Bayesian optimization become prohibitively expensive due to the large configuration space and the constant emergence of new device types. We introduce AZEEM, a scalable recommendation system leveraging few-shot prediction to rapidly identify promising configurations for new devices. The key insight behind AZEEM is that devices exhibit performance similarities that enable predictions from limited observations. Trained on offline data of device-playback configuration interactions, AZEEM efficiently narrows down the search space to a small set of configurations likely to contain optimal or near-optimal candidates. Additionally, AZEEM addresses temporal distribution shift—where the best-performing configurations change over time—by recommending a small, robust set of candidates rather than a single configuration. Evaluations using large-scale real-world datasets show that AZEEM reduces exploration cost by 5.8−13.6× and improves stream quality compared to state-of-the-art Bayesian optimization and multi-armed bandit approaches, enabling effective device-specific optimization at scale. We deploy AZEEM on a subset of Amazon Prime Video’s production traffic, where it achieved a relative QoE improvement of 2.7% on average and 10.6% at the 90th percentile over an existing treatment tuning system.

## 技术栈

AI

## 核心贡献

_（待补充结构化分析）_

---

*导入自 NSDI2026 分析项目 | ID: nsdi26-058*
