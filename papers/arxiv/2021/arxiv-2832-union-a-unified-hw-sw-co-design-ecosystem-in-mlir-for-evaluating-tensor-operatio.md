---
id: arxiv-2832
title: "Union: A Unified HW-SW Co-Design Ecosystem in MLIR for Evaluating Tensor Operations on Spatial Accelerators"
conference: arXiv 2021
date: 2021-09
authors:
  - name: "Angshuman Parashar"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Po-An Tsai"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Geonhwa Jeong"
    affiliation: ""
    is_industry: false
  - name: "Gokcen Kestor"
    affiliation: ""
    is_industry: false
  - name: "Prasanth Chatarasi"
    affiliation: ""
    is_industry: false
  - name: "Sivasankaran Rajamanickam"
    affiliation: ""
    is_industry: false
  - name: "Roberto Gioiosa"
    affiliation: ""
    is_industry: false
  - name: "Tushar Krishna"
    affiliation: ""
    is_industry: false
topics:
  - AI & Machine Learning
  - CUDA_ecosystem
  - GPU_architecture
  - AI & Machine Learning
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Artificial Intelligence and Machine Learning"
  - "Computer Architecture"
  - "Programming Languages, Systems and Tools"
external_links:
  - name: "IEEE Digital Library"
    url: "https://ieeexplore.ieee.org/document/9563040"
abstract: "To meet the extreme compute demands for deep learning across commercial and scientific applications, dataflow accelerators are becoming increasingly popular. While these “domain-specific” accelerators are not fully programmable like CPUs and GPUs, they retain varying levels of flexibility with respe"
url: "https://research.nvidia.com/publication/2021-09_union-unified-hw-sw-co-design-ecosystem-mlir-evaluating-tensor-operations"
status: new
---

# Union: A Unified HW-SW Co-Design Ecosystem in MLIR for Evaluating Tensor Operations on Spatial Accelerators

## 摘要

To meet the extreme compute demands for deep learning across commercial and scientific applications, dataflow accelerators are becoming increasingly popular. While these “domain-specific” accelerators are not fully programmable like CPUs and GPUs, they retain varying levels of flexibility with respect to data orchestration, i.e., dataflow and tiling optimizations to enhance efficiency. There are several challenges when designing new algorithms and mapping approaches to execute the algorithms for a target problem on new hardware. Previous works have addressed these challenges individually. To address this challenge as a whole, in this work, we present a HW-SW co-design ecosystem for spatial accelerators called Union1 within the popular MLIR compiler infrastructure. Our framework allows exploring different algorithms and their mappings on several accelerator cost models. Union also includes a plug-and-play library of accelerator cost models and mappers which can easily be extended. The algorithms and accelerator cost models are connected via a novel mapping abstraction that captures the map space of spatial accelerators which can be systematically pruned based on constraints from the hardware, workload, and mapper. We demonstrate the value of Union for the community with several case studies which examine offloading different tensor operations (CONV/GEMM/Tensor Contraction) on diverse accelerator architectures using different mapping schemes.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
