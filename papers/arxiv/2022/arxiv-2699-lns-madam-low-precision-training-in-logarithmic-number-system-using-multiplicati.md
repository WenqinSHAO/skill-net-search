---
id: arxiv-2699
title: "LNS-Madam: Low-Precision Training in Logarithmic Number System Using Multiplicative Weight Update"
conference: arXiv 2022
date: 2022-12
authors:
  - name: "Steve Dai"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Rangharajan Venkatesan"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Brian Zimmer"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Ming-Yu Liu"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Brucek Khailany"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "William Dally"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Jiawei Zhao"
    affiliation: ""
    is_industry: false
  - name: "Mustafa Ali"
    affiliation: ""
    is_industry: false
  - name: "Anima Anandkumar"
    affiliation: ""
    is_industry: false
topics:
  - AI & Machine Learning
  - GPU_architecture
  - AI & Machine Learning
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Artificial Intelligence and Machine Learning"
  - "Circuits and VLSI Design"
  - "Computer Architecture"
external_links:
  - name: "IEEE Xplore"
    url: "https://ieeexplore.ieee.org/abstract/document/9900267"
abstract: "Representing deep neural networks (DNNs) in low-precision is a promising approach to enable efficient acceleration and memory reduction. Previous methods that train DNNs in low-precision typically keep a copy of weights in high-precision during the weight updates. Directly training with low-precisio"
url: "https://research.nvidia.com/publication/2022-12_lns-madam-low-precision-training-logarithmic-number-system-using-multiplicative"
status: new
---

# LNS-Madam: Low-Precision Training in Logarithmic Number System Using Multiplicative Weight Update

## 摘要

Representing deep neural networks (DNNs) in low-precision is a promising approach to enable efficient acceleration and memory reduction. Previous methods that train DNNs in low-precision typically keep a copy of weights in high-precision during the weight updates. Directly training with low-precision weights leads to accuracy degradation due to complex interactions between the low-precision number systems and the learning algorithms. To address this issue, we develop a co-designed low-precision training framework, termed LNS-Madam, in which we jointly design a logarithmic number system (LNS) and a multiplicative weight update algorithm (Madam). We prove that LNS-Madam results in low quantization error during weight updates, leading to stable performance even if the precision is limited. We further propose a hardware design of LNS-Madam that resolves practical challenges in implementing an efficient datapath for LNS computations. Our implementation effectively reduces energy overhead incurred by LNS-to-integer conversion and partial sum accumulation. Experimental results show that LNS-Madam achieves comparable accuracy to full-precision counterparts with only 8 bits on popular computer vision and natural language tasks. Compared to FP32 and FP8, LNS-Madam reduces the energy consumption by over 90% and 55%, respectively.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
