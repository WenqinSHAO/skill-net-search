---
id: "arxiv-2981"
title: "OCEAN: Online Task Inference for Compositional Tasks with Context Adaptation"
conference: "arXiv 2020"
date: "2020-08"
authors:
  - name: "Hongyu Ren"
    affiliation: "Stanford University"
    is_industry: false
  - name: "Yuke Zhu"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Jure Leskovec"
    affiliation: "Stanford University"
    is_industry: false
  - name: "Anima Anandkumar"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Animesh Garg"
    affiliation: "NVIDIA"
    is_industry: true
topics:
  - Robotics_autonomous
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Robotics"
external_links:
  - name: "Paper"
    url: "http://www.auai.org/uai2020/proceedings/569_main_paper.pdf"
abstract: "Real-world tasks often exhibit a compositional structure that contains a sequence of simpler sub-tasks. For instance, opening a door requires reaching, grasping, rotating, and pulling the door knob. Such compositional tasks require an agent to reason about the sub-task at hand while orchestrating gl"
url: "https://research.nvidia.com/publication/2020-08_ocean-online-task-inference-compositional-tasks-context-adaptation"
status: "new"
---

# OCEAN: Online Task Inference for Compositional Tasks with Context Adaptation

## 摘要

Real-world tasks often exhibit a compositional structure that contains a sequence of simpler sub-tasks. For instance, opening a door requires reaching, grasping, rotating, and pulling the door knob. Such compositional tasks require an agent to reason about the sub-task at hand while orchestrating global behavior accordingly. This can be cast as an online task inference problem, where the current task identity, represented by a context variable, is estimated from the agent’s past experiences with probabilistic inference. Previous approaches have employed simple latent distributions, e.g., Gaussian, to model a single context for the entire task. However, this formulation lacks the expressiveness to capture the composition and transition of the sub-tasks. We propose a variational inference framework OCEAN to perform online task inference for compositional tasks. OCEAN models global and local context variables in a joint latent space, where the global variables represent a mixture of subtasks required for the task, while the local variables capture the transitions between the subtasks. Our framework supports flexible latent distributions based on prior knowledge of the task structure and can be trained in an unsupervised manner. Experimental results show that OCEAN provides more effective task inference with sequential context adaptation and thus leads to a performance boost on complex, multi-stage tasks.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
