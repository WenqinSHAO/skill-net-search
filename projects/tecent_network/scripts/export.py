#!/usr/bin/env python3
"""Generate auditable Excel and CSV tables, without Excel-library dependencies."""
from __future__ import annotations

import csv
import hashlib
import json
import re
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from xml.etree import ElementTree as ET
from zipfile import ZIP_DEFLATED, ZipFile

ROOT = Path(__file__).resolve().parents[1]
NS = "http://schemas.openxmlformats.org/spreadsheetml/2006/main"
REL = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
PACKAGE_REL = "http://schemas.openxmlformats.org/package/2006/relationships"
TAXONOMY = {
    "DCN": ("datacenter", "data center", "data-center", "rdma", "ecmp", "dcn", "gpu cluster", "switch"),
    "AI_infrastructure": ("llm", "training", "inference", "gpu", "machine learning", "deep learning", "collective"),
    "WAN_optical": ("wan", "wide area", "wide-area", "optical", "backbone", "traffic engineering"),
    "transport_congestion": ("transport", "congestion", "tcp", "multipath", "packet loss"),
    "routing_control": ("routing", "bgp", "router", "control plane", "sdn"),
    "cloud_virtualization": ("vpc", "virtual", "public cloud", "cloud network", "session management"),
    "measurement_reliability": ("telemetry", "monitor", "diagnos", "detect", "failure", "reliab", "irregular", "measurement", "availability"),
    "edge_CDN_media": ("cdn", "edge", "video", "streaming", "real time", "real-time", "communication quality", "gaming"),
    "wireless_mobile": ("mobile", "wireless", "wifi", "wi-fi", "cellular", "wlan"),
    "network_security": ("hijack", "ddos", "security", "attack", "encryption"),
    "programmability_offload": ("programmab", "offload", "packet processing", "nic", "hardware centric", "hardware-centric"),
}

# Matching aliases are a normalization aid; raw strings and review status are retained.
INSTITUTIONS = {
    "Tencent": ["tencent", "腾讯"],
    "Meta": ["meta"],
    "NVIDIA": ["nvidia"],
    "Bonree": ["bonree", "bonree technology", "bonree inc."],
    "JaguarMicro": ["jaguarmicro"],
    "CETC": ["cetc", "cetcsc"],
    "Harvard University": ["harvard university"],
    "Queen Mary University of London": ["queen mary university of london"],
    "City University of Hong Kong": ["city university of hong kong"],
    "Wuhan University": ["wuhan university"],
    "Zhejiang University": ["zhejiang university"],
    "Xiamen University": ["xiamen university"],
    "Columbia University": ["columbia university"],
    "University of Chinese Academy of Sciences": ["university of chinese academy of sciences"],
    "Hong Kong Polytechnic University": ["the hong kong polytechnic university", "hong kong polytechnic university"],
    "Institute of Artificial Intelligence, China": ["institute of artificial intelligence, china"],
    "Peng Cheng Laboratory": ["peng cheng laboratory"],
    "Renmin University of China": ["renmin university of china"],
    "University of Minnesota Duluth": ["university of minnesota duluth"],
    "Tsinghua University": ["tsinghua university", "tsinghua shenzhen international graduate school", "tsinghua"],
    "Peking University": ["peking university", "key laboratory of high confidence software technologies, ministry of education (pku)"],
    "Nanjing University": ["nanjing university"],
    "Nanjing University of Science and Technology": ["nanjing university of science and technology"],
    "Beijing University of Posts and Telecommunications": ["beijing university of posts and telecommunications", "bupt"],
    "Politecnico di Milano": ["politecnico di milano"],
    "University of Texas at Austin": ["university of texas at austin", "ut austin"],
    "Computer Network Information Center, Chinese Academy of Sciences": ["cnic cas", "computer network information center"],
    "Fudan University": ["fudan university"],
    "Shanghai Jiao Tong University": ["shanghai jiao tong university", "shanghai jiaotong university"],
    "Xi'an Jiaotong University": ["xi'an jiaotong university", "xi’an jiaotong university"],
    "University of Science and Technology of China": ["university of science and technology of china"],
    "Hong Kong University of Science and Technology": ["hong kong university of science and technology", "hkust"],
    "Chinese University of Hong Kong": ["chinese university of hong kong", "cuhk"],
    "Chinese University of Hong Kong, Shenzhen": ["the chinese university of hong kong, shenzhen", "chinese university of hong kong, shenzhen", "the chinese universities of hong kong, shenzhen"],
    "University of Hong Kong": ["university of hong kong"],
    "Massachusetts Institute of Technology": ["massachusetts institute of technology", "mit"],
    "Northwestern University": ["northwestern university"],
    "University of Michigan": ["university of michigan"],
    "University of Chicago": ["university of chicago"],
    "University of California, Santa Barbara": ["university of california, santa barbara", "uc santa barbara", "ucsb"],
    "University at Buffalo": ["university at buffalo", "suny buffalo"],
    "Duke University": ["duke university"],
    "Carnegie Mellon University": ["carnegie mellon university"],
    "King Abdullah University of Science and Technology": ["king abdullah university of science and technology", "kaust"],
    "National University of Singapore": ["national university of singapore", "nus"],
    "Nanyang Technological University": ["nanyang technological university", "ntu"],
    "Zhongguancun Laboratory": ["zhongguancun laboratory"],
    "Quancheng Laboratory": ["quancheng laboratory"],
}


