---
id: "arxiv-2596"
title: "VerilogCoder: Autonomous Verilog Coding Agents with Graph-based Planning and Abstract Syntax Tree (AST)-based Waveform Tracing Tool"
conference: "arXiv 2024"
date: "2024-08"
authors:
  - name: "Chia-Tung (Mark) Ho"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Mark Haoxing Ren"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Brucek Khailany"
    affiliation: "NVIDIA"
    is_industry: true
topics:
  - AI & Machine Learning
  - Foundation_models
  - GPU_architecture
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Artificial Intelligence and Machine Learning"
  - "Circuits and VLSI Design"
  - "Generative AI"
abstract: "Due to the growing complexity of modern Integrated Circuits (ICs), automating hardware design can prevent a significant amount of human error from the engineering process and result in less errors. Verilog is a popular hardware description language for designing and modeling digital systems; thus, V"
url: "https://research.nvidia.com/publication/2024-08_verilogcoder-autonomous-verilog-coding-agents-graph-based-planning-and-abstract"
status: "new"
---

# VerilogCoder: Autonomous Verilog Coding Agents with Graph-based Planning and Abstract Syntax Tree (AST)-based Waveform Tracing Tool

## 摘要

Due to the growing complexity of modern Integrated Circuits (ICs), automating hardware design can prevent a significant amount of human error from the engineering process and result in less errors. Verilog is a popular hardware description language for designing and modeling digital systems; thus, Verilog generation is one of the emerging areas of research to facilitate the design process. In this work, we propose VerilogCoder, a system of multiple Artificial Intelligence (AI) agents for Verilog code generation, to autonomously write Verilog code and fix syntax and functional errors using collaborative Verilog tools (i.e., syntax checker, simulator, and waveform tracer). Firstly, we propose a task planner that utilizes a novel Task and Circuit Relation Graph retrieval method to construct a holistic plan based on module descriptions. To debug and fix functional errors, we develop a novel and efficient abstract syntax tree (AST)-based waveform tracing tool, which is integrated within the autonomous Verilog completion flow. The proposed methodology successfully generates 94.2% syntactically and functionally correct Verilog code, surpassing the state-of-the-art methods by 33.9% on the VerilogEval-Human v2 benchmark.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
