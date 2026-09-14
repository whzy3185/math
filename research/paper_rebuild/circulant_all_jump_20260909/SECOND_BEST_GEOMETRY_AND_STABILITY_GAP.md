# Second-best fixed-period geometry and the spectral stability gap

Date: 2026-09-14

Status: **Proved**.

This theorem quantitatively strengthens `ALL_FIXED_PERIOD_BALANCED_OPTIMALITY.md`: for large period it identifies the unique runner-up and gives the complete algebraic expansion of the first-versus-second geometry gap.

## 1. Fixed-period setup

Fix

\[
N+m=2r,
\qquad r\to\infty,
\]

so the primitive coefficient period is

\[
p=8r.
\]

Let

\[
\Gamma_{N,m,q}
=8-\max_{|z|=1}\rho(H_{N,m,q}(z))^2.
\]

The unique optimum is the balanced geometry

\[
(N,m)=(r,r).
\]

Define

\[
\Gamma_r^{(1)}:=\Gamma_{r,r,q}
\]

and let

\[
\Gamma_r^{(2)}
:=
\max_{\substack{N+m=2r\\(N,m)\ne(r,r)}}
\Gamma_{N,m,q}.
\]

The compatible odd multiplier may vary arbitrarily with `r`.

## Theorem A — eventual unique second-best geometry

For all sufficiently large `r`, the unique second-best geometry is

\[
\boxed{
(N,m)=(r-1,r+1).
}
\tag{1.1}

Equivalently, after leaving balance by one unit, the better orientation is the one whose **defect arc is the longer soft arc**, i.e. the compressed-antiperiodic orientation.

The opposite one-step geometry

\[
(r+1,r-1)
\]

has the same leading soft length `r+1` but loses an algebraic amount through the periodic cusp.

---

## 2. Universal formal-series notation

Let

\[
A(\ell)=\sum_{j\ge2}a_j\ell^{-j}
\]

be the universal endpoint Robin series, and let

\[
C(\ell)=\sum_{j\ge0}c_j\ell^{-j-4}
\]

be the periodic cusp-gain series.

The all-orders global phase diagram gives

\[
\boxed{
\Gamma_r^{(1)}
\sim A(r)-C(r).
}
\tag{2.1
}
\]

For the candidate `(r-1,r+1)`, the dominant well is compressed-antiperiodic, so

\[
\boxed{
\Gamma_{r-1,r+1,q}
=A(r+1)+O(\Lambda^{-2(r-1)}),
}
\tag{2.2}

where

\[
\Lambda=3+2\sqrt2.
\]

For the opposite orientation `(r+1,r-1)`,

\[
\boxed{
\Gamma_{r+1,r-1,q}
\sim A(r+1)-C(r+1).
}
\tag{2.3}

Hence

\[
\Gamma_{r-1,r+1,q}
-
\Gamma_{r+1,r-1,q}
\sim C(r+1)>0.
\tag{2.4}
\]

Thus the compressed-antiperiodic one-step geometry beats the periodic one-step geometry for all sufficiently large `r`.

---

## 3. Excluding more distant geometries

If an unbalanced geometry is not one of the two one-step pairs, then

\[
M:=\max\{N,m\}\ge r+2.
\]

The endpoint upper bound and the all-orders Robin theorem give

\[
\Gamma_{N,m,q}
\le A(M)+o(r^{-K})
\]

for every fixed algebraic order `K`, uniformly on the fixed-period family.  Since `A` is decreasing for large argument,

\[
A(r+1)-A(r+2)
=\frac{\pi^2}{2r^3}+O(r^{-4})>0.
\]

Therefore every geometry with `M>=r+2` has smaller gap than `(r-1,r+1)` for all sufficiently large `r`.

This proves Theorem A.

---

## Theorem B — first-versus-second stability gap

Define

\[
\Delta_r:=\Gamma_r^{(1)}-\Gamma_r^{(2)}.
\]

Then, uniformly in arbitrary compatible odd multipliers,

\[
\boxed{
\Delta_r
\sim
A(r)-C(r)-A(r+1).
}
\tag{4.1}

In particular,

\[
\boxed{
\begin{aligned}
\Delta_r
={}&\frac{\pi^2}{2r^3}
-
\frac{\pi^2(25+24\sqrt2)}{32r^4}\\
&+
\frac{\pi^2}{r^5}
\left(
\frac52+rac{99\sqrt2}{64}-\frac{\pi^2}{48}
\right)\\
&+
\frac{\pi^2}{r^6}
\left(
-\frac{1279}{256}
-\frac{91\sqrt2}{24}
+\frac{5\pi^2}{96}
+\frac{15\sqrt2\pi^2}{256}
\right)\\
&+O(r^{-7})
+O(\Lambda^{-2r}).
\end{aligned}}
\tag{4.2}

The leading stability law is therefore

\[
\boxed{
\Delta_r\sim\frac{\pi^2}{2r^3}.
}
\tag{4.3}

In terms of the primitive period `p=8r`,

\[
\boxed{
\Delta_r
\sim
\frac{256\pi^2}{p^3}.
}
\tag{4.4}

---

## 5. Derivation of the displayed coefficients

Use

\[
A(r)
=a_2r^{-2}+a_3r^{-3}+a_4r^{-4}+a_5r^{-5}+a_6r^{-6}+O(r^{-7})
\]

with

\[
a_2=\frac{\pi^2}{4},
\qquad
a_3=-\frac{\sqrt2\pi^2}{4},
\]

\[
a_4=\frac{\pi^2(72-\pi^2)}{192},
\qquad
a_5=\frac{\sqrt2\pi^2(-64+3\pi^2)}{256},
\]

\[
a_6=\frac{\pi^2(\pi^4-750\pi^2+7200)}{23040},
\]

and

\[
C(r)
=\frac{\pi^2}{32r^4}
-rac{3\pi^2}{32\sqrt2\,r^5}
+rac{\pi^2(32\sqrt2-3)}{768r^6}
+O(r^{-7}).
\]

Expand

\[
(r+1)^{-j}
=r^{-j}(1+r^{-1})^{-j}
\]

binomially and collect powers through `r^-6`.  This gives (4.2).

The exponentially small physical-seam correction on the second-best compressed-antiperiodic branch is absorbed in the final `O(Lambda^-2r)` term.

---

## 6. Variational interpretation

The finite-period geometry landscape has three nested scales:

1. **best geometry:** exact balance `(r,r)`;
2. **second-best geometry:** the one-step compressed-antiperiodic orientation `(r-1,r+1)`;
3. **continuous Bloch optimization:** the balanced periodic phase slips only at the smaller `r^-4` scale.

The geometric stability gap is therefore one algebraic order larger than the internal Bloch phase-slip gain:

\[
\text{geometry stability}=\Theta(r^{-3}),
\qquad
\text{Bloch phase slip}=\Theta(r^{-4}).
\]

This quantifies the robustness of the balanced quarter-period optimizer.