# Quadratic-order Bloch gap for the antipodal even-jump family

Date: 2026-09-06.

This note strengthens `../extension_20260905/POLYNOMIAL_GAP_BOUND.md` without
modifying the frozen period-eight paper.  The notation is inherited from the
all-even construction.  For even `s>=2`, let

\[
  g_s:=8-R_s,
\]

where `R_s` is the maximum squared Bloch spectral radius of the primitive
period-`4s` antipodal word.

## Main quantitative upgrade

**Theorem QG.** For every even `s>=2`,

\[
 \boxed{\frac{1}{6s(s+2)}\le g_s
 \le 4\sin^2\frac{\pi}{s+2}.}
 \tag{QG1}
\]

Consequently

\[
  g_s=\Theta(s^{-2})
\]

along the even jumps.  In particular the exponent gap in the previous bound
`1/(2s^3) <= g_s <= 4 sin^2(pi/(s+2))` is closed.

The constants in (QG1) are not claimed sharp.  The sharper conjecture

\[
  s^2 g_s\to\pi^2
\]

remains open in this note.

The upper bound is the one already proved in
`POLYNOMIAL_GAP_BOUND.md`.  Only the lower bound is new.

## 1. Threshold notation

Write `s=2r`.  For a Bloch square-root phase `xi`, put

\[
 h=\xi+\xi^{-1}\in[-2,2],\qquad t=4-h^2\in[0,4].
\]

Let

\[
 D_{-1}(d)=0,\quad D_0(d)=1,\quad
 D_j(d)=dD_{j-1}(d)-D_{j-2}(d),
\]

and, at the threshold `y=8`,

\[
 F_j(t)=D_j(4-h)D_j(4+h),\qquad
 S_r(t)=F_r(t)-6F_{r-1}(t)+F_{r-2}(t).
\]

Set

\[
 A(w)=1-6w+w^2.
\]

The previous proof established

\[
 \mathcal S(w,t):=\sum_{r\ge0}S_r(t)w^r
 =\frac{(1-w^2)A(w)}{A(w)^2-tw(1+w)^2},
 \tag{1}
\]

with all `S_r(t)>0`, and also the shift estimate, for
`0<=k<=r`,

\[
 S_{r-k}(t)\le2\lambda^{-k}S_r(t),
 \qquad \lambda=3+2\sqrt2.
 \tag{2}
\]

We reuse these proved facts.

## 2. A two-Chebyshev decomposition

Put

\[
 \Delta=\sqrt{t(t+32)},\qquad
 x_\pm=6+\frac t2\pm\frac\Delta2.
\]

For `0<=t<=4`,

\[
 2\le x_-\le6\le x_+\le14.
\]

A direct multiplication gives

\[
 A(w)^2-tw(1+w)^2
 =(1-x_+w+w^2)(1-x_-w+w^2).
 \tag{3}
\]

For `x>=2` define `B_0(x)=1` and, for `m>=1`,

\[
 B_m(x)=2T_m(x/2).
\]

Equivalently,

\[
 \frac{1-w^2}{1-xw+w^2}=\sum_{m\ge0}B_m(x)w^m.
 \tag{4}
\]

For `t>0`, set

\[
 \alpha=\frac{x_+-6}{x_+-x_-},\qquad
 \beta=\frac{6-x_-}{x_+-x_-}.
\]

Then `alpha,beta>=0`, `alpha+beta=1`, and partial fractions in (1) give

\[
 \boxed{S_m(t)=\alpha B_m(x_+)+\beta B_m(x_-).}
 \tag{5}
\]

At `t=0`, this is understood by continuity and reduces to
`S_m(0)=B_m(6)=2T_m(3)` for `m>=1`.

### Product inequality

For `x>=2`, write `x=q+q^{-1}` with `q>=1`.  Then for `m>=1`,

\[
 B_m(x)=q^m+q^{-m}.
\]

Hence, for positive integers `i,j`,

\[
 B_i(x)B_j(x)\le2B_{i+j}(x).
 \tag{6}
\]

Moreover `B_m(x)` is nondecreasing in `x` on `[2,\infty)`.
Treat `x_+` and `x_-` as a two-point random variable with probabilities
`alpha` and `beta`.  Since `B_i` and `B_j` are increasing, their covariance
is nonnegative:

\[
 \mathbb E B_i\,\mathbb E B_j
 \le \mathbb E(B_iB_j).
\]

Combining with (6) and (5) yields the uniform convolution estimate

\[
 \boxed{S_i(t)S_j(t)\le2S_{i+j}(t)}
 \qquad(i,j\ge0,\ 0\le t\le4).
 \tag{7}
\]

If one index is zero, (7) is immediate from `S_0=1`.

## 3. Exact derivative generating identity

For variable squared spectral parameter `y`, keep `h` fixed and put

\[
 d_-=y-4-h,\qquad d_+=y-4+h.
\]

The product-continuant generating function is

\[
 \sum_{j\ge0}D_j(d_-)D_j(d_+)w^j
 =\frac{1-w^2}{P(y,h;w)},
\]

