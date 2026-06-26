---
id: "arxiv-2939"
title: "Accelerating Reinforcement Learning through GPU Atari Emulation"
conference: "arXiv 2020"
date: "2020-12"
authors:
  - name: "Iuri Frosio"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Steven Dalton"
    affiliation: "NVIDIA"
    is_industry: true
topics:
  - AI & Machine Learning
  - Simulation_HPC
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Artificial Intelligence and Machine Learning"
  - "High Performance Computing"
external_links:
  - name: "Accelerating Reinforcement Learning through GPU Atari Emulation - Neurips"
    url: "https://papers.nips.cc/paper/2020/hash/e4d78a6b4d93e1d79241f7b282fa3413-Abstract.html"
  - name: "Accelerating Reinforcement Learning through GPU Atari Emulation - Link to PDF"
    url: "https://papers.nips.cc/paper/2020/file/e4d78a6b4d93e1d79241f7b282fa3413-Paper.pdf"
abstract: "We introduce CuLE (CUDA Learning Environment), a CUDA port of the Atari Learning Environment (ALE) which is used for the development of deep reinforcement algorithms. CuLE overcomes many limitations of existing CPU-based emulators and scales naturally to multiple GPUs. It leverages GPU parallelizati"
url: "https://research.nvidia.com/publication/2020-12_accelerating-reinforcement-learning-through-gpu-atari-emulation"
status: "new"
---

# Accelerating Reinforcement Learning through GPU Atari Emulation

## 摘要

We introduce CuLE (CUDA Learning Environment), a CUDA port of the Atari Learning Environment (ALE) which is used for the development of deep reinforcement algorithms. CuLE overcomes many limitations of existing CPU-based emulators and scales naturally to multiple GPUs. It leverages GPU parallelization to run thousands of games simultaneously and it renders frames directly on the GPU, to avoid the bottleneck arising from the limited CPU-GPU communication bandwidth. CuLE generates up to 155M frames per hour on a single GPU, a finding previously achieved only through a cluster of CPUs. Beyond highlighting the differences between CPU and GPU emulators in the context of reinforcement learning, we show how to leverage the high throughput of CuLE by effective batching of the training data, and show accelerated convergence for A2C+V-trace. CuLE is available at https://github.com/NVlabs/cule.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
