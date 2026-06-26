---
id: "arxiv-2990"
title: "Angular Visual Hardness"
conference: "arXiv 2020"
date: "2020-07"
authors:
  - name: "Beidi Chen"
    affiliation: "Rice"
    is_industry: false
  - name: "Weiyang Liu"
    affiliation: "Gatech"
    is_industry: false
  - name: "Zhiding Yu"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Jan Kautz"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Anshumali Shrivastava"
    affiliation: "Rice"
    is_industry: false
  - name: "Animesh Garg"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Anima Anandkumar"
    affiliation: "NVIDIA"
    is_industry: true
topics:
  - AI & Machine Learning
  - Computer Vision
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Computer Vision"
  - "Artificial Intelligence and Machine Learning"
external_links:
  - name: "Project Page"
    url: "https://sites.google.com/nvidia.com/avh"
  - name: "Paper (arXiv)"
    url: "https://arxiv.org/abs/1912.02279"
  - name: "Code"
    url: "https://github.com/keroro824/AVH"
  - name: "Slides"
    url: "https://chrisding.github.io/publications/ICML20a_Slides.pdf"
abstract: "Recent convolutional neural networks (CNNs) have led to impressive performance but often suffer from poor calibration. They tend to be overconfident, with the model confidence not always reflecting the underlying true ambiguity and hardness. In this paper, we propose angular visual hardness (AVH), a"
url: "https://research.nvidia.com/publication/2020-07_angular-visual-hardness"
status: "new"
---

# Angular Visual Hardness

## 摘要

Recent convolutional neural networks (CNNs) have led to impressive performance but often suffer from poor calibration. They tend to be overconfident, with the model confidence not always reflecting the underlying true ambiguity and hardness. In this paper, we propose angular visual hardness (AVH), a score given by the normalized angular distance between the sample feature embedding and the target classifier to measure sample hardness. We validate this score with an in-depth and extensive scientific study, and observe that CNN models with the highest accuracy also have the best AVH scores. This agrees with an earlier finding that state-of-art models improve on the classification of harder examples. We observe that the training dynamics of AVH is vastly different compared to the training loss. Specifically, AVH quickly reaches a plateau for all samples even though the training loss keeps improving. This suggests the need for designing better loss functions that can target harder examples more effectively. We also find that AVH has a statistically significant correlation with human visual hardness. Finally, we demonstrate the benefit of AVH to a variety of applications such as self-training for domain adaptation and domain generalization.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
