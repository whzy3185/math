# Multiplier-uniform eventual endpoint locking

Date: 2026-09-09

Status: **Proved**. This note belongs only to Paper I.

This theorem strengthens `FIXED_ODD_MULTIPLIER_ENDPOINT_DOMINANCE.md`: the threshold in the endpoint-locking theorem can be chosen independently of the odd multiplier of the jump.

## 1. Statement

Let `L>=4` be even and consider the period-`2L` compressed two-defect phase with jump

\[
s=L(2q+1),\qquad q\ge0.
\]

Let

\[
R_{L,q}=\max_{|z|=1}\rho(H_{L,q}(z))^2
\]

and let

\[
e_L=8-\rho(H_{L,q}(1))^2
\]

be the endpoint gap, which is independent of `q`.

### Theorem A — uniform eventual exact locking

There exists an absolute even integer `L_0` such that for every even

\[
L\ge L_0
\]

and every `q>=0`, the global Bloch edge is attained uniquely at

\[
\boxed{z=1.}
\]

Equivalently,

\[
\boxed{
R_{L,q}=\rho(H_{L,q}(1))^2,
\qquad
8-R_{L,q}=e_L
}
\tag{1.1}
\]

for all such `(L,q)`.

In particular, the full endpoint expansion is then the global expansion uniformly over all odd multipliers:

\[
\begin{aligned}
8-R_{L,q}={}&\frac{4x_0^2}{L^2}
+\frac{16x_0^2}{3L^3}\\
&+\frac{4x_0^2}{9L^4}
\bigl(-3x_0^2+\sqrt2\,x_0+12\bigr)
+O(L^{-5}),
\end{aligned}
\tag{1.2}
\]

where

\[
x_0=\arccos(1/3).
\]

The threshold `L_0` is not optimized in this note.

---

## 2. Relaxed endpoint characteristic function

Write

\[
L=2r
\]

and put

\[
y_L:=8-e_L.
\]

For the exact two-phase characteristic equation, write

\[
d=2-\mu,
\qquad 0\le\mu\le4,
\qquad e=z+z^{-1}\le2.
\]

At the fixed spectral value `y=y_L`, define the relaxed characteristic function by replacing the basic Bloch coordinate by its largest possible value `e=2`:

\[
\mathcal P_r(\mu)
:=P_{L,q,z}(y_L)\big|_{d=2-\mu,\ e=2}.
\tag{2.1}
\]

The exact characteristic equation depends on `q` only through `(d,e)`, so `mathcal P_r` is independent of `q`.

For a physical phase with the same value of `d`,

\[
P_{L,q,z}(y_L)
=\mathcal P_r(\mu)+(2-e)
\ge\mathcal P_r(\mu).
\tag{2.2}
\]

At the endpoint,

\[
\mathcal P_r(0)=0.
\tag{2.3}
\]

Thus it is enough to prove that, for all sufficiently large `r`,

\[
\boxed{
\mathcal P_r(\mu)>0
\qquad(0<\mu\le4).
}
\tag{2.4}
\]

---

## 3. The natural scaled phase variable

Define

\[
M=r^2\mu
\]

and

\[
G_r=r^2e_L.
\]

The sharp endpoint theorem gives

\[
G_r\longrightarrow x_0^2.
\tag{3.1}
\]

At `y=y_L`, the transfer parameter is

\[
t=\frac{y_L-d-4}{2}
=1+\frac{\mu-e_L}{2}
=1+\frac{M-G_r}{2r^2}.
\tag{3.2}
\]

Hence the sign of `M-G_r` distinguishes the elliptic and hyperbolic sides of the same endpoint root.

For bounded `M`, the standard Chebyshev scaling is uniform, including one derivative with respect to `M` on compact intervals:

- if `M<G_r`, set
  \[
  x=\sqrt{G_r-M}+o(1),
  \]
  so that
  \[
  U_{r-j}(t)/r\to\sin x/x;
  \]
- if `M>G_r`, set
  \[
  \kappa=\sqrt{M-G_r}+o(1),
  \]
  so that
  \[
  U_{r-j}(t)/r\to\sinh\kappa/\kappa.
  \]

Substitution into the exact two-phase characteristic equation yields the following locally uniform `C^1` limit for

\[
\widehat{\mathcal P}_r(M):=
\mathcal P_r(M/r^2).
\]

### Lemma B — universal endpoint comparison profile

On every compact interval `0<=M<=M_1`,

\[
\widehat{\mathcal P}_r(M)
\longrightarrow \mathcal F(M)
\]

locally uniformly with one derivative, where

\[
\boxed{
\mathcal F(M)=
\begin{cases}
32-36\sin^2\!\sqrt{x_0^2-M},
&0\le M\le x_0^2,\\[1mm]
32+36\sinh^2\!\sqrt{M-x_0^2},
&M\ge x_0^2.
\end{cases}}
\tag{3.3}
\]

At the joining point the two formulas have the common value `32` and common derivative `36`, so `mathcal F` is `C^1` there.

#### Proof

This is the same elliptic/hyperbolic Chebyshev scaling used in `GLOBAL_COMPRESSED_SHARP_GAP.md`, but now the squared spectral value is fixed at the endpoint `y_L` rather than at an unknown maximizing root.

On the elliptic side, `h=e_L-mu`, so

\[
r^2h\to x_0^2-M.
\]

