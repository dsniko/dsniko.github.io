#!/usr/bin/env python3
"""Patch confirmed paperurl values into specific publication entries."""
from __future__ import annotations

import re
import sys
from pathlib import Path

PUB = Path("/sessions/lucid-hopeful-mendel/mnt/dsniko.github.io/_publications")

# (filename, paperurl, source/justification)
URLS: list[tuple[str, str, str]] = [
    # ---- High-confidence DOI / arXiv ----
    ("2001-01-01-iccs-interruptlets-java.md",
     "https://doi.org/10.1007/3-540-45545-0_31",
     "Springer LNCS ICCS 2001 chapter, exact title+author match"),
    ("2015-10-20-energy-efficient-hybrid-dram-nvm-poster.md",
     "https://ieeexplore.ieee.org/document/7429336/",
     "IEEE Xplore PACT 2015 ACM SRC poster, exact title+author match"),
    ("2017-09-01-taxonomy-task-based-technologies-hpc.md",
     "https://doi.org/10.1007/978-3-319-78054-2_25",
     "Springer LNCS PPAM 2017, exact title+author match"),
    ("2017-09-01-incremental-training-deep-cnns.md",
     "https://arxiv.org/abs/1803.10232",
     "arXiv preprint of the workshop paper, exact title+author match"),
    ("2025-10-01-vmil-memory-tiering-python.md",
     "https://doi.org/10.1145/3759548.3763372",
     "ACM DL VMIL 2025 paper, exact title+author match"),
    ("2025-11-18-polymorph-wacv.md",
     "https://arxiv.org/abs/2507.14959",
     "arXiv preprint of the WACV 2026 paper, exact title+author match"),
    ("2025-12-01-sled-speculative-llm-decoding.md",
     "https://doi.org/10.1145/3769102.3770608",
     "ACM DL ACM/IEEE SEC 2025 paper, exact title+author match"),
    ("2025-12-23-apex-ipdps.md",
     "https://arxiv.org/abs/2506.03296",
     "arXiv preprint of the IPDPS 2026 paper, exact title+author match"),
    ("2026-03-04-fan-dllm-serve-ics.md",
     "https://arxiv.org/abs/2512.17077",
     "arXiv preprint of the ICS 2026 paper, exact title+author match"),
    ("2026-02-16-marco-capwic.md",
     "https://arxiv.org/abs/2505.03906",
     "arXiv preprint of the CAPWIC 2026 paper, exact title+author match"),
    ("2026-03-04-moghadampanah-modality-inflation-iwapt.md",
     "https://arxiv.org/abs/2512.22695",
     "arXiv preprint of the iWAPT 2026 paper, exact title+author match"),
    ("2025-07-09-marvel-risc-v-extensions.md",
     "https://arxiv.org/abs/2508.01800",
     "arXiv preprint of the MARVEL paper, exact title+author match"),

    # ---- Institutional repository links (lower confidence) ----
    # These are pure.qub.ac.uk repository pages — they're stable institutional
    # links to the publication metadata for items without DOIs (keynotes,
    # ARM Research Summit talks, HiPEAC Info articles, etc.).
    ("2013-03-01-parallel-energy-pdp.md",
     "https://pure.qub.ac.uk/en/publications/connecting-the-dots-between-parallel-programming-and-energy",
     "QUB institutional repository entry for the PDP 2013 keynote"),
    ("2014-04-01-nanostreams-hipeac.md",
     "https://pure.qub.ac.uk/en/publications/nanostreams-a-hardware-and-software-stack-for-real-time-analytics",
     "QUB institutional repository entry for the HiPEAC Info article"),
    ("2017-09-01-energy-efficiency-armv8-microservers.md",
     "https://pure.qub.ac.uk/en/publications/energy-efficiency-in-armv8-based-microservers-by-hardware-margins",
     "QUB institutional repository entry for the ARM Research Summit 2017 talk"),
    ("2017-09-01-reliability-aware-system-software-arm.md",
     "https://pure.qub.ac.uk/en/publications/reliability-aware-system-software-support-on-arm-microservers",
     "QUB institutional repository entry for the ARM Research Summit 2017 talk"),
]


def patch_paperurl(text: str, url: str) -> str:
    pat = re.compile(r"^paperurl:\s*.*$", re.MULTILINE)
    if pat.search(text):
        return pat.sub(f'paperurl: "{url}"', text, count=1)
    end = text.find("\n---", 4)
    return text[:end] + f'\npaperurl: "{url}"' + text[end:]


def main() -> int:
    patched: list[str] = []
    missing: list[str] = []
    for fname, url, _ in URLS:
        p = PUB / fname
        if not p.exists():
            missing.append(fname)
            continue
        text = p.read_text(encoding="utf-8")
        new_text = patch_paperurl(text, url)
        if new_text != text:
            p.write_text(new_text, encoding="utf-8")
            patched.append(f"{fname}: {url}")
    print(f"# Patched {len(patched)} entries:")
    for line in patched:
        print(f"  {line}")
    if missing:
        print(f"\n# Missing files:")
        for m in missing:
            print(f"  {m}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
