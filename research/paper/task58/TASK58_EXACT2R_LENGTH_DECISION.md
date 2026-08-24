# Task 58 Exact-2r Length and Placement Decision

Status: `TASK58_9_EXACT2R_MAIN_SUPPLEMENT_SPLIT_LOCKED`.

This document fixes the first-submission placement of the separated-interface
exact-`2r` theorem. It is an editorial decision only. The canonical statement,
hypotheses, constants, proof dependencies, and evidence boundary remain those
in `research/paper/proof_completion/07_exact_2r/`.

## 1. Mathematical Facts That Must Not Change

Each bilateral G6 interface has a two-dimensional squared eigenspace at
`c6`: its two modes come from the simple unsquared partners at
`+sqrt(c6)` and `-sqrt(c6)`. Consequently, `r` separated G6 interfaces
produce a `2r`-dimensional local mode space. The accepted finite-ring result
is therefore an exact-`2r` theorem, not an exact-`r` theorem.

For a legal finite ring consisting of exactly `r in {1,2,3}` G6 interfaces
and period-eight bulk elsewhere, with either interface orientations and
either Hamilton holonomy, let `D` be the minimum cyclic core separation. If
`D>=1040`, then

```text
rank 1_[c6-1/400,c6+1/400](H)=2r.
```

The rank counts eigenvalues with multiplicity. It does not assert individual
simplicity, a nonzero leading interaction, an interaction sign, or an exact
finite-ring eigenvalue formula.

Every reference to the local squared edge must say rank two, and every
cluster, complement-codimension, Gram, and effective-operator dimension must
say `2r`. The superseded exact-`r`, codimension-`r`, and `r x r` formulations
are prohibited.

## 2. Main-Text Placement

Section 6 contains exactly the following exact-`2r` payload:

1. one theorem statement giving the complete scope `r in {1,2,3}`, both
   orientations, both Hamilton holonomies, `D>=1040`, the fixed window
   `[c6-1/400,c6+1/400]`, exact rank `2r`, multiplicity counting, and the
   nonclaim of individual simplicity; and
2. one proof-overview paragraph explaining only the logical chain: two local
   modes per interface, truncation to `2r` quasimodes, independence and the
   lower count, the rank-two local complement estimate plus patch
   identification and IMS for the upper count, and equality of the two
   counts.

The same proof-overview paragraph must end by saying that this theorem is a
structural refinement and is not used for the analytic `n>=240` tail, the
finite bridge, or the sharp continuous onset `48`. This dependency disclaimer
must not become a second proof paragraph, a remark, or a corollary.

No exact-`2r` formula, proof lemma, constant table, figure, appendix section,
or reproducibility discussion is added to the essential paper. The abstract
and Introduction contain no exact-`2r` refinement.

## 3. Supplement Placement

The separate supplement contains the complete mathematical proof and its
reproducibility layer, including:

- the cutoff geometry and the definitions of `S`, `L_site`, and `ell`;
- exact Floquet contraction and conditioning bounds;
- both truncated modes at every interface and the full `2r x 2r` Gram
  matrix, including same-interface cross terms;
- Gram invertibility and orthonormalization;
- residual estimates and the spectral-projection lower count;
- the codimension-`2r` complement estimate, patch identification details,
  the exact range-four IMS error, and the min--max upper count;
- the Gram-orthogonalized `2r x 2r` Feshbach operator and Schur-complement
  equation;
- all proof constants, including `q_F=9/25`, `73`, `1752`, `3504`, `3505`,
  the complement and resolvent margins, and
  `|lambda_j-c6|<3505r(9/25)^ell`;
- the sufficient exponential threshold `N_exp=3120`, explicitly labelled
  nonoptimal;
- the protected one-G6 double-top corollary in its stated symmetry class;
  and
- certificate schemas, hashes, checker commands, independent reconstruction,
  expected outputs, tamper tests, and resource notes.

The hypotheses `D>=1040` and the fixed `1/400` window remain in the main
theorem because they define its scope. Their derivation and all auxiliary
constant arithmetic belong to the supplement.

## 4. Dependency Boundary

