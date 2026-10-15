#!/usr/bin/env python3
"""Build the evidence-led, offline Tencent networking research report and SVGs."""
from __future__ import annotations

import argparse
import csv
import hashlib
import html
import io
import json
import re
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, FancyBboxPatch
import numpy as np
from bs4 import BeautifulSoup

from collect import ROOT, fetch, save
from export import build_tables, metadata_tables, institution_parts

OUT = ROOT / "output"
FIGURES = OUT / "report_figures"
WORLD_URL = "https://raw.githubusercontent.com/nvkelso/natural-earth-vector/master/geojson/ne_110m_admin_0_countries.geojson"
INK, MUTED, PAPER = "#172d3a", "#526777", "#fbfaf7"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 10, "text.color": INK,
    "axes.labelcolor": INK, "xtick.color": MUTED, "ytick.color": MUTED,
    "axes.edgecolor": "#d9e1e3", "axes.spines.top": False, "axes.spines.right": False,
    "figure.facecolor": PAPER, "axes.facecolor": PAPER, "svg.fonttype": "none", "svg.hashsalt": "tencent-survey"})


def percent(value):
    return str(Decimal(str(value)).quantize(Decimal("0.1"), rounding=ROUND_HALF_UP)) + "%"


def load_inputs():
    tables = metadata_tables(build_tables())
    annotations = json.loads((ROOT / "data/analysis_papers.json").read_text())
    content = json.loads((ROOT / "data/report_content.json").read_text())
    geography = json.loads((ROOT / "data/analysis_geography.json").read_text())
    ids = {p["paper_id"] for p in tables["Publications"]}
    assert ids == set(annotations["papers"]), "Every primary paper needs exactly one reviewed classification"
    authors = tables["Author_Affiliations"]
    papers = []
    for p in tables["Publications"]:
        a = [x for x in authors if x["paper_id"] == p["paper_id"]]
        partners = sorted({x["institution"] for x in a if x["institution_type"] in {"academic", "research_institute"}})
        others = sorted({x["institution"] for x in a if x["institution_type"] == "industry" and not x["is_tencent"]})
        all_inst = {x["institution"] for x in a if x["institution"]}
        first = [x for x in a if x["author_position"] == 1]
        first_tencent = any(x["is_tencent"] for x in first)
        first_academic = any(x["institution_type"] in {"academic", "research_institute"} for x in first)
        first_class = "Dual Tencent + academic/research" if first_tencent and first_academic else "Academic/research without Tencent" if first_academic else "Tencent without academic/research" if first_tencent else "Explicit unaffiliated / other"
        kind = "Academic/research collaboration" if partners else "Other-industry collaboration" if others else "Tencent-only" if all_inst == {"Tencent"} and not any(x["institution_type"] == "unaffiliated" for x in a) else "Other / unresolved"
        papers.append({**p, **annotations["papers"][p["paper_id"]], "partners": partners,
                       "industry_partners": others, "collaboration_type": kind,
                       "first_author_name": first[0]["author_name"], "first_author_class": first_class,
                       "first_author_institutions": "; ".join(sorted({x["institution"] for x in first if x["institution"]}))})
    return tables, annotations["topics"], content, geography, papers


def geography_rows(tables, geography, papers, acquire=False):
    deposits = json.loads((ROOT / "data/metadata_audit.json").read_text())["publisher_deposits"]
    institutions = sorted({i for p in papers for i in p["partners"]})
    history_path = ROOT / "data/analysis_geography_checks.json"
    previous = {r["institution"]: r for r in json.loads(history_path.read_text())["checks"]} if history_path.exists() else {}
    assert set(institutions) == set(geography["institutions"]), "Location roster must exactly match partners"
    def one(name):
        country, region, city, lat, lon, source = geography["institutions"][name]
        row = {"institution": name, "country": country, "region": region, "city_anchor": city,
               "latitude_approx": lat, "longitude_approx": lon, "coordinate_precision": "approximate_city_anchor_not_author_office",
               "source_url": "", "source_cache": "", "source_status": "pending"}
        if source == "publisher":
            found = [(d, a) for d in deposits.values() if d["status"] == "title_matched" for a in d["authors"]
                     if name in {piece[0] for raw in a["affiliations_raw"] for piece in institution_parts(raw)}]
            assert found, "No publisher address supports " + name
            # Prefer a deposit that actually names the selected anchor city.
            anchor_tokens = [x.strip().casefold() for x in city.split("(")[0].split("/")]
            found.sort(key=lambda item: (-any(token in " ".join(item[1]["affiliations_raw"]).casefold() for token in anchor_tokens), -len("; ".join(item[1]["affiliations_raw"]))))
            d, a = found[0]
            row.update(source_url=d["url"], source_cache=d["cache_file"], source_status="publisher_address_reviewed",
                       raw_evidence="; ".join(a["affiliations_raw"]))
        elif source == "paper":
            p = next(p for p in papers if name in p["partners"])
            row.update(source_url=p["paper_url"], source_status="country_only_in_affiliation_city_unresolved",
                       raw_evidence=name)
        else:
            row["source_url"] = source
            if not acquire and name in previous and previous[name]["source_url"] == source:
                return previous[name]
            cache = ROOT / "raw" / (hashlib.sha256(source.encode()).hexdigest()[:20] + ".html")
            try:
                if cache.exists() or acquire:
                    raw, info = fetch(source)
                    content = BeautifulSoup(raw, "html.parser").get_text(" ", strip=True)
                    row.update(source_cache=info["cache_file"], source_status="official_location_page_reviewed" if len(content) >= 80 else "official_page_empty_or_challenge")
                else:
                    row["source_status"] = "official_location_reference_not_cached"
            except Exception as exc:
                row.update(source_status="official_location_fetch_failed", source_error=str(exc))
            verified = geography.get("web_verified_addresses", {}).get(name)
            if verified and verified["source_url"] == source and row["source_status"] != "official_location_page_reviewed":
                row.update(source_status="official_location_verified_web_primary", raw_evidence=verified["address_excerpt"],
                           verification_method=verified["method"])
        return row
    with ThreadPoolExecutor(max_workers=4) as pool:
        rows = list(pool.map(one, institutions))
    for row in rows:
        verified = geography.get("web_verified_addresses", {}).get(row["institution"])
        if verified and verified["source_url"] == row["source_url"] and row["source_status"] != "official_location_page_reviewed":
            row.update(source_status="official_location_verified_web_primary", raw_evidence=verified["address_excerpt"], verification_method=verified["method"])
    save(history_path, {"checked_at": datetime.now(timezone.utc).isoformat(), "checks": rows})
    return rows


