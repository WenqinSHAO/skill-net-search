---
id: siggraph-0030
title: "Compact Neural Graphics Primitives with Learned Hash Probing"
conference: SIGGRAPH 2023
date: 2023-12
authors:
  - name: "Thomas Müller"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Merlin Nimier-David"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Sanja Fidler"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Alex Keller"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Towaki Takikawa"
    affiliation: ""
    is_industry: false
  - name: "Alex Evans"
    affiliation: ""
    is_industry: false
  - name: "Alec Jacobson"
    affiliation: ""
    is_industry: false
topics:
  - AI & Machine Learning
  - CUDA_ecosystem
  - Computer Vision
  - Graphics_rendering
  - AI & Machine Learning
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Algorithms and Numerical Methods"
  - "Artificial Intelligence and Machine Learning"
  - "Computer Graphics"
  - "Computer Vision"
external_links:
  - name: "Project Page"
    url: "https://research.nvidia.com/labs/toronto-ai/compact-ngp/"
abstract: "Neural graphics primitives are faster and achieve higher quality when their neural networks are augmented by spatial data structures that hold trainable features arranged in a grid. However, existing feature grids either come with a large memory footprint (dense or factorized grids, trees, and hash "
url: "https://research.nvidia.com/publication/2023-12_compact-neural-graphics-primitives-learned-hash-probing"
status: new
---

# Compact Neural Graphics Primitives with Learned Hash Probing

## 摘要

Neural graphics primitives are faster and achieve higher quality when their neural networks are augmented by spatial data structures that hold trainable features arranged in a grid. However, existing feature grids either come with a large memory footprint (dense or factorized grids, trees, and hash tables) or slow performance (index learning and vector quantization). In this paper, we show that a hash table with learned probes has neither disadvantage, resulting in a favorable combination of size and speed. Inference is faster than unprobed hash tables at equal quality while training is only 1.2-2.6x slower, significantly outperforming prior index learning approaches. We arrive at this formulation by casting all feature grids into a common framework: they each correspond to a lookup function that indexes into a table of feature vectors. In this framework, the lookup functions of existing data structures can be combined by simple arithmetic combinations of their indices, resulting in Pareto optimal compression and speed.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
