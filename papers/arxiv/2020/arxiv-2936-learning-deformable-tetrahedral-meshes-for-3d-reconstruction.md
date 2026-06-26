---
id: "arxiv-2936"
title: "Learning Deformable Tetrahedral Meshes for 3D Reconstruction"
conference: "arXiv 2020"
date: "2020-12"
authors:
  - name: "Jun Gao"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Wenzheng Chen"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Tommy Xiang"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Clement Fuji Tsang"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Alec Jacobson"
    affiliation: "University of Toronto"
    is_industry: false
  - name: "Morgan McGuire"
    affiliation: "NVIDIA"
    is_industry: true
topics:
  - AI & Machine Learning
  - Computer Vision
  - Graphics_rendering
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Artificial Intelligence and Machine Learning"
  - "Computer Graphics"
  - "Computer Vision"
  - "Hyperscale Graphics"
external_links:
  - name: "Supplement (PDF)"
    url: "https://nv-tlabs.github.io/DefTet/files/supplement.pdf"
  - name: "Source Code"
    url: "https://github.com/nv-tlabs/DefTet"
  - name: "Website"
    url: "https://nv-tlabs.github.io/DefTet/"
abstract: "3D shape representations that accommodate learning-based 3D reconstruction are an open problem in machine learning and computer graphics. Previous work on neural 3D reconstruction demonstrated benefits, but also limitations, of point cloud, voxel, surface mesh, and implicit function representations."
url: "https://research.nvidia.com/publication/2020-12_learning-deformable-tetrahedral-meshes-3d-reconstruction"
status: "new"
---

# Learning Deformable Tetrahedral Meshes for 3D Reconstruction

## 摘要

3D shape representations that accommodate learning-based 3D reconstruction are an open problem in machine learning and computer graphics. Previous work on neural 3D reconstruction demonstrated benefits, but also limitations, of point cloud, voxel, surface mesh, and implicit function representations. We introduce Deformable Tetrahedral Meshes (DefTet) as a particular parameterization that utilizes volumetric tetrahedral meshes for the reconstruction problem. Unlike existing volumetric approaches, DefTet optimizes for both vertex placement and occupancy, and is differentiable with respect to standard 3D reconstruction loss functions. It is thus simultaneously high-precision, volumetric, and amenable to learning-based neural architectures. We show that it can represent arbitrary, complex topology, is both memory and computationally efficient, and can produce high-fidelity reconstructions with a significantly smaller grid size than alternative volumetric approaches. The predicted surfaces are also inherently defined as tetrahedral meshes, thus do not require post-processing. We demonstrate that DefTet matches or exceeds both the quality of the previous best approaches and the performance of the fastest ones. Our approach obtains high-quality tetrahedral meshes computed directly from noisy point clouds, and is the first to showcase high-quality 3D tet-mesh results using only a single image as input.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
