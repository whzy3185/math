# Proof-reduction map

## Reading convention

This map is extracted from the local proof files on the baseline branch.  It
is a research plan, not an endorsement of their status labels.  In
particular, `exact-computer-assisted` means that the repository has a claimed
exact route; it does not establish independent reproducibility or mathematical
correctness.

## Proposed analytic spine

```text
switching and gauge
    -> flux coordinates
    -> twisted Fourier benchmark

period-eight Floquet block
    -> explicit band edge eta
    -> periodic counterexample family

gap/charge arithmetic
    -> admissible residue constructions

G6 scalar physical-edge theorem
    -> localized interface state
    -> finite-ring comparison
    -> analytic tail

small exceptional orders
    -> only the irreducible finite verification residue
```

The first two lines are the desired main-text story.  The G6 and finite-ring
lines are research targets, not assumed consequences.

## Module ledger

| Module | Local source | Current form found locally | Analytic rewrite task | Manuscript status now |
|---|---|---|---|---|
| Switching/gauge | `proof_closure/PROOF_OBLIGATION_MATRIX.md` | elementary diagonal conjugacy and cycle-space coordinates | write concise direct proof | eligible after review |
| Twisted benchmark | `proof_closure/TWISTED_SIGNING_SPECTRUM.md` | Fourier two-plane calculation | retain with direct derivation | eligible after review |
| Period-eight bulk | `proofs/TARGET_A_PERIOD8_SHARP_CONSTANT.md` | explicit quartic and positivity identity, but provenance includes audited coefficient data | derive the Floquet block and quartic by hand; retain the positive-coefficient comparison | first analytic target |
| Charge arithmetic | `proof_closure/PHASE_SLIP_AND_G6_CLOSURE.md` | endpoint-sector arithmetic | formulate as a closed word lemma with exact cyclic hypotheses | eligible after review |
| G6 local edge | `proof_closure/G6_ANALYTIC_REDUCTION.md` | degree-ten elimination plus physical-branch exclusion | produce a scalar physical Evans/Weyl function or keep a minimal exact algebraic certificate | not ready for main theorem |
| G6 localization | `proof_closure/ANALYTIC_GAP_AUDIT_CURRENT.md` | stable/unstable matching with interval multiplier bounds | derive a transparent decay estimate from the palindromic bulk relation | conditional on G6 edge |
| Residue-two family | `proof_closure/R2_BOUNDARY_RESPONSE_REDUCTION.md` | all-length bulk Riccati box; final cyclic response unresolved | prove positivity of the fixed six-by-six boundary response | priority R3 |
| Residues four/six | `proof_closure/ANALYTIC_GAP_AUDIT_CURRENT.md` | finite LDL bridge plus eventual IMS construction | prove a parameterized two-/three-interface theorem | priority R4 |
| Equality 8--30 | `proof_closure/ORDER_COVERAGE_LEDGER.md` | quotient exhaustion | seek a genuine rigidity theorem; otherwise retain as a small finite base only | finite-only |
| Equality 34--46 | `proof_closure/EQUALITY_ANALYTIC_SEARCH.md` | local-window/de Bruijn closure | replace the surviving-language table by a forbidden-pattern theorem | later target |

## First derivation target: the period-eight edge

The local record gives the candidate fiber polynomial

\[
P(y,c)=y^4-16y^3+(80-2c)y^2+(-128+16c)y+c^2-13c+38,
\]

with \(c=z+z^{-1}\in[-2,2]\), and candidate edge

\[
\eta=4+\sqrt{10+2\sqrt5}.
\]

The intended proof task is not to quote this polynomial from a JSON audit.
It is to derive the Floquet block directly from the period-eight signing,
compute its determinant, and then prove

\[
P(y,c)>0\quad\text{for }y\geq\eta,\;c\leq2,
\]

apart from \((y,c)=(\eta,2)\).  If that derivation is clean, it becomes the
first substantive analytic proposition of a new manuscript.

## Gate for an analytic-first submission

Route A (all-even classification) is available only if all of the following
are independently established:

1. direct period-eight Floquet derivation;
2. physical, globally selected G6 edge theorem;
3. all-length residue-two response theorem;
4. all-length residue-four and residue-six interface theorems;
5. a small, human-readable treatment of the remaining equality orders.

Until then the default Route B theorem is an analytic infinite
counterexample-family result, plus the smallest exact explicit
counterexamples.  It is mathematically honest, has a coherent spectral-graph
story, and does not depend on advertising the present global classification.

## Non-negotiable evidence boundary

No manuscript sentence may upgrade a computation to an analytic proof.  A
finite computation may appear only after a lemma proves its exact domain and
only with a stated verifier/reproducibility location.
