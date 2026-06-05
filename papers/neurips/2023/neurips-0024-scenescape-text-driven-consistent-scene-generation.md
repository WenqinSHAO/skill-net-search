---
id: neurips-0024
title: "SceneScape: Text-Driven Consistent Scene Generation"
conference: NeurIPS 2023
date: 2023-12
authors:
  - name: "Yoni Kasten"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Rafail Fridman"
    affiliation: ""
    is_industry: false
  - name: "Amit Abecasis"
    affiliation: ""
    is_industry: false
  - name: "Tali Dekel"
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
    url: "https://scenescape.github.io/"
abstract: "We present a method for text-driven perpetual view generation – synthesizing long-term videos of various scenes solely from an input text prompt describing the scene and camera poses. We introduce a novel framework that generates such videos in an online fashion by combining the generative power of "
url: "https://research.nvidia.com/publication/2023-12_scenescape-text-driven-consistent-scene-generation"
status: new
---

# SceneScape: Text-Driven Consistent Scene Generation

## 摘要

We present a method for text-driven perpetual view generation – synthesizing long-term videos of various scenes solely from an input text prompt describing the scene and camera poses. We introduce a novel framework that generates such videos in an online fashion by combining the generative power of a pre- trained text-to-image model with the geometric priors learned by a pre-trained monocular depth prediction model. To tackle the pivotal challenge of achieving 3D consistency, i.e., synthesizing videos that depict geometrically-plausible scenes, we deploy an online test-time training to encourage the predicted depth map of the current frame to be geometrically consistent with the synthesized scene. The depth maps are used to construct a unified mesh representation of the scene, which is progressively constructed along the video generation process. In contrast to previous works, which are applicable only to limited domains, our method generates diverse scenes, such as walkthroughs in spaceships, caves, or ice castles.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
