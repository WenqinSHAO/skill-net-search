---
id: corl-0016
title: "Online Overexposed Pixels Hallucination in Videos with Adaptive Reference Frame Selection"
conference: CoRL 2023
date: 2023-08
authors:
  - name: "Amrita Mazumdar"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Chao Liu"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Hongxu Danny Yin"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Jan Kautz"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Iuri Frosio"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Yazhou Xing"
    affiliation: ""
    is_industry: false
  - name: "Anjul Patney"
    affiliation: ""
    is_industry: false
  - name: "Qifeng Chen"
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
  - "Computational Photography and Imaging"
  - "Computer Vision"
external_links:
  - name: "Arxiv paper"
    url: "https://arxiv.org/abs/2308.15462"
abstract: "Low dynamic range (LDR) cameras cannot deal with wide dynamic range inputs, frequently leading to local overexposure issues. We present a learning-based system to reduce these artifacts without resorting to complex acquisition mechanisms like alternating exposures or costly processing that are typic"
url: "https://research.nvidia.com/publication/2023-08_online-overexposed-pixels-hallucination-videos-adaptive-reference-frame"
status: new
---

# Online Overexposed Pixels Hallucination in Videos with Adaptive Reference Frame Selection

## 摘要

Low dynamic range (LDR) cameras cannot deal with wide dynamic range inputs, frequently leading to local overexposure issues. We present a learning-based system to reduce these artifacts without resorting to complex acquisition mechanisms like alternating exposures or costly processing that are typical of high dynamic range (HDR) imaging. We propose a transformer-based deep neural network (DNN) to infer the missing HDR details. In an ablation study, we show the importance of using a multiscale DNN and train it with the proper cost function to achieve state-of-the-art quality. To aid the reconstruction of the overexposed areas, our DNN takes a reference frame from the past as an additional input. This leverages the commonly occurring temporal instabilities of autoexposure to our advantage: since well-exposed details in the current frame may be overexposed in the future, we use reinforcement learning to train a reference frame selection DNN that decides whether to adopt the current frame as a future reference. Without resorting to alternating exposures, we obtain therefore a causal, HDR hallucination algorithm with potential application in common video acquisition settings.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
