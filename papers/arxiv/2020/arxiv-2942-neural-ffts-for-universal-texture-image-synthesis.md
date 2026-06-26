---
id: "arxiv-2942"
title: "Neural FFTs for Universal Texture Image Synthesis"
conference: "arXiv 2020"
date: "2020-12"
authors:
  - name: "Morteza Mardani"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Guilin Liu"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Aysegul Dundar"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Shiqiu Liu"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Andrew Tao"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Bryan Catanzaro"
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
abstract: "Synthesizing larger texture images from a smaller exemplar is an important task in graphics and vision. The conventional CNNs, recently adopted for synthesis, require to train and test on the same set of images and fail to generalize to unseen images. This is mainly because those CNNs fully rely on "
url: "https://research.nvidia.com/publication/2020-12_neural-ffts-universal-texture-image-synthesis"
status: "new"
---

# Neural FFTs for Universal Texture Image Synthesis

## 摘要

Synthesizing larger texture images from a smaller exemplar is an important task in graphics and vision. The conventional CNNs, recently adopted for synthesis, require to train and test on the same set of images and fail to generalize to unseen images. This is mainly because those CNNs fully rely on convolutional and upsampling layers that operate locally and not suitable for a task as global as texture synthesis. In this work, inspired by the repetitive nature of texture patterns, we find that texture synthesis can be viewed as (local) \textit{upsampling} in the Fast Fourier Transform (FFT) domain. However, FFT of natural images exhibits high dynamic range and lacks local correlations. Therefore, to train CNNs we design a framework to perform FFT upsampling in feature space using deformable convolutions. Such design allows our framework to generalize to unseen images, and synthesize textures in a single pass. Extensive evaluations confirm that our method achieves state-of-the-art performance both quantitatively and qualitatively.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
