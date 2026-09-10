# A full Bloch safe region: defect arc at most half the half-period

Date: 2026-09-10

Status: **Proved**. This note belongs only to Paper I.

This is the first broad sufficient region in the two-parameter even-separation phase diagram.

## 1. Parameters

Write

\[
L=2(N+m),
\qquad
h=2m,
\qquad
N,m\ge1.
\]

Thus

\[
N=\frac{L-h}{2}
\]

is the number of alternating bulk pairs and `m=h/2` is the half-length of the defect arc.

For any odd multiplier `2q+1`, set

\[
s=L(2q+1)
\]

and use the two-defect flux word

\[
Q_0=Q_h=1,
\qquad
Q_j=-1\quad(j\ne0,h).
\]

Let

\[
R_{N,m,q}:=\max_{|z|=1}\rho(H_{L,q,h}(z))^2.
\]

## Theorem A — half-period safe region

If

\[
\boxed{m\le N,}
\tag{1.1}
\]

or equivalently

\[
\boxed{h\le L/2,}
\tag{1.2}
\]

then for every `q>=0`,

\[
\boxed{R_{N,m,q}<8.}
\tag{1.3}
\]

Thus every even-separation two-defect phase whose defect arc occupies at most half of the folded half-period is globally sub-eight on the entire Bloch circle.

---

## 2. Threshold formula

Use the compact threshold formula. Put

\[
d=z^{2q+1}+z^{-(2q+1)}\in[-2,2],
\qquad
e=z+z^{-1}\le2,
\]

\[
x=\frac{4-d}{2},
\qquad
y=\frac{4+d}{2},
\]

\[
u=U_{N-1}(x),
\qquad p=U_{m-1}(y),
\]

and

\[
X=T_N(x),
\qquad Y=T_m(y).
\]

Then

\[
P_{N,m,z}(8)=\mathcal F_{N,m}(d)-e,
\]

where

\[
\begin{aligned}
\mathcal F_{N,m}(d)-2
={}&\frac{(4-d^2)(20-d^2)}2p^2u^2\\
&+2(4-d^2)XYpu\\
&+(d^2+12d+4)p^2\\
&+(d^2-8d+12)u^2.
\end{aligned}
\tag{2.1}
\]

The first two terms are nonnegative throughout `[-2,2]`, and

\[
G(d):=d^2-8d+12=(d-2)(d-6)\ge0.
\]

The only coefficient that can be negative is

\[
E(d):=d^2+12d+4.
\]

---

## 3. The dangerous phase region

If

\[
E(d)\ge0,
\]

then every term in (2.1) is nonnegative. Strict positivity follows because the four terms cannot vanish simultaneously; in particular at `d=2`,

\[
E(2)p^2=32p^2>0.
\]

It remains only to consider

\[
E(d)<0.
\tag{3.1}
\]

The unique zero of `E` in `[-2,2]` is

\[
d_*=-6+4\sqrt2<0,
\]

so (3.1) implies `d<0`. Therefore

\[
x=\frac{4-d}{2}>rac{4+d}{2}=y.
\tag{3.2}
\]

Since `x,y>=1`, Chebyshev polynomials of the second kind are increasing both in degree and in the argument on this domain. Under `m<=N`,

\[
\boxed{
u=U_{N-1}(x)\ge U_{m-1}(x)\ge U_{m-1}(y)=p.}
\tag{3.3}
\]

Now

\[
G(d)+E(d)
=2d^2+4d+16
=2\bigl((d+1)^2+7\bigr)>0.
\tag{3.4}
\]

Because `E(d)<0`, (3.3) gives

\[
\begin{aligned}
G(d)u^2+E(d)p^2
&\ge G(d)p^2+E(d)p^2\\
&=(G(d)+E(d))p^2\\
&>0.
\end{aligned}
\tag{3.5}
\]

Adding the first two nonnegative terms in (2.1), we obtain

\[
\boxed{\mathcal F_{N,m}(d)-2>0}
\]

also throughout the dangerous phase interval.

Hence

\[
\boxed{P_{N,m,z}(8)>0}
\tag{3.6}
\]

for every unit Bloch phase.

---

## 4. From the threshold determinant to the spectral edge

At `z=1`, the general endpoint theorem proves

\[
\rho(H_{L,q,h}(1))^2<8.
\]

The Hermitian Bloch fibers vary continuously around the unit circle. Equation (3.6) prevents a squared eigenvalue from crossing the threshold `8`. Therefore the inertia of

\[
8I-H_{L,q,h}(z)^2
\]

is constant along the connected Bloch circle. Since it is positive definite at `z=1`, it remains positive definite for every `z`:

\[
8I-H_{L,q,h}(z)^2>0.
\]

Thus

\[
R_{N,m,q}<8,
\]

proving Theorem A.

---

## 5. Phase-diagram consequence

The general even-separation family now has two rigorous regions:

- **safe:**
  \[
  m\le N
  \quad\Longrightarrow\quad R<8;
  \]
- **obstructed:**
  \[
  2m>T_N(3)
  \quad\Longrightarrow\quad R>8
  \]
  by the antiperiodic threshold theorem.

The unresolved region is therefore confined to

\[
\boxed{N<m<T_N(3)/2.}
\]

The exact-converse conjecture remains that the entire unresolved strip is also safe.