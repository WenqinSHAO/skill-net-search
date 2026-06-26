---
id: "arxiv-2900"
title: "Object Rearrangement Using Learned Implicit Collision Functions"
conference: "arXiv 2021"
date: "2021-03"
authors:
  - name: "Michael Danielczuk"
    affiliation: "UC Berkeley"
    is_industry: false
  - name: "Arsalan Mousavian"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Clemens Eppner"
    affiliation: "NVIDIA"
    is_industry: true
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
    url: "https://arxiv.org/pdf/2011.10726.pdf"
  - name: "Video Presentation"
    url: "https://youtu.be/SHC2ODD1QcU"
  - name: "Video"
    url: "https://youtu.be/anXPw7o7Wx8"
  - name: "Code [Coming Soon]"
    url: "https://github.com/NVlabs/scene_collisionnet"
  - name: "Experiment Videos"
    url: "https://sites.google.com/nvidia.com/scenecollisionnet"
abstract: "Robotic object rearrangement combines the skills of picking and placing objects. When object models are unavailable, typical collision-checking models may be unable to predict collisions in partial point clouds with occlusions, making generation of collision-free grasping or placement trajectories c"
url: "https://research.nvidia.com/publication/2021-03_object-rearrangement-using-learned-implicit-collision-functions"
status: "new"
---

# Object Rearrangement Using Learned Implicit Collision Functions

## 摘要

Robotic object rearrangement combines the skills of picking and placing objects. When object models are unavailable, typical collision-checking models may be unable to predict collisions in partial point clouds with occlusions, making generation of collision-free grasping or placement trajectories challenging. We propose a learned collision model that accepts scene and query object point clouds and predicts collisions for 6DOF object poses within the scene. We train the model on a synthetic set of 1 million scene/object point cloud pairs and 2~billion collision queries. We leverage the learned collision model as part of a model predictive path integral (MPPI) policy in a tabletop rearrangement task and show that the policy can plan collision-free grasps and placements for objects unseen in training in both simulated and physical cluttered scenes with a Franka Panda robot. The learned model outperforms both traditional pipelines and learned ablations by 9.8%&nbsp;in accuracy on a dataset of simulated collision queries and is 75x faster than the best-performing baseline.&nbsp;

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
