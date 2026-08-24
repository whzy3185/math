# Task 58 Theorem-to-Section Map

Status: `TASK58_2_EDITORIAL_BLUEPRINT`.

This map assigns each of the 46 canonical accepted claim IDs exactly once.
It is an editorial placement document, not a new theorem registry. Canonical
statements, hypotheses, constants, evidence labels, and dependencies remain
those in the Task 57.5 proof-completion package. In particular, this map does
not promote an appendix result, a supplemental result, or a finite certificate
to a stronger mathematical statement.

## Placement Vocabulary

- `MAIN_THEOREM`: one of the two claims jointly forming Introduction theorem
  box 1 and the final complete-classification theorem.
- `SUPPORTING_THEOREM`: a theorem-level structural result in the body. Claims
  contributing to Introduction theorem box 2 retain their separate canonical
  identities.
- `PROPOSITION`: a body-level structural, constructive, or finite-completion
  result supporting the main theorem.
- `LEMMA`: a proof component stated and proved at the point of use in the
  body.
- `APPENDIX_ONLY`: a formal result whose complete mathematical proof or exact
  audit belongs in an essential appendix. The body may cite or summarize it,
  but does not restate its proof as a co-equal contribution.
- `SUPPLEMENT_ONLY`: material excluded from the first-submission manuscript
  and retained only in a separately removable supplement.
- `OMIT_FIRST_SUBMISSION`: accepted mathematics deliberately excluded from
  the first submission.

The body section destinations are fixed as follows:

```text
S1  Introduction
S2  Switching Coordinates and the Reference Phase
S3  Gaps, Charges, and Translation Sectors
S4  The Elementary Six-Gap Phase Slip
S5  Optimality Among Single-Gap Interfaces
S6  Phase Slips on Finite Rings
S7  Finite Completion of the Classification
S8  Concluding Remarks
```

The essential appendices are `App A: Exact spectral certification of the
reference phase and G6` and `App B: Exact finite classification and
completeness`. Appendix B includes the mathematical exact-comparison boundary
for the single-gap witnesses. The removable exact-`2r` material is assigned
to `Supplement X`, and certificate schemas, hashes, commands, tamper tests,
full witness vectors, and resource notes are assigned to `Supplement R:
Reproducibility`. There are no visible Appendix C--E gaps in the first
submission.

## Canonical Claim Placement

