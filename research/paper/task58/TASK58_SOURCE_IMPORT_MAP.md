# Task 58 Source Import Map

Status: `TASK58_0_EDITORIAL_CONTROL`.

This file is an editorial import map for the first submission. It creates no
new theorem, changes no evidence label, and does not make a review document,
research-stage artifact, script, or certificate into a mathematical source.
The normative claim statements and evidence labels remain those in
`research/paper/proof_completion/TARGET_A_FINAL_CLAIM_INVENTORY_V2.md` and
`research/paper/proof_completion/TARGET_A_FINAL_CLAIM_EVIDENCE_MATRIX_V2.md`.

## Import Rules

The canonical theorem and proof sources are under
`research/paper/proof_completion/`. The `Source` column below always names an
existing canonical file. Machine artifacts are identified only through the
canonical computer-assisted boundary and are not substitutes for the human
reduction or mathematical consequence.

Placement codes are:

```text
MAIN      import the stated result and the required human proof into the body;
OVERVIEW  retain only a statement, interpretation, and short proof overview;
APP       place the indicated proof detail in the named optional appendix;
SUPP      place reproducibility or deliberately deferred proof detail in the supplement;
OMIT      do not import into the first submission.
```

The intended body destinations are:

```text
S1  Introduction
S2  Switching Coordinates and the Reference Phase
S3  Gaps, Charges, and Translation Sectors
S4  The Elementary Six-Gap Phase Slip
S5  Optimality Among Single-Gap Interfaces
S6  Phase Slips on Finite Rings
S7  Finite Completion of the Classification
```

The intended optional appendices are:

```text
App A  Period-Eight Floquet Algebra
App B  G6 Matching Certificate
App C  Single-Gap Witnesses
App D  Separated-Interface Estimates
App E  Finite Classification Certificates
```

`CA boundary` uses the required four-stage convention: mathematical
reduction, finite exact object, independent machine verification, and
mathematical consequence. `None` means that no computation is logically
required. `Corroborative only` means that a checker may audit an analytic
proof but is not one of its premises. `Upstream` means that the displayed
deduction is analytic but uses a separately certified theorem.

## First-Submission Claim Map

