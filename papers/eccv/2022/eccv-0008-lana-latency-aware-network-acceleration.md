---
id: "eccv-0008"
title: "LANA: Latency Aware Network Acceleration"
conference: "ECCV 2022"
date: "2022-10"
authors:
  - name: "Pavlo Molchanov"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Jimmy Hall"
    affiliation: "Microsoft Research"
    is_industry: true
  - name: "Hongxu Danny Yin"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Jan Kautz"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Nicolo Fusi"
    affiliation: "Microsoft Research"
    is_industry: true
  - name: "Arash Vahdat"
    affiliation: "NVIDIA"
    is_industry: true
topics:
  - AI & Machine Learning
  - Computer Vision
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Artificial Intelligence and Machine Learning"
  - "Computer Vision"
abstract: "We introduce latency-aware network acceleration (LANA) - an approach that builds on neural architecture search techniques and teacher-student distillation to accelerate neural networks. LANA consists of two phases: in the first phase, it trains many alternative operations for every layer of the teac"
url: "https://research.nvidia.com/publication/2022-10_lana-latency-aware-network-acceleration"
status: "new"
---

# LANA: Latency Aware Network Acceleration

## 摘要

We introduce latency-aware network acceleration (LANA) - an approach that builds on neural architecture search techniques and teacher-student distillation to accelerate neural networks. LANA consists of two phases: in the first phase, it trains many alternative operations for every layer of the teacher network using layer-wise feature map distillation. In the second phase, it solves the combinatorial selection of efficient operations using a novel constrained integer linear optimization (ILP) approach. ILP brings unique properties as it (i) performs NAS within a few seconds to minutes, (ii) easily satisfies budget constraints, (iii) works on the layer-granularity, (iv) supports a huge search space&nbsp;O(10^100), surpassing prior search approaches in efficacy and efficiency. In extensive experiments, we show that LANA yields efficient and accurate models constrained by a target latency budget while being significantly faster than other techniques. We analyze three popular network architectures: EfficientNetV1, EfficientNetV2, and ResNeST, and achieve accuracy improvement for all models (up to&nbsp;3.0%) when compressing larger models to the latency level of smaller models. LANA achieves significant speed-ups (up to&nbsp;5×) with minor to no accuracy drop on GPU and CPU. The code will be shared soon.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