The coefficient expansion in the exact characteristic equation gives

\[
\widehat{\mathcal P}_r(M)
=32-36\sin^2\sqrt{x_0^2-M}+o(1).
\]

On the hyperbolic side, `delta=mu-e_L`, so

\[
r^2\delta\to M-x_0^2,
\]

and the hyperbolic expansion gives

\[
\widehat{\mathcal P}_r(M)
=32+36\sinh^2\sqrt{M-x_0^2}+o(1).
\]

The standard differentiated Chebyshev formulas are uniform on compact scaled intervals, giving the `C^1` form. No multiplier enters the calculation.

---

## 4. Strict positivity of the limiting profile

The function `mathcal F` satisfies

\[
\boxed{
\mathcal F(0)=0,
\qquad
\mathcal F(M)>0\quad(M>0).
}
\tag{4.1}
\]

In fact it is strictly increasing on `[0,infinity)`.

For `0<M<x_0^2`, put `x=sqrt(x_0^2-M)`. Then

\[
\mathcal F'(M)
=18\frac{\sin(2x)}{x}>0.
\tag{4.2}
\]

For `M>x_0^2`, put `kappa=sqrt(M-x_0^2)`. Then

\[
\mathcal F'(M)
=18\frac{\sinh(2\kappa)}{\kappa}>0.
\tag{4.3}
\]

At `M=0`,

\[
\boxed{
\mathcal F'(0)
=\frac{8\sqrt2}{x_0}>0.
}
\tag{4.4}
\]

Thus the endpoint is not merely a limiting root: it is the unique zero of the universal comparison profile.

---

## 5. Positivity for all scaled phases

We prove (2.4) by contradiction.

Suppose there exist even `r_j->infinity` and `mu_j>0` such that

\[
\mathcal P_{r_j}(\mu_j)\le0.
\]

Put

\[
M_j=r_j^2\mu_j.
\]

### Case 1: `M_j` is bounded away from zero and bounded above

After passing to a subsequence,

\[
M_j\to M>0.
\]

Lemma B gives

\[
\mathcal P_{r_j}(\mu_j)
\to\mathcal F(M)>0,
\]

a contradiction.

### Case 2: `M_j->0`

Choose `epsilon>0` so small that

\[
\mathcal F'(M)\ge\frac12\mathcal F'(0)>0
\]

on `[0,epsilon]`. By the `C^1` convergence in Lemma B, for all sufficiently large `j`,

\[
\widehat{\mathcal P}_{r_j}'(M)>0
\qquad(0\le M\le\epsilon).
\]

Since

\[
\widehat{\mathcal P}_{r_j}(0)=0,
\]

we obtain

\[
\widehat{\mathcal P}_{r_j}(M_j)>0,
\]

again a contradiction.

### Case 3: `M_j->infinity`

Then eventually

\[
\delta_j:=\mu_j-e_{L_j}>0
\]

and

\[
r_j^2\delta_j=M_j-G_{r_j}\to\infty.
\]

The nonasymptotic hyperbolic estimate from the proof of the global sharp-gap theorem applies verbatim at the fixed value `g=e_L`: for `t>=1`,

\[
u\ge w\ge0,
\qquad u\ge r-1,
\]

and the coefficient combinations satisfy, once `delta/e_L` is large,

\[
\min(A,A+B)\ge c\delta
\]

for an absolute `c>0`. Hence

\[
u^2A+uwB\ge c(r-1)^2\delta\to\infty,
\]

whereas `C-2` stays bounded below. Thus

\[
\mathcal P_{r_j}(\mu_j)\to+\infty,
\]

a contradiction.

All possibilities are excluded, proving (2.4) for every sufficiently large `r`.

---

## 6. From determinant positivity to exact edge dominance

Fix such a large `L`.

If a physical Bloch phase has `d<2`, then (2.2) and (2.4) give

\[
P_{L,q,z}(y_L)>0.
\tag{6.1}
\]

If `d=2` but `z\ne1`, then

\[
P_{L,q,z}(y_L)=2-e>0.
\tag{6.2}
\]

Thus

\[
P_{L,q,z}(y_L)>0
\qquad(z\ne1),
\tag{6.3}
\]

while `P_(L,q,1)(y_L)=0` and the endpoint top squared root is simple.

For phases sufficiently close to `z=1`, continuity keeps the second squared root below `y_L`; (6.3) then forces the simple top root to lie below `y_L`. On the punctured Bloch circle `|z|=1, z\ne1`, the number of squared roots in `(y_L,8)` can change only if a root crosses `y_L` or `8`. Equation (6.3) prevents the former, while the general compression theorem gives `P(8)>0` and prevents the latter. Since the punctured circle is connected, the number is identically zero.

Therefore

\[
\rho(H_{L,q}(z))^2<y_L
\qquad(z\ne1),
\]

and equality holds at `z=1`. This proves Theorem A and its uniqueness statement.

## 7. Consequences

1. The earlier fixed-multiplier endpoint theorem is strictly strengthened: the locking threshold is universal in `q`.
2. The odd part of the jump eventually disappears not only from the leading gap constant but from the exact maximizing Bloch phase.
3. Any possible finite-`L` phase-slip phenomenon is confined to a finite set of compressed half-periods.
4. The remaining finite problem is now sharply isolated: determine the smallest universal locking threshold, with computation suggesting `L_0=6`.