---
id: "arxiv-2651"
title: "Guided Deep Kernel Learning"
conference: "arXiv 2023"
date: "2023-08"
authors:
  - name: "Idan Achituve"
    affiliation: "Bar-Ilan University"
    is_industry: false
  - name: "Gal Chechik"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Ethan Fetaya"
    affiliation: "Bar-Ilan University"
    is_industry: false
topics:
  - AI & Machine Learning
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Artificial Intelligence and Machine Learning"
external_links:
  - name: "Arxiv"
    url: "https://arxiv.org/abs/2302.09574"
  - name: "UAI 2023"
    url: "https://www.auai.org/uai2023/"
abstract: "Combining Gaussian processes with the expressive power of deep neural networks is commonly done nowadays through deep kernel learning (DKL). Unfortunately, due to the kernel optimization process, this often results in losing their Bayesian benefits. In this study, we present a novel approach for lea"
url: "https://research.nvidia.com/publication/2023-08_guided-deep-kernel-learning"
status: "new"
---

# Guided Deep Kernel Learning

## 摘要

Combining Gaussian processes with the expressive power of deep neural networks is commonly done nowadays through deep kernel learning (DKL). Unfortunately, due to the kernel optimization process, this often results in losing their Bayesian benefits. In this study, we present a novel approach for learning deep kernels by utilizing infinite-width neural networks. We propose to use the Neural Network Gaussian Process (NNGP) model as a guide to the DKL model in the optimization process. Our approach harnesses the reliable uncertainty estimation of the NNGPs to adapt the DKL target confidence when it encounters novel data points. As a result, we get the best of both worlds, we leverage the Bayesian behavior of the NNGP, namely its robustness to overfitting, and accurate uncertainty estimation, while maintaining the generalization abilities, scalability, and flexibility of deep kernels. Empirically, we show on multiple benchmark datasets of varying sizes and dimensionality, that our method is robust to overfitting, has good predictive performance, and provides reliable uncertainty estimations

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
