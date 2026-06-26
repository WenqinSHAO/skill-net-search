---
id: "arxiv-2916"
title: "SNAP: An Efficient Sparse Neural Acceleration Processor for Unstructured Sparse Deep Neural Network Inference"
conference: "arXiv 2021"
date: "2021-02"
authors:
  - name: "Jie-Fang Zhang"
    affiliation: "University of Michigan"
    is_industry: false
  - name: "Ching-En Lee"
    affiliation: "McKinsey and Company"
    is_industry: false
  - name: "Chester Liu"
    affiliation: "University of Michigan"
    is_industry: false
  - name: "Yakun Sophia Shao"
    affiliation: "UC Berkeley"
    is_industry: false
  - name: "Steve Keckler"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Zhengya Zhang"
    affiliation: "University of Michigan"
    is_industry: false
topics:
  - GPU_architecture
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Computer Architecture"
external_links:
  - name: "Published manuscript (IEEE Digital Library)"
    url: "https://ieeexplore.ieee.org/document/9310233"
abstract: "Recent developments in deep neural network (DNN) pruning introduces data sparsity to enable deep learning applications to run more efficiently on resourceand energy-constrained hardware platforms. However, these sparse models require specialized hardware structures to exploit the sparsity for storag"
url: "https://research.nvidia.com/publication/2021-02_snap-efficient-sparse-neural-acceleration-processor-unstructured-sparse-deep"
status: "new"
---

# SNAP: An Efficient Sparse Neural Acceleration Processor for Unstructured Sparse Deep Neural Network Inference

## 摘要

Recent developments in deep neural network (DNN) pruning introduces data sparsity to enable deep learning applications to run more efficiently on resourceand energy-constrained hardware platforms. However, these sparse models require specialized hardware structures to exploit the sparsity for storage, latency, and efficiency improvements to the full extent. In this work, we present the sparse neural acceleration processor (SNAP) to exploit unstructured sparsity in DNNs. SNAP uses parallel associative search to discover valid weight (W) and input activation (IA) pairs from compressed, unstructured, sparse W and IA data arrays. The associative search allows SNAP to maintain a 75% average compute utilization. SNAP follows a channel-first dataflow and uses a two-level partial sum (psum) reduction dataflow to eliminate access contention at the output buffer and cut the psum writeback traffic by 22× compared with state-of-the-art DNN accelerator designs. SNAP's psum reduction dataflow can be configured in two modes to support general convolution (CONV) layers, pointwise CONV, and fully connected layers. A prototype SNAP chip is implemented in a 16-nm CMOS technology. The 2.3-mm^2 test chip is measured to achieve a peak effectual efficiency of 21.55 TOPS/W (16 b) at 0.55 V and 260 MHz for CONV layers with 10% weight and activation densities. Operating on a pruned ResNet-50 network, the test chip achieves a peak throughput of 90.98 frames/s at 0.80 V and 480 MHz, dissipating 348 mW.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
