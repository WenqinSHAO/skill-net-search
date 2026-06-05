---
id: arxiv-2788
title: "DefGraspSim: Physics-Based Simulation of Grasp Outcomes on 3D Deformable Objects"
conference: arXiv 2022
date: 2022-03
authors:
  - name: "Yashraj Narang"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Balakumar Sundaralingam"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Tucker Hermans"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Isabella Huang"
    affiliation: ""
    is_industry: false
  - name: "Clemens Eppner"
    affiliation: ""
    is_industry: false
  - name: "Miles Macklin"
    affiliation: ""
    is_industry: false
  - name: "Ruzena Bajcsy"
    affiliation: ""
    is_industry: false
  - name: "Dieter Fox"
    affiliation: ""
    is_industry: false
topics:
  - AI & Machine Learning
  - Robotics_autonomous
  - AI & Machine Learning
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Artificial Intelligence and Machine Learning"
  - "Robotics"
external_links:
  - name: "Website"
    url: "https://sites.google.com/nvidia.com/defgraspsim"
abstract: "Robotic grasping of 3D deformable objects (e.g., fruits/vegetables, internal organs, bottles/boxes) is critical for real-world applications such as food processing, robotic surgery, and household automation. However, developing grasp strategies for such objects is uniquely challenging. Unlike rigid "
url: "https://research.nvidia.com/publication/2022-03_defgraspsim-physics-based-simulation-grasp-outcomes-3d-deformable-objects"
status: new
---

# DefGraspSim: Physics-Based Simulation of Grasp Outcomes on 3D Deformable Objects

## 摘要

Robotic grasping of 3D deformable objects (e.g., fruits/vegetables, internal organs, bottles/boxes) is critical for real-world applications such as food processing, robotic surgery, and household automation. However, developing grasp strategies for such objects is uniquely challenging. Unlike rigid objects, deformable objects have infinite degrees of freedom and require field quantities (e.g., deformation, stress) to fully define state. Since these quantities are not easily accessible in the real world, the study of interaction with deformable objects is best informed through physics-based simulation. In this work, we simulate grasps on a wide range of 3D deformable objects using a GPU-based implementation of the corotational finite element method (FEM). To facilitate future research, we open-source our simulated dataset (34 objects, 1e5 Pa elasticity range, 6800 grasp evaluations, 1.1M grasp measurements), as well as a code repository that allows researchers to run our full FEM-based grasp evaluation pipeline on arbitrary 3D object models of their choice. Finally, we demonstrate good correspondence between grasps on simulated objects and their real-world counterparts.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
