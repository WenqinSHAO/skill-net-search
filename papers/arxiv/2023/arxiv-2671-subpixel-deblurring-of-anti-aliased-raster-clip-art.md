---
id: arxiv-2671
title: "Subpixel Deblurring of Anti-Aliased Raster Clip Art"
conference: arXiv 2023
date: 2023-05
authors:
  - name: "Nicholas Vining"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Jinfan Yang"
    affiliation: ""
    is_industry: false
  - name: "Shakiba Kheradmand"
    affiliation: ""
    is_industry: false
  - name: "Nathan Carr"
    affiliation: ""
    is_industry: false
  - name: "Leonid Sigal"
    affiliation: ""
    is_industry: false
  - name: "Alla Sheffer"
    affiliation: ""
    is_industry: false
topics:
  - AI & Machine Learning
  - Applied_perception
  - Computer Vision
  - Foundation_models
  - Graphics_rendering
  - AI & Machine Learning
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Applied Perception"
  - "Artificial Intelligence and Machine Learning"
  - "Computational Photography and Imaging"
  - "Computer Graphics"
  - "Computer Vision"
  - "Generative AI"
external_links:
  - name: "Paper"
    url: "https://diglib.eg.org/handle/10.1111/cgf14744"
abstract: "Artist generated clip-art images typically consist of a small number of distinct, uniformly colored regions with clear boundaries. Legacy artist created images are often stored in low-resolution (100x100px or less) anti-aliased raster form. Compared to anti-aliasing free rasterization, anti-aliasing"
url: "https://research.nvidia.com/publication/2023-05_subpixel-deblurring-anti-aliased-raster-clip-art"
status: new
---

# Subpixel Deblurring of Anti-Aliased Raster Clip Art

## 摘要

Artist generated clip-art images typically consist of a small number of distinct, uniformly colored regions with clear boundaries. Legacy artist created images are often stored in low-resolution (100x100px or less) anti-aliased raster form. Compared to anti-aliasing free rasterization, anti-aliasing blurs inter-region boundaries and obscures the artist's intended region topology and color palette; at the same time, it better preserves subpixel details. Recovering the underlying artist-intended images from their low-resolution anti-aliased rasterizations can facilitate resolution independent rendering, lossless vectorization, and other image processing applications. Unfortunately, while human observers can mentally deblur these low-resolution images and reconstruct region topology, color and subpixel details, existing algorithms applicable to this task fail to produce outputs consistent with human expectations when presented with such images. We recover these viewer perceived blur-free images at subpixel resolution, producing outputs where each input pixel is replaced by four corresponding (sub)pixels. Performing this task requires computing the size of the output image color palette, generating the palette itself, and associating each pixel in the output with one of the colors in the palette. We obtain these desired output components by leveraging a combination of perceptual and domain priors, and real world data. We use readily available data to train a network that predicts, for each antialiased image, a low-blur approximation of the blur-free double-resolution outputs we seek. The images obtained at this stage are perceptually closer to the desired outputs but typically still have hundreds of redundant differently colored regions with fuzzy boundaries. We convert these low-blur intermediate images into blur-free outputs consistent with viewer expectations using a discrete partitioning procedure guided by the characteristic properties of clip-art images, observations about the antialiasing process, and human perception of anti-aliased clip-art. This step dramatically reduces the size of the output color palettes, and the region counts bringing them in line with viewer expectations and enabling the image processing applications we target. We demonstrate the utility of our method by using our outputs for a number of image processing tasks, and validate it via extensive comparisons to prior art. In our comparative study, participants preferred our deblurred outputs over those produced by the best-performing alternative by a ratio of 75 to 8.5.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
