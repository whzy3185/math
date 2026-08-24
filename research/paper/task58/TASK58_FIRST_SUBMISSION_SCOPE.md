# Task 58 First-Submission Scope

Status: `TASK58_0_SCOPE_FROZEN`.

Approved base: `20eb153560df30980ff5ee842246579af40faae5`.

This document is an editorial import contract for the first submission. It
does not change, strengthen, merge, or renumber any canonical theorem. The
normative statement of every claim remains
`research/paper/proof_completion/TARGET_A_FINAL_CLAIM_INVENTORY_V2.md`; its
evidence and dependencies remain those in
`research/paper/proof_completion/TARGET_A_FINAL_CLAIM_EVIDENCE_MATRIX_V2.md`
and `research/paper/proof_completion/TARGET_A_FINAL_PROOF_DEPENDENCY_GRAPH.md`.
All source paths below are exact repository-relative paths.

## Category Semantics

The four categories are mutually exclusive at claim level.

- `MAIN_MANUSCRIPT_IMPORT`: eligible for the first-submission paper, either
  in the main narrative or in an essential mathematical appendix. This label
  does not authorize certificate schemas, hashes, commands, or research-stage
  prose.
- `STATEMENT_OVERVIEW_ONLY`: only the current theorem statement and a short
  structural interpretation may enter the paper. Its proof and constants are
  not part of the main manuscript package.
- `SUPPLEMENT_ONLY`: may appear only in a separately identified supplement or
  optional appendix that can be removed without affecting the complete
  classification proof.
- `DO_NOT_IMPORT_FIRST_SUBMISSION`: no theorem statement, proof prose, table,
  figure, numerical result, or research narrative from the item may enter the
  first submission.

Evidence labels and import categories are different notions. In particular,
a proved claim may still be omitted for editorial focus. Historical source
material remains governed by
`research/paper/proof_completion/TARGET_A_MANUSCRIPT_IMPORT_SAFETY.md`; an
exact-path blacklist there overrides this scope document.

## Introduction Contract

The proof registry retains exactly seven canonical theorem families:

| Internal family | Canonical claims | First-submission use |
|---|---|---|
| 1. Complete even-order classification | `T8.0`, `T8.4` | Introduction theorem box 1 and final theorem of the paper. |
| 2. Reference-phase edge | `T2.1`-`T2.3` | Structural input; contributes to introduction theorem box 2 but remains a distinct internal family. |
| 3. Gap, charge, and sector shift | `T3.1`-`T3.3` | Short structural theorem in the body; no separate introduction box. |
| 4. Elementary G6 phase slip | `T4.0`-`T4.3` | Technical centerpiece; contributes to introduction theorem box 2. |
| 5. Single-gap optimality | `T5.1`-`T5.2` | Completes introduction theorem box 2. |
| 6. Separated phase slips | `T6.0`-`T6.4` | IMS mechanism in the body; exact-`2r` only as a structural refinement statement. |
| 7. Residue-class upper constructions | `T7.1`-`T7.3` | Explains eventual failure and supplies the certified tail. |

The Introduction has only two theorem boxes:

1. **Complete classification and candidate attainment:** `T8.0` and `T8.4`.
2. **Reference and single-gap spectral hierarchy:** the theorem-level content
   of `T2.2`, `T4.0`-`T4.3`, and `T5.1`-`T5.2`, summarized by the exact
   hierarchy `sup sigma(H_4)=eta<c_6=sup sigma(H_6)`, the uniform separation
   for `g notin {4,6}`, and `dim ker(H_6-c_6)=2`.

The second box does not merge internal theorem families 2, 4, and 5. The
remaining canonical families appear in the roadmap and body, not as
co-equal Introduction contributions.

## MAIN_MANUSCRIPT_IMPORT

This category contains the complete-classification proof and exactly the
structural material needed to explain it.

