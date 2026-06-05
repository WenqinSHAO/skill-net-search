---
id: arxiv-2763
title: "A Formalism of DNN Accelerator Flexibility"
conference: arXiv 2022
date: 2022-06
authors:
  - name: "Michael Pellauer"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Angshuman Parashar"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Sheng-Chun Kao"
    affiliation: ""
    is_industry: false
  - name: "Hyoukjun Kwon"
    affiliation: ""
    is_industry: false
  - name: "Tushar Krishna"
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
  - name: "ACM Digital Library"
    url: "https://dl.acm.org/doi/abs/10.1145/3530907"
abstract: "The high efficiency of domain-specific hardware accelerators for machine learning (ML) has come from specialization, with the trade-off of less configurability/ flexibility. There is growing interest in developing flexible ML accelerators to make them future-proof to the rapid evolution of Deep Neur"
url: "https://research.nvidia.com/publication/2022-06_formalism-dnn-accelerator-flexibility"
status: new
---

# A Formalism of DNN Accelerator Flexibility

## 摘要

The high efficiency of domain-specific hardware accelerators for machine learning (ML) has come from specialization, with the trade-off of less configurability/ flexibility. There is growing interest in developing flexible ML accelerators to make them future-proof to the rapid evolution of Deep Neural Networks (DNNs). However, the notion of accelerator flexibility has always been used in an informal manner, restricting computer architects from conducting systematic apples-to-apples design-space exploration (DSE) across trillions of choices. In this work, we formally define accelerator flexibility and show how it can be integrated for DSE. Specifically, we capture DNN accelerator flexibility across four axes: tiling, ordering, parallelization, and array shape. We categorize existing accelerators into 16 classes based on their axes of flexibility support, and define a precise quantification of the degree of flexibility of an accelerator across each axis. We leverage these to develop a novel flexibility-aware DSE framework. We demonstrate how this can be used to perform first-of-their-kind evaluations, including an isolation study to identify the individual impact of the flexibility axes. We demonstrate that adding flexibility features to a hypothetical DNN accelerator designed in 2014 improves runtime on future (i.e., present-day) DNNs by 11.8× geomean.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
