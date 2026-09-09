# Signed-reflection chirality for arbitrary even two-defect separation

Date: 2026-09-09

Status: **Proved**. This note belongs only to Paper I.

The previously used compressed two-defect word places the two positive local fluxes at positions `0` and `2`. The reflection mechanism is in fact much more general.

## 1. Two defects at arbitrary separation

Let `L>=4` be even and let the coefficient period be `2L`. Fix an even integer

\[
2\le h\le 2L-2.
\]

Define the local flux word by

\[
Q_0=Q_h=1,
\qquad
Q_j=-1\quad(j\ne0,h).
\tag{1.1}
\]

Choose the Hamilton-gauge lift `tau_0=1` and reconstruct

\[
Q_j=\tau_j\tau_{j+1}.
\]

Then

\[
\tau_j=
\begin{cases}
1,&j=0,1,\\
(-1)^{j-1},&2\le j\le h,\\
(-1)^j,&h+1\le j<2L.
\end{cases}
\tag{1.2}
\]

(The formulas agree at the transition because `h` is even.)

### Lemma A — general reversal identity

For every index modulo `2L`,

\[
\boxed{
\tau_{h+1-j}=-\tau_j.
}
\tag{1.3}
\]

### Proof

The two defects divide the cyclic word into two alternating arcs. Reflection about the midpoint of the defect pair interchanges those arcs. A direct verification from (1.2) is immediate.

For `0<=j<=h+1`, the reflected index stays in the first arc and the parity formulas in (1.2) give the minus sign. For `h+2<=j<2L`, reduce `h+1-j` modulo `2L`; because both `h` and `2L` are even, the parity again changes by one. Thus (1.3) holds on the whole cycle.

---

## 2. The step operator

Let

\[
s=L(2q+1),
\qquad q\ge0,
\tag{2.1}
\]

and define the real periodic signed step operator

\[
(A_{L,q,h}x)_j
=x_{j-1}+x_{j+1}
+\tau_{j-s}x_{j-s}+\tau_jx_{j+s}.
\tag{2.2}
\]

Define

\[
(Dx)_j=(-1)^jx_j
\]

and the reflection

\[
(R_hx)_j=x_{L+h+1-j}.
\tag{2.3}
\]

### Theorem B — arbitrary-even-separation chirality

For every even `h`,

\[
\boxed{
(DR_h)A_{L,q,h}(DR_h)^{-1}
=-A_{L,q,h}.
}
\tag{2.4}
\]

### Proof

Reflection preserves nearest-neighbor edges, while conjugation by `D` negates every nearest-neighbor coefficient.

A chord starting at `j` has sign `tau_j`. Under `R_h`, its reflected starting index is

\[
L+h+1-j-s.
\]

Since

\[
s\equiv L\pmod{2L},
\]

this is congruent to

\[
h+1-j\pmod{2L}.
\]

Lemma A therefore gives the reflected chord sign

\[
\tau_{h+1-j}=-\tau_j.
\]

Because `s` and `L` are even, `D` contributes no sign change to a chord. Thus reflection supplies the required minus sign on every chord, while `D` supplies it on every nearest-neighbor edge. This proves (2.4).

---

## 3. Fiberwise consequence

Let `H_{L,q,h}(z)` denote the `2L x 2L` Bloch fiber under

\[
x_{j+2L}=zx_j,
\qquad |z|=1.
\]

Reflection sends `z` to `z^{-1}`, and complex conjugation sends it back. Hence

\[
\mathcal C_{h,z}:=DR_hK
\]

is an antiunitary operator on the single `z`-fiber and satisfies

\[
\boxed{
\mathcal C_{h,z}H_{L,q,h}(z)\mathcal C_{h,z}^{-1}
=-H_{L,q,h}(z).
}
\tag{3.1}
\]

Therefore

\[
\boxed{
\operatorname{spec}H_{L,q,h}(z)
=-\operatorname{spec}H_{L,q,h}(z)
}
\tag{3.2}
\]

including multiplicity, and the characteristic polynomial is even:

\[
\boxed{
\det(\lambda I-H_{L,q,h}(z))
=P_{L,q,h,z}(\lambda^2).
}
\tag{3.3}
\]

---

## 4. Why even separation is the natural chiral class

If the second defect is at an odd separation `h`, the same reconstruction gives a reversal factor `+1` rather than `-1`. Since the jump `s` is even, the alternating diagonal contributes no chord sign, and the operator no longer anticommutes with the same signed reflection.

Thus the parity of the defect separation is structural:

\[
\boxed{
h\text{ even}}
\]

is exactly the regime in which this reflection mechanism produces chiral symmetry for `s=L(2q+1)`.

---

## 5. Research consequence

The compressed `h=2` family is therefore one point in a larger even-separation family. This opens a second variational problem internal to Paper I:

> for fixed compressed period `2L`, how does the Bloch edge depend on the even defect separation `h`, and which separation maximizes the sub-eight gap?

Numerical exploration suggests that the asymptotic Robin constant changes with defect geometry. No gap theorem for general `h` is asserted in this note; only the symmetry theorem is proved.