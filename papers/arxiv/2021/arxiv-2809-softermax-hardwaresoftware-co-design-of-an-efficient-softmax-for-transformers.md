---
id: arxiv-2809
title: "Softermax: Hardware/Software Co-Design of an Efficient Softmax for Transformers"
conference: arXiv 2021
date: 2021-12
authors:
  - name: "Rangharajan Venkatesan"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Steve Dai"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Brucek Khailany"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Jacob R. Stevens"
    affiliation: ""
    is_industry: false
  - name: "Anand Raghunathan"
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
  - name: "Softermax: Hardware/Software Co-Design of an Efficient Softmax for Transformers"
    url: "https://arxiv.org/abs/2103.09301"
abstract: "Transformers have transformed the field of natural language processing. This performance is largely attributed to the use of stacked self-attention layers, each of which consists of matrix multiplies as well as softmax operations. As a result, unlike other neural networks, the softmax operation acco"
url: "https://research.nvidia.com/publication/2021-12_softermax-hardwaresoftware-co-design-efficient-softmax-transformers"
status: new
---

# Softermax: Hardware/Software Co-Design of an Efficient Softmax for Transformers

## 摘要

Transformers have transformed the field of natural language processing. This performance is largely attributed to the use of stacked self-attention layers, each of which consists of matrix multiplies as well as softmax operations. As a result, unlike other neural networks, the softmax operation accounts for a significant fraction of the total run-time of Transformers. To address this, we propose Softermax, a hardware-friendly softmax design. Softermax consists of base replacement, low-precision softmax computations, and an online normalization calculation. We show Softermax results in 2.35x the energy efficiency at 0.90x the size of a comparable baseline, with negligible impact on network accuracy.&nbsp; &nbsp; &nbsp;&nbsp;

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
