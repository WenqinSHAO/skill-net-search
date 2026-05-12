---
id: nsdi26-060
title: "Harvesting Spare CPU Resources in Container Systems"
conference: NSDI 2026
date: 2026-03
authors:
  - name: "Adam Hall and Anirudh Sarma,"
  - name: "Georgia Institute of Technology"
  - name: "Esha Choukse,"
  - name: "Microsoft Azure Research"
  - name: "Umakishore Ramachandran,"
  - name: "Georgia Institute of Technology"
topics:
  - Distributed Systems
tags:
  - distributed-systems
arxiv: ""
url: "https://www.usenix.org/conference/nsdi26/presentation/hall"
score: 8
status: analyzed
---

# Harvesting Spare CPU Resources in Container Systems

**NSDI 2026** | Adam Hall and Anirudh Sarma,; Georgia Institute of Technology;; Esha Choukse,; Microsoft Azure Research;; Umakishore Ramachandran,; Georgia Institute ...


## 摘要

Platforms like Kubernetes are widely adopted for deploying latency-sensitive cloud services in containers, and CPU resources for these containers are over-provisioned to ensure low 99th percentile tail latency under peak load. At the same time, cloud services exhibit bursty traffic patterns resulting in CPU usage variability that creates opportunity to harvest ephemerally unused CPU cores to run latency-tolerant containers. However, existing resource controls do not allow latency-sensitive containers to share unused cores without compromising their low tail latency objectives. Prior research on performance isolation is inadequate for container systems because it requires modifying applications and system software, employs offline profiling, and does not account for interference from processing container networking interrupts. We present HarvestContainers , a system that protects latency-sensitive containers from all sources of interference while harvesting their spare CPU cores to run latency-tolerant containers. Our solution dynamically determines the safe number of CPU cores to harvest and does not require rewriting applications or OS. We implement HarvestContainers integrated with Kubernetes and evaluate it experimentally. Our evaluation shows that latency-sensitive containers with microsecond-scale service level objectives can share up to 75% of their unused CPU cores while maintaining tail latency within 4% of standalone operation.

## 技术栈

System

## 核心贡献

_（待补充结构化分析）_

---

*导入自 NSDI2026 分析项目 | ID: nsdi26-060*
