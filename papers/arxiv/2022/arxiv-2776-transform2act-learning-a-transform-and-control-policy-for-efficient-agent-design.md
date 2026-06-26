---
id: "arxiv-2776"
title: "Transform2Act: Learning a Transform-and-Control Policy for Efficient Agent Design"
conference: "arXiv 2022"
date: "2022-04"
authors:
  - name: "Ye Yuan"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Yuda Song"
    affiliation: "Carnegie Mellon University"
    is_industry: false
  - name: "Zhengyi Luo"
    affiliation: "Carnegie Mellon University"
    is_industry: false
  - name: "Wen Sun"
    affiliation: "Cornell University"
    is_industry: false
  - name: "Kris Kitani"
    affiliation: "Carnegie Mellon University"
    is_industry: false
topics:
  - AI & Machine Learning
  - Robotics_autonomous
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Artificial Intelligence and Machine Learning"
  - "Robotics"
abstract: "An agent's functionality is largely determined by its design, i.e., skeletal structure and joint attributes (e.g., length, size, strength). However, finding the optimal agent design for a given function is extremely challenging since the problem is inherently combinatorial and the design space is pr"
url: "https://research.nvidia.com/publication/2022-04_transform2act-learning-transform-and-control-policy-efficient-agent-design"
status: "new"
---

# Transform2Act: Learning a Transform-and-Control Policy for Efficient Agent Design

## 摘要

An agent's functionality is largely determined by its design, i.e., skeletal structure and joint attributes (e.g., length, size, strength). However, finding the optimal agent design for a given function is extremely challenging since the problem is inherently combinatorial and the design space is prohibitively large. Additionally, it can be costly to evaluate each candidate design which requires solving for its optimal controller. To tackle these problems, our key idea is to incorporate the design procedure of an agent into its decision-making process. Specifically, we learn a conditional policy that, in an episode, first applies a sequence of transform actions to modify an agent's skeletal structure and joint attributes, and then applies control actions under the new design. To handle a variable number of joints across designs, we use a graph-based policy where each graph node represents a joint and uses message passing with its neighbors to output joint-specific actions. Using policy gradient methods, our approach enables joint optimization of agent design and control as well as experience sharing across different designs, which improves sample efficiency substantially. Experiments show that our approach, Transform2Act, outperforms prior methods significantly in terms of convergence speed and final performance. Notably, Transform2Act can automatically discover plausible designs similar to giraffes, squids, and spiders.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
