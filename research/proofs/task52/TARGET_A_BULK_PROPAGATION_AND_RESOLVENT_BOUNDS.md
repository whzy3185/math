# Bulk Propagation and Resolvent Bounds

Let `M_8(y)` be the exact period-eight monodromy. On the rational G6
neighborhood from Task 50 its characteristic polynomial is reciprocal and
has four distinct positive roots

```text
z_fast, z_slow, z_slow^(-1), z_fast^(-1),
0<z_fast<=1/8<z_slow<=9/25<1.
```

Every translated bulk sector is obtained from the same recurrence by a
finite shift and gauge conjugacy. Hence it has the same multiplier bounds.

## Exponential-dichotomy lemma

On any compact rational subinterval of the Task 50 hyperbolic interval there
are invariant stable and unstable two-planes and constants `K>=1` such that

```text
||M_8(y)^L v_s|| <= K (9/25)^L ||v_s||,
||M_8(y)^(-L) v_u|| <= K (9/25)^L ||v_u||.
```

Proof: the four roots are simple and uniformly separated on the compact
interval. The exact spectral projectors are rational functions of `M_8` and
the roots, so their norms are bounded there. Diagonal propagation then gives
the stated estimates. Translation and gauge conjugacies range over a finite
set and only enlarge `K` by a fixed factor.

In exterior-square coordinates, the stable plane itself is propagated by a
one-dimensional dominant stable wedge and all mixed errors decay
exponentially. This is the basis-free propagation estimate used by the
fixed-r quasimode argument.

## Boundary maps

Whenever a selected graph chart is transverse to the stable and unstable
planes, its finite-segment DtN/Weyl matrix satisfies

```text
Lambda_L(y)=Lambda_infinity(y)+O((9/25)^L).
```

This follows by solving the stable/unstable block matching system and using
the dichotomy estimate. The statement is uniform on a compact subinterval
on which the chart determinant stays nonzero. Task 50 certifies suitable
cofactor pivots for the isolated G6 matching interval.

Task 52 does not certify one global DtN chart for every piecewise ring and
does not derive an explicit Combes-Thomas constant or a twisted
method-of-images formula. Those stronger Green-function statements remain
open and are not used to claim a spectral cap.

Status: `BULK_EXPONENTIAL_DICHOTOMY_PROVED_DTN_GLOBAL_CHART_OPEN`.
