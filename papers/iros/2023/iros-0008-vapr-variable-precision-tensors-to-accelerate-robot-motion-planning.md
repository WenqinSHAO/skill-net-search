---
id: "iros-0008"
title: "VaPr: Variable-Precision Tensors to Accelerate Robot Motion Planning"
conference: "IROS 2023"
date: "2023-10"
authors:
  - name: "Yu-Shun Hsiao"
    affiliation: "Harvard University"
    is_industry: false
  - name: "Siva Hari"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Balakumar Sundaralingam"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Jason Yik"
    affiliation: "Harvard University"
    is_industry: false
  - name: "Thierry Tambe"
    affiliation: "Harvard University"
    is_industry: false
  - name: "Charbel Sakr"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Steve Keckler"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Vijay Janapa Reddi"
    affiliation: "Harvard University"
    is_industry: false
topics:
  - GPU_architecture
  - Robotics_autonomous
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Computer Architecture"
  - "Robotics"
abstract: "High-dimensional motion generation requires numerical precision for smooth, collision-free solutions. Typically, double-precision or single-precision floating-point (FP) formats are used for accurate results. Using these for big tensors imposes a strain on the memory bandwidth provided by the device"
url: "https://research.nvidia.com/publication/2023-10_vapr-variable-precision-tensors-accelerate-robot-motion-planning"
status: "new"
---

# VaPr: Variable-Precision Tensors to Accelerate Robot Motion Planning

## 摘要

High-dimensional motion generation requires numerical precision for smooth, collision-free solutions. Typically, double-precision or single-precision floating-point (FP) formats are used for accurate results. Using these for big tensors imposes a strain on the memory bandwidth provided by the devices and alters the memory footprint, hence limiting their applicability to low-power edge devices needed for mobile robots. The uniform application of reduced precision can be advantageous but severely degrades solutions. Using decreased precision data types for important tensors, we propose to accelerate motion generation by removing memory bottlenecks. We propose variable-precision (VaPr) search optimization to determine the appropriate precision for large tensors from a vast search space of approximately 4 million unique combinations for FP data types across the tensors.&nbsp;To obtain the efficiency gains, we exploit existing platform support for an out-of-the-box GPU speedup and evaluate prospective precision converter units for GPU types that are not currently supported.&nbsp;Our experimental results on 800 planning problems for the Franka Panda robot on the MotionBenchmaker dataset across 8 environments show that a 4-bit FP format is sufficient for the largest set of tensors in the motion generation stack.&nbsp;With the software-only solution, VaPr achieves 6.3% speedup on average for a significant portion of motion generation over the SOTA solution (CuRobo) on both Jetson Orin and RTX2080 Ti GPU devices. On these devices, VaPr achieves 9.9% and 17.7% speedups, respectively, with hardware support for FP conversions.&nbsp;

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