| Claim ID | Canonical theorem | Source | Evidence status | Main destination | Appendix | Supplement | Required proof depth | CA boundary | Forbidden historical source | Notes |
|---|---|---|---|---|---|---|---|---|---|---|
| `T1.1` | Hamilton gauge and switching invariance | `research/paper/proof_completion/03_reference_phase/FULL_PROOF.md` | `PURE_ANALYTIC_PROVED` | `MAIN S2` | None | None | Full diagonal-conjugacy and gauge argument | None | `H1`, `H2`, `ER` | Define the signed-graph model before flux coordinates. |
| `T1.2` | Cyclic `(tau,Q,alpha)` parametrization | `research/paper/proof_completion/04_charge_sector/FULL_PROOF.md` | `PURE_ANALYTIC_PROVED` | `MAIN S2` | None | None | Full lift, parity, and holonomy argument in the scope used later | None | `H1`, `H2`, `ER` | Keep candidate signing and reference phase distinct. |
| `T1.3` | Translation, reflection, lift-negation, and zone-folding equivalences | `research/paper/proof_completion/03_reference_phase/FULL_PROOF.md` | `PURE_ANALYTIC_PROVED` | Short uses in `S2`, `S5`, `S6` | `App A` | None | State the needed intertwiners; full equivalence proof in appendix | Corroborative only | `H1`, `H2`, `ER` | No machine result is a premise. |
| `T1.4` | Exact range-four formula for `H=A_tau^2` | `research/paper/proof_completion/03_reference_phase/FULL_PROOF.md` | `PURE_ANALYTIC_PROVED` | `MAIN S2` | None | None | Print and derive the local formula used by IMS and witnesses | Corroborative only | `H1`, `H2`, `ER` | Preserve unsquared `A_tau` versus squared `H_tau`. |
| `T2.1` | Exact period-eight Bloch polynomial | `research/paper/proof_completion/03_reference_phase/FULL_PROOF.md` | `COMPUTER_ASSISTED_PROVED` | Brief statement in `S2` | `App A` | Reproduction metadata | Full fiber convention and determinant identity in appendix | Exact symbolic determinant reconstruction plus independent audit | `H1`, `H2`, `ER` | Use the registered quartic exactly. |
| `T2.2` | Reference squared edge `eta` and unique Bloch maximizer | `research/paper/proof_completion/03_reference_phase/FULL_PROOF.md` | `EXACT_ALGEBRAIC_PROVED` | `MAIN S2` | `App A` | Optional arithmetic audit | Full endpoint factorization and uniqueness argument | Exact audit is corroborative; `T2.1` is the certified algebraic input | `H1`, `H2`, `ER` | State `eta=4+sqrt(10+2sqrt(5))<8`. |
| `T2.3` | Gap four is the reference bulk | `research/paper/proof_completion/03_reference_phase/FULL_PROOF.md` | `PURE_ANALYTIC_PROVED` | `MAIN S2` | None | None | Full identification up to the proved equivalences | None | `H1`, `H2`, `ER` | `g=4` is not an abnormal interface. |
| `T3.1` | Gap sum, charge sum, and cyclic parity closure | `research/paper/proof_completion/04_charge_sector/FULL_PROOF.md` | `PURE_ANALYTIC_PROVED` | `MAIN S3` | None | None | Full cyclic telescoping and lift-parity proof | None | `H1`, `H2`, `ER` | Keep `sum q_j=n-4d` and `sum q_j congruent n mod 8` separate. |
| `T3.2` | Sector law `sigma_sec(q)=q mod 4` | `research/paper/proof_completion/04_charge_sector/FULL_PROOF.md` | `PURE_ANALYTIC_PROVED` | `MAIN S3` | None | None | Full endpoint-residue proof | Corroborative only | `H1`, `H2`, `ER` | Do not replace by the false `q/2 mod 4` law. |
| `T3.3` | Additive sector composition and closure | `research/paper/proof_completion/04_charge_sector/FULL_PROOF.md` | `PURE_ANALYTIC_PROVED` | `MAIN S3` | None | None | Full concatenation argument | None | `H1`, `H2`, `ER` | Mod-4 sector shift does not replace mod-8 ring closure. |
| `T4.0` | G6 essential spectrum and exponential tail matching | `research/paper/proof_completion/05_g6_edge/ESSENTIAL_SPECTRUM_LEMMA.md` | `PURE_ANALYTIC_PROVED` | `MAIN S4` | `App B` | None | Full finite-rank decoupling, half-line essential-spectrum, discreteness, and decay bridge | Corroborative only | `H1`, `H2`, `ER` | Establish discreteness above `eta` before Evans matching. |
| `T4.1` | Exact algebraic definition and isolation of `c6` | `research/paper/proof_completion/05_g6_edge/THEOREM_STATEMENT.md` | `COMPUTER_ASSISTED_PROVED` | `MAIN S4` | `App B` | Root certificate and checker metadata | Print the degree-ten polynomial and rational isolating interval; defer isolation audit | Exact elimination and interval root count with independent checker | `H1`, `H2`, `ER` | Define `c6` exactly before giving a decimal. |
| `T4.2` | Global G6 squared spectral edge equals `c6` | `research/paper/proof_completion/05_g6_edge/FULL_PROOF.md` | `COMPUTER_ASSISTED_PROVED` | `MAIN S4` | `App B` | Certificate schema, hashes, commands, tamper tests | Full four-lemma proof skeleton; complete charts and exact exclusions in appendix | Finite resultant candidates, Grassmann cover, Sturm isolation, and unsquared physical matching | `H1`, `H2`, `ER` | Candidate completeness and physical realization must remain distinct. |
| `T4.3` | Rank-two G6 eigenspace and simple unsquared partners | `research/paper/proof_completion/05_g6_edge/FULL_PROOF.md` | `ANALYTIC_COROLLARY_OF_CERTIFIED_INPUTS` | `MAIN S4` | `App B` | Optional symmetry audit | Full proof from `K^2=-I`, `KA_6=-A_6K`, self-adjointness, and certified positive-root simplicity | Upstream `T4.2` and `C.6`; finite controls do not replace symmetry | `H1`, `H2`, `ER` | State `dim ker(H_6-c6)=2`; never call `c6` simple for `H_6`. |
| `T5.1` | G6 uniquely minimizes the abnormal single-gap edge | `research/paper/proof_completion/06_single_gap/FULL_PROOF.md` | `ANALYTIC_COROLLARY_OF_CERTIFIED_INPUTS` | `MAIN S5` | `App C` optional | Full integer vectors and reconstruction metadata | Full variational partition of all positive gaps, with exact quotient summaries | Upstream certified `c6`; exact integer witness reconstruction for finite classes | `H1`, `H2`, `ER` | Scope is single gaps only, both lifts and orientations. |
| `T5.2` | Uniform single-gap separation by `1/250` | `research/paper/proof_completion/06_single_gap/FULL_PROOF.md` | `ANALYTIC_COROLLARY_OF_CERTIFIED_INPUTS` | `MAIN S5` | `App C` optional | Complete margin table and checker metadata | Give exact rational comparison and the strict uniform conclusion | Exact cross-multiplication against the upper isolating endpoint for `c6` | `H1`, `H2`, `ER` | No decimal comparison and no multi-gap extrapolation. |
| `T6.0` | Finite-ring G6 patch identification | `research/paper/proof_completion/07_exact_2r/PATCH_IDENTIFICATION_LEMMA.md` | `PURE_ANALYTIC_PROVED` | `MAIN S6` | `App D` optional | None | Full local coefficient, seam, lift, orientation, and holonomy identification needed by IMS | Corroborative only | `H1`, `H2`, `ER` | This bridge is required even though exact-`2r` is downgraded. |
| `T6.1` | Exact discrete IMS identity and range-four error | `research/paper/proof_completion/08_residue_ims/FULL_PROOF.md` | `PURE_ANALYTIC_PROVED` | `MAIN S6` | None | None | Full double-commutator identity and cyclic tent estimate | None | `H1`, `H2`, `ER` | This, not exact-`2r`, drives the analytic tail. |
| `T6.2` | Separated-G6 patch classification and global cap | `research/paper/proof_completion/08_residue_ims/FULL_PROOF.md` | `ANALYTIC_COROLLARY_OF_CERTIFIED_INPUTS` | `MAIN S6` | None | None | Full deduction from patch identification, bulk/G6 edges, and IMS | Upstream `T4.2`; no new finite enumeration | `H1`, `H2`, `ER` | Retain only `r in {1,2,3}` and the stated separation conditions. |
| `T6.3` | Exact `2r` near-`c6` cluster | `research/paper/proof_completion/07_exact_2r/THEOREM_STATEMENT.md` | `COMPUTER_ASSISTED_PROVED` | `OVERVIEW S6` | `App D` only if page budget permits | Full proof preferred | Statement, spectral interpretation, and short proof overview only in the manuscript | Exact Floquet constants and G6 isolation verified independently | `H1`, `H2`, `ER` | Structural strengthening; not a premise of `N_star=48`. |
| `T6.4` | Codimension-`2r` complement and `2r x 2r` Feshbach theorem | `research/paper/proof_completion/07_exact_2r/FULL_PROOF.md` | `COMPUTER_ASSISTED_PROVED` | `OVERVIEW S6` without detailed formulas | `App D` only if retained | Full Gram, complement-gap, Feshbach proof and `3505r(9/25)^ell` constants | Exact rational interval and endpoint audit | `H1`, `H2`, `ER` | Never shorten `2r` to `r`. |
| `T6.5` | Sufficient exponential onset `N_exp=3120` | `research/paper/proof_completion/07_exact_2r/FULL_PROOF.md` | `COMPUTER_ASSISTED_PROVED` | No body claim beyond optional overview | `App D` only if retained | Full endpoint proof and constants | Supplemental proof depth; not needed for the sharp classification | Exact endpoint margins and monotonicity audit | `H1`, `H2`, `ER` | `N_exp` is sufficient, not optimal, and is unrelated to the sharp onset 48. |
| `T6.6` | Protected double top on the standard one-G6 ring | `research/paper/proof_completion/07_exact_2r/FULL_PROOF.md` | `COMPUTER_ASSISTED_PROVED` | Optional sentence in the `S6` overview | `App D` only if retained | Full proof and checker details | Supplemental structural result | Analytic symmetry plus certified exact-`2r` rank bound and finite checker | `H1`, `H2`, `ER` | Do not infer general finite-ring simplicity. |
| `T7.1` | Legal one-, two-, and three-G6 residue words | `research/paper/proof_completion/08_residue_ims/FULL_PROOF.md` | `PURE_ANALYTIC_PROVED` | `MAIN S6` | None | None | Full gap-sum, mod-8 closure, mod-4 sector, holonomy, and separation checks | None | `H1`, `H2`, `ER` | Use the displayed words only when exponents are nonnegative. |
| `T7.2` | Nonzero-residue `limsup` upper bounds | `research/paper/proof_completion/08_residue_ims/FULL_PROOF.md` | `ANALYTIC_COROLLARY_OF_CERTIFIED_INPUTS` | `MAIN S6` | None | None | Full limiting deduction from `T6.2` and `T7.1` | Upstream G6 edge only | `H1`, `H2`, `ER` | Say `limsup`; do not claim a lower bound or limit. |
| `T7.3` | Explicit counterexample at every even `n>=48` | `research/paper/proof_completion/01_even_order_classification/FULL_PROOF.md` | `COMPUTER_ASSISTED_PROVED` | `MAIN S6` and closure in `S7` | `App E` for the finite bridge | `C.5` artifacts and reproduction metadata | Full analytic proof for `n>=240`; state and justify the disjoint 96-order bridge | 96 exact rational LDL records for `48<=n<240`; analytic IMS afterward | `H1`, `H2`, `ER` | G6 explains eventual permanence; the finite bridge makes the exact onset 48. |
| `T8.0` | Antibalanced candidate attains `rho_-(n)` | `research/paper/proof_completion/01_even_order_classification/CANDIDATE_ATTAINMENT_LEMMA.md` | `PURE_ANALYTIC_PROVED` | `MAIN S1`, proof in `S2` | None | None | Full antiperiodic two-site Fourier proof and exact endpoint maximization | Corroborative only | `H1`, `H2`, `ER` | Required separately from exhaustion to prove equality at valid orders. |
| `T8.1` | Exact truth through order 32 | `research/paper/proof_completion/01_even_order_classification/FULL_PROOF.md` | `COMPUTER_ASSISTED_PROVED` | `MAIN S7` | `App E` | `C.1`, `C.2` artifacts | State finite reduction and exact order-32 witness; appendix proves completeness | Exhaustive switching classes plus exact Bareiss/LDL verification | `H1`, `H2`, `ER` | Separates no failures through 30 from strict failure at 32. |
| `T8.2` | No failures at `34,36,38,42,44,46` | `research/paper/proof_completion/02_small_order_34_46/FULL_PROOF.md` | `COMPUTER_ASSISTED_PROVED` | `MAIN S7` | `App E` | `C.3` artifacts and resource notes | State theorem and explain local compression; appendix proves graph soundness/completeness and terminal closure | 57,344 windows, parity-lifted graph, 64 terminals, both holonomies, zero unresolved | `H1`, `H2`, `ER` | The authoritative terminal total is 64, not 84. |
| `T8.3` | Exact strict counterexample at order 40 | `research/paper/proof_completion/02_small_order_34_46/FULL_PROOF.md` | `COMPUTER_ASSISTED_PROVED` | `MAIN S7` | `App E` | `C.4` artifacts | Short exact witness proposition; full rational LDL boundary in appendix | Independent exact rational LDL reconstruction | `H1`, `H2`, `ER` | Do not merge this witness with the six no-failure terminal records. |
| `T8.4` | Complete even-order truth classification | `research/paper/proof_completion/01_even_order_classification/FULL_PROOF.md` | `COMPUTER_ASSISTED_PROVED` | Statement in `S1`, final proof in `S7` | None beyond cited component appendices | Component reproduction only | Full disjoint partition and equality logic from `T8.0`, `T8.1`-`T8.3`, and `T7.3` | No monolithic computation; inherits the exact boundaries of the five certified finite families | `H1`, `H2`, `ER` | Classifies truth, not all minimizers or exact failing values. |