The exact-`2r` theorem has no outgoing dependency to the complete even-order
classification. In particular, it is not used to prove:

- the G6/IMS spectral cap;
- failure for every even `n>=240`;
- any of the 96 exact bridge cases `48<=n<240`; or
- the conclusion that continuous failure begins at `48`.

The onset `48` comes from the analytic tail together with the disjoint exact
finite bridge. The exact-`2r` theorem instead describes the multiplicity of
the localized near-`c6` cluster when G6 interfaces are sufficiently far
apart. Neither `D>=1040` nor `N_exp=3120` is the sharp onset.

## 5. Page Forecast and Length Control

The phase-start handoff records a 16-page build with Section 6 beginning on
page 15. The locked forecast is:

```text
Introduction                         about 4 pages
Section 6                            4--5 pages
Main narrative                       28--34 pages
Current working forecast             28--32 main pages
Appendix A                           4--5 pages
Appendix B                           4--5 pages
Paper with essential appendices      at most 45 pages
Reproducibility supplement           counted separately
```

The post-Section-6 build has 20 pages, with Section 7 beginning on page 19.
The updated working forecast is:

```text
Current compiled paper                20 pages
Projected Section 7                   5--6 pages
Projected Section 8 and availability  1--2 pages
Projected main narrative              25--28 pages
Projected Appendix A                  4--5 pages
Projected Appendix B                  4--5 pages
Projected essential paper             34--38 pages
Projected separate supplement         15--25 pages
```

The essential-paper forecast remains below the preferred 45-page ceiling,
so no proof-bearing main-text material is trimmed at this checkpoint.

This forecast assumes that the essential paper contains no exact-`2r`
appendix, no exact-`2r` geometry, and no exact-`2r` constant table. The Section
6 allocation permits only the theorem statement and one compact proof-overview
paragraph described above. Normal article typography, margins, and display
spacing remain unchanged; page control is editorial, not typographic.

If the essential paper approaches or exceeds 45 pages, trim in this order:

1. reduce the exact-`2r` overview to the theorem statement and the shortest
   logically complete single paragraph, preserving the rank-two to exact-`2r`
   mechanism and the nondependency on onset `48`;
2. move complete single-gap witness vectors and margin tables to the
   supplement;
3. remove all remaining schemas, hashes, commands, expected outputs, and
   resource notes from the essential paper;
4. compress the exposition of the G6 algebraic certificate without removing
   physical realization, candidate completeness, maximality, or rank two;
5. shorten historical and organizational prose before shortening a proof
   needed for the main classification.

Never meet the page target by weakening the classification theorem, deleting
the candidate-attainment direction, omitting finite-state completeness,
conflating the analytic tail with the finite bridge, or shrinking typography.

## 6. Editorial Acceptance Check

The Task 58.9 exact-`2r` placement is acceptable only if all of the following
hold:

- the main text has one exact-`2r` theorem statement and one proof-overview
  paragraph only;
- the theorem says local rank two and cluster rank `2r`;
- `r in {1,2,3}`, `D>=1040`, both orientations, both holonomies, the fixed
  window, and multiplicity counting are explicit;
- no individual simplicity is claimed;
- no Gram, complement, Feshbach, exponential constant, or `N_exp` proof
  appears in the essential paper;
- `N_exp=3120` is supplement-only, sufficient, and nonoptimal;
- the text states that exact-`2r` is not used to establish onset `48`; and
- the essential paper remains forecast at no more than 45 pages without
  typographic compression.

Canonical sources:

```text
research/paper/task58/TASK58_MANUSCRIPT_MASTER_BLUEPRINT.md
research/paper/task58/TASK58_THEOREM_TO_SECTION_MAP.md
research/paper/manuscript_tex_task58/sections/06_finite_rings.tex
research/paper/proof_completion/07_exact_2r/THEOREM_STATEMENT.md
research/paper/proof_completion/07_exact_2r/PROOF_OVERVIEW.md
research/paper/proof_completion/07_exact_2r/FULL_PROOF.md
research/paper/proof_completion/07_exact_2r/COMPUTER_ASSISTED_BOUNDARY.md
```
