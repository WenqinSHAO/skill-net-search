---
id: "arxiv-2618"
title: "Learning to Compare Hardware Designs for High-Level Synthesis"
conference: "arXiv 2024"
date: "2024-05"
authors:
  - name: "Yunsheng Bai"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Atefeh Sohrabizadeh"
    affiliation: "UCLA"
    is_industry: false
  - name: "Zijian Ding"
    affiliation: "UCLA"
    is_industry: false
  - name: "Rongjian Liang"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Weikai Li"
    affiliation: "UCLA"
    is_industry: false
  - name: "Ding Wang"
    affiliation: "UCLA"
    is_industry: false
  - name: "Mark Haoxing Ren"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Yizhou Sun"
    affiliation: "UCLA"
    is_industry: false
  - name: "Jason Cong"
    affiliation: "UCLA"
    is_industry: false
topics:
  - AI & Machine Learning
  - GPU_architecture
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Artificial Intelligence and Machine Learning"
  - "Circuits and VLSI Design"
external_links:
  - name: "Paper"
    url: "https://arxiv.org/abs/2409.13138"
abstract: "High-level synthesis (HLS) is an automated design process that transforms high-level code into optimized hardware designs, enabling the rapid development of efficient hardware accelerators for various applications such as image processing, machine learning, and signal processing. To achieve optimal "
url: "https://research.nvidia.com/publication/2024-05_learning-compare-hardware-designs-high-level-synthesis"
status: "new"
---

# Learning to Compare Hardware Designs for High-Level Synthesis

## 摘要

High-level synthesis (HLS) is an automated design process that transforms high-level code into optimized hardware designs, enabling the rapid development of efficient hardware accelerators for various applications such as image processing, machine learning, and signal processing. To achieve optimal performance, HLS tools rely on pragmas, which are directives inserted into the source code to guide the synthesis process, and these pragmas can have various settings and values that significantly impact the resulting hardware design. State-of-the-art ML-based HLS methods, such as harp, first train a deep learning model, typically based on graph neural networks (GNNs) applied to graph-based representations of the source code and its pragmas. They then perform design space exploration (DSE) to explore the pragma design space, rank candidate designs using the trained model, and return the top designs as the final designs. However, traditional DSE methods face challenges due to the highly nonlinear relationship between pragma settings and performance metrics, along with complex interactions between pragmas that affect performance in non-obvious ways.&nbsp;

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
