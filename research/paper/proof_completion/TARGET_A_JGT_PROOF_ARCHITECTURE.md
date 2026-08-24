# Target A JGT Proof Architecture

Status: `EDITORIAL_CANONICAL_CURRENT`.

This architecture turns the accepted result corpus into a signed-graph paper
whose primary theorem is the complete truth classification. It does not edit
either frozen manuscript and does not introduce a new unrestricted theorem.

The architecture has exactly seven main theorem families, numbered 1.1--1.7
in `TARGET_A_JGT_THEOREM_HIERARCHY.md`. In particular, separated phase slips
(Theorem 1.6) and residue-class upper constructions (Theorem 1.7) remain
distinct families even when presented in one manuscript section.

## Governing Proof Form

Every computer-assisted argument must appear in four explicit stages:

1. `MATHEMATICAL REDUCTION`: define the finite object and prove that it covers
   every mathematical case in scope.
2. `FINITE EXACT OBJECT`: specify the orbit list, state graph, polynomial,
   interval family, rational matrix, or witness table being checked.
3. `MACHINE VERIFICATION`: identify exact arithmetic, independent checker,
   certificate, and fail-closed tests.
4. `MATHEMATICAL CONSEQUENCE`: return to the variational principle, spectral
   theorem, interlacing, min-max, or set partition that proves the theorem.

The prose must never use "the script observed" as a logical step. Floating
point may propose roots or witness vectors, but no accepted endpoint decision
may depend on it.

## Recommended Main-Text Order

### 1. Introduction And Complete Classification

Lead with the complete even-order theorem `T8.4`, including both equivalent
sets of orders. State immediately that it classifies the truth value of the
conjectured inequality, not all minimizers and not exact values of `m_n`.

`MAIN_TEXT_REQUIRED`:

- the signed-graph problem and `m_n`, `rho_-(n)`;
- the squared threshold `theta_n:=rho_-(n)^2` and the rule that `m_n` is never
  compared directly with `theta_n`;
- the statement of `T8.4`;
- the explicit candidate-attainment lemma `T8.0` needed by the equality
  formulation;
- the partition `8..30`, `32`, `34..46`, `40`, `48..239`, `>=240`;
- a one-paragraph guide to which pieces are computer-assisted.

Define strict failure by `m_n<rho_-(n)`. If the introduction phrases the
original conjecture as the equality `m_n=rho_-(n)`, the final proof must cite
both the universal lower-bound/exhaustion input and a candidate-attainment
input. Absence of strict failure alone is not an attainment proof.

### 2. Switching, Flux, And The Reference Phase

Develop `T1.1`, `T1.2`, and `T1.4`, then state the period-eight reference
word and `T2.2`. Keep the determinant expansion out of the main narrative.

`MAIN_TEXT_REQUIRED`:

- Hamilton gauge, `tau`, `Q`, and `alpha`;
- the local formula for `A_tau^2`;
- the exact value `eta` and `eta<8`;
- the interpretation of gap four as the unperturbed bulk.

`APPENDIX_REQUIRED`:

- the canonical Bloch fiber and quartic polynomial;
- the exact edge factorization and equality analysis;
- operator equivalences and zone folding.

### 3. Gap Coordinates And Translation Sectors

This should be the shortest structural section. Prove `T3.1`-`T3.3`
combinatorially, without transfer matrices.

`MAIN_TEXT_REQUIRED`:

- `sum g_j=n` and `q_j=g_j-4`;
- four bulk sectors `B_s`;
- `sigma_sec(q)=q mod 4` and additivity;
- the sector-closure interpretation of one, two, and three G6 slips.

No reproducibility appendix is needed for this section.

### 4. The Elementary G6 Phase Slip

Define `c6` mathematically before giving its decimal approximation. State
`T4.2` and `T4.3` in coordinate-free language.

`MAIN_TEXT_REQUIRED`:

- the polynomial and certified isolating interval defining `c6`;
- the theorem `sup sigma(H_6)=c6`;
- a four-lemma proof skeleton: hyperbolicity, physical matching, candidate
  completeness/exclusion, realization;
- the essential-spectrum and tail-matching bridge `T4.0` before the Evans
  criterion;
- the exact symmetry and rank-two consequence.

`APPENDIX_REQUIRED`:

- transfer normalization and stable/unstable planes;
- complete Grassmann chart cover;
- resultant/Sturm isolations;
- unsquared physical determinant exclusions in independent charts;
- the distinction between candidate completeness and physical realization.

`REPRODUCIBILITY_ONLY`:

- certificate schema, hashes, checker commands, and tamper tests.

### 5. Single-Gap Optimality

Present `T5.1` and `T5.2` as one main theorem plus one corollary. This is the
cleanest variational section in the paper.

`MAIN_TEXT_REQUIRED`:

- lift and reflection conjugacies;
- the six exact small-gap Rayleigh quotients;
- the fixed vector giving `182/23` for all `g>=9`;
- equality only at G6;
- the exact uniform separation `1/250`.

`APPENDIX_REQUIRED`:

- full integer vectors and output windows;
- positive cross-multiplication margins.

Do not infer all-interface optimality from this section.

### 6. Separated Phase Slips And Residues

