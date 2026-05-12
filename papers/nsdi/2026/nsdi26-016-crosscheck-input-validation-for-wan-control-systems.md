---
id: nsdi26-016
title: "CrossCheck: Input Validation for WAN Control Systems"
conference: NSDI 2026
date: 2026-03
authors:
  - name: "Alexander Krentsel,"
  - name: "UC Berkeley / Google"
  - name: "Rishabh Iyer,"
  - name: "UC Berkeley"
  - name: "Isaac Keslassy,"
  - name: "Technion / UC Berkeley"
topics:
  - Distributed Systems
tags:
  - distributed-systems
arxiv: ""
url: "https://www.usenix.org/conference/nsdi26/presentation/krentsel"
score: 8
status: analyzed
---

# CrossCheck: Input Validation for WAN Control Systems

**NSDI 2026** | Alexander Krentsel,; UC Berkeley / Google;; Rishabh Iyer,; UC Berkeley;; Isaac Keslassy,; Technion / UC Berkeley;; Sylvia Ratnasamy,; UC Berkeley / Go...


## 摘要

We present CrossCheck, a system that validates inputs to the Software-Defined Networking (SDN) controller in a Wide Area Network (WAN). By detecting incorrect inputs - often stemming from bugs in the SDN control infrastructure - CrossCheck alerts operators before they trigger network outages.   Our analysis at a large-scale WAN operator identifies invalid inputs as a leading cause of major outages, and we show how CrossCheck would have prevented those incidents. We deployed CrossCheck as a shadow validation system for four weeks in a production WAN, during which it accurately detected the single incident of invalid inputs that occurred while sustaining a 0% false positive rate under normal operation, hence imposing little additional burden on operators. In addition, we show through simulation that CrossCheck reliably detects a wide range of invalid inputs (e.g., detecting demand perturbations as small as 5% with 100% accuracy) and maintains a near-zero false positive rate for realistic levels of noisy, missing, or buggy telemetry data (e.g., sustaining zero false positives with up to 30% of corrupted telemetry data).

## 技术栈

System

## 核心贡献

_（待补充结构化分析）_

---

*导入自 NSDI2026 分析项目 | ID: nsdi26-016*
