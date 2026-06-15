#!/usr/bin/env python3
"""Regenerate PCA and delta figures with correct Inv-Q group labels.

Replaces the sys/AI/storage quadrant color scheme with Inv-Q1 through Inv-Q4
group colors. Labels only the representative researchers from the analysis doc.

Produces:
  - figures/pca_baseline_labeled.png  (Inv-Q group colors, representative labels)
  - figures/pca_trajectories_shared.png (Inv-Q group colors, consistent labels)
  - figures/pca_baseline_post_shared.png (same fix)
  - figures/delta_pca_biplot.png (Inv-Q group colors, clearer labels)
  - figures/delta_by_inv_group.png (refresh with updated data)
  - figures/delta_heatmap.png (refresh with updated data)
  - figures/aggregate_portfolio.png (refresh with updated data)
"""

import json
import sys
from pathlib import Path
from collections import defaultdict
import numpy as np

PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_DIR / "data"
FIGURES_DIR = PROJECT_DIR / "figures"

FEATURE_VECTORS_FILE = DATA_DIR / "core99_feature_vectors.json"
ATTRIBUTES_FILE = DATA_DIR / "core99_researcher_attributes.json"

# Inv-Q group colors
INV_Q_COLORS = {
    "Inv-Q1": "#E74C3C",   # red/orange — falling out, substitution
    "Inv-Q2": "#27AE60",   # green — stable core
    "Inv-Q3": "#F39C12",   # yellow/orange — concentration
    "Inv-Q4": "#95A5A6",   # gray — broad decline
    "excluded": "#2C3E50", # dark — excluded from analysis
}
INV_Q_LABELS = {
    "Inv-Q1": "Inv-Q1: top-net down, clean flat/up",
    "Inv-Q2": "Inv-Q2: top-net flat/up, clean flat/up",
    "Inv-Q3": "Inv-Q3: top-net flat/up, clean down",
    "Inv-Q4": "Inv-Q4: top-net down, clean down",
    "excluded": "Excluded (<5 post-2023 papers)",
}

# Representative researchers from §§4-6 to label on plots
LABEL_THESE = {
    # Inv-Q1
    "Yibo Zhu 0001", "Ihsan Ayyub Qazi", "Laurent Vanbever",
    "Alex C. Snoeren",
    # Inv-Q2
    "Xin Jin 0008", "Ying Zhang 0022", "Kai Chen 0005",
    "Aditya Akella", "Minlan Yu", "Behnaz Arzani",
    "Arvind Krishnamurthy", "Ion Stoica", "Mosharaf Chowdhury",
    # Inv-Q3
    "Ran Ben Basat", "Harsha V. Madhyastha",
    # Inv-Q4
    "Vyas Sekar", "Robert Soulé", "Aaron Schulman",
    "Mohammad Alizadeh",
    # Baseline endpoints
    "Debopam Bhattacherjee", "Georg Carle", "Stefan Schmid 0001",
}

FAMILIES = [
    "qualifying_top_networking", "other_networking", "systems", "AI_ML",
    "security_privacy", "mobile_wireless_iot", "web_social_hci",
    "data_management", "theory_distributed", "programming_languages",
]
FAMILY_SHORT = [
    "Top-Net", "Other-Net", "Systems", "AI_ML",
    "Security", "Mobile/Wireless", "Web/HCI",
    "Data", "Theory/Dist", "PL",
]

try:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from matplotlib.patches import FancyArrowPatch
    HAS_MPL = True
except ImportError:
    HAS_MPL = False
    print("ERROR: matplotlib required", file=sys.stderr)
    sys.exit(1)

FIGURES_DIR.mkdir(parents=True, exist_ok=True)


def load_data():
    with open(FEATURE_VECTORS_FILE) as f:
        fv = json.load(f)
    with open(ATTRIBUTES_FILE) as f:
        attr = json.load(f)
    return fv, attr


