# NVIDIA Academia-Ecosystem Analysis Plan

See `ANALYSIS_PLAN.md` for the full implementation plan governing `analyze_transfer.py`.

## Overview

- **Input**: 891 NVIDIA research papers (2020-2026) + blog transfer evidence (442 papers, 224 posts)
- **Output**: 14 charts (PNG), 4 structured JSON files, 1 markdown report
- **GPT moment**: 2022.5 split for all temporal analyses
- **Validation**: Manual sampling of 8-10 transfer matches before full analysis

## Phases

| # | Phase | Output |
|---|-------|--------|
| 0 | Data Validation | `analysis/validation_notes.md` |
| 1 | Data Loading & Cleaning | Unified paper records |
| 2 | Domain Analysis | 5 charts + `analysis/domain_analysis.json` |
| 3 | Academic Collaboration | 4 charts + `analysis/collaboration_analysis.json` |
| 4 | Product Transfer | 5 charts + `analysis/transfer_analysis.json` |
| 5 | Report Generation | `REPORT.md` citing all figures |
| 6 | Plan Compliance Check | Compliance table in `REPORT.md` |

## Charts

1. Domain static distribution (stacked pre/post GPT)
2. Domain temporal stacked area (2020-2026)
3. Domain GPT shift scatter (pre vs post count per domain)
4. Key domain line trends (CV, GPU, Foundation_models, etc.)
5. Domain x Venue heatmap
6. Collaboration lead type pie (NVIDIA-led vs academic-led)
7. Collaboration temporal split (yearly stacked bars)
8. Collaboration by domain (grouped bars)
9. Top academic collaborators (horizontal bar)
10. Transfer evidence types by era
11. Transfer by domain (stacked bars, with/without)
12. Transfer top products
13. Transfer temporal (papers vs transferred papers)
14. Transfer scholar contribution

## Key Data Quality Decisions

- **Known-NVIDIA set**: Built from ALL papers where an author has `is_industry: true` or `affiliation: "NVIDIA"` in any paper — resolves 67% empty affiliation problem
- **Lead type**: First author in known-NVIDIA set -> nvidia_led, else academic_led
- **Product names**: Dictionary of 40+ known NVIDIA products + regex fallback from blog titles
- **Broken files**: 7 YAML files skipped, 18 "authors tbd" flagged as unknown

## Product Name Dictionary

Nemotron, TensorRT, CUDA, Isaac, Megatron, Omniverse, NIM, cuQuantum, Drive, Sionna, FLARE, Earth-2, NeMo, Dynamo, Cosmos, Alpamayo, BioNeMo, DeepStream, cuOpt, Triton, NCCL, CUTLASS, Modulus, Morpheus, MONAI, RAPIDS, cuVS, Warp, RTX, DLSS, DOCA, Spectrum-X, BlueField, Maxine, Riva, Clara, Metropolis, Holoscan, GR00T
