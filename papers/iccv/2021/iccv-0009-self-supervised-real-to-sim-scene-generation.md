---
id: "iccv-0009"
title: "Self-Supervised Real-to-Sim Scene Generation"
conference: "ICCV 2021"
date: "2021-10"
authors:
  - name: "Aayush Prakash"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Shoubhik Debnath"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Jean-Francois Lafleche"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Eric Cameracci"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Gavriel State"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Stan Birchfield"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Marc T. Law"
    affiliation: "NVIDIA"
    is_industry: true
topics:
  - Computer Vision
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Computer Vision"
abstract: "Synthetic data is emerging as a promising solution to the scalability issue of supervised deep learning, especially when real data are difficult to acquire or hard to annotate. Synthetic data generation, however, can itself be prohibitively expensive when domain experts have to manually and painstak"
url: "https://research.nvidia.com/publication/2021-10_self-supervised-real-sim-scene-generation"
status: "new"
---

# Self-Supervised Real-to-Sim Scene Generation

## 摘要

Synthetic data is emerging as a promising solution to the scalability issue of supervised deep learning, especially when real data are difficult to acquire or hard to annotate. Synthetic data generation, however, can itself be prohibitively expensive when domain experts have to manually and painstakingly oversee the process. Moreover, neural networks trained on synthetic data often do not perform well on real data because of the domain gap. To solve these challenges, we propose Sim2SG, a self-supervised automatic scene generation technique for matching the distribution of real data. Importantly, Sim2SG does not require supervision from the real-world dataset, thus making it applicable in situations for which such annotations are difficult to obtain. Sim2SG is designed to bridge both the content and appearance gaps, by matching the content of real data, and by matching the features in the source and target domains. We select scene graph (SG) generation as the downstream task, due to the limited availability of labeled datasets. Experiments demonstrate significant improvements over leading baselines in reducing the domain gap both qualitatively and quantitatively, on several synthetic datasets as well as the real-world KITTI dataset.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
