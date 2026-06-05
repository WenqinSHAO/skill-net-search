# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## This repo is dual-purpose

1. **Skill repo** — `SKILL.md` defines the `net-research` skill. When a user request matches research paper curation, project scoping, per-paper analysis, or cross-paper synthesis, invoke the net-research skill. It governs all shared-layer and project-layer workflows.
2. **Research database** — `index/all_papers.json` is the canonical shared paper index; `papers/` holds shared paper records; `projects/` holds project-specific workspaces.

## Default behavior

- Read `SKILL.md` and `SPEC.md` before any operation that touches the database.
- The shared layer (`papers/`, `index/`) is the permanent record. Never write project-specific judgements there.
- Project-layer content lives in `projects/{name}/` and is disposable; it can be rewritten or rebuilt as needed.
- Prefer incremental growth over one-shot comprehensive reports — let the database and project insights accumulate through repeated use, following the workflows in SKILL.md.

## Housekeeping

- After any shared-layer mutation (adding/updating papers), run `python scripts/validate_repo.py` to check invariants.
- Before importing papers, check for duplicates against `index/all_papers.json` using the deduplication rules in SPEC.md.
- If a project's structure becomes messy, prefer extracting the valuable parts (paper scope, insights) and starting fresh over patching in place.


## General
- Address me as <My lord>, and yourself as <Shiye>
