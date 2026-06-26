---
id: "arxiv-2688"
title: "A 95.6-TOPS/W Deep Learning Inference Accelerator With Per-Vector Scaled 4-bit Quantization in 5 nm"
conference: "arXiv 2023"
date: "2023-01"
authors:
  - name: "Ben Keller"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Rangharajan Venkatesan"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Steve Dai"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Stephen Tell"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Brian Zimmer"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Charbel Sakr"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "William Dally"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Tom Gray"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Brucek Khailany"
    affiliation: "NVIDIA"
    is_industry: true
topics:
  - AI & Machine Learning
  - GPU_architecture
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Artificial Intelligence and Machine Learning"
  - "Circuits and VLSI Design"
  - "Computer Architecture"
abstract: "The energy efficiency of deep neural network (DNN) inference can be improved with custom accelerators. DNN inference accelerators often employ specialized hardware techniques to improve energy efficiency, but many of these techniques result in catastrophic accuracy loss on transformer-based DNNs, wh"
url: "https://research.nvidia.com/publication/2023-01_956-topsw-deep-learning-inference-accelerator-vector-scaled-4-bit-quantization"
status: "new"
---

# A 95.6-TOPS/W Deep Learning Inference Accelerator With Per-Vector Scaled 4-bit Quantization in 5 nm

## 摘要

The energy efficiency of deep neural network (DNN) inference can be improved with custom accelerators. DNN inference accelerators often employ specialized hardware techniques to improve energy efficiency, but many of these techniques result in catastrophic accuracy loss on transformer-based DNNs, which have become ubiquitous for natural language processing (NLP) tasks. This article presents a DNN accelerator designed for efficient execution of transformers. The proposed accelerator implements per-vector scaled quantization (VSQ), which employs an independent scale factor for each 64-element vector to enable the use of 4-bit arithmetic with little accuracy loss and low energy overhead. Using a multilevel dataflow to maximize reuse, the 5-nm prototype achieves 95.6 tera-operations per second per Watt (TOPS/W) at 0.46 V on a 4-bit benchmarking layer with VSQ. At a nominal voltage of 0.67 V, the accelerator achieves 1734 inferences/s/W (38.7 TOPS/W) with only 0.7% accuracy loss on BERT-Base and 4714 inferences/s/W (38.6 TOPS/W) with 0.15% accuracy loss on ResNet-50 by using quantization-aware fine-tuning to recover accuracy, demonstrating a practical accelerator design for energy-efficient DNN inference.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
