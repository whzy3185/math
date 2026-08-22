# Target A Order-Nine Hidden Structure

## Exact reduction

The universal closure polynomial factors over `Q(y)` as

```text
P9(t;y)=(t-1) Q1(t;y) Q2(t;y),
```

where both `Q1,Q2` are reciprocal quartics.  `Q1` is the period-eight bulk
characteristic polynomial.  `Q2` is the nontrivial exterior-square factor.
For `Q=t^4+a t^3+b t^2+a t+1`, substitution `x=t+t^-1` gives exactly
`x^2+a x+b-2`; the two resulting discriminants are stored in
`recurrence_exact_structure.json`.

For `g_k=f_(k+1)-f_k`, exact polynomial Bezout coefficients `A,B` satisfy
`A Q1+B Q2=1`.  Hence

```text
u=B(E)Q2(E)g,  v=A(E)Q1(E)g,
g=u+v,  Q1(E)u=0,  Q2(E)v=0.
```

This proves the requested `9 -> 4+4 -> 2+2` reduction for G6/G10 and both
holonomies.  Four direct nine-term prefixes and 20 exact recurrence checks per
sequence validate the implementation independently of floating fitting.

## Sign and modal tests

At `beta=7.98,7.99,7.995,7.999`, all 36 direct initial closure polynomials and
all recurrence-extended polynomials through `k=32` have one strict coefficient
sign after `y=beta+u`.  Thus real roots in `[beta,infinity)` are excluded
exactly for this finite prefix.  The recurrence coefficients retain strict
alternating signs.  One raw quartic projection has mixed shifted coefficients,
so coefficient positivity does not descend naively to both four-dimensional
components.

Numerical modal decompositions on `[7.98,16]` show a separated positive dominant
root and a nonzero dominant coefficient.  Reciprocal coefficient pairs are not
equal, so a pure sum of positive cosh terms is unavailable.  Every tested
closure Hankel sequence has a negative leading minor by depth four.

## Route classification

| Route | Status | Reason |
|---|---|---|
| Exact factorization | STRONG | Exact `1+4+4` identity |
| `9 -> 4+4` projection | STRONG | Exact Bezout projector |
| Reciprocal `4 -> 2` | STRONG | Exact lift identity |
| Chebyshev/cosh | WEAK | Reciprocal coefficients are unequal |
| Shifted coefficient signs | STRONG_FINITE | Exact through `k=32`, not all `k` |
| Exact modal formula | PROMISING | Algebraic roots available; interval coefficients pending |
| Dominant-mode tail | PROMISING | Uniform remainder inequality not yet certified |
| Dominant tail + prefix | STRONGEST_OPEN_ROUTE | Exact prefix already available |
| Polyhedral cone | WEAK | Projected mixed signs; no rational invariant cone |
| Generating-function positivity | FALSIFIED | Modal/Hankel signs preclude positive weights |
| Closure Hankel | FALSIFIED | 24/24 diagnostics fail positivity |
| Symplectic/exterior trace | STRONG_REDUCTION | Explains `Q2`, not yet an inequality |

Final classification: `DOMINANT_MODE_PLUS_EXACT_PREFIX_PROMISING`.
