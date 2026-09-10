# Full-Bloch macroscopic gap law for the even-separation two-defect family

Date: 2026-09-10

Status: **Proved**. This strengthens `TWO_FIBER_MACROSCOPIC_GAP_ENVELOPE.md` by proving a matching lower bound for the full Bloch problem.

## 1. Setup

Write

\[
L=2(N+m),\qquad h=2m,
\]

and consider the period-`2L` even-separation two-defect phase with arbitrary odd jump multiplier

\[
s=L(2q+1).
\]

Let

\[
R_{N,m,q}:=\max_{|z|=1}\rho(H_{N,m,q}(z))^2,
\qquad
\Gamma_{N,m,q}:=8-R_{N,m,q}.
\]

Assume

\[
N\to\infty,\qquad m\to\infty,
\qquad \frac mN\to\gamma\in(0,\infty),
\tag{1.1}
\]

while the odd multiplier `2q+1` may vary arbitrarily with `(N,m)`.

Put

\[
M:=\max\{N,m\}.
\]

## Theorem A — exact macroscopic full-Bloch gap law

Under (1.1),

\[
\boxed{
M^2\Gamma_{N,m,q}\longrightarrow\frac{\pi^2}{4}.
}
\tag{1.2}
\]

Equivalently, if

\[
\alpha:=\frac hL=\frac m{N+m}\longrightarrow\alpha_0\in(0,1),
\]

then

\[
\boxed{
L^2\Gamma_{N,m,q}
\longrightarrow
\frac{\pi^2}{\max\{\alpha_0,1-\alpha_0\}^2}.
}
\tag{1.3}
\]

The convergence is sequentially uniform in the odd multiplier.

### Corollary A.1 — balanced geometry is the unique macroscopic optimum

Among all fixed separation ratios `alpha_0 in (0,1)`, the leading constant in (1.3) is maximized uniquely at

\[
\boxed{\alpha_0=\frac12,}
\]

where

\[
\boxed{
L^2\Gamma_{N,N,q}\longrightarrow4\pi^2.
}
\tag{1.4}
\]

Thus equal defect and complementary arcs are asymptotically optimal inside the entire macroscopic even-separation two-defect family.

---

## 2. Endpoint upper bound

The periodic and antiperiodic endpoint theorems give

\[
N^2e^+_{N,m}\to\frac{\pi^2}{4},
\qquad
m^2e^-_{N,m}\to\frac{\pi^2}{4},
\tag{2.1}
\]

under (1.1), where

\[
e^+_{N,m}=8-\rho(H(1))^2,
\qquad
 e^-_{N,m}=8-\rho(H(-1))^2.
\]

Since the full Bloch edge is at least both endpoint edges,

\[
\Gamma_{N,m,q}\le\min\{e^+_{N,m},e^-_{N,m}\}.
\]

If `M=N`, use the first endpoint; if `M=m`, use the second. Hence

\[
\limsup M^2\Gamma_{N,m,q}\le\frac{\pi^2}{4}.
\tag{2.2}
\]

It remains to prove the matching liminf.

---

## 3. Near-edge roots can only live near the two soft endpoints

Choose a maximizing phase `z` and write

\[
y=8-g,
\qquad g=\Gamma_{N,m,q}.
\]

By (2.2),

\[
g=O(M^{-2}).
\tag{3.1}
\]

Use the compressed long-phase coordinate

\[
d=z^{2q+1}+z^{-(2q+1)}\in[-2,2]
\]

and the basic seam coordinate

\[
e=z+z^{-1}\in[-2,2].
\]

The block-Jacobi reduction gives the two transfer half-traces

\[
a_g=\frac{y-d-4}{2},
\qquad
 a_d=\frac{y+d-4}{2}.
\tag{3.2}
\]

### Lemma B — two-well localization

For every maximizing sequence under (1.1),

\[
\boxed{
\operatorname{dist}(d,\{-2,2\})\longrightarrow0.
}
\tag{3.3}
\]

### Proof

Suppose instead that along a subsequence

\[
-2+\delta\le d\le2-\delta
\]

for some fixed `delta>0`. By (3.1), both numbers in (3.2) then stay in a compact subinterval of `(1,infinity)`.

Let

\[
u=U_{N-1}(a_g),\qquad p=U_{m-1}(a_d).
\]

Both grow exponentially in their respective arc lengths. At `y=8`, the exact compact threshold formula contains the positive leading term

\[
\frac{(4-d^2)(20-d^2)}2\,p^2u^2,
\]

while every term not containing both large factors is exponentially smaller. Hence, uniformly on the displayed compact `d`-interval,

\[
P(8;d,e)\ge c_\delta p^2u^2
\tag{3.4}
\]

for all sufficiently large `N,m`.

The exact `4 x 4` transfer determinant before setting `y=8` shows that on the interval

\[
8-CM^{-2}\le y\le8
\]

its derivative obeys

\[
|\partial_yP(y;d,e)|
\le C_\delta'(N+m)p^2u^2.
\tag{3.5}
\]

Indeed, differentiation of a Chebyshev factor in a compact hyperbolic region costs at most a constant times its degree, and all polynomial coefficients remain bounded.

By the mean-value theorem and (3.1),

\[
P(8-g;d,e)
\ge p^2u^2\left(c_\delta-O(M^{-1})\right)>0,
\]

