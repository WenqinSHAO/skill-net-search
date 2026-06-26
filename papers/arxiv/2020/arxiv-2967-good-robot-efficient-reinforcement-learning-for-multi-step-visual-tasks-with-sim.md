---
id: "arxiv-2967"
title: "“Good Robot!”: Efficient Reinforcement Learning for Multi-Step Visual Tasks with Sim to Real Transfer"
conference: "arXiv 2020"
date: "2020-10"
authors:
  - name: "Andrew Hundt"
    affiliation: "JHU"
    is_industry: false
  - name: "Benjamin Killeen"
    affiliation: "JHU"
    is_industry: false
  - name: "Nicholas Greene"
    affiliation: "JHU"
    is_industry: false
  - name: "Hongtao Wu"
    affiliation: "JHU"
    is_industry: false
  - name: "Heeyeon Kwon"
    affiliation: "JHU"
    is_industry: false
  - name: "Chris Paxton"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Gregory D Hager"
    affiliation: "JHU"
    is_industry: false
topics:
  - Robotics_autonomous
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Robotics"
abstract: "Current Reinforcement Learning (RL) algorithms struggle with long-horizon tasks where time can be wasted exploring dead ends and task progress may be easily reversed. We develop the SPOT framework, which explores within action safety zones, learns about unsafe regions without exploring them, and pri"
url: "https://research.nvidia.com/publication/2020-10_good-robot-efficient-reinforcement-learning-multi-step-visual-tasks-sim-real"
status: "new"
---

# “Good Robot!”: Efficient Reinforcement Learning for Multi-Step Visual Tasks with Sim to Real Transfer

## 摘要

Current Reinforcement Learning (RL) algorithms struggle with long-horizon tasks where time can be wasted exploring dead ends and task progress may be easily reversed. We develop the SPOT framework, which explores within action safety zones, learns about unsafe regions without exploring them, and prioritizes experiences that reverse earlier progress to learn with remarkable efficiency. The SPOT framework successfully completes simulated trials of a variety of tasks, improving a baseline trial success rate from 13% to 100% when stacking 4 cubes, from 13% to 99% when creating rows of 4 cubes, and from 84% to 95% when clearing toys arranged in adversarial patterns. Efficiency with respect to actions per trial typically improves by 30% or more, while training takes just 1-20 k actions, depending on the task. Furthermore, we demonstrate direct sim to real transfer. We are able to create real stacks in 100% of trials with 61% efficiency and real rows in 100% of trials with 59% efficiency by directly loading the simulation-trained model on the real robot with no additional real-world fine-tuning. To our knowledge, this is the first instance of reinforcement learning with successful sim to real transfer applied to long term multi-step tasks such as block-stacking and row-making with consideration of progress reversal. Code is available at https://github.com/jhulcsr/good_robot.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
