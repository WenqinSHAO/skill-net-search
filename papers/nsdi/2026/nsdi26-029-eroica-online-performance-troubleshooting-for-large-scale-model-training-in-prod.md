---
id: nsdi26-029
title: "EROICA: Online Performance Troubleshooting for Large-scale Model Training in Production"
conference: NSDI 2026
date: 2026-03
authors:
  - name: "Yu Guan, Zhiyu Yin, Haoyu Chen, Sheng Cheng, Chaojie Yang, and Kun Qian,"
  - name: "Alibaba Group"
  - name: "Tianyin Xu,"
  - name: "University of Illinois Urbana-Champaign"
  - name: "Pengcheng Zhang, Yang Zhang, Hanyu Zhao, Yong Li, Dennis Cai, and Ennan Zhai,"
  - name: "Alibaba Group"
topics:
  - Distributed Systems
tags:
  - distributed-systems
arxiv: ""
url: "https://www.usenix.org/conference/nsdi26/presentation/guan-yu"
score: 8
status: analyzed
---

# EROICA: Online Performance Troubleshooting for Large-scale Model Training in Production

**NSDI 2026** | Yu Guan, Zhiyu Yin, Haoyu Chen, Sheng Cheng, Chaojie Yang, and Kun Qian,; Alibaba Group;; Tianyin Xu,; University of Illinois Urbana-Champaign;; Pengc...


## 摘要

Troubleshooting performance problems of large model training (LMT) is immensely challenging, due to unprecedented scales of modern GPU clusters, the complexity of software-hardware interactions, and the data intensity of the training process. Existing troubleshooting approaches designed for traditional distributed systems or datacenter networks fall short and can hardly apply to real-world training systems. In this paper, we present EROICA, the first online troubleshooting system that provides both fine-grained observation based on profiling, and coverage of all machines in GPU clusters, to diagnose performance issues in production, including both hardware and software problems (or the mixture of both). EROICA effectively summarizes runtime behavior patterns of LMT function executions via online profiling, and leverages differential observability to localize the root cause with minimal production impact. EROICA has been deployed as a production service for large-scale GPU clusters of ~100,000 GPUs for 1.5 years. It has diagnosed a variety of difficult performance issues with 97.5% success.

## 技术栈

System

## 核心贡献

_（待补充结构化分析）_

---

*导入自 NSDI2026 分析项目 | ID: nsdi26-029*