contradicting the root equation `P(8-g;d,e)=0`. This proves (3.3).

---

## 4. The `d -> 2` well

Suppose along a subsequence

\[
d\to2.
\]

Put

\[
\mu:=2-d\ge0.
\]

Then the generic arc is the only possible soft channel. Its transfer parameter is

\[
a_g=1+\frac{\mu-g}{2}.
\tag{4.1}
\]

The defect channel satisfies `a_d->3` and, because `m->infinity`, its transfer power is uniformly hyperbolic.

### Lemma C — Dirichlet quantization in the `d -> 2` well

Every near-edge root satisfying (3.1) and `d->2` obeys

\[
\boxed{
N^2g\ge\frac{\pi^2}{4}+o(1).
}
\tag{4.2}
\]

### Proof

First exclude the hyperbolic soft side. If `mu>=g`, then `a_g>=1`. If

\[
N^2(\mu-g)\to\infty,
\]

the generic transfer already grows super-polynomially, while the defect transfer is exponentially hyperbolic; after division by the product of their dominant factors the characteristic determinant has a strictly positive limit, so no root is possible.

If instead `N^2(mu-g)` remains bounded and nonnegative, write

\[
N^2(\mu-g)\to\kappa^2\ge0.
\]

The hyperbolic Chebyshev scaling gives

\[
\frac1N U_{N-j}(a_g)\to\frac{\sinh\kappa}{\kappa}
\]

(with value `1` at `kappa=0`). Dividing the exact `4 x 4` transfer determinant by the dominant defect-channel factor and passing to the limit gives a positive multiple of

\[
\cosh^2\kappa,
\]

again impossible. Thus the top root lies on the elliptic side for all sufficiently large indices:

\[
\mu<g.
\tag{4.3}
\]

Define `theta>0` by

\[
g-\mu=2-2\cos\theta.
\tag{4.4}
\]

Then

\[
a_g=\cos\theta,
\]

and the generic Chebyshev factors are trigonometric. The defect factors have argument tending to `3`; because `m->infinity`, their consecutive ratio tends to the stable value

\[
\Lambda^{-1},
\qquad
\Lambda=3+2\sqrt2.
\]

Substitute these forms into the exact block-transfer determinant and divide by the square of the dominant defect factor. All seam terms are exponentially negligible relative to that factor. The surviving scalar equation is

\[
\boxed{
\cos^2(N\theta)+o(1)=0.
}
\tag{4.5}
\]

uniformly for near-edge roots. The top root belongs to the first oscillatory cell, hence

\[
N\theta\longrightarrow\frac\pi2.
\tag{4.6}
\]

From (4.4),

\[
g\ge2-2\cos\theta,
\]

so

\[
N^2g
\ge
N^2(2-2\cos\theta)
\longrightarrow\frac{\pi^2}{4}.
\]

This proves (4.2).

---

## 5. The `d -> -2` well

The argument is symmetric after interchanging the generic and defect arcs. Put

\[
\nu:=d+2\ge0.
\]

Now the defect arc is soft and the generic arc is uniformly hyperbolic because `N->infinity`. The same transfer normalization gives:

### Lemma D — Dirichlet quantization in the `d -> -2` well

Every near-edge root satisfying (3.1) and `d->-2` obeys

\[
\boxed{
m^2g\ge\frac{\pi^2}{4}+o(1).
}
\tag{5.1}
\]

More precisely, after writing

\[
g-\nu=2-2\cos\vartheta,
\]

the top root lies on the elliptic side and satisfies

\[
m\vartheta\to\frac\pi2.
\tag{5.2}
\]

---

## 6. Global lower bound

By Lemma B, every maximizing sequence has a subsequence in one of the two wells.

If `d->2`, Lemma C gives

\[
M^2g
\ge\frac{M^2}{N^2}\left(\frac{\pi^2}{4}+o(1)\right)
\ge\frac{\pi^2}{4}+o(1).
\]

If `d->-2`, Lemma D gives

\[
M^2g
\ge\frac{M^2}{m^2}\left(\frac{\pi^2}{4}+o(1)\right)
\ge\frac{\pi^2}{4}+o(1).
\]

Therefore

\[
\liminf M^2\Gamma_{N,m,q}\ge\frac{\pi^2}{4}.
\tag{6.1}
\]

Together with (2.2), this proves (1.2).

Since

\[
M=(N+m)\max\left\{\frac N{N+m},\frac m{N+m}\right\}
=\frac L2\max\{1-\alpha,\alpha\},
\]

formula (1.3) follows immediately.

---

## 7. Geometric interpretation

The full Bloch edge is asymptotically a two-well problem.

- Near `d=2`, the generic arc is soft and the defect arc becomes a Dirichlet wall; the soft quantization length is `N`.
- Near `d=-2`, the defect arc is soft and the generic arc becomes a Dirichlet wall; the soft quantization length is `m`.
- The global spectral edge chooses the longer of the two soft arcs, because that produces the smaller gap.

Thus the entire macroscopic geometry is governed by

\[
\boxed{\max\{N,m\},}
\]

not by either defect separation or total period alone.

The balanced geometry `N=m` uniquely equalizes the two competing soft channels and therefore maximizes the leading full-Bloch gap constant.