## First-Submission Computer-Assisted Lemmas

These rows expose the finite exact leaves used by the preceding claims. They
must not be restated as empirical searches.

| Claim ID | Canonical theorem | Source | Evidence status | Main destination | Appendix | Supplement | Required proof depth | CA boundary | Forbidden historical source | Notes |
|---|---|---|---|---|---|---|---|---|---|---|
| `C.1` | Exhaustion for even orders `8<=n<=30` | `research/paper/proof_completion/01_even_order_classification/COMPUTER_ASSISTED_BOUNDARY.md` | `COMPUTER_ASSISTED_PROVED` | Finite lemma summary in `S7` | `App E` | Commands, paths, expected PASS | Prove finite quotient and endpoint meaning; appendix records exhaustive object | Exact class streams and independent record/spectral reconstruction | `H1`, `H2`, `ER` | Supports `T8.1`. |
| `C.2` | Exact order-32 witness | `research/paper/proof_completion/01_even_order_classification/COMPUTER_ASSISTED_BOUNDARY.md` | `COMPUTER_ASSISTED_PROVED` | Short proposition in `S7` | `App E` | Certificate metadata | Explain why positive definiteness gives the strict spectral cap | Exact matrix, Bareiss/LDL, flux, and radical reconstruction | `H1`, `H2`, `ER` | Existence requires one verified witness, not enumeration. |
| `C.3` | Exhaustive finite-state closure at six orders | `research/paper/proof_completion/02_small_order_34_46/COMPUTER_ASSISTED_BOUNDARY.md` | `COMPUTER_ASSISTED_PROVED` | Finite theorem summary in `S7` | `App E` | Certificate schema, command, resource notes | Full mathematical reduction: local interlacing, overlap graph, parity, cyclic and holonomy closure | Independent rebuild of all windows, walks, and 64 terminal decisions | `H1`, `H2`, `ER` | `terminal_unresolved=0` is required. |
| `C.4` | Exact order-40 witness | `research/paper/proof_completion/02_small_order_34_46/COMPUTER_ASSISTED_BOUNDARY.md` | `COMPUTER_ASSISTED_PROVED` | Short proposition in `S7` | `App E` | Certificate metadata | Explain exact threshold and positive-definiteness consequence | Exact rational LDL reconstruction | `H1`, `H2`, `ER` | Separate from `C.3`. |
| `C.5` | Exact bridge for every even `48<=n<240` | `research/paper/proof_completion/01_even_order_classification/COMPUTER_ASSISTED_BOUNDARY.md` | `COMPUTER_ASSISTED_PROVED` | Finite bridge lemma in `S7` | `App E` | Paths, command, expected PASS | Prove interval coverage and explain the exact matrix inequality | 96 independently reconstructed rational LDL records | `H1`, `H2`, `ER` | The interval ends at 238. |
| `C.6` | Complete physical G6 matching audit | `research/paper/proof_completion/05_g6_edge/COMPUTER_ASSISTED_BOUNDARY.md` | `COMPUTER_ASSISTED_PROVED` | Four-stage boundary summarized in `S4` | `App B` | Schema, hashes, commands, tamper tests | Prove why physical zeros lie among finite candidates and why checked exclusions imply the edge theorem | Exact root isolation, global chart cover, resultant/Sturm candidates, and two unsquared physical chart checks | `H1`, `H2`, `ER` | Resultant roots alone do not prove `T4.2`. |
| `C.7` | Exact-`2r` constants and endpoint audit | `research/paper/proof_completion/07_exact_2r/COMPUTER_ASSISTED_BOUNDARY.md` | `COMPUTER_ASSISTED_PROVED` | No detail beyond `OVERVIEW S6` | `App D` only if retained | Full finite object, checker, constants, tamper tests | Full proof belongs in supplement unless page budget retains App D | Independent reconstruction of all cuts and rational interval/endpoint bounds | `H1`, `H2`, `ER` | Must preserve rank `2r`, codimension `2r`, and `2r x 2r`. |
| `C.8` | Exact single-gap witness arithmetic | `research/paper/proof_completion/06_single_gap/COMPUTER_ASSISTED_BOUNDARY.md` | `COMPUTER_ASSISTED_PROVED` | Exact quotient summary in `S5` | `App C` optional | Full vectors, margin table, checker metadata | Explain finite/tail partition and Rayleigh consequence; defer complete table | Independent integer reconstruction and exact cross-multiplication | `H1`, `H2`, `ER` | Covers single gaps only. |

