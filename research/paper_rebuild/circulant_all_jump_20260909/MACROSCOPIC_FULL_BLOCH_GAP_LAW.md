# Full macroscopic Bloch gap law for even defect geometry

Date: 2026-09-10

Status: **Proved**. This is a headline theorem for Paper I.

This theorem upgrades the two-fiber envelope to an exact full-Bloch asymptotic and identifies the unique asymptotically optimal macroscopic defect geometry.

## 1. Setup

Write

\[
L=2(N+m),\qquad h=2m,
\qquad N,m\to\infty,
\]

and assume

\[
\boxed{
\frac hL=\frac m{N+m}\longrightarrow\alpha\in(0,1).
}
\tag{1.1}
\]

For an arbitrary sequence of odd multipliers

\[
s=L(2q+1),
\]

let

\[
R_{N,m,q}:=\max_{|z|=1}\rho(H_{N,m,q}(z))^2
\]

and define

\[
\Gamma_{N,m,q}:=8-R_{N,m,q}.
\]

## Theorem A — exact macroscopic full-Bloch gap law

Under (1.1), uniformly with respect to arbitrary variation of the odd multiplier,

\[
\boxed{
L^2\Gamma_{N,m,q}
\longrightarrow
\frac{\pi^2}{\max\{\alpha,1-\alpha\}^2}.
}
\tag{1.2}
\]

Equivalently,

\[
\Gamma_{N,m,q}
=\frac{\pi^2}{L^2\max\{\alpha,1-\alpha\}^2}
+o(L^{-2}).
\]

### Corollary A.1 — unique balanced optimum

Among macroscopic ratios `0<alpha<1`, the leading gap constant is uniquely maximized at

\[
\boxed{\alpha=\frac12,}
\]

where

\[
\boxed{
L^2\Gamma_{N,m,q}\longrightarrow4\pi^2.
}
\tag{1.3}
\]

Thus balanced defect and complementary arcs are the unique asymptotically optimal geometry inside the macroscopic even-separation two-defect family.

---

## 2. Upper bound from the two special fibers

The periodic endpoint theorem gives

\[
L^2e^+_{N,m}
\longrightarrow\frac{\pi^2}{(1-\alpha)^2},
\tag{2.1}
\]

while the antiperiodic Dirichlet theorem gives

\[
L^2e^-_{N,m}
\longrightarrow\frac{\pi^2}{\alpha^2}.
\tag{2.2}
\]

Since the full Bloch edge dominates both special-fiber edges,

\[
\Gamma_{N,m,q}\le\min\{e^+_{N,m},e^-_{N,m}\}.
\]

Therefore

\[
\limsup L^2\Gamma_{N,m,q}
\le
\frac{\pi^2}{\max\{\alpha,1-\alpha\}^2}.
\tag{2.3}
\]

It remains to prove the matching lower bound.

---

## 3. Near-edge phases must approach one of the two soft endpoints

Choose a Bloch phase attaining the global edge and write

\[
g:=\Gamma_{N,m,q}=8-\rho(H(z))^2.
\]

By (2.3),

\[
g=O(L^{-2}).
\tag{3.1}
\]

Let

\[
d=z^{2q+1}+z^{-(2q+1)}\in[-2,2]
\]

be the compressed long-phase coordinate.

We claim that every convergent subsequence of maximizing phases satisfies

\[
\boxed{d\to2\quad\text{or}\quad d\to-2.}
\tag{3.2}
\]

Indeed, suppose instead that along a subsequence

\[
d\in[-2+\delta,2-\delta]
\]

for some fixed `delta>0`. In the block-transfer normal form the two scalar-square transfer arguments at `y=8-g` are

\[
\frac{y-d-4}{2}
=\frac{4-d-g}{2},
\]

and

\[
\frac{y+d-4}{2}
=\frac{4+d-g}{2}.
\]

By (3.1), both remain uniformly larger than `1` on such a compact interior phase interval. Since `N,m` are both proportional to `L`, both Chebyshev transfer factors grow exponentially.

Divide the exact `4 x 4` transfer determinant by the product of the two dominant Chebyshev squares. At `g=0`, its leading coefficient is the sum of the first two terms in the compact threshold formula,

\[
\frac{(4-d^2)(20-d^2)}2p^2u^2
+2(4-d^2)XYpu,
\]

which is strictly positive on every compact subinterval of `(-2,2)`. The normalized transfer ratios depend continuously on `g`, and `g=O(L^{-2})`; hence the normalized characteristic determinant remains bounded away from zero for all sufficiently large indices. It therefore cannot vanish at the top eigenvalue. This contradiction proves (3.2).

Thus every near-edge maximizing subsequence enters one of two endpoint boundary layers.

---

## 4. Universal Dirichlet boundary-layer lemma

The same transfer calculation gives the local limiting law at either endpoint. We record it in the form needed below.

### Lemma B — soft-arc quantization

Suppose `g=O(L^-2)` along a sequence with `N,m` proportional to `L`.