def norm(value):
    return re.sub(r"[^\w]+", " ", value.casefold()).strip()


def institution_parts(raw):
    if re.fullmatch(r"unaffiliated(?:,.*)?", raw.casefold().strip()):
        return [("", raw, "unaffiliated", "explicit_none")]
    # Do not split 'and' inside one institution's official name (e.g. HKUST).
    protected = raw
    # A department's internal conjunction is not a second affiliation.
    protected = re.sub(r"School of Computer Science and Technology", lambda m: m.group().replace(" and ", " __AND__ "), protected, flags=re.I)
    for aliases in INSTITUTIONS.values():
        for alias in aliases:
            if " and " in alias:
                protected = re.sub(re.escape(alias), lambda m: re.sub(r"\s+and\s+", " __AND__ ", m.group(), flags=re.I), protected, flags=re.I)
    pieces = re.split(r";|\s+and\s+|\s*&\s*", protected.strip(" ;"))
    result = []
    for piece in pieces:
        piece = piece.replace("__AND__", "and").strip(" ,;")
        if not piece:
            continue
        matching = [(name, m.start(), m.end()) for name, aliases in INSTITUTIONS.items() for alias in aliases
                    for m in re.finditer(r"(?<!\w)" + re.escape(alias) + r"(?!\w)", piece, re.I)]
        selected = []
        for match in sorted(matching, key=lambda item: item[2] - item[1], reverse=True):
            if not any(match[1] < old[2] and old[1] < match[2] for old in selected):
                selected.append(match)
        canonicals = list(dict.fromkeys(m[0] for m in sorted(selected, key=lambda item: item[1]))) or [piece]
        for canonical in canonicals:
            kind = "industry" if canonical in {"Tencent", "Meta", "NVIDIA", "Bonree", "JaguarMicro", "CETC"} else "academic" if re.search(r"university|institute of technology|politecnico", canonical, re.I) else "research_institute" if re.search(r"laboratory|institute|academy|chinese academy", canonical, re.I) else "unknown"
            result.append((canonical, piece, kind, "alias_rule_review_pending" if matching else "raw_unreviewed"))
    return result