## Canonical Claims Omitted From The First Submission

These accepted claims remain true at their registered evidence level, but the
Task 58 scope contract forbids importing them into the first submission.

| Claim ID | Canonical theorem | Source | Evidence status | Main destination | Appendix | Supplement | Required proof depth | CA boundary | Forbidden historical source | Notes |
|---|---|---|---|---|---|---|---|---|---|---|
| `A.1` | General squared-moment identities | `research/paper/proof_completion/09_moments_periodic/FULL_PROOF.md` | `COMPUTER_ASSISTED_PROVED` | `OMIT` | None | None | None for this submission | Not imported | `H1`, `H2`, `ER` | Full/general moment machinery is outside the locked story. |
| `A.2` | Period-eight trichotomy | `research/paper/proof_completion/09_moments_periodic/FULL_PROOF.md` | `COMPUTER_ASSISTED_PROVED` | `OMIT` | None | None | None for this submission | Not imported | `H1`, `H2`, `ER` | Do not use as optional structural decoration. |
| `A.3` | Primitive periodic frontier through period 24 | `research/paper/proof_completion/09_moments_periodic/FULL_PROOF.md` | `COMPUTER_ASSISTED_PROVED` | `OMIT` | None | None | None for this submission | Not imported | `H1`, `H2`, `ER` | The bounded frontier and all period-25/26 data are excluded. |
| `A.4` | Support-at-most-18 multi-gap obstruction | `research/paper/proof_completion/TARGET_A_FINAL_CLAIM_INVENTORY_V2.md` | `COMPUTER_ASSISTED_PROVED` | `OMIT` | None | None | None for this submission | Not imported | `H1`, `H2`, `ER` | Multi-gap obstruction package is excluded. |
| `A.5` | Arbitrary-length `(3,3)` local obstruction | `research/paper/proof_completion/TARGET_A_FINAL_CLAIM_INVENTORY_V2.md` | `COMPUTER_ASSISTED_PROVED` | `OMIT` | None | None | None for this submission | Not imported | `H1`, `H2`, `ER` | Do not broaden single-gap optimality. |
| `A.6` | Remaining multi-gap finite-alphabet reduction | `research/paper/proof_completion/TARGET_A_FINAL_CLAIM_INVENTORY_V2.md` | `ANALYTIC_COROLLARY_OF_CERTIFIED_INPUTS` | `OMIT` | None | None | None for this submission | Not imported | `H1`, `H2`, `ER` | No universal finite-core theorem follows. |
| `C.9` | Primitive periodic finite orbit through period 24 | `research/paper/proof_completion/09_moments_periodic/COMPUTER_ASSISTED_BOUNDARY.md` | `COMPUTER_ASSISTED_PROVED` | `OMIT` | None | None | None for this submission | Not imported | `H1`, `H2`, `ER` | The periodic frontier is not a first-submission lemma. |

