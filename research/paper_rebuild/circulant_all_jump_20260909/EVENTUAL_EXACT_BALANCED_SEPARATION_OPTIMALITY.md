# Eventual exact balanced-separation optimality at fixed period

Date: 2026-09-10

Status: **Proved**. This closes the finite-period separation optimization problem asymptotically in the period.

## 1. Fixed-period geometry

Fix an integer `r>=1` and take

\[
N+m=2r.
\]

Then

\[
L=2(N+m)=4r
\]

and the primitive coefficient period is

\[
p=2L=8r.
\]

The even defect separation is

\[
h=2m.
\]

For an arbitrary odd multiplier define

\[
\Gamma_{N,m,q}
:=8-\max_{|z|=1}\rho(H_{N,m,q}(z))^2.
\]

The exactly balanced geometry is

\[
\boxed{N=m=r,\qquad h=L/2=2r.}
\tag{1.1}
\]

## Theorem A — eventual exact discrete optimizer

There exists an absolute integer `r_0` such that for every

\[
r\ge r_0
\]

and every odd multiplier,

\[
\boxed{
\Gamma_{r,r,q}
>
\Gamma_{N,m,q}
}
\tag{1.2}
\]

for every integer pair

\[
N+m=2r,
\qquad
(N,m)\ne(r,r).
\]

Thus, for every sufficiently large primitive period `p=8r`, the balanced two-defect separation is the unique gap-maximizing even separation inside the complete reflection-chiral two-defect family.

The conclusion includes unsafe geometries automatically: if `R_{N,m,q}>8`, then `Gamma_{N,m,q}<0` and they cannot compete with the balanced sub-eight phase.

---

## 2. Balanced lower asymptotic

The balanced endpoint cubic correction gives

\[
e_r
=
\frac{\pi^2}{4r^2}
-
\frac{\pi^2}{2\sqrt2\,r^3}
+O(r^{-4}),
\tag{2.1}
\]

where `e_r` is the better of the two endpoint gaps. The balanced phase-slip theorem changes the gap only at order `r^-4`:

\[
e_r-\Gamma_{r,r,q}
=
\frac{\pi^2}{32r^4}+o(r^{-4}).
\tag{2.2}
\]

Hence

\[
\boxed{
\Gamma_{r,r,q}
=
\frac{\pi^2}{4r^2}
-
\frac{\pi^2}{2\sqrt2\,r^3}
+O(r^{-4}),
}
\tag{2.3}
\]

uniformly in the odd multiplier.

---

## 3. Endpoint upper bound for every competitor

For an arbitrary competitor put

\[
M:=\max\{N,m\}.
\]

Since `N+m=2r` and the geometry is unbalanced,

\[
\boxed{M\ge r+1.}
\tag{3.1}
\]

If `M=N`, use the periodic endpoint; if `M=m`, use the antiperiodic endpoint. In either case the full Bloch gap is bounded above by the endpoint gap belonging to the longer soft arc:

\[
\Gamma_{N,m,q}\le e_M^{\rm soft}.
\tag{3.2}
\]

We split the competitors into a macroscopic-imbalance and a near-balanced regime.

### Case 1: macroscopic imbalance

Fix a small `epsilon>0`. If

\[
M\ge(1+\epsilon)r,
\]

then the two-fiber upper bound gives

\[
\Gamma_{N,m,q}
\le
\frac{\pi^2+o(1)}{4M^2}
\le
\frac{\pi^2+o(1)}{4(1+\epsilon)^2r^2},
\]

which is strictly smaller than (2.3) for all sufficiently large `r`.

### Case 2: near balance

It remains to consider

\[
r+1\le M<(1+\epsilon)r.
\]

Then the shorter arc is at least `(1-epsilon)r`, so the ratio of the two arc lengths stays in a compact subset of `(0,infinity)`. The universal endpoint cubic theorem applies uniformly:

\[
\boxed{
e_M^{\rm soft}
=
\frac{\pi^2}{4M^2}
-
\frac{\pi^2}{2\sqrt2\,M^3}
+O(r^{-4}).
}
\tag{3.3}
\]

Define

\[
f(x)=
\frac{\pi^2}{4x^2}
-
\frac{\pi^2}{2\sqrt2\,x^3}.
\]

For all sufficiently large `x`,

\[
f'(x)<0.
\]

Thus by (3.1),

\[
e_M^{\rm soft}
\le f(r+1)+O(r^{-4}).
\tag{3.4}
\]

A direct expansion gives

\[
\boxed{
f(r)-f(r+1)
=
\frac{\pi^2}{2r^3}+O(r^{-4}).}
\tag{3.5}
\]

Combining (2.3)--(3.5),

\[
\begin{aligned}
\Gamma_{r,r,q}-\Gamma_{N,m,q}
&\ge f(r)-f(r+1)+O(r^{-4})\\
&=
\frac{\pi^2}{2r^3}+O(r^{-4})>0
\end{aligned}
\]

for all sufficiently large `r`. This proves Theorem A.

---

## Corollary B — asymptotic discrete spectral gap between the best and second-best geometries

Let

\[
\Gamma_r^{(1)}
\]

be the balanced optimum and

\[
\Gamma_r^{(2)}
\]

be the largest full-Bloch gap among all unbalanced even separations in the same period. Then

\[
\boxed{
\Gamma_r^{(1)}-\Gamma_r^{(2)}
\ge
\frac{\pi^2}{2r^3}+O(r^{-4}).
}
\tag{4.1}
\]

The nearest competitors are the one-step imbalances

\[
(N,m)=(r-1,r+1)
\]

and its arc-dual geometry, at least at the level of the endpoint upper bound. Consequently the discrete separation optimization is resolved one full algebraic order before the balanced phase-slip correction enters.

---

## Corollary C — optimal minimal 2-adic phase for large valuation

If

\[
2^k\Vert s,
\qquad k\to\infty,
\]

then the minimal compatible period is

\[
p=2^{k+1}=8r,
\qquad r=2^{k-2}.
\]

For all sufficiently large `k`, the unique optimal even separation inside this minimal reflection-chiral two-defect cell is exactly

\[
\boxed{h=2^{k-1}=p/4.}
\tag{5.1}
\]

Equivalently, the two positive flux defects are separated by one quarter of the full coefficient period.

Thus the large-valuation optimized construction is now completely discrete:

1. arithmetic fixes the minimal period `2^{k+1}`;
2. spectral optimization fixes the defect separation `2^{k-1}`;
3. the full Bloch edge then has the balanced phase-slip refinement.

## 6. Significance

This theorem upgrades balanced geometry from a macroscopic variational statement to an eventual exact finite-cell optimizer. The key scale separation is

\[
\text{one-site imbalance loss}=\Theta(r^{-3}),
\]

whereas

\[
\text{balanced Bloch phase-slip gain}=\Theta(r^{-4}).
\]

Therefore the discrete geometry locks before the continuous Bloch phase does.