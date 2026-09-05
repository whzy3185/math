# A polynomial spectral gap and an explicit finite comparison threshold

Date: 2026-09-05. This note strengthens the quantitative estimate in
`EVEN_JUMP_THEOREM_AND_PROOF.md`. It uses that note's proved positive
definiteness, exact determinant and nonnegative generating function.
The article at the freeze tag is unchanged.

## 1. Quantitative theorem

For every even `s>=2`, let `R_s` be the squared Bloch edge of the explicit
antipodal period-`4s` word. Then

\[
 \boxed{\frac1{2s^3}\le8-R_s\le4\sin^2\frac{\pi}{s+2}.}
\tag{1}
\]

In particular `R_s -> 8` as the even jump tends to infinity. The estimates
do not prove that the gap is of order `s^(-2)`: the two exponents still
differ. For `s>=4` the proof gives the slightly stronger lower bound
`4/(7s^3)`.

For finite orders `N=4sL`, either holonomy of the constructed word has
smaller spectral radius than either alternating-word signing whenever

\[
 \boxed{L>\pi\sqrt{\frac{s(1+s^2)}2}.}
\tag{2}
\]

This replaces the exponential sufficient threshold of the first proof by
a polynomial one. It is not claimed sharp. For `s=2`, the frozen result's
threshold `L>=4` is stronger than this common bound.

## 2. Improving the determinant lower bound

Use the notation `s=2r`, `h=xi+xi^(-1)`, `t=4-h^2`, and

\[
 a=D_{r-1}(4-h),\quad b=D_{r-1}(4+h),\quad S=S_r(t).
\]

We have `S>=4(a+b)` for `r>=2`. Monotonicity of `D_j` also gives
`h(a^2-b^2)<=0`. Consequently

\[
\begin{split}
 &(2+h)a^2+(2-h)b^2+(4-h^2)ab\\
 &=2(a+b)^2+h(a^2-b^2)-h^2ab\le2(a+b)^2.
\end{split}
\]

The exact compact determinant identity therefore implies

\[
 q_r(8,h)\ge S^2-8(a+b)^2-h^2
 \ge\frac12 S^2-4\ge\frac13S^2.
\tag{3}
\]

For the last step, `S>=2T_r(3)>=34` at `r>=2` is more than enough.
This keeps the dominant square, rather than discarding it in favor of a
small constant.

## 3. A coefficient comparison

Set `lambda=3+2sqrt(2)` and `A(w)=1-6w+w^2`. The generating function
from the first proof has the form

\[
 \sum_{j\ge0}S_j(t)w^j=B(w)G(w,t),\quad
 B(w)=\frac{1-w^2}{A(w)},\quad
 G(w,t)=\sum_{k\ge0}t^k
     \left(\frac{w(1+w)^2}{A(w)^2}\right)^k.
\]

For fixed `t>=0`, all coefficients of `G` are nonnegative. Write `B_j`
for the coefficient of `w^j` in `B`. Then

\[
 B_0=1,\qquad B_j=\lambda^j+\lambda^{-j}\quad(j\ge1).
\]

For integers `j,k>=0`,

\[
 B_{j+k}\ge\frac12\lambda^k B_j.
\]

Convolving with the nonnegative coefficients of `G` proves, for
`0<=k<=r`,

\[
 S_{r-k}(t)\le2\lambda^{-k}S_r(t).
\tag{4}
\]

Since `sum F_j w^j=(sum S_j w^j)/A(w)`, it follows that

\[
\begin{split}
 F_{r-1}(t)
 &=\sum_{j=0}^{r-1}U_j(3)S_{r-1-j}(t)\\
 &\le\frac{2r}{\lambda-\lambda^{-1}}S_r(t)
 =\frac{r}{2\sqrt2}S_r(t)\le\frac r2S_r(t).
\end{split}\tag{5}
\]

Here we used
`U_j(3)=(lambda^(j+1)-lambda^(-j-1))/(lambda-lambda^(-1))`.
The estimate is uniform in the full interval `0<=t<=4`.

## 4. Derivative bound and the inverse trace

For this section only, extend the notation to variable `y` by