def aggregate(papers, topics, locations):
    lookup = {x["institution"]: x for x in locations}
    by_id = {p["paper_id"]: p for p in papers}
    n = len(papers)
    topic_rows = []
    for topic, meta in topics.items():
        observed = [p for p in papers if p["topic"] == topic]
        core_count = sum(p["scope_status"] == "included" for p in observed)
        topic_rows.append({"topic": topic, "label": meta["label"], "papers": len(observed), "share_percent": len(observed)/n*100,
            "networking_core_papers": core_count, "networking_core_share_percent": core_count/sum(p["scope_status"] == "included" for p in papers)*100,
            "academic_research_collaboration": sum(bool(p["partners"]) for p in observed),
            "tencent_only": sum(p["collaboration_type"] == "Tencent-only" for p in observed)})
    year_rows = [{"year": year, "topic": topic, "label": topics[topic]["label"],
                  "papers": sum(p["year"] == year and p["topic"] == topic for p in papers),
                  "year_total": sum(p["year"] == year for p in papers),
                  "period_status": "dated_2026_corpus_not_annualized" if year == 2026 else "observed_publication_cohort"}
                 for year in range(2019, 2027) for topic in topics]
    first = {name: min(p["year"] for p in papers if name in p["partners"]) for name in lookup}
    partner_rows, edges = [], []
    for name in lookup:
        observed = [p for p in papers if name in p["partners"]]
        partner_rows.append({**lookup[name], "paper_count": len(observed), "fractional_paper_credit": sum(1/len(p["partners"]) for p in observed),
            "first_observed_year": first[name], "last_observed_year": max(p["year"] for p in observed),
            "topic_count": len({p["topic"] for p in observed}),
            "topics": "; ".join(topics[t]["label"] for t in topics if any(p["topic"] == t for p in observed)),
            "paper_ids": "; ".join(p["paper_id"] for p in observed)})
        for p in observed:
            edges.append({"paper_id": p["paper_id"], "short": p["short"], "year": p["year"], "topic": p["topic"],
                          "institution": name, "country": lookup[name]["country"], "region": lookup[name]["region"],
                          "full_count": 1, "fractional_count": 1/len(p["partners"])})
    partner_rows.sort(key=lambda x: (-x["paper_count"], x["institution"]))
    country_rows = [{"country": country, "institutions": sum(x["country"] == country for x in locations),
                     "papers": len({e["paper_id"] for e in edges if e["country"] == country}),
                     "paper_share_percent": len({e["paper_id"] for e in edges if e["country"] == country})/n*100}
                    for country in sorted({x["country"] for x in locations})]
    region_year = []
    for year in range(2019, 2027):
        represented = {i for p in papers if p["year"] == year for i in p["partners"]}
        region_year.append({"year": year, "represented_institutions": len(represented),
            "newly_observed": sum(first[x] == year for x in represented), "returning": sum(first[x] < year for x in represented),
            "countries": "; ".join(sorted({lookup[i]["country"] for i in represented})),
            "papers_with_non_china_partner": sum(p["year"] == year and any(lookup[i]["country"] != "China" for i in p["partners"]) for p in papers)})
    tag_rows = [{"tag": tag, "papers": sum(tag in p["tags"] for p in papers),
                 "share_percent": sum(tag in p["tags"] for p in papers)/n*100}
                for tag in sorted({tag for p in papers for tag in p["tags"]})]
    return {"generated_at": datetime.now(timezone.utc).isoformat(), "paper_count": n,
        "networking_core_count": sum(p["scope_status"] == "included" for p in papers),
        "academic_research_papers": sum(bool(p["partners"]) for p in papers),
        "collaboration_counts": dict(Counter(p["collaboration_type"] for p in papers)),
        "explicit_ai_workload_papers": sum("AI workload" in p["tags"] for p in papers),
        "distinct_academic_research_institutions": len(lookup),
        "papers_with_non_china_partner": sum(any(lookup[i]["country"] != "China" for i in p["partners"]) for p in papers),
        "academic_research_paper_institution_edges": len(edges), "topic_partition": topic_rows,
        "year_topics": year_rows, "partners": partner_rows, "country_distribution": country_rows,
        "region_year": region_year, "secondary_tags": tag_rows, "edges": edges,
        "deployment_labels": dict(Counter(p["deployment"] for p in papers)),
        "first_author_classes": dict(Counter(p["first_author_class"] for p in papers)),
        "source_notes": "Descriptive selected-corpus statistics; topic shares use 32 papers; secondary tags/countries overlap; fractional credits sum to one per academically collaborative paper, not one across all papers."}


def write_csv(name, rows):
    path = OUT / ("analysis_" + name + ".csv")
    headers = list(dict.fromkeys(k for row in rows for k in row)) or ["status"]
    with path.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, headers, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def save_figure(fig, name):
    FIGURES.mkdir(exist_ok=True)
    fig.savefig(FIGURES / (name + ".svg"), bbox_inches="tight", metadata={"Date": None})
    fig.savefig(FIGURES / (name + ".png"), bbox_inches="tight", dpi=150)
    plt.close(fig)


