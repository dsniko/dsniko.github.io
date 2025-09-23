#!/usr/bin/env zsh
set -euo pipefail

# Where to write the markdown files
OUT_DIR="_publications"
mkdir -p "$OUT_DIR"

# Common metadata
DATE="2025-11-01"  # adjust if you want a specific SC'25 day
VENUE_SHORT="SC 2025 (St. Louis, MO) — Poster"
VENUE_CIT_HTML="Proceedings of the International Conference on High Performance Computing, Networking, Storage and Analysis (SC25)"
LOCATION="St. Louis, MO"

slugify() {
  # lower-case, replace non-alnum with dashes, trim dashes
  # requires iconv (usually present)
  local s="$1"
  print -r -- "$s" \
  | iconv -t ascii//TRANSLIT 2>/dev/null \
  | tr '[:upper:]' '[:lower:]' \
  | sed -E 's/[^a-z0-9]+/-/g; s/^-+//; s/-+$//'
}

yaml_escape() {
  # escape double quotes for YAML
  local s="$1"
  print -r -- "$s" | sed 's/"/\\"/g'
}

html_quote() {
  # replace " with &quot; for the citation field (which is HTML-capable)
  local s="$1"
  print -r -- "$s" | sed 's/"/\&quot;/g'
}

write_entry() {
  local title="$1"
  local authors="$2"
  local year="$3"

  # Clean LaTeX non-breaking spaces (~) in author names for display
  local authors_clean
  authors_clean=$(print -r -- "$authors" | sed 's/~//g')

  local slug
  slug=$(slugify "$title")
  local permalink="/publication/${DATE}-${slug}"

  local title_yaml
  title_yaml=$(yaml_escape "$title")

  local title_cit
  title_cit=$(html_quote "$title")

  local filename="${OUT_DIR}/${DATE}-${slug}.md"

  cat > "$filename" <<EOF
---
title: "${title_yaml}"
collection: publications
category: posters
permalink: ${permalink}
excerpt: "Refereed poster: ${title_yaml}."
date: ${DATE}
venue: "${VENUE_SHORT}"
paperurl: ""
citation: '${authors_clean} (${year}). &quot;${title_cit}.&quot; In <i>${VENUE_CIT_HTML}</i>. Poster.'
---
EOF

  echo "Wrote: $filename"
}

# ---- Posters to add ----
# 1) Energy-Efficient Multimodal LLM Inference
write_entry \
  "Energy-Efficient Multimodal LLM Inference: Stage-Level Characterization and Input-Aware Controls" \
  "Mona Moghadampanah, Adib Rezaei Shahmirzadi, and Dimitrios S. Nikolopoulos" \
  "2025"

# 2) HydraCache
write_entry \
  "HydraCache: Long-Context Prefill Parallelization via Distributed Cache Blending" \
  "Adib Rezaei Shahmirzadi, Shayan Shabihi, Furong Huang, and Dimitrios S. Nikolopoulos" \
  "2025"

# 3) Divide, Conquer, and Denoise (Parallel Diffusion)
write_entry \
  "Divide, Conquer, and Denoise: Hybrid Parallel Diffusion with Memory-Aware Coarse-to-Fine Inference" \
  "Farhana Amin, Kanchon Gharami, and Dimitrios S. Nikolopoulos" \
  "2025"

# 4) DiffPro
write_entry \
  "DiffPro: Joint Timestep and Layer-Wise Precision Optimization for Efficient Diffusion Inference" \
  "Farhana Amin, Kanchon Gharami, and Dimitrios S. Nikolopoulos" \
  "2025"