| Claim ID | Editorial class | Exact destination | Required proof depth | Scope guard |
|---|---|---|---|---|
| `T1.1` | `PROPOSITION` | `S2`, Switching reduction | Full body proof of diagonal conjugacy and Hamilton gauge | Spectrum preservation only; no historical gauge narrative |
| `T1.2` | `PROPOSITION` | `S2`, Flux and holonomy coordinates | Full body proof in the cyclic scope used later | Retain both holonomies and distinguish a gauge-fixed word from an arbitrary signing |
| `T1.3` | `APPENDIX_ONLY` | `App A`, Operator equivalences; cited locally in `S2`, `S5`, `S6` | State only the needed intertwining consequences in the body; give the full unitary-equivalence proof in `App A` | No periodic-frontier inference |
| `T1.4` | `LEMMA` | `S2`, Squared local operator | Print and derive the complete range-four formula in the body | Keep unsquared `A_tau` distinct from squared `H_tau=A_tau^2` |
| `T2.1` | `APPENDIX_ONLY` | `App A`, Period-eight determinant identity; one-line citation in `S2` | Give the fiber convention and exact quartic identity in `App A`; metadata only in `Supplement R` | Do not import bounded-period results |
| `T2.2` | `SUPPORTING_THEOREM` | `S2`, Reference-phase edge; summarized in Introduction theorem box 2 | Full body proof of endpoint factorization, exact value of `eta`, and uniqueness at `z=1`; algebraic expansion may cite `App A` | `eta` is a squared edge and must be defined exactly |
| `T2.3` | `PROPOSITION` | `S2`, Reference bulk identification | Full short body proof up to the registered equivalences | Gap four is the reference bulk, not an abnormal interface |
| `T3.1` | `PROPOSITION` | `S3`, Cyclic gaps and charge | Full body telescoping and lift-parity proof | Keep exact sum identities and mod-8 ring closure distinct |
| `T3.2` | `PROPOSITION` | `S3`, Translation-sector law | Full body endpoint-residue proof of `sigma_sec(q)=q mod 4` | Never replace the law by `q/2 mod 4` |
| `T3.3` | `PROPOSITION` | `S3`, Sector composition and cyclic closure | Full body concatenation proof | Mod-4 sector shifts do not replace mod-8 charge closure |
| `T4.0` | `LEMMA` | `S4`, Essential spectrum and decay bridge; technical details in `App A` | Full body argument at theorem-proof depth, with finite-rank decoupling, half-line spectrum, discreteness, and decay; defer long operator details to `App A` | Essential spectrum gives discreteness above `eta`, not existence of `c_6` |
| `T4.1` | `LEMMA` | `S4`, Algebraic definition of `c_6`; isolation audit in `App A` | Print the degree-ten polynomial and rational isolating interval in the body; put the exact isolation audit in `App A` and metadata in `Supplement R` | Decimal values are orientation only |
| `T4.2` | `SUPPORTING_THEOREM` | `S4`, G6 global edge; summarized in Introduction theorem box 2 | Full four-lemma proof chain in the body; complete Grassmann charts, root exclusions, and physical matching in `App A` | Separate candidate completeness, realization, and maximality |
| `T4.3` | `PROPOSITION` | `S4`, G6 rank-two symmetry; summarized in Introduction theorem box 2 | Full body deduction from `K^2=-I`, anticommutation, self-adjointness, and the certified edge theorem | State `dim ker(H_6-c_6)=2`; the squared edge is not simple |
| `T5.1` | `SUPPORTING_THEOREM` | `S5`, Single-gap spectral hierarchy; summarized in Introduction theorem box 2 | Full body variational partition and exact quotient summary; detailed finite witness arithmetic may be cited from `App C` | Quantifier is positive single gaps only, including both lifts and orientations |
| `T5.2` | `SUPPORTING_THEOREM` | `S5`, Uniform single-gap separation; summarized in Introduction theorem box 2 | Full exact body comparison proving the strict `1/250` margin; complete witness table in `Supplement R` | No decimal proof and no multi-gap extrapolation |
| `T6.0` | `LEMMA` | `S6`, Finite-ring patch identification | Full body proof of coefficient matching, seam clearance, lift, orientation, holonomy, and bulk-patch coverage | This analytic bridge is independent of exact-`2r` counting |
| `T6.1` | `LEMMA` | `S6`, Discrete IMS localization | Full body proof of the double-commutator identity and cyclic tent error estimate | This is the localization engine for the analytic tail |
| `T6.2` | `SUPPORTING_THEOREM` | `S6`, Separated-slip global cap | Full body deduction from patch identification, reference/G6 local edges, and IMS | Only `r in {1,2,3}` and the registered separation hypotheses; it proves eventual failure, not onset 48 |
| `T6.3` | `SUPPORTING_THEOREM` | `S6`, exact-`2r` structural refinement overview | **Overview only:** state exact `2r` multiplicity counting, `r in {1,2,3}`, `D>=1040`, the fixed window, and a short spectral interpretation; place the full proof in `Supplement X` | Not a premise of `N_star=48`; no Gram, complement, Feshbach, or decay-constant details in the manuscript |
| `T6.4` | `SUPPLEMENT_ONLY` | `Supplement X`, Exact-`2r` Gram/Feshbach theorem | Full supplemental proof of the codimension-`2r` complement, `2r x 2r` Feshbach reduction, and `3505r(9/25)^ell` bound | Never revert `2r` to `r`; not used for sharp onset 48 |
| `T6.5` | `SUPPLEMENT_ONLY` | `Supplement X`, Exponential sufficient onset | Full supplemental endpoint and monotonicity proof | `N_exp=3120` is sufficient and nonoptimal, not the continuous onset 48 |
| `T6.6` | `SUPPLEMENT_ONLY` | `Supplement X`, Protected one-G6 double top | Full supplemental proof in the stated one-G6 symmetry class | Do not infer general finite-ring simplicity |
| `T7.1` | `PROPOSITION` | `S6`, Residue-class G6 constructions | Full body verification of gap sums, mod-8 closure, mod-4 sectors, holonomy, legal exponent range, and separation | Use the displayed words only where their exponents are nonnegative |
| `T7.2` | `PROPOSITION` | `S6`, Residue-class asymptotic upper bounds | Full body limiting deduction from T6.2 and T7.1 | Retain `limsup`; assert neither a lower bound nor a limit |
| `T7.3` | `SUPPORTING_THEOREM` | `S6`, analytic tail, and `S7`, finite bridge closure | Full analytic proof for `n>=240` in `S6`; state and justify the disjoint exact bridge `48<=n<240` in `S7`, with details in `App E` | G6 explains eventual permanence; finite verification determines exact continuous onset 48 |
| `T8.0` | `MAIN_THEOREM` | Introduction theorem box 1; proof in `S2`, Candidate attainment | Full body antiperiodic two-site Fourier proof and exact endpoint maximization | This supplies `m_n<=rho_-(n)` and remains logically separate from exhaustion |
| `T8.1` | `PROPOSITION` | `S7`, Orders 8 through 32; exact leaves in `App E` | State the finite reduction and exact order-32 witness in the body; put exhaustive object and endpoint proof in `App E` | Distinguish validity through 30 from strict failure at 32 |
| `T8.2` | `PROPOSITION` | `S7`, Six valid orders from 34 through 46; completeness in `App E` | Body theorem statement and local-compression overview; full soundness, completeness, cyclic closure, both holonomies, 64 terminals, and zero unresolved records in `App E` | The authoritative terminal count is 64, not 84 |
| `T8.3` | `PROPOSITION` | `S7`, Exact order-40 counterexample; LDL details in `App E` | Short exact witness proof in the body; complete rational LDL audit in `App E` | Keep the witness separate from the six no-failure terminal records |
| `T8.4` | `MAIN_THEOREM` | Introduction theorem box 1; final synthesis theorem and proof in `S7` | Full body proof from the disjoint order partition, T8.0, T8.1-T8.3, and T7.3 | Classifies truth/equality, not all minimizers or exact failing values |
| `A.1` | `OMIT_FIRST_SUBMISSION` | No destination | No proof or statement imported | Full/general moment machinery excluded |
| `A.2` | `OMIT_FIRST_SUBMISSION` | No destination | No proof or statement imported | Period-eight moment trichotomy excluded |
| `A.3` | `OMIT_FIRST_SUBMISSION` | No destination | No proof or statement imported | Primitive periodic frontier through `p<=24` excluded |
| `A.4` | `OMIT_FIRST_SUBMISSION` | No destination | No proof or statement imported | Bounded-support multi-gap obstruction package excluded |
| `A.5` | `OMIT_FIRST_SUBMISSION` | No destination | No proof or statement imported | `(3,3)` multi-gap obstruction excluded |
| `A.6` | `OMIT_FIRST_SUBMISSION` | No destination | No proof or statement imported | Remaining multi-gap reduction excluded |
| `C.1` | `APPENDIX_ONLY` | `App B`, Exact exhaustion for even orders 8 through 30; cited in `S7` | Prove quotient finiteness and endpoint meaning, then state exact independent reconstruction; commands and PASS strings in `Supplement R` | Supports T8.1; not an empirical scan |
| `C.2` | `APPENDIX_ONLY` | `App B`, Exact order-32 witness; cited in `S7` | Full positive-definiteness consequence and exact matrix audit; metadata in `Supplement R` | One verified witness proves existence; enumeration is unnecessary |
| `C.3` | `APPENDIX_ONLY` | `App B`, Parity-lifted six-order closure; cited in `S7` | Full local-interlacing reduction, overlap-graph soundness/completeness, parity, cyclic and holonomy closure, and all 64 terminal decisions; reproduction data in `Supplement R` | Require `terminal_unresolved=0` |
| `C.4` | `APPENDIX_ONLY` | `App B`, Exact order-40 witness; cited in `S7` | Full exact threshold and rational LDL consequence; metadata in `Supplement R` | Separate from C.3 terminal records |
| `C.5` | `APPENDIX_ONLY` | `App B`, Ninety-six-order finite bridge; cited in `S7` | Prove coverage of every even `48<=n<240` and the matrix-inequality consequence; exact records and commands in `Supplement R` | Interval ends at 238; 240 begins the analytic proof, not the failure set |
| `C.6` | `APPENDIX_ONLY` | `App A`, Physical G6 matching audit; summarized in `S4` | Full mathematical reduction to physical zeros, exact root isolation, global chart coverage, candidate exclusions, and both unsquared matching checks; metadata in `Supplement R` | Resultants alone do not prove the G6 edge |
| `C.7` | `SUPPLEMENT_ONLY` | `Supplement X`, exact-`2r` finite audit, with reproducibility metadata in `Supplement R` | Full independent reconstruction of Floquet cuts, complement gap, constants, and endpoints | Preserve rank `2r`, codimension `2r`, and `2r x 2r` throughout |
| `C.8` | `APPENDIX_ONLY` | `App B`, Exact single-gap comparison boundary; cited in `S5` | Prove the finite/tail partition and Rayleigh consequence; retain only the exact quotient/margin summary in `App B`, with full vectors and checker metadata in `Supplement R` | Covers single gaps only |
| `C.9` | `OMIT_FIRST_SUBMISSION` | No destination | No proof, statement, orbit count, or checker discussion imported | Periodic frontier certificate excluded |

## Introduction and Dependency Discipline

Introduction theorem box 1 consists only of T8.0 and T8.4. Introduction
theorem box 2 is the **Reference and Single-Gap Spectral Hierarchy**, assembled
from the theorem-level content of T2.2, T4.0-T4.3, and T5.1-T5.2;
the claims keep the editorial classes assigned above and are not merged into
a new canonical theorem.

The proof order is not the narrative reveal order. Candidate attainment,
reference bulk, charge/sector structure, the G6 edge, patch identification,
IMS localization, the exact finite bridge, and small-order closure feed the
complete classification. Exact-`2r` is a structural refinement and is not a
dependency of the sharp onset `N_star=48`.

## Coverage Audit

The map contains exactly 46 rows: 31 `T` claims, six `A` claims, and nine
`C` claims. Every canonical accepted claim ID occurs in exactly one row.
The forced first-submission decisions are:

```text
T6.3                    SUPPORTING_THEOREM, overview only in S6
T6.4--T6.6, C.7         SUPPLEMENT_ONLY
A.1--A.6, C.9           OMIT_FIRST_SUBMISSION
```

No exact-`r`, codimension-`r`, `r x r` Feshbach, unrestricted multi-gap,
common-limit, or bounded-period-frontier statement is imported by this map.
