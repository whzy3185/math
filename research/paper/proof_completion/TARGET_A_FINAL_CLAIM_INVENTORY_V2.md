# Target A Final Claim Inventory V2

Status: `CANONICAL_CURRENT` at research checkpoint
`e6a01d8bf30088dae1042a237398bee2df138280`.

This inventory is the stable claim namespace for the JGT proof package. It
does not alter the historical meaning of the earlier claim inventory. The
canonical notation is fixed in [TARGET_A_FINAL_NOTATION.md](TARGET_A_FINAL_NOTATION.md),
the evidence attached to every accepted claim is recorded in
[TARGET_A_FINAL_CLAIM_EVIDENCE_MATRIX_V2.md](TARGET_A_FINAL_CLAIM_EVIDENCE_MATRIX_V2.md),
and the mathematical dependency order is recorded in
[TARGET_A_FINAL_PROOF_DEPENDENCY_GRAPH.md](TARGET_A_FINAL_PROOF_DEPENDENCY_GRAPH.md).

## Evidence Vocabulary

| Label | Meaning |
|---|---|
| `PURE_ANALYTIC_PROVED` | A complete human proof uses only stated algebraic, combinatorial, or operator arguments. |
| `EXACT_ALGEBRAIC_PROVED` | A complete proof uses explicit exact polynomial or rational identities; a machine audit may check arithmetic but is not the source of finiteness. |
| `COMPUTER_ASSISTED_PROVED` | A mathematical reduction to a finite exact object, an exact certificate, and an independent checker jointly prove the claim. |
| `ANALYTIC_COROLLARY_OF_CERTIFIED_INPUTS` | The deduction is human and exact; one or more named premises are computer-assisted theorems. |
| `EXACT_FINITE_READ_ONLY` | An exact bounded computation exists, but the retained producer/checker boundary is insufficient for theorem promotion. |
| `EXACT_FINITE_PRODUCER` | A deterministic exact certificate exists, but an independent checker or a mathematical bridge is absent. |
| `OPEN` | The current corpus does not prove the statement. |
| `FALSIFIED_AS_STATED` | The statement is contradicted by an accepted theorem and must not appear as current mathematics. |

`MAIN_TEXT`, `APPENDIX`, and `REPRODUCIBILITY` are editorial placements, not
evidence labels. A claim can require more than one placement when its theorem
statement belongs in the main text and its finite certificate belongs in an
appendix or reproducibility supplement.

## T1. Signed-Graph Setup

| ID | Canonical claim | Evidence | Placement |
|---|---|---|---|
| `T1.1` | Every signing of `C_n(1,2)` admits the Hamilton gauge used in this package; switching is diagonal unitary conjugacy and preserves the spectrum. | `PURE_ANALYTIC_PROVED` | `MAIN_TEXT` |
| `T1.2` | In Hamilton gauge, the step-two word `tau`, flux word `Q_i=tau_i tau_(i+1)`, and Hamilton holonomy `alpha` encode the switching class in the stated cyclic scope. | `PURE_ANALYTIC_PROVED` | `MAIN_TEXT` |
| `T1.3` | Translation, reflection, global `tau` negation, and repeated-cell zone folding give the stated unitary equivalences and preserve the squared spectral edge. | `PURE_ANALYTIC_PROVED` | `APPENDIX` |
| `T1.4` | The displayed local formula for `H=A_tau^2` has range four and is valid before any periodic or interface specialization. | `PURE_ANALYTIC_PROVED` | `MAIN_TEXT` |

## T2. Period-Eight Reference Phase

| ID | Canonical claim | Evidence | Placement |
|---|---|---|---|
| `T2.1` | For `tau=(+,+,-,+,-,-,+,-)`, the exact Bloch characteristic relation is `det(xI-A_tau(z))=P(x^2,z+z^(-1))` with the registered quartic `P`. | `COMPUTER_ASSISTED_PROVED` | `APPENDIX`, `REPRODUCIBILITY` |
| `T2.2` | The squared spectral edge of the reference phase is `eta=4+sqrt(10+2sqrt(5))<8`, attained only at Bloch parameter `z=1`. | `EXACT_ALGEBRAIC_PROVED` | `MAIN_TEXT` |
| `T2.3` | The reference flux has positive sites in one residue class modulo four; equivalently, its cyclic gaps are all equal to four. | `PURE_ANALYTIC_PROVED` | `MAIN_TEXT` |

The polynomial in `T2.1` is fixed as

```text
P(y,c)=y^4-16y^3+(80-2c)y^2+(-128+16c)y+c^2-13c+38.
```

## T3. Gap, Charge, And Sectors

