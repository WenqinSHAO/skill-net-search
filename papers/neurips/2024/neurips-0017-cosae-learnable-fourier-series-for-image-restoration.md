---
id: "neurips-0017"
title: "CosAE: Learnable Fourier Series for Image Restoration"
conference: "NeurIPS 2024"
date: "2024-12"
authors:
  - name: "Sifei Liu"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Shalini De Mello"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Jan Kautz"
    affiliation: "NVIDIA"
    is_industry: true
topics:
  - AI & Machine Learning
  - Computer Vision
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Artificial Intelligence and Machine Learning"
  - "Computer Vision"
external_links:
  - name: "Project Page"
    url: "https://sifeiliu.net/CosAE-page/"
  - name: "Video"
    url: "https://www.youtube.com/watch?v=eYvohDeF8CE"
abstract: "In this paper, we introduce Cosine Autoencoder (CosAE), a novel, generic Autoencoder that seamlessly leverages the classic Fourier series with a feed-forward neural network. CosAE represents an input image as a series of 2D Cosine time series, each defined by a tuple of learnable frequency and Fouri"
url: "https://research.nvidia.com/publication/2024-12_cosae-learnable-fourier-series-image-restoration"
status: "new"
---

# CosAE: Learnable Fourier Series for Image Restoration

## 摘要

In this paper, we introduce Cosine Autoencoder (CosAE), a novel, generic Autoencoder that seamlessly leverages the classic Fourier series with a feed-forward neural network. CosAE represents an input image as a series of 2D Cosine time series, each defined by a tuple of learnable frequency and Fourier coefficients. This method stands in contrast to a conventional Autoencoder that often sacrifices detail in their reduced-resolution bottleneck latent spaces. CosAE, however, encodes frequency coefficients, i.e., the amplitudes and phases, in its bottleneck. This encoding enables extreme spatial compression, e.g., 64× downsampled feature maps in the bottleneck, without losing detail upon decoding. We showcase the advantage of CosAE via extensive experiments on flexible-resolution superresolution and blind image restoration, two highly challenging tasks that demand the restoration network to effectively generalize to complex and even unknown image degradations. Our method surpasses state-of-the-art approaches, highlighting its capability to learn a generalizable representation for image restoration. The project page is maintained at https://sifeiliu.net/CosAE-page/.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
