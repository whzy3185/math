# Primitive Multi-Gap Cores Through Support Sum 18

## Theorem

Let

```text
g=(g_1,...,g_m),  g_i in Z_{>0},  m>=2,
S=sum_i g_i in {2,6,10,14,18}.
```

Put the first defect at `x_0=0` and set

```text
x_j=g_1+...+g_j,  1<=j<=m.
```

Two words are identified by reflection, with canonical representative
`min(g,reversed(g))` in integer-tuple lexicographic order.  Call `g`
primitive when no nonempty contiguous subword has zero charge:

```text
sum_{k=i}^j (g_k-4) != 0.
```

There are exactly 31,008 canonical primitive words in this class.  For every
one of them, the associated bilateral open-interface signed adjacency operator
`A_g` satisfies

```text
sup sigma(A_g^2) > c_6.
```

This is a finite, computer-assisted theorem.  It is not a classification of
primitive cores of arbitrary support.

## Open-Interface Convention

The defect set is

```text
D=(-4 Z_{>=0}) union {x_0,...,x_m} union (S+4 Z_{>=0}).
```

Define `Q_i=+1` for `i in D` and `Q_i=-1` otherwise.  Fix `tau_0=1` and
extend by

```text
tau_(i+1)=Q_i tau_i.
```

In the tree gauge used throughout Target A,

```text
(A_g v)_k = v_(k-1)+v_(k+1)
            +tau_(k-2)v_(k-2)+tau_k v_(k+2).                 (1)
```

The anchor only selects one of the two lifts.  For
`(Du)_i=(-1)^i u_i`, direct substitution gives
`A_(-tau)=-D A_tau D`, and hence the two lifts have unitarily equivalent
squared operators.  No spectral conclusion depends on choosing `tau_0=1`.

For each word the certificate vector has support

```text
I_g=[-2,S+2] intersect Z.
```

Equation (1) is evaluated on the full image window

```text
J_g=[-4,S+4] intersect Z.
```

This point is essential: the certified numerator is `||A_g v||^2`, not the
smaller and generally incorrect quantity `||(P_I A_g P_I)v||^2`.

## Complete Enumeration

A positive composition of `S` is uniquely encoded by a subset of the `S-1`
possible separator positions.  The producer iterates all separator masks,
then applies only the three stated predicates: `m>=2`, reflection
canonicality, and absence of a zero-charge contiguous subword.  The checker
independently generates positive compositions by recursion and applies the
same mathematical predicates through prefix-charge differences.  Both obtain:

| `S` | canonical primitive words |
|---:|---:|
| 2 | 1 |
| 6 | 16 |
| 10 | 186 |
| 14 | 2,275 |
| 18 | 28,530 |
| **Total** | **31,008** |

The words are sorted by `(S,g)`.  The SHA-256 digest of the compact, one-word
per line projection is

```text
1c635aa6c50d8dc2387508cf7ce63f67e6a2ced490a3ca6b4eacbe8b8c912bfb.
```

Because every listed `S` is `2 mod 4`, the whole word cannot have zero charge.
Thus the stated primitive condition agrees here with the equivalent wording
"no proper nonempty zero-charge contiguous subword."

## Exact Rayleigh Certificates

For each `g`, let `C_g:R^{I_g}->R^{J_g}` be the integer matrix defined by
(1).  A numerical highest eigenvector of `C_g^T C_g` is used only to propose
an integer vector:

```text
v = primitive_sign_normalized(round(20 u)).
```

The highest branch is first located in FP64.  Rayleigh-quotient iteration at
80 and 120 decimal digits must give the same rounded primitive vector.  Any
disagreement aborts production.

Acceptance is then entirely exact.  Python integer arithmetic reconstructs
all coordinates of `A_g v` on `J_g` and computes

```text
N_g=||A_g v||^2,  D_g=||v||^2.
```

The record is accepted only if

```text
N_g * 10^15 > 7905369311620328 * D_g.                       (2)
```

Task 51 isolates `c_6` as the unique root in

```text
(7905369311620327/10^15, 7905369311620328/10^15)
```

of

```text
16y^10-520y^9+6913y^8-48448y^7+191768y^6-423904y^5
+484528y^4-270464y^3+137856y^2-19968y+256.
```

The Lane D checker binds the Task 51 certificate by SHA-256 and independently
rebuilds the Sturm chain, obtaining exactly one root in that rational
interval.  Hence (2) gives

```text
<v,A_g^2 v>/<v,v> = N_g/D_g > c_6.
```

The variational principle proves the theorem.

## Extremal Audit Data

Across all records:

```text
max |v_i| = 11,
max N_g   = 6226,
max D_g   = 442.
```

The unique weakest certificate is

```text
g=(3,3),
v=(3,0,5,7,6,9,7,8,6,2,4),
N_g/D_g=2930/369.
```

The exact certificate stream is compact ASCII JSONL with terminal LF.  Its
SHA-256 digest is

```text
9c8ef135fc11ca7b8c1761c3d45fb89c65790d97c12f2081787814f046c038bf.
```

The independent checker rejects missing, duplicate, or reordered rows;
noncanonical words or vectors; malformed JSON scalars; any convention or hash
change; and every failure of (2).

## Boundary

The following statements are deliberately not inferred:

- a universal `B0 -> B2` theorem for all primitive multi-gap cores;
- a lower bound for motif-free words with `S>18`;
- spectral invariance under insertion or removal of a reference cell.

The last mechanism is rejected: inserting a reference cell multiplies the
matching relation by a non-scalar bulk monodromy, so it is not a spectral
equivalence.  The arbitrary-length subclass containing `(3,3)` is handled by
the separate local lemma, not by reference-cell deletion.
