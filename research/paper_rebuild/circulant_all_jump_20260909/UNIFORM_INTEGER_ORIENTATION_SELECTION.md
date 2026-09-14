# Uniform integer orientation selection in the macroscopic two-defect family

Date: 2026-09-14

Status: **Proved**. This unifies the fixed-ratio, balanced, and fixed-offset transition theorems.

## 1. Setup

Write

\[
L=2(N+m),
\]

with

\[
N,m\to\infty,
\qquad
0<c_0\le m/N\le c_1<\infty.
\tag{1.1}
\]

Let

\[
\Gamma_{N,m,q}
=8-\max_{|z|=1}\rho(H_{N,m,q}(z))^2.
\]

The two distinguished endpoint gaps are

\[
e^+_{N,m}=8-\rho(H(1))^2,
\qquad
e^-_{N,m}=8-\rho(H(-1))^2.
\]

The periodic well has an algebraic cusp improvement

\[
e^+_{N,m}-\Gamma_+(N)
=\frac{\pi^2}{32N^4}+O(N^{-5}),
\tag{1.2}
\]

whereas the antiperiodic well is analytic and has no algebraic phase slip.

## Theorem A — eventual exact orientation selection

There exists `N_0=N_0(c_0,c_1)` such that whenever (1.1) holds and

\[
\min\{N,m\}\ge N_0,
\]

the following dichotomy is exact.

### Periodic side

If

\[
\boxed{m\le N,}
\]

then every global maximizing Bloch phase lies in the periodic well. If `m<N`, the periodic well is separated from the antiperiodic well by order at least `N^-3`; if `m=N`, the endpoint values are algebraically degenerate but the periodic cusp wins at order `N^-4`.

Thus

\[
\boxed{
\Gamma_{N,m,q}=\Gamma_+(N),
\qquad m\le N.
}
\tag{1.3}

### Antiperiodic side

If

\[
\boxed{m>N,}
\]

then the global maximizing phase is exactly

\[
\boxed{z=-1}
\]

and

\[
\boxed{
\Gamma_{N,m,q}=e^-_{N,m}.
}
\tag{1.4}

The statement is uniform over the compatible odd multiplier.

---

## 2. Uniform endpoint splitting

By the all-orders Robin theorem, the two endpoint gaps are evaluations of the same universal decreasing function of the soft length, up to exponentially small errors. In particular, uniformly under (1.1),

\[
E(\ell)
=\frac{\pi^2}{4\ell^2}
-\frac{\sqrt2\pi^2}{4\ell^3}
+O(\ell^{-4}),
\tag{2.1}
\]

and

\[
E'(\ell)
=-\frac{\pi^2}{2\ell^3}+O(\ell^{-4}).
\tag{2.2}
\]

Hence there are constants `a,b>0` such that for all large comparable lengths,

\[
-\frac b{\ell^3}
\le E'(\ell)
\le-\frac a{\ell^3}.
\tag{2.3}
\]

If `m>N`, the mean-value theorem gives

\[
\boxed{
 e^+_{N,m}-e^-_{N,m}
 \ge c\frac{m-N}{N^3}
 +O(\Lambda^{-c'N}),
}
\tag{2.4}
\]

for an absolute positive `c` after fixing the compact ratio range. Since `m-N` is a positive integer,

\[
e^+_{N,m}-e^-_{N,m}\ge cN^{-3}
\tag{2.5}
\]

for all sufficiently large parameters.

Similarly, if `N>m`,

\[
 e^-_{N,m}-e^+_{N,m}\ge cN^{-3}.
\tag{2.6}
\]

---

## 3. Comparison with the cusp scale

The entire periodic-well phase-slip improvement is only

\[
O(N^{-4}).
\tag{3.1}
\]

Therefore a one-integer-unit imbalance already produces an endpoint advantage of order `N^-3`, one full algebraic scale larger than the cusp correction.

If `m>N`, equations (2.5) and (3.1) imply

\[
e^-_{N,m}
<\Gamma_+(N)
\]

for all large parameters. Thus the antiperiodic well wins even after allowing the best periodic phase slip.

If `N>m`, equations (2.6) and (3.1) imply

\[
\Gamma_+(N)<e^-_{N,m},
\]

so the periodic well wins.

At `N=m`, the endpoint gaps differ only exponentially, while (1.2) is algebraic and strictly positive; hence the periodic cusp wins.

---

## 4. Excluding all other phases

The full-Bloch hard/soft localization theorem shows that any phase capable of competing within `O(N^-2)` of the edge lies in a shrinking neighborhood of one of the two endpoint wells. Away from those neighborhoods there is a uniform leading-order spectral penalty.

On the periodic side, the local cusp theorem identifies the unique improving pair of phases and its gap. On the antiperiodic side, the local characteristic function is analytic, even in the displacement, and has a strictly positive quadratic gap coefficient; hence `z=-1` is a strict local maximizer of the squared edge.

Combining this local information with the endpoint comparison above proves (1.3)--(1.4).

---

## 5. Consequences

1. The physical transition is exactly located at the integer hyperplane
   \[
   \boxed{m=N.}
   \]
2. The balanced point belongs to the **periodic-cusp side** of the higher-order phase diagram.
3. The first unbalanced point `m=N+1` already belongs to the **exact antiperiodic-locking side**.
4. There is no physical algebraic crossover band wider than one lattice point.
5. Once the side is known, the full global gap inherits the corresponding all-orders local expansion.