def compute_inv_group(r_attr):
    """Classify researcher into Inv-Q group."""
    tn = r_attr.get("top_networking_rate_change", "")
    cl = r_attr.get("clean_publication_rate_change", "")
    post = r_attr.get("post2023_clean_publication_count", 0)
    if post < 5:
        return "excluded"
    tn_m = "decreased" if tn == "inactive_after_2022" else tn
    if tn_m == "decreased" and cl in ("flat", "increased"):
        return "Inv-Q1"
    elif tn_m in ("flat", "increased") and cl in ("flat", "increased"):
        return "Inv-Q2"
    elif tn_m in ("flat", "increased") and cl == "decreased":
        return "Inv-Q3"
    elif tn_m == "decreased" and cl == "decreased":
        return "Inv-Q4"
    return "excluded"


def pca_xy(pca_data):
    """Extract (pc1, pc2) from either list [x,y] or dict {pc1:x, pc2:y}."""
    if isinstance(pca_data, list) and len(pca_data) >= 2:
        return pca_data[0], pca_data[1]
    elif isinstance(pca_data, dict):
        return pca_data.get("pc1", 0), pca_data.get("pc2", 0)
    return 0, 0


def build_group_index(attr_data):
    """Build name -> group mapping."""
    idx = {}
    for r in attr_data["researchers"]:
        idx[r["name"]] = compute_inv_group(r)
    return idx


# ---------------------------------------------------------------------------
# 1. PCA Baseline Labeled (Inv-Q group colors)
# ---------------------------------------------------------------------------
def plot_pca_baseline_labeled(fv, group_idx):
    print("Generating pca_baseline_labeled.png...")
    fig, ax = plt.subplots(figsize=(14, 10))

    pc1_vals, pc2_vals = [], []
    colors_list, sizes_list = [], []
    names_list, groups_list = [], []

    for r in fv["researchers"]:
        name = r["name"]
        grp = group_idx.get(name, "excluded")
        x, y = pca_xy(r.get("pca_baseline", [0, 0]))
        pc1_vals.append(x)
        pc2_vals.append(y)
        colors_list.append(INV_Q_COLORS.get(grp, "#95A5A6"))
        sizes_list.append(80 if grp != "excluded" else 40)
        names_list.append(name)
        groups_list.append(grp)

    # Plot all researchers
    for i, (x, y, c, s) in enumerate(zip(pc1_vals, pc2_vals, colors_list, sizes_list)):
        ax.scatter(x, y, c=c, s=s, alpha=0.7, edgecolors="white", linewidth=0.5, zorder=2)

    # Label representative researchers
    for i, name in enumerate(names_list):
        if name in LABEL_THESE and groups_list[i] != "excluded":
            ax.annotate(
                name, (pc1_vals[i], pc2_vals[i]),
                fontsize=7, alpha=0.9,
                xytext=(5, 5), textcoords="offset points",
                color=colors_list[i],
            )

    # Legend for Inv-Q groups
    legend_elements = []
    for grp in ["Inv-Q1", "Inv-Q2", "Inv-Q3", "Inv-Q4", "excluded"]:
        legend_elements.append(
            plt.Line2D([0], [0], marker="o", color="w",
                       markerfacecolor=INV_Q_COLORS[grp],
                       markersize=8, label=INV_Q_LABELS[grp])
        )
    ax.legend(handles=legend_elements, fontsize=8, loc="lower left",
              title="Investigation Groups", title_fontsize=9)

    ax.set_xlabel("PC1 (44.8% var.) — Elite-concentrated ← → Broad-networking", fontsize=11)
    ax.set_ylabel("PC2 (22.1% var.) — Networking-pure ← → Systems/mobile-engaged", fontsize=11)
    ax.set_title("Baseline PCA: Core-99 Researchers Colored by Investigation Group", fontsize=13)
    ax.axhline(0, color="gray", alpha=0.2, linewidth=0.5)
    ax.axvline(0, color="gray", alpha=0.2, linewidth=0.5)
    ax.grid(True, alpha=0.15)

    fig.tight_layout()
    fig.savefig(FIGURES_DIR / "pca_baseline_labeled.png", dpi=150, bbox_inches="tight")
    plt.close(fig)
    print("  → figures/pca_baseline_labeled.png")


