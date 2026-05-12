---
id: nsdi26-011
title: "FalconFS: Distributed File System for Large-Scale Deep Learning Pipeline"
conference: NSDI 2026
date: 2026-03
authors:
  - name: "Jingwei Xu,"
  - name: "Shanghai Jiao Tong University and Huawei Technologies"
  - name: "Junbin Kang,"
  - name: "Huawei Technologies"
  - name: "Mingkai Dong,"
  - name: "Shanghai Jiao Tong University"
topics:
  - Distributed Systems
tags:
  - distributed-systems
arxiv: ""
url: "https://www.usenix.org/conference/nsdi26/presentation/xu"
score: 8
status: analyzed
---

# FalconFS: Distributed File System for Large-Scale Deep Learning Pipeline

**NSDI 2026** | Jingwei Xu,; Shanghai Jiao Tong University and Huawei Technologies;; Junbin Kang,; Huawei Technologies;; Mingkai Dong,; Shanghai Jiao Tong University;...


## 摘要

Client-side metadata caching has long been considered an effective method for accelerating metadata operations in distributed file systems (DFSs). However, we have found that client-side state (e.g., caching) is not only ineffective but also consumes valuable memory resources in the deep learning pipelines. We thus propose FalconFS, a DFS optimized for deep learning pipelines with the stateless-client architecture. Specifically, instead of performing client-side path resolution and caching, FalconFS efficiently resolves paths on the server side using hybrid metadata indexing and lazy namespace replication . FalconFS also boosts server concurrency with concurrent request merging and provides easy deployment with VFS shortcut . Evaluations against CephFS and Lustre show that FalconFS achieves up to 5.72× throughput for small file read/write and up to 12.81× throughput for deep learning model training. FalconFS has been running in Huawei autonomous driving system's production environment with 10,000 NPUs for one year and has been open-sourced.

## 技术栈

System

## 核心贡献

_（待补充结构化分析）_

---

*导入自 NSDI2026 分析项目 | ID: nsdi26-011*
