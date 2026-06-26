---
id: "arxiv-2725"
title: "Ray Tracing of Signed Distance Function Grids"
conference: "arXiv 2022"
date: "2022-09"
authors:
  - name: "Herman Hansson-Söderlund"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Alex Evans"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Tomas Akenine-Möller"
    affiliation: "NVIDIA"
    is_industry: true
topics:
  - Graphics_rendering
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Computer Graphics"
abstract: "We evaluate the performance of a wide set of combinations of traversal and voxel intersection testing of signed distance function grids in a path tracing setting. In addition, we present an optimized way to compute the intersection between a ray and the surface defined by trilinear interpolation of "
url: "https://research.nvidia.com/publication/2022-09_ray-tracing-signed-distance-function-grids"
status: "new"
---

# Ray Tracing of Signed Distance Function Grids

## 摘要

We evaluate the performance of a wide set of combinations of traversal and voxel intersection testing of signed distance function grids in a path tracing setting. In addition, we present an optimized way to compute the intersection between a ray and the surface defined by trilinear interpolation of signed distances at the eight corners of a voxel. We also provide a novel way to compute continuous normals across voxels and an optimization for shadow rays. On an NVIDIA RTX 3090, the fastest method uses the GPU's ray tracing hardware to trace against a bounding volume hierarchy, built around all non-empty voxels, and then applies either an analytic cubic solver or a repeated linear interpolation for voxel intersection.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
