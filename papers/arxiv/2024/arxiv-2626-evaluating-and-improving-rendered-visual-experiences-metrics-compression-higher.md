---
id: "arxiv-2626"
title: "Evaluating and Improving Rendered Visual Experiences: Metrics, Compression, Higher Frame Rates &amp; Recoloring"
conference: "arXiv 2024"
date: "2024-02"
authors:
  - name: "Pontus Ebelin"
    affiliation: "NVIDIA"
    is_industry: true
topics:
  - Applied_perception
  - Graphics_rendering
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Applied Perception"
  - "Computer Graphics"
  - "Real-Time Rendering"
external_links:
  - name: "PhD Thesis (Electronic) [308 MB]"
    url: "https://portal.research.lu.se/files/171170278/PontusEbelinPhDThesis.pdf"
  - name: "PhD Thesis at Lund University&#039;s Research Portal"
    url: "https://portal.research.lu.se/en/publications/evaluating-and-improving-rendered-visual-experiences-metrics-comp"
abstract: "Rendered imagery is presented to us daily. Special effects in movies, video games, scientific visualizations, and marketing catalogs all often rely on images generated through computer graphics. However, with all the possibilities that rendering offers come also a plethora of challenges. This thesis"
url: "https://research.nvidia.com/publication/2024-02_evaluating-and-improving-rendered-visual-experiences"
status: "new"
---

# Evaluating and Improving Rendered Visual Experiences: Metrics, Compression, Higher Frame Rates &amp; Recoloring

## 摘要

Rendered imagery is presented to us daily. Special effects in movies, video games, scientific visualizations, and marketing catalogs all often rely on images generated through computer graphics. However, with all the possibilities that rendering offers come also a plethora of challenges. This thesis proposes novel ways of evaluating the visual errors caused when some of those challenges are not completely overcome. The thesis also suggests ways to improve on the visual experience observers have when viewing rendered content.In the introduction of this thesis, I provide an overview of a subset of the many and fantastic aspects of the human visual system. I also describe how images are rendered using computer graphics, some of the related challenges, and how the final result is displayed to users. Finally, I discuss some of the basics of image and video quality assessment. The scientific publications contained in this thesis focus on image quality metrics, compression, and rendering at high frame rates. In addition, one paper considers the recoloring of images with the goal of giving people with color vision deficiencies an improved visual experience in a process known as daltonization.Papers I–III suggest ways to evaluate and communicate the errors that users may see in rendered images. In those papers, an image’s error is determined by how much it visually differs from a perfect-quality version of the same view. The focus is on the error map, an image that indicates the magnitude and locations of errors. In Paper IV, tools proposed in the first three papers are used to convey how a novel material texture compression algorithm results in lower visual error compared to competing techniques at similar, low bit rates. To achieve good quality at high compression rates, the proposed algorithm exploits similarities in the textures used for materials.Starting with Paper V, the thesis puts increased emphasis on temporal effects. That paper estimates the temporal edge detection filters in human vision, while previous research had mainly examined spatial edge detection filters. Paper VI demonstrates how perceived quality in rendering can be improved by leveraging the human visual system. The paper suggests a method for rendering ~4× more frames per second, which, paired with content-dependent sampling patterns and reconstruction, improves the overall visual experience of rendered image sequences despite reducing the quality of individual frames. This thesis’ final paper, Paper VII, presents a real-time daltonization algorithm that recolors images in a temporally consistent manner, so as to avoid flickering hue changes in image sequences, which are often an issue for competing algorithms that target single images. The proposed recoloring preserves luminance and, thus, the important visual ques it provides.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
