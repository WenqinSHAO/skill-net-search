---
id: "cvpr-0019"
title: "What You See is What You GAN: Rendering Every Pixel for High-Fidelity Geometry in 3D GANs"
conference: "CVPR 2024"
date: "2024-06"
authors:
  - name: "Alexander Trevithick"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Matthew Chan"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Towaki Takikawa"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Umar Iqbal"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Shalini De Mello"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Manmohan Chandraker"
    affiliation: "University of California at San Diego"
    is_industry: false
  - name: "Ravi Ramamoorthi"
    affiliation: "University of California at San Diego"
    is_industry: false
  - name: "Koki Nagano"
    affiliation: "NVIDIA"
    is_industry: true
topics:
  - AI & Machine Learning
  - Computer Vision
  - Foundation_models
  - Graphics_rendering
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Artificial Intelligence and Machine Learning"
  - "Computer Graphics"
  - "Computer Vision"
  - "Generative AI"
external_links:
  - name: "Project Page"
    url: "https://research.nvidia.com/labs/nxp/wysiwyg/"
  - name: "ArXiv"
    url: "https://arxiv.org/abs/2401.02411"
abstract: "3D-aware Generative Adversarial Networks (GANs) have shown remarkable progress in learning to generate multi-view-consistent images and 3D geometries of scenes from collections of 2D images via neural volume rendering. Yet, the significant memory and computational costs of dense sampling in volume r"
url: "https://research.nvidia.com/publication/2024-06_what-you-see-what-you-gan-rendering-every-pixel-high-fidelity-geometry-3d-gans"
status: "new"
---

# What You See is What You GAN: Rendering Every Pixel for High-Fidelity Geometry in 3D GANs

## 摘要

3D-aware Generative Adversarial Networks (GANs) have shown remarkable progress in learning to generate multi-view-consistent images and 3D geometries of scenes from collections of 2D images via neural volume rendering. Yet, the significant memory and computational costs of dense sampling in volume rendering have forced 3D GANs to adopt patch-based training or employ low-resolution rendering with post-processing 2D super resolution, which sacrifices multiview consistency and the quality of resolved geometry. Consequently, 3D GANs have not yet been able to fully resolve the rich 3D geometry present in 2D images. In this work, we propose techniques to scale neural volume rendering to the much higher resolution of native 2D images, thereby resolving fine-grained 3D geometry with unprecedented detail. Our approach employs learningbased samplers for accelerating neural rendering for 3D GAN training using up to 5 times fewer depth samples. This enables us to explicitly ”render every pixel” of the full-resolution image during training and inference without post-processing superresolution in 2D. Together with our strategy to learn high-quality surface geometry, our method synthesizes high-resolution 3D geometry and strictly viewconsistent images while maintaining image quality on par with baselines relying on post-processing super resolution. We demonstrate state-of-the-art 3D gemetric quality on FFHQ and AFHQ, setting a new standard for unsupervised learning of 3D shapes in 3D GANs.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