where

\[
 P=1-d_-d_+w+(d_-^2+d_+^2-2)w^2-d_-d_+w^3+w^4.
\]

Thus

\[
 \mathcal S(y,h;w)=\frac{(1-w^2)A(w)}{P(y,h;w)}.
\]

At `y=8`,

\[
 \partial_yP=-8w(1-w)^2.
\]

Therefore

\[
 \boxed{
 \left.\partial_y\mathcal S(y,h;w)\right|_{y=8}
 =8w\,C(w)\,\mathcal S(w,t)^2,
 }
 \tag{8}
\]

with

\[
 C(w)=\frac{1-w}{(1+w)(1-6w+w^2)}.
\]

The coefficients of `C` are positive.  More precisely, if the Pell numbers
are

\[
 P_0=0,\quad P_1=1,\quad P_{n+1}=2P_n+P_{n-1},
\]

then

\[
 C(w)=\sum_{n\ge0}P_{n+1}^2w^n.
 \tag{9}
\]

Let `c_n=P_{n+1}^2`.  With `a=1+sqrt(2)` and `lambda=a^2`, Binet's formula
for the Pell numbers gives, for `n>=0`,

\[
 c_n\le\frac14\lambda^{n+1}.
 \tag{10}
\]

Indeed

\[
 P_m=\frac{a^m-(-a^{-1})^m}{2\sqrt2}
\]

and `1+a^{-2m}<=sqrt(2)` for `m>=1`.

## 4. The missing `O(r^2)` logarithmic derivative bound

Write

\[
 S'_r(t)=\left.\partial_yS_r(y,h)\right|_{y=8}.
\]

Extracting the coefficient of `w^r` from (8) gives

\[
 S'_r(t)=8\sum_{n=0}^{r-1}c_n
   \sum_{i+j=r-1-n}S_i(t)S_j(t).
 \tag{11}
\]

For fixed `n`, there are `r-n` ordered pairs `(i,j)` in the inner sum.
By (7),

\[
 \sum_{i+j=r-1-n}S_iS_j
 \le2(r-n)S_{r-1-n}.
\]

Apply the old shift bound (2), with `k=n+1`, and then (10):

\[
\begin{aligned}
 \frac{S'_r(t)}{S_r(t)}
 &\le32\sum_{n=0}^{r-1}(r-n)c_n\lambda^{-(n+1)}\\
 &\le8\sum_{n=0}^{r-1}(r-n)
 =4r(r+1).
\end{aligned}
\tag{12}
\]

This is the step that removes the extra factor of `r` from the previous
trace estimate.  The earlier proof bounded `S'_r` after discarding a
cancellation in the defining combination
`F_r-6F_{r-1}+F_{r-2}`; identity (8) keeps that cancellation exactly.

## 5. From the determinant to the quadratic gap

Let

\[
 C_s(\xi)=8I-K_s(\xi)>0
\]

be the reduced threshold matrix from the all-even proof, and let
`q_r(y,h)` be its characteristic determinant in the squared variable.
The previous note proved, for `r>=2`,

\[
 q_r(8,h)\ge\frac13S_r(t)^2.
 \tag{13}
\]

It also established the compact determinant identity

\[
 q_r(y,h)=S_r(y,h)^2-4E_r(y,h)-h^2,
\]

where `E_r'(8,h)>=0`.  Hence

\[
 q_r'(8,h)\le2S_r(t)S'_r(t).
\]

Since `C_s(xi)` is positive definite,

\[
 \operatorname{tr}(C_s(\xi)^{-1})
 =\frac{q_r'(8,h)}{q_r(8,h)}
 \le6\frac{S'_r(t)}{S_r(t)}
 \le24r(r+1).
 \tag{14}
\]

The reciprocal of the least eigenvalue is one positive term of this trace,
so

\[
 \lambda_{\min}(C_s(\xi))
 \ge\frac1{24r(r+1)}.
 \tag{15}
\]

This holds uniformly in the Bloch phase.  Since `s=2r`,

\[
 \lambda_{\min}(C_s(\xi))
 \ge\frac1{6s(s+2)}.
\]

Taking the minimum over phases proves the lower bound in (QG1) for
`s>=4`.  For `s=2`, the exact period-eight gap from the frozen calculation
is greater than `1/8`, hence certainly greater than `1/48`; this completes
all even `s>=2`.

## 6. Consequences and status

The explicit family now has a two-sided gap of the correct polynomial
order:

\[
 \frac1{6s(s+2)}\le8-R_s
 \le4\sin^2\frac\pi{s+2}
 \le\frac{4\pi^2}{(s+2)^2}.
\]

Thus the finite comparison threshold against the alternating signing can
also be improved by replacing the previous `s^{-3}` target gap by an
`s^{-2}` target gap.  A separate note should optimize that threshold and
track constants carefully.

This theorem does **not** prove the sharp constant `pi^2`, nor does it
assert that the maximizing Bloch phase is zero.  The latter statement is
in fact addressed separately in `PHASE_SLIP_COUNTEREXAMPLE.md`.