\[
 F_j(y,h)=D_j(y-4-h)D_j(y-4+h),\quad
 S_r(y,h)=F_r(y,h)-6F_{r-1}(y,h)+F_{r-2}(y,h).
\]

All derivatives below are taken with respect to `y` at fixed `h`, then
evaluated at `y=8`. The root formula for the path continuant gives

\[
 \frac{D_j'(d)}{D_j(d)}
 =\sum_{k=1}^j\frac1{d-2\cos(k\pi/(j+1))}
 \le\frac{D_j'(2)}{D_j(2)}=\frac{j(j+2)}6
 \quad(d\ge2).
\]

The last equality follows as well from the positive expansion at `d=2`.
Thus `F_j' <= j(j+2)F_j/3`, and all `F_j'` are nonnegative. Dropping the
negative middle derivative in `S_r'` and using (5) yields

\[
\begin{split}
 S_r'&\le F_r'+F_{r-2}'
 \le\frac{r(r+2)}3(F_r+F_{r-2})\\
 &=\frac{r(r+2)}3(S_r+6F_{r-1})
 \le\frac{r(r+2)(1+3r)}3S_r.
\end{split}\tag{6}
\]

The compact identity

\[
 q_r(y,h)=S_r(y,h)^2
 -4\big((2+h)a(y)^2+(2-h)b(y)^2+(4-h^2)a(y)b(y)\big)-h^2
\]

holds for general `y`, by the same continuant identity used in the first
proof. At `y=8`, the subtracted expression has nonnegative derivative.
Hence `q_r'<=2S_r S_r'`. Positive definiteness of `C=8I-K_s(xi)` gives

\[
 \operatorname{tr}(C^{-1})
 =\frac{q_r'(8,h)}{q_r(8,h)}
 \le6\frac{S_r'}{S_r}
 \le2r(r+2)(1+3r)\le14r^3.
\tag{7}
\]

Since the reciprocal of the smallest positive eigenvalue is one term in
this trace,

\[
 \lambda_{\min}(C)\ge\frac1{14r^3}=\frac4{7s^3}
 \ge\frac1{2s^3}\quad(s\ge4).
\]

For `s=2`, use the exact squared edge
`eta=4+sqrt(10+2sqrt(5))`. The elementary inequalities
`sqrt(5)<5/2` and `sqrt(15)<31/8` give `eta<63/8`, so its gap exceeds
`1/8>1/(2s^3)`. This proves the lower bound in (1).

## 5. An analytic upper bound on the gap

At `xi=1`, the reduced threshold matrix `C_s(1)` contains, as a principal
submatrix on the first `r=s/2` even-chain sites, the path matrix with
diagonal `2` and off-diagonal `-1`. Its smallest eigenvalue is

\[
 2-2\cos\frac{\pi}{r+1}=4\sin^2\frac{\pi}{s+2}.
\]

Extend its sine eigenvector by zero to the remaining coordinates. The
Rayleigh principle shows that `lambda_min(C_s(1))` is at most this value.
The global Bloch gap is a minimum over phases, so it is at most the same
value. This also holds for the one-vertex path when `s=2`.

Together with the lower bound this proves (1) and `R_s -> 8`.

## 6. Finite comparison

Every finite target fiber is covered by the lower gap estimate, so

\[
 \rho(A_{s,L,\alpha})^2\le8-\frac1{2s^3}.
\]

The alternating negative-holonomy radius obeys the already proved bound

\[
 \rho(A^{\rm alt}_{N,s,-})^2\ge8-\frac{4\pi^2(1+s^2)}{N^2}.
\]

For `N=4sL`, condition (2) makes this last lower bound strictly greater
than `8-1/(2s^3)`. The positive alternating sector has squared radius
exactly `8`. This proves the stated comparison for both target and both
alternating holonomies.

## 7. Remaining sharp question

The two-sided inequality proves convergence to eight with explicit rates,
but leaves a factor of order `s` between its lower and upper gap bounds.
The conjecture `s^2(8-R_s)->pi^2` and exact location of the maximizing
phase are separate open questions. Phase-zero eigenvalues alone do not
resolve either claim. No new Lean coverage is asserted.
