---
id: "neurips-0028"
title: "Norm-guided latent space exploration for text-to-image generation"
conference: "NeurIPS 2023"
date: "2023-10"
authors:
  - name: "Dvir Samuel"
    affiliation: "Bar-Ilan University"
    is_industry: false
  - name: "Rami Ben-Ari"
    affiliation: "Bar-Ilan University"
    is_industry: false
  - name: "Nir Darshan"
    affiliation: "Bar-Ilan University"
    is_industry: false
  - name: "Haggai Maron"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Gal Chechik"
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
  - name: "Arxiv"
    url: "https://arxiv.org/abs/2306.08687"
abstract: "Text-to-image diffusion models show great potential in synthesizing a large variety of concepts in new compositions and scenarios. However, their latent seed space is still not well understood and has been shown to have an impact in generating new and rare concepts. Specifically, simple operations l"
url: "https://research.nvidia.com/publication/2023-10_norm-guided-latent-space-exploration-text-image-generation"
status: "new"
---

# Norm-guided latent space exploration for text-to-image generation

## 摘要

Text-to-image diffusion models show great potential in synthesizing a large variety of concepts in new compositions and scenarios. However, their latent seed space is still not well understood and has been shown to have an impact in generating new and rare concepts. Specifically, simple operations like interpolation and centroid finding work poorly with the standard Euclidean and spherical metrics in the latent space. This paper makes the observation that current training procedures make diffusion models biased toward inputs with a narrow range of norm values. This has strong implications for methods that rely on seed manipulation for image generation that can be further applied to few-shot and long-tail learning tasks. To address this issue, we propose a novel method for interpolating between two seeds and demonstrate that it defines a new non-Euclidean metric that takes into account a norm-based prior on seeds. We describe a simple yet efficient algorithm for approximating this metric and use it to further define centroids in the latent seed space. We show that our new interpolation and centroid evaluation techniques significantly enhance the generation of rare concept images. This further leads to state-of-the-art performance on few-shot and long-tail benchmarks, improving prior approach in terms of generation speed, image quality, and semantic content.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
