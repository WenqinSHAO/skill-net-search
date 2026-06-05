---
id: arxiv-3054
title: "FIST: A Feature-Importance Sampling and Tree-Based Method for Automatic Design Flow Parameter Tuning"
conference: arXiv 2020
date: 2020-01
authors:
  - name: "Yanqing Zhang"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Brucek Khailany"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Zhiyao Xie"
    affiliation: ""
    is_industry: false
  - name: "Guan-Qi Fang"
    affiliation: ""
    is_industry: false
  - name: "Yu-Hung Huang"
    affiliation: ""
    is_industry: false
  - name: "Mark Haoxing Ren"
    affiliation: ""
    is_industry: false
  - name: "Shao-Yun Fang"
    affiliation: ""
    is_industry: false
  - name: "Jiang Hu"
    affiliation: ""
    is_industry: false
  - name: "Yiran Chen"
    affiliation: ""
    is_industry: false
  - name: "Erick Carvajal Barboza"
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
  - "Circuits and VLSI Design"
  - "Artificial Intelligence and Machine Learning"
abstract: "Design flow parameters are of utmost importance to chip design quality and require a painfully long time to evaluate their effects. In reality, flow parameter tuning is usually performed manually based on designers’ experience in an ad hoc manner. In this work, we introduce a machine learning based "
url: "https://research.nvidia.com/publication/2020-01_fist-feature-importance-sampling-and-tree-based-method-automatic-design-flow"
status: new
---

# FIST: A Feature-Importance Sampling and Tree-Based Method for Automatic Design Flow Parameter Tuning

## 摘要

Design flow parameters are of utmost importance to chip design quality and require a painfully long time to evaluate their effects. In reality, flow parameter tuning is usually performed manually based on designers’ experience in an ad hoc manner. In this work, we introduce a machine learning based automatic parameter tuning methodology that aims to find the best design quality with a limited number of trials. Instead of merely plugging in machine learning engines, we develop clustering and approximate sampling techniques for improving tuning efficiency. The feature extraction in this method can reuse knowledge from prior designs. Furthermore, we leverage a state-of-the-art XGBoost model and propose a novel dynamic tree technique to overcome overfitting. Experimental results on benchmark circuits show that our approach achieves 25% improvement in design quality or 37% reduction in sampling cost compared to random forest method, which is the kernel of a highly cited previous work. Our approach is further validated on two industrial designs. By sampling less than 0.02% of possible parameter sets, it reduces area by 1.83% and 1.43% compared to the best solutions hand-tuned by experienced designers.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
