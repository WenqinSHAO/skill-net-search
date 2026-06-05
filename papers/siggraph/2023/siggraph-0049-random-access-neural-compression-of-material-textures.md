---
id: siggraph-0049
title: "Random-Access Neural Compression of Material Textures"
conference: SIGGRAPH 2023
date: 2023-08
authors:
  - name: "Bart Wronski"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Tomas Akenine-Möller"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Pontus Ebelin"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Aaron Lefohn"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Karthik Vaidyanathan"
    affiliation: ""
    is_industry: false
  - name: "Marco Salvi"
    affiliation: ""
    is_industry: false
topics:
  - AI & Machine Learning
  - Graphics_rendering
  - AI & Machine Learning
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Artificial Intelligence and Machine Learning"
  - "Computer Graphics"
external_links:
  - name: "Project Page"
    url: "https://research.nvidia.com/labs/rtr/neural_texture_compression/"
abstract: "The continuous advancement of photorealism in rendering is accompanied by a growth in texture data and, consequently, increasing storage and memory demands. To address this issue, we propose a novel neural compression technique specifically designed for material textures. We unlock two more levels o"
url: "https://research.nvidia.com/publication/2023-08_random-access-neural-compression-material-textures"
status: new
---

# Random-Access Neural Compression of Material Textures

## 摘要

The continuous advancement of photorealism in rendering is accompanied by a growth in texture data and, consequently, increasing storage and memory demands. To address this issue, we propose a novel neural compression technique specifically designed for material textures. We unlock two more levels of detail, i.e., 16×&nbsp;more texels, using low bitrate compression, with image quality that is better than advanced image compression techniques, such as AVIF and JPEG XL. At the same time, our method allows for on-demand, real-time decompression with random access similar to block texture compression on GPUs. This extends our compression benefits all the way from disk storage to memory. The key idea behind our approach is compressing multiple material textures and their mipmap chains together, and using a small neural network, that is optimized for each material, to decompress them. Finally, we use a custom training implementation to achieve practical compression speeds, whose performance surpasses that of general frameworks, like PyTorch, by an order of magnitude.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
