#!/usr/bin/env python3
"""Independent first-page affiliation checks; occurrences are leads, not inclusions."""
import hashlib
import json
import re
import subprocess
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone

import requests

from collect import ROOT, save


def check(url):
    key = hashlib.sha256(url.encode()).hexdigest()[:20]
    path = ROOT / "raw" / (key + ".pdf")
    txt = path.with_suffix(".txt")
    try:
        if not path.exists():
            r = requests.get(url, timeout=(10, 35))
            r.raise_for_status()
            if not r.content.startswith(b"%PDF"):
                raise ValueError("Response is not a PDF")
            path.write_bytes(r.content)
        if not txt.exists():
            subprocess.run(["pdftotext", "-f", "1", "-l", "2", "-layout", str(path), str(txt)], check=True, capture_output=True)
        content = txt.read_text(errors="replace")
        matches = [{"offset": m.start(), "excerpt": content[max(0, m.start()-400):m.end()+400]}
                   for m in re.finditer(r"\btencent\b|腾讯", content, re.I)]
        result = {"url": url, "status": "first_two_pages_checked", "cache_file": str(path.relative_to(ROOT)),
                  "text_cache": str(txt.relative_to(ROOT)), "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
                  "retrieved_at": datetime.fromtimestamp(path.stat().st_mtime, timezone.utc).isoformat(),
                  "checked_at": datetime.now(timezone.utc).isoformat(), "tencent_occurrences": matches,
                  "interpretation": "manual_header_review_required" if matches else "no_explicit_tencent_on_first_two_pages"}
        save(path.with_suffix(".json"), result)
        return result
    except Exception as exc:
        return {"url": url, "status": "fetch_or_extract_error", "detail": str(exc)}


def main():
    discovery = json.loads((ROOT / "data/program_discovery.json").read_text())
    urls = {u for p in discovery["pages"] for u in p["pdf_urls"] if "/papers/" in u or "/paper/" in u}
    urls.update(["https://jessiehuiwang.github.io/files/2021CoNEXT.pdf",
                 "https://conferences.sigcomm.org/sigcomm/2021/files/papers/3452296.3472927.pdf",
                 "https://yunmingxiao.github.io/publication/fiat/conext22-xiao.pdf"])
    results = []
    reviewed = json.loads((ROOT / "data/manual_checks.json").read_text())["checks"] if (ROOT / "data/manual_checks.json").exists() else []
    decisions = {p["source_url"]: p["decision"] for p in reviewed}
    with ThreadPoolExecutor(max_workers=4) as pool:
        for i, result in enumerate(pool.map(check, sorted(urls)), 1):
            if result["url"] in decisions:
                result["manual_decision"] = decisions[result["url"]]
            results.append(result)
            if result.get("tencent_occurrences") or result["status"] == "fetch_or_extract_error":
                print(json.dumps(result, ensure_ascii=False), flush=True)
            if i % 20 == 0:
                print(f"PDF audit: {i}/{len(urls)}", flush=True)
            save(ROOT / "data/independent_pdf_audit.json", {"checks": results})


if __name__ == "__main__":
    main()
