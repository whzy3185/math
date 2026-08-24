# Target A JGT Theorem Hierarchy

Status: `EDITORIAL_CANONICAL_CURRENT`.

This hierarchy names mathematical results rather than research stages. Claim
IDs refer to [TARGET_A_FINAL_CLAIM_INVENTORY_V2.md](TARGET_A_FINAL_CLAIM_INVENTORY_V2.md).

There are exactly seven main theorem families, Theorems 1.1--1.7. No
six-family abbreviation is canonical.

## Theorem 1.1: Complete Even-Order Classification

For every even integer `n>=8`,

```text
m_n<rho_-(n)
```

if and only if

```text
n=32, n=40, or n>=48.
```

Equivalently, the conjectured inequality holds exactly for

```text
{8,10,...,30,34,36,38,42,44,46}.
```

Here `theta_n:=rho_-(n)^2`. Failure means
`m_n<rho_-(n)`, equivalently `m_n^2<theta_n`; the theorem never compares
`m_n` directly with `theta_n`. The displayed strict-failure classification
is logically distinct from attainment. If the original conjecture is stated
as the equality `m_n=rho_-(n)`, equality at every order in the displayed
validity set additionally uses an explicit candidate with spectral radius at
most `rho_-(n)`, together with the universal lower bound. The exhaustion
inequality alone does not imply equality.

Canonical claims: `T8.0`, `T8.4`. Claim `T8.0` supplies the explicit
attaining signing; `T8.4` combines it with the exhaustive lower/strict
classification.

Role: first theorem in the introduction and final theorem proved in the body.
The early statement is followed by a roadmap; the proof is completed after
the finite and infinite pieces have been established.

## Theorem 1.2: Reference-Phase Edge

For the canonical period-eight phase,

```text
sup_(|z|=1) rho(A_ref(z))^2
=eta
=4+sqrt(10+2sqrt(5))<8,
```

and equality occurs only at `z=1`.

Canonical claims: `T2.1`, `T2.2`.

Role: establishes the unperturbed bulk and the first constant in
`eta<c6<8`.

## Theorem 1.3: Gap/Charge And Sector Shift

For positive-`Q` gaps `g_j` and charges `q_j=g_j-4`,

```text
sum_j g_j=n,
sum_j q_j=n-4d,
sigma_sec(q)=q mod 4,
sigma_sec(PQ)=sigma_sec(P)+sigma_sec(Q) mod 4.
```

Canonical claims: `T3.1`-`T3.3`.

Role: a short combinatorial theorem preparing the legal residue
constructions.

## Theorem 1.4: Elementary G6 Phase Slip

Let `c6` be the uniquely isolated root of the registered degree-ten
polynomial. For either G6 orientation,

```text
sup sigma(H_6)=c6,
dim ker(H_6-c6)=2.
```

The unsquared partners at `+/-sqrt(c6)` are simple.

Canonical claims: `T4.0`-`T4.3`. Claim `T4.0` separates the periodic
essential spectrum from the discrete matching problem.

Role: technical centerpiece. The main text gives a four-lemma proof chain;
the exact atlas and root audit are isolated in an appendix.

## Theorem 1.5: Single-Gap Optimality

For every positive abnormal gap `g!=4`, in both lifts and orientations,

```text
sup sigma(H_g)>=c6,
```

with equality if and only if `g=6`. Moreover, if `g notin {4,6}`,

```text
sup sigma(H_g)>c6+1/250.
```

Canonical claims: `T5.1`, `T5.2`.

Role: main-text variational theorem and its uniform-separation corollary. It
is explicitly limited to one abnormal gap.

## Theorem 1.6: Separated Phase Slips

For `r in {1,2,3}` separated G6 interfaces, the finite-ring spectral top is
bounded by the local G6 edge plus an explicit IMS error. Under `D>=1040`, the
fixed near-`c6` window contains exactly `2r` squared levels counted with
multiplicity, and

```text
|lambda_j-c6|<3505r(9/25)^ell.
```

The effective Feshbach space is `2r` dimensional.

Canonical claims: `T6.0`-`T6.4`. Claim `T6.0` identifies every localized
finite-ring patch with the certified line model before local spectral bounds
are applied.

Role: the IMS cap belongs in the main text; exact-`2r`, complement gap, and
Feshbach constants belong in the appendix.

## Theorem 1.7: Residue-Class Upper Constructions

The explicit one-, two-, and three-G6 words are legal in residues `2`, `4`,
and `6` modulo eight and satisfy

```text
limsup_(k->infinity) m_(8k+r)^2<=c6,
r in {2,4,6}.
```

Together with the exact finite bridge and the IMS tail, every even `n>=48`
has an explicit counterexample.

Canonical claims: `T7.1`-`T7.3`.

Role: completes the infinite construction and supplies the final large-order
input to Theorem 1.1. The theorem says `limsup`, not limit.

## Supporting Propositions

| Proposed label | Claim IDs | Placement |
|---|---|---|
| Proposition 2.1, Switching and operator equivalences | `T1.1`-`T1.4` | main text plus Appendix A |
| Proposition 4.1, G6 anticommuting symmetry | `T4.3` | main text |
| Proposition 6.1, Standard one-G6 protected double level | `T6.6` | Appendix D |
| Proposition 6.2, Exponential sufficient onset | `T6.5` | Appendix D |
| Proposition 7.1, Exact classifications through order 32 | `T8.1` | main text plus Appendix E |
| Proposition 7.2, Six-order finite-state closure | `T8.2` | main text plus Appendix E |
| Proposition 7.3, Exact order-40 witness | `T8.3` | main text plus Appendix E |

## Optional Appendix Theorems

| Proposed label | Claim IDs | Editorial decision |
|---|---|---|
| General moment identities | `A.1` | retain in Appendix F if used by the periodic frontier |
| Period-eight trichotomy | `A.2` | retain in Appendix F as structural context |
| Primitive periodic frontier through 24 | `A.3` | retain in Appendix F; state the bound prominently |
| Finite multi-gap obstruction package | `A.4`-`A.6` | Appendix G or omit for length; not needed for Theorem 1.1 |

## Computer-Assisted Lemma Placement

| Lemma family | IDs | Appendix |
|---|---|---|
| finite orders through 32 | `C.1`, `C.2` | Appendix E |
| six no-counterexample orders and order 40 | `C.3`, `C.4` | Appendix E |
| 96-order exact bridge | `C.5` | Appendix E |
| G6 physical matching completeness | `C.6` | Appendix B |
| exact-`2r` constants | `C.7` | Appendix D |
| single-gap integer witnesses | `C.8` | Appendix C |
| bounded periodic frontier | `C.9` | Appendix F |

## Claims Not In The Theorem Hierarchy

The following are not theorem statements in the final paper:

- universal multi-gap interface optimality;
- unrestricted common liminf or common limit;
- all-period periodic optimality;
- period-25/26 read-only computations;
- producer-only reference-graph consequences;
- exact `r`, codimension `r`, or an `r x r` G6 Feshbach model;
- general finite-ring simplicity or interaction-coefficient asymptotics.

The hierarchy is therefore complete without being inflated: seven main
theorem families, seven supporting propositions, and isolated exact
computer-assisted lemmas.

All manuscript reuse is additionally governed by
[TARGET_A_MANUSCRIPT_IMPORT_SAFETY.md](TARGET_A_MANUSCRIPT_IMPORT_SAFETY.md).
