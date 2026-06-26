---
id: "arxiv-2963"
title: "AV-FUZZER: Finding Safety Violations in Autonomous Driving Systems"
conference: "arXiv 2020"
date: "2020-10"
authors:
  - name: "Guangpeng Li"
    affiliation: "UIUC"
    is_industry: false
  - name: "Yiran Li"
    affiliation: "UIUC"
    is_industry: false
  - name: "Saurabh Jha"
    affiliation: "UIUC"
    is_industry: false
  - name: "Timothy Tsai"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Michael B. Sullivan"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Siva Hari"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Zbigniew Kalbarczyk"
    affiliation: "UIUC"
    is_industry: false
  - name: "Ravishankar Iyer"
    affiliation: "UIUC"
    is_industry: false
topics:
  - Robotics_autonomous
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Autonomous Vehicles"
  - "Resilience and Safety"
external_links:
  - name: "IEEE Digital Library"
    url: "https://ieeexplore.ieee.org/document/9251068"
abstract: "This paper proposes AV-FUZZER, a testing framework, to find the safety violations of an autonomous vehicle (AV) in the presence of an evolving traffic environment. We perturb the driving maneuvers of traffic participants to create situations in which an AV can run into safety violations. To optimall"
url: "https://research.nvidia.com/publication/2020-10_av-fuzzer-finding-safety-violations-autonomous-driving-systems"
status: "new"
---

# AV-FUZZER: Finding Safety Violations in Autonomous Driving Systems

## 摘要

This paper proposes AV-FUZZER, a testing framework, to find the safety violations of an autonomous vehicle (AV) in the presence of an evolving traffic environment. We perturb the driving maneuvers of traffic participants to create situations in which an AV can run into safety violations. To optimally search for the perturbations to be introduced, we leverage domain knowledge of vehicle dynamics and genetic algorithm to minimize the safety potential of an AV over its projected trajectory. The values of the perturbation determined by this process provide parameters that define participants’ trajectories. To improve the efficiency of the search, we design a local fuzzer that increases the exploitation of local optima in the areas where highly likely safety-hazardous situations are observed. By repeating the optimization with significantly different starting points in the search space, AV-FUZZER determines several diverse AV safety violations. We demonstrate AV-FUZZER on an industrial-grade AV platform, Baidu Apollo, and find five distinct types of safety violations in a short period of time. In comparison, other existing techniques can find at most two. We analyze the safety violations found in Apollo and discuss their overarching causes.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
