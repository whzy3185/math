# Task 58 Narrative and Dependency Maps

Status: `TASK58_2_INTERNAL_PLANNING_ARTIFACT`.

This document fixes two different orders for the first-submission manuscript:
the order in which the result should be revealed to a reader and the order in
which the final theorem is mathematically proved. It introduces no theorem,
changes no evidence label, and does not enlarge the scope frozen in
`TASK58_FIRST_SUBMISSION_SCOPE.md`.

## 1. Narrative Reveal Map

The Introduction should reveal the story in the following order:

```text
the fixed-graph signing problem and Suvagiya's conjecture
  -> the explicit candidate and its proposed value rho_-(n)
  -> the surprising complete answer
       equality at 8,10,...,30,34,36,38,42,44,46
       strict failure at 32, 40, and every even n>=48
  -> the structural explanation, beginning with the question:
       what makes failure eventually permanent?
  -> the period-eight reference bulk and its edge eta
  -> gap/charge coordinates and the two closure laws
  -> G6 as the unique least-cost abnormal positive single gap
       eta=E(4)<c_6=E(6)
       E(g)>c_6+1/250 for g notin {4,6}
       dim ker(H_6-c_6)=2
  -> legal one-, two-, and three-G6 finite-ring constructions
  -> patch identification plus IMS localization
       explains and proves eventual permanence for n>=240
  -> exact finite classification
       determines the irregular small-order pattern
       and the 48--238 bridge sharpens the continuous onset to 48
  -> the complete classification revisited as a proved synthesis
```

The first appearance of the complete answer is a **narrative reveal**, not a
premise from which the later structural results are deduced. The reader sees
the classification early because it is the headline. The subsequent sections
then explain the large-order mechanism and close every logical component.

Three verbs are deliberately distinct:

- The exact finite classification **determines** the irregular small-order
  pattern, including the isolated failures at 32 and 40 and the return to
  equality at 34, 36, 38, 42, 44, and 46. It does not provide a G6-style
  conceptual explanation for that irregularity.
- The reference phase, G6 construction, patch theorem, and IMS argument
  **explain and prove eventual permanence** of failure. Their direct analytic
  range begins at 240, not 48.
- The 96-order exact finite bridge for `48<=n<240` **sharpens the continuous
  onset to 48**. Thus G6/IMS supplies the permanent tail mechanism, while the
  finite bridge identifies its sharp certified onset in the final theorem.

## 2. Mathematical Dependency Map

The proof DAG is noncircular and ends, rather than begins, with the complete
classification.

```text
switching invariance and cyclic (tau,Q,alpha) coordinates
  +--------------------------------------------------------------+
  |                                                              |
  v                                                              v
candidate attainment                                      finite exact branch
T8.0: m_n<=rho_-(n) for every even n                 C.1,C.2 -> T8.1
                                                         C.3 -> T8.2
                                                         C.4 -> T8.3
                                                               |
                                                               |
reference phase T2.1--T2.3                                   |
  -> gap/charge and sector laws T3.1--T3.3                    |
  -> G6 essential-spectrum and edge chain T4.0--T4.3          |
  -> finite-ring patch identification T6.0                    |
  -> exact IMS and separated-patch cap T6.1--T6.2             |
  -> legal residue constructions T7.1                         |
  -> analytic failure for every even n>=240                   |
            +                                                  |
     C.5: 96 exact certificates for every even 48<=n<240      |
            |                                                  |
            v                                                  |
     T7.3: failure for every even n>=48 -----------------------+
                                                               |
T8.0 + T8.1 + T8.2 + T8.3 + T7.3                              |
  -> disjoint exhaustive partition of all even n>=8 <----------+
  -> T8.4 complete classification
```

Expanded by order range, the terminal synthesis is:

```text
C.1 + T8.0  -> equality for even 8<=n<=30
C.2         -> strict failure at n=32
C.3 + T8.0  -> equality at n=34,36,38,42,44,46
C.4         -> strict failure at n=40
C.5         -> strict failure for every even 48<=n<240
G6 + patch + IMS + residue constructions
             -> strict failure for every even n>=240
all six disjoint regions
             -> T8.4
```

Candidate attainment and finite exhaustion are separate inputs. A
no-counterexample certificate supplies the universal lower bound
`m_n>=rho_-(n)`; it becomes equality only after `T8.0` supplies
`m_n<=rho_-(n)`. Conversely, one exact witness is enough to prove strict
failure. No optimizer classification or exact value of `m_n` at a failing
order is used or obtained.

The single-gap hierarchy `T5.1`--`T5.2` is the structural optimality theorem
that explains why G6 is distinguished among abnormal positive single gaps.
It strengthens the manuscript's explanation but is not a hidden premise of
the finite decisions `C.1`--`C.5`. Likewise, the exact-`2r` refinement
`T6.3`--`T6.4` is valid but nonessential to `T7.3`, `N_star=48`, and `T8.4`.

## 3. Theorem-Source Traceability

The following table binds each node used above to the canonical source from
which manuscript prose may later be reconstructed.

