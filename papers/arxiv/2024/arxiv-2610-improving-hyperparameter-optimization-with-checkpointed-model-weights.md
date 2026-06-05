---
id: arxiv-2610
title: "Improving Hyperparameter Optimization with Checkpointed Model Weights"
conference: arXiv 2024
date: 2024-06
authors:
  - name: "Nikhil Mehta"
    affiliation: ""
    is_industry: false
  - name: "Jonathan Lorraine"
    affiliation: ""
    is_industry: false
  - name: "Steve Masson"
    affiliation: ""
    is_industry: false
  - name: "Ramanathan Arunachalam"
    affiliation: ""
    is_industry: false
  - name: "Zaid Pervaiz Bhat"
    affiliation: ""
    is_industry: false
  - name: "James Lucas"
    affiliation: ""
    is_industry: false
  - name: "Arun George Zachariah"
    affiliation: ""
    is_industry: false
topics:
  - AI & Machine Learning
  - CUDA_ecosystem
  - AI & Machine Learning
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Algorithms and Numerical Methods"
  - "Artificial Intelligence and Machine Learning"
external_links:
  - name: "Project Page"
    url: "https://research.nvidia.com/labs/toronto-ai/FMS/"
  - name: "Code"
    url: "https://github.com/NVlabs/forecasting-model-search"
abstract: "When training deep learning models, the performance depends largely on the selected hyperparameters. However, hyperparameter optimization (HPO) is often one of the most expensive parts of model design. Classical HPO methods treat this as a black-box optimization problem. However, gray-box HPO method"
url: "https://research.nvidia.com/publication/2024-06_improving-hyperparameter-optimization-checkpointed-model-weights"
status: new
---

# Improving Hyperparameter Optimization with Checkpointed Model Weights

## 摘要

When training deep learning models, the performance depends largely on the selected hyperparameters. However, hyperparameter optimization (HPO) is often one of the most expensive parts of model design. Classical HPO methods treat this as a black-box optimization problem. However, gray-box HPO methods, which incorporate more information about the setup, have emerged as a promising direction for more efficient optimization. For example, we can use intermediate loss evaluations to terminate bad selections. In this work, we propose an HPO method for neural networks that uses logged checkpoints of the trained weights to guide future hyperparameter selections. Our Forecasting Model Search (FMS) method embeds weights into a Gaussian process deep kernel surrogate model, to be data-efficient with the logged network weights. To facilitate reproducibility and further research, we&nbsp;open-source our code.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
