---
id: "neurips-0033"
title: "Elucidating the Design Space of Diffusion-Based Generative Models"
conference: "NeurIPS 2022"
date: "2022-11"
authors:
  - name: "Tero Karras"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Miika Aittala"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Timo Aila"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Samuli Laine"
    affiliation: "NVIDIA"
    is_industry: true
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
  - name: "ArXiv"
    url: "https://arxiv.org/abs/2206.00364"
  - name: "PyTorch implementation"
    url: "https://github.com/NVlabs/edm"
abstract: "We argue that the theory and practice of diffusion-based generative models are currently unnecessarily convoluted and seek to remedy the situation by presenting a design space that clearly separates the concrete design choices. This lets us identify several changes to both the sampling and training "
url: "https://research.nvidia.com/publication/2022-11_elucidating-design-space-diffusion-based-generative-models"
status: "new"
---

# Elucidating the Design Space of Diffusion-Based Generative Models

## 摘要

We argue that the theory and practice of diffusion-based generative models are currently unnecessarily convoluted and seek to remedy the situation by presenting a design space that clearly separates the concrete design choices. This lets us identify several changes to both the sampling and training processes, as well as preconditioning of the score networks. Together, our improvements yield new state-of-the-art FID of 1.79 for CIFAR-10 in a class-conditional setting and 1.97 in an unconditional setting, with much faster sampling (35 network evaluations per image) than prior designs. To further demonstrate their modular nature, we show that our design changes dramatically improve both the efficiency and quality obtainable with pre-trained score networks from previous work, including improving the FID of a previously trained ImageNet-64 model from 2.07 to near-SOTA 1.55, and after re-training with our proposed improvements to a new SOTA of 1.36.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
