# Spectral-mass monotonicity and the critical layer `L=4`

Date: 2026-09-09

Status: **Proved**. This note belongs only to Paper I.

## 1. Setup

Use the compressed two-defect family of period `2L`, with `L>=4` even and jump

\[
s=L(2q+1).
\]

In the folded two-component gauge, write

\[
\omega=z^q\eta=e^{i\beta},
\qquad
\eta^2=z,
\]

and put

\[
c=\cos\beta,
\qquad
r=\sin\beta.
\]

The `L` onsite blocks are

\[
V_j=2c\,\sigma_x
\quad(j\ne1,2),
\]

and

\[
V_1=V_2=2r\,\sigma_y.
\]

All nearest-neighbor blocks are unitary Pauli blocks, including the closing Bloch block.

Define

\[
d=\omega^2+\omega^{-2}=2\cos(2\beta).
\]

Then

\[
r^2=\frac{2-d}{4}.
\]

---

## Theorem A — exact second spectral moment

For every even `L>=4`, every odd multiplier, and every Bloch phase,

\[
\boxed{
\operatorname{tr}H_{L,q}(z)^2
=12L-16-2(L-4)(2-d).}
\tag{1.1}
\]

Equivalently,

\[
\boxed{
\operatorname{tr}H_{L,q}(z)^2
=12L-16-8(L-4)\sin^2\beta.}
\tag{1.2}
\]

### Proof

The folded fiber is an `L`-cycle of two-component sites.

Each of the `L` nearest-neighbor block edges is unitary. An undirected block edge contributes

\[
2\operatorname{tr}(I_2)=4
\]

to `tr(H^2)`. Hence the nearest-neighbor contribution is

\[
4L.
\]

For the onsite blocks,

\[
V_j^2=4c^2I_2
\]

at the `L-2` generic sites, while

\[
V_1^2=V_2^2=4r^2I_2.
\]

Therefore

\[
\sum_j\operatorname{tr}(V_j^2)
=8\bigl((L-2)c^2+2r^2\bigr).
\]

Using

\[
c^2=1-r^2
\]

gives

\[
\begin{aligned}
\operatorname{tr}H^2
&=4L+8\bigl((L-2)(1-r^2)+2r^2\bigr)\\
&=12L-16-8(L-4)r^2,
\end{aligned}
\]

which is (1.2). Substituting `r^2=(2-d)/4` gives (1.1).

---

## Corollary B — exact `L=4` criticality

If

\[
L=4,
\]

then

\[
\boxed{
\operatorname{tr}H_{4,q}(z)^2=32}
\]

for every Bloch phase.

Thus the second spectral moment is completely insensitive to the transfer of mass between generic and defect onsite blocks.

If

\[
L>4,
\]

then

\[
\boxed{
\operatorname{tr}H_{L,q}(z)^2
\le12L-16,}
\]

with equality if and only if

\[
d=2.
\]

Hence every departure from a long-jump resonance strictly decreases the total squared spectral mass.

---

## Corollary C — analytic explanation of the exceptional first layer

The exact endpoint-dominance conjecture has a unique small-period obstruction in the observed data: `L=4` permits non-endpoint global maxima for some odd multipliers, whereas every tested `L>=6` is endpoint dominated.

Theorem A identifies a structural reason why `L=4` is exceptional:

\[
\boxed{L-4}
\]

is exactly the coefficient controlling the spectral-mass penalty away from `d=2`.

Thus `L=4` is not merely a small numerical exception. It is the unique layer at which the generic onsite population `L-2` and the two defect sites balance so that the second spectral moment loses all preference for the resonant phase.

For `L>4`, the imbalance produces the strict penalty

\[
2(L-4)(2-d).
\]

This does not by itself prove spectral-radius endpoint dominance, but it supplies a global moment mechanism consistent with and structurally supporting that stronger theorem.

---

## 4. Editorial role

This theorem should be placed immediately before the finite endpoint-dominance discussion. It explains why the general compression theorem starts at `L=4`, why `L=4` behaves differently from higher layers, and why exact endpoint locking is plausible from `L=6` onward.
