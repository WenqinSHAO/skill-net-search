---
id: arxiv-2754
title: "Ruby: Improving Hardware Efficiency for Tensor Algebra Accelerators Through Imperfect Factorization"
conference: arXiv 2022
date: 2022-06
authors:
  - name: "Po-An Tsai"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Angshuman Parashar"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Joel Emer"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Mark Horeni"
    affiliation: ""
    is_industry: false
  - name: "Pooria Taheri"
    affiliation: ""
    is_industry: false
  - name: "Siddharth Joshi"
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
external_links:
  - name: "IEEE Digital Library"
    url: "https://ieeexplore.ieee.org/document/9804679"
abstract: "Finding high-quality mappings of Deep Neural Network (DNN) models onto tensor accelerators is critical for efficiency. State-of-the-art mapping exploration tools use remainderless (i.e., perfect) factorization to allocate hardware resources, through tiling the tensors, based on factors of tensor dim"
url: "https://research.nvidia.com/publication/2022-06_ruby-improving-hardware-efficiency-tensor-algebra-accelerators-through"
status: new
---

# Ruby: Improving Hardware Efficiency for Tensor Algebra Accelerators Through Imperfect Factorization

## 摘要

Finding high-quality mappings of Deep Neural Network (DNN) models onto tensor accelerators is critical for efficiency. State-of-the-art mapping exploration tools use remainderless (i.e., perfect) factorization to allocate hardware resources, through tiling the tensors, based on factors of tensor dimensions. This limits the size of the search space, (i.e., mapspace), but can lead to low resource utilization. We introduce a new mapspace, Ruby, that adds remainders (i.e., imperfect factorization) to expand the mapspace with high-quality mappings for user-defined architectures. This expansion allows us to allocate resources more precisely by generating tile sizes that better conform to hardware resources. However, this mapspace expansion also incurs an increase in the number of unique mappings. Consequently, this paper studies the trade-off between Ruby’s mapspace expansion and mapping quality. We propose Ruby-S (Spatial) to only employ imperfect factorization towards improved parallelism. Ruby-S incurs a moderate mapspace expansion while reducing energy-delay product (EDP) up to 50% when implementing ResNet-50 on an Eyeriss-like architecture with an average improvement of 20%. For the most part, this improvement can be attributed to higher compute utilization. EDP on a Simba-like architecture improves up to 40% with an average of 10%. For DeepBench workloads Ruby-S yields improvements of up to 45% with an average improvement of 10% on an Eyeriss-like architecture. Ruby-S is robust to accelerator configurations and improves EDP by 20% on average, with a maximum improvement of 55% when implementing ResNet-50 on different accelerator configurations. Ruby-S mappings form a new Pareto frontier, improving the performance of previous configurations by an average of 30% and 20% for ResNet-50 and DeepBench workloads respectively.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
