---
id: "icra-0030"
title: "Camera-to-Robot Pose Estimation from a Single Image"
conference: "ICRA 2020"
date: "2020-05"
authors:
  - name: "Timothy E. Lee"
    affiliation: "NVIDIA, CMU"
    is_industry: true
  - name: "Jonathan Tremblay"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Thang To"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Jia Cheng"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Terry Mosier"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Oliver Kroemer"
    affiliation: "CMU"
    is_industry: false
  - name: "Dieter Fox"
    affiliation: "NVIDIA"
    is_industry: true
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
  - name: "arXiv paper"
    url: "https://arxiv.org/abs/1911.09231"
  - name: "video"
    url: "https://youtu.be/O1qAFboFQ8A"
  - name: "code, datasets, and pretrained models"
    url: "https://github.com/NVlabs/DREAM"
abstract: "We present an approach for estimating the pose of an external camera with respect to a robot using a single RGB image of the robot. The image is processed by a deep neural network to detect 2D projections of keypoints (such as joints) associated with the robot. The network is trained entirely on sim"
url: "https://research.nvidia.com/publication/2020-05_camera-robot-pose-estimation-single-image"
status: "new"
---

# Camera-to-Robot Pose Estimation from a Single Image

## 摘要

We present an approach for estimating the pose of an external camera with respect to a robot using a single RGB image of the robot. The image is processed by a deep neural network to detect 2D projections of keypoints (such as joints) associated with the robot. The network is trained entirely on simulated data using domain randomization to bridge the reality gap. Perspective-n-point (PnP) is then used to recover the camera extrinsics, assuming that the camera intrinsics and joint configuration of the robot manipulator are known. Unlike classic hand-eye calibration systems, our method does not require an off-line calibration step. Rather, it is capable of computing the camera extrinsics from a single frame, thus opening the possibility of on-line calibration. We show experimental results for three different robots and camera sensors, demonstrating that our approach is able to achieve accuracy with a single frame that is comparable to that of classic off-line hand-eye calibration using multiple frames. With additional frames from a static pose, accuracy improves even further. Code, datasets, and pretrained models for three widely-used robot manipulators are made available.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
