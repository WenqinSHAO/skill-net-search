---
id: arxiv-2928
title: "Flexion: A Quantitative Metric for Flexibility in DNN Accelerators"
conference: arXiv 2021
date: 2021-01
authors:
  - name: "Michael Pellauer"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Angshuman Parashar"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Hyoukjun Kwon"
    affiliation: ""
    is_industry: false
  - name: "Tushar Krishna"
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
  - "Computer Architecture"
external_links:
  - name: "IEEE Digital Library"
    url: "https://ieeexplore.ieee.org/document/9293373"
abstract: "Dataflow and tile size choices, which we collectively refer to as mappings, dictate the efficiency (i.e., latency and energy) of DNN accelerators. Rapidly evolving DNN models is one of the major challenges for DNN accelerators since the optimal mapping heavily depends on the layer shape and size. To"
url: "https://research.nvidia.com/publication/2021-01_flexion-quantitative-metric-flexibility-dnn-accelerators"
status: new
---

# Flexion: A Quantitative Metric for Flexibility in DNN Accelerators

## 摘要

Dataflow and tile size choices, which we collectively refer to as mappings, dictate the efficiency (i.e., latency and energy) of DNN accelerators. Rapidly evolving DNN models is one of the major challenges for DNN accelerators since the optimal mapping heavily depends on the layer shape and size. To maintain high efficiency across multiple DNN models, flexible accelerators that can support multiple mappings have emerged. However, we currently lack a metric to evaluate accelerator flexibility and quantitatively compare their capability to run different mappings. In this work, we formally define the concept of flexibility in DNN accelerators and propose flexion (flexibility fraction), flexion, which is a quantitative metric of mapping flexibility on DNN accelerators. We codify the formalism we construct and evaluate the flexibility of accelerators based on Eyeriss, NVDLA, and TPUv1. We show that Eyeriss-like accelerator is 2.2x and 17.0x more flexible (i.e., capable of running more mappings) than NVDLA and TPUv1-based accelerators on selected ResNet-50 and MobileNetV2 layers. This work is the first work to enable such a quantitative comparison of the flexibility of accelerators.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
