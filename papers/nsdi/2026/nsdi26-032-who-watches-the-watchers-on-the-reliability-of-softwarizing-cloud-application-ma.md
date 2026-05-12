---
id: nsdi26-032
title: "Who Watches the Watchers? On the Reliability of Softwarizing Cloud Application Management"
conference: NSDI 2026
date: 2026-03
authors:
  - name: "Jiawei Tyler Gu, Zhen Tang, Yiming Su, Bogdan Alexandru Stoica, Xudong Sun, and William X. Zheng,"
  - name: "University of Illinois Urbana-Champaign"
  - name: "Yue Zhang and Akond Rahman,"
  - name: "Auburn University"
  - name: "Chen Wang,"
  - name: "IBM Research"
topics:
  - Distributed Systems
tags:
  - distributed-systems
arxiv: ""
url: "https://www.usenix.org/conference/nsdi26/presentation/gu"
score: 8
status: analyzed
---

# Who Watches the Watchers? On the Reliability of Softwarizing Cloud Application Management

**NSDI 2026** | Jiawei Tyler Gu, Zhen Tang, Yiming Su, Bogdan Alexandru Stoica, Xudong Sun, and William X. Zheng,; University of Illinois Urbana-Champaign;; Yue Zhang...


## 摘要

Modern cloud applications are increasingly managed by software programs, often named “operators,” which automate laborious, human-based operations. While operator programs largely prevent human mistakes, their own reliability has unprecedented impact on managed applications. This paper discusses the emerging challenges of operator program reliability on cloud-native platforms like Kubernetes. Our work is grounded in a rigorous analysis of 412 real-world failures of thirteen Kubernetes operators. We find that challenges of operator reliability come from the multifold complexity of an operator’s interactions with its managed applications, environment, and user interface. Among these, operators’ interactions with managed applications are the largest contributor to real-world operator failures, but they are largely overlooked—these interactions are often ad hoc and lack well-defined interfaces. We advocate to rethink the management interface of cloud applications and demonstrate this urgent need by showing the prevalence of defects in existing operators. Specifically, we develop a simple testing tool to exercise interactions between operators and the managed cloud applications, which discovered 86 new bugs in six popular Kubernetes operators.

## 技术栈

System

## 核心贡献

_（待补充结构化分析）_

---

*导入自 NSDI2026 分析项目 | ID: nsdi26-032*
