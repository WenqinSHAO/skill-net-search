---
id: siggraph-0014
title: "TurboEdit: Text-Based Image Editing Using Few-Step Diffusion Models"
conference: SIGGRAPH 2024
date: 2024-08
authors:
  - name: "Gilad Deutch"
    affiliation: ""
    is_industry: false
  - name: "Rinon Gal"
    affiliation: ""
    is_industry: false
  - name: "Daniel Garibi"
    affiliation: ""
    is_industry: false
  - name: "Or Patashnik"
    affiliation: ""
    is_industry: false
  - name: "Daniel Cohen-Or"
    affiliation: ""
    is_industry: false
topics:
  - Computer Vision
  - Foundation_models
  - Graphics_rendering
  - AI & Machine Learning
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Computer Graphics"
  - "Computer Vision"
  - "Generative AI"
abstract: "Diffusion models have opened the path to a wide range of text-based image editing frameworks. However, these typically build on the multi-step nature of the diffusion backwards process, and adapting them to distilled, fast-sampling methods has proven surprisingly challenging. Here, we focus on a pop"
url: "https://research.nvidia.com/publication/2024-08_turboedit-text-based-image-editing-using-few-step-diffusion-models"
status: new
---

# TurboEdit: Text-Based Image Editing Using Few-Step Diffusion Models

## 摘要

Diffusion models have opened the path to a wide range of text-based image editing frameworks. However, these typically build on the multi-step nature of the diffusion backwards process, and adapting them to distilled, fast-sampling methods has proven surprisingly challenging. Here, we focus on a popular line of text-based editing frameworks - the ``edit-friendly'' DDPM-noise inversion approach. We analyze its application to fast sampling methods and categorize its failures into two classes: the appearance of visual artifacts, and insufficient editing strength. We trace the artifacts to mismatched noise statistics between inverted noises and the expected noise schedule, and suggest a shifted noise schedule which corrects for this offset. To increase editing strength, we propose a pseudo-guidance approach that efficiently increases the magnitude of edits without introducing new artifacts. All in all, our method enables text-based image editing with as few as three diffusion steps, while providing novel insights into the mechanisms behind popular text-based editing approaches.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