## Exact-Path Blacklist

The blacklist overrides every directory-level import permission. Codes `H1`
and `H2` are `DO_NOT_IMPORT_CURRENT_CLAIMS`; code `ER` denotes the entire
superseded exact-`r` corpus. None of these paths may supply a current theorem,
formula, lemma, proof step, mode count, codimension, or Feshbach dimension.

### Current-Claim Hazards

| Code | Exact path | Category | Hazard |
|---|---|---|---|
| `H1` | `research/proofs/task52/TARGET_A_MULTI_SLIP_INTERACTION_ASYMPTOTICS.md` | `DO_NOT_IMPORT_CURRENT_CLAIMS` | Contains the obsolete heuristic `H_eff=c6 I_r+...`; the accepted local space has dimension `2r`. |
| `H2` | `research/proofs/task54/TARGET_A_COMMON_RESIDUE_LIMIT_SCOPE.md` | `DO_NOT_IMPORT_CURRENT_CLAIMS` | Calls a later-falsified exact-`r` theory current and must not source limit or rank claims. |

### Superseded Exact-`r` Corpus (`ER`)

Every path below is `HISTORICAL_ONLY`:

```text
research/proofs/task53/TARGET_A_FESHBACH_EFFECTIVE_MATRIX.md
research/proofs/task53/TARGET_A_TASK53_REVIEWS.md
research/proofs/task54/TARGET_A_COMPLEMENT_GAP_THEOREM.md
research/proofs/task54/TARGET_A_EFFECTIVE_COUPLING_FORMULAS.md
research/proofs/task54/TARGET_A_EXACT_R_PHASE_SLIP_EXCITATION_THEOREM.md
research/proofs/task54/TARGET_A_EXACT_R_RIESZ_THEOREM.md
research/proofs/task54/TARGET_A_EXPONENTIAL_EVENTUAL_THRESHOLD.md
research/proofs/task54/TARGET_A_EXPONENTIAL_FIXED_R_GLOBAL_CAP.md
research/proofs/task54/TARGET_A_EXPONENTIAL_RESIDUE_BOUNDS.md
research/proofs/task54/TARGET_A_FESHBACH_EFFECTIVE_HAMILTONIAN.md
research/proofs/task54/TARGET_A_GEOMETRIC_RESOLVENT_GLUE.md
research/proofs/task54/TARGET_A_TASK54_CONTINUATION_BASELINE.md
research/proofs/task54/TARGET_A_TASK54_CONTINUATION_DEPENDENCY_GRAPH.md
research/proofs/task54/TARGET_A_TASK54_CONTINUATION_MASTER_LEDGER.md
research/proofs/task54/TARGET_A_TASK54_CONTINUATION_SYNTHESIS.md
research/proofs/task54/lanes/exponential_cap/HANDOFF.md
research/proofs/task54/certificates/exact_r_complement_gap.json
research/scripts/target_a_task54_exact_r.py
research/scripts/verify_target_a_task54_exact_r.py
```

