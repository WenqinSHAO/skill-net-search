---
id: "cvpr-0043"
title: "FreeNeRF: Improving Few-shot Neural Rendering with Free Frequency Regularization"
conference: "CVPR 2023"
date: "2023-03"
authors:
  - name: "Heng Yang"
    affiliation: "NVIDIA"
    is_industry: true
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
abstract: "The two-stage object pose estimation paradigm first detects semantic keypoints on the image and then estimates the 6D pose by minimizing reprojection errors. Despite performing well on standard benchmarks, existing techniques offer no provable guarantees on the quality and uncertainty of the estimat"
url: "https://research.nvidia.com/publication/2023-03_freenerf-improving-few-shot-neural-rendering-free-frequency-regularization"
status: "new"
---

# FreeNeRF: Improving Few-shot Neural Rendering with Free Frequency Regularization

## 摘要

The two-stage object pose estimation paradigm first detects semantic keypoints on the image and then estimates the 6D pose by minimizing reprojection errors. Despite performing well on standard benchmarks, existing techniques offer no provable guarantees on the quality and uncertainty of the estimation. In this paper, we inject two fundamental changes, namely conformal keypoint detection and geometric uncertainty propagation, into the two-stage paradigm and propose the first pose estimator that endows an estimation with provable and computable worst-case error bounds. On one hand, conformal keypoint detection applies the statistical machinery of inductive conformal prediction to convert heuristic keypoint detections into circular or elliptical prediction sets that cover the groundtruth keypoints with a user-specified marginal probability (e.g., 90%). Geometric uncertainty propagation, on the other, propagates the geometric constraints on the keypoints to the 6D object pose, leading to a Pose UnceRtainty SEt (PURSE) that guarantees coverage of the groundtruth pose with the same probability. The PURSE, however, is a nonconvex set that does not directly lead to estimated poses and uncertainties. Therefore, we develop RANdom SAmple averaGing (RANSAG) to compute an average pose and apply semidefinite relaxation to upper bound the worst-case errors between the average pose and the groundtruth. On the LineMOD Occlusion dataset we demonstrate: (i) the PURSE covers the groundtruth with valid probabilities; (ii) the worst-case error bounds provide correct uncertainty quantification; and (iii) the average pose achieves better or similar accuracy as representative methods based on sparse keypoints.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
