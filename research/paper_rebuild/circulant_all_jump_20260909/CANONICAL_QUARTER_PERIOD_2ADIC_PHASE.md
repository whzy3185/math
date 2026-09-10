# Canonical quarter-period 2-adic phase for every sufficiently even jump

Date: 2026-09-10

Status: **Proved**. This packages the period-compression, exact phase-diagram, and geometry-optimization results directly in the original jump variable.

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
s=L n
\]

and `n` is odd, this word is compatible with the jump.

The geometry is exactly balanced. In the standard parameters

\[
L=2(N+m),
\qquad
h=2m,
\]

we have

\[
\boxed{N=m=2^{k-2}.}
\tag{1.3}
\]

Let `R_s^{\rm can}` be its continuous squared Bloch edge.

## Theorem A — canonical exact sub-eight phase

For every `k>=2` and every odd `n`,

\[
\boxed{R_s^{\rm can}<8.}
\tag{2.1}
\]

### Proof

The exact even-separation phase diagram gives

\[
R<8
\iff
2m<T_N(3).
\]

Here `m=N=2^{k-2}`. Since `T_N(3)>=3N` for every `N>=1`,

\[
2m=2N<T_N(3),
\]

and hence (2.1) follows.

Thus the quarter-period balanced word gives a strict sub-eight phase for every jump with `v_2(s)>=2`.

---

## Theorem B — minimal period inside the reflection-chiral two-defect class

The period `p=2^{k+1}` in (1.1) is the shortest possible primitive period within the compatible reflection-chiral two-defect ansatz.

Indeed compatibility requires

\[
s\equiv L\pmod{2L},
\]

or equivalently

\[
L\mid s,
\qquad
s/L\text{ odd}.
\]

Thus

\[
v_2(L)=v_2(s)=k,
\]

so the smallest possible `L` is `2^k`, giving the smallest period

\[
\boxed{p_{\min}=2^{k+1}.}
\tag{3.1}
\]

Hence the canonical balanced phase achieves strict spectral improvement without enlarging the shortest arithmetic period.

---

## Theorem C — sharp large-valuation gap

Let `k->infinity`, while the odd part `n` may vary arbitrarily. Then

\[
\boxed{
p^2\bigl(8-R_s^{\rm can}\bigr)
\longrightarrow16\pi^2.
}
\tag{4.1}
\]

Equivalently,

\[
\boxed{
8-R_s^{\rm can}
=\frac{16\pi^2}{p^2}+o(p^{-2})
=\frac{4\pi^2}{4^k}+o(4^{-k}).
}
\tag{4.2}
\]

### Proof

The balanced macroscopic full-Bloch theorem gives

\[
L^2(8-R_s^{\rm can})\to4\pi^2.
\]

Since `p=2L`, multiplication by four gives (4.1).

---

## Theorem D — eventual uniqueness of the quarter-period separation

There exists `k_0` such that for every

\[
k\ge k_0
\]

and every odd part `n`, the separation

\[
\boxed{h=p/4}
\]

is the unique even defect separation that maximizes the full Bloch gap among all reflection-chiral two-defect words having the same minimal period `p=2^{k+1}`.

This is exactly the eventual finite balanced-separation optimality theorem with

\[
r=2^{k-2}.
\]

---

## Theorem E — second-order Bloch phase slip of the canonical phase

Write

\[
r=2^{k-2}.
\]

Let `z_k` be a global maximizing Bloch phase and measure its displacement from the nearer compressed endpoint using

\[
\delta_k
=(2q+1)\arg z_k-\psi_{\rm end},
\qquad
\psi_{\rm end}\in\{0,\pi\}.
\]

Then

\[
\boxed{
r^2|\delta_k|
\to\frac{\pi}{4\sqrt2},}
\tag{5.1}
\]

and, if `e_r` denotes the better endpoint gap,

\[
\boxed{
r^4\left(e_r-(8-R_s^{\rm can})\right)
\to\frac{\pi^2}{32}.}
\tag{5.2}
\]

Thus the discrete geometry locks exactly at quarter period before the continuous Bloch phase locks: the latter retains a universal `r^-2` compressed phase slip.

---

## 6. Comparison with the original `h=2` compressed phase

At the same minimal period, the shortest-separation phase has normalized leading constant

\[
16\arccos(1/3)^2
\]

in `p^2(8-R)` normalization, whereas the canonical balanced phase has

\[
16\pi^2.
\]

Therefore the asymptotic improvement factor is

\[
\boxed{
\left(\frac{\pi}{\arccos(1/3)}\right)^2\approx6.51.
}
\tag{6.1}
\]

The gain comes entirely from defect geometry; the primitive period is unchanged.

## 7. Recommended headline formulation

The even-jump construction can now be stated directly as follows:

> **If `v_2(s)=k>=2`, there is an explicit two-defect signing of the shortest compatible period `2^{k+1}` whose defects are separated by one quarter of the period and whose continuous squared Bloch edge is strictly below `8`. As `k->infinity`, its period-normalized gap tends to the optimal two-defect constant `16pi^2`; for all sufficiently large `k`, the quarter-period separation is the unique gap-maximizing even separation within that minimal period.**

This is the canonical even-jump theorem that should replace the old period-`4s` construction in the abstract and introduction.