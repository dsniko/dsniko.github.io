#!/usr/bin/env python3
"""
Fast audit of _publications/*.md files for the dsniko.github.io site.

Checks:
  - YAML frontmatter parses cleanly
  - Required fields present:   title, collection, category, permalink, date
  - Recommended fields present: excerpt, venue, paperurl, citation
  - category is one of the allowed values in _config.yml
  - collection == 'publications'
  - permalink matches filename convention   /publication/<basename>
  - filename matches YYYY-MM-DD-<slug>.md
  - date frontmatter parses as a real date
  - paperurl looks like a URL (or is empty)
  - no duplicate permalinks
  - URL list extracted from each entry (paperurl, slidesurl, bibtexurl, links inside citation/excerpt)

Outputs:
  - publications_audit.csv      machine-readable per-file findings
  - publications_audit.md       human-readable summary
  - publications_urls.csv       title, file, paperurl, other_urls
"""
from __future__ import annotations

import csv
import os
import re
import sys
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path
from typing import Any

import yaml

PUB_DIR = Path("/sessions/lucid-hopeful-mendel/mnt/dsniko.github.io/_publications")
CFG = Path("/sessions/lucid-hopeful-mendel/mnt/dsniko.github.io/_config.yml")
OUT_DIR = Path("/sessions/lucid-hopeful-mendel/mnt/outputs")
OUT_DIR.mkdir(parents=True, exist_ok=True)

ALLOWED_CATEGORIES: set[str] = set()
try:
    with CFG.open() as f:
        cfg = yaml.safe_load(f)
    pc = cfg.get("publication_category", {}) or {}
    ALLOWED_CATEGORIES = set(pc.keys())
except Exception as exc:
    print(f"warn: could not parse _config.yml ({exc})", file=sys.stderr)

REQUIRED = ["title", "collection", "category", "permalink", "date"]
RECOMMENDED = ["excerpt", "venue", "paperurl", "citation"]
URL_KEYS = ["paperurl", "slidesurl", "bibtexurl"]

FILENAME_RE = re.compile(r"^(\d{4})-(\d{2})-(\d{2})-(.+)\.md$")
PERMALINK_RE = re.compile(r"^/publication/(.+)$")
URL_IN_TEXT_RE = re.compile(r"https?://[^\s\"'<>)\]]+")


def split_frontmatter(text: str) -> tuple[str, str]:
    """Return (frontmatter_yaml, body). Frontmatter is between two '---' lines."""
    if not text.startswith("---"):
        return "", text
    parts = text.split("\n", 1)
    rest = parts[1] if len(parts) > 1 else ""
    end = rest.find("\n---")
    if end == -1:
        return "", text
    fm = rest[:end]
    body = rest[end + 4 :]
    return fm, body


def audit_one(p: Path) -> dict[str, Any]:
    rec: dict[str, Any] = {
        "file": p.name,
        "path": str(p),
        "ok": True,
        "errors": [],
        "warnings": [],
        "title": "",
        "category": "",
        "permalink": "",
        "date": "",
        "venue": "",
        "paperurl": "",
        "other_urls": [],
        "filename_date": "",
        "filename_slug": "",
    }
    try:
        text = p.read_text(encoding="utf-8")
    except Exception as exc:
        rec["ok"] = False
        rec["errors"].append(f"read failed: {exc}")
        return rec

    fm_text, body = split_frontmatter(text)
    if not fm_text:
        rec["ok"] = False
        rec["errors"].append("missing or unterminated frontmatter")
        return rec

    try:
        fm = yaml.safe_load(fm_text) or {}
    except yaml.YAMLError as exc:
        rec["ok"] = False
        rec["errors"].append(f"YAML parse error: {exc}")
        return rec

    # Required
    for k in REQUIRED:
        if k not in fm or fm[k] in (None, ""):
            rec["errors"].append(f"missing required '{k}'")
    # Recommended
    for k in RECOMMENDED:
        if k not in fm or fm[k] in (None, ""):
            rec["warnings"].append(f"missing recommended '{k}'")

    # Category
    cat = fm.get("category")
    if cat is not None:
        rec["category"] = str(cat)
        if ALLOWED_CATEGORIES and cat not in ALLOWED_CATEGORIES:
            rec["errors"].append(
                f"unknown category '{cat}' (allowed: {sorted(ALLOWED_CATEGORIES)})"
            )

    # Collection
    if fm.get("collection") and fm["collection"] != "publications":
        rec["errors"].append(f"collection should be 'publications', got '{fm['collection']}'")

    # Date
    d = fm.get("date")
    rec["date"] = str(d) if d is not None else ""
    if isinstance(d, date):
        pass  # ok
    elif isinstance(d, str):
        if not re.match(r"^\d{4}-\d{2}-\d{2}", d):
            rec["warnings"].append(f"date '{d}' is not YYYY-MM-DD")

    # Filename ↔ permalink consistency
    m = FILENAME_RE.match(p.name)
    if m:
        rec["filename_date"] = f"{m.group(1)}-{m.group(2)}-{m.group(3)}"
        rec["filename_slug"] = m.group(4)
        permalink = fm.get("permalink", "")
        rec["permalink"] = str(permalink)
        pm = PERMALINK_RE.match(str(permalink))
        if not pm:
            rec["errors"].append(f"permalink should start with /publication/ (got '{permalink}')")
        else:
            expected = p.stem  # filename without .md
            if pm.group(1) != expected:
                rec["warnings"].append(
                    f"permalink slug '{pm.group(1)}' != filename stem '{expected}'"
                )
        # date consistency: filename date vs frontmatter date (only the YYYY-MM-DD part)
        if rec["date"]:
            head = rec["date"][:10]
            if head != rec["filename_date"]:
                rec["warnings"].append(
                    f"frontmatter date '{rec['date']}' differs from filename date '{rec['filename_date']}'"
                )
    else:
        # special case: 2025-marvel-risc-v-extensions.md (no full date in name)
        rec["warnings"].append("filename does not match YYYY-MM-DD-<slug>.md")

    # Title
    rec["title"] = str(fm.get("title", "")).strip()

    # Venue
    rec["venue"] = str(fm.get("venue", "")).strip()

    # paperurl
    pu = (fm.get("paperurl") or "").strip()
    rec["paperurl"] = pu
    if pu and not re.match(r"^https?://", pu):
        rec["warnings"].append(f"paperurl is not http(s): '{pu}'")

    # collect any other URLs in citation/excerpt
    other_urls: list[str] = []
    for k in ("slidesurl", "bibtexurl"):
        v = (fm.get(k) or "").strip()
        if v:
            other_urls.append(v)
    for k in ("citation", "excerpt"):
        v = fm.get(k) or ""
        if isinstance(v, str):
            for url in URL_IN_TEXT_RE.findall(v):
                if url != pu and url not in other_urls:
                    other_urls.append(url)
    rec["other_urls"] = other_urls

    rec["ok"] = not rec["errors"]
    return rec


