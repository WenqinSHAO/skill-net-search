---
id: "arxiv-2952"
title: "Modular Primitives for High-Performance Differentiable Rendering"
conference: "arXiv 2020"
date: "2020-11"
authors:
  - name: "Samuli Laine"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Janne Hellsten"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Tero Karras"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Yeongho Seol"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Jaakko Lehtinen"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Timo Aila"
    affiliation: "NVIDIA"
    is_industry: true
topics:
  - AI & Machine Learning
  - Graphics_rendering
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Artificial Intelligence and Machine Learning"
  - "Computer Graphics"
external_links:
  - name: "Paper (arXiv)"
    url: "https://arxiv.org/abs/2011.03277"
  - name: "Code (GitHub)"
    url: "https://github.com/NVlabs/nvdiffrast"
abstract: "We present a modular differentiable renderer design that yields performance superior to previous methods by leveraging existing, highly optimized hardware graphics pipelines. Our design supports all crucial operations in a modern graphics pipeline: rasterizing large numbers of triangles, attribute i"
url: "https://research.nvidia.com/publication/2020-11_modular-primitives-high-performance-differentiable-rendering"
status: "new"
---

# Modular Primitives for High-Performance Differentiable Rendering

## 摘要

We present a modular differentiable renderer design that yields performance superior to previous methods by leveraging existing, highly optimized hardware graphics pipelines. Our design supports all crucial operations in a modern graphics pipeline: rasterizing large numbers of triangles, attribute interpolation, filtered texture lookups, as well as user-programmable shading and geometry processing, all in high resolutions. Our modular primitives allow custom, high-performance graphics pipelines to be built directly within automatic differentiation frameworks such as PyTorch or TensorFlow. As a motivating application, we formulate facial performance capture as an inverse rendering problem and show that it can be solved efficiently using our tools. Our results indicate that this simple and straightforward approach achieves excellent geometric correspondence between rendered results and reference imagery.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
