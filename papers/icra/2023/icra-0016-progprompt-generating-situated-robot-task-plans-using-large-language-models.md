---
id: "icra-0016"
title: "ProgPrompt: Generating Situated Robot Task Plans Using Large Language Models"
conference: "ICRA 2023"
date: "2023-05"
authors:
  - name: "Ishika Singh"
    affiliation: "University of Southern California"
    is_industry: false
  - name: "Valts Blukis"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Arsalan Mousavian"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Ankit Goyal"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Danfei Xu"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Jonathan Tremblay"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Dieter Fox"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Jesse Thomason"
    affiliation: "University of Southern California"
    is_industry: false
  - name: "Animesh Garg"
    affiliation: "NVIDIA"
    is_industry: true
topics:
  - AI & Machine Learning
  - Foundation_models
  - Robotics_autonomous
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Artificial Intelligence and Machine Learning"
  - "Generative AI"
  - "Robotics"
external_links:
  - name: "Website"
    url: "https://progprompt.github.io/"
abstract: "Task planning can require defining myriad domain knowledge about the world in which a robot needs to act. To ameliorate that effort, large language models (LLMs) can be used to score potential next actions during task planning, and even generate action sequences directly, given an instruction in nat"
url: "https://research.nvidia.com/publication/2023-05_progprompt-generating-situated-robot-task-plans-using-large-language-models"
status: "new"
---

# ProgPrompt: Generating Situated Robot Task Plans Using Large Language Models

## 摘要

Task planning can require defining myriad domain knowledge about the world in which a robot needs to act. To ameliorate that effort, large language models (LLMs) can be used to score potential next actions during task planning, and even generate action sequences directly, given an instruction in natural language with no additional domain information. However, such methods either require enumerating all possible next steps for scoring, or generate free-form text that may contain actions not possible on a given robot in its current context. We present a programmatic LLM prompt structure that enables plan generation functional across situated environments, robot capabilities, and tasks. Our key insight is to prompt the LLM with program-like specifications of the available actions and objects in an environment, as well as with example programs that can be executed. We make concrete recommendations about prompt structure and generation constraints through ablation experiments, demonstrate state of the art success rates in VirtualHome household tasks, and deploy our method on a physical robot arm for tabletop tasks.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
