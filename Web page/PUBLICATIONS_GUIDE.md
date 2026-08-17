# Publications — format, audit, and how to add new entries

This is a working note for the `_publications/` folder of the
`dsniko.github.io` site (an Academic Pages / Jekyll site). It explains the
exact `.md` format used today, the small irregularities that exist across the
350 entries, and how to add or audit publications quickly.

---

## 1. Where things live

| Path | Purpose |
|---|---|
| `_publications/*.md` | One file per publication. Front matter only — body is empty. |
| `_publications/new_entries.zsh` | Existing helper script for batch-adding posters from SC '25. |
| `_pages/publications.html` | Section page; iterates `site.publications` by category. |
| `_includes/archive-single.html` | Renders one entry: title link, venue/year, excerpt, `Download Paper` link from `paperurl`. |
| `_config.yml` → `publication_category:` | Authoritative list of valid `category` values. |

The page renders categories in the order defined in `_config.yml`
(`books → manuscripts → conferences → workshops → bookchapters → magazines → posters → volumes → invited → keynotes → techreports`).

---

## 2. Canonical front matter

A publication entry is **only** YAML front matter (no body). Fields below in
**bold** are required for the page to render correctly.

```yaml
---
title: "FULL TITLE — keep punctuation as in print"
collection: publications
category: conferences           # see allowed list below
permalink: /publication/YYYY-MM-DD-short-slug
excerpt: "One- or two-sentence summary used on the listing page."
date: YYYY-MM-DD
venue: "Proceedings of … / Journal name"
paperurl: "https://…"           # leave as "" if no public URL yet
slidesurl: ""                   # optional
bibtexurl: ""                   # optional
citation: 'Last, F., & Nikolopoulos, D. S. (YEAR). &quot;Full Title.&quot; In <i>Venue</i>.'
---
```

Required: **title, collection, category, permalink, date**.
Strongly recommended: **excerpt, venue, paperurl, citation**.

Allowed `category` values (from `_config.yml`):

```
books, manuscripts, conferences, workshops, bookchapters, magazines,
posters, volumes, invited, keynotes, techreports
```

Filename convention: `YYYY-MM-DD-<slug>.md`, where `<slug>` is the lowercase,
dash-joined version of the title. The `permalink` should be
`/publication/<filename without .md>` — i.e. the file `2026-06-01-foo-bar.md`
should set `permalink: /publication/2026-06-01-foo-bar`.

Notes on quoting (these are subtle and matter):
- `title:` uses **double quotes**. Escape any internal `"` as `\"`.
- `citation:` uses **single quotes** at the YAML level so that it can contain
  HTML (`<i>…</i>`). Replace internal `"` characters with `&quot;` so the HTML
  renders cleanly.
- `paperurl:` empty value is fine (`paperurl: ""`); the template
  `archive-single.html` simply omits the `Download Paper` link in that case.

---

## 3. Fast audit summary (run on 2026-04-30, post-fix)

350 markdown files audited. **0 hard errors, 60 informational warnings**
(58 missing-paperurl + 2 missing-venue). Categories present:

| Category | Count |
|---|---|
| `conferences` | 154 |
| `manuscripts` | 74 |
| `workshops` | 38 |
| `techreports` | 31 |
| `volumes` | 19 |
| `posters` | 13 |
| `bookchapters` | 7 |
| `invited` | 6 |
| `keynotes` | 6 |
| `magazines` | 2 |
| **Total** | **350** |

(Category `books` exists in `_config.yml` but no entries currently use it.)

### 3.1 Hard errors (0)

`2014-11-16-e2sc.md` was the only blocker (old `type: volumes` schema,
no `permalink`, no `excerpt`, no `citation`); it has been rewritten to
the standard Academic Pages schema and now renders under "Edited Volumes
and Special Issues."

### 3.2 Filename / permalink mismatches — fixed

The 14 mismatch cases were patched in place:

- 10 permalink-slug fixes (filename stem now wins): `comparison-online-offline-strategies`, `nanostreams-advancing-hardware-software`, `access-aware-dram-failure-rate`, `error-resilient-server-ecosystems`, `welcome-general-chairs-ispass`, `vineyard-integrated-framework-accelerators`, `implementing-efficient-message-logging`, `hired-attention-token-dropping`, `diffpro-arxiv`, plus `…-server-ecosystem` whose permalink date was off by a month.
- 3 date-mismatch fixes (filename date wins): `marco`, `polymorph-wacv`, `apex-ipdps` (the frontmatter dates `2025-05-06`, `2026-01-15`, `2026-01-15` were aligned to the filename dates). Update those manually if the print date differs from the filename date.
- 1 OneDrive conflict-style filename: renamed
  `2018-12-01-dynamic-precision-refinement 2025-05-20 02_25_29.md` →
  `2018-12-01-dynamic-precision-refinement.md`.
- 1 dot-vs-dash typo: renamed
  `2020-11-01-enorm-edge-resource.management.md` →
  `…-resource-management.md`.

### 3.3 Filenames missing the day component — fixed

All four were renamed to `YYYY-MM-DD-<slug>.md`:

| Old | New |
|---|---|
| `2011-cluster-ppac-workshop.md` | `2011-01-01-cluster-ppac-workshop.md` |
| `2020-01-0-feasibility-fog-computing.md` | `2020-01-01-feasibility-fog-computing.md` |
| `2023-hotinfra-fine-grain-slicing.md` | `2023-01-01-hotinfra-fine-grain-slicing.md` |
| `2025-marvel-risc-v-extensions.md` | `2025-07-09-marvel-risc-v-extensions.md` |

(Where the original lacked a day, `01` was used; for `marvel`, the
frontmatter date `2025-07-09` was used in the filename.)

### 3.4 Missing `paperurl` (58)

Roughly one entry in six has no `paperurl`. Most of these are pre-2015
papers, posters, keynotes, and forewords that legitimately don't have a
public URL. The full list with titles is at
`publications_audit.md` § "Entries missing `paperurl`" and as a column in
`publications_audit.csv` / `publications_urls.csv`.

If you'd like me to mine arXiv / DOI / publisher URLs for any of these and
patch them in, just point me at a subset.

### 3.5 Missing `venue` (2)

These two newer entries have no venue set yet:

- `2025-12-23-dllm.md`
- `2026-01-23-wisp.md`

(Both also exist in expanded form: `2026-03-04-fan-dllm-serve-ics.md` and
`2026-06-01-wisp-sigmetrics.md`. You may want to delete the placeholders
or fill in their venue.)

---

## 4. Tracing URLs across publications

`publications_urls.csv` is the per-entry URL map. Columns:

```
file, title, category, paperurl, other_urls
```

`other_urls` aggregates `slidesurl`, `bibtexurl`, and any URLs that appear
inside `citation` / `excerpt`. To find every entry pointing at a host, just
grep the CSV — for example:

```sh
# all arxiv links across publications
awk -F, 'NR>1 && ($4 ~ /arxiv/ || $5 ~ /arxiv/) {print $1": "$4" "$5}' publications_urls.csv

# all entries with no link at all
awk -F, 'NR>1 && $4=="" && $5=="" {print $1": "$2}' publications_urls.csv
```

Or, on the publication source files directly:

```sh
# every URL that appears in the entire publications corpus
grep -horE 'https?://[^"<> )]+' _publications/ | sort -u
```

---

## 5. Adding a new publication

Two equivalent options.

### 5.1 Copy the template

`publication_template.md` is the canonical empty entry:

```yaml
---
title: "FULL TITLE — keep punctuation as in print"
collection: publications
category: conferences
permalink: /publication/YYYY-MM-DD-short-slug
excerpt: "One- or two-sentence summary used on the listing page."
date: YYYY-MM-DD
venue: "Proceedings of … / Journal name"
paperurl: "https://…"
slidesurl: ""
bibtexurl: ""
citation: 'Last, F., & Nikolopoulos, D. S. (YEAR). &quot;Full Title.&quot; In <i>Venue</i>.'
---
```

Save it as `_publications/YYYY-MM-DD-<slug>.md`. Done.

### 5.2 Use the `add_publication.py` helper

`add_publication.py` writes a properly formatted file from CLI args and
will refuse to overwrite an existing file unless `--force` is passed. Use
`--dry-run` to preview the YAML.

```sh
python3 add_publication.py \
  --category conferences \
  --date 2026-09-15 \
  --title "Cool Paper Title" \
  --authors "Foo, B., Bar, A., & Nikolopoulos, D. S." \
  --year 2026 \
  --venue "Proceedings of XYZ '26" \
  --paperurl "https://arxiv.org/abs/2609.12345" \
  --excerpt "One-sentence abstract for the listing." \
  --pub-dir "/Users/dsn/Library/CloudStorage/OneDrive-VirginiaTech/Web/dsniko.github.io/_publications"
```

That writes `2026-09-15-cool-paper-title.md` with a permalink of
`/publication/2026-09-15-cool-paper-title` and a citation matching the
existing house style.

For multi-entry batches (e.g. all the posters from one conference), the
existing `new_entries.zsh` pattern in `_publications/` is still the
fastest way: copy it, change the metadata at the top, list the
`write_entry "..." "..." "..."` calls, run it.

---

## 6. Applied fixes

All audit findings from §3 except the legitimate "missing paperurl" /
"missing venue" cases were applied in place by `apply_fixes.py` (also
saved to this folder for reference). To re-run the same fixes from a
fresh checkout, just `python3 apply_fixes.py`. The script is
idempotent — it edits front-matter fields by name and refuses to clobber
rename targets that already exist.

---

## 7. Re-running the audit

```sh
python3 audit_publications.py
```

This regenerates three files in `outputs/`:

- `publications_audit.md`  — human-readable report (errors, warnings, counts)
- `publications_audit.csv` — one row per file, with `errors` and `warnings` columns
- `publications_urls.csv`  — one row per file, listing every URL it references

The script lives in this folder; copy it into the repo (e.g.
`scripts/audit_publications.py`) if you want to make it part of a CI check.
