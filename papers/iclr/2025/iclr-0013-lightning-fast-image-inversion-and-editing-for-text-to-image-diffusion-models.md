---
id: "iclr-0013"
title: "Lightning-Fast Image Inversion and Editing for Text-to-Image Diffusion Models,"
conference: "ICLR 2025"
date: "2025-04"
authors:
  - name: "Dvir Samuel"
    affiliation: "Bar-Ilan University"
    is_industry: false
  - name: "Barak Meiri"
    affiliation: "Hebrew University"
    is_industry: false
  - name: "Haggai Maron"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Yoad Tewel"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Nir Darshan"
    affiliation: "Origin AI"
    is_industry: false
  - name: "Shai Avidan"
    affiliation: "Tel-Aviv University"
    is_industry: false
  - name: "Gal Chechik"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Rami Ben-Ari"
    affiliation: "Origin AI"
    is_industry: false
topics:
  - AI & Machine Learning
  - Foundation_models
  - Graphics_rendering
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Artificial Intelligence and Machine Learning"
  - "Computer Graphics"
  - "Generative AI"
external_links:
  - name: "ICLR 2025"
    url: "https://iclr.cc/virtual/2025/poster/28072"
  - name: "Arxiv"
    url: "https://arxiv.org/abs/2312.12540"
abstract: "Diffusion inversion is the problem of taking an image and a text prompt that describes it and finding a noise latent that would generate the exact same image. Most current deterministic inversion techniques operate by approximately solving an implicit equation and may converge slowly or yield poor r"
url: "https://research.nvidia.com/publication/2025-04_lightning-fast-image-inversion-and-editing-text-image-diffusion-models"
status: "new"
---

# Lightning-Fast Image Inversion and Editing for Text-to-Image Diffusion Models,

## 摘要

Diffusion inversion is the problem of taking an image and a text prompt that describes it and finding a noise latent that would generate the exact same image. Most current deterministic inversion techniques operate by approximately solving an implicit equation and may converge slowly or yield poor reconstructed images. We formulate the problem by finding the roots of an implicit equation and devlop a method to solve it efficiently. Our solution is based on Newton-Raphson (NR), a well-known technique in numerical analysis. We show that a vanilla application of NR is computationally infeasible while naively transforming it to a computationally tractable alternative tends to converge to out-of-distribution solutions, resulting in poor reconstruction and editing. We therefore derive an efficient guided formulation that fastly converges and provides high-quality reconstructions and editing. We showcase our method on real image editing with three popular open-sourced diffusion models: Stable Diffusion, SDXL-Turbo, and Flux with different deterministic schedulers. Our solution, Guided Newton-Raphson Inversion, inverts an image within 0.4 sec (on an A100 GPU) for few-step models (SDXL-Turbo and Flux.1), opening the door for interactive image editing. We further show improved results in image interpolation and generation of rare objects.&nbsp;

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
