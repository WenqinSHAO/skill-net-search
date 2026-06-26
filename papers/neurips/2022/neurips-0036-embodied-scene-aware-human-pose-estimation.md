---
id: "neurips-0036"
title: "Embodied Scene-aware Human Pose Estimation"
conference: "NeurIPS 2022"
date: "2022-11"
authors:
  - name: "Zhengyi Luo"
    affiliation: "Carnegie Mellon University"
    is_industry: false
  - name: "Shun Iwase"
    affiliation: "Carnegie Mellon University"
    is_industry: false
  - name: "Ye Yuan"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Kris Kitani"
    affiliation: "Carnegie Mellon University"
    is_industry: false
topics:
  - Computer Vision
  - Graphics_rendering
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Computer Vision"
  - "VR, AR and Display Technology"
external_links:
  - name: "Paper"
    url: "https://arxiv.org/abs/2206.09106"
  - name: "Video"
    url: "https://www.youtube.com/watch?v=8Ae0xzqAtm8"
  - name: "Code"
    url: "https://github.com/zhengyiluo/EmbodiedPose"
abstract: "We propose embodied scene-aware human pose estimation where we estimate 3D poses based on a simulated agent's proprioception and scene awareness, along with external third-person observations. Unlike prior methods that often resort to multistage optimization, non-causal inference, and complex contac"
url: "https://research.nvidia.com/publication/2022-11_embodied-scene-aware-human-pose-estimation"
status: "new"
---

# Embodied Scene-aware Human Pose Estimation

## 摘要

We propose embodied scene-aware human pose estimation where we estimate 3D poses based on a simulated agent's proprioception and scene awareness, along with external third-person observations. Unlike prior methods that often resort to multistage optimization, non-causal inference, and complex contact modeling to estimate human pose and human scene interactions, our method is one stage, causal, and recovers global 3D human poses in a simulated environment. Since 2D third-person observations are coupled with the camera pose, we propose to disentangle the camera pose and use a multi-step projection gradient defined in the global coordinate frame as the movement cue for our embodied agent. Leveraging a physics simulation and prescanned scenes (e.g., 3D mesh), we simulate our agent in everyday environments (libraries, offices, bedrooms, etc.) and equip our agent with environmental sensors to intelligently navigate and interact with scene geometries. Our method also relies only on 2D keypoints and can be trained on synthetic datasets derived from popular human motion databases. To evaluate, we use the popular H36M and PROX datasets and, for the first time, achieve a success rate of 96.7% on the challenging PROX dataset without ever using PROX motion sequences for training.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
