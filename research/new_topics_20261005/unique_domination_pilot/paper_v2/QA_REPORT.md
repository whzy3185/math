# Manuscript quality assurance

Version 2, 5 October 2026.

## Build and visual review

Two pdfLaTeX passes using build.sh succeeded. The final build log has no LaTeX warnings, undefined citations or references, overfull boxes or underfull boxes. The PDF has 10 A4 pages, 25 mm margins, and 11-point text.

Every page was rendered at a 1550-pixel long edge and individually inspected. The title and attribution are legible on page 1; both main theorems remain together on page 2; the shared local lemmas fit on page 4; the complete second-boundary case analysis occupies pages 7–8; the supplementary tables and all references are clean on pages 9–10. There is no clipping, overlap, missing symbol, stranded heading or reference-only near-empty final page.

The workspace-local TeX format and font map avoid changing system configuration.

## Mathematical integration checklist

- Both graph classes retain finiteness, simplicity, bipartiteness, absence of isolated vertices and unique minimum-cardinality domination
- The first equality statement is now all γ≥2, with the audited low-γ proof included
- The second equality statement asserts only connected attainment and at least two nonisomorphic even-γ examples
- The construction formula is restricted here to r=1,2; no general-r extremal theorem is implied
- Every local replacement keeps the residual vertices dominated or includes them in its cell
- The opposite-side edge zw is counted exactly once
- The p=0 and q=1 boundary cases remain explicit
- The exceptional possible one-edge excess for even γ is excluded by an explicit second dominating set
- The source's six-vertex argument is credited
- Erlbacher's earlier n=13 and n=14 examples, q=1 family, and cutoff observation are credited
- All four local pattern counts and the two family-value columns match exact certificates
- No Lean verification, journal peer review or exhaustive priority claim is made

The underlying three mathematical components have independent audit PASS reports. The final integrated manuscript review also passed, with no revision requested; see audit/FINAL_INTEGRATED_REVIEW.md. The reviewer independently checked the written proofs, actual pinned prior source and all ten rendered pages.
