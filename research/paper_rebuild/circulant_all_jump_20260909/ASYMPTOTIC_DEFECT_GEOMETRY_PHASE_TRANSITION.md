# Sharp asymptotic phase transition in the defect geometry

Date: 2026-09-10

Status: **Proved**. This note belongs only to Paper I.

This theorem identifies the sharp exponential transition scale in the general even-separation two-defect family.

## 1. Statement

Write

\[
L=2(N+m),\qquad h=2m,
\qquad N,m\ge1,
\]

and put

\[
u_N:=U_{N-1}(3).
\]

For any odd multiplier `2q+1`, let

\[
R_{N,m,q}:=\max_{|z|=1}\rho(H_{L,q,h}(z))^2.
\]

### Theorem A — sharp asymptotic geometry threshold

For every fixed `epsilon>0`, there exists `N_0(epsilon)` such that for all `N>=N_0(epsilon)`:

1. if
   \[
   \boxed{m\le(\sqrt2-\epsilon)u_N,}
   \tag{1.1}
   \]
   then for every `q>=0`,
   \[
   \boxed{R_{N,m,q}<8;}
   \tag{1.2}
   \]
2. if
   \[
   \boxed{m\ge(\sqrt2+\epsilon)u_N,}
   \tag{1.3}
   \]
   then for every `q>=0`,
   \[
   \boxed{\rho(H_{L,q,h}(-1))^2>8.}
   \tag{1.4}
   \]

Thus the global sub-eight/super-eight transition occurs on the sharp scale

\[
\boxed{m\sim\sqrt2\,U_{N-1}(3).}
\tag{1.5}
\]

Since

\[
U_{N-1}(3)
=\frac{(3+2\sqrt2)^N-(3-2\sqrt2)^N}{4\sqrt2},
\]

the equivalent leading scale is

\[
\boxed{m\sim\frac14(3+2\sqrt2)^N.}
\tag{1.6}
\]

---

## 2. The obstructed side

The exact antiperiodic theorem gives

\[
P_{N,m,-1}(8)
=4\bigl(T_N(3)^2-4m^2\bigr).
\]

The Chebyshev identity

\[
T_N(3)^2-8U_{N-1}(3)^2=1
\]

gives

\[
\frac{T_N(3)}{2u_N}
=\sqrt{2+\frac1{4u_N^2}}
\longrightarrow\sqrt2.
\tag{2.1}
\]

Hence (1.3) implies

\[
2m>T_N(3)
\]

for all sufficiently large `N`. The antiperiodic determinant is then negative, so the monic squared characteristic polynomial has a real root above `8`. This proves (1.4).

---

## 3. Reduction of the safe side to an exponentially thin boundary layer

Suppose, toward a contradiction, that the safe assertion fails. Then there are sequences

\[
N_j\to\infty,
\qquad
m_j\le(\sqrt2-\epsilon)u_{N_j},
\]

and a phase coordinate `d_j in [-2,2]` for which

\[
\mathcal F_{N_j,m_j}(d_j)\le2.
\tag{3.1}
\]

The threshold localization estimate forces

\[
d_j=-2+4t_j,
\qquad
0\le t_j<\frac1{4u_{N_j}^2}.
\tag{3.2}
\]

Define the scaled variable

\[
\xi_j=t_j u_{N_j}^2\in[0,1/4).
\tag{3.3}
\]

After passage to a subsequence,

\[
\xi_j\to\xi\in[0,1/4],
\qquad
\frac{m_j}{u_{N_j}}\to c
\]

with

\[
0\le c\le\sqrt2-\epsilon.
\tag{3.4}
\]

---

## 4. Universal boundary-layer profile

Put

\[
x_j=3-2t_j,
\qquad y_j=1+2t_j,
\]

\[
u_j=U_{N_j-1}(x_j),
\qquad p_j=U_{m_j-1}(y_j).
\]

Because `N_j t_j->0`, the positive-power representation of `U_{N-1}(3-2t)` gives

\[
\frac{u_j}{u_{N_j}}\longrightarrow1.
\tag{4.1}
\]

