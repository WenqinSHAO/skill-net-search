---
id: arxiv-2927
title: "Acting in Delayed Environments with Non-Stationary Markov Policies"
conference: arXiv 2021
date: 2021-01
authors:
  - name: "Gal Dalal"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Shie Mannor"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Esther Derman"
    affiliation: ""
    is_industry: false
topics:
  - AI & Machine Learning
  - AI & Machine Learning
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Artificial Intelligence and Machine Learning"
abstract: "The standard Markov Decision Process (MDP) formulation hinges on the assumption that an action is executed immediately after it was chosen. However, assuming it is often unrealistic and can lead to catastrophic failures in applications such as robotic manipulation, cloud computing, and finance. We i"
url: "https://research.nvidia.com/publication/2021-01_acting-delayed-environments-non-stationary-markov-policies"
status: new
---

# Acting in Delayed Environments with Non-Stationary Markov Policies

## 摘要

The standard Markov Decision Process (MDP) formulation hinges on the assumption that an action is executed immediately after it was chosen. However, assuming it is often unrealistic and can lead to catastrophic failures in applications such as robotic manipulation, cloud computing, and finance. We introduce a framework for learning and planning in MDPs where the decision-maker commits actions that are executed with a delay of m steps. The brute-force state augmentation baseline where the state is concatenated to the last m committed actions suffers from an exponential complexity in m, as we show for policy iteration. We then prove that with execution delay, Markov policies in the original state-space are sufficient for attaining maximal reward, but need to be non-stationary. As for stationary Markov policies, we show they are sub-optimal in general. Consequently, we devise a non-stationary Q-learning style model-based algorithm that solves delayed execution tasks without resorting to state-augmentation. Experiments on tabular, physical, and Atari domains reveal that it converges quickly to high performance even for substantial delays, while standard approaches that either ignore the delay or rely on state-augmentation struggle or fail due to divergence.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