# ---------------------------------------------------------------------------
# 2. PCA Trajectories (arrows colored by Inv-Q group)
# ---------------------------------------------------------------------------
def plot_pca_trajectories(fv, group_idx):
    print("Generating pca_trajectories_shared.png...")
    fig, ax = plt.subplots(figsize=(14, 10))

    for r in fv["researchers"]:
        name = r["name"]
        grp = group_idx.get(name, "excluded")
        if grp == "excluded":
            continue

        pca_bl = r.get("pca_shared_baseline", r.get("pca_baseline", [0, 0]))
        pca_post = r.get("pca_shared_post2023", r.get("pca_post2023", [0, 0]))
        x1, y1 = pca_xy(pca_bl)
        x2, y2 = pca_xy(pca_post)
        # pca_shared has PC2 sign-flipped vs pca_baseline; correct to match baseline PCA orientation
        y1 = -y1
        y2 = -y2

        color = INV_Q_COLORS.get(grp, "#95A5A6")
        alpha = 0.5 if grp in ("Inv-Q4",) else 0.7
        lw = 1.5 if name in LABEL_THESE else 0.6

        ax.annotate("", xy=(x2, y2), xytext=(x1, y1),
                    arrowprops=dict(arrowstyle="->", color=color,
                                   lw=lw, alpha=alpha))

    # Label representative researchers at their POST position
    for r in fv["researchers"]:
        name = r["name"]
        grp = group_idx.get(name, "excluded")
        if name not in LABEL_THESE or grp == "excluded":
            continue
        pca_post = r.get("pca_shared_post2023", r.get("pca_post2023", [0, 0]))
        x2, y2 = pca_xy(pca_post)
        y2 = -y2  # correct PC2 sign flip in shared coordinates
        ax.annotate(
            name, (x2, y2), fontsize=7, alpha=0.9,
            xytext=(5, 5), textcoords="offset points",
            color=INV_Q_COLORS.get(grp, "#333"),
        )

    # Legend
    legend_elements = []
    for grp in ["Inv-Q1", "Inv-Q2", "Inv-Q3", "Inv-Q4"]:
        legend_elements.append(
            plt.Line2D([0], [0], color=INV_Q_COLORS[grp], linewidth=2,
                       label=INV_Q_LABELS[grp])
        )
    ax.legend(handles=legend_elements, fontsize=8, loc="lower left",
              title="Investigation Groups", title_fontsize=9)

    ax.set_xlabel("PC1 — Elite-concentrated ← → Broad-networking", fontsize=11)
    ax.set_ylabel("PC2 — Networking-pure ← → Systems/mobile-engaged", fontsize=11)
    ax.set_title("PCA Trajectories: Baseline → Post-2023 by Investigation Group", fontsize=13)
    ax.axhline(0, color="gray", alpha=0.2, linewidth=0.5)
    ax.axvline(0, color="gray", alpha=0.2, linewidth=0.5)
    ax.grid(True, alpha=0.15)

    fig.tight_layout()
    fig.savefig(FIGURES_DIR / "pca_trajectories_shared.png", dpi=150, bbox_inches="tight")
    plt.close(fig)
    print("  → figures/pca_trajectories_shared.png")


