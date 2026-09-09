# Direct \(L^\infty\) upgrade via Choi's Neumann local boundedness theorem

Date: 2026-09-09
Status: **Proved / source-pinned**

## Equation to which the theorem is applied

Let
\[
q=u-\bar u_0.
\]
Since
\[
u_t=\Delta(\varphi(v)u),
\]
we have
\[
q_t-\nabla\cdot(a\nabla q)=\nabla\cdot B,
\tag{1}
\]
where
\[
a=\varphi(v),
\qquad
B=u\varphi'(v)\nabla v.
\]
The no-flux condition becomes
\[
(a\nabla q+B)\cdot\nu=0.
\tag{2}
\]
On the compact signal range \(I\),
\[
0<a_*:=\min_I\varphi\le a(x,t)\le a^*:=\max_I\varphi<\infty.
\]
Thus (1) is a scalar uniformly parabolic divergence-form equation with Neumann/conormal boundary data.

## Input estimates already proved

From the previous proof nodes,
\[
\|q(t)\|_2\le C_2e^{-\lambda_2t}
\tag{3}
\]
and
\[
\|\nabla v(t)\|_\infty\le C_ve^{-\lambda_vt}.
\tag{4}
\]
Uniform boundedness of \(u\) and bounded \(|\varphi'|\) then give
\[
\|B(t)\|_\infty
\le C_Be^{-\lambda_vt}.
\tag{5}
\]

## External theorem

Use Theorem 1.1 of:

J. Choi,
*Note on local estimates for weak solution of boundary value problem for second order parabolic equation*,
Bull. Korean Math. Soc. 53 (2016), 1123–1148,
DOI 10.4134/BKMS.b150567.

Choi treats
\[
Pu=\operatorname{div}F+f
\]
with conormal/Neumann boundary condition
\[
(A_{ij}D_ju+A_i u+F_i)n_i=0.
\]
Theorem 1.1 gives local boundedness up to the boundary. In the notation relevant here, with lower-order terms and \(f\) absent,
\[
\|q\|_{L^\infty(Q_{r/2})}
\le
C r^{-(n+2)/2}\|q\|_{L^2(Q_r)}
+
C r^{1-n/p_1-2/q_1}\|B\|_{L^{p_1,q_1}(Q_r)},
\tag{6}
\]
provided
\[
p_1>n,
\qquad q_1>2,
\qquad \frac n{p_1}+\frac2{q_1}<1.
\]

## Matching the hypotheses

Take \(A_{ij}=a\delta_{ij}\), \(A_i=B_i=C=f=0\) in Choi's operator notation, and take Choi's forcing vector \(F=B\) from (1). Uniform ellipticity follows from \(a_*\le a\le a^*\). The smooth bounded domain is a Sobolev extension domain. The conormal condition is exactly (2).

Because the lower-order coefficient quantity in Choi's theorem is zero here, a fixed admissible radius \(r_0>0\) can be chosen independently of the terminal time.

## Exponential conclusion

Fix such \(r_0\). For a backward cylinder ending at time \(t\), (3) gives
\[
\|q\|_{L^2(Q_{r_0})}
\le C e^{-\lambda_2(t-r_0^2)},
\]
and (5) gives
\[
\|B\|_{L^{p_1,q_1}(Q_{r_0})}
\le C e^{-\lambda_v(t-r_0^2)}.
\]
Since \(r_0\) is fixed, (6) yields
\[
\|q\|_{L^\infty(Q_{r_0/2})}
\le C e^{-\lambda_\infty t}
\]
for some \(\lambda_\infty>0\). Cover \(\overline\Omega\) by finitely many radius-\(r_0/2\) neighborhoods. Evaluating at the terminal time gives
\[
\boxed{
\|u(t)-\bar u_0\|_\infty
\le Ce^{-\lambda_\infty t}
}
\qquad t\ge2.
\]

This closes the final proof dependency without requiring a separate uniform Holder estimate for \(u\).
