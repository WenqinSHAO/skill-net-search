---
id: arxiv-2826
title: "Optimizing Selective Protection for CNN Resilience"
conference: arXiv 2021
date: 2021-10
authors:
  - name: "Siva Hari"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Charbel Sakr"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Pavlo Molchanov"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Michael B. Sullivan"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Steve Keckler"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Abdulrahman Mahmoud"
    affiliation: ""
    is_industry: false
  - name: "Christopher W. Fletcher"
    affiliation: ""
    is_industry: false
  - name: "Sarita V. Adve"
    affiliation: ""
    is_industry: false
  - name: "Naresh Shanbhag"
    affiliation: ""
    is_industry: false
  - name: "Timothy Tsai"
    affiliation: ""
    is_industry: false
topics:
  - AI & Machine Learning
  - GPU_architecture
  - Robotics_autonomous
  - AI & Machine Learning
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Artificial Intelligence and Machine Learning"
  - "Computer Architecture"
  - "Resilience and Safety"
external_links:
  - name: "IEEE Digital Library"
    url: "https://ieeexplore.ieee.org/document/9700317"
abstract: "As CNNs are being extensively employed in high performance and safety-critical applications that demand high reliability, it is important to ensure that they are resilient to transient hardware errors. Traditional full redundancy solutions provide high error coverage, but the associated overheads ar"
url: "https://research.nvidia.com/publication/2021-10_optimizing-selective-protection-cnn-resilience"
status: new
---

# Optimizing Selective Protection for CNN Resilience

## 摘要

As CNNs are being extensively employed in high performance and safety-critical applications that demand high reliability, it is important to ensure that they are resilient to transient hardware errors. Traditional full redundancy solutions provide high error coverage, but the associated overheads are often prohibitively high for resource-constrained systems. In this work, we propose software-directed selective protection techniques to target the most vulnerable work in a CNN, providing a low-cost solution. We propose and evaluate two domain-specific selective protection techniques for CNNs that target different granularities. First, we develop a feature-map level resilience technique (FLR), which identifies and statically protects the most vulnerable feature maps in a CNN. Second, we develop an inference level resilience technique (ILR), which selectively reruns vulnerable inferences by analyzing their output. Third, we show that the combination of both techniques (FILR) is highly efficient, achieving nearly full error coverage (99.78% on average) for quantized inferences via selective protection. Our tunable approach enables developers to evaluate CNN resilience to hardware errors before deployment using MAC operations as overhead for quicker trade-off analysis. For example, targeting 100% error coverage on ResNet50 with FILR requires 20.8% additional MACs, while measurements on a Jetson Xavier GPU shows 4.6% runtime overhead.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
