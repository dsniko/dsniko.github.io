#!/usr/bin/env zsh
# Usage: ./generate_undergrads_vt_2023.zsh [output_dir]
# Default output dir: .   (must already exist; script does NOT create it)

set -e
set -u
set -o pipefail

OUTDIR="${1:-.}"
[[ -d "$OUTDIR" ]] || { print -r -- "Error: output dir '$OUTDIR' does not exist."; exit 1; }

# TSV columns: name <TAB> end_year <TAB> thesis_title <TAB> department
DATA=$(cat <<'TSV'
Jack Williamson    2023    Supporting flexible SIMD ISAs in WebAssembly    Computer Science, Virginia Tech
Anthony Nguyen    2023    WebAssembly Performance Profiling    Computer Science, Virginia Tech
Alex Lin    2023    Supporting GPUs in WebAssembly    Computer Science, Virginia Tech
Gianfranco Vivanco    2023    Performance Characterization of LLM Inference    Computer Science, Virginia Tech
Tatiana Monteiro    2023    Optimization of Inference from Decision Trees    Computer Science, Virginia Tech
Jamie Whiting    2023    RISC-V Simulation and System Software    Computer Science, Virginia Tech
Riyos Pudasaini    2023    Scalable Memory Allocators for Rust    Computer Science, Virginia Tech
TSV
)

slugify() {
  local s="$1"
  if command -v iconv >/dev/null 2>&1; then
    s="$(print -r -- "$s" | iconv -t ascii//TRANSLIT 2>/dev/null || print -r -- "$s")"
  fi
  s="$(print -r -- "$s" \
      | tr '[:upper:]' '[:lower:]' \
      | sed -E 's/[^a-z0-9]+/-/g; s/-{2,}/-/g; s/^-+|-+$//g')"
  print -r -- "$s"
}

strip_trailing_period() {
  print -r -- "$1" | sed -E 's/[[:space:]]*\.$//'
}

escape_yaml() {
  print -r -- "$1" | sed -e 's/\\/\\\\/g' -e 's/"/\\"/g'
}

while IFS=$'\t' read -r name end_year thesis_raw department; do
  [[ -z "${name:-}" ]] && continue

  thesis="$(strip_trailing_period "$thesis_raw")"

  # Permalink slug per your pattern: <name> <year> <thesis> <department> ug
  slug_input="${name} ${end_year} ${thesis} ${department} ug"
  slug="$(slugify "$slug_input")"
  file="$OUTDIR/${slug}.md"

  title="$(escape_yaml "$name")"
  thesis_esc="$(escape_yaml "$thesis")"
  dept_esc="$(escape_yaml "$department")"

  if [[ -e "$file" ]]; then
    print -r -- "Skip (exists): $file"
    continue
  fi

  cat > "$file" <<YAML
---
title: "$title"
collection: mentees
permalink: /mentee/${slug}
category: undergrad
end_year: $end_year
status: alumni
thesis_title: "$thesis_esc"
department: "$dept_esc"
current_position: ""
website: ""
scholar: ""
---
YAML

  print -r -- "Wrote $file"
done <<< "$DATA"
