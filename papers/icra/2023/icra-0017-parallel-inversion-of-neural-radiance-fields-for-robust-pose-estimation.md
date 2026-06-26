---
id: "icra-0017"
title: "Parallel Inversion of Neural Radiance Fields for Robust Pose Estimation"
conference: "ICRA 2023"
date: "2023-05"
authors:
  - name: "Yunzhi Lin"
    affiliation: "Georgia Institute of Technology"
    is_industry: false
  - name: "Thomas Müller"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Jonathan Tremblay"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Bowen Wen"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Stephen Tyree"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Alex Evans"
    affiliation: "Midjourney"
    is_industry: false
  - name: "Patricio A. Vela"
    affiliation: "Georgia Institute of Technology"
    is_industry: false
  - name: "Stan Birchfield"
    affiliation: "NVIDIA"
    is_industry: true
topics:
  - AI & Machine Learning
  - Computer Vision
  - Robotics_autonomous
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Artificial Intelligence and Machine Learning"
  - "Computer Vision"
  - "Robotics"
external_links:
  - name: "Project page"
    url: "https://pnerfp.github.io/"
  - name: "Video"
    url: "https://www.youtube.com/watch?v=QNsiPk6zqmU"
abstract: "We present a parallelized optimization method based on fast Neural Radiance Fields (NeRF) for estimating 6-DoF target poses. Given a single observed RGB image of the target, we can predict the translation and rotation of the camera by minimizing the residual between pixels rendered from a fastNeRF m"
url: "https://research.nvidia.com/publication/2023-05_parallel-inversion-neural-radiance-fields-robust-pose-estimation"
status: "new"
---

# Parallel Inversion of Neural Radiance Fields for Robust Pose Estimation

## 摘要

We present a parallelized optimization method based on fast Neural Radiance Fields (NeRF) for estimating 6-DoF target poses. Given a single observed RGB image of the target, we can predict the translation and rotation of the camera by minimizing the residual between pixels rendered from a fastNeRF model and pixels in the observed image. We integrate a momentum-based camera extrinsic optimization procedure intoInstant Neural Graphics Primitives, a recent exceptionally fastNeRF implementation. By introducing parallel Monte Carlo sampling into the pose estimation task, our method over comes local minima and improves efficiency in a more extensive search space. We also show the importance of adopting a more robust pixel-based loss function to reduce error. Experiments demonstrate that our method can achieve improved generalization and robustness on both synthetic and real-world benchmarks.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
