---
id: "siggraph-0033"
title: "Flexible Isosurface Extraction for Gradient-Based Mesh Optimization"
conference: "SIGGRAPH 2023"
date: "2023-08"
authors:
  - name: "Tianchang Shen"
    affiliation: "NVIDIA, University of Toronto, Vector Institute"
    is_industry: true
  - name: "Jacob Munkberg"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Jon Hasselgren"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Kangxue Yin"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Zian Wang"
    affiliation: "NVIDIA, University of Toronto, Vector Institute"
    is_industry: true
  - name: "Wenzheng Chen"
    affiliation: "NVIDIA, University of Toronto, Vector Institute"
    is_industry: true
  - name: "Zan Gojcic"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Sanja Fidler"
    affiliation: "NVIDIA, University of Toronto, Vector Institute"
    is_industry: true
  - name: "Nicholas Sharp"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Jun Gao"
    affiliation: "NVIDIA"
    is_industry: true
topics:
  - AI & Machine Learning
  - Computer Vision
  - Foundation_models
  - Graphics_rendering
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Artificial Intelligence and Machine Learning"
  - "Computer Graphics"
  - "Computer Vision"
  - "Generative AI"
external_links:
  - name: "Project page"
    url: "https://research.nvidia.com/labs/toronto-ai/flexicubes/"
  - name: "Paper"
    url: "https://dl.acm.org/doi/abs/10.1145/3592430"
abstract: "This work considers gradient-based mesh optimization, where we iteratively optimize for a 3D surface mesh by representing it as the isosurface of a scalar field, an increasingly common paradigm in applications including photogrammetry, generative modeling, and inverse physics. Existing implementatio"
url: "https://research.nvidia.com/publication/2023-08_flexible-isosurface-extraction-gradient-based-mesh-optimization"
status: "new"
---

# Flexible Isosurface Extraction for Gradient-Based Mesh Optimization

## 摘要

This work considers gradient-based mesh optimization, where we iteratively optimize for a 3D surface mesh by representing it as the isosurface of a scalar field, an increasingly common paradigm in applications including photogrammetry, generative modeling, and inverse physics. Existing implementations adapt classic isosurface extraction algorithms like Marching Cubes or Dual Contouring; these techniques were designed to extract meshes from fixed, known fields, and in the optimization setting they lack the degrees of freedom to represent high-quality feature-preserving meshes, or suffer from numerical instabilities. We introduce&nbsp;FlexiCubes, an isosurface representation specifically designed for optimizing an unknown mesh with respect to geometric, visual, or even physical objectives. Our main insight is to introduce additional carefully-chosen parameters into the representation, which allow local flexible adjustments to the extracted mesh geometry and connectivity. These parameters are updated along with the underlying scalar field via automatic differentiation when optimizing for a downstream task. We base our extraction scheme on Dual Marching Cubes for improved topological properties, and present extensions to optionally generate tetrahedral and hierarchically-adaptive meshes. Extensive experiments validate&nbsp;FlexiCubes&nbsp;on both synthetic benchmarks and real-world applications, showing that it offers significant improvements in mesh quality and geometric fidelity.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