| Claim ID | Theorem/result | Exact canonical source path | Manuscript role | Import restriction |
|---|---|---|---|---|
| `T1.1` | Hamilton gauge and switching invariance | `research/paper/proof_completion/TARGET_A_FINAL_CLAIM_EVIDENCE_MATRIX_V2.md` | Definitions and switching reduction in the setup section. | Import only the current diagonal-conjugacy proof; no historical gauge narrative. |
| `T1.2` | `(tau,Q,alpha)` parametrization | `research/paper/proof_completion/04_charge_sector/FULL_PROOF.md` | Flux, lift, and holonomy coordinates used by all finite and residue arguments. | State the cyclic scope and retain both holonomies; do not identify `tau` with an arbitrary signing before gauge fixing. |
| `T1.3` | Translation, reflection, lift negation, and zone folding | `research/paper/proof_completion/03_reference_phase/FULL_PROOF.md` | Supporting operator-equivalence proposition in an essential appendix. | Use only proved unitary equivalences; do not expand into a periodic-classification narrative. |
| `T1.4` | Exact range-four formula for `H=A^2` | `research/paper/proof_completion/TARGET_A_FINAL_CLAIM_EVIDENCE_MATRIX_V2.md` | Local operator identity underlying IMS, local windows, and witnesses. | Keep `A` unsquared and `H=A^2`; no obsolete symbol reuse. |
| `T2.1` | Exact period-eight Bloch polynomial | `research/paper/proof_completion/03_reference_phase/FULL_PROOF.md` | Essential appendix proof of the reference edge. | The determinant expansion stays out of the main narrative; no bounded-period frontier inference. |
| `T2.2` | Exact reference edge `eta` and unique Bloch maximizer | `research/paper/proof_completion/03_reference_phase/FULL_PROOF.md` | Reference-background theorem and part of Introduction box 2. | Define `eta` exactly before any decimal and state uniqueness only at `z=1`. |
| `T2.3` | Gap four is the reference bulk | `research/paper/proof_completion/03_reference_phase/FULL_PROOF.md` | Identifies the unperturbed crystalline background. | Gap four is not an abnormal interface. |
| `T3.1` | Cyclic gap sum and excess-charge sum | `research/paper/proof_completion/04_charge_sector/FULL_PROOF.md` | Combinatorial coordinate theorem. | Keep the exact cyclic hypotheses and distinguish the defect-free case. |
| `T3.2` | Sector law `sigma_sec(q)=q mod 4` | `research/paper/proof_completion/04_charge_sector/FULL_PROOF.md` | Explains translation-sector change across one oriented interface. | Do not replace the mod 4 sector law by the mod 8 ring-closure law. |
| `T3.3` | Additivity and cyclic sector closure | `research/paper/proof_completion/04_charge_sector/FULL_PROOF.md` | Connects one/two/three G6 constructions to legal cyclic closure. | Use together with `sum q_j = n (mod 8)` when explaining residue classes. |
| `T4.0` | G6 essential spectrum and exponential tail bridge | `research/paper/proof_completion/05_g6_edge/ESSENTIAL_SPECTRUM_LEMMA.md` | First lemma in the G6 proof chain and part of Introduction box 2. | Essential spectrum alone gives discreteness above `eta`, not existence of `c_6`. |
| `T4.1` | Exact algebraic definition and isolation of `c_6` | `research/paper/proof_completion/05_g6_edge/FULL_PROOF.md` | Defines the structural constant before the G6 edge theorem. | Use the degree-ten polynomial and rational isolating interval; decimals are orientation only. |
| `T4.2` | Global G6 squared spectral edge | `research/paper/proof_completion/05_g6_edge/FULL_PROOF.md` | Technical centerpiece and part of Introduction box 2. | Separate candidate completeness from physical matching and realization. |
| `T4.3` | Rank-two G6 symmetry and simple unsquared partners | `research/paper/proof_completion/05_g6_edge/FULL_PROOF.md` | Structural multiplicity proposition and part of Introduction box 2. | State `dim ker(H_6-c_6)=2`; never call `c_6` simple for `H_6`. |
| `T5.1` | G6 uniquely minimizes abnormal positive single gaps | `research/paper/proof_completion/06_single_gap/FULL_PROOF.md` | Main variational theorem and part of Introduction box 2. | Quantifier is single-gap only, with both lifts and orientations; no arbitrary multi-gap inference. |
| `T5.2` | Uniform single-gap separation by `1/250` | `research/paper/proof_completion/06_single_gap/FULL_PROOF.md` | Corollary completing the structural hierarchy. | Preserve the strict inequality and exact cross-multiplication; no decimal endpoint argument. |
| `T6.0` | Finite-ring G6 patch identification | `research/paper/proof_completion/07_exact_2r/PATCH_IDENTIFICATION_LEMMA.md` | Analytic bridge from finite rings to the certified line model. | Import only the patch-identification part; exact-`2r` Gram/Feshbach details remain outside the main manuscript. |
| `T6.1` | Exact discrete IMS identity and range-four error | `research/paper/proof_completion/08_residue_ims/FULL_PROOF.md` | Main analytic localization lemma. | Retain the exact identity and support hypotheses; do not describe it as numerical evidence. |
| `T6.2` | Fixed-interface patch classification and global cap | `research/paper/proof_completion/08_residue_ims/FULL_PROOF.md` | Explains why G6 constructions force eventual failure. | Scope is `r in {1,2,3}` separated G6 rings; it does not use exact-`2r` and does not prove onset 48. |
| `T7.1` | Legal one-, two-, and three-G6 residue words | `research/paper/proof_completion/08_residue_ims/FULL_PROOF.md` | Explicit constructions for residues 2, 4, and 6 modulo 8. | Print the legal range of exponents and keep mod 8 charge closure distinct from mod 4 sector shift. |
| `T7.2` | Nonzero-residue `limsup` upper bounds | `research/paper/proof_completion/08_residue_ims/FULL_PROOF.md` | Asymptotic upper-construction corollary. | Say `limsup` only; no lower bound, common liminf, limit, or minimizer classification. |
| `T7.3` | Counterexample at every even `n>=48` | `research/paper/proof_completion/01_even_order_classification/FULL_PROOF.md` | Combines the 96-order exact bridge with the analytic `n>=240` tail. | State that phase-slip theory explains eventual permanence while exact finite verification places continuous onset at 48. |
| `T8.0` | Antibalanced candidate attains `rho_-(n)` | `research/paper/proof_completion/01_even_order_classification/CANDIDATE_ATTAINMENT_LEMMA.md` | One half of Introduction box 1 and the equality direction at valid orders. | Explicitly use `Q_i=-1`, `alpha=-1`; nonfailure alone does not imply equality. |
| `T8.1` | Exact truth for even orders 8 through 32 | `research/paper/proof_completion/01_even_order_classification/FULL_PROOF.md` | Finite completion: valid orders 8--30 and first failure at 32. | Present mathematical reduction and exact endpoint logic; detailed artifacts stay in the supplement. |
| `T8.2` | Six no-counterexample orders in 34--46 | `research/paper/proof_completion/02_small_order_34_46/FULL_PROOF.md` | Determines the irregular small-order truth pattern. | State 64 terminal records and zero unresolved; do not claim a conceptual G6 explanation for these isolated valid orders. |
| `T8.3` | Exact order-40 counterexample | `research/paper/proof_completion/02_small_order_34_46/FULL_PROOF.md` | Second isolated failure in the finite completion. | Import the exact witness and LDL consequence, not discovery chronology. |
| `T8.4` | Complete even-order equality/failure classification | `research/paper/proof_completion/01_even_order_classification/THEOREM_STATEMENT.md` | Introduction theorem box 1 and final synthesis theorem. | Failure set is exactly 32, 40, and even `n>=48`; do not claim all minimizers or exact `m_n` at failing orders. |
| `C.1` | Exhaustive exact decisions for even 8--30 | `research/paper/proof_completion/01_even_order_classification/COMPUTER_ASSISTED_BOUNDARY.md` | Essential computer-assisted lemma supporting `T8.1`. | Paper must prove finiteness and coverage before reporting exact verification. |
| `C.2` | Exact order-32 witness | `research/paper/proof_completion/01_even_order_classification/COMPUTER_ASSISTED_BOUNDARY.md` | Essential exact-matrix lemma supporting `T8.1`. | One existence witness suffices; schema, hash, and command are supplement-only. |
| `C.3` | Parity-lifted finite-state closure at six orders | `research/paper/proof_completion/02_small_order_34_46/COMPUTER_ASSISTED_BOUNDARY.md` | Essential appendix proof of completeness for `T8.2`. | Include soundness, completeness, cyclic closure, both holonomies, 64 terminals, and `terminal_unresolved=0`. |
| `C.4` | Exact order-40 witness | `research/paper/proof_completion/02_small_order_34_46/COMPUTER_ASSISTED_BOUNDARY.md` | Essential exact LDL lemma supporting `T8.3`. | Keep it separate from the six no-counterexample terminal records. |
| `C.5` | Ninety-six exact certificates for `48<=n<240` | `research/paper/proof_completion/01_even_order_classification/COMPUTER_ASSISTED_BOUNDARY.md` | Exact finite bridge between small orders and the analytic tail. | State all-order coverage of the interval; do not call 240 the classification onset. |
| `C.6` | Complete physical G6 matching audit | `research/paper/proof_completion/05_g6_edge/COMPUTER_ASSISTED_BOUNDARY.md` | Essential G6 algebraic appendix behind `T4.2`-`T4.3`. | Resultants alone are insufficient; retain chart coverage, root isolation, and unsquared physical exclusions. |
| `C.8` | Exact single-gap witness arithmetic | `research/paper/proof_completion/06_single_gap/COMPUTER_ASSISTED_BOUNDARY.md` | Essential exact input to `T5.1`-`T5.2`. | Import the finite partition and exact margins; the complete integer-vector tables are supplement-only. |

