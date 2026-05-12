---
id: nsdi26-015
title: "Attack of the Bubbles: Straggler-Resilient Pipeline Parallelism for Large Model Training"
conference: NSDI 2026
date: 2026-03
authors:
  - name: "Tianyuan Wu, Lunxi Cao, Hanfeng Lu, and Xiaoxiao Jiang,"
  - name: "Hong Kong University of Science and Technology"
  - name: "Yinghao Yu, Siran Yang, Guodong Yang, Jiamang Wang, Lin Qu, and Liping Zhang,"
  - name: "Alibaba Group"
  - name: "Wei Wang,"
  - name: "Hong Kong University of Science and Technology"
topics:
  - Distributed Systems
tags:
  - distributed-systems
arxiv: ""
url: "https://www.usenix.org/conference/nsdi26/presentation/wu-tianyuan"
score: 8
status: analyzed
---

# Attack of the Bubbles: Straggler-Resilient Pipeline Parallelism for Large Model Training

**NSDI 2026** | Tianyuan Wu, Lunxi Cao, Hanfeng Lu, and Xiaoxiao Jiang,; Hong Kong University of Science and Technology;; Yinghao Yu, Siran Yang, Guodong Yang, Jiaman...


## 摘要

Training large Deep Neural Network (DNN) models at scale often encounters straggler issues, mostly in communications due to network congestion, RNIC/switch defects, or topological asymmetry. Under advanced pipeline parallelism, even minor communication delays can induce significant training slowdowns. This occurs because (1) slow communication disrupts the pipeline schedule, creating cascading “bubbles” in a domino effect, and (2) current GPU kernel scheduling is susceptible to head-of-line blocking, where slow communication blocks subsequent computations, further adding to these bubbles. To address these challenges, we present PIPEMORPH, a straggler-resilient training system with two key optimizations. First, it optimally adapts the pipeline schedule in the presence of stragglers to absorb communication delays without inducing cascading bubbles, using a simple yet effective algorithm guided by an analytical model. Second, upon detecting slow communication, PIPEMORPH offloads communication operations from GPU to host memory and utilizes CPU-side RDMA for data transfer. This eliminates head-of-line blocking as subsequent computation kernels can be scheduled immediately on GPUs. Together, these optimizations effectively reduce pipeline stalls in the presence of communication stragglers, improving the training iteration time by 1.2-3.5× in our experiments under various settings.

## 技术栈

System

## 核心贡献

_（待补充结构化分析）_

---

*导入自 NSDI2026 分析项目 | ID: nsdi26-015*
