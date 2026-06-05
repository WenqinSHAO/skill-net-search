---
id: arxiv-3011
title: "Self-Supervised Viewpoint Learning From Image Collections"
conference: arXiv 2020
date: 2020-06
authors:
  - name: "Shalini De Mello"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Sifei Liu"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Umar Iqbal"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Jan Kautz"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Siva Karthik Mustikovela"
    affiliation: ""
    is_industry: false
  - name: "Varun Jampani"
    affiliation: ""
    is_industry: false
  - name: "Carsten Rother"
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
  - "Computer Vision"
  - "Artificial Intelligence and Machine Learning"
external_links:
  - name: "Code"
    url: "https://github.com/NVlabs/SSV"
abstract: "Training deep neural networks to estimate the viewpoint of objects requires large labeled training datasets. However, manually labeling viewpoints is notoriously hard, error-prone, and time-consuming. On the other hand, it is relatively easy to mine many unlabeled images of an object category from t"
url: "https://research.nvidia.com/publication/2020-06_self-supervised-viewpoint-learning-image-collections"
status: new
---

# Self-Supervised Viewpoint Learning From Image Collections

## 摘要

Training deep neural networks to estimate the viewpoint of objects requires large labeled training datasets. However, manually labeling viewpoints is notoriously hard, error-prone, and time-consuming. On the other hand, it is relatively easy to mine many unlabeled images of an object category from the internet, e.g., of cars or faces. We seek to answer the research question of whether such unlabeled collections of in-the-wild images can be successfully utilized to train viewpoint estimation networks for general object categories purely via self-supervision. Self-supervision here refers to the fact that the only true supervisory signal that the network has is the input image itself. We propose a novel learning framework which incorporates an analysis-by-synthesis paradigm to reconstruct images in a viewpoint aware manner with a generative network, along with symmetry and adversarial constraints to successfully supervise our viewpoint estimation network. We show that our approach performs competitively to fully-supervised approaches for several object categories like human faces, cars, buses, and trains. Our work opens up further research in self-supervised viewpoint learning and serves as a robust baseline for it. We open-source our code at https://github.com/NVlabs/SSV.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