## STATEMENT_OVERVIEW_ONLY

| Claim ID | Theorem/result | Exact canonical source path | Manuscript role | Import restriction |
|---|---|---|---|---|
| `T6.3` | Exact `2r` near-`c_6` cluster for separated G6 interfaces | `research/paper/proof_completion/07_exact_2r/THEOREM_STATEMENT.md` | One theorem statement and a short physical/spectral interpretation after the IMS classification mechanism. | State rank `2r`, multiplicity counting, `r in {1,2,3}`, and `D>=1040`; do not put the Gram proof, complement proof, Feshbach formula, or explicit decay constants in the main manuscript. This refinement is not a premise of `N_star=48`. |

## SUPPLEMENT_ONLY

| Claim ID | Theorem/result | Exact canonical source path | Manuscript role | Import restriction |
|---|---|---|---|---|
| `T6.4` | Codimension-`2r` complement, `2r x 2r` Feshbach theorem, and exponential cluster bound | `research/paper/proof_completion/07_exact_2r/FULL_PROOF.md` | Optional exact-`2r` supplement. | Preserve the corrected `2r` dimensions and current constants; never import as a premise of the sharp classification onset. |
| `T6.5` | Sufficient exponential onset `N_exp=3120` | `research/paper/proof_completion/07_exact_2r/FULL_PROOF.md` | Optional corollary in the exact-`2r` supplement. | It is sufficient but nonoptimal and is not the continuous onset 48. |
| `T6.6` | Protected double top on the standard one-G6 ring | `research/paper/proof_completion/07_exact_2r/PROOF_OVERVIEW.md` | Optional structural corollary in the exact-`2r` supplement. | Scope is the stated one-G6 symmetry class only; do not infer general finite-ring simplicity. |
| `C.7` | Exact-`2r` Floquet, complement-gap, and endpoint audit | `research/paper/proof_completion/07_exact_2r/COMPUTER_ASSISTED_BOUNDARY.md` | Reproducibility layer for the optional exact-`2r` supplement. | Full Gram data, complement-gap proof, Feshbach details, `3505r(9/25)^ell`, checker metadata, and resource notes remain outside the main manuscript. |

