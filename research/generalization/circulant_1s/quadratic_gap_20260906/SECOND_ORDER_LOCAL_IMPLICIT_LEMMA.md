# Local implicit lemma for the second-order phase boundary layer

Date: 2026-09-06.

This note isolates the quantitative step used in
`EVEN_SECOND_ORDER_PHASE_SLIP_THEOREM.md`.  The point is to avoid hiding the
`O(r^-4)` phase localization inside a qualitative implicit-function argument.

Let `s=2r`.  For an oscillatory soft root write

\[
 g-\mu=2-2\cos\theta,
 \qquad
 x=r\theta,
\]

with

\[
 \mu=2-h,
 \qquad h\in[0,2].
\]

Let `e_r` and `x_r^0` be the phase-zero endpoint gap and its soft coordinate.
The endpoint theorem gives

\[
 x_r^0\to\pi/2.
\]

## Lemma L1 — local inverse bound

There exist absolute constants `r0`, `delta>0` and `c0>0` such that, for
`r>=r0` and

\[
 |x-\pi/2|\le\delta,
\]

the normalized hard-divided left side of the root equation has `x`
derivative of magnitude at least `c0`.

More precisely, with

\[
 \lambda=3+2\sqrt2,
 \qquad q=\lambda^{-1},
\]

the derivative converges uniformly on shrinking neighborhoods of the first
soft root to

\[
 -(1-q^2),
\]

and `1-q^2>0`.

### Proof

At the endpoint scale the normalized left side is

\[
 \frac{2\sin(\theta/2)}{\theta}
 \left[
 \cos\frac{(2r+1)\theta}{2}
 -q^2\cos\frac{(2r-1)\theta}{2}
 \right]
\]

plus an error that is uniform `O(r^-2)+O(e^{-cr})`.  In the coordinate
`x=r theta`, differentiation therefore converges uniformly to

\[
 -(1-q^2)\sin x.
\]

At `x=pi/2` this is `-(1-q^2)`, so a fixed neighborhood gives the stated
lower derivative bound for all large `r`.

## Lemma L2 — endpoint subtraction estimate

Suppose a global edge lies in the oscillatory regime and write its variables
as `(g_r,mu_r,x_r)`.  For all large `r`,

\[
 |x_r-x_r^0|
 \le C\left(
 \sqrt{\mu_r}+|g_r-e_r|+\mu_r+e^{-cr}
 \right).
\tag{L2}
\]

### Proof

Subtract the exact hard-divided root equation at `(g_r,mu_r,x_r)` from the
endpoint equation at `(e_r,0,x_r^0)`.

1. By Lemma L1, the `x` change costs at least `c0 |x_r-x_r^0|`.
2. The hard ratios `beta=B_(r-1)/B_r` and `gamma=B_(r-2)/B_r` are smooth
   functions of the hard-channel argument near `6`; hence their difference
   is `O(|g_r-e_r|+mu_r)`.
3. The endpoint right side is exponentially small.
4. The phase-dependent square-root term is `O(sqrt(mu_r))`; all terms
   involving `A_(r-1)/B_r` are exponentially small in the first soft window.

Absorbing the uniform constants yields (L2).

## Lemma L3 — global optimality bootstraps to `mu=O(r^-4)`

If `g_r` is the global phase minimum, then

\[
 \boxed{\mu_r=O(r^{-4}).}
\tag{L3}
\]

### Proof

Since phase zero is admissible,

\[
 g_r\le e_r.
\]

Also

\[
 g_r-e_r
 =\mu_r+d_r(x_r)-d_r(x_r^0),
 \qquad
 d_r(x)=2-2\cos(x/r).
\]

Therefore

\[
 \mu_r
 \le d_r(x_r^0)-d_r(x_r)
 \le \frac C{r^2}|x_r-x_r^0|.
\tag{1}
\]

Moreover

\[
 |g_r-e_r|
 =e_r-g_r
 \le d_r(x_r^0)-d_r(x_r)
 \le \frac C{r^2}|x_r-x_r^0|.
\tag{2}
\]

Insert (2) into Lemma L2.  Since the leading global theorem already gives
`mu_r=o(r^-2)`, the terms multiplied by `r^-2` are absorbable, and

\[
 |x_r-x_r^0|\le C\sqrt{\mu_r}+O(e^{-cr}).
\tag{3}
\]

Combining (1) and (3), and setting `u_r=sqrt(mu_r)`, gives

\[
 u_r^2\le \frac C{r^2}u_r+O(e^{-cr}).
\]

Hence `u_r=O(r^-2)` and (L3) follows.

The same argument also gives

\[
 |x_r-x_r^0|=O(r^{-2}),
 \qquad
 |g_r-e_r|=O(r^{-4}).
\tag{4}
\]

## Lemma L4 — sharp displacement in the boundary layer

Assume

\[
 r^2\sqrt{\mu_r}\to z.
\]

On the lower soft branch,

\[
 \boxed{
 r^2(x_r-x_r^0)
 \to -\frac{z}{2\sqrt2}.}
\tag{L4}
\]

On the companion branch the sign is positive.

### Proof

By Lemma L3 and (4), the hard ratios at the two roots differ by `O(r^-4)`.
The phase square-root term divided by the hard channel is

\[
 2q\sqrt{\mu_r}+o(r^{-2}),
 \qquad q=\lambda^{-1}.
\]

Linearizing the endpoint-subtracted equation and using Lemma L1 gives

\[
 -(1-q^2)(x_r-x_r^0)
 =2q\sqrt{\mu_r}+o(r^{-2})
\]

on the lower branch.  Finally

\[
 \frac{2q}{1-q^2}
 =\frac1{2\sqrt2}.
\]

This proves (L4).

## Consequence

Lemmas L3--L4 turn the qualitative global localization

\[
 r^2(2-h_r)\to0
\]

from `EVEN_GLOBAL_PI2_THEOREM.md` into the sharp boundary-layer scale

\[
 2-h_r=O(r^{-4}),
 \qquad
 \phi_r=O(r^{-2}),
\]

and provide the exact coefficient needed for the effective parabola in
`EVEN_SECOND_ORDER_PHASE_SLIP_THEOREM.md`.

A future Lean formalization can split this note into a local inverse lemma,
a hard-ratio Lipschitz lemma, and the elementary quadratic bootstrap
`u^2 <= C u/r^2 => u=O(r^-2)`.
