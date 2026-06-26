---
id: "cvpr-0018"
title: "Outdoor Scene Extrapolation with Hierarchical Generative Cellular Automata"
conference: "CVPR 2024"
date: "2024-06"
authors:
  - name: "Dongsu Zhang"
    affiliation: "Seoul National University"
    is_industry: false
  - name: "Francis Williams"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Zan Gojcic"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Karsten Kreis"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Sanja Fidler"
    affiliation: "NVIDIA, Vector Institute, University of Toronto"
    is_industry: true
  - name: "Young Min Kim"
    affiliation: "Seoul National University"
    is_industry: false
  - name: "Amlan Kar"
    affiliation: "NVIDIA, Vector Institute, University of Toronto"
    is_industry: true
topics:
  - AI & Machine Learning
  - Computer Vision
  - Foundation_models
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Artificial Intelligence and Machine Learning"
  - "Computer Vision"
  - "Generative AI"
external_links:
  - name: "Project Website"
    url: "https://research.nvidia.com/labs/toronto-ai/hGCA/"
abstract: "We aim to generate fine-grained 3D geometry from large-scale sparse LiDAR scans, abundantly captured by autonomous vehicles (AV). Contrary to prior work on AV scene completion, we aim to extrapolate fine geometry from unlabeled and beyond spatial limits of LiDAR scans, taking a step towards generati"
url: "https://research.nvidia.com/publication/2024-06_outdoor-scene-extrapolation-hierarchical-generative-cellular-automata"
status: "new"
---

# Outdoor Scene Extrapolation with Hierarchical Generative Cellular Automata

## 摘要

We aim to generate fine-grained 3D geometry from large-scale sparse LiDAR scans, abundantly captured by autonomous vehicles (AV). Contrary to prior work on AV scene completion, we aim to extrapolate fine geometry from unlabeled and beyond spatial limits of LiDAR scans, taking a step towards generating realistic, high-resolution simulation-ready 3D street environments. We propose hierarchical Generative Cellular Automata (hGCA), a spatially scalable conditional 3D generative model, which grows geometry recursively with local kernels following, in a coarse-to-fine manner, equipped with a light-weight planner to induce global consistency. Experiments on synthetic scenes show that hGCA generates plausible scene geometry with higher fidelity and completeness compared to state-of-the-art baselines. Our model generalizes strongly from sim-to-real, qualitatively outperforming baselines on the Waymo-open dataset. We also show anecdotal evidence of the ability to create novel objects from real-world geometric cues even when trained on limited synthetic content.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
