---
id: nsdi26-043
title: "HEDGE: Traffic Engineering with Probabilistic Link Capacities"
conference: NSDI 2026
date: 2026-03
authors:
  - name: "Arjun Devraj,"
  - name: "Cornell University"
  - name: "Bill Owens,"
  - name: "NYSERNet"
  - name: "Umesh Krishnaswamy,"
  - name: "Microsoft"
topics:
  - Distributed Systems
tags:
  - distributed-systems
arxiv: ""
url: "https://www.usenix.org/conference/nsdi26/presentation/devraj"
score: 8
status: analyzed
---

# HEDGE: Traffic Engineering with Probabilistic Link Capacities

**NSDI 2026** | Arjun Devraj,; Cornell University;; Bill Owens,; NYSERNet;; Umesh Krishnaswamy,; Microsoft;; Ying Zhang,; Meta;; Rachee Singh,; Cornell University


## 摘要

Cloud providers have adopted higher modulation formats to achieve higher data-rate wavelengths in their optical wide-area networks. However, higher modulation formats reduce signal quality margins, making wavelengths more susceptible to wavelength-specific faults (WSFs)—temporary faults that selectively affect certain wavelengths while others remain unaffected, even though they all share the same optical fiber and equipment. WSFs cause the capacity of inter-datacenter links to fluctuate, frequently disrupting traffic engineering systems. We propose HEDGE, a system that mitigates the effects of WSFs by implementing link-local resilience and global network-wide resilience against WSFs. For local resilience, HEDGE provisions inter-datacenter links with a guaranteed minimum capacity and availability target, in spite of WSFs, while using the fewest possible constituent wavelengths. For global resilience, HEDGE optimally balances throughput and availability while allocating flows on a stochastic wide-area network with fluctuating link capacities. HEDGE sustains equivalent throughput with state-of-the-art traffic engineering systems, while dropping 12.2× less network flow in worst-case scenarios and reducing disruptions to tunnel allocations by 622× in spite of a rapidly changing topology.

## 技术栈

Algorithm

## 核心贡献

_（待补充结构化分析）_

---

*导入自 NSDI2026 分析项目 | ID: nsdi26-043*
