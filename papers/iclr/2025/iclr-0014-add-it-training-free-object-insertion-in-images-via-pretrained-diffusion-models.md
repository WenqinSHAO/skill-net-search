---
id: iclr-0014
title: "Add-it: Training-Free Object Insertion in Images via Pretrained Diffusion Models"
conference: ICLR 2025
date: 2025-04
authors:
  - name: "Yoad Tewel"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Yuval Atzmon"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Gal Chechik"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Rinon Gal"
    affiliation: ""
    is_industry: false
  - name: "Dvir Samuel"
    affiliation: ""
    is_industry: false
  - name: "Lior Wolf"
    affiliation: ""
    is_industry: false
topics:
  - AI & Machine Learning
  - Graphics_rendering
  - AI & Machine Learning
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Artificial Intelligence and Machine Learning"
  - "Computer Graphics"
external_links:
  - name: "ICLR 2025"
    url: "https://iclr.cc/virtual/2025/poster/29207"
abstract: "Adding Object into images based on text instructions is a challenging task in semantic image editing, requiring a balance between preserving the original scene and seamlessly integrating the new object in a fitting location. Despite extensive efforts, existing models often struggle with this balance"
url: "https://research.nvidia.com/publication/2025-04_add-it-training-free-object-insertion-images-pretrained-diffusion-models"
status: new
---

# Add-it: Training-Free Object Insertion in Images via Pretrained Diffusion Models

## 摘要

Adding Object into images based on text instructions is a challenging task in semantic image editing, requiring a balance between preserving the original scene and seamlessly integrating the new object in a fitting location. Despite extensive efforts, existing models often struggle with this balance, particularly with finding a natural location for adding an object in complex scenes. We introduce Add-it, a training-free approach that extends diffusion models' attention mechanisms to incorporate information from three key sources: the scene image, the text prompt, and the generated image itself. Our weighted extended-attention mechanism maintains structural consistency and fine details while ensuring natural object placement. Without task-specific fine-tuning, Add-it achieves state-of-the-art results on both real and generated image insertion benchmarks, including our newly constructed "Additing Affordance Benchmark" for evaluating object placement plausibility, outperforming supervised methods. Human evaluations show that Add-it is preferred in over 80% of cases, and it also demonstrates improvements in various automated metrics.&nbsp;

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
