#!/usr/bin/env python3
"""Apply audit fixes in place to _publications/."""
from __future__ import annotations

import os
import re
import shutil
import sys
from pathlib import Path

PUB = Path("/sessions/lucid-hopeful-mendel/mnt/dsniko.github.io/_publications")

# ----------------------------------------------------------------------
# A) Rewrite the e2sc.md entry to the standard Academic Pages schema.
# ----------------------------------------------------------------------
E2SC_NEW = '''---
title: "Proceedings of the 2nd International Workshop on Energy Efficient Supercomputing"
collection: publications
category: volumes
permalink: /publication/2014-11-16-e2sc
excerpt: "Edited proceedings of the 2nd International Workshop on Energy Efficient Supercomputing (E2SC), held with SC'14 in New Orleans, LA."
date: 2014-11-16
venue: "International Conference for High Performance Computing, Networking, Storage and Analysis (SC)"
paperurl: "https://dl.acm.org/doi/proceedings/10.5555/2689710"
citation: 'Cameron, K., Hoisie, A., Kerbyson, D., Lowenthal, D., Nikolopoulos, D. S., Yalamanchili, S., & Marquez, A. (Eds.) (2014). &quot;Proceedings of the 2nd International Workshop on Energy Efficient Supercomputing.&quot; IEEE. ISBN 978-1-4799-7036-0.'
---
'''

# ----------------------------------------------------------------------
# B) File renames.  (old_name, new_name).  None means no rename, just edit.
# ----------------------------------------------------------------------
RENAMES = [
    # OneDrive conflict-style filename
    ("2018-12-01-dynamic-precision-refinement 2025-05-20 02_25_29.md",
     "2018-12-01-dynamic-precision-refinement.md"),
    # `.` instead of `-` in the filename
    ("2020-11-01-enorm-edge-resource.management.md",
     "2020-11-01-enorm-edge-resource-management.md"),
    # Filenames missing the day component
    ("2011-cluster-ppac-workshop.md",
     "2011-01-01-cluster-ppac-workshop.md"),
    ("2020-01-0-feasibility-fog-computing.md",
     "2020-01-01-feasibility-fog-computing.md"),
    ("2023-hotinfra-fine-grain-slicing.md",
     "2023-01-01-hotinfra-fine-grain-slicing.md"),
    ("2025-marvel-risc-v-extensions.md",
     "2025-07-09-marvel-risc-v-extensions.md"),
]

