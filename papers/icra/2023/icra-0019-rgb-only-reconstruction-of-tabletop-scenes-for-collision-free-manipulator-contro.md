---
id: "icra-0019"
title: "RGB-Only Reconstruction of Tabletop Scenes for Collision-Free Manipulator Control"
conference: "ICRA 2023"
date: "2023-05"
authors:
  - name: "Zhenggang Tang"
    affiliation: "Univ of Illinois"
    is_industry: false
  - name: "Balakumar Sundaralingam"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Jonathan Tremblay"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Bowen Wen"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Ye Yuan"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Stephen Tyree"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Charles Loop"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Alexander Schwing"
    affiliation: "Univ of Illinois"
    is_industry: false
  - name: "Stan Birchfield"
    affiliation: "NVIDIA"
    is_industry: true
topics:
  - Computer Vision
  - Robotics_autonomous
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Computer Vision"
  - "Robotics"
external_links:
  - name: "project page"
    url: "https://ngp-mpc.github.io/"
abstract: "We present a system for collision-free control of a robot manipulator that uses only RGB views of the world. Perceptual input of a tabletop scene is provided by multiple images of an RGB camera (without depth) that is either handheld or mounted on the robot end effector. A NeRF-like process is used "
url: "https://research.nvidia.com/publication/2023-05_rgb-only-reconstruction-tabletop-scenes-collision-free-manipulator-control"
status: "new"
---

# RGB-Only Reconstruction of Tabletop Scenes for Collision-Free Manipulator Control

## 摘要

We present a system for collision-free control of a robot manipulator that uses only RGB views of the world. Perceptual input of a tabletop scene is provided by multiple images of an RGB camera (without depth) that is either handheld or mounted on the robot end effector. A NeRF-like process is used to reconstruct the 3D geometry of the scene, from which the Euclidean full signed distance function (ESDF) is computed. A model predictive control algorithm is then used to control the manipulator to reach a desired pose while avoiding obstacles in the ESDF. We show results on a real dataset collected and annotated in our lab.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