def short_institution(name):
    return {"University of California, Santa Barbara": "UC Santa Barbara", "Massachusetts Institute of Technology": "MIT",
        "King Abdullah University of Science and Technology": "KAUST", "Computer Network Information Center, Chinese Academy of Sciences": "CNIC CAS",
        "Chinese University of Hong Kong, Shenzhen": "CUHK Shenzhen", "Hong Kong University of Science and Technology": "HKUST",
        "Beijing University of Posts and Telecommunications": "BUPT", "University of Chinese Academy of Sciences": "UCAS",
        "University of Science and Technology of China": "USTC", "National University of Singapore": "NUS",
        "Nanjing University of Science and Technology": "NJUST", "Queen Mary University of London": "Queen Mary London"}.get(name, name.replace("University", "Univ."))


def plots(results, papers, topics, world):
    rows = results["topic_partition"]
    fig, (ax, share) = plt.subplots(1, 2, figsize=(12, 5.2), gridspec_kw={"width_ratios": [1.7, 1]})
    y = np.arange(len(rows))
    ax.barh(y, [r["papers"] for r in rows], color=[topics[r["topic"]]["color"] for r in rows], height=.62)
    ax.set_yticks(y, [r["label"] for r in rows]); ax.invert_yaxis(); ax.set_xlim(0, 10); ax.set_xlabel("Papers · one primary topic per paper")
    for i, r in enumerate(rows): ax.text(r["papers"]+.15, i, f'{r["papers"]}  ·  {percent(r["share_percent"])}', va="center", fontsize=10)
    share.pie([r["papers"] for r in rows], colors=[topics[r["topic"]]["color"] for r in rows], startangle=90, counterclock=False, wedgeprops={"width": .27, "edgecolor": PAPER})
    share.text(0, .1, "32", ha="center", fontsize=38, weight="bold"); share.text(0, -.22, "primary papers", ha="center", fontsize=11)
    fig.tight_layout(); save_figure(fig, "topic_partition")

    fig, axes = plt.subplots(2, 1, figsize=(12, 7), sharex=True, gridspec_kw={"height_ratios": [1.25, 1]})
    years = np.arange(2019, 2027); bottom = np.zeros(8); pct_bottom = np.zeros(8)
    totals = np.array([sum(p["year"] == y for p in papers) for y in years])
    for t, meta in topics.items():
        values = np.array([sum(p["year"] == y and p["topic"] == t for p in papers) for y in years])
        axes[0].bar(years, values, bottom=bottom, color=meta["color"], width=.65, label=meta["label"]); bottom += values
        pct = np.divide(values*100, totals, out=np.zeros(8), where=totals > 0)
        axes[1].bar(years, pct, bottom=pct_bottom, color=meta["color"], width=.65); pct_bottom += pct
    for y, total in zip(years, totals):
        axes[0].text(y, total+.3, str(total) if total else "none\nobserved", ha="center", fontsize=9)
    axes[0].set_ylim(0, max(totals)+3); axes[0].set_ylabel("Observed papers"); axes[1].set_ylabel("Within-year share (%)")
    axes[1].set_xticks(years, [str(y) + ("*" if y == 2026 else "") for y in years]); axes[1].set_xlabel("Publication year · *2026 dated corpus; no annualization")
    axes[0].legend(loc="upper left", ncol=2, frameon=False, fontsize=8)
    for ax in axes: ax.axvspan(2025.55, 2026.45, color="#dfe8ec", alpha=.35, zorder=0)
    fig.tight_layout(); save_figure(fig, "topic_evolution")

    fig, ax = plt.subplots(figsize=(12, 4.5))
    y = np.arange(len(rows)); academic = [r["academic_research_collaboration"] for r in rows]; solo = [r["tencent_only"] for r in rows]
    ax.barh(y, academic, color="#137f83", label="Academic/research institution represented")
    ax.barh(y, solo, left=academic, color="#d47c38", label="Tencent-only")
    ax.set_yticks(y, [r["label"] for r in rows]); ax.invert_yaxis(); ax.set_xlabel("Paper count · dual affiliations count as institutional presence")
    ax.legend(loc="lower right", frameon=False, fontsize=9); ax.set_xlim(0, 10)
    fig.tight_layout(); save_figure(fig, "collaboration_types")

    top = results["partners"][:15]
    fig, axes = plt.subplots(1, 2, figsize=(12, 6.2), gridspec_kw={"width_ratios": [1, 1.25]})
    axes[0].barh(np.arange(len(top)), [r["paper_count"] for r in top], color="#137f83", height=.65)
    axes[0].set_yticks(np.arange(len(top)), [short_institution(r["institution"]) for r in top]); axes[0].invert_yaxis(); axes[0].set_xlabel("Full paper–institution counts")
    for i, r in enumerate(top): axes[0].text(r["paper_count"]+.15, i, str(r["paper_count"]), va="center", fontsize=9)
    axes[0].set_xlim(0, max(r["paper_count"] for r in top)+2)
    matrix = np.array([[sum(p["topic"] == t and r["institution"] in p["partners"] for p in papers) for t in topics] for r in top])
    axes[1].imshow(matrix, cmap="GnBu", aspect="auto", vmin=0, vmax=max(1, matrix.max()))
    axes[1].set_yticks(np.arange(len(top)), [short_institution(r["institution"]) for r in top])
    axes[1].set_xticks(np.arange(len(topics)), ["DCN / AI", "Gateways", "QoE", "WAN", "Operations", "Security", "Resources"], rotation=40, ha="right")
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            if matrix[i,j]: axes[1].text(j, i, str(matrix[i,j]), ha="center", va="center", color="white" if matrix[i,j] > matrix.max()/2 else INK, fontsize=9)
    fig.tight_layout(); save_figure(fig, "partner_matrix")

    fig, axes = plt.subplots(1, 2, figsize=(12, 5.2), gridspec_kw={"width_ratios": [1.6, 1]})
    city = defaultdict(list)
    for row in results["partners"]:
        if row["latitude_approx"] is not None: city[(row["longitude_approx"], row["latitude_approx"])].append(row)
    for ax in axes:
        for feature in world["features"]:
            geometry = feature["geometry"]; polygons = geometry["coordinates"] if geometry["type"] == "MultiPolygon" else [geometry["coordinates"]]
            for polygon in polygons:
                coords = polygon[0]
                ax.add_patch(Polygon(coords, facecolor="#e4e9e6", edgecolor="#b9c6c5", linewidth=.35, zorder=0))
        for (lon, lat), items in city.items():
            count = len(items)
            ax.scatter(lon, lat, s=45*count, color="#137f83", edgecolor="white", linewidth=.9, alpha=.8, zorder=3)
        ax.set_facecolor("#f0f5f5"); ax.grid(alpha=.15); ax.set_xlabel("Longitude"); ax.set_ylabel("Latitude")
    axes[0].set_xlim(-130, 150); axes[0].set_ylim(-8, 68); axes[0].set_title("Global institutional anchors", loc="left", fontsize=11)
    axes[1].set_xlim(100, 126); axes[1].set_ylim(18, 43); axes[1].set_title("Mainland China / Hong Kong detail", loc="left", fontsize=11)
    labels = {"Beijing": (-55, 12), "Beijing (parent anchor)": (-80, 15), "Nanjing": (10, 12), "Shanghai": (-60, -8), "Hong Kong": (-65, -24), "Shenzhen": (-70, 6), "Xi'an": (-20, 8), "Wuhan": (-65, -8), "Hangzhou": (4, -20), "Xiamen": (8, -5), "Jinan": (6, 4), "Hefei (Hefei/Suzhou affiliations)": (-45, 25)}
    for (lon, lat), items in city.items():
        label = "Beijing" if lon == 116.4 else items[0]["city_anchor"]
        if 100 <= lon <= 124 and 18 <= lat <= 43:
            dx, dy = labels.get(label, (5, 5))
            axes[1].annotate(label.replace(" (Hefei/Suzhou affiliations)", "").replace(" (parent anchor)", " / Tsinghua"), (lon, lat), xytext=(dx, dy), textcoords="offset points", fontsize=7, arrowprops={"arrowstyle": "-", "lw": .5, "color": MUTED})
    handles = [axes[0].scatter([], [], s=45*n, color="#137f83", alpha=.8, edgecolor="white", label=f'{n} institution' + ('s' if n != 1 else '')) for n in [1, 3, 6]]
    axes[0].legend(handles=handles, loc="lower left", frameon=True, fontsize=7, facecolor=PAPER)
    fig.tight_layout(); save_figure(fig, "partner_geography")

    fig, axes = plt.subplots(1, 2, figsize=(12, 4.4))
    ry = results["region_year"]
    axes[0].bar([r["year"] for r in ry], [r["returning"] for r in ry], color="#137f83", label="Previously observed institution")
    axes[0].bar([r["year"] for r in ry], [r["newly_observed"] for r in ry], bottom=[r["returning"] for r in ry], color="#a4c7c0", label="First observed in this corpus")
    axes[0].set_ylabel("Distinct institutions represented that year"); axes[0].legend(frameon=False, fontsize=8); axes[0].set_xticks(years, [str(y) + ("*" if y == 2026 else "") for y in years], rotation=35)
    c = sorted(results["country_distribution"], key=lambda x: -x["papers"])
    axes[1].barh(np.arange(len(c)), [r["papers"] for r in c], color="#3868b2")
    axes[1].set_yticks(np.arange(len(c)), [r["country"] for r in c]); axes[1].invert_yaxis(); axes[1].set_xlabel("Papers with ≥1 institution in location\nOverlapping counts, not a partition")
    for i, r in enumerate(c): axes[1].text(r["papers"]+.2, i, str(r["papers"]), va="center", fontsize=9)
    axes[1].set_xlim(0, max(r["papers"] for r in c)+3)
    fig.tight_layout(); save_figure(fig, "geography_evolution")

    fig, ax = plt.subplots(figsize=(12, 5.1)); ax.set_xlim(0, 12); ax.set_ylim(0, 5.3); ax.axis("off")
    layers = [
        (4.2, "Workloads & experience", "AFR / LADR · interactive QoE    |    SwiftEP / Holmes · AI efficiency", "rtc_qoe"),
        (3.2, "Control & reliability", "DSR / TENSOR / Janus    |    MegaTE / PreTE    |    P-ECMP / Harp", "cloud_gateway"),
        (2.2, "Offload & transport", "Elixir / Fornax / Dorado / XFir    |    DistDPU / Pegasus", "dcn_ai"),
        (1.2, "Physical bottlenecks", "OpTel / FlexWAN · optics    |    BLADE · Wi-Fi contention", "wan"),
        (.2, "Observe, replay, diagnose", "Looking Glass / MirSwitch / MirrorNet / CubeTrace", "operations")]
    for y0, label, body, t in layers:
        ax.add_patch(FancyBboxPatch((.05, y0), 11.8, .82, boxstyle="round,pad=.02,rounding_size=.07", linewidth=0, facecolor=topics[t]["color"], alpha=.10))
        ax.text(.25, y0+.48, label, fontsize=11, weight="bold", color=topics[t]["color"])
        ax.text(3.25, y0+.4, body, fontsize=9, va="center")
    save_figure(fig, "technology_stack")


