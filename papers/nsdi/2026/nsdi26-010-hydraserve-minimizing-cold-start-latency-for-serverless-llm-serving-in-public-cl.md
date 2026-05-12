---
id: nsdi26-010
title: "HydraServe: Minimizing Cold Start Latency for Serverless LLM Serving in Public Clouds"
conference: NSDI 2026
date: 2026-03
authors:
  - name: "Chiheng Lou, Sheng Qi, and Chao Jin,"
  - name: "School of Computer Science, Peking University"
  - name: "Dapeng Nie, Haoran Yang, and Yu Ding,"
  - name: "Alibaba Group"
  - name: "Xuanzhe Liu and Xin Jin,"
  - name: "School of Computer Science, Peking University"
topics:
  - Distributed Systems
tags:
  - distributed-systems
arxiv: ""
url: "https://www.usenix.org/conference/nsdi26/presentation/lou"
score: 8
status: analyzed
---

# HydraServe: Minimizing Cold Start Latency for Serverless LLM Serving in Public Clouds

**NSDI 2026** | Chiheng Lou, Sheng Qi, and Chao Jin,; School of Computer Science, Peking University;; Dapeng Nie, Haoran Yang, and Yu Ding,; Alibaba Group;; Xuanzhe L...


## 摘要

With the proliferation of large language model (LLM) variants, developers are turning to serverless computing for cost-efficient LLM deployment. However, public cloud providers often struggle to provide performance guarantees for serverless LLM serving due to significant cold start latency caused by substantial model sizes and complex runtime dependencies. To address this problem, we present HydraServe, a serverless LLM serving system designed to minimize cold start latency in public clouds. HydraServe proactively distributes models across servers to quickly fetch them, and overlaps cold-start stages within workers to reduce startup latency. Additionally, HydraServe strategically places workers across GPUs to avoid network contention among cold-start instances. To minimize resource consumption during cold starts, HydraServe further introduces pipeline consolidation that can merge groups of workers into individual serving endpoints. Our comprehensive evaluations under diverse settings demonstrate that HydraServe reduces the cold start latency by 1.7×–4.7× and improves service level objective attainment by 1.43×–1.74× compared to baselines.

## 技术栈

System

## 核心贡献

_（待补充结构化分析）_

---

*导入自 NSDI2026 分析项目 | ID: nsdi26-010*
