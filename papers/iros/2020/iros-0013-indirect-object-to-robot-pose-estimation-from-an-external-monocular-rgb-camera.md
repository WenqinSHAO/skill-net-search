---
id: "iros-0013"
title: "Indirect Object-to-Robot Pose Estimation from an External Monocular RGB Camera"
conference: "IROS 2020"
date: "2020-07"
authors:
  - name: "Jonathan Tremblay"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Stephen Tyree"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Terry Mosier"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Stan Birchfield"
    affiliation: "NVIDIA"
    is_industry: true
topics:
  - Computer Vision
  - Robotics_autonomous
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Computer Vision"
  - "Robotics"
external_links:
  - name: "arXiv paper"
    url: "https://arxiv.org/abs/2008.11822"
  - name: "Video"
    url: "https://youtu.be/E0J91llX-ys"
abstract: "We present a robotic grasping system that uses a single external monocular RGB camera as input. The object-to-robot pose is computed indirectly by combining the output of two neural networks:&nbsp; one that estimates the object-to-camera pose, and another that estimates the robot-to-camera pose. Bot"
url: "https://research.nvidia.com/publication/2020-07_indirect-object-robot-pose-estimation-external-monocular-rgb-camera"
status: "new"
---

# Indirect Object-to-Robot Pose Estimation from an External Monocular RGB Camera

## 摘要

We present a robotic grasping system that uses a single external monocular RGB camera as input. The object-to-robot pose is computed indirectly by combining the output of two neural networks:&nbsp; one that estimates the object-to-camera pose, and another that estimates the robot-to-camera pose. Both networks are trained entirely on synthetic data, relying on domain randomization to bridge the sim-to-real gap. Because the latter network performs online camera calibration, the camera can be moved freely during execution without affecting the quality of the grasp. Experimental results analyze the effect of camera placement, image resolution, and pose refinement in the context of grasping several household objects. We also present results on a new set of 28 textured household toy grocery objects, which have been selected to be accessible to other researchers. To aid reproducibility of the research, we offer 3D scanned textured models, along with pre-trained weights for pose estimation.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
