# Endpoint dominance for every fixed even spectral moment

Date: 2026-09-09

Status: **Proved**. This note belongs only to Paper I.

## 1. Statement

Fix an integer

\[
m\ge1.
\]

For the period-`2L` compressed two-defect family, let

\[
M_{m,L}(z):=\operatorname{tr}H_{L,q}(z)^{2m}.
\]

### Theorem A — fixed-moment endpoint dominance

For every fixed `m`, there exists an even integer `L_m` such that for every even

\[
L\ge L_m,
\]

every odd multiplier, and every Bloch phase,

\[
\boxed{
\operatorname{tr}H_{L,q}(z)^{2m}
\le
\operatorname{tr}H_{L,q}(1)^{2m}.}
\tag{1.1}
\]

Equality is possible only at the long-phase resonance

\[
d=z^{2q+1}+z^{-(2q+1)}=2.
\tag{1.2}
\]

Thus every fixed Schatten moment eventually selects the same resonant endpoint.

The theorem is uniform in the odd multiplier.

---

## 2. Bulk comparison operator

Put

\[
x=\sin^2\beta=\frac{2-d}{4}\in[0,1].
\]

Away from the two defect sites, the folded operator is the homogeneous two-component chain with onsite block

\[
2\sqrt{1-x}\,\sigma_x
\]

and nearest-neighbor block `sigma_z`.

Its infinite-volume Fourier symbol is

\[
\mathcal H_x(\theta)
=2\cos\theta\,\sigma_z
+2\sqrt{1-x}\,\sigma_x.
\]

Since the two Pauli matrices anticommute,

\[
\mathcal H_x(\theta)^2
=4\bigl(1-x+\cos^2\theta\bigr)I_2.
\]

Hence the bulk `2m`th moment per block site is

\[
\boxed{
B_m(x)
=\frac{2\,4^m}{2\pi}
\int_0^{2\pi}
\bigl(1-x+\cos^2\theta\bigr)^m\,d\theta.}
\tag{2.1}
\]

---

## 3. Uniform bulk penalty

Differentiating (2.1),

\[
-B_m'(x)
=\frac{2\,4^m m}{2\pi}
\int_0^{2\pi}
\bigl(1-x+\cos^2\theta\bigr)^{m-1}\,d\theta.
\]

The integrand decreases with `x`, so for `0<=x<=1`,

\[
-B_m'(x)
\ge
c_m,
\]

where

\[
\boxed{
c_m=
\frac{2\,4^m m}{2\pi}
\int_0^{2\pi}\cos^{2m-2}\theta\,d\theta>0.}
\tag{3.1}
\]

Therefore

\[
\boxed{
B_m(0)-B_m(x)\ge c_m x.}
\tag{3.2}
\]

This is the extensive spectral-moment penalty for moving mass away from the endpoint.

---

## 4. The defect correction is only local

Assume first

\[
L>2m.
\tag{4.1}
\]

A closed block walk of length `2m` cannot wind around the `L`-cycle. Hence its Bloch boundary phase cancels, and the moment depends on the long phase only through

\[
d=2-4x.
\]

Compare the two-defect fiber with the homogeneous bulk cycle at the same `x`. A closed walk that never enters the `2m`-neighborhood of either defect has exactly the homogeneous contribution.

Thus

\[
\boxed{
\operatorname{tr}H_{L,q}(z)^{2m}
=L B_m(x)+E_{m,L}(x),}
\tag{4.2}
\]

where the correction comes from only `O(m)` starting block sites.

For fixed `m`, the local closed-walk population is finite. Each block matrix has norm at most `2` onsite and `1` offsite, so there is a constant `C_m` independent of `L`, `q`, and the phase such that the coefficients of the local correction are bounded by `C_m`.

Moreover `E_{m,L}` is a polynomial in `d`, hence in `x`. This follows either directly from closed-walk phase cancellation or from the exact two-phase characteristic equation and Newton identities; when `2m<L`, no basic winding term `e=z+z^{-1}` can occur.

At `x=0`, the defect correction has its endpoint value. Since the correction polynomial has degree at most `m` and uniformly bounded coefficients, there is a constant, again denoted `C_m`, such that

\[
\boxed{
|E_{m,L}(x)-E_{m,L}(0)|\le C_m x}
\tag{4.3}
\]

for every `x in [0,1]` and every `L>2m`.

---

## 5. Extensive bulk beats the finite defect

Combining (3.2), (4.2), and (4.3),

\[
\begin{aligned}
&M_{m,L}(1)-M_{m,L}(z)\\
&\qquad=L\bigl(B_m(0)-B_m(x)\bigr)
+E_{m,L}(0)-E_{m,L}(x)\\
&\qquad\ge(Lc_m-C_m)x.
\end{aligned}
\tag{5.1}
\]

Choose an even `L_m` so large that

\[
L_m>2m
\]

and

\[
L_m c_m>C_m.
\]

Then for every even `L>=L_m`,

\[
M_{m,L}(1)-M_{m,L}(z)>0
\]

whenever `x>0`, proving (1.1)--(1.2).

---

## 6. Relation to the exact low moments

For the first three values of `m`, stronger finite statements are already proved:

\[
m=1,2,3:
\qquad
L\ge6
\Longrightarrow
M_{m,L}(z)\le M_{m,L}(1),
\]

with explicit closed formulas for the differences.

Theorem A shows that this is not a low-order coincidence. Every fixed even spectral moment eventually exhibits the same endpoint preference.

---

## 7. Scope

The threshold `L_m` produced by the bulk-defect proof is not optimized and may grow with `m`. Therefore this theorem alone does not yet allow one to fix `L` and send `m->infinity`; exact spectral-radius endpoint dominance for every `L>=6` remains stronger.

Nevertheless the theorem establishes a full asymptotic Schatten hierarchy:

\[
\boxed{
\text{for every fixed }m,
\quad
\|H(z)\|_{S_{2m}}
\le\|H(1)\|_{S_{2m}}
\text{ for all sufficiently large }L.}
\]

This places the spectral-radius conjecture inside a coherent hierarchy of rigorously proved moment inequalities.
