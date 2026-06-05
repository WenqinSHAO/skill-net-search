---
id: neurips-0018
title: "Diffusion-Reward Adversarial Imitation Learning"
conference: NeurIPS 2024
date: 2024-12
authors:
  - name: "Frank Wang"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Min-Hung Chen"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Chun-Mao Lai"
    affiliation: ""
    is_industry: false
  - name: "Hsiang-Chun Wang"
    affiliation: ""
    is_industry: false
  - name: "Ping-Chun Hsieh"
    affiliation: ""
    is_industry: false
  - name: "Shao-Hua Sun"
    affiliation: ""
    is_industry: false
topics:
  - AI & Machine Learning
  - Foundation_models
  - Robotics_autonomous
  - AI & Machine Learning
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Artificial Intelligence and Machine Learning"
  - "Generative AI"
  - "Robotics"
external_links:
  - name: "Project Website"
    url: "https://nturobotlearninglab.github.io/DRAIL/"
  - name: "arXiv"
    url: "https://arxiv.org/abs/2405.16194"
  - name: "Code"
    url: "https://github.com/NVlabs/DRAIL"
abstract: "Imitation learning aims to learn a policy from observing expert demonstrations without access to reward signals from environments. Generative adversarial imitation learning (GAIL) formulates imitation learning as adversarial learning, employing a generator policy learning to imitate expert behaviors"
url: "https://research.nvidia.com/publication/2024-12_diffusion-reward-adversarial-imitation-learning"
status: new
---

# Diffusion-Reward Adversarial Imitation Learning

## 摘要

Imitation learning aims to learn a policy from observing expert demonstrations without access to reward signals from environments. Generative adversarial imitation learning (GAIL) formulates imitation learning as adversarial learning, employing a generator policy learning to imitate expert behaviors and discriminator learning to distinguish the expert demonstrations from agent trajectories. Despite its encouraging results, GAIL training is often brittle and unstable. Inspired by the recent dominance of diffusion models in generative modeling, this work proposes Diffusion-Reward Adversarial Imitation Learning (DRAIL), which integrates a diffusion model into GAIL, aiming to yield more precise and smoother rewards for policy learning. Specifically, we propose a diffusion discriminative classifier to construct an enhanced discriminator; then, we design diffusion rewards based on the classifier's output for policy learning. We conduct extensive experiments in navigation, manipulation, and locomotion, verifying DRAIL's effectiveness compared to prior imitation learning methods. Moreover, additional experimental results demonstrate the generalizability and data efficiency of DRAIL. Visualized learned reward functions of GAIL and DRAIL suggest that DRAIL can produce more precise and smoother rewards. Code available at this https URL.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
