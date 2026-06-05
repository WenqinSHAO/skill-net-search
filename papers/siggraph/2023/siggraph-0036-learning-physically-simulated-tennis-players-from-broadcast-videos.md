---
id: siggraph-0036
title: "Learning Physically Simulated Tennis Players from Broadcast Videos"
conference: SIGGRAPH 2023
date: 2023-08
authors:
  - name: "Ye Yuan"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Haotian Zhang"
    affiliation: ""
    is_industry: false
  - name: "Viktor Makoviychuk"
    affiliation: ""
    is_industry: false
  - name: "Yunrong Guo"
    affiliation: ""
    is_industry: false
  - name: "Sanja Fidler"
    affiliation: ""
    is_industry: false
  - name: "Jason Peng"
    affiliation: ""
    is_industry: false
  - name: "Kayvon Fatahalian"
    affiliation: ""
    is_industry: false
topics:
  - AI & Machine Learning
  - Computer Vision
  - Graphics_rendering
  - AI & Machine Learning
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Artificial Intelligence and Machine Learning"
  - "Computer Graphics"
  - "Computer Vision"
external_links:
  - name: "Project Page"
    url: "https://research.nvidia.com/labs/toronto-ai/vid2player3d/"
abstract: "Motion capture (mocap) data has been the most popular data source for computer animation techniques that combine deep reinforcement learning and motion imitation to produce lifelike motions and perform diverse skills. However, mocap data for specialized skills can be costly to acquire at scale while"
url: "https://research.nvidia.com/publication/2023-08_learning-physically-simulated-tennis-players-broadcast-videos"
status: new
---

# Learning Physically Simulated Tennis Players from Broadcast Videos

## 摘要

Motion capture (mocap) data has been the most popular data source for computer animation techniques that combine deep reinforcement learning and motion imitation to produce lifelike motions and perform diverse skills. However, mocap data for specialized skills can be costly to acquire at scale while there exists an enormous corpus of athletic motion data in the form of video recordings. In this paper, we present a system to learn diverse and complex tennis skills leveraging large-scale but lower-quality motions harvested from broadcast videos, for physically simulated characters to play tennis rallies. Our video imitation system is built upon hierarchical models, combining a low-level imitation policy and a high-level motion planning policy to steer the character in a motion space learned from large video datasets, so that complex skills such as hitting tennis balls with different types of shots and spins can be learned using only simple rewards and without explicit annotations of the action types. Specifically, we address the low-quality demonstrations by correcting the estimated motion with physics-based imitation. The corrected motion is then used to construct a motion embedding that can produce diverse human-like tennis motions. Besides, we also propose an important hybrid control method that combines imperfect motion (e.g. inaccurate wrist motion) from the motion embedding with joint correction predicted by the high-level policy to accomplish the task better. Our system produces controllers for physically-simulated tennis players that can hit the incoming ball to target positions accurately using diverse skills, such as serves, forehands and backhands, topspins and slices. Notably, our system can synthesize novel animation of extended tennis rallies between two simulated characters with different playing styles.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
