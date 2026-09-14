# Canonical quarter-period `2`-adic phase for every sufficiently even jump

Date: 2026-09-14

Status: **Proved**. This packages the exact period-compression, all-layer geometry optimization, and Bloch phase-slip results directly in the original jump variable.

## 1. Construction

Let

\[
s=2^k n,
\qquad n\text{ odd},
\qquad k\ge2.
\]

Set

\[
\boxed{p:=2^{k+1}}
\tag{1.1}
\]

and

\[
L:=p/2=2^k.
\]

Inside one period `p=2L`, place the two positive local flux defects at

\[
0
\qquad\text{and}\qquad
\boxed{h:=p/4=2^{k-1}},
\tag{1.2}
\]

with every other local flux equal to `-1`.

Since

\[
s=Ln
\]

and `n` is odd, this word is compatible with the jump.

In the standard geometry parameters

\[
L=2(N+m),
\qquad h=2m,
\]

the phase is exactly balanced:

\[
\boxed{N=m=2^{k-2}.}
\tag{1.3}
\]

Let `R_s^{can}` be its continuous squared Bloch edge and

\[
\Gamma_s^{can}:=8-R_s^{can}.
\]

---

## Theorem A — canonical exact sub-eight phase

For every `k>=2` and every odd `n`,

\[
\boxed{R_s^{can}<8.}
\tag{2.1}
\]

### Proof

The exact even-separation phase diagram gives

\[
R<8
\iff
2m<T_N(3).
\]

Here `m=N=2^(k-2)`. Since `T_N(3)>=3N` for every `N>=1`,

\[
2m=2N<T_N(3),
\]

so the canonical phase is strictly sub-eight.

---

## Theorem B — minimal period inside the reflection-chiral two-defect class

The period in (1.1) is the shortest possible primitive period within the compatible reflection-chiral two-defect ansatz:

\[
\boxed{p_{min}=2^{k+1}.}
\tag{3.1}
\]

Indeed compatibility is equivalent to

\[
L\mid s,
\qquad s/L\text{ odd},
\]

so `v_2(L)=v_2(s)=k`; the smallest possible half-period is `L=2^k`.

---

## Theorem C — exact all-layer geometry optimality

For **every** integer `k>=2`, not merely for sufficiently large `k`, the quarter-period separation

\[
\boxed{h=p/4}
\]

is the unique even defect separation maximizing the full continuous Bloch gap among all reflection-chiral two-defect phases of the same minimal primitive period `p=2^(k+1)`.

Equivalently, with

\[
r=2^{k-2},
\]

for every positive integer pair

\[
N+m=2r
\]

and every odd part `n`,

\[
\boxed{
\Gamma_{r,r,q}
>
\Gamma_{N,m,q}
\qquad((N,m)\ne(r,r)).
}
\tag{4.1}
\]

### Proof structure

The complete proof is `ALL_LAYER_MINIMAL_PERIOD_QUARTER_OPTIMALITY.md`.

The universal competitor bound is

\[
\Gamma_{N,m,q}
< D_{\max\{N,m\}},
\qquad
D_j:=2-2\cos\frac\pi{2j}.
\]

Thus an unbalanced pair with `N+m=2r` obeys

\[
\Gamma_{N,m,q}<D_{r+1}.
\]

The balanced comparison is then closed as follows:

- `k=2`, `r=1`: there is no competing geometry;
- `k=3`, `r=2`: exact rational certificate;
- `k=4`, `r=4`: exact all-energy degree-16 Bernstein certificate;
- `k=5`, `r=8`: exact all-energy degree-32 Bernstein certificate;
- `k>=6`, hence `r>=16`: the analytic all-phase Dirichlet comparison theorem gives
  \[
  \Gamma_{r,r,q}>D_{r+1}
  \]
  uniformly in the odd multiplier.

Independent exact certificates at `r=16` and `r=32` audit the beginning of the analytic tail.

