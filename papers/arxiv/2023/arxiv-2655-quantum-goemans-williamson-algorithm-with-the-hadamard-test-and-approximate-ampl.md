---
id: "arxiv-2655"
title: "Quantum Goemans-Williamson Algorithm with the Hadamard Test and Approximate Amplitude Constraints"
conference: "arXiv 2023"
date: "2023-07"
authors:
  - name: "Taylor Patti"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Jean Kossaifi"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Anima Anandkumar"
    affiliation: "Caltech, NVIDIA"
    is_industry: true
  - name: "Susanne F. Yelin"
    affiliation: "Harvard University"
    is_industry: false
topics:
  - Quantum_computing
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Quantum Computing"
abstract: "Semidefinite programs are optimization methods with a wide array of applications, such as approximating difficult combinatorial problems. One such semidefinite program is the Goemans-Williamson algorithm, a popular integer relaxation technique. We introduce a variational quantum algorithm for the Go"
url: "https://research.nvidia.com/publication/2023-07_quantum-goemans-williamson-algorithm-hadamard-test-and-approximate-amplitude"
status: "new"
---

# Quantum Goemans-Williamson Algorithm with the Hadamard Test and Approximate Amplitude Constraints

## 摘要

Semidefinite programs are optimization methods with a wide array of applications, such as approximating difficult combinatorial problems. One such semidefinite program is the Goemans-Williamson algorithm, a popular integer relaxation technique. We introduce a variational quantum algorithm for the Goemans-Williamson algorithm that uses only n+1 qubits, a constant number of circuit preparations, and poly(n) expectation values in order to approximately solve semidefinite programs with up to N=2^n variables and M∼O(N) constraints. Efficient optimization is achieved by encoding the objective matrix as a properly parameterized unitary conditioned on an auxilary qubit, a technique known as the Hadamard Test. The Hadamard Test enables us to optimize the objective function by estimating only a single expectation value of the ancilla qubit, rather than separately estimating exponentially many expectation values. Similarly, we illustrate that the semidefinite programming constraints can be effectively enforced by implementing a second Hadamard Test, as well as imposing a polynomial number of Pauli string amplitude constraints. We demonstrate the effectiveness of our protocol by devising an efficient quantum implementation of the Goemans-Williamson algorithm for various NP-hard problems, including MaxCut. Our method exceeds the performance of analogous classical methods on a diverse subset of well-studied MaxCut problems from the GSet library.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