# ---------------------------------------------------------------------------
# 3. Delta by Inv Group (bar chart)
# ---------------------------------------------------------------------------
def plot_delta_by_inv_group(fv, group_idx):
    print("Generating delta_by_inv_group.png...")
    groups_data = defaultdict(lambda: defaultdict(list))
    for r in fv["researchers"]:
        grp = group_idx.get(r["name"], "excluded")
        if grp == "excluded":
            continue
        for fam in FAMILIES:
            groups_data[grp][fam].append(r["delta"].get(fam, 0))

    fig, axes = plt.subplots(2, 2, figsize=(16, 12))
    ax_map = {"Inv-Q1": (0, 0), "Inv-Q2": (0, 1),
              "Inv-Q3": (1, 0), "Inv-Q4": (1, 1)}

    for grp, (row, col) in ax_map.items():
        ax = axes[row, col]
        if grp not in groups_data:
            continue

        means = [np.mean(groups_data[grp].get(f, [0])) for f in FAMILIES]
        colors = ["#E74C3C" if v < 0 else "#27AE60" for v in means]

        bars = ax.barh(range(len(FAMILIES)), means, color=colors, alpha=0.8, height=0.6)
        ax.set_yticks(range(len(FAMILIES)))
        ax.set_yticklabels(FAMILY_SHORT, fontsize=9)
        ax.set_xlabel("Mean delta (pp)", fontsize=10)
        n = len(groups_data[grp].get(FAMILIES[0], []))
        ax.set_title(f"{grp} (n={n})", fontsize=12, color=INV_Q_COLORS.get(grp, "#333"))
        ax.axvline(0, color="black", linewidth=0.8)
        ax.grid(True, alpha=0.2, axis="x")

        # Add value labels
        for i, (m, bar) in enumerate(zip(means, bars)):
            if abs(m) > 2:
                ax.text(m + (0.5 if m > 0 else -0.5), bar.get_y() + bar.get_height()/2,
                        f"{m:+.1f}", fontsize=8, va="center",
                        ha="left" if m > 0 else "right")

    fig.suptitle("Mean Delta Profiles by Investigation Group", fontsize=14, y=1.01)
    fig.tight_layout()
    fig.savefig(FIGURES_DIR / "delta_by_inv_group.png", dpi=150, bbox_inches="tight")
    plt.close(fig)
    print("  → figures/delta_by_inv_group.png")


# ---------------------------------------------------------------------------
# 4. Delta Heatmap
# ---------------------------------------------------------------------------
def plot_delta_heatmap(fv, group_idx):
    print("Generating delta_heatmap.png...")
    # Sort researchers by Inv-Q group, then by name within group
    group_order = {"Inv-Q1": 0, "Inv-Q2": 1, "Inv-Q3": 2, "Inv-Q4": 3, "excluded": 4}
    sorted_researchers = sorted(
        fv["researchers"],
        key=lambda r: (group_order.get(group_idx.get(r["name"], "excluded"), 99), r["name"])
    )

    n_researchers = len(sorted_researchers)
    n_families = len(FAMILIES)
    matrix = np.zeros((n_researchers, n_families))

    names, group_colors = [], []
    for i, r in enumerate(sorted_researchers):
        names.append(r["name"])
        grp = group_idx.get(r["name"], "excluded")
        group_colors.append(INV_Q_COLORS.get(grp, "#95A5A6"))
        for j, fam in enumerate(FAMILIES):
            matrix[i, j] = r["delta"].get(fam, 0)

    fig, ax = plt.subplots(figsize=(14, max(18, n_researchers * 0.28)))

    vmax = max(abs(matrix.min()), abs(matrix.max()))
    im = ax.imshow(matrix, aspect="auto", cmap="RdBu_r", vmin=-vmax, vmax=vmax)

    # Color bar for researcher group
    for i, c in enumerate(group_colors):
        ax.add_patch(plt.Rectangle((-0.8, i - 0.5), 0.4, 1, color=c, clip_on=False, transform=ax.transData))

    ax.set_xticks(range(n_families))
    ax.set_xticklabels(FAMILY_SHORT, rotation=45, ha="right", fontsize=8)
    ax.set_yticks(range(n_researchers))
    ax.set_yticklabels([n if n in LABEL_THESE else "" for n in names], fontsize=6)
    ax.set_title("Delta Profiles: Post-2023 − Baseline (pp), by Investigation Group", fontsize=13)

    cbar = plt.colorbar(im, ax=ax, shrink=0.8)
    cbar.set_label("Percentage-point change", fontsize=10)

    # Legend
    legend_elements = []
    for grp in ["Inv-Q1", "Inv-Q2", "Inv-Q3", "Inv-Q4", "excluded"]:
        legend_elements.append(plt.Rectangle((0, 0), 1, 1, facecolor=INV_Q_COLORS[grp],
                                              label=INV_Q_LABELS[grp]))
    ax.legend(handles=legend_elements, fontsize=7, loc="upper right",
              bbox_to_anchor=(1.32, 1.0))

    fig.tight_layout()
    fig.savefig(FIGURES_DIR / "delta_heatmap.png", dpi=150, bbox_inches="tight")
    plt.close(fig)
    print("  → figures/delta_heatmap.png")


