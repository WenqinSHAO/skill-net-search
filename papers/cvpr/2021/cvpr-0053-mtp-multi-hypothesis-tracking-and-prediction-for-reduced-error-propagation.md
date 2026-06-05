---
id: cvpr-0053
title: "MTP: Multi-Hypothesis Tracking and Prediction for Reduced Error Propagation"
conference: CVPR 2021
date: 2021-10
authors:
  - name: "Boris Ivanovic"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Marco Pavone"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Xinshuo Weng"
    affiliation: ""
    is_industry: false
topics:
  - Computer Vision
  - Robotics_autonomous
  - AI & Machine Learning
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Autonomous Vehicles"
  - "Computer Vision"
external_links:
  - name: "Paper"
    url: "https://arxiv.org/abs/2110.09481"
abstract: "Recently, there has been tremendous progress in developing each individual module of the standard perception-planning robot autonomy pipeline, including detection, tracking, prediction of other agents' trajectories, and ego-agent trajectory planning. Nevertheless, there has been less attention given"
url: "https://research.nvidia.com/publication/2021-10_mtp-multi-hypothesis-tracking-and-prediction-reduced-error-propagation"
status: new
---

# MTP: Multi-Hypothesis Tracking and Prediction for Reduced Error Propagation

## 摘要

Recently, there has been tremendous progress in developing each individual module of the standard perception-planning robot autonomy pipeline, including detection, tracking, prediction of other agents' trajectories, and ego-agent trajectory planning. Nevertheless, there has been less attention given to the principled integration of these components, particularly in terms of the characterization and mitigation of cascading errors. This paper addresses the problem of cascading errors by focusing on the coupling between the tracking and prediction modules. First, by using state-of-the-art tracking and prediction tools, we conduct a comprehensive experimental evaluation of how severely errors stemming from tracking can impact prediction performance. On the KITTI and nuScenes datasets, we find that predictions consuming tracked trajectories as inputs (the typical case in practice) can experience a significant (even order of magnitude) drop in performance in comparison to the idealized setting where ground truth past trajectories are used as inputs. To address this issue, we propose a multi-hypothesis tracking and prediction framework. Rather than relying on a single set of tracking results for prediction, our framework simultaneously reasons about multiple sets of tracking results, thereby increasing the likelihood of including accurate tracking results as inputs to prediction. We show that this framework improves overall prediction performance over the standard single-hypothesis tracking-prediction pipeline by up to 34.2% on the nuScenes dataset, with even more significant improvements (up to ~70%) when restricting the evaluation to challenging scenarios involving identity switches and fragments -- all with an acceptable computation overhead.&nbsp;

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
