---
id: siggraph-0064
title: "AdaptiBrush: Adaptive General and Predictable VR Ribbon Brush"
conference: SIGGRAPH 2021
date: 2021-12
authors:
  - name: "Nicholas Vining"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Enrique Rosales"
    affiliation: ""
    is_industry: false
  - name: "Chrystiano Araujo"
    affiliation: ""
    is_industry: false
  - name: "Jafet Rodriguez"
    affiliation: ""
    is_industry: false
  - name: "Dongwook Yoon"
    affiliation: ""
    is_industry: false
  - name: "Alla Sheffer"
    affiliation: ""
    is_industry: false
topics:
  - Applied_perception
  - Graphics_rendering
  - AI & Machine Learning
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Computer Graphics"
  - "Human Computer Interaction"
  - "VR, AR and Display Technology"
external_links:
  - name: "Project Webpage"
    url: "https://www.cs.ubc.ca/labs/imager/tr/2021/AdaptiBrush/"
abstract: "Virtual reality drawing applications let users draw 3D shapes using brushes that form&nbsp;ribbon&nbsp;shaped, or ruled-surface, strokes. Each ribbon is uniquely defined by its user-specified ruling length, path, and the ruling directions at each point along this path. Existing brushes use the traje"
url: "https://research.nvidia.com/publication/2021-12_adaptibrush-adaptive-general-and-predictable-vr-ribbon-brush"
status: new
---

# AdaptiBrush: Adaptive General and Predictable VR Ribbon Brush

## 摘要

Virtual reality drawing applications let users draw 3D shapes using brushes that form&nbsp;ribbon&nbsp;shaped, or ruled-surface, strokes. Each ribbon is uniquely defined by its user-specified ruling length, path, and the ruling directions at each point along this path. Existing brushes use the trajectory of a handheld controller in 3D space as the ribbon path, and compute the ruling directions using a&nbsp;fixed&nbsp;mapping from a specific controller coordinate-frame axis. This fixed mapping forces users to rotate the controller and thus their wrists to change ribbon normal or ruling directions, and requires substantial physical effort to draw even medium complexity ribbons. Since human ability to rotate their wrists continuously is heavily restricted, the space of ribbon geometries users can comfortably draw using these brushes is limited. These brushes can be unpredictable, producing ribbons with unexpectedly varying width or flipped and wobbly normals in response to seemingly natural hand gestures. Our&nbsp;AdaptiBrush&nbsp;ribbon brush system dramatically extends the space of ribbon geometries users can comfortably draw while enabling them to accurately predict the ribbon shape that a given hand motion produces. We achieve this by introducing a novel&nbsp;adaptive&nbsp;ruling direction computation method, enabling users to easily change ribbon ruling and normal orientation using predominantly translational controller, and thus wrist, motion. We facilitate ease-of-use by computing predictable ruling directions that smoothly change in both world and controller coordinate systems, and facilitate ease-of-learning by prioritizing ruling directions which are well-aligned with one of the controller coordinate system axes. Our comparative user studies confirm that our more general and predictable ruling computation leads to significant improvements in brush usability and effectiveness compared to all prior brushes; in a head to head comparison users preferred AdaptiBrush over the next-best brush by a margin of 2 to 1.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