Prove the global upper theory before stating the exact cluster refinement.
The classification theorem needs the IMS cap, not exact-`2r`; this ordering
keeps the main proof short.

`MAIN_TEXT_REQUIRED`:

- exact discrete IMS identity;
- pure-bulk/one-G6 patch classification;
- fixed-`r` global cap;
- legal residue words and the three `limsup` conclusions;
- analytic counterexample tail for `n>=240`.

`APPENDIX_REQUIRED`:

- exact `2r` cluster and codimension-`2r` complement;
- the finite-ring patch-identification bridge `T6.0` before importing the
  one-interface complement gap;
- `2r x 2r` Feshbach reduction;
- `3505r(9/25)^ell` and `N_exp=3120`;
- the protected double level on the standard one-G6 ring.

The appendix must state that exact-`2r` is a structural strengthening, not a
premise of the sharper contiguous onset `N_star=48`.

This section contains two main theorem families: Theorem 1.6 is the separated
phase-slip spectral theorem, while Theorem 1.7 is the residue-class upper
construction theorem. Shared placement does not merge their statements or
dependencies.

### 7. Finite Completion And The Main Theorem

Return to `T8.4` only after all infinite constructions are available.

`MAIN_TEXT_REQUIRED`:

- one theorem for the six no-counterexample orders;
- short exact witness propositions for `n=32` and `n=40`;
- the 96-order full-matrix bridge stated as a finite lemma;
- the disjoint exhaustive partition proving `T8.4`.

`APPENDIX_REQUIRED`:

- why the local-window criterion is valid;
- soundness and completeness of the parity-lifted de Bruijn graph;
- cyclic and holonomy closure;
- the meaning of the 64 terminal records and the corrected historical sum;
- exact terminal decisions and `terminal_unresolved=0`;
- the exact LDL certificate boundary.

`REPRODUCIBILITY_ONLY`:

- one checker command for each finite family;
- certificate paths and expected PASS strings;
- resource notes for the large small-order certificate.

## Supporting Appendices

### Appendix A. Period-Eight Floquet Algebra

Contains `T1.3`, `T2.1`, and the detailed proof of `T2.2`.

### Appendix B. G6 Matching Certificate

Contains `T4.1`, `C.6`, chart coverage, exact root isolation, and physical
branch selection.

### Appendix C. Single-Gap Witnesses

Contains `C.8`, all integer vectors, and the `1/250` margin table.

### Appendix D. Separated-Interface Estimates

Contains `T6.3`-`T6.6`, `C.7`, Gram bounds, complement gap, Feshbach formula,
and explicit constants.

### Appendix E. Finite Classification Certificates

Contains `C.1`-`C.5`, with special emphasis on the proof of completeness for
`C.3`.

### Appendix F. Supporting Periodic And Moment Results

Contains `A.1`-`A.3`. The period frontier is explicitly bounded by `p<=24`.
The period-25/26 read-only calculation is omitted from theorem statements.

### Appendix G. Additional Interface Obstructions

Contains `A.4`-`A.6` only if length permits. These results are not needed for
the main classification and must not interrupt the phase-slip narrative.

### Reproducibility Supplement

Contains only artifact schemas, paths, hashes, checker commands, expected
outputs, independence statements, and tamper-test descriptions. It should not
contain unstated mathematical reductions.

## Dependency Compression Rules

1. Main-text theorems cite human-readable theorem names, never research-task
   identifiers.
2. The proof of `T8.4` cites only `T8.1`-`T8.3` and `T7.3`.
3. The proof of `T7.3` cites local spectral caps and the 96-order finite
   bridge; it does not cite exact-`2r`.
4. The proof of `T5.2` cites the exact witness table and the upper isolating
   endpoint for `c6`; it uses no decimal comparison.
5. The proof of `T4.2` separates resultant candidate completeness from
   unsquared physical matching.
6. The exact-`2r` appendix starts from a rank-two one-interface basis and
   never inherits rank-one notation.
7. A truth classification for the equality conjecture cites candidate
   attainment in addition to the lower-bound/exhaustion argument.
8. Every source import obeys
   `TARGET_A_MANUSCRIPT_IMPORT_SAFETY.md`; an exact-path blacklist overrides a
   directory-level default.

## Editorial Exclusions

Do not promote or center:

- universal multi-gap optimality;
- unrestricted common liminf or common limit;
- arbitrary-period uniqueness;
- period-25/26 read-only counts;
- the producer-only reference graph;
- finite-ring level simplicity outside the proved one-G6 symmetry class;
- interaction coefficients or three-body effects.

They may appear only as carefully delimited future work, or be omitted.

## Readiness Gate For Manuscript Reframe

The later manuscript reframe may begin when each main theorem package has:

- a natural theorem statement;
- a complete human proof skeleton;
- every finite domain proved exhaustive;
- every endpoint certified exactly;
- an independent checker for every logically essential computation;
- no current rank-`r` language;
- a direct mapping to `MAIN_TEXT`, `APPENDIX`, and `REPRODUCIBILITY`.
- an import category under `TARGET_A_MANUSCRIPT_IMPORT_SAFETY.md`.

The canonical registry satisfies the editorial mapping. Completion of the
remaining theorem-specific packages is tracked outside this Lane A directory.
