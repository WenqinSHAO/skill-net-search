---
id: "arxiv-2602"
title: "fVDB: A Deep-Learning Framework for Sparse, Large-Scale, and High-Performance Spatial Intelligence"
conference: "arXiv 2024"
date: "2024-07"
authors:
  - name: "Francis Williams"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Jiahui Huang"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Jonathan Swartz"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Gergely Klar"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Vijay Thakkar"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Matthew Cong"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Xuanchi Ren"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Ruilong Li"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Clement Fuji-Tsang"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Sanja Fidler"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Eftychios Sifakis"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Ken Museth"
    affiliation: "NVIDIA"
    is_industry: true
topics:
  - Foundation_models
  - Graphics_rendering
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Computer Graphics"
  - "Generative AI"
external_links:
  - name: "Project Page"
    url: "https://research.nvidia.com/labs/prl/publication/williams2024fvdb/"
abstract: "We present fVDB, a novel GPU-optimized framework for deep learning on large-scale 3D data. fVDB provides a complete set of differentiable primitives to build deep learning architectures for common tasks in 3D learning such as convolution, pooling, attention, ray-tracing, meshing, etc. fVDB simultane"
url: "https://research.nvidia.com/publication/2024-07_fvdb-deep-learning-framework-sparse-large-scale-and-high-performance-spatial"
status: "new"
---

# fVDB: A Deep-Learning Framework for Sparse, Large-Scale, and High-Performance Spatial Intelligence

## 摘要

We present fVDB, a novel GPU-optimized framework for deep learning on large-scale 3D data. fVDB provides a complete set of differentiable primitives to build deep learning architectures for common tasks in 3D learning such as convolution, pooling, attention, ray-tracing, meshing, etc. fVDB simultaneously provides a much larger feature set (primitives and operators) than established frameworks with no loss in efficiency: our operators match or exceed the performance of other frameworks with narrower scope. Furthermore, fVDB can process datasets with much larger footprint and spatial resolution than prior works, while providing a competitive memory footprint on small inputs. &nbsp;To achieve this combination of versatility and performance, fVDB relies on a single novel VDB index grid acceleration structure paired with several key innovations including GPU accelerated sparse grid construction, convolution using tensor cores, fast ray tracing kernels using HDDA, and jagged tensors.&nbsp;Our framework is fully integrated with PyTorch enabling interoperability with existing pipelines, and we demonstrate its effectiveness on a number of representative tasks such as large-scale point-cloud segmentation, high resolution 3D generative modeling, unbounded scale Neural Radiance Fields, and large-scale point cloud reconstruction.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
