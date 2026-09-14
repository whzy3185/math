# Discrete one-lattice-step transition across balanced defect geometry

Date: 2026-09-14

Status: **Proved after hostile-audit correction**.

The orientation transition remains exactly one lattice step wide.  The correction is that the positive side is locked to the **compressed antiperiodic well** up to an exponentially small physical-seam shift, not necessarily to the literal phase `z=-1` when the odd multiplier exceeds one.

## 1. Setup

Write

\[
L=2(N+m),\qquad h=2m,
\]

and fix

\[
j:=m-N\in\mathbb Z.
\]

Let

\[
N\to\infty,
\qquad m=N+j.
\]

For an odd multiplier `n=2q+1`, let

\[
\Gamma_{N,N+j,q}
=8-\max_{|z|=1}\rho(H_{N,N+j,q}(z))^2.
\]

The periodic optimized well has

\[
\Gamma_+(N)
=\frac{\pi^2}{4N^2}
-\frac{\sqrt2\pi^2}{4N^3}
+\frac{\pi^2(66-\pi^2)}{192N^4}
+O(N^{-5}).
\tag{1.1}
\]

The compressed-antiperiodic well has, to every algebraic order, the universal endpoint series evaluated at `m=N+j`:

\[
A(N+j)
=\frac{\pi^2}{4(N+j)^2}
-\frac{\sqrt2\pi^2}{4(N+j)^3}
+\frac{\pi^2(72-\pi^2)}{192(N+j)^4}
+O_j(N^{-5}).
\tag{1.2}
\]

Its actual physical optimizer differs from the exact `d=-2` set only by an exponentially small compressed displacement.

---

## Theorem A — exact side selection for every fixed integer offset

For every fixed integer `j`, the following holds for all sufficiently large `N`.

### (i) Negative side: `j<=-1`

If

\[
m=N+j<N,
\]

then the periodic well is globally selected and

\[
\boxed{
\Gamma_{N,N+j,q}=\Gamma_+(N).
}
\tag{2.1}

### (ii) Balanced point: `j=0`

If

\[
m=N,
\]

then the two endpoint gaps agree to every algebraic order, but the periodic cusp lowers the true global gap by

\[
\frac{\pi^2}{32N^4}+O(N^{-5}).
\]

Hence

\[
\boxed{
\Gamma_{N,N,q}=\Gamma_+(N).
}
\tag{2.2}

### (iii) Positive side: `j>=1`

If

\[
m=N+j>N,
\]

then the compressed-antiperiodic well is globally selected.  If `z_*` is a maximizing phase and `z_0^n=-1` is the nearest compressed-antiperiodic root, write

\[
z_*=z_0e^{i\delta/n}.
\]

Then

\[
\boxed{
|\delta|=O(\Lambda^{-2N}),
\qquad\Lambda=3+2\sqrt2.
}
\tag{2.3}

Moreover

\[
\boxed{
\Gamma_{N,N+j,q}
=A(N+j)+O(\Lambda^{-2N}).
}
\tag{2.4}

Among the exact roots `z_0^n=-1`, the physical seam coordinate is largest at

\[
z_0=e^{\pm i\pi/n}.
\]

Thus the one-lattice-step transition is exact at algebraic scale; only the finite physical phase within the positive-side well is shifted exponentially.

---

## 2. Algebraic splitting of the two wells

Expanding (1.2) in powers of `N^-1` gives

\[
\boxed{
\Gamma_+(N)-A(N+j)
=
\frac{\pi^2j}{2N^3}
-
\frac{\pi^2(24j^2+24\sqrt2\,j+1)}{32N^4}
+O_j(N^{-5}).
}
\tag{3.1}

If `j>=1`, the leading term is positive, so the compressed-antiperiodic well has the smaller gap and hence the larger spectral edge by order `N^-3`.  The exponential physical-seam correction cannot change that algebraic sign.

If `j<=-1`, the periodic well wins by order `N^-3`.

At `j=0`,

\[
\Gamma_+(N)-A(N)
=-\frac{\pi^2}{32N^4}+O(N^{-5}),
\]

which is the periodic cusp gain.

---

## 3. No physical continuous crossover window

Formally interpolate `m=N+delta` with real `delta=o(1)`. Then

\[
\Gamma_+(N)-A(N+\delta)
=
\frac{\pi^2\delta}{2N^3}
-
\frac{\pi^2}{32N^4}
+o(N^{-4}).
\]

The formal equality occurs at

\[
\delta_c(N)\sim\frac1{16N}.
\]

But `delta=m-N` is integral in the graph problem, so the only lattice point in this shrinking window is `delta=0`.  Hence the physical orientation changes directly from

\[
\boxed{j=0\quad\text{to}\quad j=1.}
\]

The seam-induced positive-side displacement is exponentially smaller still and does not create an additional algebraic crossover scale.

## 4. Structural picture

- `m<N`: periodic avoided crossing and algebraic phase slip;
- `m=N`: periodic cusp resolves the balanced degeneracy;
- `m>N`: compressed-antiperiodic analytic well, with only an exponentially small physical-seam displacement.

Thus balance remains an isolated codimension-one lattice geometry with a fourth-order spectral anomaly.