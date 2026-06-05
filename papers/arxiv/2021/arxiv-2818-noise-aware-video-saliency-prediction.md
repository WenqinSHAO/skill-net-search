---
id: arxiv-2818
title: "Noise-Aware Video Saliency Prediction"
conference: arXiv 2021
date: 2021-11
authors:
  - name: "Ekta Prashnani"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Joohwan Kim"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Josef Spjut"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Iuri Frosio"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Orazio Gallo"
    affiliation: ""
    is_industry: false
  - name: "Pradeep Sen"
    affiliation: ""
    is_industry: false
topics:
  - AI & Machine Learning
  - Computer Vision
  - AI & Machine Learning
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Artificial Intelligence and Machine Learning"
  - "Computer Vision"
external_links:
  - name: "Noise-Aware Video Saliency Prediction - Arxiv preprint"
    url: "https://arxiv.org/abs/2104.08038"
abstract: "We tackle the problem of predicting saliency maps for videos of dynamic scenes. We note that the accuracy of the maps reconstructed from the gaze data of a fixed number of observers varies with the frame, as it depends on the content of the scene. This issue is particularly pressing when a limited n"
url: "https://research.nvidia.com/publication/2021-11_noise-aware-video-saliency-prediction"
status: new
---

# Noise-Aware Video Saliency Prediction

## 摘要

We tackle the problem of predicting saliency maps for videos of dynamic scenes. We note that the accuracy of the maps reconstructed from the gaze data of a fixed number of observers varies with the frame, as it depends on the content of the scene. This issue is particularly pressing when a limited number of observers are available. In such cases, directly minimizing the discrepancy between the predicted and measured saliency maps, as traditional deep-learning methods do, results in overfitting to the noisy data. We propose a noise-aware training (NAT) paradigm that quantifies and accounts for the uncertainty arising from frame-specific gaze data inaccuracy. We show that NAT is especially advantageous when limited training data is available, with experiments across different models, loss functions, and datasets. We also introduce a video game-based saliency dataset, with rich temporal semantics, and multiple gaze attractors per frame. The dataset and source code are available at https://github.com/NVlabs/NAT-saliency.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
