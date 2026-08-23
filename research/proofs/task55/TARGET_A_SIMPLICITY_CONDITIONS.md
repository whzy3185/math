# Simplicity Conditions for the Near-c6 Cluster

Status: abstract criteria `PROVED`; simplicity of the physical finite-ring
cluster `OPEN`.

## 1. Statement

There are three distinct notions that must not be conflated.

1. The unsquared single-G6 roots `+sqrt(c6)` and `-sqrt(c6)` are individually
   simple.
2. The squared single-interface level `c6` has multiplicity two.
3. Simplicity of the split finite-ring levels is a separate interaction
   question.

The first two facts do not imply the third. In particular, the symmetry
`KA=-AK` explains why two simple unsquared roots coalesce after squaring.

## 2. Static two-level criterion

Let

```text
M = [ a       t ]
    [ conj(t) b ]
```

be Hermitian. Its eigenvalues are

```text
(a+b)/2 +/- (1/2)sqrt((a-b)^2+4|t|^2).
```

Hence they are simple if and only if

```text
(a-b)^2+4|t|^2>0,                                    (1)
```

or equivalently, if and only if `M` is not a scalar matrix. This criterion is
exact and requires no genericity language.

A quantitative perturbative version is also immediate. If a Hermitian
matrix `M0` has simple eigenvalues with minimum gap `gamma>0`, and another
Hermitian matrix `M` satisfies

```text
||M-M0|| < gamma/2,                                  (2)
```

then the ordered Weyl intervals around the eigenvalues of `M0` are disjoint,
so every eigenvalue of `M` is simple.

## 3. Exact Feshbach root criterion

Assume a valid finite-dimensional Feshbach reduction on a real interval `I`:

```text
F(z)=det(H_eff(z)-z I_m),
QHQ-z invertible for z in I.                          (3)
```

Block determinant factorization gives

```text
det(H-z)=det(QHQ-z) F(z)                              (4)
```

up to the fixed nonzero coordinate normalization. Therefore a real
`z0 in I` is a simple eigenvalue of `H` exactly when

```text
F(z0)=0,   F'(z0) !=0.                                (5)
```

For the finite self-adjoint matrix `H`, algebraic and geometric multiplicity
agree. Condition (5), unlike a visual separation in a decimal root table, is
a certificate-ready criterion.

## 4. Evidence and current limitation

The Task 55 rank correction, two mathematical audits, and the independent
checker prove a `2r`-dimensional reduction for `r in {1,2,3}` at large
separation. That theorem gives only a common cluster window and a common norm
bound. It explicitly makes no simplicity assertion.

The representative high-precision transfer-Evans roots show splitting in
some orientation/holonomy cases and apparent multiplicity in others. Such
tables can propose intervals and derivatives, but they cannot establish (5)
without interval or exact control. A computed difference below double
precision is not a zero, while a printed repeated root is not a proof of
multiplicity.

Neither (1) nor (2) currently applies to the physical cluster because no
certified static leading matrix with a nonzero gap has been extracted.
Likewise, (5) has not been checked uniformly over all allowed separations,
orientations, and holonomies.

## 5. Dependencies

- The correct physical coordinate space has dimension `2r`, not `r`.
- The verified codimension-`2r` complementary resolvent supplies (3), but not
  the derivative or gap condition (5).
- A uniform perturbative use of (2) requires exact or interval-certified
  enclosures for every entry of a leading matrix and its remainder.
- The old exact-`r` and `r x r` Feshbach claims are rejected dependencies.

## 6. Next lemma

Produce a root-by-root Evans certificate on each finite set of phase,
orientation, and holonomy classes. It should isolate every root in the fixed
cluster window and prove either `F'(z)` has a fixed nonzero sign on that root
interval or an exact common factor forces multiplicity. The uniform analytic
version should instead prove a lower bound

```text
gap(T_lead) >=g0>0
```

and an error bound below `g0/2`. Until one of these routes closes, finite-ring
simplicity remains `OPEN`.
