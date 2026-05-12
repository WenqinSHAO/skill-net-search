---
id: nsdi26-051
title: "A Fast Solver-Free Algorithm for Traffic Engineering in Large-Scale Data Center Network"
conference: NSDI 2026
date: 2026-03
authors:
  - name: "Yingming Mao,"
  - name: "Xi'an Jiaotong University and Shanghai Innovation Institute"
  - name: "Qiaozhu Zhai,"
  - name: "Xi'an Jiaotong University"
  - name: "Ximeng Liu,"
  - name: "Shanghai Jiao Tong University"
topics:
  - Distributed Systems
tags:
  - distributed-systems
arxiv: ""
url: "https://www.usenix.org/conference/nsdi26/presentation/mao"
score: 8
status: analyzed
---

# A Fast Solver-Free Algorithm for Traffic Engineering in Large-Scale Data Center Network

**NSDI 2026** | Yingming Mao,; Xi'an Jiaotong University and Shanghai Innovation Institute;; Qiaozhu Zhai,; Xi'an Jiaotong University;; Ximeng Liu,; Shanghai Jiao Ton...


## 摘要

Rapid growth of data center networks (DCNs) poses significant challenges for large-scale traffic engineering (TE). Existing acceleration strategies, which rely on commercial solvers or deep learning, face scalability issues and struggle with degrading performance or long computational time. Unlike existing algorithms adopting parallel strategies, we propose Sequential Source-Destination Optimization (SSDO), a sequential solver-free algorithm for intra-DCN TE. SSDO decomposes the problem into subproblems, each focused on adjusting the split ratios for a specific source-destination (SD) demand while keeping others fixed. To enhance the efficiency of subproblem optimization, we design a Balanced Binary Search Method (BBSM), which identifies the most balanced split ratios among multiple solutions that minimize Maximum Link Utilization (MLU). SSDO dynamically updates the sequence of SDs based on real-time utilization, which accelerates convergence and enhances solution quality. We evaluate SSDO primarily on Meta DCNs, and additionally on two WAN topologies as auxiliary demonstrations of generality. In a Meta topology, SSDO achieves a 65% and 60% reduction in normalized MLU compared to TEAL and POP, two state-of-the-art TE acceleration methods, while delivering a 12× speedup over POP. These results demonstrate the superior performance of SSDO in large-scale TE.

## 技术栈

Algorithm

## 核心贡献

_（待补充结构化分析）_

---

*导入自 NSDI2026 分析项目 | ID: nsdi26-051*
