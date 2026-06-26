---
id: "corl-0002"
title: "Dexplore: Scalable Neural Control for Dexterous Manipulation from Reference-Scoped Exploration"
conference: "CoRL 2025"
date: "2025-09"
authors:
  - name: "Sirui Xu"
    affiliation: "UIUC"
    is_industry: false
  - name: "Yu-Wei Chao"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Liuyu Bian"
    affiliation: "UIUC"
    is_industry: false
  - name: "Arsalan Mousavian"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Yu-Xiong Wang"
    affiliation: "UIUC"
    is_industry: false
  - name: "Liang-Yan Gui"
    affiliation: "UIUC"
    is_industry: false
  - name: "Wei Yang"
    affiliation: "NVIDIA"
    is_industry: true
topics:
  - Robotics_autonomous
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Physical AI"
  - "Robotics"
external_links:
  - name: "Paper, Video"
    url: "https://sirui-xu.github.io/dexplore"
abstract: "Hand-object motion-capture (MoCap) repositories offer large-scale, contact-rich demonstrations and hold promise for scaling dexterous robotic manipulation. Yet demonstration inaccuracies and embodiment gaps between human and robot hands limit the straightforward use of these data. Existing methods a"
url: "https://research.nvidia.com/publication/2025-09_dexplore-scalable-neural-control-dexterous-manipulation-reference-scoped"
status: "new"
---

# Dexplore: Scalable Neural Control for Dexterous Manipulation from Reference-Scoped Exploration

## 摘要

Hand-object motion-capture (MoCap) repositories offer large-scale, contact-rich demonstrations and hold promise for scaling dexterous robotic manipulation. Yet demonstration inaccuracies and embodiment gaps between human and robot hands limit the straightforward use of these data. Existing methods adopt a three-stage workflow, including retargeting, tracking, and residual correction, which often leaves demonstrations underused and compound errors across stages. We introduce Dexplore, a unified single-loop optimization that jointly performs retargeting and tracking to learn robot control policies directly from MoCap at scale. Rather than treating demonstrations as ground truth, we use them as soft guidance. From raw trajectories, we derive adaptive spatial scopes, and train with reinforcement learning to keep the policy in-scope while minimizing control effort and accomplishing the task. This unified formulation preserves demonstration intent, enables robot-specific strategies to emerge, improves robustness to noise, and scales to large demonstration corpora. We distill the scaled tracking policy into a vision-based, skill-conditioned generative controller that encodes diverse manipulation skills in a rich latent representation, supporting generalization across objects and real-world deployment. Taken together, these contributions position Dexplore as a principled bridge that transforms imperfect demonstrations into effective training signals for dexterous manipulation.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
