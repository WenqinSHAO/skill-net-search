---
id: "neurips-0026"
title: "PAC-Bayes Generalization Certificates for Learned Inductive Conformal Prediction"
conference: "NeurIPS 2023"
date: "2023-12"
authors:
  - name: "Apoorva Sharma"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Sushant Veer"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Asher Hancock"
    affiliation: "Princeton University"
    is_industry: false
  - name: "Heng Yang"
    affiliation: "Harvard University & NVIDIA"
    is_industry: true
  - name: "Marco Pavone"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Anirudha Majumdar"
    affiliation: "Princeton University"
    is_industry: false
topics:
  - Robotics_autonomous
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Autonomous Vehicles"
abstract: "Inductive Conformal Prediction (ICP) provides a practical and effective approach for equipping deep learning models with uncertainty estimates in the form of set-valued predictions which are guaranteed to contain the ground truth with high probability. Despite the appeal of this coverage guarantee, "
url: "https://research.nvidia.com/publication/2023-12_pac-bayes-generalization-certificates-learned-inductive-conformal-prediction"
status: "new"
---

# PAC-Bayes Generalization Certificates for Learned Inductive Conformal Prediction

## 摘要

Inductive Conformal Prediction (ICP) provides a practical and effective approach for equipping deep learning models with uncertainty estimates in the form of set-valued predictions which are guaranteed to contain the ground truth with high probability. Despite the appeal of this coverage guarantee, these sets may not be efficient: the size and contents of the prediction sets are not directly controlled, and instead depend on the underlying model and choice of score function. To remedy this, recent work has proposed learning model and score function parameters using data to directly optimize the efficiency of the ICP prediction sets. While appealing, the generalization theory for such an approach is lacking: direct optimization of empirical efficiency may yield prediction sets that are either no longer efficient on test data, or no longer obtain the required coverage on test data. In this work, we use PAC-Bayes theory to obtain generalization bounds on both the coverage and the efficiency of set-valued predictors which can be directly optimized to maximize efficiency while satisfying a desired test coverage. In contrast to prior work, our framework allows us to utilize the entire calibration dataset to learn the parameters of the model and score function, instead of requiring a separate hold-out set for obtaining test-time coverage guarantees. We leverage these theoretical results to provide a practical algorithm for using calibration data to simultaneously fine-tune the parameters of a model and score function while guaranteeing test-time coverage and efficiency of the resulting prediction sets. We evaluate the approach on regression and classification tasks, and outperform baselines calibrated using a Hoeffding bound-based PAC guarantee on ICP, especially in the low-data regime.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
