---
id: "arxiv-2755"
title: "ScePT: Scene-consistent, Policy-based Trajectory Predictions for Planning"
conference: "arXiv 2022"
date: "2022-06"
authors:
  - name: "Yuxiao Chen"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Boris Ivanovic"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Marco Pavone"
    affiliation: "NVIDIA"
    is_industry: true
topics:
  - AI & Machine Learning
  - Computer Vision
  - Robotics_autonomous
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Artificial Intelligence and Machine Learning"
  - "Autonomous Vehicles"
  - "Computer Vision"
external_links:
  - name: "Paper"
    url: "https://openaccess.thecvf.com/content/CVPR2022/html/Chen_ScePT_Scene-Consistent_Policy-Based_Trajectory_Predictions_for_Planning_CVPR_2022_paper.html"
  - name: "Code"
    url: "https://github.com/NVlabs/ScePT"
abstract: "Trajectory prediction is a critical functionality of autonomous systems that share environments with uncontrolled agents, one prominent example being self-driving vehicles. Currently, most prediction methods do not enforce scene consistency, i.e., there are a substantial amount of self-collisions be"
url: "https://research.nvidia.com/publication/2022-06_scept-scene-consistent-policy-based-trajectory-predictions-planning"
status: "new"
---

# ScePT: Scene-consistent, Policy-based Trajectory Predictions for Planning

## 摘要

Trajectory prediction is a critical functionality of autonomous systems that share environments with uncontrolled agents, one prominent example being self-driving vehicles. Currently, most prediction methods do not enforce scene consistency, i.e., there are a substantial amount of self-collisions between predicted trajectories of different agents in the scene. Moreover, many approaches generate individual trajectory predictions per agent instead of joint trajectory predictions of the whole scene, which makes downstream planning difficult. In this work, we present ScePT, a policy planning-based trajectory prediction model that generates accurate, scene-consistent trajectory predictions suitable for autonomous system motion planning. It explicitly enforces scene consistency and learns an agent interaction policy that can be used for conditional prediction. Experiments on multiple real-world pedestrians and autonomous vehicle datasets show that ScePT matches current state-of-the-art prediction accuracy with significantly improved scene consistency. We also demonstrate ScePT’s ability to work with a downstream contingency planner.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
