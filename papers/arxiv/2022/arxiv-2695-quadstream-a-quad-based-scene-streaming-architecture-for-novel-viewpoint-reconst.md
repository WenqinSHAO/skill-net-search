---
id: "arxiv-2695"
title: "QuadStream: A Quad-Based Scene Streaming Architecture for Novel Viewpoint Reconstruction"
conference: "arXiv 2022"
date: "2022-12"
authors:
  - name: "Jozef Hladky"
    affiliation: "Max-Planck-Institut für Informatik"
    is_industry: false
  - name: "Michael Stengel"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Nicholas Vining"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Bernhard Kerbl"
    affiliation: "TU Wien"
    is_industry: false
  - name: "Hans-Peter Seidel"
    affiliation: "Max-Planck-Institut für Informatik"
    is_industry: false
  - name: "Markus Steinberger"
    affiliation: "TU Graz"
    is_industry: false
topics:
  - Graphics_rendering
  - Interconnect_networking
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Computer Graphics"
  - "Hyperscale Graphics"
  - "Networking"
  - "Real-Time Rendering"
  - "Telecommunications"
external_links:
  - name: "Project Webpage"
    url: "https://www.cg.tuwien.ac.at/research/publications/2022/hladky-2022-QS/"
abstract: "Cloud rendering is attractive when targeting thin client devices such as phones or VR/AR headsets, or any situation where a high-end GPU is not available due to thermal or power constraints. However, it introduces the challenge of streaming rendered data over a network in a manner that is robust to "
url: "https://research.nvidia.com/publication/2022-12_quadstream-quad-based-scene-streaming-architecture-novel-viewpoint"
status: "new"
---

# QuadStream: A Quad-Based Scene Streaming Architecture for Novel Viewpoint Reconstruction

## 摘要

Cloud rendering is attractive when targeting thin client devices such as phones or VR/AR headsets, or any situation where a high-end GPU is not available due to thermal or power constraints. However, it introduces the challenge of streaming rendered data over a network in a manner that is robust to latency and potential dropouts. Current approaches range from streaming transmitted video and correcting it on the client---which fails in the presence of disocclusion events---to solutions where the server sends geometry and all rendering is performed on the client. To balance the competing goals of disocclusion robustness and minimal client workload, we introduce QuadStream, a new streaming technique that reduces motion-to-photon latency by allowing clients to render novel views on the fly and is robust against disocclusions. Our key idea is to transmit an approximate geometric scene representation to the client which is independent of the source geometry and can render both the current view frame and nearby adjacent views. Motivated by traditional macroblock approaches to video codec design, we decompose the scene seen from positions in a view cell into a series of view-aligned quads from multiple views, or QuadProxies. By operating on a rasterized G-Buffer, our approach is independent of the representation used for the scene itself. Our technical contributions are an efficient parallel quad generation, merging, and packing strategy for proxy views that cover potential client movement in a scene; a packing and encoding strategy allowing masked quads with depth information to be transmitted as a frame coherent stream; and an efficient rendering approach that takes advantage of modern hardware capabilities to turn our QuadStream representation into complete novel views on thin clients. According to our experiments, our approach achieves superior quality compared both to streaming methods that rely on simple video data and to geometry-based streaming.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
