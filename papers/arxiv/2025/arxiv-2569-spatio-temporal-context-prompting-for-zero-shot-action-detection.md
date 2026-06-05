---
id: arxiv-2569
title: "Spatio-Temporal Context Prompting for Zero-Shot Action Detection"
conference: arXiv 2025
date: 2025-02
authors:
  - name: "Min-Hung Chen"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Wei-Jhe Huang"
    affiliation: ""
    is_industry: false
  - name: "Shang-Hong Lai"
    affiliation: ""
    is_industry: false
topics:
  - AI & Machine Learning
  - Applied_perception
  - Computer Vision
  - Foundation_models
  - AI & Machine Learning
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Applied Perception"
  - "Artificial Intelligence and Machine Learning"
  - "Computer Vision"
  - "Natural Language Processing"
external_links:
  - name: "arXiv"
    url: "https://arxiv.org/abs/2408.15996"
  - name: "Code"
    url: "https://github.com/webber2933/ST-CLIP"
  - name: "Project page"
    url: "https://webber2933.github.io/ST-CLIP-project-page/"
abstract: "Spatio-temporal action detection encompasses the tasks of localizing and classifying individual actions within a video. Recent works aim to enhance this process by incorporating interaction modeling, which captures the relationship between people and their surrounding context. However, these approac"
url: "https://research.nvidia.com/publication/2025-02_spatio-temporal-context-prompting-zero-shot-action-detection"
status: new
---

# Spatio-Temporal Context Prompting for Zero-Shot Action Detection

## 摘要

Spatio-temporal action detection encompasses the tasks of localizing and classifying individual actions within a video. Recent works aim to enhance this process by incorporating interaction modeling, which captures the relationship between people and their surrounding context. However, these approaches have primarily focused on fully-supervised learning, and the current limitation lies in the lack of generalization capability to recognize unseen action categories. In this paper, we aim to adapt the pretrained image-language models to detect unseen actions. To this end, we propose a method which can effectively leverage the rich knowledge of visual-language models to perform Person-Context Interaction. Meanwhile, our Context Prompting module will utilize contextual information to prompt labels, thereby enhancing the generation of more representative text features. Moreover, to address the challenge of recognizing distinct actions by multiple people at the same timestamp, we design the Interest Token Spotting mechanism which employs pretrained visual knowledge to find each person's interest context tokens, and then these tokens will be used for prompting to generate text features tailored to each individual. To evaluate the ability to detect unseen actions, we propose a comprehensive benchmark on J-HMDB, UCF101-24, and AVA datasets. The experiments show that our method achieves superior results compared to previous approaches and can be further extended to multi-action videos, bringing it closer to real-world applications. The code and data can be found in this https URL.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
