---
id: "icml-0015"
title: "Bayesian Reparameterization of Reward-Conditioned Reinforcement Learning with Energy-based Models"
conference: "ICML 2023"
date: "2023-05"
authors:
  - name: "Wenhao Ding"
    affiliation: "Carnegie Mellon University"
    is_industry: false
  - name: "Tong Che"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Ding Zhao"
    affiliation: "Carnegie Mellon University"
    is_industry: false
  - name: "Marco Pavone"
    affiliation: "NVIDIA"
    is_industry: true
topics:
  - Robotics_autonomous
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Autonomous Vehicles"
abstract: "Recently, reward-conditioned reinforcement learning (RCRL) has gained popularity due to its simplicity, flexibility, and off-policy nature. However, we will show that current RCRL approaches are fundamentally limited and fail to address two critical challenges of RCRL -- improving generalization on "
url: "https://research.nvidia.com/publication/2023-05_bayesian-reparameterization-reward-conditioned-reinforcement-learning-energy"
status: "new"
---

# Bayesian Reparameterization of Reward-Conditioned Reinforcement Learning with Energy-based Models

## 摘要

Recently, reward-conditioned reinforcement learning (RCRL) has gained popularity due to its simplicity, flexibility, and off-policy nature. However, we will show that current RCRL approaches are fundamentally limited and fail to address two critical challenges of RCRL -- improving generalization on high reward-to-go (RTG) inputs, and avoiding out-of-distribution (OOD) RTG queries during testing time. To address these challenges when training vanilla RCRL architectures, we propose Bayesian Reparameterized RCRL (BR-RCRL), a novel set of inductive biases for RCRL inspired by Bayes' theorem. BR-RCRL removes a core obstacle preventing vanilla RCRL from generalizing on high RTG inputs -- a tendency that the model treats different RTG inputs as independent values, which we term ``RTG Independence". BR-RCRL also allows us to design an accompanying adaptive inference method, which maximizes total returns while avoiding OOD queries that yield unpredictable behaviors in vanilla RCRL methods. We show that BR-RCRL achieves state-of-the-art performance on the Gym-Mujoco and Atari offline RL benchmarks, improving upon vanilla RCRL by up to 11%.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
