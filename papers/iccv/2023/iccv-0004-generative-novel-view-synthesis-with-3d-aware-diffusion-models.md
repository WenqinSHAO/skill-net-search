---
id: "iccv-0004"
title: "Generative Novel View Synthesis with 3D-Aware Diffusion Models"
conference: "ICCV 2023"
date: "2023-10"
authors:
  - name: "Eric R. Chan"
    affiliation: "Stanford University, NVIDIA"
    is_industry: true
  - name: "Koki Nagano"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Matthew Chan"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Alexander W. Bergman"
    affiliation: "Stanford University"
    is_industry: false
  - name: "Jeong Joon Park"
    affiliation: "Stanford University"
    is_industry: false
  - name: "Axel Levy"
    affiliation: "Stanford University"
    is_industry: false
  - name: "Miika Aittala"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Shalini De Mello"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Tero Karras"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Gordon Wetzstein"
    affiliation: "Stanford University"
    is_industry: false
topics:
  - AI & Machine Learning
  - Foundation_models
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Artificial Intelligence and Machine Learning"
  - "Generative AI"
external_links:
  - name: "Project page"
    url: "https://nvlabs.github.io/genvs/"
  - name: "ArXiv"
    url: "https://arxiv.org/abs/2304.02602"
abstract: "We present a diffusion-based model for 3D-aware generative novel view synthesis from as few as a single input image. Our model samples from the distribution of possible renderings consistent with the input and, even in the presence of ambiguity, is capable of rendering diverse and plausible novel vi"
url: "https://research.nvidia.com/publication/2023-10_generative-novel-view-synthesis-3d-aware-diffusion-models"
status: "new"
---

# Generative Novel View Synthesis with 3D-Aware Diffusion Models

## 摘要

We present a diffusion-based model for 3D-aware generative novel view synthesis from as few as a single input image. Our model samples from the distribution of possible renderings consistent with the input and, even in the presence of ambiguity, is capable of rendering diverse and plausible novel views. To achieve this, our method makes use of existing 2D diffusion backbones but, crucially, incorporates geometry priors in the form of a 3D feature volume. This latent feature field captures the distribution over possible scene representations and improves our method’s ability to generate view-consistent novel renderings. In addition to generating novel views, our method has the ability to autoregressively synthesize 3D-consistent sequences. We demonstrate state-of-the-art results on synthetic renderings and room-scale scenes; we also show compelling results for challenging, real-world objects.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
