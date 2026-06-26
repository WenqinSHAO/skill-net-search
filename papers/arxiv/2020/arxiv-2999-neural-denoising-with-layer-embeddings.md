---
id: "arxiv-2999"
title: "Neural Denoising with Layer Embeddings"
conference: "arXiv 2020"
date: "2020-06"
authors:
  - name: "Jacob Munkberg"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Jon Hasselgren"
    affiliation: "NVIDIA"
    is_industry: true
topics:
  - Graphics_rendering
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Computer Graphics"
  - "Real-Time Rendering"
external_links:
  - name: "Paper"
    url: "https://diglib.eg.org/bitstream/handle/10.1111/cgf14049/v39i4pp001-012.pdf"
  - name: "Supplemental material"
    url: "https://diglib.eg.org/bitstream/handle/10.1111/cgf14049/supplemental_camera.zip?sequence=2&amp;isAllowed=y"
  - name: "Source code on github"
    url: "https://github.com/NVlabs/layerdenoise/"
abstract: "We propose a novel approach for denoising Monte Carlo path traced images, which uses data from individual samples rather than relying on pixel aggregates. Samples are partitioned into layers, which are filtered separately, giving the network more freedom to handle outliers and complex visibility. Fi"
url: "https://research.nvidia.com/publication/2020-06_neural-denoising-layer-embeddings"
status: "new"
---

# Neural Denoising with Layer Embeddings

## 摘要

We propose a novel approach for denoising Monte Carlo path traced images, which uses data from individual samples rather than relying on pixel aggregates. Samples are partitioned into layers, which are filtered separately, giving the network more freedom to handle outliers and complex visibility. Finally the layers are composited front-to-back using alpha blending. The system is trained end-to-end, with learned layer partitioning, filter kernels, and compositing. We obtain similar image quality as recent state-of-the-art sample based denoisers at a fraction of the computational cost and memory requirements.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
