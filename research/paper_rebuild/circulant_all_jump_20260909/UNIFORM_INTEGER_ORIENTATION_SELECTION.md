# Uniform integer orientation selection in the macroscopic two-defect family

Date: 2026-09-14

Status: **Proved after hostile-audit correction**.

This theorem unifies the fixed-ratio, balanced, and fixed-offset transition results.  The orientation selection is exact, while the antiperiodic-side phase location is exponentially rather than exactly locked for a general odd multiplier.

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
n=2q+1
\]

and

\[
\Gamma_{N,m,q}
=8-\max_{|z|=1}\rho(H_{N,m,q}(z))^2.
\]

The two distinguished compressed wells are

\[
d=z^n+z^{-n}\approx2
\]

and

\[
d\approx-2.
\]

The periodic well has an algebraic cusp improvement

\[
e^+_{N,m}-\Gamma_+(N)
=\frac{\pi^2}{32N^4}+O(N^{-5}),
\tag{1.2}
\]

whereas the compressed-antiperiodic well is analytic at algebraic scale and has only an exponentially small physical-seam displacement.

## Theorem A — uniform orientation selection

There exists `N_0=N_0(c_0,c_1)` such that whenever (1.1) holds and

\[
\min\{N,m\}\ge N_0,
\]

the following dichotomy holds.

### Periodic side

If

\[
\boxed{m\le N,}
\]

then every global maximizing Bloch phase lies in the periodic well.  If `m<N`, that well is separated from the competing well at order at least `N^-3`; if `m=N`, the endpoint values are algebraically degenerate but the periodic cusp wins at order `N^-4`.

Thus

\[
\boxed{
\Gamma_{N,m,q}=\Gamma_+(N),
\qquad m\le N,
}
\tag{1.3}

where `Gamma_+(N)` denotes the periodic-cusp branch.

### Compressed-antiperiodic side

If

\[
\boxed{m>N,}
\]

then every global maximizing phase lies exponentially close to

\[
\boxed{d=-2.}
\]

Among the exact physical roots `z^n=-1`, the seam coordinate is largest at

\[
\boxed{z_0=e^{\pm i\pi/n}.}
\]

Writing

\[
z=z_0e^{i\delta/n},
\]

the actual maximizing phase satisfies

\[
\boxed{
|\delta|=O(\Lambda^{-2N}),
\qquad
\Lambda=3+2\sqrt2.
}
\tag{1.4}

The global gap satisfies

\[
\boxed{
\Gamma_{N,m,q}=e^-_{N,m}+O(\Lambda^{-2N}),
}
\tag{1.5}

where `e^-_{N,m}` may be evaluated at the convenient physical fiber `z=-1`.  Hence, to every algebraic order,

\[
\boxed{
\Gamma_{N,m,q}\sim A(m),
}
\tag{1.6}

with `A` the universal endpoint Robin series.

For `n=1`, the selected compressed endpoint is literally `z=-1` and the exponentially small seam displacement vanishes by symmetry.

---

## 2. Uniform endpoint splitting

By the all-orders Robin theorem, the two endpoint gap scales are evaluations of the same universal decreasing function of the soft length, up to exponentially small errors. In particular,

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

Hence there are constants `a,b>0` such that for all sufficiently large comparable lengths,

\[
-\frac b{\ell^3}
\le E'(\ell)
\le-\frac a{\ell^3}.
\tag{2.3}
\]

If `m>N`, the mean-value theorem gives a compressed-antiperiodic well advantage

\[
\boxed{
 e^+_{N,m}-E(m)
 \ge c\frac{m-N}{N^3}
 +O(\Lambda^{-c'N}).
}
\tag{2.4}

Since `m-N` is a positive integer, this advantage is at least order `N^-3`, one full algebraic scale larger than the periodic cusp gain `O(N^-4)`.

The same comparison with roles reversed holds when `N>m`.

---

## 3. Comparison with the cusp scale

If `m>N`, the `N^-3` soft-length advantage of the compressed-antiperiodic well dominates both

- the periodic cusp gain `O(N^-4)`, and
- the physical seam correction `O(Lambda^-2N)`.

Hence that well is globally selected.

If `N>m`, the periodic well has the corresponding `N^-3` endpoint advantage and remains globally selected after its cusp improvement.

At `N=m`, the two endpoint gaps agree to every algebraic order, while the periodic cusp gain is algebraic and strictly positive, so the periodic well wins.

This proves the orientation dichotomy.

---

## 4. Excluding all other phases

The full-Bloch hard/soft localization theorem shows that any phase capable of competing within `O(N^-2)` of the edge lies in a shrinking neighborhood of one of the two compressed wells.

On the periodic side, the local cusp theorem identifies the improving phases and their all-orders expansion.

On the compressed-antiperiodic side, after division by the exponentially growing hard-channel transfer, the normalized soft root is analytic with positive quadratic coefficient in the compressed displacement.  The physical seam contributes an exponentially small linear perturbation, shifting the optimizer by only `O(Lambda^-2N)`.  This is proved in `ANTIPERIODIC_EXACT_LOCKING_AND_HIGH_ORDER_GAP.md` in its corrected form.

No third phase region can compete.

---

## 5. Consequences

1. The physical orientation transition is exactly located at the integer hyperplane
   \[
   \boxed{m=N.}
   \]
2. The balanced point belongs to the **periodic-cusp side** of the algebraic phase diagram.
3. The first unbalanced point `m=N+1` already belongs to the **compressed-antiperiodic side**.
4. There is no algebraic crossover band wider than one lattice point.
5. For `m>N`, the global phase is not generally exactly `z=-1`; instead it is exponentially close to the best physical representative of `d=-2`.
6. The full global gap nevertheless inherits the same universal Robin series `A(m)` to every algebraic order.
