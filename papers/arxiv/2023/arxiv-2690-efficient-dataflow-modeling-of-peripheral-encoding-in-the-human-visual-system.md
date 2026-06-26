---
id: "arxiv-2690"
title: "Efficient Dataflow Modeling of Peripheral Encoding in the Human Visual System"
conference: "arXiv 2023"
date: "2023-01"
authors:
  - name: "Rachel Brown"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Vasha DuTell"
    affiliation: "UC Berkeley"
    is_industry: false
  - name: "Bruce Walter"
    affiliation: "Cornell University"
    is_industry: false
  - name: "Ruth Rosenholtz"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Peter Shirley"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Morgan McGuire"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "David Luebke"
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
abstract: "Computer graphics seeks to deliver compelling images, generated within a computing budget, targeted at a specific display device, and ultimately viewed by an individual user. The foveated nature of human vision offers an opportunity to efficiently allocate computation and compression to appropriate "
url: "https://research.nvidia.com/publication/2023-01_efficient-dataflow-modeling-peripheral-encoding-human-visual-system"
status: "new"
---

# Efficient Dataflow Modeling of Peripheral Encoding in the Human Visual System

## 摘要

Computer graphics seeks to deliver compelling images, generated within a computing budget, targeted at a specific display device, and ultimately viewed by an individual user. The foveated nature of human vision offers an opportunity to efficiently allocate computation and compression to appropriate areas of the viewer’s visual field, of particular importance with the rise of high-resolution and wide field-of-view display devices. However, while variations in acuity and contrast sensitivity across the field of view have been well-studied and modeled, a more consequential variation concerns peripheral vision’s degradation in the face of clutter, known as crowding. Understanding of peripheral crowding has greatly advanced in recent years, in terms of both phenomenology and modeling. Accurately leveraging this knowledge is critical for many applications, as peripheral vision covers a majority of pixels in the image. We advance computational models for peripheral vision aimed toward their eventual use in computer graphics. In particular, researchers have recently developed high-performing models of peripheral crowding, known as “pooling” models, which predict a wide range of phenomena but are computationally inefficient. We reformulate the problem as a dataflow computation, which enables faster processing and operating on larger images. Further, we account for the explicit encoding of “end stopped” features in the image, which was missing from previous methods. We evaluate our model in the context of perception of textures in the periphery, including a novel texture dataset and updated textural descriptors. Our improved computational framework may simplify development and testing of more sophisticated, complete models in more robust and realistic settings relevant to computer graphics.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
