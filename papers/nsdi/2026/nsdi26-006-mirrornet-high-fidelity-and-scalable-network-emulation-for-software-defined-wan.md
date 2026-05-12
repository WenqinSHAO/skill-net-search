---
id: nsdi26-006
title: "MirrorNet: High-fidelity and Scalable Network Emulation for Software-defined WAN"
conference: NSDI 2026
date: 2026-03
authors:
  - name: "Congcong Miao,"
  - name: "Tencent"
  - name: "Yuejie Wang,"
  - name: "Peking University"
  - name: "Jianming Wang, Xuefeng Ji, Guozhi Shan, Sirui Li, Pan Fang, and Yanke Zhang,"
  - name: "Tencent"
topics:
  - Distributed Systems
tags:
  - distributed-systems
arxiv: ""
url: "https://www.usenix.org/conference/nsdi26/presentation/miao"
score: 8
status: analyzed
---

# MirrorNet: High-fidelity and Scalable Network Emulation for Software-defined WAN

**NSDI 2026** | Congcong Miao,; Tencent;; Yuejie Wang,; Peking University;; Jianming Wang, Xuefeng Ji, Guozhi Shan, Sirui Li, Pan Fang, and Yanke Zhang,; Tencent;; Ji...


## 摘要

Operating a large-scale WAN reliably is becoming increasingly challenging due to the surge in traffic volumes, and the growing complexity of both software and hardware. In this paper, we introduce MirrorNet, our production-grade emulation framework designed to mirror a software-based WAN. Unlike traditional emulators and simulators that access only a partial set of network information, MirrorNet functions as a comprehensive twin of the production network, encompassing the controller, data plane, and network traffic. Our key challenge lies in striking a balance between the requirements for a fine-grained and high-fidelity emulation, scalability, and resource efficiency. To address these, we have developed a multi-faceted approach: i) we employ an incremental storage and replay method to reconstruct the historical production network at a second-by-second level; ii) we propose a network update strategy that maintains consistent alignment between the emulation and production networks; and iii) we design a custom orchestrator capable of rapidly deploying one or more large-scale emulation networks, which can operate concurrently to expedite testing. MirrorNet has been deployed in TWAN for over 2 years and integral in our daily WAN management tasks, aiding in troubleshooting, parameter tuning, testing, and capacity assessment.

## 技术栈

System

## 核心贡献

_（待补充结构化分析）_

---

*导入自 NSDI2026 分析项目 | ID: nsdi26-006*
