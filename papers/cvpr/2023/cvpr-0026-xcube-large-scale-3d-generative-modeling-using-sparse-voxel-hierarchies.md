---
id: cvpr-0026
title: "XCube: Large-Scale 3D Generative Modeling using Sparse Voxel Hierarchies"
conference: CVPR 2023
date: 2023-12
authors:
  - name: "Xuanchi Ren"
    affiliation: ""
    is_industry: false
  - name: "Jiahui Huang"
    affiliation: ""
    is_industry: false
  - name: "Xiaohui Zeng"
    affiliation: ""
    is_industry: false
  - name: "Ken Museth"
    affiliation: ""
    is_industry: false
  - name: "Sanja Fidler"
    affiliation: ""
    is_industry: false
  - name: "Francis Williams"
    affiliation: ""
    is_industry: false
topics:
  - AI & Machine Learning
  - Computer Vision
  - Foundation_models
  - AI & Machine Learning
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Artificial Intelligence and Machine Learning"
  - "Computer Vision"
  - "Generative AI"
external_links:
  - name: "Project Page"
    url: "https://research.nvidia.com/labs/toronto-ai/xcube/"
  - name: "Project Video"
    url: "https://www.youtube.com/watch?v=GX0lzwy8nU"
abstract: "We present XCube, a novel generative model for high-resolution sparse 3D voxel grids with arbitrary attributes. Our model can generate millions of voxels with a finest effective resolution of up to $1024^3$ in a feed-forward fashion without time-consuming test-time optimization. To achieve this, we "
url: "https://research.nvidia.com/publication/2023-12_xcube-large-scale-3d-generative-modeling-using-sparse-voxel-hierarchies"
status: new
---

# XCube: Large-Scale 3D Generative Modeling using Sparse Voxel Hierarchies

## 摘要

We present XCube, a novel generative model for high-resolution sparse 3D voxel grids with arbitrary attributes. Our model can generate millions of voxels with a finest effective resolution of up to $1024^3$ in a feed-forward fashion without time-consuming test-time optimization. To achieve this, we employ a hierarchical voxel latent diffusion model which generates progressively higher resolution grids in a coarse-to-fine manner using a custom framework built on the highly efficient VDB data structure. Apart from generating high-resolution objects, we demonstrate the effectiveness of \ShortName on large outdoor scenes at scales of 100m $\times$ 100m with a voxel size as small as 10cm. We observe clear qualitative and quantitative improvements over past approaches. In addition to unconditional generation, we show that our model can be used to solve a variety of tasks such as user-guided editing, scene completion from a single scan, and text-to-3D.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
