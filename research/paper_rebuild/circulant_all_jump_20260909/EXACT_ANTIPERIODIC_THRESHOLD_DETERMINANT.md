# Exact antiperiodic threshold determinant for growing defect width

Date: 2026-09-09

Status: **Proved**. This note belongs only to Paper I.

This theorem sharpens the logarithmic wide-defect obstruction. In the geometry

\[
L=2r,
\qquad h=r-k,
\]

the sign of the antiperiodic characteristic determinant at the squared edge `8` is given by one closed formula involving `T_k(3)`.

## 1. Setup

The two positive local flux defects are placed at positions `0` and `2h`, so the defect interval has length

\[
2h=2(r-k)
\]

and the generic complement has length

\[
2k.
\]

Let

\[
s=L(2q+1),
\qquad q\ge0,
\]

and take the antiperiodic Bloch phase

\[
z=-1.
\]

The fiber is independent of the odd multiplier up to unitary equivalence.

Put

\[
N:=r-k.
\]

## Theorem A — exact threshold determinant

For every integer `r>k>=1`,

\[
\boxed{
\det\!\left(\sqrt8\,I-H^{(r-k)}_{2r,q}(-1)\right)
=4T_k(3)^2-16(r-k)^2.
}
\tag{1.1}
\]

Equivalently, in the squared characteristic polynomial,

\[
\boxed{
P_{r,k,-1}(8)
=4T_k(3)^2-16N^2.
}
\tag{1.2}
\]

Since `T_k(3)` is odd for every `k`, equality cannot occur for integer `N`.

---

## 2. Transfer derivation

At `z=-1`, choose `eta=i`. In the folded Pauli gauge, the long defect block has paired transfer coefficient

\[
A_d=\lambda\sigma_z+2i\sigma_x,
\]

while the generic block has

\[
A_g=\lambda\sigma_z.
\]

At the squared threshold

\[
y=\lambda^2=8,
\]

we have

\[
A_d^2=4I,
\qquad
A_g^2=8I.
\]

The defect block contains `2N` sites. Its matrix continuants are therefore evaluated at the parabolic Chebyshev point

\[
\frac{y-6}{2}=1.
\]

Thus

\[
U_N(1)=N+1,
\qquad
U_{N-1}(1)=N.
\tag{2.1}
\]

The generic complement contains `2k` sites. Pairing them gives an `SL_2` transfer with half-trace

\[
\frac{y-2}{2}=3.
\]

Hence its two channel traces are expressed by

\[
T_k(3)
\]

and the corresponding `U`-polynomials.

Substituting these two fixed transfer blocks into the `4 x 4` antiperiodic closing determinant and using the standard identity

\[
T_k(x)^2-(x^2-1)U_{k-1}(x)^2=1
\]

collapses all mixed terms. The result is

\[
P_{r,k,-1}(8)
=4T_k(3)^2-16N^2,
\]

which is (1.2).

This identity can also be obtained by specializing the exact long-defect/fixed-complement determinant in `FINITE_COMPLEMENT_BOUND_STATE_HIERARCHY.md` to the parabolic point `y=8`.

---

## 3. Exact finite obstruction

### Corollary B

If

\[
\boxed{2(r-k)>T_k(3),}
\tag{3.1}
\]

then the antiperiodic fiber has a squared eigenvalue strictly above `8`. Consequently

\[
\boxed{R^{(r-k)}_{2r,q}>8.}
\tag{3.2}
\]

### Proof

Condition (3.1) makes (1.2) strictly negative. The squared characteristic polynomial is monic and therefore tends to `+infinity` as `y->infinity`. Since the fiber is Hermitian, its squared roots are real and nonnegative. A negative value at `y=8` forces at least one root in `(8,infinity)`.

---

## 4. Exact logarithmic scale

The obstruction condition is

\[
2N>T_k(3),
\qquad N=r-k.
\tag{4.1}
\]

Using

\[
T_k(3)
=\frac{(3+2\sqrt2)^k+(3-2\sqrt2)^k}{2},
\]

we obtain the asymptotic threshold

\[
\boxed{
(3+2\sqrt2)^k
<4(r-k)(1+o(1)).
}
\tag{4.2}
\]

Equivalently,

\[
\boxed{
k
<\log_{3+2\sqrt2}(4r)+O(1).}
\tag{4.3}
\]

Thus the logarithmic scale suggested by the bound-state asymptotics is already visible in an exact finite threshold determinant.

## 5. Examples

The first values are

\[
T_1(3)=3,
\quad
T_2(3)=17,
\quad
T_3(3)=99,
\quad
T_4(3)=577.
\]

Therefore:

- `k=1`: every `N>=2` is obstructed;
- `k=2`: every `N>=9` is obstructed;
- `k=3`: every `N>=50` is obstructed;
- `k=4`: every `N>=289` is obstructed.

These thresholds explain the long preasymptotic sub-eight windows observed numerically for larger fixed complements.

## 6. Remaining converse problem

The formula (1.2) proves the above-edge side exactly. The natural converse is:

> if `2(r-k)<T_k(3)`, is the antiperiodic fiber entirely below `8`?

Numerical evidence supports this converse, which would turn (3.1) into an exact `if and only if` antiperiodic phase-transition theorem. It is not asserted here until the inertia of `8I-H(-1)^2` is fully controlled.