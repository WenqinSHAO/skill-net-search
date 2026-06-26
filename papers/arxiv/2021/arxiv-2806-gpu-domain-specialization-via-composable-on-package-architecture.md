---
id: "arxiv-2806"
title: "GPU Domain Specialization via Composable On-Package Architecture"
conference: "arXiv 2021"
date: "2021-12"
authors:
  - name: "Yaosheng Fu"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Evgeny Bolotin"
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
topics:
  - GPU_architecture
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Computer Architecture"
external_links:
  - name: "ACM Digital Library"
    url: "https://dl.acm.org/doi/full/10.1145/3484505"
abstract: "As GPUs scale their low-precision matrix math throughput to boost deep learning (DL) performance, they&nbsp;upset the balance between math throughput and memory system capabilities. We demonstrate that a converged&nbsp;GPU design trying to address diverging architectural requirements between FP32 (o"
url: "https://research.nvidia.com/publication/2021-12_gpu-domain-specialization-composable-package-architecture"
status: "new"
---

# GPU Domain Specialization via Composable On-Package Architecture

## 摘要

As GPUs scale their low-precision matrix math throughput to boost deep learning (DL) performance, they&nbsp;upset the balance between math throughput and memory system capabilities. We demonstrate that a converged&nbsp;GPU design trying to address diverging architectural requirements between FP32 (or larger)-based&nbsp;HPC and FP16 (or smaller)-based DL workloads results in sub-optimal configurations for either of the application&nbsp;domains. We argue that a Composable On-PAckage GPU (COPA-GPU) architecture to provide&nbsp;domain-specialized GPU products is the most practical solution to these diverging requirements. A COPA-GPU&nbsp;leverages multi-chip-module disaggregation to support maximal design reuse, along with memory system&nbsp;specialization per application domain. We show how a COPA-GPU enables DL-specialized products by&nbsp;modular augmentation of the baseline GPU architecture with up to 4× higher off-die bandwidth, 32× larger&nbsp;on-package cache, and 2.3× higher DRAM bandwidth and capacity, while conveniently supporting scaled-down&nbsp;HPC-oriented designs. This work explores the microarchitectural design necessary to enable composable&nbsp;GPUs and evaluates the benefits composability can provide to HPC, DL training, and DL inference. We&nbsp;show that when compared to a converged GPU design, a DL-optimized COPA-GPU featuring a combination&nbsp;of 16× larger cache capacity and 1.6× higher DRAM bandwidth scales per-GPU training and inference performance&nbsp;by 31% and 35%, respectively, and reduces the number of GPU instances by 50% in scale-out training&nbsp;scenarios.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