| ID | Canonical claim | Evidence | Placement |
|---|---|---|---|
| `T3.1` | If the cyclic positive-`Q` gaps are `g_1,...,g_d`, then `sum_j g_j=n`; with `q_j=g_j-4`, one has `sum_j q_j=n-4d`. | `PURE_ANALYTIC_PROVED` | `MAIN_TEXT` |
| `T3.2` | An oriented charge `q=g-4` shifts the reference bulk sector by `sigma(q)=q mod 4`. | `PURE_ANALYTIC_PROVED` | `MAIN_TEXT` |
| `T3.3` | Sector shifts add modulo four under concatenation, and the resulting total shift supplies the cyclic sector-closure test used by the residue constructions. | `PURE_ANALYTIC_PROVED` | `MAIN_TEXT` |

## T4. The Elementary G6 Phase Slip

| ID | Canonical claim | Evidence | Placement |
|---|---|---|---|
| `T4.1` | `c6` is the unique root in `(7905369311620327/10^15,7905369311620328/10^15)` of the registered irreducible degree-ten polynomial. | `COMPUTER_ASSISTED_PROVED` | `MAIN_TEXT`, `APPENDIX`, `REPRODUCIBILITY` |
| `T4.2` | For either orientation of the bilateral G6 interface, `sup sigma(H_6)=c6`; candidate completeness and physical matching exclude all spectral points above `c6`. | `COMPUTER_ASSISTED_PROVED` | `MAIN_TEXT`, `APPENDIX`, `REPRODUCIBILITY` |
| `T4.3` | The exact symmetry `K^2=-I`, `KA_6=-A_6K`, `KH_6=H_6K` gives `dim ker(H_6-c6)=2`; the unsquared partners at `+/-sqrt(c6)` are simple. | `ANALYTIC_COROLLARY_OF_CERTIFIED_INPUTS` | `MAIN_TEXT`, `APPENDIX` |

## T5. Abnormal Single Gaps

| ID | Canonical claim | Evidence | Placement |
|---|---|---|---|
| `T5.1` | For every positive abnormal single gap `g!=4`, `sup sigma(H_g)>=c6`; equality holds exactly at `g=6`. | `ANALYTIC_COROLLARY_OF_CERTIFIED_INPUTS` | `MAIN_TEXT`, `APPENDIX`, `REPRODUCIBILITY` |
| `T5.2` | Uniformly for every `g notin {4,6}`, `sup sigma(H_g)>c6+1/250`. | `ANALYTIC_COROLLARY_OF_CERTIFIED_INPUTS` | `MAIN_TEXT`, `APPENDIX`, `REPRODUCIBILITY` |

The quantifier in `T5.1` and `T5.2` includes both `tau` lifts and both
orientations. It does not include arbitrary multi-gap finite cores.

## T6. Localization And Separated Phase Slips

| ID | Canonical claim | Evidence | Placement |
|---|---|---|---|
| `T6.1` | The exact discrete IMS identity holds for `H=A^2`; the cyclic tent partition has the stated range-four error bound. | `PURE_ANALYTIC_PROVED` | `MAIN_TEXT`, `APPENDIX` |
| `T6.2` | A ring made from period-eight bulk and `r in {1,2,3}` sufficiently separated G6 interfaces has only pure-bulk or one-G6 local patches and satisfies the global cap `rho(A)^2<=c6+576/R^2`. | `ANALYTIC_COROLLARY_OF_CERTIFIED_INPUTS` | `MAIN_TEXT`, `APPENDIX` |
| `T6.3` | For `r in {1,2,3}` and minimum interface distance `D>=1040`, exactly `2r` squared eigenvalues, counted with multiplicity, lie in `[c6-1/400,c6+1/400]`. | `COMPUTER_ASSISTED_PROVED` | `APPENDIX`, `REPRODUCIBILITY` |
| `T6.4` | The correct near-`c6` Feshbach space is `2r` dimensional, its complement lies below `c6-1/200`, and every cluster level satisfies `|lambda_j-c6|<3505r(9/25)^ell`. | `COMPUTER_ASSISTED_PROVED` | `APPENDIX`, `REPRODUCIBILITY` |
| `T6.5` | The exponential construction gives a sufficient continuous counterexample onset `N_exp=3120`; no optimality of this constant is asserted. | `COMPUTER_ASSISTED_PROVED` | `APPENDIX`, `REPRODUCIBILITY` |
| `T6.6` | On the standard one-G6 ring with `n=8k+2` and `alpha=+1`, the cyclic symmetry protects even squared multiplicity; for `n>=1042` the near-`c6` top is one double squared level. | `COMPUTER_ASSISTED_PROVED` | `APPENDIX` |

