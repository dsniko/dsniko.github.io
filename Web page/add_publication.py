#!/usr/bin/env python3
"""
Add a new publication entry to _publications/ for the dsniko.github.io site.

Usage (CLI):
  ./add_publication.py \
      --category conferences \
      --date 2026-08-15 \
      --title "Cool Paper Title" \
      --authors "Foo, B., Bar, A., & Nikolopoulos, D. S." \
      --year 2026 \
      --venue "Proceedings of XYZ Conference (XYZ '26)" \
      --paperurl "https://arxiv.org/abs/2608.12345" \
      --excerpt "One- or two-sentence summary used in listings."

Usage (programmatic): import add_publication and call render_entry(...).

The script writes a file named <DATE>-<slug>.md inside _publications/, where
<slug> is the lowercase, dash-joined version of the title. It prints the
filename it wrote and the YAML it produced.

If --dry-run is given, nothing is written; the YAML is printed to stdout.
"""
from __future__ import annotations

import argparse
import re
import sys
import unicodedata
from pathlib import Path
from typing import Optional

PUB_DIR_DEFAULT = Path(
    "/sessions/lucid-hopeful-mendel/mnt/dsniko.github.io/_publications"
)

ALLOWED_CATEGORIES = {
    "books",
    "manuscripts",      # Journal Articles
    "conferences",
    "workshops",
    "bookchapters",
    "magazines",
    "posters",
    "volumes",          # Edited Volumes / Special Issues
    "invited",
    "keynotes",
    "techreports",
}

DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def slugify(s: str) -> str:
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode("ascii")
    s = s.lower()
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s


def yaml_dq(s: str) -> str:
    """Escape a string for use inside double quotes in YAML."""
    return s.replace("\\", "\\\\").replace('"', '\\"')


def html_quote(s: str) -> str:
    """Replace " with &quot; for HTML-rendered fields (citation)."""
    return s.replace('"', "&quot;")


def render_entry(
    *,
    title: str,
    authors: str,
    year: str,
    venue: str,
    date_str: str,
    category: str,
    paperurl: str = "",
    slidesurl: str = "",
    bibtexurl: str = "",
    excerpt: Optional[str] = None,
    citation: Optional[str] = None,
    slug: Optional[str] = None,
    extra_citation_suffix: str = "",
) -> tuple[str, str]:
    """Return (filename, yaml_text)."""
    if category not in ALLOWED_CATEGORIES:
        raise ValueError(
            f"category '{category}' not in allowed set {sorted(ALLOWED_CATEGORIES)}"
        )
    if not DATE_RE.match(date_str):
        raise ValueError(f"date '{date_str}' must be YYYY-MM-DD")

    if slug is None:
        slug = slugify(title)

    permalink = f"/publication/{date_str}-{slug}"
    filename = f"{date_str}-{slug}.md"

    if excerpt is None:
        excerpt = title  # safe fallback; usually you'll write a real summary

    if citation is None:
        cit_title = html_quote(title)
        cit_venue = venue  # already-rendered HTML/italics permitted in venue
        suffix = f" {extra_citation_suffix}".rstrip() if extra_citation_suffix else ""
        citation = (
            f"{authors} ({year}). &quot;{cit_title}.&quot; "
            f"In <i>{cit_venue}</i>.{(' ' + suffix.strip()) if suffix else ''}"
        )

    lines = [
        "---",
        f'title: "{yaml_dq(title)}"',
        "collection: publications",
        f"category: {category}",
        f"permalink: {permalink}",
        f'excerpt: "{yaml_dq(excerpt)}"',
        f"date: {date_str}",
        f'venue: "{yaml_dq(venue)}"',
        f'paperurl: "{yaml_dq(paperurl)}"',
    ]
    if slidesurl:
        lines.append(f'slidesurl: "{yaml_dq(slidesurl)}"')
    if bibtexurl:
        lines.append(f'bibtexurl: "{yaml_dq(bibtexurl)}"')
    lines.append(f"citation: '{citation}'")
    lines.append("---")
    lines.append("")
    return filename, "\n".join(lines)


def main() -> int:
    p = argparse.ArgumentParser(description="Add a new publication entry.")
    p.add_argument("--category", required=True, choices=sorted(ALLOWED_CATEGORIES))
    p.add_argument("--date", required=True, help="YYYY-MM-DD")
    p.add_argument("--title", required=True)
    p.add_argument("--authors", required=True)
    p.add_argument("--year", required=True)
    p.add_argument("--venue", required=True)
    p.add_argument("--paperurl", default="")
    p.add_argument("--slidesurl", default="")
    p.add_argument("--bibtexurl", default="")
    p.add_argument("--excerpt", default=None)
    p.add_argument("--citation", default=None, help="Override the auto-generated citation.")
    p.add_argument("--slug", default=None, help="Override the auto-generated slug.")
    p.add_argument(
        "--extra-citation-suffix",
        default="",
        help='Extra trailing text for citation, e.g. "Vol. 6, pp. 445-456" or "Poster."',
    )
    p.add_argument(
        "--pub-dir",
        default=str(PUB_DIR_DEFAULT),
        help="Override the destination _publications/ directory.",
    )
    p.add_argument("--dry-run", action="store_true")
    p.add_argument("--force", action="store_true", help="Overwrite if the target file exists.")
    args = p.parse_args()

    filename, yaml_text = render_entry(
        title=args.title,
        authors=args.authors,
        year=args.year,
        venue=args.venue,
        date_str=args.date,
        category=args.category,
        paperurl=args.paperurl,
        slidesurl=args.slidesurl,
        bibtexurl=args.bibtexurl,
        excerpt=args.excerpt,
        citation=args.citation,
        slug=args.slug,
        extra_citation_suffix=args.extra_citation_suffix,
    )

    if args.dry_run:
        print(f"# would write: {filename}")
        print(yaml_text)
        return 0

    out = Path(args.pub_dir) / filename
    if out.exists() and not args.force:
        print(f"refusing to overwrite existing {out}; pass --force to override", file=sys.stderr)
        return 2
    out.write_text(yaml_text, encoding="utf-8")
    print(f"wrote {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
