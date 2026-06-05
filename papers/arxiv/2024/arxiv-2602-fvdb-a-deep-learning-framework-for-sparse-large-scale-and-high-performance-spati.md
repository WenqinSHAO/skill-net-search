---
id: arxiv-2602
title: "fVDB: A Deep-Learning Framework for Sparse, Large-Scale, and High-Performance Spatial Intelligence"
conference: arXiv 2024
date: 2024-07
authors:
  - name: "Francis Williams"
    affiliation: ""
    is_industry: false
  - name: "Jiahui Huang"
    affiliation: ""
    is_industry: false
  - name: "Jonathan Swartz"
    affiliation: ""
    is_industry: false
  - name: "Gergely Klar"
    affiliation: ""
    is_industry: false
  - name: "Vijay Thakkar"
    affiliation: ""
    is_industry: false
  - name: "Matthew Cong"
    affiliation: ""
    is_industry: false
  - name: "Xuanchi Ren"
    affiliation: ""
    is_industry: false
  - name: "Ruilong Li"
    affiliation: ""
    is_industry: false
  - name: "Clement Fuji-Tsang"
    affiliation: ""
    is_industry: false
  - name: "Sanja Fidler"
    affiliation: ""
    is_industry: false
  - name: "Eftychios Sifakis"
    affiliation: ""
    is_industry: false
  - name: "Ken Museth"
    affiliation: ""
    is_industry: false
topics:
  - Foundation_models
  - Graphics_rendering
  - AI & Machine Learning
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
status: new
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
