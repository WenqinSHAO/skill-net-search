---
id: "rss-0011"
title: "IndustReal: Transferring Contact-Rich Assembly Tasks from Simulation to Reality"
conference: "RSS 2023"
date: "2023-05"
authors:
  - name: "Bingjie Tang"
    affiliation: "University of Southern California"
    is_industry: false
  - name: "Michael A. Lin"
    affiliation: "Stanford University"
    is_industry: false
  - name: "Iretiayo Akinola"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Ankur Handa"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Gaurav S. Sukhatme"
    affiliation: "University of Southern California"
    is_industry: false
  - name: "Fabio Ramos"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Dieter Fox"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Yashraj Narang"
    affiliation: "NVIDIA"
    is_industry: true
topics:
  - AI & Machine Learning
  - Robotics_autonomous
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Artificial Intelligence and Machine Learning"
  - "Physical AI"
  - "Robotics"
external_links:
  - name: "Short Video (7.5 min)"
    url: "https://player.vimeo.com/video/807609001?h=1b59e1b166"
  - name: "Long Video (14 min)"
    url: "https://player.vimeo.com/video/802878552?h=1b0186507a"
  - name: "Tech Blog"
    url: "https://developer.nvidia.com/blog/transferring-industrial-robot-assembly-tasks-from-simulation-to-reality/"
  - name: "IndustRealKit (hardware repo)"
    url: "https://github.com/NVlabs/industrealkit"
  - name: "Code for original IndustRealSim (environments and training repo in Isaac Gym)"
    url: "https://github.com/isaac-sim/IsaacGymEnvs/tree/main/isaacgymenvs/tasks/industreal"
  - name: "Docs for original IndustRealSim"
    url: "https://github.com/isaac-sim/IsaacGymEnvs/blob/main/docs/industreal.md"
  - name: "Code for new IndustRealSim (environments and training repo in Isaac Lab)"
    url: "https://github.com/isaac-sim/IsaacLab/tree/main/source/isaaclab_tasks/isaaclab_tasks/direct/factory"
  - name: "Docs for new IndustRealSim"
    url: "https://github.com/isaac-sim/IsaacLab/blob/main/docs/source/overview/environments.rst#contact-rich-manipulation"
  - name: "IndustRealLib (deployment repo)"
    url: "https://github.com/NVLabs/industreallib"
abstract: "Robotic assembly is a longstanding challenge, requiring contact-rich interaction and high precision and accuracy. Many applications also require adaptivity to diverse parts, poses, and environments, as well as low cycle times. In other areas of robotics, simulation is a powerful tool to develop algo"
url: "https://research.nvidia.com/publication/2023-05_industreal-transferring-contact-rich-assembly-tasks-simulation-reality"
status: "new"
---

# IndustReal: Transferring Contact-Rich Assembly Tasks from Simulation to Reality

## 摘要

Robotic assembly is a longstanding challenge, requiring contact-rich interaction and high precision and accuracy. Many applications also require adaptivity to diverse parts, poses, and environments, as well as low cycle times. In other areas of robotics, simulation is a powerful tool to develop algorithms, generate datasets, and train agents. However, simulation has had a more limited impact on assembly. We present IndustReal, a set of algorithms, systems, and tools that solve assembly tasks in simulation with reinforcement learning (RL) and successfully achieve policy transfer to the real world. Specifically, we propose 1) simulation-aware policy updates, 2) signed-distance-field rewards, and 3) sampling-based curricula for robotic RL agents. We use these algorithms to enable robots to solve contact-rich pick, place, and insertion tasks in simulation. We then propose 4) a policy-level action integrator to minimize error at policy deployment time. We build and demonstrate a real-world robotic assembly system that uses the trained policies and action integrator to achieve repeatable performance in the real world. Finally, we present hardware and software tools that allow other researchers to reproduce our system and results.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