The following payloads are also `SUPPLEMENT_ONLY` even though their parent
claims remain in `MAIN_MANUSCRIPT_IMPORT`:

| Payload key | Payload | Exact canonical source path | Restriction |
|---|---|---|---|
| `SG_WITNESS_PAYLOAD` | Complete single-gap integer witness vectors and output windows supporting claim `C.8` | `research/paper/proof_completion/06_single_gap/COMPUTER_ASSISTED_BOUNDARY.md` | The paper may state the finite partition and exact comparisons; full vectors move to the supplement. |
| `REPRODUCIBILITY_PAYLOAD` | Certificate schemas, hashes, checker commands, expected PASS strings, tamper tests, and resource notes supporting `C.1`-`C.6` and `C.8` | `research/paper/proof_completion/10_computer_assisted/MINIMAL_REPRODUCTION.md` | Reproducibility metadata is not proof prose and must not interrupt the mathematical argument. |

## DO_NOT_IMPORT_FIRST_SUBMISSION

The following accepted claims are mathematically retained in the canonical
registry but intentionally omitted from the first submission.

| Claim ID | Theorem/result | Exact canonical source path | Manuscript role | Import restriction |
|---|---|---|---|---|
| `A.1` | Full/general moment machinery | `research/paper/proof_completion/09_moments_periodic/FULL_PROOF.md` | None. | Do not import formulas, necessary inequalities, proof prose, tables, or motivation. |
| `A.2` | Period-eight moment trichotomy | `research/paper/proof_completion/09_moments_periodic/FULL_PROOF.md` | None. | Do not use it as an alternate story for the reference phase. |
| `A.3` | Primitive periodic frontier for `p<=24` | `research/paper/proof_completion/09_moments_periodic/FULL_PROOF.md` | None. | Bounded frontier is not needed for the classification and must not appear in text, appendix, abstract, or figures. |
| `A.4` | 31,008 bounded-support multi-gap exclusions | `research/paper/proof_completion/TARGET_A_FINAL_CLAIM_EVIDENCE_MATRIX_V2.md` | None. | Do not import the multi-gap package or its computational counts. |
| `A.5` | Arbitrary-length `(3,3)` local obstruction | `research/paper/proof_completion/TARGET_A_FINAL_CLAIM_EVIDENCE_MATRIX_V2.md` | None. | Do not use this local result to suggest universal interface optimality. |
| `A.6` | Remaining multi-gap finite-alphabet reduction | `research/paper/proof_completion/TARGET_A_FINAL_CLAIM_EVIDENCE_MATRIX_V2.md` | None. | Do not import the reduction, forbidden-pair language, or open-ended search program. |
| `C.9` | Finite exact certificate for the `p<=24` frontier | `research/paper/proof_completion/09_moments_periodic/COMPUTER_ASSISTED_BOUNDARY.md` | None. | Do not import orbit counts, certificate records, checker discussion, or bounded-frontier conclusions. |

