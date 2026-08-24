# Task 58 Manuscript Build Baseline

Status: `TASK58_3_SCAFFOLD_COMPILED_AND_RENDERED`.

## Current artifacts

| Artifact | Value |
|---|---|
| Manuscript root | `research/paper/manuscript_tex_task58/` |
| Identified source | `main.tex` |
| Anonymous source | `main_anonymous.tex` |
| Identified PDF | `main.pdf` |
| Anonymous PDF | `main_anonymous.pdf` |
| Page count | 4 for each entry point |
| Numbered sections | 8 |
| Unnumbered availability section | 1 |
| Essential appendices | 2 |
| Grayscale TikZ source budget | 3 |
| Exact draft-stub markers | 34 |

The final clean build commands were:

```text
tectonic main.tex
tectonic main_anonymous.tex
```

Both commands exited successfully and emitted no TeX or BibTeX warning. The
PDF page size is 612 by 792 points (US Letter), PDF version 1.5. No auxiliary,
log, or cache file is part of the manuscript tree.

## Reuse record

The new tree reuses only the following harmless infrastructure from
`research/paper/manuscript_tex_pub/`:

- the standard 11 pt article choice and stable package family;
- anonymous-entry mechanics;
- author-metadata placeholders;
- the BibTeX build pattern; and
- a byte-for-byte mechanical copy of `references.bib`.

No old abstract, section, theorem, proof, caption, table, or other mathematical
prose was copied. The new title, eight-section tree, appendix boundary, and
draft files were created from the locked Task 58 blueprint.

## Freeze and validation

The historical English tree remains
`59e3a8f73a152ef06f994e979b7219a3365efeae`; the historical Chinese tree
remains `57ae03fb5b90866f84d0d72b414008678e8f5004`. The Task 58.3 verifier checks
these hashes, the full file inventory, bibliography identity, section and
appendix counts, unified stub policy, stale-claim blacklist, absence of
footnotes, and existence of the compiled PDF.

The scaffold is a build baseline, not a mathematical draft. Its sparse pages
measure only the source structure and typography; manuscript page forecasts
remain 28--32 pages for the main narrative and 36--42 with the essential
appendices.