## T7. Residue Constructions And The Counterexample Tail

| ID | Canonical claim | Evidence | Placement |
|---|---|---|---|
| `T7.1` | The explicit one-, two-, and three-G6 gap words are legal cyclic signings in residues `2`, `4`, and `6` modulo eight, with the claimed gap sums, sector closure, holonomy choices, and separations. | `PURE_ANALYTIC_PROVED` | `MAIN_TEXT` |
| `T7.2` | For `r in {2,4,6}`, `limsup_(k->infinity) m_(8k+r)^2<=c6`; no matching lower bound or limit is claimed. | `ANALYTIC_COROLLARY_OF_CERTIFIED_INPUTS` | `MAIN_TEXT` |
| `T7.3` | Every even `n>=48` has an explicit certified counterexample: exact full-matrix certificates cover `48<=n<240`, and the IMS construction covers `n>=240`. | `COMPUTER_ASSISTED_PROVED` | `MAIN_TEXT`, `APPENDIX`, `REPRODUCIBILITY` |

The canonical representatives in `T7.1` are

```text
n=8k+2: (6,4^(2k-1)),
n=8k+4: (6,4^(k-1),6,4^(k-1)),
n=8k+6: (6,4^a,6,4^b,6,4^c),
```

where `a=floor((2k-3)/3)`, `b=floor((2k-2)/3)`, and
`c=floor((2k-1)/3)`. These formulas are used when their displayed gap
exponents are nonnegative; the finite bridge handles the remaining small
orders. In `T7.3`, `N_star=48` denotes the beginning of the contiguous
explicit-witness tail, not the first failing order.

## T8. Complete Even-Order Classification

| ID | Canonical claim | Evidence | Placement |
|---|---|---|---|
| `T8.1` | No even order `8<=n<=30` is a counterexample, while the displayed order-32 signing is an exact strict counterexample. | `COMPUTER_ASSISTED_PROVED` | `MAIN_TEXT`, `APPENDIX`, `REPRODUCIBILITY` |
| `T8.2` | No counterexample exists at `n in {34,36,38,42,44,46}`; the parity-lifted finite-state closure has 64 terminal `(Q,alpha)` records and zero unresolved records. | `COMPUTER_ASSISTED_PROVED` | `MAIN_TEXT`, `APPENDIX`, `REPRODUCIBILITY` |
| `T8.3` | The displayed order-40 signing is an exact strict counterexample. | `COMPUTER_ASSISTED_PROVED` | `MAIN_TEXT`, `APPENDIX`, `REPRODUCIBILITY` |
| `T8.4` | For every even `n>=8`, `m_n<rho_-(n)` if and only if `n=32`, `n=40`, or `n>=48`. | `COMPUTER_ASSISTED_PROVED` | `MAIN_TEXT` |

`T8.4` classifies the truth value of the inequality. It does not classify all
minimizers or compute `m_n` exactly at each failing order.

## A. Supporting Appendix Claims

| ID | Canonical claim | Evidence | Placement |
|---|---|---|---|
| `A.1` | The registered arbitrary-period formulas for the first three squared moments and their necessary `R(Q)<=8` inequalities hold for every displayed period. | `COMPUTER_ASSISTED_PROVED` | `APPENDIX`, `REPRODUCIBILITY` |
| `A.2` | Among legal period-eight phases, the target class is exactly the `R(Q)<8` class, the all-negative flux has edge `8`, and every other class has edge greater than `8`. | `COMPUTER_ASSISTED_PROVED` | `APPENDIX`, `REPRODUCIBILITY` |
| `A.3` | Up to the proved equivalences, the period-eight target is the unique primitive phase of period at most 24 with squared edge below `c6`. | `COMPUTER_ASSISTED_PROVED` | `APPENDIX`, `REPRODUCIBILITY` |
| `A.4` | Every one of the 31,008 canonical primitive multi-gap cores with support sum in `{2,6,10,14,18}` has an exact integer Rayleigh witness above `c6`. | `COMPUTER_ASSISTED_PROVED` | `APPENDIX`, `REPRODUCIBILITY` |
| `A.5` | Any finite core containing consecutive gaps `(3,3)` has squared spectral edge at least `419/53>c6`. | `COMPUTER_ASSISTED_PROVED` | `APPENDIX`, `REPRODUCIBILITY` |
| `A.6` | Any remaining primitive multi-gap competitor has support at least 22, uses gaps in `{2,3,5,6,...,44}`, and has no adjacent pair entirely in `{2,3,5}`; word length remains unbounded. | `ANALYTIC_COROLLARY_OF_CERTIFIED_INPUTS` | `APPENDIX` |

