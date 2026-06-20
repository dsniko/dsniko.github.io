# Mentees page — accuracy review & redesign notes

_Generated from the live `_mentees` collection (125 records) on 2026-06-20._

## Verified counts (these are correct on the current page)

| Group | Count |
|---|---|
| Current students (all PhD) | 9 |
| PhD graduates | 27 |
| **PhD students, total** | **36** (27 graduated + 9 current) |
| Postdocs | 17 |
| Master's students | 29 |
| Undergraduate researchers | 43 |
| **Total mentees** | **125** |

Placement of the 92 graduated mentees with a known current role: **63 in industry, 18 in academia, 11 at national labs / research institutes** (24 alumni have no position listed yet).

## Accuracy issues found

1. **About page is out of date.** `_pages/about.md` (line ~35) says Dimitrios
   "has mentored **24 Ph.D. students and 16 postdoctoral researchers**." The collection
   now holds **36 PhD students (27 graduated + 9 current) and 17 postdocs.**
   Suggested wording: *"mentored 36 Ph.D. students (27 graduated) and 17 postdoctoral researchers."*
   **Not changed automatically** — confirm the framing you prefer (e.g. graduated-only vs. total) and I'll edit it.

2. **Two malformed LinkedIn URLs — FIXED in the live source:**
   - `riyos-pudasaini-…-ug.md` had a trailing `""` (link rendered broken). ✅ corrected
   - `2015-02-01-aleksandr-khasymski.md` had a trailing `//`. ✅ corrected

3. **24 alumni have no `current_position`.** Not an error, but filling these would make the
   "Where they are now" band more complete. Optional.

## What the redesign adds (visual)

- A **stats band** (total + per-category counts) at the top, auto-computed from the collection.
- A **"Where they are now"** placement bar (industry / academia / national labs), auto-computed.
- **Current students as a card grid** instead of a plain list, with co-advisor noted.
- **Alumni as clean, bordered rows** grouped by category, with position emphasized.
- (Mockup only) a live **search + category filter** over the alumni.

## Files in this folder

| File | Purpose |
|---|---|
| `mentees-redesign-mockup.html` | Standalone visual preview — open in any browser. Includes search/filter. |
| `mentees.md` | Drop-in replacement for `_pages/mentees.md` (still 100% data-driven). |
| `_mentees.scss` | Companion styles → save as `_sass/_mentees.scss`, then add `@import "mentees";` to `assets/css/main.scss`. |

The mockup's interactive search is plain JS for preview purposes; the Jekyll `mentees.md`
keeps the same look using your theme's CSS (search can be added later if you want it live).
