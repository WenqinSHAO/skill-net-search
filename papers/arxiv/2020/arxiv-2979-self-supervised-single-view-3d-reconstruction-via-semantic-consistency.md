---
id: "arxiv-2979"
title: "Self-supervised Single-view 3D Reconstruction via Semantic Consistency"
conference: "arXiv 2020"
date: "2020-08"
authors:
  - name: "Xueting Li"
    affiliation: "NVIDIA, UC Merced"
    is_industry: true
  - name: "Sifei Liu"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Kihwan Kim"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Shalini De Mello"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Varun Jampani"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Ming-Hsuan Yang"
    affiliation: "UC Merced"
    is_industry: false
  - name: "Jan Kautz"
    affiliation: "NVIDIA"
    is_industry: true
topics:
  - AI & Machine Learning
  - Computer Vision
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Artificial Intelligence and Machine Learning"
  - "Computer Vision"
external_links:
  - name: "Paper"
    url: "https://www.ecva.net/papers/eccv_2020/papers_ECCV/papers/123590664.pdf"
  - name: "ArXiv"
    url: "https://arxiv.org/pdf/2003.06473.pdf"
  - name: "Project Page"
    url: "https://sites.google.com/nvidia.com/unsup-mesh-2020"
  - name: "Video"
    url: "https://www.youtube.com/watch?v=P_inKc9wJvo"
abstract: "We learn a self-supervised, single-view 3D reconstruction model that predicts the 3D mesh shape, texture and camera pose of a target object with a collection of 2D images and silhouettes. The proposed method does not necessitate 3D supervision, manually annotated keypoints, multi-view images of an o"
url: "https://research.nvidia.com/publication/2020-08_self-supervised-single-view-3d-reconstruction-semantic-consistency"
status: "new"
---

# Self-supervised Single-view 3D Reconstruction via Semantic Consistency

## 摘要

We learn a self-supervised, single-view 3D reconstruction model that predicts the 3D mesh shape, texture and camera pose of a target object with a collection of 2D images and silhouettes. The proposed method does not necessitate 3D supervision, manually annotated keypoints, multi-view images of an object or a prior 3D template. The key insight of our work is that objects can be represented as a collection of deformable parts, and each part is semantically coherent across different instances of the same category (e.g., wings on birds and wheels on cars). Therefore, by leveraging self-supervisedly learned part segmentation of a large collection of category-specific images, we can effectively enforce semantic consistency between the reconstructed meshes and the original images. This significantly reduces ambiguities during joint prediction of shape and camera pose of an object, along with texture. To the best of our knowledge, we are the first to try and solve the single-view reconstruction problem without a category-specific template mesh or semantic keypoints. Thus our model can easily generalize to various object categories without such labels, e.g., horses, penguins, etc. Through a variety of experiments on several categories of deformable and rigid objects, we demonstrate that our unsupervised method performs comparably if not better than existing category-specific reconstruction methods learned with supervision.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
