---
id: "arxiv-2946"
title: "Contextual Reinforcement Learning of Visuo-tactile Multi-fingered Grasping Policies"
conference: "arXiv 2020"
date: "2020-11"
authors:
  - name: "Visak Kumar"
    affiliation: "NVIDIA, Georgia Tech"
    is_industry: true
  - name: "Tucker Hermans"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Dieter Fox"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Stan Birchfield"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Jonathan Tremblay"
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
  - name: "arXiv paper"
    url: "https://arxiv.org/abs/1911.09233"
abstract: "Using simulation to train robot manipulation policies holds the promise of an almost unlimited amount of training data, generated safely out of harm's way. One of the key challenges of using simulation, to date, has been to bridge the reality gap, so that policies trained in simulation can be deploy"
url: "https://research.nvidia.com/publication/2020-11_contextual-reinforcement-learning-visuo-tactile-multi-fingered-grasping"
status: "new"
---

# Contextual Reinforcement Learning of Visuo-tactile Multi-fingered Grasping Policies

## 摘要

Using simulation to train robot manipulation policies holds the promise of an almost unlimited amount of training data, generated safely out of harm's way. One of the key challenges of using simulation, to date, has been to bridge the reality gap, so that policies trained in simulation can be deployed in the real world. We explore the reality gap in the context of learning a contextual policy for multi-fingered robotic grasping. We propose a Grasping Objects Approach for Tactile (GOAT) robotic hands, learning to overcome the reality gap problem. In our approach we use human hand motion demonstration to initialize and reduce the search space for learning. We contextualize our policy with the bounding cuboid dimensions of the object of interest, which allows the policy to work on a more flexible representation than directly using an image or point cloud. Leveraging fingertip touch sensors in the hand allows the policy to overcome the reduction in geometric information introduced by the coarse bounding box, as well as pose estimation uncertainty. We show our learned policy successfully runs on a real robot without any fine tuning, thus bridging the reality gap.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