The last three paths may be retained or run only to verify the historical
retraction. They do not prove a positive exact-`r` theorem.

## Global Import Prohibitions

The first submission must not import any theorem, formula, proof prose, table,
figure, or narrative from the following research topics, even when a valid
repository artifact exists:

```text
periodic frontier through p<=24;
full or general moment machinery;
multi-gap obstruction package;
reference-relative graph;
period-25/26 enumeration;
interaction or pairwise-splitting fits;
three-body asymptotics;
unrestricted common-liminf or common-limit programs;
research correction history and Task 52--57 discovery chronology.
```

The frozen directories
`research/paper/manuscript_tex_pub/` and
`research/paper/manuscript_tex_pub_zh/` are `HISTORICAL_ONLY`. Their
mathematical statements and proof prose are not import sources. Only the
separately authorized class, package, author, bibliography, macro, and build
infrastructure may later be reused.

## Fail-Closed Checks

Before any manuscript section imports a claim from this map, verify all of
the following:

1. The claim ID and evidence label still match the canonical inventory.
2. The named canonical source path exists and remains `CANONICAL_IMPORT`.
3. Equality at a valid order uses both exhaustion and `T8.0` attainment.
4. `m_n` is compared with `rho_-(n)`, while `m_n^2` is compared with
   `theta_n=rho_-(n)^2`.
5. Mod-8 charge closure and mod-4 sector shift are stated separately.
6. G6 contributes two squared modes: rank `2r`, codimension `2r`, and a
   `2r x 2r` problem-specific Feshbach operator.
7. `T7.2` remains a `limsup` statement.
8. Exact-`2r` is not used to prove the sharp contiguous onset `N_star=48`.
9. Producer output is never described as independent verification.
10. No `H1`, `H2`, or `ER` path has supplied current mathematical prose.