def figure(name, title, caption):
    svg = (FIGURES / (name + ".svg")).read_text()
    svg = svg[svg.index("<svg"):]
    # Matplotlib's figure/axes IDs repeat across standalone SVGs. Prefix every
    # ID and reference before embedding so one figure cannot clip another.
    svg = re.sub(r'\bid="([^"]+)"', lambda m: 'id="' + name + '-' + m[1] + '"', svg)
    svg = svg.replace('url(#', 'url(#' + name + '-').replace('href="#', 'href="#' + name + '-')
    svg = svg.replace("<svg ", f'<svg role="img" aria-label="{html.escape(title, quote=True)}" ', 1)
    return f'<figure id="fig-{name}"><div class="figure-title">{html.escape(title)}</div><div class="chart-hint">Scroll the figure horizontally on a narrow screen.</div><div class="chart-scroll" tabindex="0" role="group" aria-label="{html.escape(title, quote=True)}">{svg}</div><figcaption>{html.escape(caption)}</figcaption></figure>'


def table(headers, rows, cls=""):
    return '<div class="table-wrap"><table class="' + cls + '"><thead><tr>' + ''.join('<th scope="col">'+html.escape(str(h))+'</th>' for h in headers) + '</tr></thead><tbody>' + ''.join('<tr>'+''.join('<td>'+str(x)+'</td>' for x in row)+'</tr>' for row in rows) + '</tbody></table></div>'


