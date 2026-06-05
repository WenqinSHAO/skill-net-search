---
id: neurips-0021
title: "Point-Cloud Completion with Pretrained Text-to-image Diffusion Models"
conference: NeurIPS 2023
date: 2023-12
authors:
  - name: "Yoni Kasten"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Gal Chechik"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Ohad Rahamim"
    affiliation: ""
    is_industry: false
topics:
  - AI & Machine Learning
  - Computer Vision
  - Foundation_models
  - AI & Machine Learning
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Artificial Intelligence and Machine Learning"
  - "Computer Vision"
  - "Generative AI"
external_links:
  - name: "Project Page"
    url: "https://sds-complete.github.io/"
abstract: "Point-cloud data collected in real-world applications are often incomplete, be- cause objects are being observed from specific viewpoints, which only capture one perspective. Data can also be incomplete due to occlusion and low-resolution sampling. Existing approaches to completion rely on training "
url: "https://research.nvidia.com/publication/2023-12_point-cloud-completion-pretrained-text-image-diffusion-models"
status: new
---

# Point-Cloud Completion with Pretrained Text-to-image Diffusion Models

## 摘要

Point-cloud data collected in real-world applications are often incomplete, be- cause objects are being observed from specific viewpoints, which only capture one perspective. Data can also be incomplete due to occlusion and low-resolution sampling. Existing approaches to completion rely on training models with datasets of predefined objects to guide the completion of point clouds. Unfortunately, these approaches fail to generalize when tested on objects or real-world setups that are poorly represented in their training set. Here, we leverage recent advances in text-guided 3D shape generation, showing how to use image priors for gen- erating 3D objects. We describe an approach called SDS-Complete that uses a pre-trained text-to-image diffusion model and leverages the text semantics of a given incomplete point cloud of an object, to obtain a complete surface representa- tion. SDS-Complete can complete a variety of objects using test-time optimization without expensive collection of 3D data. We evaluate SDS-Complete on a col- lection of incomplete scanned objects, captured by real-world depth sensors and LiDAR scanners. We find that it effectively reconstructs objects that are absent from common datasets, reducing Chamfer loss by about 50% on average compared with current methods.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