def main() -> None:
    files = sorted(p for p in PUB_DIR.iterdir() if p.suffix == ".md")
    records = [audit_one(p) for p in files]

    # Duplicate permalinks
    permalinks: defaultdict[str, list[str]] = defaultdict(list)
    for r in records:
        if r["permalink"]:
            permalinks[r["permalink"]].append(r["file"])
    duplicates = {k: v for k, v in permalinks.items() if len(v) > 1}
    for k, v in duplicates.items():
        for r in records:
            if r["permalink"] == k:
                r["errors"].append(f"duplicate permalink across files: {v}")
                r["ok"] = False

    # Counts
    by_category = Counter(r["category"] for r in records if r["category"])
    missing_paperurl = [r for r in records if not r["paperurl"]]
    with_errors = [r for r in records if r["errors"]]
    with_warnings = [r for r in records if r["warnings"]]

    # CSV output
    csv_path = OUT_DIR / "publications_audit.csv"
    with csv_path.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(
            [
                "file",
                "ok",
                "category",
                "date",
                "title",
                "venue",
                "paperurl",
                "errors",
                "warnings",
            ]
        )
        for r in records:
            w.writerow(
                [
                    r["file"],
                    "yes" if r["ok"] else "no",
                    r["category"],
                    r["date"],
                    r["title"],
                    r["venue"],
                    r["paperurl"],
                    " | ".join(r["errors"]),
                    " | ".join(r["warnings"]),
                ]
            )

    urls_path = OUT_DIR / "publications_urls.csv"
    with urls_path.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["file", "title", "category", "paperurl", "other_urls"])
        for r in records:
            w.writerow(
                [
                    r["file"],
                    r["title"],
                    r["category"],
                    r["paperurl"],
                    " | ".join(r["other_urls"]),
                ]
            )

    # Markdown report
    md_path = OUT_DIR / "publications_audit.md"
    lines: list[str] = []
    lines.append(f"# Publications audit — {len(records)} entries")
    lines.append("")
    lines.append(f"Source folder: `_publications/` ({PUB_DIR})")
    lines.append("")
    lines.append("## Counts by category")
    lines.append("")
    lines.append("| Category | Count |")
    lines.append("|---|---|")
    for cat, n in sorted(by_category.items(), key=lambda kv: -kv[1]):
        lines.append(f"| `{cat}` | {n} |")
    lines.append(f"| **Total** | **{len(records)}** |")
    lines.append("")
    lines.append(f"Allowed categories (from `_config.yml`): {sorted(ALLOWED_CATEGORIES)}")
    lines.append("")

    lines.append("## Hard errors")
    lines.append("")
    lines.append(f"{len(with_errors)} files have one or more errors.")
    lines.append("")
    if with_errors:
        for r in with_errors:
            lines.append(f"- **{r['file']}**")
            for e in r["errors"]:
                lines.append(f"  - error: {e}")
    else:
        lines.append("None.")
    lines.append("")

    lines.append("## Warnings (look-but-not-blocking)")
    lines.append("")
    lines.append(f"{len(with_warnings)} files have one or more warnings.")
    lines.append("")
    # Group warnings by type for skim-ability
    warn_buckets: defaultdict[str, list[str]] = defaultdict(list)
    for r in with_warnings:
        for w in r["warnings"]:
            head = w.split(":")[0]
            warn_buckets[head].append(f"{r['file']} — {w}")
    for head, items in sorted(warn_buckets.items(), key=lambda kv: -len(kv[1])):
        lines.append(f"### {head} ({len(items)})")
        lines.append("")
        for it in items[:50]:
            lines.append(f"- {it}")
        if len(items) > 50:
            lines.append(f"- … and {len(items) - 50} more")
        lines.append("")

    lines.append("## Entries missing `paperurl`")
    lines.append("")
    lines.append(f"{len(missing_paperurl)} entries have no paperurl set.")
    lines.append("")
    for r in missing_paperurl:
        lines.append(f"- {r['file']} — *{r['title'][:80]}*")
    lines.append("")

    md_path.write_text("\n".join(lines), encoding="utf-8")

    # Console summary
    print(f"Audited {len(records)} files")
    print(f"  errors:   {len(with_errors)}")
    print(f"  warnings: {len(with_warnings)}")
    print(f"  no paperurl: {len(missing_paperurl)}")
    print(f"  by category: {dict(by_category)}")
    print(f"\nWrote:")
    print(f"  {csv_path}")
    print(f"  {urls_path}")
    print(f"  {md_path}")


if __name__ == "__main__":
    main()