Therefore the minimal-period geometry is uniquely fixed at every `2`-adic layer.

---

## Theorem D — sharp large-valuation gap

Let `k->infinity`, while the odd part `n` may vary arbitrarily. Then

\[
\boxed{
p^2\Gamma_s^{can}
\longrightarrow16\pi^2.
}
\tag{5.1}
\]

Equivalently,

\[
\Gamma_s^{can}
=\frac{16\pi^2}{p^2}+o(p^{-2}).
\]

Since `p=2L`, this is the optimal period-normalized constant in the macroscopic even-separation two-defect family.

---

## Theorem E — all-orders Bloch phase slip of the canonical phase

Put

\[
r=2^{k-2}.
\]

At balanced geometry, the periodic compressed endpoint is the algebraically improving well. Let `delta_r` denote the compressed displacement from that periodic endpoint. Then

\[
\boxed{
|\delta_r|
=r^{-2}\left(
\frac\pi{4\sqrt2}
-\frac\pi{8r}
+\frac{\pi(32-27\sqrt2)}{192r^2}
+\cdots
\right).
}
\tag{6.1}
\]

The phase-slip gain also admits a full algebraic series,

\[
\boxed{
 e_r^+-\Gamma_s^{can}
=r^{-4}\left(
\frac{\pi^2}{32}
-\frac{3\pi^2}{32\sqrt2\,r}
+\frac{\pi^2(32\sqrt2-3)}{768r^2}
+\cdots
\right).
}
\tag{6.2}
\]

The existence of both complete series is proved in `ALL_ORDERS_PERIODIC_PHASE_SLIP_EXPANSION.md`.

Important orientation statement: the antiperiodic well is analytic and carries no cusp. At balance its endpoint gap agrees with the periodic endpoint to every algebraic order, but the periodic cusp lowers the true global gap by the algebraic amount (6.2), thereby selecting the periodic Bloch well.

---

## 7. Full high-order global series

Let

\[
A(r)=\sum_{j\ge2}a_jr^{-j}
\]

be the universal Robin endpoint series and

\[
C(r)=\sum_{j\ge0}c_jr^{-j-4}
\]

be the periodic cusp-gain series. Then the canonical balanced phase satisfies, to every algebraic order,

\[
\boxed{
\Gamma_s^{can}\sim A(r)-C(r).
}
\tag{7.1}

The first displayed terms are

\[
\begin{aligned}
\Gamma_s^{can}={}&\frac{\pi^2}{4r^2}
-\frac{\sqrt2\pi^2}{4r^3}
+\frac{\pi^2(66-\pi^2)}{192r^4}\\
&+\frac{\sqrt2\pi^2(-52+3\pi^2)}{256r^5}
+O(r^{-6}).
\end{aligned}
\tag{7.2}
\]

All higher coefficients are recursively determined by the two analytic implicit equations for the Robin root and the periodic cusp minimizer.

---

## 8. Comparison with the original shortest-separation compressed phase

At the same minimal period, the old separation-two compressed family has period-normalized leading constant

\[
16\arccos(1/3)^2,
\]

whereas the canonical balanced phase has

\[
16\pi^2.
\]

The asymptotic improvement factor is therefore

\[
\boxed{
\left(\frac{\pi}{\arccos(1/3)}\right)^2.
}
\tag{8.1}
\]

The improvement is purely geometric: no extra period is paid.

## 9. Headline formulation

The even-jump construction can now be stated without an eventuality qualifier:

> **If `v_2(s)=k>=2`, the shortest compatible reflection-chiral two-defect period is `2^{k+1}`. Within that minimal period there is a unique gap-maximizing even defect geometry: the two positive flux defects are separated by exactly one quarter of the period. The resulting canonical phase is strictly sub-eight for every finite layer, has optimal period-normalized gap constant `16pi^2`, and admits a complete Bloch phase-slip asymptotic expansion.**
