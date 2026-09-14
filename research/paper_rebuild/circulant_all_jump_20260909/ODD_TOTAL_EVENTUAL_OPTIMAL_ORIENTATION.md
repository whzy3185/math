# Eventual optimal geometry when the total arc parameter is odd

Date: 2026-09-14

Status: **Proved, with corrected beyond-all-orders seam term**.

When the coefficient period is congruent to `4 mod 8`, exact balance is impossible. The two nearest-balanced orientations agree at leading Dirichlet order but are separated by the periodic cusp at algebraic order four; the compressed-antiperiodic orientation also carries a much smaller hard-channel tunneling correction.

## 1. Setup

Fix

\[
N+m=2r+1,
\qquad r\to\infty,
\]

so

\[
p=8r+4.
\]

Let

\[
A_r=(r+1,r)
\]

be the periodic-cusp orientation and

\[
B_r=(r,r+1)
\]

the compressed-antiperiodic orientation. Put

\[
\Gamma_{N,m,q}=8-\max_{|z|=1}\rho(H_{N,m,q}(z))^2,
\qquad n=2q+1.
\]

## Theorem A — eventual unique optimizer

There exists `r_0` such that for every `r>=r_0` and every compatible odd multiplier,

\[
\boxed{
\Gamma_{r,r+1,q}
>
\Gamma_{N,m,q}
}
\]

for every other pair `N+m=2r+1`.

Thus the eventual unique optimizer is

\[
\boxed{(N,m)=(r,r+1),}
\]

i.e. the defect arc is one unit longer.

---

## 2. Precise nearest-orientation splitting

Let `A(ell)` be the universal endpoint Robin series and `C(ell)` the periodic cusp-gain series. Then

\[
\Gamma_{A_r}
\sim A(r+1)-C(r+1).
\tag{2.1}
\]

For the compressed-antiperiodic orientation define

\[
U_r:=U_{r-1}(3)
\]

and

\[
\boxed{
S_{r,n}:=
\frac{(2+2\cos(\pi/n))\pi^2}
{64\sqrt2\,U_r(r+1)^3}
\left(1+O(r^{-1})\right)
+O(U_r^{-2}(r+1)^{-6}).
}
\tag{2.2}

The seam-tunneling theorem gives

\[
\boxed{
\Gamma_{B_r}
=A(r+1)-S_{r,n}+O_K(r^{-K})
}
\tag{2.3}

for every fixed algebraic order `K` after the displayed Robin truncation is interpreted asymptotically.

Since

\[
S_{r,n}=O((3+2\sqrt2)^{-r}r^{-3})
\]

while

\[
C(r+1)
\sim\frac{\pi^2}{32(r+1)^4},
\]

we obtain

\[
\boxed{
\Gamma_{B_r}-\Gamma_{A_r}
=C(r+1)-S_{r,n}+o(r^{-K})
\sim\frac{\pi^2}{32r^4}>0.
}
\tag{2.4}

Thus the physical seam reduces the advantage of the compressed-antiperiodic orientation only by an exponentially small amount; it cannot change the eventual sign.

---

## 3. More distant geometries

Every pair other than `A_r,B_r` has

\[
M=\max\{N,m\}\ge r+2.
\]

The universal endpoint Dirichlet bound gives

\[
\Gamma_{N,m,q}<D_M,
\qquad D_M=2-2\cos\frac\pi{2M}.
\]

At algebraic scale the best possible soft-length improvement is bounded by `A(M)`, and

\[
A(r+1)-A(r+2)
=\frac{\pi^2}{2r^3}+O(r^{-4}).
\]

The tunneling correction (2.2) is exponentially smaller. Hence `B_r` beats every geometry with `M>=r+2` by order `r^-3` for all sufficiently large `r`.

---

## 4. Two stability scales

The odd-total geometry has two distinct stability scales:

\[
\boxed{
\Gamma_{B_r}-\Gamma_{A_r}
\sim\frac{\pi^2}{32r^4},
}
\]

while the separation from any geometry farther than one unit from balance is

\[
\Theta(r^{-3}).
\]

The physical seam adds only the beyond-all-orders correction `S_(r,n)`.

## 5. Finite switch

Exact rational certificates establish:

- `r=1,...,5`: `(r+1,r)` is uniquely optimal;
- `r=6,7,8`: `(r,r+1)` is uniquely optimal.

Thus the finite orientation switch is known to occur exactly between `r=5` and `r=6`. Making the eventual theorem effective from `r>=9` yields the complete all-period classification for `p=8r+4`.