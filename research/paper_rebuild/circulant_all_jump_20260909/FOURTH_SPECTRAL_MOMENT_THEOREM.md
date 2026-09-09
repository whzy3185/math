# Exact fourth spectral moment for the compressed two-defect family

Date: 2026-09-09

Status: **Proved**. This note belongs only to Paper I.

## 1. Setup

Use the folded `L`-site two-component representation of the period-`2L` compressed two-defect family, with `L>=6` even.

Let

\[
\omega=e^{i\beta},
\qquad
c=\cos\beta,
\qquad
r=\sin\beta,
\]

so

\[
c^2+r^2=1.
\]

The generic onsite blocks are

\[
V_g=2c\,\sigma_x,
\]

and the two defect onsite blocks are

\[
V_d=2r\,\sigma_y.
\]

The nearest-neighbor block edges are unitary Pauli blocks. For `L>=6`, the two-step graph has no short-cycle collision, so the Frobenius decomposition of `H^2` is local.

---

## Theorem A — exact fourth moment

For every even `L>=6`, every odd multiplier, and every Bloch phase,

\[
\boxed{
\operatorname{tr}H^4
=4\Bigl(19L-24+(64-24L)r^2+8Lr^4\Bigr).}
\tag{1.1}
\]

Equivalently, since

\[
r^2=\frac{2-d}{4},
\]

this is a quadratic polynomial in the long-phase mass `2-d`.

### Proof

Write the folded fiber as a block cycle. The diagonal blocks of `H^2` are

\[
D_j=2I_2+V_j^2.
\]

Hence

\[
D_g=(2+4c^2)I_2=(6-4r^2)I_2,
\]

and

\[
D_d=(2+4r^2)I_2.
\]

Their contribution to `tr(H^4)=||H^2||_F^2` is

\[
2(L-2)(6-4r^2)^2+4(2+4r^2)^2.
\tag{1.2}
\]

For a nearest-neighbor block edge with block `E`, the corresponding off-diagonal block of `H^2` is

\[
V_jE+EV_{j+1}.
\]

On generic-generic and defect-defect edges this vanishes by the Pauli anticommutation and equality of neighboring onsite blocks. There are exactly two generic-defect interfaces. At either interface,

\[
\|V_d-V_g\|_F^2
=\operatorname{tr}\bigl((V_d-V_g)^*(V_d-V_g)\bigr)
=8(c^2+r^2)=8.
\]

Since each off-diagonal block occurs with its adjoint, the two interfaces contribute

\[
2\cdot2\cdot8=32.
\tag{1.3}
\]

Finally, every distance-two block of `H^2` is a product of two unitary Pauli edge blocks and therefore has Frobenius norm squared `2`. For `L>=6` there are `L` unordered distance-two pairs, giving

\[
2\cdot L\cdot2=4L.
\tag{1.4}
\]

Adding (1.2)--(1.4) yields

\[
\operatorname{tr}H^4
=2(L-2)(6-4r^2)^2
+4(2+4r^2)^2
+32+4L,
\]

which simplifies to (1.1).

---

## Corollary B — fourth-moment endpoint dominance

At the long-phase resonance

\[
r=0
\qquad(d=2),
\]

we have

\[
\operatorname{tr}H^4=4(19L-24).
\]

Subtracting the general value gives

\[
\boxed{
\operatorname{tr}H(1)^4-\operatorname{tr}H(z)^4
=32r^2\bigl((3L-8)-Lr^2\bigr).}
\tag{2.1}
\]

For `0<=r^2<=1` and `L>4`,

\[
(3L-8)-Lr^2
\ge2L-8>0.
\]

Hence for every even `L>=6`,

\[
\boxed{
\operatorname{tr}H(z)^4
\le\operatorname{tr}H(1)^4,}
\tag{2.2}
\]

with equality if and only if

\[
r=0
\qquad\Longleftrightarrow\qquad d=2.
\]

Thus the endpoint is the unique maximizer not only of the second spectral moment but also of the fourth spectral moment.

---

## 3. Relation to the `L=4` anomaly

The fourth-moment formula also clarifies the first layer. Formally setting `L=4` in (2.1) gives

\[
32r^2(4-4r^2)=128r^2(1-r^2),
\]

so both `r=0` and `r=1` are fourth-moment maximizers. This is consistent with the special period-eight layer, where non-endpoint resonant behavior can compete.

For `L>4`, the degeneracy disappears completely.

---

## 4. Structural consequence

Together with the second-moment theorem,

\[
\operatorname{tr}H^2
=12L-16-8(L-4)r^2,
\]

we now have two independent global moment inequalities selecting the endpoint:

\[
\boxed{
\operatorname{tr}H(z)^{2m}
\le\operatorname{tr}H(1)^{2m}
\quad\text{for }m=1,2,\ L>=6.}
\]

This strongly suggests an all-even-moment theorem. If proved for every `m`, the spectral-radius endpoint dominance would follow by taking `2m`th roots and letting `m->infinity`.

That all-moment extension is the next structural target.
