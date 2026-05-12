---
id: nsdi26-026
title: "TurboTest: Learning When Less is Enough through Early Termination of Internet Speed Tests"
conference: NSDI 2026
date: 2026-03
authors:
  - name: "Haarika Manda,"
  - name: "University of California, Santa Barbara"
  - name: "Manshi Sagar, Yogesh, and Kartikay Singh,"
  - name: "IIT Delhi"
  - name: "Xintong Zhao,"
  - name: "University of California, Santa Barbara"
topics:
  - Distributed Systems
tags:
  - distributed-systems
arxiv: ""
url: "https://www.usenix.org/conference/nsdi26/presentation/manda"
score: 8
status: analyzed
---

# TurboTest: Learning When Less is Enough through Early Termination of Internet Speed Tests

**NSDI 2026** | Haarika Manda,; University of California, Santa Barbara;; Manshi Sagar, Yogesh, and Kartikay Singh,; IIT Delhi;; Xintong Zhao,; University of Californ...


## 摘要

Internet speed tests are indispensable for users, ISPs, and policymakers, but their static flooding-based design imposes growing costs: a single high-speed test can transfer hundreds of megabytes, and collectively, platforms like Ookla, M-Lab, and Fast.com generate petabytes of traffic each month. Reducing this burden requires deciding when a test can be stopped early without sacrificing accuracy. We frame this as an optimal stopping problem and show that existing heuristics-static thresholds, BBR pipe-full signals, or throughput stability rules from Fast.com and FastBTS-capture only a narrow portion of the achievable accuracy-savings trade-off. This paper introduces TURBOTEST, a systematic framework for speed test termination that sits atop existing platforms. The key idea is to decouple throughput prediction (Stage 1) from test termination (Stage 2): Stage 1 trains a regressor to estimate final throughput from partial measurements, while Stage 2 trains a classifier to decide when sufficient evidence has accumulated to stop. Leveraging richer transport-level features (RTT, retransmissions, congestion window) alongside throughput, TURBOTEST exposes a single tunable parameter for accuracy tolerance and includes a fallback mechanism for high-variability cases. Evaluation on 173,000 M-Lab NDT speed tests (2024-2025) shows that TURBOTEST achieves nearly 2-4x higher data savings than an approach based on BBR signals while reducing median error. These results demonstrate that adaptive ML-based termination can deliver accurate, efficient, and deployable speed tests at scale.

## 技术栈

Measurement

## 核心贡献

_（待补充结构化分析）_

---

*导入自 NSDI2026 分析项目 | ID: nsdi26-026*
