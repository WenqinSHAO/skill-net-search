---
id: nsdi26-013
title: "ZooRoute: Enhancing Cloud-Scale Network Reliability via Candidate Path Provisioning and Overlay Proactive Rerouting"
conference: NSDI 2026
date: 2026-03
authors:
  - name: "Xiaoqing Sun,"
  - name: "Alibaba Cloud"
  - name: "Xing Li,"
  - name: "Zhejiang University and Alibaba Cloud"
  - name: "Xionglie Wei, Tian Pan, Ju Zhang, Bowen Yang, Yi Wang, Ye Yang, Yu Qi, and Le Yu,"
  - name: "Alibaba Cloud"
topics:
  - Distributed Systems
tags:
  - distributed-systems
arxiv: ""
url: "https://www.usenix.org/conference/nsdi26/presentation/sun"
score: 8
status: analyzed
---

# ZooRoute: Enhancing Cloud-Scale Network Reliability via Candidate Path Provisioning and Overlay Proactive Rerouting

**NSDI 2026** | Xiaoqing Sun,; Alibaba Cloud;; Xing Li,; Zhejiang University and Alibaba Cloud;; Xionglie Wei, Tian Pan, Ju Zhang, Bowen Yang, Yi Wang, Ye Yang, Yu Qi...


## 摘要

This paper presents ZooRoute, a tenant-transparent, fast failure recovery service that requires no modifications to physical devices. ZooRoute leverages the overlay layer and enables traffic flows to bypass failures by altering source ports (srcPorts) in packet headers during encapsulation. To enable deployment in large-scale cloud networks, ZooRoute proposes: 1) On-demand probing to efficiently monitor a vast number of hosts while minimizing telemetry costs. 2) Table compression to record the states of numerous paths with limited on-chip resources. 3) A device-sensing mechanism to prevent unnecessary reconnections in stateful forwarding. Deployed in Alibaba Cloud for 18 months, ZooRoute has significantly improved network reliability, reducing cumulative outage time by 92.71%.

## 技术栈

System

## 核心贡献

_（待补充结构化分析）_

---

*导入自 NSDI2026 分析项目 | ID: nsdi26-013*