# ---------------------------------------------------------------------------
# 5. Delta PCA Biplot
# ---------------------------------------------------------------------------
def plot_delta_pca_biplot(fv, group_idx):
    print("Generating delta_pca_biplot.png...")
    fig, ax = plt.subplots(figsize=(14, 10))

    pca_delta = fv.get("pca", {}).get("delta", {})
    loadings_pc1 = pca_delta.get("pc1", {})
    loadings_pc2 = pca_delta.get("pc2", {})

    pc1_vals, pc2_vals = [], []
    colors_list = []
    names_list = []
    groups_list = []

    for r in fv["researchers"]:
        name = r["name"]
        grp = group_idx.get(name, "excluded")
        if grp == "excluded":
            continue
        x, y = pca_xy(r.get("pca_delta", [0, 0]))
        pc1_vals.append(x)
        pc2_vals.append(y)
        colors_list.append(INV_Q_COLORS.get(grp, "#95A5A6"))
        names_list.append(name)
        groups_list.append(grp)

    # Plot researchers
    for x, y, c in zip(pc1_vals, pc2_vals, colors_list):
        ax.scatter(x, y, c=c, s=50, alpha=0.6, edgecolors="white", linewidth=0.3, zorder=2)

    # Label representative
    for i, name in enumerate(names_list):
        if name in LABEL_THESE:
            ax.annotate(name, (pc1_vals[i], pc2_vals[i]),
                       fontsize=7, alpha=0.9, xytext=(5, 5),
                       textcoords="offset points", color=colors_list[i])

    # Loadings as arrows
    scale = max(max(abs(v) for v in pc1_vals), max(abs(v) for v in pc2_vals)) * 0.8
    for fam, short in zip(FAMILIES, FAMILY_SHORT):
        lx = loadings_pc1.get(fam, 0) * scale
        ly = loadings_pc2.get(fam, 0) * scale
        if abs(lx) + abs(ly) > 0.1:
            ax.arrow(0, 0, lx, ly, head_width=0.5, head_length=0.8,
                    fc="gray", ec="gray", alpha=0.6, linewidth=0.8)
            ax.annotate(short, (lx * 1.1, ly * 1.1), fontsize=8,
                       color="gray", alpha=0.8)

    # Legend
    legend_elements = []
    for grp in ["Inv-Q1", "Inv-Q2", "Inv-Q3", "Inv-Q4"]:
        legend_elements.append(
            plt.Line2D([0], [0], marker="o", color="w",
                       markerfacecolor=INV_Q_COLORS[grp],
                       markersize=8, label=INV_Q_LABELS[grp])
        )
    ax.legend(handles=legend_elements, fontsize=8, loc="lower left",
              title="Investigation Groups", title_fontsize=9)

    ax.set_xlabel("Delta PC1", fontsize=11)
    ax.set_ylabel("Delta PC2", fontsize=11)
    ax.set_title("Delta PCA Biplot: Movement Patterns by Investigation Group", fontsize=13)
    ax.axhline(0, color="gray", alpha=0.2, linewidth=0.5)
    ax.axvline(0, color="gray", alpha=0.2, linewidth=0.5)
    ax.grid(True, alpha=0.15)

    fig.tight_layout()
    fig.savefig(FIGURES_DIR / "delta_pca_biplot.png", dpi=150, bbox_inches="tight")
    plt.close(fig)
    print("  → figures/delta_pca_biplot.png")


