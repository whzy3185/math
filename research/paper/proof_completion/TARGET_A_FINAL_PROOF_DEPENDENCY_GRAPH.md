# Target A Final Proof Dependency Graph

Status: `CANONICAL_CURRENT`.

This is a mathematical dependency DAG. Research chronology, task numbers,
commit hashes, script names, and certificate paths are intentionally absent.
They belong to the evidence matrix, not to theorem logic.

An arrow

```text
X -> Y
```

means that claim `Y` uses claim `X`. Nodes `C.x` are explicit finite exact
lemmas whose mathematical premises and machine-verification boundaries must
be stated in the computer-assisted appendix.

## Layer 0: Elementary Definitions And Identities

```text
T1.1  switching invariance and Hamilton gauge
T1.2  flux/holonomy parametrization
T1.3  periodic operator equivalences
T1.4  local range-four formula for A^2
```

Edges:

```text
T1.1 -> T1.2
T1.1 -> T1.3
T1.2 -> T1.3
T1.2 -> T1.4
```

These are analytic leaves. They require no numerical premise.

## Layer 1: Reference Phase And Coordinates

```text
T1.2, T1.3 -> T2.1  exact period-eight Bloch polynomial
T2.1          -> T2.2  exact edge eta and unique Bloch maximizer
T1.2          -> T2.3  reference gap equals four

T1.2, T2.3 -> T3.1  cyclic gap and charge sums
T2.3, T3.1 -> T3.2  sector shift sigma_sec(q)=q mod 4
T3.2        -> T3.3  additive sector composition and closure
```

`T2.1` is an explicit computer-assisted algebraic lemma. `T2.2` is an exact
algebraic consequence of that polynomial. `T2.3` and `T3.1`-`T3.3` are
elementary combinatorial facts.

## Layer 2: Elementary G6 Interface

```text
T1.4, T2.2          -> T4.1  algebraic root c6 and isolation
T2.2, T4.1, C.6    -> T4.2  global G6 squared edge
T4.2, C.6           -> T4.3  rank-two G6 eigenspace
```

The explicit finite lemma is

```text
T2.1, T4.1 -> C.6
```

where `C.6` includes bulk hyperbolicity, a complete Grassmann chart cover,
resultant/Sturm candidate completeness, and unsquared physical matching.
Resultant roots alone are not enough: the edge `C.6 -> T4.2` is valid only
because the physical matching exclusions are included in `C.6`.

## Layer 3: Single-Gap Optimality

```text
T1.3, T4.2, C.8 -> T5.1  complete abnormal single-gap hierarchy
T4.1, T5.1, C.8 -> T5.2  uniform separation by 1/250
```

The finite lemma is

```text
T1.4, T4.1 -> C.8
```

and consists of exact integer Rayleigh identities for the six exceptional
small gaps, one fixed tail witness, and exact cross-multiplication against
the rational upper endpoint for `c6`.

There is no edge from `T5.1` or `T5.2` to the universal finite-core interface
claim `O.1`.

## Layer 4: Localization And Separated Interfaces

```text
T1.4                         -> T6.1  exact discrete IMS lemma
T1.3, T2.2, T4.2, T6.1      -> T6.2  patch classification and global cap
T4.2, T4.3, T6.1, C.7       -> T6.3  exact 2r cluster
T6.3, C.7                    -> T6.4  2r Feshbach and 3505r bound
T2.2, T6.4, T7.1, C.7       -> T6.5  N_exp=3120
T4.3, T6.3                   -> T6.6  protected one-G6 double level
```

The finite exact node `C.7` depends on the already established one-interface
facts:

```text
T4.2, T4.3 -> C.7.
```

It verifies all eight Floquet cuts, the rational decay and conditioning
bounds, complement-gap constants, and threshold endpoint inequalities. The
analytic arrows from `C.7` to `T6.3`-`T6.5` pass through Gram control,
min-max, and Schur-complement arguments.

## Layer 5: Residue Constructions And Infinite Tail

