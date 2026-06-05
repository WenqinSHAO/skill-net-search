---
id: siggraph-0040
title: "Micro-Mesh Construction"
conference: SIGGRAPH 2023
date: 2023-08
authors:
  - name: "Andrea Maggiordomo"
    affiliation: ""
    is_industry: false
  - name: "Henry Moreton"
    affiliation: ""
    is_industry: false
  - name: "Marco Tarini"
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
abstract: "Micro-meshes (𝜇-meshes) are a new structured graphics primitive supporting a large increase in geometric fidelity without commensurate memory and run-time processing costs, consisting of a base mesh enriched by a displacement map. A new generation of GPUs support this structure with native hardware "
url: "https://research.nvidia.com/publication/2023-08_micro-mesh-construction"
status: new
---

# Micro-Mesh Construction

## 摘要

Micro-meshes (𝜇-meshes) are a new structured graphics primitive supporting a large increase in geometric fidelity without commensurate memory and run-time processing costs, consisting of a base mesh enriched by a displacement map. A new generation of GPUs support this structure with native hardware 𝜇-mesh ray-tracing, which leverages a self-bounding, compressed displacement mapping scheme to achieve these efficiencies. In this paper, we present an automatic method to convert an existing multi-million triangle mesh into this compact format, unlocking the advantages of the data representation for a large number of scenarios. We identify the requirements for high-quality 𝜇-meshes, and show how existing re-meshing and displacement-map baking tools are ill-suited for their generation. Our method is based on a simplification scheme tailored to the generation of high-quality base meshes, optimized for tessellation and displacement sampling, in conjunction with algorithms for determining displacement vectors to control the direction and range of displacements. We also explore the optimization of 𝜇-meshes for texture maps and boundary representations. We demonstrate our method with extensive batch processing, converting an existing collection of high-resolution scanned models to the micro-mesh representation, providing the data and an inspection tool as additional material.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
