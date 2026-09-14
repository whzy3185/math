# Eventual optimal geometry when the total arc parameter is odd

Date: 2026-09-14

Status: **Proved**.

This complements `ALL_FIXED_PERIOD_BALANCED_OPTIMALITY.md`.  When the coefficient period is congruent to `4 mod 8`, exact balance is impossible; the two nearest-balanced orientations are no longer equivalent beyond leading order.

## 1. Setup

Fix

\[
N+m=2r+1,
\qquad r\to\infty.
\]

Then

\[
L=2(N+m)=4r+2
\]

and the primitive coefficient period is

\[
\boxed{p=2L=8r+4.}
\]

Let

\[
\Gamma_{N,m,q}
=8-\max_{|z|=1}\rho(H_{N,m,q}(z))^2.
\]

The two nearest-balanced geometries are

\[
A_r=(r+1,r)
\]

and

\[
B_r=(r,r+1).
\]

Both have the same dominant soft length `r+1`, but they have opposite orientation:

- `A_r` belongs to the periodic-cusp side;
- `B_r` belongs to the compressed-antiperiodic analytic side.

## Theorem A — eventual unique optimizer

There exists `r_0` such that for every

\[
r\ge r_0
\]

and every compatible odd multiplier,

\[
\boxed{
\Gamma_{r,r+1,q}
>
\Gamma_{N,m,q}
}
\tag{1.1}

for every other positive integer pair

\[
N+m=2r+1,
\qquad
(N,m)\ne(r,r+1).
\]

Thus for all sufficiently large periods

\[
p\equiv4\pmod8,
\]

the unique gap-maximizing two-defect geometry is the nearly balanced orientation with the **defect arc one unit longer**:

\[
\boxed{m=N+1.}
\tag{1.2}

---

## 2. Comparison of the two nearest-balanced orientations

Let

\[
A(\ell)=\sum_{j\ge2}a_j\ell^{-j}
\]

be the universal endpoint Robin series and

\[
C(\ell)=\sum_{j\ge0}c_j\ell^{-j-4}
\]

be the periodic cusp-gain series.

For `A_r=(r+1,r)`, the dominant soft length is `r+1` and the periodic cusp applies:

\[
\boxed{
\Gamma_{A_r}
\sim A(r+1)-C(r+1).
}
\tag{2.1}

For `B_r=(r,r+1)`, the dominant soft length is also `r+1`, but the compressed-antiperiodic well is analytic.  The corrected physical-seam theorem gives

\[
\boxed{
\Gamma_{B_r}
=A(r+1)+O(\Lambda^{-2r}),
\qquad
\Lambda=3+2\sqrt2.
}
\tag{2.2}

Therefore

\[
\boxed{
\Gamma_{B_r}-\Gamma_{A_r}
\sim C(r+1)
\sim\frac{\pi^2}{32(r+1)^4}>0.
}
\tag{2.3}

The exponentially small physical-seam correction in (2.2) is negligible compared with the algebraic cusp gap. Hence `B_r` strictly beats `A_r` for every sufficiently large `r`.

---

## 3. Excluding more distant geometries

Every pair other than `A_r,B_r` has

\[
M:=\max\{N,m\}\ge r+2.
\]

The universal endpoint Dirichlet bound gives

\[
\Gamma_{N,m,q}<D_M,
\qquad
D_M=2-2\cos\frac\pi{2M}.
\]

At the algebraic level, the best possible gap with soft length at least `r+2` is governed by

\[
A(r+2)
=
A(r+1)-\frac{\pi^2}{2r^3}+O(r^{-4}).
\]

By contrast,

\[
\Gamma_{B_r}
=A(r+1)+O(\Lambda^{-2r}).
\]

Thus

\[
\Gamma_{B_r}-\Gamma_{N,m,q}
\ge\frac{c}{r^3}
\]

for all sufficiently large `r`, uniformly over every geometry with `M>=r+2` and every compatible odd multiplier.

This excludes all non-nearest geometries and proves Theorem A.

---

## 4. Two different stability scales

The odd-total geometry has two nested spectral separations.

### Orientation splitting

Between the two nearest-balanced orientations,

\[
\boxed{
\Gamma_{B_r}-\Gamma_{A_r}
\sim\frac{\pi^2}{32r^4}.
}
\tag{4.1}

This is exactly the periodic cusp scale.

### Distance-from-balance splitting

Between the winner `B_r` and any geometry two or more units away from balance, the gap is

\[
\boxed{\Theta(r^{-3}).}
\tag{4.2}

Thus the hierarchy is

\[
\text{coarse geometry cost }r^{-3}
\gg
\text{orientation/cusp cost }r^{-4}.
\]

---

## 5. Full period-parity picture

Together with `ALL_FIXED_PERIOD_BALANCED_OPTIMALITY.md`, the large-period variational geometry is now:

- if
  \[
  p\equiv0\pmod8,
  \]
  exact balance is available and is uniquely optimal;
- if
  \[
  p\equiv4\pmod8,
  \]
  exact balance is impossible and the unique eventual optimizer is the one-step orientation
  \[
  \boxed{m=N+1.}
  \]

The asymmetry in the second case is entirely a fourth-order Bloch effect: at leading Dirichlet order the two nearest-balanced orientations are indistinguishable.