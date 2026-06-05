---
id: arxiv-2886
title: "GPU Domain Specialization via Composable On-Package Architecture"
conference: arXiv 2021
date: 2021-04
authors:
  - name: "Yaosheng Fu"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Niladrish Chatterjee"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "David Nellans"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Steve Keckler"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Evgeny Bolotin"
    affiliation: ""
    is_industry: false
topics:
  - GPU_architecture
  - AI & Machine Learning
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Computer Architecture"
abstract: "As GPUs scale their low precision matrix math throughput to boost deep learning (DL) performance, they upset the balance between math throughput and memory system capabilities. We demonstrate that converged GPU design trying to address diverging architectural requirements between FP32 (or larger) ba"
url: "https://research.nvidia.com/publication/2021-04_gpu-domain-specialization-composable-package-architecture"
status: new
---

# GPU Domain Specialization via Composable On-Package Architecture

## 摘要

As GPUs scale their low precision matrix math throughput to boost deep learning (DL) performance, they upset the balance between math throughput and memory system capabilities. We demonstrate that converged GPU design trying to address diverging architectural requirements between FP32 (or larger) based HPC and FP16 (or smaller) based DL workloads results in sub-optimal configuration for either of the application domains. We argue that a Composable On-PAckage GPU (COPAGPU) architecture to provide domain-specialized GPU products is the most practical solution to these diverging requirements. A COPA-GPU leverages multi-chip-module disaggregation to support maximal design reuse, along with memory system specialization per application domain. We show how a COPA-GPU enables DL-specialized products by modular augmentation of the baseline GPU architecture with up to 4x higher off-die bandwidth, 32x larger on-package cache, 2.3x higher DRAM bandwidth and capacity, while conveniently supporting scaled-down HPC-oriented designs. This work explores the microarchitectural design necessary to enable composable GPUs and evaluates the benefits composability can provide to HPC, DL training, and DL inference. We show that when compared to a converged GPU design, a DL-optimized COPA-GPU featuring a combination of 16x larger cache capacity and 1.6x higher DRAM bandwidth scales per-GPU training and inference performance by 31% and 35% respectively and reduces the number of GPU instances by 50% in scale-out training scenarios.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
