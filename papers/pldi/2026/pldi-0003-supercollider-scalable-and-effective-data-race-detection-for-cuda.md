---
id: "pldi-0003"
title: "SuperCollider: Scalable and Effective Data Race Detection for CUDA"
conference: "PLDI 2026"
date: "2026-06"
authors:
  - name: "Mark Stephenson"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Sana Damani"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Mohamed Tarek Ibn Ziad"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Anis Ladram"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Michael Garland"
    affiliation: "NVIDIA"
    is_industry: true
topics:
  - CUDA_ecosystem
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Programming Languages, Systems and Tools"
abstract: "Data races, which occur when two or more threads incorrectly access the same memory location without appropriate synchronization, cause CUDA programmers considerable pain. Even experts struggle to reason about extreme parallelism, multiple memory spaces and scopes, and diverse synchronization mechan"
url: "https://research.nvidia.com/publication/2026-06_supercollider-scalable-and-effective-data-race-detection-cuda"
status: "new"
---

# SuperCollider: Scalable and Effective Data Race Detection for CUDA

## 摘要

Data races, which occur when two or more threads incorrectly access the same memory location without appropriate synchronization, cause CUDA programmers considerable pain. Even experts struggle to reason about extreme parallelism, multiple memory spaces and scopes, and diverse synchronization mechanisms. Races can manifest as subtle data corruption, deadlock, or livelock, which are difficult to reproduce in a debugging environment. To date, there is no generally reliable tool for identifying races in GPU programs at scale. State-of-the-art dynamic GPU race detectors attempt to detect data races by faithfully tracking the memory operations, barriers, and memory fences executed by tens of thousands of threads. While this complexity enables the detection of subtle races, it comes with a cost: existing tools incur substantial memory-footprint overheads (e.g., greater than 9x) and/or runtime overheads (e.g., 1000x), and tend to report false positives. This paper introduces SuperCollider, a simple race detector for CUDA that tracks only thread-level state, is agnostic to synchronization protocols, introduces no memory-footprint overhead, seamlessly handles shared, global, and tensor memory spaces, does not produce false positives, and is relatively fast. Although SuperCollider cannot detect all races, we demonstrate that it effectively catches many data races in professionally authored CUDA programs, including races that prior art cannot. Our approach exposed over 90 data races across libraries and CUDA benchmarks, and even found a race in the CUDA Programming Guide. Unlike prior art, SuperCollider can operate at the extreme scales required by modern GPU workloads.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
