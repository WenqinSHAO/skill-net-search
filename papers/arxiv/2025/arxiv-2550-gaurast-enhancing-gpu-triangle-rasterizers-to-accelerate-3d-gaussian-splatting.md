---
id: "arxiv-2550"
title: "GauRast: Enhancing GPU Triangle Rasterizers to Accelerate 3D Gaussian Splatting"
conference: "arXiv 2025"
date: "2025-06"
authors:
  - name: "Sixu Li"
    affiliation: "Georgia Tech"
    is_industry: false
  - name: "Ben Keller"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Yingyan Celine Lin"
    affiliation: "Georgia Tech"
    is_industry: false
  - name: "Brucek Khailany"
    affiliation: "NVIDIA"
    is_industry: true
topics:
  - GPU_architecture
  - Graphics_rendering
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Computer Architecture"
  - "Computer Graphics"
abstract: "3D intelligence leverages rich 3D features and stands as a promising frontier in AI, with 3D rendering fundamental to many downstream applications. 3D Gaussian Splatting (3DGS), an emerging high-quality 3D rendering method, requires significant computation, making real-time execution on existing GPU"
url: "https://research.nvidia.com/publication/2025-06_gaurast-enhancing-gpu-triangle-rasterizers-accelerate-3d-gaussian-splatting"
status: "new"
---

# GauRast: Enhancing GPU Triangle Rasterizers to Accelerate 3D Gaussian Splatting

## 摘要

3D intelligence leverages rich 3D features and stands as a promising frontier in AI, with 3D rendering fundamental to many downstream applications. 3D Gaussian Splatting (3DGS), an emerging high-quality 3D rendering method, requires significant computation, making real-time execution on existing GPU-equipped edge devices infeasible. Previous efforts to accelerate 3DGS rely on dedicated accelerators that require substantial integration overhead and hardware costs. This work proposes an acceleration strategy that leverages the similarities between the 3DGS pipeline and the highly optimized conventional graphics pipeline in modern GPUs. Instead of developing a dedicated accelerator, we enhance existing GPU rasterizer hardware to efficiently support 3DGS operations. Our results demonstrate a 23× increase in processing speed and a 24× reduction in energy consumption, with improvements yielding 6× faster end-to-end runtime for the original 3DGS algorithm and 4× for the latest efficiency-improved pipeline, achieving 24 FPS and 46 FPS respectively. These enhancements incur only a minimal area overhead of 0.2% relative to the entire SoC chip area, underscoring the practicality and efficiency of our approach for enabling 3DGS rendering on resource-constrained platforms.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
