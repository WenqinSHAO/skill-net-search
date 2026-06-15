#!/usr/bin/env bash
# Run the full networking-to-ai-migration pipeline.
# Each phase is idempotent and supports resume.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"
cd "$PROJECT_DIR"

echo "============================================"
echo "Networking → AI Migration Pipeline"
echo "============================================"
echo ""

# Phase 1: Identify cohort
echo ">>> Phase 1: Identify Qualified Researcher Cohort"
python3 "$SCRIPT_DIR/identify_cohort.py"
echo ""

# Phase 2: Fetch publication history
echo ">>> Phase 2: Fetch Full Publication History"
python3 "$SCRIPT_DIR/fetch_publications.py"
echo ""

# Phase 3: Classify zones
echo ">>> Phase 3: Classify Papers into Zones"
python3 "$SCRIPT_DIR/classify_zones.py"
echo ""

# Phase 4: Assign geographic regions
echo ">>> Phase 4: Assign Geographic Regions"
python3 "$SCRIPT_DIR/assign_geo.py"
echo ""

# Phase 5: Build researcher itineraries
echo ">>> Phase 5: Build Researcher Itineraries"
python3 "$SCRIPT_DIR/build_itineraries.py"
echo ""

# Phase 6: Compute legacy/auxiliary transition metrics
echo ">>> Phase 6: Compute Auxiliary Transition Metrics"
python3 "$SCRIPT_DIR/compute_metrics.py"
echo ""

# Phase 7: Generate legacy charts and report
echo ">>> Phase 7: Generate Legacy Charts and Report"
python3 "$SCRIPT_DIR/generate_charts.py"
echo ""

echo "============================================"
echo "Pipeline complete!"
echo "Report: $(pwd)/REPORT.md"
echo "Charts: $(pwd)/figures/"
echo "============================================"
