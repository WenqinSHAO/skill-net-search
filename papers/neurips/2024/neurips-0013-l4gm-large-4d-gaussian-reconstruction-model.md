---
id: neurips-0013
title: "L4GM: Large 4D Gaussian Reconstruction Model"
conference: NeurIPS 2024
date: 2024-12
authors:
  - name: "Karsten Kreis"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Jiawei Ren"
    affiliation: ""
    is_industry: false
  - name: "Kevin Xie"
    affiliation: ""
    is_industry: false
  - name: "Ashkan Mirzaei"
    affiliation: ""
    is_industry: false
  - name: "Hanxue Liang"
    affiliation: ""
    is_industry: false
  - name: "Xiaohui Zeng"
    affiliation: ""
    is_industry: false
  - name: "Ziwei Liu"
    affiliation: ""
    is_industry: false
  - name: "Antonio Torralba"
    affiliation: ""
    is_industry: false
  - name: "Sanja Fidler"
    affiliation: ""
    is_industry: false
  - name: "Seung Wook Kim"
    affiliation: ""
    is_industry: false
  - name: "Huan Ling"
    affiliation: ""
    is_industry: false
topics:
  - AI & Machine Learning
  - Computer Vision
  - Foundation_models
  - AI & Machine Learning
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Artificial Intelligence and Machine Learning"
  - "Computer Vision"
  - "Generative AI"
external_links:
  - name: "Project Website"
    url: "https://research.nvidia.com/labs/toronto-ai/l4gm/"
abstract: "We present L4GM, the first 4D Large Reconstruction Model that produces animated objects from a single-view video input -- in a single feed-forward pass that takes only a second. Key to our success is a novel dataset of multiview videos containing curated, rendered animated objects from Objaverse. Th"
url: "https://research.nvidia.com/publication/2024-12_l4gm-large-4d-gaussian-reconstruction-model"
status: new
---

# L4GM: Large 4D Gaussian Reconstruction Model

## 摘要

We present L4GM, the first 4D Large Reconstruction Model that produces animated objects from a single-view video input -- in a single feed-forward pass that takes only a second. Key to our success is a novel dataset of multiview videos containing curated, rendered animated objects from Objaverse. This dataset depicts 44K diverse objects with 110K animations rendered in 48 viewpoints, resulting in 12M videos with a total of 300M frames. We keep our L4GM simple for scalability and build directly on top of LGM, a pretrained 3D Large Reconstruction Model that outputs 3D Gaussian ellipsoids from multiview image input. L4GM outputs a per-frame 3D Gaussian Splatting representation from video frames sampled at a low fps and then upsamples the representation to a higher fps to achieve temporal smoothness. We add temporal self-attention layers to the base LGM to help it learn consistency across time, and utilize a per-timestep multiview rendering loss to train the model. The representation is upsampled to a higher framerate by training an interpolation model which produces intermediate 3D Gaussian representations. We showcase that L4GM that is only trained on synthetic data generalizes extremely well on in-the-wild videos, producing high quality animated 3D assets.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
