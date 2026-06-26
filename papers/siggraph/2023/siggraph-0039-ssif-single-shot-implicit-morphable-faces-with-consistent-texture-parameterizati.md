---
id: "siggraph-0039"
title: "SSIF: Single-shot Implicit Morphable Faces With Consistent Texture Parameterization"
conference: "SIGGRAPH 2023"
date: "2023-08"
authors:
  - name: "Connor Zhizhen Lin"
    affiliation: "Stanford University"
    is_industry: false
  - name: "Koki Nagano"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Jan Kautz"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Eric R. Chan"
    affiliation: "Stanford University"
    is_industry: false
  - name: "Umar Iqbal"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Leonidas Guibas"
    affiliation: "Stanford University"
    is_industry: false
  - name: "Gordon Wetzstein"
    affiliation: "Stanford University"
    is_industry: false
  - name: "Sameh Khamis"
    affiliation: "NVIDIA"
    is_industry: true
topics:
  - AI & Machine Learning
  - Computer Vision
  - Graphics_rendering
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Artificial Intelligence and Machine Learning"
  - "Computer Graphics"
  - "Computer Vision"
external_links:
  - name: "Project"
    url: "https://research.nvidia.com/labs/toronto-ai/ssif/"
abstract: "There is a growing demand for the accessible creation of high-quality 3D avatars that are animatable and customizable. Although 3D morphable models provide intuitive control for editing and animation, and robustness for single-view face reconstruction, they cannot easily capture geometric and appear"
url: "https://research.nvidia.com/publication/2023-08_ssif-single-shot-implicit-morphable-faces-consistent-texture-parameterization"
status: "new"
---

# SSIF: Single-shot Implicit Morphable Faces With Consistent Texture Parameterization

## 摘要

There is a growing demand for the accessible creation of high-quality 3D avatars that are animatable and customizable. Although 3D morphable models provide intuitive control for editing and animation, and robustness for single-view face reconstruction, they cannot easily capture geometric and appearance details. Methods based on neural implicit representations, such as signed distance functions (SDF) or neural radiance fields, approach photo-realism, but are difficult to animate and do not generalize well to unseen data. To tackle this problem, we propose a novel method for constructing implicit 3D morphable face models that are both generalizable and intuitive for editing. Trained from a collection of high-quality 3D scans, our face model is parameterized by geometry, expression, and texture latent codes with a learned SDF and explicit UV texture parameterization. Once trained, we can reconstruct an avatar from a single in-the-wild image by leveraging the learned prior to project the image into the latent space of our model. Our implicit morphable face models can be used to render an avatar from novel views, animate facial expressions by modifying expression codes, and edit textures by directly painting on the learned UV-texture maps. We demonstrate quantitatively and qualitatively that our method improves upon photo-realism, geometry, and expression accuracy compared to state-of-the-art methods.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
