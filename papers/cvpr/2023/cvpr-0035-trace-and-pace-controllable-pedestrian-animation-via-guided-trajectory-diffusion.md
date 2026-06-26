---
id: "cvpr-0035"
title: "Trace and Pace: Controllable Pedestrian Animation via Guided Trajectory Diffusion"
conference: "CVPR 2023"
date: "2023-06"
authors:
  - name: "Davis Rempe"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Zhengyi Luo"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Xue Bin Peng"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Ye Yuan"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Kris Kitani"
    affiliation: "Carnegie Mellon University"
    is_industry: false
  - name: "Karsten Kreis"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Sanja Fidler"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Or Litany"
    affiliation: "NVIDIA"
    is_industry: true
topics:
  - AI & Machine Learning
  - Graphics_rendering
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Artificial Intelligence and Machine Learning"
  - "Computer Graphics"
external_links:
  - name: "Paper"
    url: "https://arxiv.org/abs/2304.01893"
  - name: "Website"
    url: "https://nv-tlabs.github.io/trace-pace/"
  - name: "Demo"
    url: "https://nv-tlabs.github.io/trace-pace/supp.html"
abstract: "We introduce a method for generating realistic pedestrian trajectories and full-body animations that can be controlled to meet user-defined goals. We draw on recent advances in guided diffusion modeling to achieve test-time controllability of trajectories, which is normally only associated with rule"
url: "https://research.nvidia.com/publication/2023-06_trace-and-pace-controllable-pedestrian-animation-guided-trajectory-diffusion"
status: "new"
---

# Trace and Pace: Controllable Pedestrian Animation via Guided Trajectory Diffusion

## 摘要

We introduce a method for generating realistic pedestrian trajectories and full-body animations that can be controlled to meet user-defined goals. We draw on recent advances in guided diffusion modeling to achieve test-time controllability of trajectories, which is normally only associated with rule-based systems. Our guided diffusion model allows users to constrain trajectories through target waypoints, speed, and specified social groups while accounting for the surrounding environment context. This trajectory diffusion model is integrated with a novel physics-based humanoid controller to form a closed-loop, full-body pedestrian animation system capable of placing large crowds in a simulated environment with varying terrains. We further propose utilizing the value function learned during RL training of the animation controller to guide diffusion to produce trajectories better suited for particular scenarios such as collision avoidance and traversing uneven terrain. Video results are available on the project page at&nbsp;this https URL&nbsp;.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