def build_tables():
    data = json.loads((ROOT / "data/publications.json").read_text())
    overrides = json.loads((ROOT / "data/overrides.json").read_text())
    institution_metadata = json.loads((ROOT / "data/institutions_reviewed.json").read_text())
    papers, authors, edges, quality = [], [], [], []
    institution_rows = {}
    for original in data["publications"]:
        p = {**original, **overrides.get(original["paper_id"], {})}
        title = p["title"].casefold()
        tags = p.get("analyst_tags", [tag for tag, words in TAXONOMY.items() if any(w in title for w in words)])
        tag_status = p.get("tag_status", "title_rule_suggested_review_pending")
        paper_authors = p.get("authors", [])
        partner_ids, tencent_names = set(), set()
        observed_institutions = set()
        for position, a in enumerate(paper_authors, 1):
            authorship_id = f'{p["paper_id"]}-a{position:03d}'
            affiliations = a.get("affiliations_raw", [])
            expanded = [item for raw in affiliations for item in institution_parts(raw)] or [("", "", "unknown", "missing")]
            expanded_unique = {item[0]: item for item in expanded}
            for canonical, raw, kind, normalization_status in expanded_unique.values():
                iid = "i-" + hashlib.sha256(canonical.encode()).hexdigest()[:12] if canonical else ""
                reviewed = institution_metadata.get(canonical, {})
                kind = reviewed.get("institution_type", kind)
                row = {"paper_id": p["paper_id"], "title": p["title"], "venue": p["venue"], "year": p["year"],
                       "author_position": position, "authorship_id": authorship_id, "author_name": a["name"],
                       "name_key": norm(a["name"]), "person_identity_status": "paper_local_not_disambiguated",
                       "dblp_pid": a.get("dblp_pid", ""), "orcid": a.get("orcid", ""),
                       "orcid_source": a.get("orcid_source", ""), "name_as_in_pdf": a.get("name_as_in_pdf", a["name"]),
                       "institution_id": iid, "affiliation_raw": raw, "affiliations_original": "; ".join(affiliations),
                       "institution": canonical, "institution_type": kind, "country": reviewed.get("country", ""),
                       "region": reviewed.get("region", ""), "is_tencent": canonical == "Tencent",
                       "is_dual_affiliation": len(expanded_unique) > 1, "normalization_status": reviewed.get("status", normalization_status),
                       "affiliation_status": p.get("affiliation_status", ""), "source_url": p["affiliation_source"],
                       "author_line_raw": p["author_line_raw"],
                       "publisher_affiliations_raw": "; ".join(a.get("publisher_affiliations_raw", [])),
                       "author_header_review": p.get("author_header_review", "pending"),
                       "source_cache": p.get("affiliation_metadata_cache") if p["affiliation_status"] == "publisher_deposit_verified" else p.get("affiliation_pdf_cache", p["source_cache"])}
                authors.append(row)
                if not canonical:
                    if kind != "unaffiliated":
                        quality.append({"paper_id": p["paper_id"], "field": "author_affiliation", "status": "missing", "detail": a["name"]})
                    continue
                observed_institutions.add(canonical)
                institution_rows[iid] = {"institution_id": iid, "institution": canonical, "institution_type": kind,
                                         "country": reviewed.get("country", ""), "region": reviewed.get("region", ""),
                                         "geography_source": reviewed.get("source_url", ""),
                                         "normalization_status": reviewed.get("status", normalization_status)}
                if canonical == "Tencent":
                    tencent_names.add(a["name"])
                elif kind in {"academic", "research_institute"}:
                    partner_ids.add(iid)
        can_analyze = bool(tencent_names) and p["scope_status"] == "included" and p.get("author_list_check") != "mismatch_review_required"
        for iid in sorted(partner_ids):
            inst = institution_rows[iid]
            partner_authors = sorted({a["author_name"] for a in authors if a["paper_id"] == p["paper_id"] and a["institution_id"] == iid})
            edges.append({"paper_id": p["paper_id"], "title": p["title"], "year": p["year"], "venue": p["venue"],
                          "publication_type": p["publication_type"],
                          "source_institution": "Tencent", "partner_institution_id": iid, "partner_institution": inst["institution"],
                          "partner_type": inst["institution_type"], "country": inst["country"], "region": inst["region"],
                          "tencent_authors": "; ".join(sorted(tencent_names)), "partner_authors": "; ".join(partner_authors),
                          "analyst_tags": "; ".join(tags), "tag_status": tag_status, "scope_status": p["scope_status"],
                          "analysis_eligible": can_analyze, "full_paper_weight": 1, "fractional_partner_weight": 1 / len(partner_ids),
                          "evidence_type": p["affiliation_status"], "affiliation_status": p["affiliation_status"],
                          "source_url": p["affiliation_source"]})
        papers.append({"paper_id": p["paper_id"], "shared_paper_id": p.get("shared_paper_id", ""), "title": p["title"],
                       "abstract": p.get("abstract", ""), "abstract_status": p.get("abstract_status", "available" if p.get("abstract") else "missing"),
                       "abstract_source": p.get("abstract_source", ""), "author_keywords": "; ".join(p.get("author_keywords", [])),
                       "keyword_status": "available" if p.get("author_keywords") else p.get("keyword_status", "not_collected"),
                       "keyword_source": p.get("keyword_source", ""),
                       "analyst_tags": "; ".join(tags), "tag_status": tag_status, "venue": p["venue"], "year": p["year"],
                       "scope_review_source": p.get("review_source", p["url"] if tag_status == "analyst_review_primary_program" else ""),
                       "publication_type": p["publication_type"], "doi": p.get("doi", ""), "url": p["url"], "pdf_url": p.get("pdf_url", ""),
                       "authors_ordered": "; ".join(a["name"] for a in paper_authors), "author_count": len(paper_authors),
                       "affiliations": "; ".join(sorted(observed_institutions)), "academic_partner_count": len(partner_ids),
                       "tencent_authors": "; ".join(sorted(tencent_names)), "tencent_relationship": p["tencent_relationship"],
                       "scope_status": p["scope_status"], "inclusion_reason": p["inclusion_reason"], "analysis_eligible": can_analyze,
                       "affiliation_status": p["affiliation_status"], "author_list_check": p.get("author_list_check", "not_checked"),
                       "author_list_check_source": p.get("author_list_check_source", p.get("dblp_url", "")),
                       "dblp_author_list_check": p.get("dblp_author_list_check", p.get("author_list_check", "not_checked")),
                       "dblp_url": p.get("dblp_url", ""), "version_group_id": p.get("version_group_id", ""),
                       "version_status": p["version_status"], "source_cache": p["source_cache"], "retrieved_at": p["retrieved_at"],
                       "publisher": p.get("publisher", ""), "pages": p.get("pages", ""), "published_date": p.get("published_date", ""),
                       "doi_url": "https://doi.org/" + p["doi"] if p.get("doi") else "",
                       "paper_url": "https://doi.org/" + p["doi"] if p.get("doi") else p["url"],
                       "pdf_access_status": p.get("pdf_access_status", "not_checked"),
                       "user_reviewed_primary_set": p.get("user_reviewed_primary_set", False),
                       "publisher_author_list_check": p.get("publisher_author_list_check", "not_available"),
                       "author_header_review": p.get("author_header_review", "pending"),
                       "metadata_status": p.get("metadata_status", "review_pending"),
                       "metadata_notes": p.get("metadata_notes", ""), "metadata_checked_at": p.get("metadata_checked_at", "")})
        for field in ("abstract", "doi", "author_keywords", "pdf_url"):
            if field == "author_keywords" and p.get("keyword_status") == "not_present_in_reviewed_front_matter":
                continue
            if not p.get(field):
                quality.append({"paper_id": p["paper_id"], "field": field, "status": "missing_or_not_collected", "detail": ""})
        for field in ("author_list_check", "scope_status", "affiliation_status", "version_status"):
            if field == "affiliation_status" and p.get(field) == "publisher_deposit_verified":
                continue
            if p.get(field) != {"author_list_check": "exact_order_match", "scope_status": "included", "affiliation_status": "pdf_verified", "version_status": "reviewed"}[field]:
                quality.append({"paper_id": p["paper_id"], "field": field, "status": p.get(field, "missing"), "detail": ""})
        if tag_status != "analyst_review_primary_program":
            quality.append({"paper_id": p["paper_id"], "field": "tag_status", "status": tag_status, "detail": ""})
        if p.get("pdf_access_status") != "public_pdf_cached":
            quality.append({"paper_id": p["paper_id"], "field": "pdf_access", "status": p.get("pdf_access_status", "not_checked"), "detail": "A publisher PDF URL is not evidence that its author block was retrieved."})
    coverage_data = json.loads((ROOT / "data/coverage.json").read_text())
    coverage = coverage_data["attempts"] + [{"venue": v, "status": "not_started", "completeness": "not_established"} for v in coverage_data["pending_venues"]]
    attempted = {(e["venue"], e.get("year")) for e in coverage_data["attempts"]}
    for venue, first_year in [("SIGCOMM", 1998), ("NSDI", 2004)]:
        for year in range(first_year, datetime.now().year + 1):
            if (venue, year) not in attempted:
                coverage.append({"venue": venue, "year": year, "status": "not_started", "completeness": "not_established", "note": "Historical sweep pending; not a zero-publication year"})
    instructions = [
        {"topic": "Status", "description": "Initial partial corpus. Coverage is not established; do not present these counts as all Tencent publications."},
        {"topic": "Author affiliations", "description": "One row per publication-author-institution assignment. Dual affiliations have multiple rows. Preserve publication-time affiliations."},
        {"topic": "Identity", "description": "Authorship IDs are paper-local. Name keys do not resolve homonyms. DBLP PIDs are supplied only after exact author-order checks."},
        {"topic": "Keywords", "description": "Author keywords are separate from analyst tags. Tag status identifies primary-program review or provisional title rules. Missing keyword fields have not yet been collected."},
        {"topic": "Analysis eligibility", "description": "Requires included networking scope, parsed Tencent assignment, and no known author-order mismatch. PDF affiliation review and version review still remain; provisional tags are not validated."},
        {"topic": "Weights", "description": "Full count=1 per paper-partner edge. Fractional weight=1/number of academic/research institution partners on that paper."},
        {"topic": "Geography", "description": "Country and region require reviewed institution metadata with a source. Blank geography means unknown, not China."},
        {"topic": "Versions", "description": "Version families are not yet reconciled. Do not combine conference/journal/preprint counts without version review."},
        {"topic": "Corrections", "description": "Edit data/overrides.json and data/institutions_reviewed.json, then rerun scripts/export.py. Retain evidence URLs."},
        {"topic": "Sources", "description": "Official programs, recovered CoNEXT Angular templates, independent OpenAlex indexing, DBLP catalogs and author-hosted PDFs are cached under raw/. See Independent_Checks, Discovery_Audit and PDF_Checks for methods and exclusions."},
        {"topic": "Counting", "description": "Annual_Stats separates main-venue records, networking-scope included records, boundary candidates, and posters. Zero confirmed papers is not proof of absence. 2026 is year-to-date; CoNEXT/PACMNET long papers must not be double-counted."},
        {"topic": "Excluded venues", "description": "ICNP and mobile-centric conferences are excluded by user request. HotNets is a workshop venue; its primary papers belong in the five-venue series, unlike SIGCOMM poster/demo and affiliated-workshop outputs."},
        {"topic": "Generated", "description": datetime.now(timezone.utc).isoformat()},
    ]
    taxonomy = [{"tag": tag, "status": "provisional_title_rule", "matching_terms": "; ".join(words)} for tag, words in TAXONOMY.items()]
    tables = {"Readme": instructions, "Publications": papers, "Author_Affiliations": authors,
              "Institutions": list(institution_rows.values()), "Collaboration": edges, "Coverage": coverage,
              "Quality": quality, "Taxonomy": taxonomy}
    metadata_audit = ROOT / "data/metadata_audit.json"
    if metadata_audit.exists():
        tables["Metadata_Checks"] = [{k:v for k,v in r.items() if k != "publisher_affiliations_raw"}
                                     for r in json.loads(metadata_audit.read_text())["checks"]]
        tables["User_Program_Check"] = json.loads((ROOT / "data/user_program_check.json").read_text())["checks"]
        instructions.append({"topic": "Metadata completion", "description": "User-reviewed primary set: 32 papers. Required metadata means title, venue/year, full sourced abstract, ordered author names and individual publication-time affiliations; it does not imply all author keywords, person identities, PDF access, versions or venue recall are complete. PDF and publisher-deposit affiliation reviews are labeled separately. Source conflicts remain in metadata notes."})
    tables["Annual_Stats"] = []
    for year in range(2019, 2027):
        for venue in ["NSDI", "SIGCOMM", "CoNEXT", "IMC", "HotNets"]:
            observed = [p for p in papers if p["year"] == year and p["venue"] == venue]
            primary = [p for p in observed if p["publication_type"] in {"conference_paper", "workshop_paper", "journal_paper"}]
            tables["Annual_Stats"].append({"year": year, "venue": venue, "primary_venue_records": len(primary),
                "networking_scope_included": sum(p["scope_status"] == "included" for p in primary),
                "boundary_candidates": sum(p["scope_status"] != "included" for p in primary),
                "posters": sum(p["publication_type"] == "poster" for p in observed),
                "completeness": "not_established", "year_status": "year_to_date" if year == 2026 else "historical",
                "note": "Observed inventory, not exhaustive output. CoNEXT includes associated PACMNET papers when found."})
    manual = ROOT / "data/manual_checks.json"
    if manual.exists():
        tables["Independent_Checks"] = json.loads(manual.read_text())["checks"]
    audit = ROOT / "data/audit_summary.json"
    if audit.exists():
        tables["Discovery_Audit"] = json.loads(audit.read_text())["venue_year_checks"]
    pdf_audit = ROOT / "data/independent_pdf_audit.json"
    if pdf_audit.exists():
        tables["PDF_Checks"] = [{**{k:v for k,v in p.items() if k != "tencent_occurrences"},
            "tencent_occurrence_count": len(p.get("tencent_occurrences", [])),
            "tencent_contexts": json.dumps(p.get("tencent_occurrences", []), ensure_ascii=False)}
            for p in json.loads(pdf_audit.read_text())["checks"]]
    ledger_pdf = ROOT / "data/ledger_pdf_audit.json"
    if ledger_pdf.exists():
        tables.setdefault("PDF_Checks", []).extend({**{k:v for k,v in p.items() if k != "tencent_occurrences"},
            "tencent_occurrence_count": len(p.get("tencent_occurrences", [])),
            "tencent_contexts": json.dumps(p.get("tencent_occurrences", []), ensure_ascii=False)}
            for p in json.loads(ledger_pdf.read_text())["checks"])
    metadata_pdf = ROOT / "data/metadata_pdf_checks.json"
    if metadata_pdf.exists():
        tables.setdefault("PDF_Checks", []).extend({**{k:v for k,v in p.items() if k != "tencent_occurrences"},
            "tencent_occurrence_count": len(p.get("tencent_occurrences", [])),
            "tencent_contexts": json.dumps(p.get("tencent_occurrences", []), ensure_ascii=False)}
            for p in json.loads(metadata_pdf.read_text())["checks"])
    ledger_path = ROOT / "data/proceedings_ledger.json"
    dashboard_path = ROOT / "data/completeness_dashboard.json"
    if ledger_path.exists() and dashboard_path.exists():
        ledger = json.loads(ledger_path.read_text())["publications"]
        dashboard = json.loads(dashboard_path.read_text())
        tables["Proceedings_Ledger"] = ledger
        tables["Completeness"] = dashboard["venue_years"]
        tables["Unresolved_Queue"] = [p for p in ledger if p["decision"] == "unresolved"]
        tables["Source_Parse_Log"] = dashboard["source_parse_logs"]
        tables["Excluded_Records"] = dashboard["excluded_non_paper_records"]
        instructions.append({"topic": "Completeness ledger", "description": "Proceedings_Ledger accounts for all discovered venue records, not Tencent papers alone. Completeness covers 40 venue/year cells. Unresolved_Queue exposes gaps; PDF string screening does not certify exhaustive affiliations. Unclassified records and title variants still require review."})
    return tables


