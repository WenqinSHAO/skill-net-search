---
id: iclr-0010
title: "Latent Action Pretraining from Videos"
conference: ICLR 2025
date: 2025-04
authors:
  - name: "Ajay Mandlekar"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Yu-Wei Chao"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Seonghyeon Ye"
    affiliation: ""
    is_industry: false
  - name: "Joel Jang"
    affiliation: ""
    is_industry: false
  - name: "Byeongguk Jeon"
    affiliation: ""
    is_industry: false
  - name: "Sejune Joo"
    affiliation: ""
    is_industry: false
  - name: "Jianwei Yang"
    affiliation: ""
    is_industry: false
  - name: "Baolin Peng"
    affiliation: ""
    is_industry: false
  - name: "Reuben Tan"
    affiliation: ""
    is_industry: false
  - name: "Yuchen Lin"
    affiliation: ""
    is_industry: false
  - name: "Lars Liden"
    affiliation: ""
    is_industry: false
  - name: "Kimin Lee"
    affiliation: ""
    is_industry: false
  - name: "Jianfeng Gao"
    affiliation: ""
    is_industry: false
  - name: "Luke Zettlemoyer"
    affiliation: ""
    is_industry: false
  - name: "Dieter Fox"
    affiliation: ""
    is_industry: false
  - name: "Minjoon Seo"
    affiliation: ""
    is_industry: false
topics:
  - AI & Machine Learning
  - Robotics_autonomous
  - AI & Machine Learning
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Artificial Intelligence and Machine Learning"
  - "Physical AI"
  - "Robotics"
external_links:
  - name: "Paper, Video, Code, Model"
    url: "https://latentactionpretraining.github.io"
abstract: "We introduce Latent Action Pretraining, the first unsupervised method for pretraining Vision-Language-Action (VLA) models without ground-truth robot action labels. Existing Vision-Language-Action models require action labels typically collected by human teleoperators during pretraining, which signif"
url: "https://research.nvidia.com/publication/2025-04_latent-action-pretraining-videos"
status: new
---

# Latent Action Pretraining from Videos

## 摘要

We introduce Latent Action Pretraining, the first unsupervised method for pretraining Vision-Language-Action (VLA) models without ground-truth robot action labels. Existing Vision-Language-Action models require action labels typically collected by human teleoperators during pretraining, which significantly limits possible data sources and scale. In this work, we propose a method to learn from internet-scale videos that do not have robot action labels. We first train an action quantization model leveraging VQ-VAE-based objective to learn discrete latent actions between image frames, then pretrain a latent VLA model to predict these latent actions from observations and task descriptions, and finally finetune the VLA on small-scale robot manipulation data to map from latent to robot actions. Experimental results demonstrate that our method significantly outperforms existing techniques that train robot manipulation policies from large-scale videos. Furthermore, it outperforms the state-of-the-art VLA model trained with robotic action labels on real-world manipulation tasks that require language conditioning, generalization to unseen objects, and semantic generalization to unseen instructions. Training only on human manipulation videos also shows positive transfer, opening up the potential for leveraging web-scale data for robotics foundation models. We will open-source the model checkpoints and code at https://latentactionpretraining.github.io.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