def render(results, papers, topics, content, geography):
    by_short = {p["short"]: p for p in papers}
    def cite(short):
        p = by_short[short]
        return f'<a class="paper-ref" href="#paper-{p["paper_id"]}">{html.escape(short)} {p["year"]}</a>'
    n, partners = results["paper_count"], results["distinct_academic_research_institutions"]
    academic = results["academic_research_papers"]
    nav = [("overview", "Overview"), ("topics", "Topics & evolution"), ("connections", "Connections & geography"), ("deepdives", "Topic deep dives"), ("outlook", "Implications & questions"), ("methods", "Methods"), ("evidence", "Paper evidence")]
    body = f'''<header class="hero"><div class="eyebrow">RESEARCH PORTFOLIO / 2019–2026</div><h1>{html.escape(content['title'])}</h1><p class="subtitle">{html.escape(content['subtitle'])}</p><div class="hero-meta">Analysis snapshot · 15 October 2026 &nbsp; / &nbsp; Corpus metadata checked · 14 October 2026<br>NSDI · SIGCOMM · CoNEXT/PACMNET · IMC · HotNets</div></header>
    <div class="report-shell"><nav aria-label="Report sections"><div class="nav-title">IN THIS REPORT</div>{''.join(f'<a href="#{k}">{v}</a>' for k,v in nav)}<a href="tencent_networking_metadata.xlsx">Metadata workbook ↗</a><a href="../ANALYSIS_PLAN.md">Analysis plan ↗</a></nav><main id="main">
    <section id="overview"><div class="section-number">01 / OVERVIEW</div><h2>A portfolio built around operational bottlenecks</h2>
    <div class="stats"><div><strong>{n}</strong><span>reviewed primary papers</span></div><div><strong>{partners}</strong><span>academic/research institutions</span></div><div><strong>{academic}/{n}</strong><span>academic/research coauthorship</span></div><div><strong>{results['explicit_ai_workload_papers']}</strong><span>explicit AI-workload papers</span></div></div>
    <p class="lead">The strongest unifying theme is not a single protocol. It is the repeated conversion of production bottlenecks into programmable, measurable and more resource-efficient systems—from cloud gateways and optical backbones to interactive streaming and AI infrastructure.</p>
    <div class="callout"><strong>Read the denominator correctly.</strong> This is a selected, user-reviewed publication corpus, not all Tencent networking research. It includes one cloud-resource boundary paper; the networking-core sensitivity view has 31 papers. Two posters are excluded from headline counts. Observed zeros in 2019/2020 are not proven zero output; 2026 is a dated corpus, not a complete annual total.</div>
    <div class="insight-grid"><article><h3>Academic presence is the norm</h3><p>{academic/n:.1%} of the papers list an academic/research institution. Only {cite('LADR')} is Tencent-only. This describes published authorship, not the proportion of Tencent's internal R&amp;D done with universities.</p></article><article><h3>AI arrives as a stack problem</h3><p>{cite('Holmes')}, {cite('Astral')}, {cite('SwiftEP')}, {cite('DistDPU')} and {cite('Pegasus')} connect observability, communication, virtualization and physical infrastructure. General datacenter work is not automatically counted as AI.</p></article><article><h3>Operational leverage, not a proven moat</h3><p>Reported cost, latency and reliability gains suggest plausible competitive mechanisms. The corpus does not establish comparative market share, causal revenue gains or an independently audited advantage over competitors.</p></article></div></section>
    <section id="topics"><div class="section-number">02 / WHAT IS BEING RESEARCHED</div><h2>A broad systems portfolio, with a recent AI layer</h2>'''
    body += figure("topic_partition", "Topic partition · 32 papers, one primary assignment each", "Shares sum to 100% before rounding. Mechanism/workload tags overlap and are shown separately. Hestia is the single gray boundary paper.")
    body += table(["Primary topic", "Papers", "Share / 32", "Core sensitivity / 31", "Academic / research", "Tencent-only"],
                  [[html.escape(r["label"]), r["papers"], percent(r["share_percent"]), f'{r["networking_core_papers"]} · {percent(r["networking_core_share_percent"])}', r["academic_research_collaboration"], r["tencent_only"]] for r in results["topic_partition"]])
    body += figure("topic_evolution", "Publication cohorts · volume and composition", "Publication year is not project start or deployment date. Larger recent cohorts can reflect disclosure and venue timing as well as research activity; no growth rate or 2026 annual projection is inferred.")
    ai_year = [(y, sum(p["year"] == y and "AI workload" in p["tags"] for p in papers), sum(p["year"] == y for p in papers)) for y in [2024, 2025, 2026]]
    body += '<p><strong>The mix is not a monotonic AI takeover.</strong> Explicit AI-workload papers are ' + ', '.join(f'{a}/{total} in {y}' for y,a,total in ai_year) + '. Turbo is a data-analytics communication paper, while P-ECMP and Harp are general datacenter work. Those distinctions prevent inflated AI counts.</p>'
    body += figure("collaboration_types", "Academic collaboration versus Tencent-only research", "Academic/research presence includes dual affiliations and research laboratories. Other-industry-only collaboration is zero in this selected primary corpus. Tencent-only is an authorship classification, not evidence that no external ideas or tools were used.")
    tags = sorted(results["secondary_tags"], key=lambda r: -r["papers"])[:12]
    body += '<details><summary>Overlapping technology/workload tags and counting rules</summary>' + table(["Secondary tag", "Papers", "Share / 32"], [[html.escape(r["tag"]), r["papers"], percent(r["share_percent"])] for r in tags]) + '<p>These percentages are not a partition and must not be added. Primary-topic classifications were reviewed from full collected abstracts, not generated from title keywords alone.</p></details></section>'
    body += '<section id="connections"><div class="section-number">03 / WHO WORKS WITH WHOM</div><h2>A China-centered network with recurring international links</h2>'
    body += figure("partner_matrix", "Partner recurrence and topic breadth · top 15 institutions", "One count per paper–institution pair, regardless of the number of coauthors or dual-affiliation rows. Rankings are full counts; fractional credits are available below and in the CSV. This is institutional coauthorship, not contracts or funding.")
    body += figure("partner_geography", "Where the represented institutions are located", "Bubble area scales with the number of represented institutions at an approximate city anchor, not publication volume. Nearby anchors may overlap. One country-only institute is unmapped; NJUST's city anchor remains provisional because its official page is empty to the collector. Tsinghua and USTC use parent anchors despite multiple campuses. Boundaries: public-domain Natural Earth; no author nationality or mobility is mapped.")
    body += figure("geography_evolution", "How the observed institutional footprint changes", "First observed means first appearance in this selected corpus, not the start of a real-world partnership. Countries overlap within papers. Hong Kong is a separate region within China in the geography data, not counted as a separate country here.")
    body += f'<p><strong>{results["papers_with_non_china_partner"]}/{n} papers</strong> include at least one institution located outside China. This is a coauthorship footprint, not the nationality of researchers. Repeated affiliations can also follow one researcher across institution combinations; the two explanations cannot be separated by this dataset alone.</p>'
    leaders = results["partners"][:3]
    body += '<p><strong>The recurrent institutional anchors are ' + ', '.join(html.escape(r["institution"]) + f' ({r["paper_count"]} papers)' for r in leaders) + '.</strong> The European footprint comes from Astral alone (Politecnico di Milano and Queen Mary); NUS appears on five 2026 papers. These are observed portfolio connections, not evidence that an entirely new partnership started in that year.</p>'
    body += '<h3>Researcher cohorts: useful lenses, not formal organizations</h3><p>The following cohorts are analyst-curated, overlapping thematic groupings. Recurrence refers to name strings on papers; common names are not globally merged into verified researcher identities.</p><div class="cohorts">'
    raw_authors = metadata_tables(build_tables())["Author_Affiliations"]
    for cohort in content["cohorts"]:
        roster = []
        for name in cohort["people"]:
            count = len({a["paper_id"] for a in raw_authors if a["author_name"] == name})
            assert count, "Cohort name absent from corpus: " + name
            roster.append(f'{html.escape(name)} <span class="muted">({count})</span>')
        body += f'<article><h4>{html.escape(cohort["name"])}</h4><p>{html.escape(cohort["reading"])}</p><p class="roster">' + ' · '.join(roster) + '</p><p>' + ' '.join(cite(s) for s in cohort["papers"]) + '</p></article>'
    body += '</div><h3>What can actually be said about academic roles?</h3><p>Institutional presence is strong evidence of coauthorship but weak evidence of task ownership. Retrieved PDFs provide a few more concrete observations: explicit internships, dual affiliations, equal-contribution markers and corresponding-author credits. These support hands-on participation and shared credited authorship—not a blanket “universities do theory, Tencent does engineering” story.</p>'
    role_evidence = json.loads((ROOT / "data/analysis_role_evidence.json").read_text())["checks"]
    body += table(["Paper", "Explicitly credited relationship", "Evidence"], [[cite(r["paper"]), html.escape(r["claim"]), f'<a href="{html.escape(r["source_url"], quote=True)}">PDF ↗</a> · {html.escape(r["evidence"])}'] for r in role_evidence])
    body += '<details><summary>First-author affiliation structure (position is not leadership)</summary>' + table(["First-author affiliation category", "Papers"], [[html.escape(k), v] for k,v in results["first_author_classes"].items()]) + '<p class="small">The categories are mutually exclusive and include all 32 first-author positions. They describe affiliations only; equal contribution and corresponding authorship can differ from the first-listed position.</p></details>'
    body += '<h3>Observed affiliation combinations—not career histories</h3>'
    trajectory_rows = []
    for name in ["Congcong Miao", "Yunming Xiao", "Zili Meng", "Heng Yu"]:
        years = []
        for year in range(2021, 2027):
            affiliated = sorted({a["institution"] for a in raw_authors if a["author_name"] == name and a["year"] == year and a["institution"]})
            if affiliated: years.append(f'<strong>{year}</strong>: ' + html.escape(', '.join(short_institution(i) for i in affiliated)))
        trajectory_rows.append([html.escape(name), '<br>'.join(years)])
    body += table(["Recurring name", "Affiliations appearing on this corpus's papers"], trajectory_rows)
    body += '<p class="small">A year can contain different combinations, dual appointments or program discrepancies. These observations do not establish a move date, employment relationship or absence of Tencent collaboration after an affiliation changes.</p>'
    body += '<details><summary>All represented academic/research institutions, locations and fractional credit</summary>' + table(["Institution", "Location", "Papers", "Fractional credit", "Observed years", "Location evidence"],
        [[html.escape(r["institution"]), html.escape(r["region"]), r["paper_count"], f'{r["fractional_paper_credit"]:.2f}', f'{r["first_observed_year"]}–{r["last_observed_year"]}', f'<a href="{html.escape(r["source_url"], quote=True)}">Source ↗</a> · {html.escape(r["source_status"])}'] for r in results["partners"]]) + '</details></section>'
    body += '<section id="deepdives"><div class="section-number">04 / TOPIC DEEP DIVES</div><h2>Follow the bottleneck, then ask what it changes</h2>'
    body += figure("technology_stack", "Technology-stack lens · an analytical alignment", "Rows group where mechanisms act. Horizontal proximity and vertical ordering do not establish production integration, direct dependency or a common codebase. Some papers span multiple layers; this diagram is a synthesis, not Tencent's published architecture.")
    for index, dive in enumerate(content["deepdives"], 1):
        row = next(r for r in results["topic_partition"] if r["topic"] == dive["topic"])
        body += f'<article class="deepdive" id="topic-{dive["topic"]}" style="--topic-color:{topics[dive["topic"]]["color"]}"><div class="topic-kicker">{row["papers"]} papers · {percent(row["share_percent"])} of selected portfolio</div><h3>{html.escape(dive["heading"])}</h3><p class="thesis">{html.escape(dive["thesis"])}</p>'
        for sequence in dive["sequences"]:
            body += '<div class="paper-sequence">' + '<span class="arrow" aria-hidden="true">→</span>'.join(cite(s) for s in sequence) + '</div>'
        body += f'<div class="two-col"><div><h4>Academic connections and their evidenced role</h4><p>{html.escape(dive["partners"])}</p><h4>Plausible operational leverage</h4><p>{html.escape(dive["leverage"])}</p></div><div><h4>What the evidence does not establish</h4><p>{html.escape(dive["limits"])}</p><h4>Next research question <span class="badge hypothesis">Hypothesis</span></h4><p>{html.escape(dive["future"])}</p></div></div>'
        observed = [p for p in papers if p["topic"] == dive["topic"]]
        body += '<details><summary>Paper mechanisms and evidence settings · full results in the linked appendix</summary>' + table(["Paper", "Mechanism", "Evidence setting"],
            [[cite(p["short"]), html.escape(p["mechanism"]), html.escape(p["deployment"].replace('_', ' '))] for p in observed]) + '</details></article>'
    body += '</section><section id="outlook"><div class="section-number">05 / IMPLICATIONS AND NEXT INVESTIGATIONS</div><h2>Potential advantage: an operational learning loop</h2><p class="lead">The defensible synthesis is a capability pattern: production access reveals a bottleneck; systems research proposes a more programmable or efficient abstraction; measurements and deployments feed the next iteration. The papers support pieces of that pattern, not a measured causal moat.</p>'
    body += '<div class="insight-grid"><article><h3>Cost / useful work</h3><p>Optical capacity, commodity DDR, hardware-centric management and GPU data movement all target over-provisioning. Report the specific denominator; never multiply heterogeneous savings.</p></article><article><h3>Experience / resilience</h3><p>Client queues, loss sources, path failures and optical degradation require different control loops. Better latency or detection does not directly demonstrate customer retention or avoided financial loss.</p></article><article><h3>Iteration speed</h3><p>Tracing and emulation may reduce the cost of understanding a heterogeneous production stack. This is a plausible organizational capability, not a paper-count measure of engineering productivity.</p></article></div>'
    body += table(["Unanswered question", "What remains unknown", "Next investigation"], [[html.escape(x) for x in row] for row in content["open_questions"]])
    body += '</section><section id="methods"><div class="section-number">06 / METHODS AND LIMITS</div><h2>What was counted—and what was not inferred</h2><ol><li><strong>Scope.</strong> 32 reviewed primary papers, 2019–2026, selected from five venues. 31 are in the networking core; Hestia remains a boundary candidate. The two posters are separate in the workbook and excluded here.</li><li><strong>Taxonomy.</strong> One primary topic per paper. Mechanism and workload tags overlap. Classifications are analyst judgments reviewed against full abstracts, not publisher keywords or inferred corporate priorities.</li><li><strong>Coauthorship.</strong> Institution counts deduplicate author positions and joint-affiliation rows within each paper. Academic and research institutes are grouped for the headline, but industry partners and explicit unaffiliated authors are not silently relabeled as universities.</li><li><strong>Full and fractional counts.</strong> Each paper–institution edge has full weight 1. A paper with k academic/research partners gives each 1/k; Tencent-only papers have no academic edge. Fractional academic credits therefore sum to 31, not 32. No citation weighting is applied.</li><li><strong>Identity and roles.</strong> Author positions are preserved. Name recurrence does not establish person identity, leadership, funding or the division of intellectual/engineering labor.</li><li><strong>Geography.</strong> Publication-time institution assignments are used, with publisher/official institutional location evidence. Map coordinates are approximate city anchors; parent normalization hides campus detail. One institute has an unresolved city. Location is not nationality.</li><li><strong>Results.</strong> Metrics are author-reported and not independently reproduced. Production, prototype, simulation and experimental objective values are labeled separately. Results with different baselines, workloads or resources are not pooled into a universal score.</li><li><strong>Evidence quality.</strong> Author mappings are PDF-reviewed for 27 primary papers and publisher-deposit-reviewed for five. All 32 have complete sourced abstracts. Implementation/role claims for the five missing final PDFs remain limited. Dorado and Holmes source discrepancies remain documented.</li></ol>'
    body += '<h3>Sensitivity and audit trail</h3><p>Removing Hestia leaves 31 networking-core papers and removes the only USTC tie. Replacing Dorado’s three conflicting publisher assignments with final-program assignments would replace that paper’s UCAS presence with Zhongguancun Laboratory and move Heng Yu’s affiliation from Tsinghua to Zhongguancun; other coauthors still retain Tsinghua on Dorado. This changes institutional attribution, not the paper total or its China/international footprint.</p>'
    body += '<p class="small">Normalization correction in this analysis: “School of Computer Science and Technology” is a department within the USTC affiliation, not a separate institution. CityU Hong Kong, University of Hong Kong, CUHK and CUHK Shenzhen are not merged. Joint university/laboratory assignments remain visible in raw metadata.</p>'
    body += '<div class="downloads"><a href="tencent_networking_metadata.xlsx">Clean metadata workbook</a><a href="tencent_networking_publications.xlsx">Full audit workbook</a><a href="analysis_topic_partition.csv">Topic chart data</a><a href="analysis_partners.csv">Partner/location data</a><a href="analysis_paper_evidence.csv">Paper evidence annotations</a><a href="../data/analysis_results.json">All aggregates (JSON)</a></div></section>'
    body += '<section id="evidence"><div class="section-number">07 / PAPER-LEVEL EVIDENCE</div><h2>Inspect the papers behind the story</h2><p>Filter by title, year, topic, researcher name or institution. Each card separates the reported mechanism/result from the analyst interpretation. Follow the original source for the full evaluation and assumptions.</p><label for="paper-search">Search the 32-paper evidence appendix</label><input id="paper-search" type="search" placeholder="Try: MoE, 2026, Tsinghua, cloud gaming…"><p id="search-count" aria-live="polite">32 papers shown</p><div class="paper-cards">'
    for p in papers:
        search = ' '.join([p["title"], str(p["year"]), p["short"], topics[p["topic"]]["label"], p["authors_ordered"], '; '.join(p["partners"]), '; '.join(p["tags"])])
        body += f'<article class="paper-card" id="paper-{p["paper_id"]}" data-search="{html.escape(search.casefold(), quote=True)}"><div class="paper-card-meta">{p["venue"]} {p["year"]} · {html.escape(topics[p["topic"]]["label"])}</div><h3>{html.escape(p["title"])}</h3><p><strong>Mechanism.</strong> {html.escape(p["mechanism"])}</p><p><strong>Reported result.</strong> {html.escape(p["result"])}</p><p><strong>Evaluation context.</strong> {html.escape(p["evaluation"])}</p><p><strong>Analyst interpretation.</strong> {html.escape(p["implication"])}</p><p class="small"><strong>Academic/research institutions:</strong> {html.escape("; ".join(p["partners"]) or "None listed (Tencent-only)")}</p><p class="small"><strong>Other industry:</strong> {html.escape("; ".join(p["industry_partners"]) or "None listed")}</p><details><summary>Ordered author list and metadata caveats</summary><p class="small">{html.escape(p["authors_ordered"])}</p><p class="small">{html.escape(p["metadata_notes"] or "No additional source discrepancy recorded.")}</p></details><div class="paper-links"><a href="{html.escape(p["paper_url"], quote=True)}">Paper / DOI ↗</a><a href="{html.escape(p["abstract_source"], quote=True)}">Result source ↗</a>'
        if p["pdf_url"]: body += f'<a href="{html.escape(p["pdf_url"], quote=True)}">PDF link ↗</a>'
        body += f'<span class="badge">{html.escape(p["affiliation_status"].replace("_", " "))}</span></div></article>'
    body += '</div></section><footer>Prepared by Shiye · Project analysis, not a Tencent statement. Built from reviewed metadata and auditable annotations. No external JavaScript, fonts or chart services are required. Natural Earth base-map data is public domain.</footer></main></div>'
    css = (ROOT / "scripts/report_style.css").read_text()
    script = """const search=document.querySelector('#paper-search');const cards=[...document.querySelectorAll('.paper-card')];search.addEventListener('input',()=>{let n=0;for(const card of cards){const show=card.dataset.search.includes(search.value.toLocaleLowerCase().trim());card.hidden=!show;if(show)n++;}document.querySelector('#search-count').textContent=n+' papers shown';});document.querySelectorAll('a[href^="#paper-"]').forEach(a=>a.addEventListener('click',()=>{search.value='';cards.forEach(c=>c.hidden=false);document.querySelector('#search-count').textContent=cards.length+' papers shown';}));"""
    return f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="description" content="Evidence-led analysis of Tencent networking publications, topics, academic connections and research evolution."><title>{html.escape(content["title"])}</title><style>{css}</style></head><body><a class="skip-link" href="#main">Skip to report</a>{body}<script>{script}</script></body></html>'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--acquire-geography-sources", action="store_true")
    args = parser.parse_args()
    tables, topics, content, geography, papers = load_inputs()
    locations = geography_rows(tables, geography, papers, args.acquire_geography_sources)
    results = aggregate(papers, topics, locations)
    raw, info = fetch(WORLD_URL)
    world = json.loads(raw)
    results["map_source"] = {**info, "license": "Natural Earth public domain", "license_url": "https://www.naturalearthdata.com/about/terms-of-use/"}
    save(ROOT / "data/analysis_results.json", results)
    for name in ["topic_partition", "year_topics", "partners", "country_distribution", "region_year", "secondary_tags", "edges"]:
        write_csv(name, results[name])
    write_csv("paper_evidence", [{k:p[k] for k in ["paper_id", "short", "title", "year", "topic", "mechanism", "result", "evaluation", "deployment", "implication", "abstract_source", "collaboration_type", "first_author_name", "first_author_class", "first_author_institutions"]} for p in papers])
    plots(results, papers, topics, world)
    report = render(results, papers, topics, content, geography)
    (OUT / "tencent_networking_report.html").write_text(report)
    print(json.dumps({"report": "output/tencent_networking_report.html", "papers": len(papers),
        "topic_partition": results["topic_partition"], "collaboration": results["collaboration_counts"],
        "partner_institutions": len(locations), "country_distribution": results["country_distribution"],
        "location_evidence_status": dict(Counter(r["source_status"] for r in locations))}, indent=2))


if __name__ == "__main__":
    main()
