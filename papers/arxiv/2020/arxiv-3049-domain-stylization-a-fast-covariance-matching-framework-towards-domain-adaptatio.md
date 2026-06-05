---
id: arxiv-3049
title: "Domain Stylization: A Fast Covariance Matching Framework towards Domain Adaptation"
conference: arXiv 2020
date: 2020-01
authors:
  - name: "Ming-Yu Liu"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Zhiding Yu"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Ting-Chun Wang"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Jan Kautz"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Aysegul Dundar"
    affiliation: ""
    is_industry: false
  - name: "John Zedlewski"
    affiliation: ""
    is_industry: false
topics:
  - AI & Machine Learning
  - Computer Vision
  - Graphics_rendering
  - AI & Machine Learning
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Computer Graphics"
  - "Computer Vision"
  - "Artificial Intelligence and Machine Learning"
external_links:
  - name: "Paper"
    url: "https://ieeexplore.ieee.org/document/8968319"
abstract: "Generating computer graphics (CG) rendered synthetic images has been widely used to create simulation environments for robotics/autonomous driving and generate labeled data. Yet, the problem of training models purely with synthetic data remains challenging due to the considerable domain gaps caused "
url: "https://research.nvidia.com/publication/2020-01_domain-stylization-fast-covariance-matching-framework-towards-domain-adaptation"
status: new
---

# Domain Stylization: A Fast Covariance Matching Framework towards Domain Adaptation

## 摘要

Generating computer graphics (CG) rendered synthetic images has been widely used to create simulation environments for robotics/autonomous driving and generate labeled data. Yet, the problem of training models purely with synthetic data remains challenging due to the considerable domain gaps caused by current limitations on rendering. In this paper, we propose a simple yet effective domain adaptation framework towards closing such gap at image level. Unlike many GAN-based approaches, our method aims to match the covariance of the universal feature embeddings across domains, making the adaptation a fast, convenient "on-the-fly" step and avoiding the need for potentially difficult GAN trainings. To align domains more precisely, we further propose a conditional covariance matching framework which iteratively estimates semantic segmentation regions and conditionally matches the class-wise feature covariance given the segmentation regions. We demonstrate that both tasks can mutually refine and considerably improve each other, leading to state-of-the-art domain adaptation results. Extensive experiments under multiple synthetic-to-real settings show that our approach exceeds the performance of latest domain adaptation approaches. In addition, we offer a quantitative analysis where our framework shows considerable reduction in Frechet Inception distance between source and target domains, demonstrating the effectiveness of this work in bridging the synthetic-to-real domain gap.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
