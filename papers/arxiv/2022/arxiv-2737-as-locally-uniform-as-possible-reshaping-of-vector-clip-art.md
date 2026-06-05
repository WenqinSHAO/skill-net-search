---
id: arxiv-2737
title: "As-Locally-Uniform-as-Possible Reshaping of Vector Clip Art"
conference: arXiv 2022
date: 2022-08
authors:
  - name: "Nicholas Vining"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Chrystiano Araujo"
    affiliation: ""
    is_industry: false
  - name: "Enrique Rosales"
    affiliation: ""
    is_industry: false
  - name: "Giorgio Gori"
    affiliation: ""
    is_industry: false
  - name: "Alla Sheffer"
    affiliation: ""
    is_industry: false
topics:
  - Applied_perception
  - CUDA_ecosystem
  - Graphics_rendering
  - AI & Machine Learning
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Algorithms and Numerical Methods"
  - "Applied Perception"
  - "Computer Graphics"
external_links:
  - name: "Project Webpage"
    url: "https://www.cs.ubc.ca/labs/imager/tr/2022/ALUP/"
abstract: "Vector clip-art images consist of regions bounded by a network of vector curves. Users often wish to reshape, or rescale, existing clip-art images by changing the locations, proportions, or scales of different image elements. When reshaping images depicting synthetic content they seek to preserve gl"
url: "https://research.nvidia.com/publication/2022-08_locally-uniform-possible-reshaping-vector-clip-art"
status: new
---

# As-Locally-Uniform-as-Possible Reshaping of Vector Clip Art

## 摘要

Vector clip-art images consist of regions bounded by a network of vector curves. Users often wish to reshape, or rescale, existing clip-art images by changing the locations, proportions, or scales of different image elements. When reshaping images depicting synthetic content they seek to preserve global and local structures. These structures are best preserved when the gradient of the mapping between the original and the reshaped curve networks is locally as close as possible to a uniform scale; mappings that satisfy this property maximally preserve the input curve orientations and minimally change the shape of the input's geometric details, while allowing changes in the relative scales of the different features. The expectation of approximate scale uniformity is local; while reshaping operations are typically expected to change the relative proportions of a subset of network regions, users expect the change to be minimal away from the directly impacted regions and expect such changes to be gradual and distributed as evenly as possible. Unfortunately, existing methods for editing 2D curve networks do not satisfy these criteria. We propose a targeted As-Locally-Uniform-as-Possible (ALUP) vector clip-art reshaping method that satisfies the properties above. We formulate the computation of the desired output network as the solution of a constrained variational optimization problem. We effectively compute the desired solution by casting this continuous problem as a minimization of a non-linear discrete energy function, and obtain the desired minimizer by using a custom iterative solver. We validate our method via perceptual studies comparing our results to those created via algorithmic alternatives and manually generated ones. Participants preferred our results over the closest alternative by a ratio of 6 to 1.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
