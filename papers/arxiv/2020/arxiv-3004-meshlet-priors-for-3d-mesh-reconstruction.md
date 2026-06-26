---
id: "arxiv-3004"
title: "Meshlet Priors for 3D Mesh Reconstruction"
conference: "arXiv 2020"
date: "2020-06"
authors:
  - name: "Abhishek Badki"
    affiliation: "UC Santa Barbara"
    is_industry: false
  - name: "Orazio Gallo"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Jan Kautz"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Pradeep Sen"
    affiliation: "UC Santa Barbara"
    is_industry: false
topics:
  - AI & Machine Learning
  - Computer Vision
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Computational Photography and Imaging"
  - "Computer Vision"
  - "Artificial Intelligence and Machine Learning"
external_links:
  - name: "Video teaser"
    url: "https://youtu.be/glZyJ66ktog"
  - name: "Paper on arXiv"
    url: "https://arxiv.org/abs/2001.01744"
  - name: "Code (coming soon)"
    url: "https://github.com/NVlabs/meshlets"
abstract: "Estimating a mesh from an unordered set of sparse, noisy 3D points is a challenging problem that requires to carefully select priors. Existing hand-crafted priors, such as smoothness regularizers, impose an undesirable trade-off between attenuating noise and preserving local detail. Recent deep-lear"
url: "https://research.nvidia.com/publication/2020-06_meshlet-priors-3d-mesh-reconstruction"
status: "new"
---

# Meshlet Priors for 3D Mesh Reconstruction

## 摘要

Estimating a mesh from an unordered set of sparse, noisy 3D points is a challenging problem that requires to carefully select priors. Existing hand-crafted priors, such as smoothness regularizers, impose an undesirable trade-off between attenuating noise and preserving local detail. Recent deep-learning approaches produce impressive results by learning priors directly from the data. However, the priors are learned at the object level, which makes these algorithms class-specific and even sensitive to the pose of the object. We introduce meshlets, small patches of mesh that we use to learn local shape priors. Meshlets act as a dictionary of local features and thus allow to use learned priors to reconstruct object meshes in any pose and from unseen classes, even when the noise is large and the samples sparse.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
