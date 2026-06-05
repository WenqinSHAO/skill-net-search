---
id: arxiv-2937
title: "Convolutional Tensor-Train LSTM for Spatio-Temporal Learning"
conference: arXiv 2020
date: 2020-12
authors:
  - name: "Wonmin Byeon"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Jean Kossaifi"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Jan Kautz"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Jiahao Su"
    affiliation: ""
    is_industry: false
  - name: "Furong Huang"
    affiliation: ""
    is_industry: false
  - name: "Anima Anandkumar"
    affiliation: ""
    is_industry: false
topics:
  - AI & Machine Learning
  - AI & Machine Learning
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Artificial Intelligence and Machine Learning"
external_links:
  - name: "Paper"
    url: "https://papers.nips.cc/paper/2020/hash/9e1a36515d6704d7eb7a30d783400e5d-Abstract.html"
  - name: "Code"
    url: "https://github.com/NVlabs/conv-tt-lstm"
  - name: "Slides"
    url: "https://docs.google.com/presentation/d/1wnjgvaR5jixWx5RYwHu9Ne4rt1gsmmXepygFOTt2914/edit#slide=id.p1"
abstract: "Learning from spatio-temporal data has numerous applications such as human-behavior analysis, object tracking, video compression, and physics simulation. However, existing methods still perform poorly on challenging video tasks suchas long-term forecasting. The gap partially is because these kinds o"
url: "https://research.nvidia.com/publication/2020-12_convolutional-tensor-train-lstm-spatio-temporal-learning"
status: new
---

# Convolutional Tensor-Train LSTM for Spatio-Temporal Learning

## 摘要

Learning from spatio-temporal data has numerous applications such as human-behavior analysis, object tracking, video compression, and physics simulation. However, existing methods still perform poorly on challenging video tasks suchas long-term forecasting. The gap partially is because these kinds of challenging tasks require learning long-term spatio-temporal correlations in the video sequence. We propose a higher-order convolutional LSTM model that can efficiently learn these correlations with a succinct representation of the history. Our model relies on a novel tensor-train module that performs prediction by combining convolutional features across time. To make computation and memory requirements feasible, we develop a novel convolutional tensor-train decomposition of the higher-ordermodel. This decomposition reduces the model complexity by jointly approximatinga sequence of convolutional kernels as a low-rank tensor-train factorization. Asa result, our model outperforms existing approaches but uses only a fraction of parameters, including the baseline models. Our results achieve state-of-the-artperformance in a wide range of applications and datasets, including the multi-stepsvideo prediction on the Moving-MNIST-2 and KTH action datasets as well as earlyactivity recognition on the Something-Something V2 dataset.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
