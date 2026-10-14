#!/usr/bin/env python3
"""Independent institution-index discovery, matched to the five-venue bibliography."""
import json
from urllib.parse import urlencode

from collect import ROOT, WORKSPACE, fetch, norm, save


def main():
    url = "https://api.openalex.org/institutions?search=tencent&per-page=20"
    raw, info = fetch(url)
    institutions = json.loads(raw)["results"]
    print("Institutions:", [(i["id"], i["display_name"]) for i in institutions], flush=True)
    data = WORKSPACE / "projects/networking-to-ai-migration/data"
    refs = json.loads((data / "topnet_venue_year_papers.json").read_text())["papers"]
    refs += json.loads((data / "pacmnet_toc_papers.json").read_text())["papers"]
    by_title = {(p["year"], norm(p["title"])): p for p in refs if 2019 <= p["year"] <= 2026}
    existing = json.loads((ROOT / "data/publications.json").read_text())["publications"]
    collected = {(p["year"], norm(p["title"])) for p in existing}
    matches, source_logs, works = [], [], {}
    for institution in institutions:
        cursor = "*"
        seen = set()
        while cursor and cursor not in seen:
            seen.add(cursor)
            params = {"filter": f'institutions.id:{institution["id"].split("/")[-1]},publication_year:2019-2026',
                      "per-page": 200, "cursor": cursor,
                      "select": "id,doi,title,publication_year,type,primary_location"}
            url = "https://api.openalex.org/works?" + urlencode(params)
            try:
                raw, cache = fetch(url)
                response = json.loads(raw)
            except Exception as exc:
                source_logs.append({"institution_id": institution["id"], "url": url, "status": "error", "detail": str(exc)})
                break
            rows = response["results"]
            source_logs.append({"institution_id": institution["id"], "url": url, "status": "fetched", "source_cache": cache["cache_file"], "reported_total": response["meta"]["count"], "returned": len(rows)})
            for work in rows:
                works[work["id"]] = work
                key = (work["publication_year"], norm(work["title"]))
                if key in by_title:
                    reference = by_title[key]
                    matches.append({"title": work["title"], "year": work["publication_year"], "venue": reference["venue"],
                                    "openalex_id": work["id"], "doi": work.get("doi", ""), "institution_id": institution["id"],
                                    "already_collected": key in collected, "bibliography": reference, "source_cache": cache["cache_file"],
                                    "status": "index_affiliation_candidate_primary_verification_required"})
            save(ROOT / "data/independent_openalex.json", {"institutions": [{"id": i["id"], "name": i["display_name"]} for i in institutions],
                 "works_seen": len(works), "five_venue_matches": matches, "source_logs": source_logs})
            print(f'{institution["display_name"]}: {len(works)} works seen; {len(matches)} venue matches', flush=True)
            cursor = response.get("meta", {}).get("next_cursor") if rows else None
    save(ROOT / "data/openalex_work_inventory.json", {"works": list(works.values())})
    print("Five-venue candidates:", [(m["venue"], m["year"], m["title"], m["already_collected"]) for m in matches])


if __name__ == "__main__":
    main()
