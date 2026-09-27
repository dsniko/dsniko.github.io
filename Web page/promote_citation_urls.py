#!/usr/bin/env python3
"""For each entry with empty paperurl but a URL inside citation, promote it.

Looks for the first http(s) URL in the citation field and writes it as
paperurl. Reports what was patched.
"""
from __future__ import annotations

import re
from pathlib import Path

import yaml

PUB = Path("/sessions/lucid-hopeful-mendel/mnt/dsniko.github.io/_publications")
URL_RE = re.compile(r"https?://[^\s\"'<>)\]]+")


def split_fm(text: str) -> tuple[str, str, int]:
    """Return (frontmatter_yaml, body, end_index_of_closing_---)."""
    if not text.startswith("---"):
        return "", text, -1
    rest = text.split("\n", 1)[1] if "\n" in text else ""
    end = rest.find("\n---")
    if end == -1:
        return "", text, -1
    return rest[:end], text[len(text) - len(rest) + end + 4 :], end


def patch_field(text: str, field: str, value: str) -> str:
    pat = re.compile(rf"^({re.escape(field)}):\s*.*$", re.MULTILINE)
    if pat.search(text):
        return pat.sub(f'{field}: "{value}"', text, count=1)
    # Insert before closing ---
    end = text.find("\n---", 4)
    return text[:end] + f'\n{field}: "{value}"' + text[end:]


def main() -> int:
    patched: list[tuple[str, str]] = []
    skipped: list[str] = []

    for p in sorted(PUB.iterdir()):
        if p.suffix != ".md":
            continue
        text = p.read_text(encoding="utf-8")
        fm_text, _, _ = split_fm(text)
        if not fm_text:
            continue
        try:
            fm = yaml.safe_load(fm_text) or {}
        except Exception:
            continue
        pu = (fm.get("paperurl") or "").strip()
        if pu:
            continue
        cit = fm.get("citation") or ""
        if not isinstance(cit, str):
            continue
        m = URL_RE.search(cit)
        if not m:
            continue
        url = m.group(0).rstrip(".,;)")
        # Skip URLs that aren't paper-pointing (e.g., institution homepages)
        if "doi.org" not in url and "arxiv.org" not in url and \
           "dl.acm.org" not in url and "ieeexplore" not in url and \
           "springer" not in url and "sciencedirect" not in url and \
           "computer.org" not in url and "usenix.org" not in url and \
           "researchgate" not in url and "openaccess" not in url and \
           "openreview" not in url:
            skipped.append(f"{p.name}: non-paper URL {url}")
            continue

        new_text = patch_field(text, "paperurl", url)
        if new_text != text:
            p.write_text(new_text, encoding="utf-8")
            patched.append((p.name, url))

    print(f"# Promoted {len(patched)} URLs from citation -> paperurl:")
    for f, u in patched:
        print(f"  {f}: {u}")
    if skipped:
        print(f"\n# Skipped {len(skipped)} non-paper URLs:")
        for s in skipped:
            print(f"  {s}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