The following non-promoted or editorial materials are also barred. They are
listed because their omission is part of the first-submission story, even
though they are not among the 46 accepted `T`, `A`, and `C` claim IDs.

| Claim/result key | Theorem/result | Exact canonical source path | Manuscript role | Import restriction |
|---|---|---|---|---|
| `R.1` | Period 25 and period 26 read-only frontier computation | `research/paper/proof_completion/TARGET_A_FINAL_CLAIM_INVENTORY_V2.md` | None. | Exact finite read-only evidence is not a theorem and cannot extend `A.3`. |
| `R.2` | Producer-only reference graph | `research/paper/proof_completion/TARGET_A_FINAL_CLAIM_INVENTORY_V2.md` | None. | Do not import the reference graph, state/edge counts, costs, or any inferred spectral coercivity. |
| `O.1` | Universal finite-core or arbitrary multi-gap optimality | `research/paper/proof_completion/TARGET_A_FINAL_CLAIM_INVENTORY_V2.md` | None. | Open; `T5.1` is single-gap only. |
| `O.2` | Common liminf and common limit programs | `research/paper/proof_completion/TARGET_A_FINAL_CLAIM_INVENTORY_V2.md` | None. | Open; do not strengthen `T7.2` beyond `limsup`. |
| `O.3` | Interaction coefficients, pairwise splitting fits, simplicity, and three-body asymptotics | `research/paper/proof_completion/TARGET_A_FINAL_CLAIM_INVENTORY_V2.md` | None. | Open; no fit, plot, coefficient, or asymptotic claim enters the first submission. |
| `O.4` | All-period uniqueness of the period-eight phase | `research/paper/proof_completion/TARGET_A_FINAL_CLAIM_INVENTORY_V2.md` | None. | Open; neither `A.3` nor period 25/26 evidence implies it. |
| `X.1` | Rank-one G6 / exact-`r` squared cluster | `research/paper/proof_completion/TARGET_A_MANUSCRIPT_IMPORT_SAFETY.md` | None. | Falsified as stated; no active or historical discussion enters the first submission. |
| `X.2` | Codimension-`r` complement and `r x r` G6 Feshbach model | `research/paper/proof_completion/TARGET_A_MANUSCRIPT_IMPORT_SAFETY.md` | None. | Falsified as stated; only corrected `2r` mathematics is eligible under the categories above. |
| `X.3` | Single-gap theorem promoted to every finite-core interface | `research/paper/proof_completion/TARGET_A_FINAL_CLAIM_INVENTORY_V2.md` | None. | Falsified quantifier extension; omit entirely. |
| `EDITORIAL_HISTORY` | Research correction history and Task 52--57 discovery chronology | `research/paper/proof_completion/TARGET_A_STALE_RANK_CLAIM_AUDIT.md` | Internal import control only. | Do not import correction chronology, task numbers, agent language, commit narrative, or retraction story into the paper. |
| `REVIEW_HISTORY` | Hostile reviews and editorial verdicts | `research/paper/proof_completion/12_referee_review/TASK575_HOSTILE_REVIEW.md` | Internal quality control only. | A review verdict is not theorem evidence and must not be copied as proof or manuscript narrative. |