# ----------------------------------------------------------------------
# C) Permalink (and optional date) alignment.
#    Keyed by NEW filename (after any rename above).
# ----------------------------------------------------------------------
ALIGNMENTS: dict[str, dict[str, str]] = {
    # Pure permalink alignments (filename stem wins)
    "2007-03-01-comparison-online-offline-strategies.md": {
        "permalink": "/publication/2007-03-01-comparison-online-offline-strategies",
    },
    "2014-10-01-nanostreams-advancing-hardware-software.md": {
        "permalink": "/publication/2014-10-01-nanostreams-advancing-hardware-software",
    },
    "2016-12-02-energy-efficient-error-resilient-server-ecosystem.md": {
        "permalink": "/publication/2016-12-02-energy-efficient-error-resilient-server-ecosystem",
    },
    "2017-07-01-access-aware-dram-failure-rate.md": {
        "permalink": "/publication/2017-07-01-access-aware-dram-failure-rate",
    },
    "2017-12-01-error-resilient-server-ecosystems.md": {
        "permalink": "/publication/2017-12-01-error-resilient-server-ecosystems",
    },
    "2018-04-01-welcome-general-chairs-ispass.md": {
        "permalink": "/publication/2018-04-01-welcome-general-chairs-ispass",
    },
    "2018-07-01-vineyard-integrated-framework-accelerators.md": {
        "permalink": "/publication/2018-07-01-vineyard-integrated-framework-accelerators",
    },
    "2019-09-01-implementing-efficient-message-logging.md": {
        "permalink": "/publication/2019-09-01-implementing-efficient-message-logging",
    },
    "2025-04-11-hired-attention-token-dropping.md": {
        "permalink": "/publication/2025-04-11-hired-attention-token-dropping",
    },
    "2025-11-20-diffpro-arxiv.md": {
        "permalink": "/publication/2025-11-20-diffpro-arxiv",
    },
    # Permalink + date alignments (filename date wins)
    "2025-05-01-marco.md": {
        "permalink": "/publication/2025-05-01-marco",
        "date": "2025-05-01",
    },
    "2025-11-18-polymorph-wacv.md": {
        "permalink": "/publication/2025-11-18-polymorph-wacv",
        "date": "2025-11-18",
    },
    "2025-12-23-apex-ipdps.md": {
        "permalink": "/publication/2025-12-23-apex-ipdps",
        "date": "2025-12-23",
    },
    # Renamed-file permalinks (filename stem wins)
    "2018-12-01-dynamic-precision-refinement.md": {
        "permalink": "/publication/2018-12-01-dynamic-precision-refinement",
    },
    "2020-11-01-enorm-edge-resource-management.md": {
        "permalink": "/publication/2020-11-01-enorm-edge-resource-management",
    },
    "2011-01-01-cluster-ppac-workshop.md": {
        "permalink": "/publication/2011-01-01-cluster-ppac-workshop",
    },
    "2020-01-01-feasibility-fog-computing.md": {
        "permalink": "/publication/2020-01-01-feasibility-fog-computing",
    },
    "2023-01-01-hotinfra-fine-grain-slicing.md": {
        "permalink": "/publication/2023-01-01-hotinfra-fine-grain-slicing",
    },
    "2025-07-09-marvel-risc-v-extensions.md": {
        "permalink": "/publication/2025-07-09-marvel-risc-v-extensions",
    },
}


def patch_yaml_field(text: str, field: str, new_value: str) -> str:
    """Replace `^<field>: …` (single line) in the YAML frontmatter."""
    pat = re.compile(rf"^({re.escape(field)}):\s*.*$", re.MULTILINE)
    if not pat.search(text):
        # field not present: insert before the closing '---'
        end = text.find("\n---", 4)
        if end == -1:
            raise ValueError(f"frontmatter not closed; cannot insert {field}")
        return text[:end] + f"\n{field}: {new_value}" + text[end:]
    return pat.sub(f"{field}: {new_value}", text, count=1)


def main() -> int:
    actions: list[str] = []
    errors: list[str] = []

    # Step A: rewrite e2sc
    target = PUB / "2014-11-16-e2sc.md"
    if target.exists():
        target.write_text(E2SC_NEW, encoding="utf-8")
        actions.append(f"rewrote {target.name}")
    else:
        errors.append(f"missing {target}")

    # Step B: renames
    for old, new in RENAMES:
        op, np = PUB / old, PUB / new
        if not op.exists():
            errors.append(f"rename source missing: {old}")
            continue
        if np.exists():
            errors.append(f"rename target already exists: {new} (skipping)")
            continue
        shutil.move(str(op), str(np))
        actions.append(f"renamed {old} -> {new}")

    # Step C: permalink/date alignments
    for fname, fields in ALIGNMENTS.items():
        p = PUB / fname
        if not p.exists():
            errors.append(f"alignment target missing: {fname}")
            continue
        text = p.read_text(encoding="utf-8")
        new_text = text
        for k, v in fields.items():
            new_text = patch_yaml_field(new_text, k, v)
        if new_text != text:
            p.write_text(new_text, encoding="utf-8")
            actions.append(f"patched {fname}: {list(fields.keys())}")

    print("# Actions")
    for a in actions:
        print(f"  {a}")
    if errors:
        print("\n# Errors")
        for e in errors:
            print(f"  {e}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
