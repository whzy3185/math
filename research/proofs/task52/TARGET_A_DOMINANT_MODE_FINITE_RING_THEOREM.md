# Dominant-Mode Finite-Ring Insurance Status

Task 51 proves the exact closure factorization

```text
P9(t;y)=(t-1)Q1(t;y)Q2(t;y),
9 -> 4+4 -> 2+2,
```

with exact Bezout projectors and reciprocal reductions. It also proves the
shifted-sign exclusion for both G6/G10 holonomies through `k=32` on
`y>=7.98`.

Task 52 did not obtain a uniform Q1/Q2 ordering, a fixed-sign dominant modal
coefficient, or a remainder bound below the dominant term. The inherited
interval starts above `c6`, so the exact prefix does not supply the missing
fixed-r global cap near `c6`. No finite-Evans/Rouche winding certificate was
implemented.

The strongest viable route remains dominant algebraic mode plus an exact
finite prefix, with finite Evans/Rouche as fallback. Repeating the rejected
positive-cosh, positive-weight, Hankel, or monomial-cone routes would not add
evidence.

Status: `INSURANCE_ROUTE_PARTIAL`.
