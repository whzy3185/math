# Logarithmic obstruction for growing generic complements

Date: 2026-09-09

Status: **Proved**. This note belongs only to Paper I.

This theorem upgrades the fixed-complement bound-state hierarchy to a double-scaling result. It proves one side of the defect-width phase transition and shows that the critical generic-complement scale is at least logarithmic in the half-period.

## 1. Geometry

Write

\[
L=2r,
\qquad
h=r-k,
\]

so that the long defect interval has length

\[
2h=2(r-k)
\]

and the complementary generic interval has length

\[
2k.
\]

Let

\[
s=L(2q+1)
\]

and consider the antiperiodic Bloch phase

\[
z=-1.
\]

Put

\[
\Lambda:=3+2\sqrt2,
\qquad
\Lambda^{-1}=3-2\sqrt2.
\]

## Theorem A — transfer-scale obstruction

Let `k=k(r)` be any integer sequence with

\[
1\le k<r
\]

such that

\[
\boxed{
\frac{r-k}{T_k(3)}\longrightarrow\infty.
}
\tag{1.1}
\]

Then the antiperiodic fiber has a squared eigenvalue `y_(r,k)>8` satisfying

\[
\boxed{
y_{r,k}-8
=\frac{4+o(1)}{T_k(3)^2}.}
\tag{1.2}
\]

Consequently

\[
\boxed{R^{(r-k)}_{2r,q}>8}
\tag{1.3}
\]

for all sufficiently large `r`, uniformly in the odd multiplier `2q+1`.

The theorem includes fixed `k` as a special case, but its main content is that `k` may grow with `r`.

---

## 2. Hyperbolic bulk representation

For `y>8`, put

\[
t=\frac{y-6}{2}=\cosh\eta,
\qquad
 a=e^{-\eta}=t-\sqrt{t^2-1}.
\tag{2.1}
\]

The long defect block has paired length

\[
N=r-k.
\]

Its Chebyshev coefficients are

\[
U_N(t)
=\frac{a^{-N-1}-a^{N+1}}{a^{-1}-a},
\]

\[
U_{N-1}(t)
=\frac{a^{-N}-a^N}{a^{-1}-a}.
\tag{2.2}
\]

Hence

\[
\boxed{
\frac{U_{N-1}(t)}{U_N(t)}
=a\frac{1-a^{2N}}{1-a^{2N+2}}.
}
\tag{2.3}
\]

When

\[
N(1-a)\to\infty,
\]

this ratio equals

\[
a+o(1-a)
\]

with an exponentially small relative error, and the reciprocal product of the two Chebyshev factors is exponentially small as well.

---

## 3. Infinite-bulk bound state for a generic complement of length `2k`

Let `P_k(a)` be the fixed-complement secular polynomial from `FINITE_COMPLEMENT_BOUND_STATE_HIERARCHY.md`. Its physical root closest to `1`, denoted `a_k`, satisfies

\[
\boxed{
1-a_k
=\frac{2+o(1)}{T_k(3)}
}
\tag{3.1}
\]

as `k->infinity`. The associated infinite-bulk squared energy is

\[
y_k=6+a_k+a_k^{-1}
\]

and therefore

\[
\boxed{
y_k-8
=\frac{4+o(1)}{T_k(3)^2}.}
\tag{3.2}
\]

For bounded `k`, the same argument uses the fixed positive number `1-a_k` rather than (3.1).

At the root scale (3.1),

\[
N(1-a_k)
\sim\frac{2N}{T_k(3)}.
\]

Thus the hypothesis (1.1) implies

\[
\boxed{N(1-a_k)\to\infty.}
\tag{3.3}
\]

The two interfaces of the long defect block are therefore separated by many localization lengths of the infinite-bulk bound state.

---

## 4. Finite-cell persistence of the bound state

The exact finite antiperiodic transfer determinant is obtained from the infinite-bulk secular determinant by replacing the stable multiplier `a` by the finite ratio in (2.3) and retaining one reciprocal-product term.

On the root scale `a=a_k+O(T_k(3)^{-1})`, equations (2.3) and (3.3) give

\[
\frac{U_{N-1}}{U_N}
=a+O\!\left(
(1-a)e^{-2N(1-a)}
\right),
\tag{4.1}
\]

while the reciprocal-product term is

\[
O\!\left(
(1-a)^2e^{-2N(1-a)}
\right).
\tag{4.2}
\]

The finite generic transfer has size controlled by `T_k(3)` on this neighborhood. Since

\[
N/T_k(3)\to\infty,
\]

the exponential factors in (4.1)--(4.2) dominate every polynomial factor in `T_k(3)`. Hence the finite normalized secular function converges to the fixed-complement one uniformly on a shrinking interval of width comparable to `T_k(3)^(-1)` around `a_k`, including its first derivative.

The physical zero `a_k` is simple on this scale; equivalently, the rescaled secular derivative is asymptotic to a nonzero multiple of `T_k(3)`. The implicit-root argument therefore gives a finite-cell zero

\[
\boxed{
a_{r,k}=a_k+o(T_k(3)^{-1}).}
\tag{4.3}
\]

Its squared energy is

\[
y_{r,k}=6+a_{r,k}+a_{r,k}^{-1}.
\]

Using (3.1) and (4.3),

\[
\begin{aligned}
y_{r,k}-8
&=\frac{(1-a_{r,k})^2}{a_{r,k}}\\
&=\frac{4+o(1)}{T_k(3)^2}>0.
\end{aligned}
\]

This proves Theorem A.

---

## 5. Explicit logarithmic corollary

Because

\[
T_k(3)
=\frac{\Lambda^k+\Lambda^{-k}}2
\asymp\Lambda^k,
\]

condition (1.1) holds whenever, for some fixed `epsilon>0`,

\[
\boxed{
k
\le
(1-\epsilon)
\frac{\log r}{\log\Lambda}
}
\tag{5.1}
\]

for all sufficiently large `r`.

### Corollary B — logarithmic failure regime

For every `epsilon>0`, if

\[
k(r)
\le
(1-\epsilon)
\log_{3+2\sqrt2}r,
\]

then the almost-wide two-defect phase is eventually above the threshold at `z=-1`:

\[
\boxed{R^{(r-k)}_{2r,q}>8.}
\tag{5.2}
\]

If additionally `k(r)->infinity`, the above-edge excess satisfies

\[
\boxed{
R^{(r-k)}_{2r,q}-8
\ge
\frac{4+o(1)}{T_{k(r)}(3)^2}
\asymp
16(3-2\sqrt2)^{2k(r)}.
}
\tag{5.3}
\]

The inequality uses only one explicit Bloch fiber, so it is a lower bound for the global edge.

---

## 6. What is now proved about the transition

The defect-width problem has three rigorously distinct regimes:

1. **fixed defect width `h`:** global edge is below `8`, with a Robin gap of order `L^-2`;
2. **fixed generic complement `k=r-h`:** global edge is eventually above `8`, with a persistent bound state;
3. **growing but subcritical generic complement** satisfying (5.1): the above-edge bound state still survives.

Therefore any transition back to the sub-eight regime must occur no earlier than the logarithmic scale

\[
k\sim\log_{3+2\sqrt2}r.
\]

The opposite logarithmic implication — proving sub-eight behavior when `k` lies sufficiently above this scale — remains open and is the natural next theorem.