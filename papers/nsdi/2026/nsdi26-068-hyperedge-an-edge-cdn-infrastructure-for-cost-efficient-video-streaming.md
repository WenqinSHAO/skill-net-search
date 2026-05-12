---
id: nsdi26-068
title: "HyperEdge: An Edge CDN Infrastructure for Cost Efficient Video Streaming"
conference: NSDI 2026
date: 2026-03
authors:
  - name: "Dehui Wei,"
  - name: "National University of Singapore"
  - name: "Jiao Zhang,"
  - name: "Beijing University of Posts and Telecommunications, and Purple Mountain Laboratories"
  - name: "Haozhe Li, Rui Han, Zhichen Xue, Yajie Peng, Xiaofei Pang, and Yan Ma,"
  - name: "ByteDance"
topics:
  - Distributed Systems
tags:
  - distributed-systems
arxiv: ""
url: "https://www.usenix.org/conference/nsdi26/presentation/wei"
score: 8
status: analyzed
---

# HyperEdge: An Edge CDN Infrastructure for Cost Efficient Video Streaming

**NSDI 2026** | Dehui Wei,; National University of Singapore;; Jiao Zhang,; Beijing University of Posts and Telecommunications, and Purple Mountain Laboratories;; Hao...


## 摘要

As ByteDance’s business expands, the cost of video streaming using content delivery networks (CDN) has become prohibitively high. We have discovered a sea of under-utilized edge devices with the potential to reduce content distribution cost. The unreliable performance of an edge network, however, presents deep challenges to video streaming services. In this work, we introduce HyperEdge, an edge-assisted content delivery system for video streaming. HyperEdge seamlessly integrates the robustness of a conventional CDN with the cost-efficiency of an edge network. It offers dependable streaming quality to users while minimizing traffic expenses. HyperEdge employs a centralized tracker cluster to optimize content distribution to a pool of edge devices, based on real-time monitoring. To ensure satisfactory video playback quality, we develop a novel multi-path protocol for client-edge video transmission. Having been in stable operation for six years, HyperEdge manages over a hundred thousand edge devices, serving about a hundred million users daily, and saving hundreds of millions of dollars in content delivery cost annually.

## 技术栈

System

## 核心贡献

_（待补充结构化分析）_

---

*导入自 NSDI2026 分析项目 | ID: nsdi26-068*
