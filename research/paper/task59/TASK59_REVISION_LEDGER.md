# Task 59 Revision Ledger

## Baseline and invariants

- Baseline commit: `a274240fce3c73c0a34e36e6c9c61986e9f4844f`.
- Frozen source packages: `manuscript_tex_task58/` and
  `manuscript_tex_task58_supplement/`.
- Revision packages: `manuscript_tex_task59/` and
  `manuscript_tex_task59_supplement/`.
- No theorem conclusion, threshold, certificate, or proof dependency may be
  changed in Task 59.
- The English and Chinese publication archives remain untouched.

## Decisions

| ID | Referee suggestion | Decision | Implementation target | Acceptance test |
|---|---|---|---|---|
| 59-L01 | Narrow the title to the proved scope | ACCEPT | `frontmatter.tex`, PDF metadata | Title names twisted-signing optimality, not unrestricted minimization |
| 59-L02 | Qualify every "complete classification" claim | ACCEPT | front matter, introduction, conclusion | Every such claim identifies the conjectured equality/truth set |
| 59-L03 | Remove the degree-ten polynomial and 15-digit interval from the introduction | ACCEPT | `sections/01_introduction.tex` | Introduction states only `eta<c_6<8` and points forward |
| 59-L04 | Add an immediately readable truth pattern | MODIFY | introduction | Compact table, not an infographic |
| 59-L05 | Expand related work by method | ACCEPT | introduction, `references.bib` | Every added citation supports a nearby claim |
| 59-L06 | Centralize the exact-computation convention | ACCEPT | introduction, Section 7 | One convention plus local statements only where logically needed |
| 59-L07 | Demote exact-(2r) from the main theorem line | ACCEPT | Section 6, supplement | Main text contains a remark and supplement carries theorem/proof |
| 59-L08 | Redraw Figure 2 | ACCEPT | `figures/figure_reference_slips.tex` | `g=4 -> g=6`, charge, and three residue constructions are legible |
| 59-L09 | Add a proof-architecture flowchart | REJECT | none | Mathematical figures remain object-centered |
| 59-L10 | Add visual material for its own sake | REJECT | none | Figure count grows only for mathematical need |
| 59-L11 | Separate human proof from machine certificate data | ACCEPT | Appendix A, supplement | Main/appendix explain implications; manifest owns raw artifacts |
| 59-L12 | Make reproducibility submission-ready | ACCEPT WITH EXTERNAL BLOCKER | availability, supplement, handoff | Clean-checkout commands, runtime/memory, producer/verifier roles, immutable-archive status |
| 59-L13 | Compress defensive language and normalize terminology | ACCEPT | all Task 59 sources | Term audit and manual prose review pass |
| 59-L14 | Compress typography to save pages | REJECT | none | 11 pt and 1-inch margins retained |
| 59-L15 | Fill author and archive metadata speculatively | REJECT | front matter, availability | Placeholders remain explicit until supplied externally |

## Completion gate

Task 59 is complete when all three PDFs compile, the Task 58 mathematical
verification chain still passes, the Task 59 textual and anonymity audits
pass, representative pages pass rendered visual inspection, and the branch
is pushed with no pull request. Until author metadata and an immutable
archive identifier are supplied, the strongest honest status is
`SUBMISSION_READY_MODULO_AUTHOR_METADATA_AND_ARCHIVE`.