## Claim Coverage Audit

Every accepted canonical claim ID is assigned exactly once at claim level:

```text
MAIN_MANUSCRIPT_IMPORT:
T1.1-T1.4, T2.1-T2.3, T3.1-T3.3, T4.0-T4.3, T5.1-T5.2,
T6.0-T6.2, T7.1-T7.3, T8.0-T8.4, C.1-C.6, C.8.

STATEMENT_OVERVIEW_ONLY:
T6.3.

SUPPLEMENT_ONLY:
T6.4-T6.6, C.7.

DO_NOT_IMPORT_FIRST_SUBMISSION:
A.1-A.6, C.9.
```

This is 46 accepted claim IDs in total. Supporting payload rows do not
reclassify their parent claims.

## Locked Editorial Consequences

1. The first-submission story is one problem with two answer layers: the
   exact even-order classification says what happens; the reference/G6
   mechanism explains why failure is eventually permanent.
2. Exact finite classification determines the irregular small-order pattern.
   It does not claim a conceptual G6 explanation for the isolated failures at
   32 and 40.
3. Phase-slip localization gives the analytic tail `n>=240`; exact finite
   verification of `48<=n<240` shows that continuous failure begins precisely
   at order 48.
4. Exact-`2r` is a structural strengthening, not a dependency of the sharp
   classification threshold. Its full proof is the first removable module if
   the submission is too long.
5. No p<=24 frontier, moments, multi-gap result, reference graph, period 25,
   period 26, interaction analysis, common liminf/limit program, or correction
   history may be imported automatically or manually into the first
   submission without a later explicit scope revision.