1. If
   \[
   d=2-\mu\to2,
   \qquad \mu\ge0,
   \]
   then necessarily, after excluding a hyperbolic subsequence,
   \[
   0\le\mu<g
   \]
   for all sufficiently large indices. Define `theta_+` by
   \[
   g-\mu=2-2\cos\theta_+.
   \]
   Then
   \[
   \boxed{N\theta_+\to\frac\pi2.}
   \tag{4.1}
   \]

2. If
   \[
   d=-2+\nu\to-2,
   \qquad \nu\ge0,
   \]
   then necessarily
   \[
   0\le\nu<g
   \]
   eventually. Define `theta_-` by
   \[
   g-\nu=2-2\cos\theta_-.
   \]
   Then
   \[
   \boxed{m\theta_-\to\frac\pi2.}
   \tag{4.2}
   \]

The seam coordinate `e=z+z^{-1}` and the odd multiplier do not enter the leading law.

### Proof

We give the `d->2` case; the other is obtained by interchanging the generic and defect arcs.

At `d=2-mu`, the generic transfer argument is

\[
1+\frac{\mu-g}{2},
\]

while the defect transfer argument tends to `3`. The defect block therefore supplies an exponentially nondegenerate hard channel because `m` is proportional to `L`.

If

\[
\delta:=\mu-g\ge0,
\]

write, on the scale `N^2 delta`, the generic Chebyshev factor in hyperbolic form. Dividing the exact transfer determinant by the square of the dominant defect-channel factor and passing to any finite scaled limit gives

\[
32\cosh^2\sqrt D>0,
\qquad D=\lim N^2\delta\ge0.
\]

If `N^2 delta->infinity`, the same normalized hyperbolic term diverges positively. Both alternatives contradict the characteristic equation. Hence `mu<g` eventually.

Now write

\[
g-\mu=2-2\cos\theta_+,
\qquad x=N\theta_+.
\]

Because `g=O(L^-2)` and `N\asymp L`, the variable `x` stays bounded. The generic Chebyshev factors are oscillatory,

\[
U_{N-j}(\cos\theta_+)
=\frac{\sin((N-j+1)\theta_+)}{\sin\theta_+},
\]

whereas the defect-channel ratios converge exponentially to the stable ratio associated with the hard transfer root `3+2sqrt(2)`. Divide the characteristic determinant by the dominant hard-channel square. The seam terms are lower by that exponential factor and vanish. The remaining normalized equation converges to

\[
32\cos^2x=0.
\]

The top root lies in the first oscillatory cell, so `0<=x<=pi`; hence

\[
x\to\frac\pi2.
\]

This proves (4.1). The `d->-2` calculation is identical with the two arcs interchanged; it is also the local form of the exact antiperiodic calculation in `ANTIPERIODIC_DIRICHLET_GAP_LAW.md`. This proves (4.2).

---

## 5. Lower bound along each endpoint layer

Suppose first that a maximizing subsequence has `d->2`. By Lemma B,

\[
N^2(g-\mu)\to\frac{\pi^2}{4}.
\]

Since `mu>=0`,

\[
\liminf N^2g\ge\frac{\pi^2}{4}.
\]

Using

\[
\frac LN=\frac{2(N+m)}N\longrightarrow\frac2{1-\alpha},
\]

we get

\[
\liminf L^2g
\ge\frac{\pi^2}{(1-\alpha)^2}.
\tag{5.1}
\]

If instead `d->-2`, Lemma B gives

\[
\liminf m^2g\ge\frac{\pi^2}{4},
\]

and therefore

\[
\liminf L^2g
\ge\frac{\pi^2}{\alpha^2}.
\tag{5.2}
\]

Every maximizing subsequence has one of these two forms. Consequently

\[
\boxed{
\liminf L^2\Gamma_{N,m,q}
\ge
\min\left\{
\frac{\pi^2}{(1-\alpha)^2},
\frac{\pi^2}{\alpha^2}
\right\}.
}
\tag{5.3}
\]

Combining (5.3) with the upper bound (2.3) proves (1.2).

---

## 6. Balanced geometry

The limiting constant is

\[
C(\alpha)=
\frac{\pi^2}{\max\{\alpha,1-\alpha\}^2}.
\]

Since `max{alpha,1-alpha}` is uniquely minimized at `alpha=1/2`,

\[
C(\alpha)\le4\pi^2
\]

with equality only at `alpha=1/2`. This proves Corollary A.1.

## 7. Interpretation

The macroscopic family is a two-well Dirichlet problem. A near-edge Bloch phase can make only one of the two arcs soft:

- near `d=2`, the complementary bulk of pair-length `N` is soft and the defect arc is exponentially hard;
- near `d=-2`, the defect arc of pair-length `m` is soft and the complementary arc is exponentially hard.

The full Bloch gap is therefore controlled by the longer of the two physical arcs, equivalently by the smaller of the two Dirichlet energies. Balanced geometry equalizes the two competing endpoint obstructions and uniquely maximizes the leading gap.