def col(index):
    result = ""
    while index:
        index, mod = divmod(index - 1, 26)
        result = chr(65 + mod) + result
    return result


def xml_bytes(element):
    return ET.tostring(element, encoding="utf-8", xml_declaration=True)


def xlsx(path, tables):
    """Write plain text, numeric, and boolean cells; prevent formula injection."""
    ET.register_namespace("", NS)
    ET.register_namespace("r", REL)
    workbook = ET.Element("workbook", xmlns=NS)
    sheets = ET.SubElement(workbook, "sheets")
    relationships = ET.Element("Relationships", xmlns=PACKAGE_REL)
    types = ET.Element("Types", xmlns="http://schemas.openxmlformats.org/package/2006/content-types")
    for extension, mime in [("rels", "application/vnd.openxmlformats-package.relationships+xml"), ("xml", "application/xml")]:
        ET.SubElement(types, "Default", Extension=extension, ContentType=mime)
    ET.SubElement(types, "Override", PartName="/xl/workbook.xml", ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml")
    with ZipFile(path, "w", ZIP_DEFLATED) as archive:
        ET.SubElement(relationships, "Relationship", Id="rIdStyles", Type=REL + "/styles", Target="styles.xml")
        ET.SubElement(types, "Override", PartName="/xl/styles.xml", ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.styles+xml")
        styles = ET.Element("styleSheet", xmlns=NS)
        fonts = ET.SubElement(styles, "fonts", count="2")
        for bold in (False, True):
            font = ET.SubElement(fonts, "font")
            ET.SubElement(font, "sz", val="11")
            ET.SubElement(font, "name", val="Calibri")
            if bold:
                ET.SubElement(font, "b")
                ET.SubElement(font, "color", rgb="FFFFFFFF")
        fills = ET.SubElement(styles, "fills", count="3")
        for pattern in ("none", "gray125", "solid"):
            fill = ET.SubElement(fills, "fill")
            pattern_node = ET.SubElement(fill, "patternFill", patternType=pattern)
            if pattern == "solid":
                ET.SubElement(pattern_node, "fgColor", rgb="FF175B66")
        borders = ET.SubElement(styles, "borders", count="1")
        ET.SubElement(borders, "border")
        style_xfs = ET.SubElement(styles, "cellStyleXfs", count="1")
        ET.SubElement(style_xfs, "xf", numFmtId="0", fontId="0", fillId="0", borderId="0")
        cell_xfs = ET.SubElement(styles, "cellXfs", count="3")
        for font_id, fill_id, wrap in [(0, 0, False), (1, 2, True), (0, 0, True)]:
            xf = ET.SubElement(cell_xfs, "xf", numFmtId="0", fontId=str(font_id), fillId=str(fill_id), borderId="0", xfId="0")
            if wrap:
                ET.SubElement(xf, "alignment", vertical="top", wrapText="1")
        cell_styles = ET.SubElement(styles, "cellStyles", count="1")
        ET.SubElement(cell_styles, "cellStyle", name="Normal", xfId="0", builtinId="0")
        archive.writestr("xl/styles.xml", xml_bytes(styles))
        for index, (name, rows) in enumerate(tables.items(), 1):
            headers = list(dict.fromkeys(key for row in rows for key in row)) or ["status"]
            ET.SubElement(sheets, "sheet", name=name, sheetId=str(index), attrib={f"{{{REL}}}id": f"rId{index}"})
            ET.SubElement(relationships, "Relationship", Id=f"rId{index}", Type=REL + "/worksheet", Target=f"worksheets/sheet{index}.xml")
            ET.SubElement(types, "Override", PartName=f"/xl/worksheets/sheet{index}.xml", ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml")
            worksheet = ET.Element("worksheet", xmlns=NS)
            ET.SubElement(worksheet, "dimension", ref=f"A1:{col(len(headers))}{len(rows) + 1}")
            views = ET.SubElement(worksheet, "sheetViews")
            view = ET.SubElement(views, "sheetView", workbookViewId="0")
            ET.SubElement(view, "pane", ySplit="1", topLeftCell="A2", activePane="bottomLeft", state="frozen")
            columns = ET.SubElement(worksheet, "cols")
            for c, header in enumerate(headers, 1):
                width = 85 if header in {"abstract", "author_line_raw", "description"} else 55 if header in {"title", "source_url", "url"} else 28
                ET.SubElement(columns, "col", min=str(c), max=str(c), width=str(width), customWidth="1")
            sheet_data = ET.SubElement(worksheet, "sheetData")
            values = [headers] + [[row.get(h, "") for h in headers] for row in rows]
            for r, row_values in enumerate(values, 1):
                row_node = ET.SubElement(sheet_data, "row", r=str(r), ht="30" if r == 1 else "60" if name == "Publications" else "36", customHeight="1")
                for c, value in enumerate(row_values, 1):
                    attrs = {"r": f"{col(c)}{r}", "s": "1" if r == 1 else "2"}
                    if isinstance(value, bool):
                        attrs["t"] = "b"
                        cell = ET.SubElement(row_node, "c", attrs)
                        ET.SubElement(cell, "v").text = str(int(value))
                    elif isinstance(value, (int, float)):
                        cell = ET.SubElement(row_node, "c", attrs)
                        ET.SubElement(cell, "v").text = str(value)
                    else:
                        attrs["t"] = "inlineStr"
                        cell = ET.SubElement(row_node, "c", attrs)
                        inline = ET.SubElement(cell, "is")
                        ET.SubElement(inline, "t", attrib={"{http://www.w3.org/XML/1998/namespace}space": "preserve"}).text = str(value or "")
            ET.SubElement(worksheet, "autoFilter", ref=f"A1:{col(len(headers))}{len(rows) + 1}")
            archive.writestr(f"xl/worksheets/sheet{index}.xml", xml_bytes(worksheet))
        package = ET.Element("Relationships", xmlns=PACKAGE_REL)
        ET.SubElement(package, "Relationship", Id="rId1", Type=REL + "/officeDocument", Target="xl/workbook.xml")
        archive.writestr("_rels/.rels", xml_bytes(package))
        archive.writestr("xl/workbook.xml", xml_bytes(workbook))
        archive.writestr("xl/_rels/workbook.xml.rels", xml_bytes(relationships))
        archive.writestr("[Content_Types].xml", xml_bytes(types))


def csv_value(value):
    if isinstance(value, str) and value.lstrip().startswith(("=", "+", "-", "@")):
        return "'" + value
    return value


def metadata_tables(tables):
    """Compact handoff: curated metadata, separate from the proceedings audit."""
    primary = [p for p in tables["Publications"] if p.get("user_reviewed_primary_set")]
    columns = ["paper_id", "title", "venue", "year", "publication_type", "abstract", "abstract_status",
               "authors_ordered", "author_count", "affiliations", "tencent_authors", "author_keywords",
               "keyword_status", "keyword_source", "doi", "doi_url", "publisher", "published_date", "pages",
               "paper_url", "url", "pdf_url", "pdf_access_status", "abstract_source", "affiliation_status",
               "author_header_review", "publisher_author_list_check", "author_list_check", "author_list_check_source", "dblp_author_list_check", "metadata_status",
               "metadata_notes", "metadata_checked_at", "analyst_tags", "tag_status", "scope_status"]
    primary_rows = [{k:p[k] for k in columns} for p in primary]
    primary_ids = {p["paper_id"] for p in primary}
    authors = [a for a in tables["Author_Affiliations"] if a["paper_id"] in primary_ids]
    poster_ids = {p["paper_id"] for p in tables["Publications"] if p["publication_type"] == "poster"}
    institutions = {a["institution_id"] for a in authors if a["institution_id"]}
    return {
        "Readme": [
            {"topic": "Scope", "description": "32 primary papers explicitly checked by the user in COLLECTION_PLAN.md, 2019–2026. Includes the existing networking-scope boundary candidate; two posters are separate. This is a metadata-completed set, not a certified exhaustive venue survey."},
            {"topic": "Required metadata", "description": "All 32 have full source abstracts, ordered author names and reviewed individual publication-time affiliations. PDF verification (27) and publisher-deposit verification (5) are labeled separately. Publisher links may still be inaccessible; PDF access status is explicit."},
            {"topic": "Author rows", "description": "One row per author–institution assignment. Dual affiliations have multiple rows; author_position preserves the complete ordered list. Explicit unaffiliated authors keep a row with a blank institution. Paper-local authorship IDs are not global researcher identities."},
            {"topic": "Sources", "description": "paper_url points to the paper/DOI; url retains the discovery program. Abstract and affiliation source URLs are retained. PDF spellings and publisher raw affiliations preserve discrepancies; metadata notes explain Dorado, Holmes, FlexWAN and XFir."},
            {"topic": "Keywords", "description": "Author keywords are separate from analyst tags. NSDI front matter does not supply a keyword field; remaining inaccessible ACM keywords are not_collected, not fabricated."},
            {"topic": "Posters", "description": "Posters are not primary-paper counts. The 2019 poster abstract is still missing from accessible primary metadata; TOO's existing repository abstract remains separately labeled."},
            {"topic": "Generated", "description": datetime.now(timezone.utc).isoformat()},
        ],
        "Publications": primary_rows,
        "Author_Affiliations": authors,
        "Institutions": [i for i in tables["Institutions"] if i["institution_id"] in institutions],
        "Metadata_Checks": [r for r in tables["Metadata_Checks"] if r["paper_id"] in primary_ids],
        "Poster_Publications": [{k:p[k] for k in columns} for p in tables["Publications"] if p["paper_id"] in poster_ids],
        "Poster_Affiliations": [a for a in tables["Author_Affiliations"] if a["paper_id"] in poster_ids],
        "User_Program_Check": tables["User_Program_Check"],
    }


def main():
    tables = build_tables()
    output = ROOT / "output"
    output.mkdir(exist_ok=True)
    for name, rows in tables.items():
        headers = list(dict.fromkeys(key for row in rows for key in row)) or ["status"]
        with (output / (name.lower() + ".csv")).open("w", encoding="utf-8-sig", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=headers)
            writer.writeheader()
            writer.writerows({k: csv_value(v) for k, v in row.items()} for row in rows)
    xlsx(output / "tencent_networking_publications.xlsx", tables)
    if "Metadata_Checks" in tables:
        compact = metadata_tables(tables)
        xlsx(output / "tencent_networking_metadata.xlsx", compact)
        for name, rows in compact.items():
            headers = list(dict.fromkeys(key for row in rows for key in row)) or ["status"]
            with (output / ("metadata_" + name.lower() + ".csv")).open("w", encoding="utf-8-sig", newline="") as handle:
                writer = csv.DictWriter(handle, fieldnames=headers)
                writer.writeheader()
                writer.writerows({k: csv_value(v) for k,v in row.items()} for row in rows)
    report = {"generated_at": datetime.now(timezone.utc).isoformat(), "coverage": "not_established",
              "sheet_rows": {name: len(rows) for name, rows in tables.items()},
              "scope_status": dict(Counter(p["scope_status"] for p in tables["Publications"])),
              "author_list_checks": dict(Counter(p["author_list_check"] for p in tables["Publications"])),
              "quality_flags": dict(Counter(q["field"] for q in tables["Quality"]))}
    (output / "quality_report.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
