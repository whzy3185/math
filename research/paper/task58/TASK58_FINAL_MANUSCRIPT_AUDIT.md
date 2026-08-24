# Task 58 Final Manuscript Audit

Status: `ANONYMOUS_REVIEW_PACKAGE_READY`; identified-submission metadata and
immutable archive pending.

## Package summary

| Item | Final audit value |
|---|---|
| Title | *Spectral Radius Minimization for Signed Squares of Cycles* |
| Abstract | 153 source words, six sentences |
| Identified-source PDF | 38 pages; author metadata placeholders remain |
| Anonymous PDF | 38 pages; repository and SHA suppressed |
| Main narrative | 23 pages |
| Appendix A | pages 24--30, algebraic G6 certification |
| Appendix B | pages 31--37, exact finite classification |
| Bibliography | page 38 |
| Supplement | 13 pages |
| Main-text figures | 3 |
| Main-paper tables | 7 |
| Draft stubs | 0 |
| Author footnotes | 0 |
| Historical manuscripts | both frozen tree hashes PASS |

## Build result

Clean-state Tectonic 0.17.0 builds were run into independent temporary output
directories:

```text
tectonic --keep-intermediates --outdir <tmp-main> main.tex
tectonic --keep-intermediates --outdir <tmp-anon> main_anonymous.tex
tectonic --keep-intermediates --outdir <tmp-supp> main.tex
```

All three builds completed without TeX or BibTeX warnings. The source trees
contain no auxiliary, log, output, or synchronization files. The tracked PDFs
are:

```text
research/paper/manuscript_tex_task58/main.pdf
research/paper/manuscript_tex_task58/main_anonymous.pdf
research/paper/manuscript_tex_task58_supplement/main.pdf
```

## Theorem inventory

The main paper contains 4 theorem environments, 8 propositions, and 5 lemmas.
The publication hierarchy is:

1. complete truth classification for every even order;
2. analytic candidate attainment at every even order;
3. exact period-eight reference edge;
4. charge and translation-sector laws;
5. G6 essential spectrum, physical global edge, and rank-two squared level;
6. complete abnormal positive single-gap hierarchy;
7. finite-ring patch/IMS cap and residue limsup bounds;
8. analytic strict-failure tail for every even order at least 240;
9. exact finite closure through 238 and sharp continuous onset 48; and
10. exact-`2r` separated-interface cluster as a structural refinement only.

The exact-`2r` full proof, its Feshbach constants, the sufficient nonoptimal
exponential onset `N_exp=3120`, and all single-gap integer witnesses are in the
separate supplement.

## Classification consistency

The Abstract, Introduction theorem, Section 7 synthesis, and Conclusion all
state the same result:

```text
m_n < rho_-(n)
if and only if n=32, n=40, or n is even and n>=48.
```

The equality set is consistently

```text
8,10,12,14,16,18,20,22,24,26,28,30,34,36,38,42,44,46.
```

Order 32 is called the first failure, not the continuous onset. The analytic
tail begins at 240. Continuous failure begins at 48 only after combining the
96-order exact bridge with the analytic tail.

## Computer-assisted theorem inventory

| Component | Exact finite object | Verification boundary | Consequence |
|---|---|---|---|
| G6 edge | transfers, local root interval, Grassmann atlas, resultants | exact interval signs, Sturm counts, two coordinate exclusions | `sup spec(H_6)=c_6`, rank two |
| Even 8--30 | full switching/flux quotient decisions | integer and algebraic reconstruction | universal lower bounds, equality by attainment |
| Order 32 | explicit matrix and rational threshold | Bareiss and rational LDL | first strict counterexample |
| Recovery orders | all windows, parity walks, 64 terminals | independent exact rebuild, none unresolved | equality at 34,36,38,42,44,46 |
| Order 40 | explicit matrix and 40 rational pivots | independent exact LDL | strict counterexample |
| Even 48--238 | 96 explicit matrices and rational bounds | full-matrix rational LDL rebuild | complete strict finite bridge |
| Exact-`2r` | Floquet, Gram, complement, Feshbach data | exact checker plus focused tests | rank `2r` in the fixed window |

The supplement manifest includes the Task 50/51 G6 certificates, Task 56
integer-witness checker, and all finite-classification certificate families.
Every named repository artifact was checked to exist. Pytest suites are
invoked through `python3 -m pytest -q`, not as inert plain scripts.

## Labels, references, and bibliography

```text
Labels: 131
Duplicate labels: 0
Undefined references: 0
Undefined citations: 0
Duplicate BibTeX keys: 0
Duplicate DOI values: 0
Actually cited bibliography records: 10
Unused retained infrastructure records: 12
```

Suvagiya's direct preprint is cited as the source of Conjecture 3 and the
candidate formula. JGT analogy references are used only for methodological
context. Formal journal records are preferred when available.

## Figure and visual inventory

1. cycle-square edges and switching/flux coordinates;
2. reference gap, G6 charge, and residue closures; and
3. finite-ring localization and infinite G6 patch identification.

All figures are explicitly cited, monochrome, grayscale-safe, and readable at
100 percent. All 38 main-paper pages and all 13 supplement pages were rendered
and reviewed. Typography, theorem hierarchy, margins, tables, captions, and
appendix transitions pass. No decorative boxes, slide/report styling, manual
font reduction, margin reduction, overlap, clipping, or serious whitespace
defect remains.

## Literature and novelty

The direct-literature and novelty audits are dated 2026-08-24. The direct
predecessor is prominently credited. The final cautious novelty wording is
restricted to all `{+1,-1}` edge signings of the fixed family `C_n(1,2)`.
The unpublished fixed-graph signing seminar remains a pre-submission
watchlist item and is not represented as a theorem.

## Open questions

The Conclusion contains exactly three questions:

1. whether the nonzero residue subsequences converge to `c_6`, beyond the
   proved limsup upper bounds;
2. whether G6 is optimal among broader sector-changing finite cores, beyond
   the proved single-gap class; and
3. whether large-order minimizers have an eventual separated-phase-slip
   structure.

## Hard scans

```text
TASK58_DRAFT_STUB=0
TODO=0
TBD=0
FIXME=0
PLACEHOLDER token=0
author footnotes=0
unresolved references=0
active stale exact-r/rank-one claims=0
main-paper internal research paths=0 outside the identified availability text
```

## Archival and metadata status

```text
Development repository: https://github.com/whzy3185/math
Audited preparation checkpoint: e365e1553ad73a8a534fb67f5ee76562521609ce
Immutable archive: IMMUTABLE_ARCHIVE_PENDING
Author metadata: PENDING_USER_METADATA
```

No DOI or archive identifier has been invented. Before an identified
submission is uploaded, the author name, affiliation, corresponding email,
ORCID, and real immutable release/archive identifier must replace the pending
metadata. The anonymous review PDF is already identity-safe and complete.

## Final verdict

The mathematical proof package, anonymous manuscript, appendices,
bibliography, and supplement pass the final submission audit. Identified
submission is conditional only on user-supplied author metadata and creation
of the promised immutable archive.

