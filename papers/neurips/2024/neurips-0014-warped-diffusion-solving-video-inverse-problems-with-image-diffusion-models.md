---
id: "neurips-0014"
title: "Warped Diffusion: Solving Video Inverse Problems with Image Diffusion Models"
conference: "NeurIPS 2024"
date: "2024-12"
authors:
  - name: "Giannis Daras"
    affiliation: "UT Austin"
    is_industry: false
  - name: "Weili Nie"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Karsten Kreis"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Alexandros G. Dimakis"
    affiliation: "UT Austin"
    is_industry: false
  - name: "Morteza Mardani"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Nikola Kovachki"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Arash Vahdat"
    affiliation: "NVIDIA"
    is_industry: true
topics:
  - AI & Machine Learning
  - Computer Vision
  - Foundation_models
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Artificial Intelligence and Machine Learning"
  - "Computer Vision"
  - "Generative AI"
external_links:
  - name: "Project Website"
    url: "https://giannisdaras.github.io/warped_diffusion.github.io/"
abstract: "Using image models naively for solving inverse video problems often suffers from flickering, texture-sticking, and temporal inconsistency in generated videos. To tackle these problems, in this paper, we view frames as continuous functions in the 2D space, and videos as a sequence of continuous warpi"
url: "https://research.nvidia.com/publication/2024-12_warped-diffusion-solving-video-inverse-problems-image-diffusion-models"
status: "new"
---

# Warped Diffusion: Solving Video Inverse Problems with Image Diffusion Models

## 摘要

Using image models naively for solving inverse video problems often suffers from flickering, texture-sticking, and temporal inconsistency in generated videos. To tackle these problems, in this paper, we view frames as continuous functions in the 2D space, and videos as a sequence of continuous warping transformations between different frames. This perspective allows us to train function space diffusion models only on images and utilize them to solve temporally correlated inverse problems. The function space diffusion models need to be equivariant with respect to the underlying spatial transformations. To ensure temporal consistency, we introduce a simple post-hoc test-time guidance towards (self)-equivariant solutions. Our method allows us to deploy state-of-the-art latent diffusion models such as Stable Diffusion XL to solve video inverse problems. We demonstrate the effectiveness of our method for video inpainting and 8x video super-resolution, outperforming existing techniques based on noise transformations. We provide generated video results in the following URL: https://giannisdaras.github.io/warped_diffusion.github.io/.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
