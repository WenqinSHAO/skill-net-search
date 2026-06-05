---
id: arxiv-2689
title: "BufFormer: A Generative ML Framework for Scalable Buffering"
conference: arXiv 2023
date: 2023-01
authors:
  - name: "Rongjian Liang"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Siddhartha Nath"
    affiliation: ""
    is_industry: false
  - name: "Anand Rajaram"
    affiliation: ""
    is_industry: false
  - name: "Jiang Hu"
    affiliation: ""
    is_industry: false
  - name: "Mark Haoxing Ren"
    affiliation: ""
    is_industry: false
topics:
  - Foundation_models
  - GPU_architecture
  - AI & Machine Learning
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Circuits and VLSI Design"
  - "Generative AI"
external_links:
  - name: "https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&amp;arnumber=10044843"
    url: "https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&amp;arnumber=10044843"
abstract: "Buffering is a prevalent interconnect optimization technique to help timing closure and is often performed after placement. A common buffering approach is to construct a Steiner tree and then buffers are inserted on the tree based on Ginneken-Lillis style algorithm. Such an approach is difficult to "
url: "https://research.nvidia.com/publication/2023-01_bufformer-generative-ml-framework-scalable-buffering"
status: new
---

# BufFormer: A Generative ML Framework for Scalable Buffering

## 摘要

Buffering is a prevalent interconnect optimization technique to help timing closure and is often performed after placement. A common buffering approach is to construct a Steiner tree and then buffers are inserted on the tree based on Ginneken-Lillis style algorithm. Such an approach is difficult to scale with large nets. Our work attempts to solve this problem with a generative machine-learning (ML) approach without Steiner tree construction. Our approach can extract and reuse knowledge from high quality samples and therefore has significantly improved scalability. A generative ML framework, BufFormer, is proposed to construct abstract tree topol-ogy while simultaneously determining buffer sizes &amp; locations. A baseline method, FLUTE-based Steiner tree construction followed by Ginneken-Lillis style buffer insertion, is implemented to generate training samples. After training, BufFormer can produce solutions for unseen nets highly comparable to baseline results with a correlation coefficient 0.977 in terms of buffer area and 0.934 for driver-sink delays. On average, BufFormer-generated tree achieves similar de-lays with slightly larger buffer area. And up to 160X speedup can be achieved for large nets when running on a GPU over the baseline on a single CPU thread.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
