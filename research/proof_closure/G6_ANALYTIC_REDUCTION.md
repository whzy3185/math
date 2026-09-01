# G6 Analytic Reduction

## What has already been reduced analytically

The period-eight bulk quartic is palindromic. With `y=lambda^2` and
`w=z+z^-1`, it becomes the quadratic

```text
w^2+a(y)w+b(y)-2=0,
a(y)=-2y^2+16y-13,
b(y)=y^4-16y^3+80y^2-128y+40.
```

This gives the stable/unstable multiplier branches explicitly. For G6, the
matching determinant is symmetric in the two stable multipliers. Eliminating
their elementary symmetric functions yields the irreducible degree-ten
polynomial

```text
p(y)=16y^10-520y^9+6913y^8-48448y^7+191768y^6-423904y^5
     +484528y^4-270464y^3+137856y^2-19968y+256.
```

The physical level is the unique root in the stated rational interval near
`7.905369...`; its exact isolation by a Sturm chain is a reasonable final
algebraic component and does not need to be replaced by decimal numerics.

## Why the scalar polynomial is not yet a complete G6 proof

The same polynomial also contains the physical gap-2 root above 8. Squaring,
elimination of the stable multiplier, cleared denominators, and cofactor
coordinates all create candidate branches. There is also a second candidate
near `7.808686...` that has no physical G6 match. Hence

```text
p(y)=0  does not imply  y is a G6 eigenvalue.
```

The remaining exact content is the basis-free condition

```text
(Lambda^2 D_6(y) U_L(y)) wedge S_R(y)=0.
```

It excludes the nonphysical candidates and, together with the norm bound,
proves the global edge. The present chart-by-chart interval verification is
therefore logically necessary in the current reduction.

## Research target

To improve this theorem, one must prove a scalar physical Evans or Weyl
function is globally defined on the relevant branch and has a fixed-sign
derivative. A valid proof would replace the candidate-resultant atlas by

```text
analytic branch selection -> scalar monotone equation -> one Sturm interval.
```

No such monotonicity is proved here. The current status is
`ANALYTIC_WITH_FINITE_BASE_CASES` for the algebraic root and `ANALYTIC_OPEN`
for the desired global scalar reduction.
