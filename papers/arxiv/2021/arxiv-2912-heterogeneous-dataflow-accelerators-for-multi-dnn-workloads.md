---
id: "arxiv-2912"
title: "Heterogeneous Dataflow Accelerators for Multi-DNN Workloads"
conference: "arXiv 2021"
date: "2021-02"
authors:
  - name: "Hyoukjun Kwon"
    affiliation: "Georgia Tech"
    is_industry: false
  - name: "Liangzhen Lai"
    affiliation: "Facebook"
    is_industry: true
  - name: "Michael Pellauer"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Tushar Krishna"
    affiliation: "Georgia Tech"
    is_industry: false
  - name: "Yu-Hsin Chen"
    affiliation: "Facebook"
    is_industry: true
  - name: "Vikas Chandra"
    affiliation: "Facebook"
    is_industry: true
topics:
  - AI & Machine Learning
  - GPU_architecture
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Artificial Intelligence and Machine Learning"
  - "Computer Architecture"
external_links:
  - name: "IEEE Digital Library"
    url: "https://ieeexplore.ieee.org/document/9407116"
abstract: "AI-enabled applications such as augmented and virtual reality (AR/VR) leverage multiple deep neural network (DNN) models for various sub-tasks such as object detection, image segmentation, eye-tracking, speech recognition, and so on. Because of the diversity of the sub-tasks, the layers within and a"
url: "https://research.nvidia.com/publication/2021-02_heterogeneous-dataflow-accelerators-multi-dnn-workloads"
status: "new"
---

# Heterogeneous Dataflow Accelerators for Multi-DNN Workloads

## 摘要

AI-enabled applications such as augmented and virtual reality (AR/VR) leverage multiple deep neural network (DNN) models for various sub-tasks such as object detection, image segmentation, eye-tracking, speech recognition, and so on. Because of the diversity of the sub-tasks, the layers within and across the DNN models are highly heterogeneous in operation and shape. Diverse layer operations and shapes are major challenges for a fixed dataflow accelerator (FDA) that employs a fixed dataflow strategy on a single DNN accelerator substrate since each layer prefers different dataflows (computation order and parallelization) and tile sizes. Reconfigurable DNN accelerators (RDAs) have been proposed to adapt their dataflows to diverse layers to address the challenge. However, the dataflow flexibility in RDAs is enabled at the cost of expensive hardware structures (switches, interconnects, controller, etc.) and requires per-layer reconfiguration, which introduces considerable energy costs. Alternatively, this work proposes a new class of accelerators, heterogeneous dataflow accelerators (HDAs), which deploy multiple accelerator substrates (i.e., sub-accelerators), each supporting a different dataflow. HDAs enable coarser-grained dataflow flexibility than RDAs with higher energy efficiency and lower area cost comparable to FDAs. To exploit such benefits, hardware resource partitioning across sub-accelerators and layer execution schedule need to be carefully optimized. Therefore, we also present Herald, a framework for co-optimizing hardware partitioning and layer scheduling. Using Herald on a suite of AR/VR and MLPerf workloads, we identify a promising HDA architecture, Maelstrom, which demonstrates 65.3% lower latency and 5.0% lower energy compared to the best fixed dataflow accelerators and 22.0% lower energy at the cost of 20.7% higher latency compared to a state-of-the-art reconfigurable DNN accelerator (RDA). The results suggest that HDA is an alternative class of Pareto-optimal accelerators to RDA with strength in energy, which can be a better choice than RDAs depending on the use cases.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