## C. Explicit Computer-Assisted Lemmas

These IDs isolate the finite exact statements that a referee may accept and
reproduce independently of the surrounding mathematical deductions.

| ID | Finite exact lemma | Evidence | Placement |
|---|---|---|---|
| `C.1` | The switching-class computation for even `8<=n<=30` is exhaustive and every endpoint decision is exact. | `COMPUTER_ASSISTED_PROVED` | `APPENDIX`, `REPRODUCIBILITY` |
| `C.2` | Exact Bareiss and rational `LDL^T` certify the displayed order-32 counterexample. | `COMPUTER_ASSISTED_PROVED` | `APPENDIX`, `REPRODUCIBILITY` |
| `C.3` | Local-window deletion plus parity-lifted de Bruijn closure exhausts `n=34,36,38,42,44,46`, including both holonomies, with `terminal_unresolved=0`. | `COMPUTER_ASSISTED_PROVED` | `APPENDIX`, `REPRODUCIBILITY` |
| `C.4` | Exact rational `LDL^T` certifies the displayed order-40 counterexample. | `COMPUTER_ASSISTED_PROVED` | `APPENDIX`, `REPRODUCIBILITY` |
| `C.5` | Ninety-six exact full-matrix `LDL^T` certificates cover every even `48<=n<240`. | `COMPUTER_ASSISTED_PROVED` | `APPENDIX`, `REPRODUCIBILITY` |
| `C.6` | Exact transfer, root isolation, Grassmann-atlas coverage, and unsquared physical matching prove the G6 global edge and its isolation data. | `COMPUTER_ASSISTED_PROVED` | `APPENDIX`, `REPRODUCIBILITY` |
| `C.7` | Exact rational Floquet and localization bounds verify the rank-`2r` cluster, complement gap, exponential constants, and endpoint `N_exp=3120`. | `COMPUTER_ASSISTED_PROVED` | `APPENDIX`, `REPRODUCIBILITY` |
| `C.8` | Exact rational witness rows prove the abnormal single-gap comparisons, including the uniform `1/250` margin. | `COMPUTER_ASSISTED_PROVED` | `APPENDIX`, `REPRODUCIBILITY` |
| `C.9` | The finite orbit and exact Rayleigh computation proves the primitive periodic frontier through period 24. | `COMPUTER_ASSISTED_PROVED` | `APPENDIX`, `REPRODUCIBILITY` |

## Results Deliberately Not Promoted

| ID | Statement | Status | Paper treatment |
|---|---|---|---|
| `O.1` | Every finite-core `B_0 -> B_2` interface has spectral edge at least `c6`. | `OPEN` | `FUTURE_WORK` |
| `O.2` | The unrestricted nonzero-residue common liminf equals `c6`, or the corresponding common limit exists. | `OPEN` | `FUTURE_WORK` |
| `O.3` | General multi-interface squared levels are simple, have nonzero universal pair interactions, or exhibit a genuine three-body term. | `OPEN` | `FUTURE_WORK` |
| `O.4` | The period-eight phase is the unique minimizer over all periods. | `OPEN` | `FUTURE_WORK` |
| `R.1` | The period-25/26 frontier recomputation and its 153 exact witnesses. | `EXACT_FINITE_READ_ONLY` | `OMIT` |
| `R.2` | The reference-relative 105/164 graph and 420/656 lift. | `EXACT_FINITE_PRODUCER` | `OMIT` |
| `X.1` | One squared G6 mode per interface; exactly `r` near-`c6` squared levels. | `FALSIFIED_AS_STATED` | `OMIT`; historical correction note only |
| `X.2` | A codimension-`r` complement and problem-specific `r x r` Feshbach model. | `FALSIFIED_AS_STATED` | `OMIT`; replace by `T6.3`-`T6.4` |
| `X.3` | The single-gap theorem implies optimality over all finite-core interfaces. | `FALSIFIED_AS_STATED` | `OMIT`; quantifier error |

## Canonical Main-Theorem Set

The main paper should promote exactly these seven theorem families:

1. `T8.4`, Complete Even-Order Classification.
2. `T2.2`, Reference-Phase Edge.
3. `T3.1`-`T3.3`, Gap/Charge and Sector Shift.
4. `T4.1`-`T4.3`, Elementary G6 Phase Slip.
5. `T5.1`-`T5.2`, Single-Gap Optimality and Uniform Separation.
6. `T6.1`-`T6.4`, Separated Phase Slips.
7. `T7.1`-`T7.3`, Residue Constructions and the Explicit Tail.

All other accepted claims support those families or belong in appendices.
