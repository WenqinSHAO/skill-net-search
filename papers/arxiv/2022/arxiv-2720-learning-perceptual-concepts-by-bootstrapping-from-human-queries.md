---
id: arxiv-2720
title: "Learning Perceptual Concepts by Bootstrapping from Human Queries"
conference: arXiv 2022
date: 2022-10
authors:
  - name: "Wei Yang"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Balakumar Sundaralingam"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Yu-Wei Chao"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Andreea Bobu"
    affiliation: ""
    is_industry: false
  - name: "Chris Paxton"
    affiliation: ""
    is_industry: false
  - name: "Maya Cakmak"
    affiliation: ""
    is_industry: false
  - name: "Dieter Fox"
    affiliation: ""
    is_industry: false
topics:
  - Robotics_autonomous
  - AI & Machine Learning
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Robotics"
external_links:
  - name: "Website"
    url: "https://sites.google.com/nvidia.com/active-concept-learning"
  - name: "Code"
    url: "https://github.com/NVlabs/concept_learning"
  - name: "arXiv"
    url: "https://arxiv.org/abs/2111.05251"
  - name: "Video"
    url: "https://www.youtube.com/watch?v=LszKCwmOle8&amp;feature=youtu.be&amp;ab_channel=AndreeaBobu"
abstract: "Robots need to be able to learn concepts from their users in order to adapt their capabilities to each user’s unique task. But when the robot operates on high-dimensional inputs, like images or point clouds, this is impractical: the robot needs an unrealistic amount of human effort to learn the new "
url: "https://research.nvidia.com/publication/2022-10_learning-perceptual-concepts-bootstrapping-human-queries"
status: new
---

# Learning Perceptual Concepts by Bootstrapping from Human Queries

## 摘要

Robots need to be able to learn concepts from their users in order to adapt their capabilities to each user’s unique task. But when the robot operates on high-dimensional inputs, like images or point clouds, this is impractical: the robot needs an unrealistic amount of human effort to learn the new concept. To address this challenge, we propose a new approach whereby the robot learns a low-dimensional variant of the concept and uses it to generate a larger data set for learning the concept in the high-dimensional space. This lets it take advantage of semantically meaningful privileged information only accessible at training time, like object poses and bounding boxes, that allows for richer human interaction to speed up learning. We evaluate our approach by learning prepositional concepts that describe object state or multi-object relationships, like above, near, or aligned, which are key to user specification of task goals and execution constraints for robots. Using a simulated human, we show that our approach improves sample complexity when compared to learning concepts directly in the high-dimensional space. We also demonstrate the utility of the learned concepts in motion planning tasks on a 7-DoF Franka robot.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
