---
id: "siggraph-0059"
title: "Detecting Viewer-Perceived Intended Vector Sketch Connectivity"
conference: "SIGGRAPH 2022"
date: "2022-08"
authors:
  - name: "Jerry Yin"
    affiliation: "University of British Columbia"
    is_industry: false
  - name: "Chenxi Liu"
    affiliation: "University of British Columbia"
    is_industry: false
  - name: "Rebecca Liu"
    affiliation: "University of British Columbia"
    is_industry: false
  - name: "Nicholas Vining"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Helge Rhodin"
    affiliation: "University of British Columbia"
    is_industry: false
  - name: "Alla Sheffer"
    affiliation: "University of British Columbia"
    is_industry: false
topics:
  - AI & Machine Learning
  - Applied_perception
  - Graphics_rendering
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Applied Perception"
  - "Artificial Intelligence and Machine Learning"
  - "Computer Graphics"
external_links:
  - name: "Project Webpage"
    url: "https://www.cs.ubc.ca/labs/imager/tr/2022/SketchConnectivity/"
abstract: "Many sketch processing applications target precise vector drawings with accurately specified stroke intersections, yet free-form artist drawn sketches are typically inexact: strokes that are intended to intersect often stop short of doing so. While human observers easily perceive the artist intended"
url: "https://research.nvidia.com/publication/2022-08_detecting-viewer-perceived-intended-vector-sketch-connectivity"
status: "new"
---

# Detecting Viewer-Perceived Intended Vector Sketch Connectivity

## 摘要

Many sketch processing applications target precise vector drawings with accurately specified stroke intersections, yet free-form artist drawn sketches are typically inexact: strokes that are intended to intersect often stop short of doing so. While human observers easily perceive the artist intended stroke connectivity, manually, or even semi-manually, correcting drawings to generate correctly connected outputs is tedious and highly time consuming. We propose a novel, robust algorithm that extracts viewer-perceived stroke connectivity from inexact free-form vector drawings by leveraging observations about local and global factors that impact human perception of inter-stroke connectivity. We employ the identified local cues to train classifiers that assess the likelihood that pairs of strokes are perceived as forming end-to-end or T- junctions based on local context. We then use these classifiers within an incremental framework that combines classifier provided likelihoods with a more global, contextual and closure-based, analysis. We demonstrate our method on over 95 diversely sourced inputs, and validate it via a series of perceptual studies; participants prefer our outputs over the closest alternative by a factor of 9 to 1.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