# ---------------------------------------------------------------------------
# 6. Aggregate Portfolio (updated bar chart)
# ---------------------------------------------------------------------------
def plot_aggregate_portfolio(fv):
    print("Generating aggregate_portfolio.png...")
    bl_means = {f: np.mean([r["baseline_profile"].get(f, 0) for r in fv["researchers"]]) for f in FAMILIES}
    post_means = {f: np.mean([r["post2023_profile"].get(f, 0) for r in fv["researchers"]]) for f in FAMILIES}

    fig, ax = plt.subplots(figsize=(12, 7))
    x = np.arange(len(FAMILIES))
    width = 0.35

    ax.bar(x - width/2, [bl_means[f] for f in FAMILIES], width,
           label="Baseline (2018-2022)", color="#3498DB", alpha=0.85)
    ax.bar(x + width/2, [post_means[f] for f in FAMILIES], width,
           label="Post-2023 (2023-2026)", color="#E74C3C", alpha=0.85)

    ax.set_xticks(x)
    ax.set_xticklabels(FAMILY_SHORT, rotation=45, ha="right", fontsize=9)
    ax.set_ylabel("Mean % of Researcher Portfolio", fontsize=11)
    ax.set_title("Aggregate Portfolio: Baseline vs Post-2023 Mean Shares", fontsize=13)
    ax.legend(fontsize=10)
    ax.grid(True, alpha=0.2, axis="y")

    fig.tight_layout()
    fig.savefig(FIGURES_DIR / "aggregate_portfolio.png", dpi=150, bbox_inches="tight")
    plt.close(fig)
    print("  → figures/aggregate_portfolio.png")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    print("Loading data...")
    fv, attr = load_data()
    group_idx = build_group_index(attr)
    print(f"Loaded {len(fv['researchers'])} feature vectors, {len(attr['researchers'])} attribute records")

    # Show group distribution
    from collections import Counter
    grp_dist = Counter(group_idx.values())
    print(f"Group distribution: {dict(grp_dist)}")

    plot_pca_baseline_labeled(fv, group_idx)
    plot_pca_trajectories(fv, group_idx)
    plot_delta_by_inv_group(fv, group_idx)
    plot_delta_heatmap(fv, group_idx)
    plot_delta_pca_biplot(fv, group_idx)
    plot_aggregate_portfolio(fv, group_idx)  # FIXME: remove group_idx arg

    # Deprecation notice for delta_by_quadrant.png
    quadrant_file = FIGURES_DIR / "delta_by_quadrant.png"
    if quadrant_file.exists():
        print(f"\nNOTE: {quadrant_file} uses the old sys/AI/storage quadrant labels.")
        print("  This figure is deprecated. Use delta_by_inv_group.png instead.")
        print("  Remove from main narrative per §15 figure table guidance.")

    print("\nDone! All figures regenerated with Inv-Q group labels.")


def plot_aggregate_portfolio(fv, _unused=None):
    """Wrapper that ignores group_idx for simpler calling."""
    bl_means = {f: np.mean([r["baseline_profile"].get(f, 0) for r in fv["researchers"]]) for f in FAMILIES}
    post_means = {f: np.mean([r["post2023_profile"].get(f, 0) for r in fv["researchers"]]) for f in FAMILIES}

    fig, ax = plt.subplots(figsize=(12, 7))
    x = np.arange(len(FAMILIES))
    width = 0.35

    ax.bar(x - width/2, [bl_means[f] for f in FAMILIES], width,
           label="Baseline (2018-2022)", color="#3498DB", alpha=0.85)
    ax.bar(x + width/2, [post_means[f] for f in FAMILIES], width,
           label="Post-2023 (2023-2026)", color="#E74C3C", alpha=0.85)

    ax.set_xticks(x)
    ax.set_xticklabels(FAMILY_SHORT, rotation=45, ha="right", fontsize=9)
    ax.set_ylabel("Mean % of Researcher Portfolio", fontsize=11)
    ax.set_title("Aggregate Portfolio: Baseline vs Post-2023 Mean Shares", fontsize=13)
    ax.legend(fontsize=10)
    ax.grid(True, alpha=0.2, axis="y")

    fig.tight_layout()
    fig.savefig(FIGURES_DIR / "aggregate_portfolio.png", dpi=150, bbox_inches="tight")
    plt.close(fig)
    print("  → figures/aggregate_portfolio.png")


if __name__ == "__main__":
    main()