| Map node | Claim IDs | Canonical theorem source | Logical role |
|---|---|---|---|
| Switching and flux coordinates | `T1.1`--`T1.4` | `research/paper/proof_completion/TARGET_A_FINAL_CLAIM_EVIDENCE_MATRIX_V2.md`; `research/paper/proof_completion/04_charge_sector/FULL_PROOF.md` | Defines the fixed optimization problem and the cyclic coordinates used by both branches. |
| Candidate attainment | `T8.0` | `research/paper/proof_completion/01_even_order_classification/CANDIDATE_ATTAINMENT_LEMMA.md` | Gives `m_n<=rho_-(n)` analytically for every even `n>=8`. |
| Reference phase | `T2.1`--`T2.3` | `research/paper/proof_completion/03_reference_phase/FULL_PROOF.md` | Establishes the period-eight bulk and its exact squared edge `eta`. |
| Gap, charge, and sector closure | `T3.1`--`T3.3` | `research/paper/proof_completion/04_charge_sector/FULL_PROOF.md` | Separates mod-8 ring closure from mod-4 local sector shift and validates residue words. |
| G6 spectral edge | `T4.0`--`T4.3`, `C.6` | `research/paper/proof_completion/05_g6_edge/ESSENTIAL_SPECTRUM_LEMMA.md`; `research/paper/proof_completion/05_g6_edge/FULL_PROOF.md`; `research/paper/proof_completion/05_g6_edge/COMPUTER_ASSISTED_BOUNDARY.md` | Proves discreteness above `eta`, realizes and globally identifies `c_6`, and proves rank two. |
| Single-gap hierarchy | `T5.1`--`T5.2`, `C.8` | `research/paper/proof_completion/06_single_gap/FULL_PROOF.md`; `research/paper/proof_completion/06_single_gap/COMPUTER_ASSISTED_BOUNDARY.md` | Identifies G6 as the unique least-cost abnormal positive single gap and proves the strict `1/250` separation. |
| Patch and IMS mechanism | `T6.0`--`T6.2` | `research/paper/proof_completion/07_exact_2r/PATCH_IDENTIFICATION_LEMMA.md`; `research/paper/proof_completion/08_residue_ims/FULL_PROOF.md` | Transfers the infinite G6 edge to separated finite-ring competitors and yields the analytic tail. |
| Residue constructions and eventual tail | `T7.1`--`T7.3` | `research/paper/proof_completion/08_residue_ims/FULL_PROOF.md`; `research/paper/proof_completion/01_even_order_classification/FULL_PROOF.md` | Supplies legal constructions and combines the analytic `n>=240` tail with the finite bridge. |
| Small-order decisions | `T8.1`--`T8.3`, `C.1`--`C.4` | `research/paper/proof_completion/01_even_order_classification/FULL_PROOF.md`; `research/paper/proof_completion/02_small_order_34_46/FULL_PROOF.md` | Determines the irregular finite pattern exactly. |
| Finite onset bridge | `C.5` | `research/paper/proof_completion/01_even_order_classification/COMPUTER_ASSISTED_BOUNDARY.md` | Covers all 96 even orders `48<=n<240` and sharpens the continuous onset to 48. |
| Complete theorem | `T8.4` | `research/paper/proof_completion/01_even_order_classification/THEOREM_STATEMENT.md`; `research/paper/proof_completion/01_even_order_classification/FULL_PROOF.md` | Combines the candidate, finite decisions, finite bridge, and analytic tail over a disjoint exhaustive partition. |
| Optional exact-`2r` refinement | `T6.3`--`T6.4`, `C.7` | `research/paper/proof_completion/07_exact_2r/THEOREM_STATEMENT.md`; `research/paper/proof_completion/07_exact_2r/FULL_PROOF.md` | Statement/overview only; not a dependency of the classification or sharp onset. |

Evidence labels, finite-object boundaries, and independent-checker provenance
remain normative in
`research/paper/proof_completion/TARGET_A_FINAL_CLAIM_EVIDENCE_MATRIX_V2.md`
and the corresponding `COMPUTER_ASSISTED_BOUNDARY.md` files. This planning
document cannot upgrade a finite computation or replace its human reduction.

## 4. Internal-Only Use

These maps are internal planning artifacts and must **not** become manuscript
infographics. They answer two editorial questions that a single published
diagram would blur:

1. The narrative map is deliberately chronological from the reader's point
   of view and announces the surprising complete answer before its proof.
2. The dependency map is a logical DAG and permits the complete theorem only
   at the end, after its analytic and computer-assisted leaves are closed.

Turning either map into a polished figure would invite readers to interpret
narrative arrows as mathematical implication, hide the distinction between
analytic deductions and exact finite certificates, and compete with the
three authorized figures that depict actual mathematical objects. The paper
should instead express the narrative map in the Introduction roadmap and the
dependency map through theorem order, explicit cross-references, and the
computer-assisted proof boundary.

## 5. Forbidden Collapses and Inferences

- Do not infer the isolated small-order pattern from G6 or IMS.
- Do not claim that G6/IMS alone proves the sharp onset `N_star=48`.
- Do not infer equality from nonfailure without candidate attainment `T8.0`.
- Do not replace the mod-8 ring-closure law by the mod-4 sector-shift law.
- Do not infer arbitrary multi-gap optimality from the single-gap hierarchy.
- Do not use exact-`2r`, `3505r(9/25)^ell`, or `N_exp=3120` as premises of
  the sharp classification.
- Do not infer a common liminf or limit from the residue-class `limsup`.
- Do not claim a classification of all minimizers or exact failing values.

The canonical proof package overrides this document if any wording conflict
is discovered during manuscript reconstruction.
