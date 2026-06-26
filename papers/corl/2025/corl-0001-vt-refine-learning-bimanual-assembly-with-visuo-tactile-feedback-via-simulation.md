---
id: "corl-0001"
title: "VT-Refine: Learning Bimanual Assembly with Visuo-Tactile Feedback via Simulation Fine-Tuning"
conference: "CoRL 2025"
date: "2025-09"
authors:
  - name: "Binghao Huang"
    affiliation: "Columbia"
    is_industry: false
  - name: "Jie Xu"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Iretiayo Akinola"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Wei Yang"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Balakumar Sundaralingam"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Rowland O'Flaherty"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Dieter Fox"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Xiaolong Wang"
    affiliation: "NVIDIA, UCSD"
    is_industry: true
  - name: "Arsalan Mousavian"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Yu-Wei Chao"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Yunzhu Li"
    affiliation: "Columbia"
    is_industry: false
  - name: "Rowland O&#039;Flaherty"
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
  - name: "Paper, Video, Code"
    url: "https://binghao-huang.github.io/vt_refine"
abstract: "Humans excel at bimanual assembly tasks by adapting to rich tactile feedback—a capability that remains difficult to replicate in robots through behavioral cloning alone, due to the suboptimality and limited diversity of human demonstrations. In this work, we present VT-Refine, a visuo-tactile policy"
url: "https://research.nvidia.com/publication/2025-09_vt-refine-learning-bimanual-assembly-visuo-tactile-feedback-simulation-fine"
status: "new"
---

# VT-Refine: Learning Bimanual Assembly with Visuo-Tactile Feedback via Simulation Fine-Tuning

## 摘要

Humans excel at bimanual assembly tasks by adapting to rich tactile feedback—a capability that remains difficult to replicate in robots through behavioral cloning alone, due to the suboptimality and limited diversity of human demonstrations. In this work, we present VT-Refine, a visuo-tactile policy learning framework that combines real-world demonstrations, high-fidelity tactile simulation, and reinforcement learning to tackle precise, contact-rich bimanual assembly. We begin by training a diffusion policy on a small set of demonstrations using synchronized visual and tactile inputs. This policy is then transferred to a simulated digital twin equipped with simulated tactile sensors and further refined via largescale reinforcement learning to enhance robustness and generalization. To enable accurate sim-to-real transfer, we leverage high-resolution piezoresistive tactile sensors that provide normal force signals and can be realistically modeled in parallel using GPU-accelerated simulation. Experimental results show that VT-Refine improves assembly performance in both simulation and the real world by increasing data diversity and enabling more effective policy fine-tuning. Our project page is available at https://binghao-huang.github.io/vt_refine/.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