```text
T1.2, T3.3             -> T7.1  legal one/two/three-G6 residue words
T6.2, T7.1             -> T7.2  nonzero-residue limsup upper bounds
T2.2, T4.2, T6.1,
T6.2, T7.1, C.5        -> T7.3  explicit failure for every even n>=48
```

The finite bridge is

```text
T1.2, T7.1 -> C.5,
```

which consists of 96 exact full-matrix positive-definiteness certificates for
the disjoint interval `48<=n<240`. The infinite part of `T7.3` is analytic
once the local bulk and G6 spectral caps are accepted.

There is an arrow `T6.2 -> T7.2`, but no reverse arrow and no arrow from
`T7.2` to an unrestricted liminf or limit.

## Layer 6: Finite Classification

```text
T1.1, T1.2 -> C.1  exhaustive exact decisions for 8<=n<=30
T1.2        -> C.2  exact order-32 witness
T1.2, T1.4 -> C.3  six-order finite-state closure
T1.2        -> C.4  exact order-40 witness

C.1, C.2 -> T8.1
C.3      -> T8.2
C.4      -> T8.3
```

The central finite-state implication is

```text
local interlacing lemma
-> exhaustive surviving-window graph
-> parity and cyclic closure
-> canonical (Q,alpha) terminals
-> exact terminal decisions
-> terminal_unresolved=0
-> T8.2.
```

Each arrow is mathematical. The checker verifies the finite objects at the
middle four steps; the variational and completeness implications are stated
outside the program.

## Layer 7: Main Classification

```text
T8.1, T8.2, T8.3, T7.3 -> T8.4.
```

Expanded by disjoint regions:

```text
C.1                    -> no failure for even 8<=n<=30
C.2                    -> failure at n=32
C.3                    -> no failure at n=34,36,38,42,44,46
C.4                    -> failure at n=40
C.5                    -> failure for every even 48<=n<240
T2.2,T4.2,T6.1,T6.2   -> failure for every even n>=240
```

These regions are pairwise disjoint and exhaust every even `n>=8`.
Therefore

```text
m_n<rho_-(n)
iff n=32, n=40, or n is even and n>=48.
```

No optimizer-classification node occurs in this chain.

## Supporting Appendix DAG

```text
T1.4              -> A.1  general moment identities
T1.3,T2.2,A.1     -> A.2  period-eight trichotomy
T1.3,T4.1,A.1,C.9 -> A.3  primitive periodic frontier through p=24
T1.4,T4.1         -> A.4  support-at-most-18 multi-gap exclusions
T1.4,T4.1         -> A.5  arbitrary-length (3,3) obstruction
T5.1,A.4,A.5      -> A.6  remaining finite-alphabet necessary condition
```

`C.9` is the complete finite orbit and exact-witness certificate for the
bounded periodic frontier. `A.3` has no outgoing edge to an all-period
theorem.

## Main-Theorem Closure Table

| Final theorem family | Analytic leaves | Explicit computer-assisted leaves |
|---|---|---|
| Reference-Phase Edge | `T1.1`-`T1.3` | `T2.1` |
| Gap/Charge and Sector Shift | `T1.2`, `T2.3` | none |
| Elementary G6 Phase Slip | `T1.4`, `T2.2` | `T4.1`, `C.6` |
| Single-Gap Optimality | `T1.3`, variational principle | `T4.2`, `C.8` |
| Separated Phase Slips | `T6.1`, min-max, Schur complement | `T4.2`, `T4.3`, `C.7` |
| Residue-Class Upper/Tail | `T3.3`, `T6.1`, patch classification | `T4.2`, `C.5` |
| Complete Even-Order Classification | exhaustive set partition | `C.1`-`C.5` plus certified inputs to the analytic tail |

## Forbidden Edges

The following arrows do not exist:

```text
T4.3 -/-> exact r
T5.1 -/-> universal multi-gap optimality
T7.2 -/-> common liminf or common limit
A.3  -/-> all-period classification
R.1  -/-> theorem through period 26
R.2  -/-> spectral coercivity
```

The first prohibited arrow is stronger: `T4.3` falsifies one squared mode
per interface and forces the corrected `2r` chain `T6.3`-`T6.4`.
