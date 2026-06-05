---
id: arxiv-2853
title: "Neural Scene Graph Rendering"
conference: arXiv 2021
date: 2021-06
authors:
  - name: "Fabrice Rousselle"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Jan Novák"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Jonathan Granskog"
    affiliation: ""
    is_industry: false
  - name: "Till Schnabel"
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
abstract: "We present a neural scene graph—a modular and controllable representation of scenes with elements that are learned from data. We focus on the forward rendering problem, where the scene graph is provided by the user and references learned elements. The elements correspond to geometry and material def"
url: "https://research.nvidia.com/publication/2021-06_neural-scene-graph-rendering"
status: new
---

# Neural Scene Graph Rendering

## 摘要

We present a neural scene graph—a modular and controllable representation of scenes with elements that are learned from data. We focus on the forward rendering problem, where the scene graph is provided by the user and references learned elements. The elements correspond to geometry and material definitions of scene objects and constitute the leaves of the graph; we store them as high-dimensional vectors. The position and appearance of scene objects can be adjusted in an artist-friendly manner via familiar transformations, e.g. translation, bending, or color hue shift, which are stored in the inner nodes of the graph. In order to apply a (non-linear) transformation to a learned vector, we adopt the concept of linearizing a problem by lifting it into higher dimensions: we first encode the transformation into a high-dimensional matrix and then apply it by standard matrix-vector multiplication. The transformations are encoded using neural networks. We render the scene graph using a streaming neural renderer, which can handle graphs with a varying number of objects, and thereby facilitates scalability. Our results demonstrate a precise control over the learned object representations in a number of animated 2D and 3D scenes. Despite the limited visual complexity, our work presents a step towards marrying traditional editing mechanisms with learned representations, and towards high-quality, controllable neural rendering.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
