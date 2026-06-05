---
id: cvpr-0004
title: "Adapting to the Unknown: Training-Free Audio-Visual Event Perception with Dynamic Thresholds"
conference: CVPR 2025
date: 2025-06
authors:
  - name: "Gal Chechik"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Eitan Shaar"
    affiliation: ""
    is_industry: false
  - name: "Ariel Shaulov"
    affiliation: ""
    is_industry: false
  - name: "Lior Wolf"
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
  - name: "arxiv"
    url: "https://arxiv.org/abs/2503.13693"
abstract: "Abstract: In the domain of audio-visual event perception, which focuses on the temporal localization and classification of events across distinct modalities (audio and visual), existing approaches are constrained by the vocabulary available in their training data. This limitation significantly imped"
url: "https://research.nvidia.com/publication/2025-06_adapting-unknown-training-free-audio-visual-event-perception-dynamic-thresholds"
status: new
---

# Adapting to the Unknown: Training-Free Audio-Visual Event Perception with Dynamic Thresholds

## 摘要

Abstract: In the domain of audio-visual event perception, which focuses on the temporal localization and classification of events across distinct modalities (audio and visual), existing approaches are constrained by the vocabulary available in their training data. This limitation significantly impedes their capacity to generalize to novel, unseen event categories. Furthermore, the annotation process for this task is labor-intensive, requiring extensive manual labeling across modalities and temporal segments, limiting the scalability of current methods. Current state-of-the-art models ignore the shifts in event distributions over time, reducing their ability to adjust to changing video dynamics. Additionally, previous methods rely on late fusion to combine audio and visual information. While straightforward, this approach results in a significant loss of multimodal interactions. To address these challenges, we propose Audio-Visual Adaptive Video Analysis (AV2A), a model-agnostic approach that requires no further training and integrates an early fusion technique to retain richer multimodal interactions. AV2A also includes a within-video label shift algorithm, leveraging input video data and predictions from prior frames to dynamically adjust event distributions for subsequent frames. Moreover, we present the first training-free, open-vocabulary baseline for audio-visual event perception, demonstrating that achieves substantial improvements over naive training-free baselines. We demonstrate the effectiveness of AV2A on both zero-shot and weakly-supervised state-of-the-art methods, achieving notable improvements in performance metrics over existing approaches.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
