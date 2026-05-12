---
id: nsdi26-040
title: "Controlling Arbitrary Internet Queues with Titrate"
conference: NSDI 2026
date: 2026-03
authors:
  - name: "Anchengcheng Zhou and Joshua Lau,"
  - name: "Princeton University"
  - name: "P. Brighten Godfrey,"
  - name: "University of Illinois Urbana–Champaign and Broadcom"
  - name: "Maria Apostolaki,"
  - name: "Princeton University"
topics:
  - Distributed Systems
tags:
  - distributed-systems
arxiv: ""
url: "https://www.usenix.org/conference/nsdi26/presentation/zhou-titrate"
score: 8
status: analyzed
---

# Controlling Arbitrary Internet Queues with Titrate

**NSDI 2026** | Anchengcheng Zhou and Joshua Lau,; Princeton University;; P. Brighten Godfrey,; University of Illinois Urbana–Champaign and Broadcom;; Maria Apostolak...


## 摘要

Router buffers are critical to networks for absorbing short-lived congestion and allowing full throughput. However, excessive buffering can lead to high queuing delay, poor burst absorption, and even low throughput for queues sharing the buffer memory. Existing queue management schemes designed for Internet routers (e.g., CoDel, PIE) prevent such excessive buffering only under stringent assumptions about the queue composition (flows in the queue), while more recent approaches (e.g., L4S) require end-host collaboration. In this work, we revisit queue management for Internet routers from first principles and introduce Titrate, a closed-loop controller that senses queue dynamics and adjusts thresholds for any given queue to achieve high throughput, low latency and effective burst absorption. To balance convergence speed and stability, Titrate draws inspiration from TCP’s control loop, combining a multiplicative-increase-additive-decrease approach with an ssthresh-like variable. We evaluate Titrate’s performance via simulation and Internet experiments. Across a wide range of realistic traffic mixes, Titrate increases minimum throughput by 39%, 14% compared to CoDel, PIE, while keeping 59% lower queuing latency compared to static-threshold baselines of on-par throughput. It also improves end-user quality of experience over static-threshold baselines. We further show that Titrate reacts swiftly to bandwidth and traffic changes and offers device-wide benefits.

## 技术栈

Protocol

## 核心贡献

_（待补充结构化分析）_

---

*导入自 NSDI2026 分析项目 | ID: nsdi26-040*
