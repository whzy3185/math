# Exact sixth spectral moment for the compressed two-defect family

Date: 2026-09-09

Status: **Proved**. This note belongs only to Paper I.

## 1. Setup

Use the folded `L`-site two-component representation of the compressed two-defect family, with `L>=6` even. Put

\[
x:=\sin^2\beta\in[0,1],
\qquad
c^2=1-x.
\]

The generic onsite blocks are `2c sigma_x`, the two defect onsite blocks are `2 sqrt(x) sigma_y`, and the nearest-neighbor blocks are unitary Pauli blocks.

Let

\[
K:=H^2.
\]

Then the diagonal blocks of `K` are scalar:

\[
D_g=(6-4x)I_2,
\qquad
D_d=(2+4x)I_2.
\tag{1.1}
\]

The only nonzero distance-one blocks of `K` are the two generic-defect interfaces; each has Frobenius norm squared `8`. Every distance-two block is unitary and has Frobenius norm squared `2`.

---

## Theorem A — exact sixth moment

For every even `L>=6`, every odd multiplier, and every Bloch phase,

\[
\boxed{
\begin{aligned}
\operatorname{tr}H^6={}&(504L-544)
+(-912L+2112)x\\
&+(576L-768)x^2
+(-128L+512)x^3.
\end{aligned}}
\tag{1.2}
\]

### Proof

Since

\[
\operatorname{tr}H^6=\operatorname{tr}K^3,
\]

we enumerate the closed three-step walks in the block graph of `K`.

### (i) Three diagonal steps

Let

\[
a_g=6-4x,
\qquad
a_d=2+4x.
\]

The diagonal contribution is

\[
2\bigl((L-2)a_g^3+2a_d^3\bigr).
\tag{1.3}
\]

### (ii) One diagonal step and one off-diagonal edge traversed twice

For an unordered block edge `{i,j}` with block `E`, the three cyclic placements of the diagonal step contribute

\[
3(a_i+a_j)\|E\|_F^2.
\]

For the `L` distance-two unitary edges, `||E||_F^2=2`. Each site is incident to two such edges, so

\[
\sum_{\{i,j\}_{\rm dist\,2}}(a_i+a_j)
=2\sum_i a_i.
\]

Their total contribution is therefore

\[
12\bigl((L-2)a_g+2a_d\bigr).
\tag{1.4}
\]

There are two generic-defect distance-one interfaces, each with squared Frobenius norm `8`. Their contribution is

\[
48(a_g+a_d).
\tag{1.5}
\]

### (iii) Three off-diagonal steps

For `L>=8`, the off-diagonal block graph contains no relevant triangle, so there is no contribution of this type.

When `L=6`, the distance-two graph has two three-cycles, but a direct Pauli multiplication around either cycle has trace zero. Hence the same formula remains valid at `L=6`.

Adding (1.3)--(1.5) gives

\[
\begin{aligned}
\operatorname{tr}H^6={}&
2\bigl((L-2)(6-4x)^3+2(2+4x)^3\bigr)\\
&+12\bigl((L-2)(6-4x)+2(2+4x)\bigr)\\
&+48\bigl((6-4x)+(2+4x)\bigr).
\end{aligned}
\]

Expanding yields exactly (1.2).

---

## Corollary B — sixth-moment endpoint dominance

At the resonant endpoint `x=0`,

\[
\operatorname{tr}H(1)^6=504L-544.
\]

Subtracting (1.2),

\[
\boxed{
\begin{aligned}
&\operatorname{tr}H(1)^6-\operatorname{tr}H(z)^6\\
&\qquad=16x\Bigl[(57L-132)
-(36L-48)x
+(8L-32)x^2\Bigr].
\end{aligned}}
\tag{2.1}
\]

The bracket is strictly decreasing on `[0,1]` for `L>=6`, because its derivative is

\[
-(36L-48)+2(8L-32)x
\le-(20L+16)<0.
\]

Hence its minimum occurs at `x=1`, where it equals

\[
29L-116=29(L-4).
\]

Therefore, for every even `L>=6`,

\[
\boxed{
\operatorname{tr}H(z)^6
\le\operatorname{tr}H(1)^6,}
\tag{2.2}
\]

with equality if and only if

\[
x=0
\qquad\Longleftrightarrow\qquad d=2.
\]

---

## 3. Moment hierarchy so far

The endpoint now uniquely maximizes the first three even spectral moments:

\[
\boxed{
\operatorname{tr}H(z)^{2m}
\le\operatorname{tr}H(1)^{2m},
\qquad m=1,2,3,\quad L>=6.}
\]

The exact differences all contain a strict factor measuring departure from the long-phase resonance. This makes an all-even-moment theorem increasingly plausible.

If such a theorem is established, then

\[
\rho(H(z))
=\lim_{m\to\infty}\bigl(\operatorname{tr}H(z)^{2m}\bigr)^{1/(2m)}
\]

would immediately imply exact endpoint spectral-radius dominance.
