---
id: iros-0014
title: "MVLidarNet: Real-Time Multi-Class Scene Understanding for Autonomous Driving Using Multiple Views"
conference: IROS 2020
date: 2020-06
authors:
  - name: "Stan Birchfield"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Ke Chen"
    affiliation: ""
    is_industry: false
  - name: "Ryan Oldja"
    affiliation: ""
    is_industry: false
  - name: "Nikolai Smolyanskiy"
    affiliation: ""
    is_industry: false
  - name: "Alexander Popov"
    affiliation: ""
    is_industry: false
  - name: "David Wehr"
    affiliation: ""
    is_industry: false
  - name: "Ibrahim Eden"
    affiliation: ""
    is_industry: false
  - name: "Joachim Pehserl"
    affiliation: ""
    is_industry: false
topics:
  - Applied_perception
  - Computer Vision
  - Robotics_autonomous
  - AI & Machine Learning
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Applied Perception"
  - "Autonomous Vehicles"
  - "Computer Vision"
  - "Robotics"
external_links:
  - name: "arXiv paper"
    url: "https://arxiv.org/abs/2006.05518"
  - name: "video"
    url: "https://youtu.be/2ck5_sToayc"
abstract: "Autonomous driving requires the inference of actionable information such as detecting and classifying objects, and determining the drivable space. To this end, we present Multi-View LidarNet (MVLidarNet), a two-stage deep neural network for multi-class object detection and drivable space segmentatio"
url: "https://research.nvidia.com/publication/2020-06_mvlidarnet-real-time-multi-class-scene-understanding-autonomous-driving-using"
status: new
---

# MVLidarNet: Real-Time Multi-Class Scene Understanding for Autonomous Driving Using Multiple Views

## 摘要

Autonomous driving requires the inference of actionable information such as detecting and classifying objects, and determining the drivable space. To this end, we present Multi-View LidarNet (MVLidarNet), a two-stage deep neural network for multi-class object detection and drivable space segmentation using multiple views of a single LiDAR point cloud. The first stage processes the point cloud projected onto a perspective view in order to semantically segment the scene. The second stage then processes the point cloud (along with semantic labels from the first stage) projected onto a bird's eye view, to detect and classify objects. Both stages use an encoder-decoder architecture. We show that our multi-view, multi-stage, multi-class approach is able to detect and classify objects while simultaneously determining the drivable space using a single LiDAR scan as input, in challenging scenes with more than one hundred vehicles and pedestrians at a time.&nbsp; The system operates efficiently at 150 fps on an embedded GPU designed for a self-driving car, including a postprocessing step to maintain identities over time. We show results on both KITTI and a much larger internal dataset, thus demonstrating the method's ability to scale by an order of magnitude.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