Write

\[
y_j=\cosh\beta_j.
\]

Since

\[
t_j=\frac{\xi_j}{u_{N_j}^2},
\]

we have

\[
u_{N_j}\beta_j\longrightarrow2\sqrt\xi.
\tag{4.2}
\]

The hyperbolic Chebyshev formula then gives

\[
\frac{p_j}{u_{N_j}}
\longrightarrow
S(c,\xi),
\tag{4.3}
\]

where

\[
S(c,\xi)=
\begin{cases}
\dfrac{\sinh(2c\sqrt\xi)}{2\sqrt\xi},&\xi>0,\\[2mm]
c,&\xi=0.
\end{cases}
\tag{4.4}
\]

The remaining mixed Chebyshev term in the compact threshold formula is lower by one power of `u_N` after normalization and tends to zero. Dividing the rescaled formula by `u_{N_j}^2` gives

\[
\boxed{
\frac{\mathcal F_{N_j,m_j}(d_j)-2}{16u_{N_j}^2}
\longrightarrow
\Phi(c,\xi),}
\tag{4.5}
\]

with

\[
\boxed{
\Phi(c,\xi)
=2+(8\xi-1)S(c,\xi)^2.}
\tag{4.6}
\]

This profile is independent of the detailed sequences.

---

## 5. Positivity of the boundary-layer profile below the critical ratio

If

\[
\xi\ge\frac18,
\]

then directly

\[
\Phi(c,\xi)\ge2.
\tag{5.1}
\]

Now suppose

\[
0\le\xi\le\frac18.
\]

Put

\[
r=2c\sqrt\xi.
\]

Since `c<=sqrt2`,

\[
0\le r\le1.
\]

For `r>0`,

\[
S(c,\xi)=c\frac{\sinh r}{r}.
\]

Hence

\[
\Phi(c,\xi)
=2+(2r^2-c^2)\left(\frac{\sinh r}{r}\right)^2.
\tag{5.2}
\]

We use the elementary inequality

\[
\boxed{
(1-r^2)\left(\frac{\sinh r}{r}\right)^2\le1
\qquad(0\le r\le1).}
\tag{5.3}
\]

To prove it, note that

\[
\frac{r}{\sqrt{1-r^2}}-\sinh r
\]

vanishes at zero and has nonnegative derivative because

\[
(1-r^2)^{-3/2}\ge e^{r^2/2}\ge\cosh r.
\]

Here `-log(1-r^2)>=r^2`, and

\[
\log\cosh r\le r^2/2
\]

because the derivative of `r^2/2-log cosh r` is `r-tanh r>=0`.

Using `c^2<=2`, (5.2)--(5.3) give

\[
\begin{aligned}
\Phi(c,\xi)-(2-c^2)
&=2r^2S_0^2-c^2(S_0^2-1)\\
&\ge2\left[r^2S_0^2-(S_0^2-1)\right]\\
&=2\left[1-(1-r^2)S_0^2\right]\ge0,
\end{aligned}
\]

where `S_0=sinh(r)/r`. Therefore

\[
\boxed{
\Phi(c,\xi)\ge2-c^2.}
\tag{5.4}
\]

By (3.4),

\[
2-c^2
\ge2-(\sqrt2-\epsilon)^2
=2\sqrt2\,\epsilon-\epsilon^2>0
\]

(after replacing `epsilon` by `min(epsilon,1)` if necessary).

Thus `Phi(c,xi)>0` in every case, contradicting (3.1) and (4.5). This proves the safe assertion.

---

## 6. Interpretation

The exact antiperiodic curve and the global safe estimate now meet asymptotically at the same constant. There is no longer a constant-factor uncertainty in the large-`N` phase diagram.

The transition scale can be written in three equivalent ways:

\[
m\sim\sqrt2 U_{N-1}(3),
\]

\[
2m\sim T_N(3),
\]

or

\[
m\sim\frac14(3+2\sqrt2)^N.
\]

The remaining open problem is finite, not asymptotic: determine whether the exact all-`N` criterion is already

\[
2m<T_N(3).
\]
