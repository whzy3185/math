# General signed-reflection chirality for the two-defect family

Date: 2026-09-09

Status: **Proved**. This is a structural theorem for Paper I. It applies to arbitrary even half-period and is independent of the finite-global extremal problem.

## 1. Two-defect word of period `2L`

Let `L>=4` be even. On the cyclic index set modulo `2L`, define the local flux word

\[
Q_0=Q_2=1,
\qquad
Q_j=-1\quad(j\ne0,2).
\]

Choose `tau_0=1` and reconstruct the Hamilton-gauge word from

\[
Q_j=\tau_j\tau_{j+1}.
\]

Then

\[
\tau=(1,1,-1,-1,1,-1,1,-1,\ldots,1,-1),
\]

that is,

\[
\tau_0=\tau_1=1,
\qquad
\tau_2=\tau_3=-1,
\qquad
\tau_j=(-1)^j\quad(4\le j<2L).
\tag{1.1}
\]

### Lemma 1 — reversal identity

For every index modulo `2L`,

\[
\boxed{\tau_{3-j}=-\tau_j.}
\tag{1.2}
\]

#### Proof

For `j=0,1,2,3`, (1.2) follows directly from the first four entries

\[
(1,1,-1,-1).
\]

If `4<=j<2L`, then `3-j mod 2L=2L+3-j`, which again lies between `4` and `2L-1`. Hence by (1.1), using that `2L` is even,

\[
\tau_{3-j}
=(-1)^{2L+3-j}
=(-1)^{3-j}
=-(-1)^j
=-\tau_j.
\]

This proves the identity.

---

## 2. Infinite signed step operator

Let

\[
s=L(2q+1),
\qquad q\ge0.
\]

Because `L` is even, `s` is even. Define the real self-adjoint periodic operator on sequences on `Z` by

\[
(A_sx)_j
=x_{j-1}+x_{j+1}
+\tau_{j-s}x_{j-s}
+\tau_jx_{j+s}.
\tag{2.1}
\]

The coefficient word has period `2L`.

Define the alternating diagonal unitary

\[
(Dx)_j=(-1)^jx_j
\]

and the reflection

\[
(Rx)_j=x_{L+3-j}.
\]

### Theorem 2 — signed-reflection chirality

The unitary involutive symmetry on the infinite operator satisfies

\[
\boxed{(DR)A_s(DR)^{-1}=-A_s.}
\tag{2.2}
\]

Consequently the infinite periodic spectrum is symmetric about zero.

#### Proof

Reflection preserves the nearest-neighbor geometry, while conjugation by `D` changes the sign of every nearest-neighbor matrix element because adjacent indices have opposite parity.

Consider now a chord edge joining `j` to `j+s`, whose sign is `tau_j`. Reflection sends this unordered edge to the edge joining

\[
L+3-j-s
\quad\text{and}\quad
L+3-j.
\]

The reflected chord therefore has Hamilton-gauge sign

\[
\tau_{L+3-j-s}.
\]

Since

\[
s=L(2q+1)\equiv L\pmod{2L},
\]

we have

\[
L+3-j-s\equiv3-j\pmod{2L}.
\]

Lemma 1 gives

\[
\tau_{L+3-j-s}=\tau_{3-j}=-\tau_j.
\]

Because `s` is even, the alternating diagonal `D` contributes the factor

\[
(-1)^j(-1)^{j+s}=(-1)^s=1
\]

on a chord. Thus reflection supplies exactly one minus sign to each chord coefficient, while `D` supplies exactly one minus sign to each nearest-neighbor coefficient. Every matrix element of `A_s` is therefore negated under conjugation by `DR`, which proves (2.2).

---

## 3. Fiberwise antiunitary chirality

Let `H_s(z)` be the `2L x 2L` Bloch fiber with

\[
x_{j+2L}=zx_j,
\qquad |z|=1.
\]

Reflection changes the Bloch multiplier from `z` to `z^{-1}`. Complex conjugation `K` also changes `z` to `z^{-1}`, because all coefficients of the infinite operator are real.

Therefore

\[
\mathcal C_z:=DRK
\]

acts antiunitarily on the single `z`-fiber.

### Corollary 3 — even characteristic polynomial

For every unit Bloch phase `z`,

\[
\boxed{\mathcal C_z H_s(z)\mathcal C_z^{-1}=-H_s(z).}
\tag{3.1}
\]

Hence

\[
\operatorname{spec}H_s(z)
=-\operatorname{spec}H_s(z),
\]

including multiplicity, and

\[
\boxed{
\det(\lambda I-H_s(z))=P_{L,q,z}(\lambda^2)
}
\tag{3.2}
\]

for a monic degree-`L` polynomial in `lambda^2`.

This conclusion is conceptual and does not come from a determinant accident.

---

## 4. Relation to the proved arithmetic layers

The `v_2(s)=2` period-eight theorem is the case

\[
L=4,
\qquad 2L=8.
\]

The `v_2(s)=3` period-sixteen theorem is the case

\[
L=8,
\qquad 2L=16.
\]

For larger powers of two `L=2^k`, the same theorem supplies chirality for the natural candidate period

\[
2L=2^{k+1}
\]

whenever

\[
s=L(2q+1).
\]

Thus the conjectural higher `2`-adic hierarchy already has a rigorous symmetry theorem in all layers. What remains open is not the symmetry, but the uniform positivity of

\[
8I-H_s(z)^2
\]

for every `L`.

---

## 5. Editorial role

This theorem should appear before the individual period-eight and period-sixteen calculations in the final manuscript. It turns the arithmetic examples into specializations of one general structural mechanism:

\[
\text{two local flux defects}
\Longrightarrow
\text{signed reflection}
\Longrightarrow
\text{fiberwise chirality}
\Longrightarrow
\text{even squared spectral problem}.
\]

The remaining spectral inequalities then determine which arithmetic layers actually cross below the squared edge `8`.
