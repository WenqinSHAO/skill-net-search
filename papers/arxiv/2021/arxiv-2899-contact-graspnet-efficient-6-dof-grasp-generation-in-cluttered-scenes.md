---
id: "arxiv-2899"
title: "Contact-GraspNet:  Efficient  6-DoF  Grasp  Generation in  Cluttered  Scenes"
conference: "arXiv 2021"
date: "2021-03"
authors:
  - name: "Martin Sundermeyer"
    affiliation: "DLR, TUM"
    is_industry: false
  - name: "Arsalan Mousavian"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Rudolph Triebel"
    affiliation: "DLR, TUM"
    is_industry: false
  - name: "Dieter Fox"
    affiliation: "NVIDIA"
    is_industry: true
topics:
  - Robotics_autonomous
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Robotics"
external_links:
  - name: "Paper"
    url: "https://arxiv.org/pdf/2103.14127.pdf"
  - name: "Video"
    url: "https://www.youtube.com/watch?v=qRLKYSLXElM"
abstract: "Grasping unseen objects in unconstrained, cluttered environments is an essential skill for autonomous robotic manipulation.Despite recent progress in full 6-DoF grasp learning, existing approaches often consist of complex sequential pipelines that possess several potential failure points and run-tim"
url: "https://research.nvidia.com/publication/2021-03_contact-graspnet-efficient-6-dof-grasp-generation-cluttered-scenes"
status: "new"
---

# Contact-GraspNet:  Efficient  6-DoF  Grasp  Generation in  Cluttered  Scenes

## 摘要

Grasping unseen objects in unconstrained, cluttered environments is an essential skill for autonomous robotic manipulation.Despite recent progress in full 6-DoF grasp learning, existing approaches often consist of complex sequential pipelines that possess several potential failure points and run-times unsuitable for closed-loop grasping.&nbsp;Therefore, we propose an end-to-end network that efficiently generates a distribution of 6-DoF parallel-jaw grasps directly from a depth recording of a scene.&nbsp;Our novel grasp representation treats 3D points of the recorded point cloud as potential grasp contacts.&nbsp;By rooting the full 6-DoF grasp pose and width in the observed point cloud, we can reduce the dimensionality of our grasp representation to 4-DoF which greatly facilitates the learning process.&nbsp;Our class-agnostic approach is trained on 17 million simulated grasps and generalizes well to real world sensor data. In a robotic grasping study of unseen objects in structured clutter we achieve over 90% success rate, cutting the failure rate in half compared to a recent state-of-the-art method.&nbsp;

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
