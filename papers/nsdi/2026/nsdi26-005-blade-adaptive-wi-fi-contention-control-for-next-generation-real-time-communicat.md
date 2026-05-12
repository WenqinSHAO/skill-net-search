---
id: nsdi26-005
title: "BLADE: Adaptive Wi-Fi Contention Control for Next-Generation Real-Time Communication"
conference: NSDI 2026
date: 2026-03
authors:
  - name: "Fengqian Guo,"
  - name: "University of Science and Technology of China"
  - name: "Yuhan Zhou,"
  - name: "Peking University"
  - name: "Longwei Jiang and Congcong Miao,"
  - name: "Tencent"
topics:
  - Distributed Systems
tags:
  - distributed-systems
arxiv: ""
url: "https://www.usenix.org/conference/nsdi26/presentation/guo-fengqian"
score: 8
status: analyzed
---

# BLADE: Adaptive Wi-Fi Contention Control for Next-Generation Real-Time Communication

**NSDI 2026** | Fengqian Guo,; University of Science and Technology of China;; Yuhan Zhou,; Peking University;; Longwei Jiang and Congcong Miao,; Tencent;; Yuxin Liu,...


## 摘要

Next-generation real-time communication (NGRTC) applications, such as cloud gaming and XR, demand consistently ultra-low latency. However, through our first large-scale measurement, we find that despite the deployment of edge servers, dedicated congestion control, and loss recovery mechanisms, cloud gaming users still experience long-tail latency in Wi-Fi networks. We further identify that Wi-Fi last-mile access points (APs) serve as the primary latency bottleneck. Specifically, short-term packet delivery droughts, caused by fundamental limitations in Wi-Fi contention control standards, are the root cause. To address this issue, we propose BLADE, an adaptive contention control algorithm that dynamically adjusts the contention windows (CW) of all Wi-Fi transmitters based on the channel contention level in a fully distributed manner. Our NS3 simulations and real-world evaluations with commercial Wi-Fi APs demonstrate that, compared to standard contention control, BLADE reduces Wi-Fi packet transmission tail latency by over 5X under heavy channel contention and significantly stabilizes MAC throughput while ensuring fast and fair convergence. Consequently, BLADE reduces the video stall rate in cloud gaming by over 90%.

## 技术栈

Protocol

## 核心贡献

_（待补充结构化分析）_

---

*导入自 NSDI2026 分析项目 | ID: nsdi26-005*
