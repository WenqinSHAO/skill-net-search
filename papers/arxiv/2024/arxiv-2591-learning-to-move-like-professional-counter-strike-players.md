---
id: arxiv-2591
title: "Learning to Move Like Professional Counter-Strike Players"
conference: arXiv 2024
date: 2024-09
authors:
  - name: "Iuri Frosio"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Chen Tessler"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Joohwan Kim"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "David Durst"
    affiliation: ""
    is_industry: false
  - name: "F. Xie"
    affiliation: ""
    is_industry: false
  - name: "V. Sarukkai"
    affiliation: ""
    is_industry: false
  - name: "Brennan Shacklett"
    affiliation: ""
    is_industry: false
  - name: "C. Taylor"
    affiliation: ""
    is_industry: false
  - name: "G. Bernstein"
    affiliation: ""
    is_industry: false
  - name: "S. Choudhury"
    affiliation: ""
    is_industry: false
  - name: "P. Hanrahan"
    affiliation: ""
    is_industry: false
  - name: "Kayvon Fatahalian"
    affiliation: ""
    is_industry: false
topics:
  - AI & Machine Learning
  - Applied_perception
  - Foundation_models
  - Graphics_rendering
  - Robotics_autonomous
  - AI & Machine Learning
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Artificial Intelligence and Machine Learning"
  - "Computer Graphics"
  - "Esports"
  - "Generative AI"
  - "Human Computer Interaction"
  - "Robotics"
external_links:
  - name: "Link to the paper"
    url: "https://dl.acm.org/doi/10.1111/cgf.15173"
abstract: "In multiplayer, first-person shooter games like Counter-Strike: Global Offensive (CS:GO), coordinated movement is a critical component of high-level strategic play. However, the complexity of team coordination and the variety of conditions present in popular game maps make it impractical to author h"
url: "https://research.nvidia.com/publication/2024-09_learning-move-professional-counter-strike-players"
status: new
---

# Learning to Move Like Professional Counter-Strike Players

## 摘要

In multiplayer, first-person shooter games like Counter-Strike: Global Offensive (CS:GO), coordinated movement is a critical component of high-level strategic play. However, the complexity of team coordination and the variety of conditions present in popular game maps make it impractical to author hand-crafted movement policies for every scenario. We show that it is possible to take a data-driven approach to creating human-like movement controllers for CS:GO. We curate a team movement dataset comprising 123 hours of professional game play traces, and use this dataset to train a transformer-based movement model that generates human-like team movement for all players in a "Retakes" round of the game. Importantly, the movement prediction model is efficient. Performing inference for all players takes less than 0.5 ms per game step (amortized cost) on a single CPU core, making it plausible for use in commercial games today. Human evaluators assess that our model behaves more like humans than both commercially-available bots and procedural movement controllers scripted by experts (16% to 59% higher by TrueSkill rating of "human-like"). Using experiments involving in-game bot vs. bot self-play, we demonstrate that our model performs simple forms of teamwork, makes fewer common movement mistakes, and yields movement distributions, player lifetimes, and kill locations similar to those observed in professional CS:GO match play.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
