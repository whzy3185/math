# Direct \(L^\infty\) upgrade from finite \(L^p\) control

Date: 2026-09-11
Status: **Proved / source-pinned, including the one-dimensional endpoint**

## Equation to which the estimate is applied

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
The manuscript states the boundary conditions explicitly as
\[
\partial_\nu u=\partial_\nu v=0.
\]
Hence
\[
(a\nabla q+B)\cdot\nu
=\varphi(v)\partial_\nu u+u\varphi'(v)\partial_\nu v=0.
\tag{2}
\]
On the compact signal range \(I\),
\[
0<a_*:=\min_I\varphi\le a(x,t)\le a^*:=\max_I\varphi<\infty.
\]
Thus (1) is a scalar uniformly parabolic divergence-form equation with conormal boundary data.

## Inputs from the finite-\(L^p\) theorem

Assume for some finite
\[
p>\max\{n,2\}
\]
that
\[
\sup_{t\ge T}\|u(t)\|_p\le U_p.
\]
The earlier proof steps give either exponential strong signal decay or, in the degenerate case, for every admissible \(\mu\),
\[
\|\nabla v(t)\|_\infty=O((1+t-T)^{-\mu}),
\tag{3}
\]
and
\[
\|q(t)\|_2=O((1+t-T)^{-\mu}).
\tag{4}
\]
Therefore
\[
\|B(t)\|_p
\le U_p\max_I|\varphi'|\,\|\nabla v(t)\|_\infty,
\tag{5}
\]
so the forcing flux has the same rate in \(L^p\).

## Choi theorem for \(n\ge2\)

Use Theorem 1.1 of:

J. Choi,
*Note on local estimates for weak solution of boundary value problem for second order parabolic equation*,
Bull. Korean Math. Soc. 53 (2016), 1123–1148,
DOI 10.4134/BKMS.b150567.

Choi treats
\[
Pu=\operatorname{div}F+f
\]
with conormal boundary condition
\[
(A_{ij}D_ju+A_i u+F_i)n_i=0.
\]
For our equation take
\[
A_{ij}=a\delta_{ij},
\qquad A_i=B_i=C=f=0,
\qquad F=B.
\]
Choi's local boundedness estimate becomes, on a backward cylinder,
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

Set
\[
p_1=p,
\qquad
q_1=Q_*:=\frac{4p}{p-n}.
\]
Then
\[
\frac np+\frac2{Q_*}=\frac{p+n}{2p}<1.
\]
Because all lower-order coefficients vanish, the admissible radius in Choi's theorem is fixed independently of the terminal time. On fixed cylinders, the radius powers in (6) are harmless constants.

## Why \(n=1\) is also covered

Choi states Theorem 1.1 for a Sobolev extension domain in \(\mathbb R^d\) with \(d\ge2\). The manuscript keeps the natural \(n\ge1\) scope of the Qin--Zheng model by supplying the one-dimensional replacement for the only dimension-specific analytic input in Choi's De Giorgi proof.

On a bounded interval, if
\[
2\le P<\infty,
\qquad
2<Q\le\infty,
\qquad
\frac1P+\frac2Q=\frac12,
\]
then the one-dimensional Gagliardo--Nirenberg inequality gives, for every space--time cutoff \(h\),
\[
\|h\|_{L_t^Q L_x^P}
\le C\left(
\sup_\tau\|h(\tau)\|_2
+\|\partial_x h\|_{L^2_{x,t}}
\right).
\tag{7}
\]
Indeed, at each time
\[
\|h\|_P
\le C\|h_x\|_2^{2/Q}\|h\|_2^{1-2/Q}+C\|h\|_2,
\]
and raising to the \(Q\)-th power and integrating in time yields (7).

Equation (7) is precisely the one-dimensional analogue of Choi's Lemma 2.3. The other geometric ingredient, the lower measure bound
\[
|\Omega\cap B_r(x_0)|\ge cr,
\]
is automatic for an interval. In our application all lower-order terms are zero, so after replacing Lemma 2.3 by (7), the remaining De Giorgi iteration in Choi's proof of Theorem 1.1 is unchanged. Consequently (6) also holds in dimension one whenever
\[
\frac1p+\frac2{Q_*}<1,
\]
which follows from \(p>2\).

## Rate conclusion

Fix a sufficiently small radius \(r_0\in(0,1]\). For every \(t\ge T+2\), the backward cylinders of radius \(r_0\) stay inside the time region where (3)--(5) hold. Hence in the algebraic case
\[
\|q\|_{L^2(Q_{r_0})}
+\|B\|_{L^{p,Q_*}(Q_{r_0})}
=O((1+t-T)^{-\mu}),
\]
and in the quadratic case both quantities decay exponentially. The local estimate and a finite spatial covering yield
\[
\boxed{
\|u(t)-\bar u_0\|_\infty
=O((1+t-T)^{-\mu})
}
\]
in the degenerate branch and exponential decay in the quadratic branch.

This closes the final strong-norm dependency from eventual finite \(L^p\) control, without requiring a uniform \(L^\infty\) bound for \(u\), and retains the theorem for every spatial dimension \(n\ge1\).
