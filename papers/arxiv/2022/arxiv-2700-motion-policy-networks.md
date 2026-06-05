---
id: arxiv-2700
title: "Motion Policy Networks"
conference: arXiv 2022
date: 2022-12
authors:
  - name: "Adithya Murali"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Adam Fishman"
    affiliation: ""
    is_industry: false
  - name: "Clemens Eppner"
    affiliation: ""
    is_industry: false
  - name: "Bryan Peele"
    affiliation: ""
    is_industry: false
  - name: "Byron Boots"
    affiliation: ""
    is_industry: false
  - name: "Dieter Fox"
    affiliation: ""
    is_industry: false
topics:
  - AI & Machine Learning
  - Computer Vision
  - Robotics_autonomous
  - AI & Machine Learning
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Artificial Intelligence and Machine Learning"
  - "Computer Vision"
  - "Robotics"
external_links:
  - name: "Project Website"
    url: "https://mpinets.github.io/"
  - name: "Code"
    url: "https://github.com/NVlabs/motion-policy-networks"
abstract: "Collision-free motion generation in unknown environments is a core building block for robot manipulation. Generating such motions is challenging due to multiple objectives; not only should the solutions be optimal, the motion generator itself must be fast enough for real-time performance and reliabl"
url: "https://research.nvidia.com/publication/2022-12_motion-policy-networks"
status: new
---

# Motion Policy Networks

## 摘要

Collision-free motion generation in unknown environments is a core building block for robot manipulation. Generating such motions is challenging due to multiple objectives; not only should the solutions be optimal, the motion generator itself must be fast enough for real-time performance and reliable enough for practical deployment. A wide variety of methods have been proposed ranging from local controllers to global planners, often being combined to offset their shortcomings. We present an end-to-end neural model called Motion Policy Networks (MπNets) to generate collision-free, smooth motion from just a single depth camera observation. MπNets are trained on over 3 million motion planning problems in over 500,000 environments. Our experiments show that MπNets are significantly faster than global planners while exhibiting the reactivity needed to deal with dynamic scenes. They are&nbsp;46%&nbsp;better than prior neural planners and more robust than local control policies. Despite being only trained in simulation, MπNets transfer well to the real robot with noisy partial point clouds.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
