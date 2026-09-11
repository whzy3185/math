# Mass-weighted damping and a rate dichotomy for chemotaxis with signal-dependent motility

## Abstract

We consider the signal-dependent-motility system
\[
 u_t=\Delta(\varphi(v)u),\qquad
 v_t=\Delta v+uF(v)
\]
in a smooth bounded connected domain under homogeneous no-flux boundary conditions. The main observation is that the signal equation contains a mass-weighted damping mechanism which can be converted into an unweighted coercive estimate without any pointwise lower bound for the cell density. More precisely, a nonlinear mass-weighted coercivity inequality yields a rate dichotomy for equilibria satisfying
\[
 F(v_*)=0,\qquad (s-v_*)F(s)\le -\beta |s-v_*|^q,
 \qquad q\ge2.
\]
The quadratic case \(q=2\) gives exponential signal decay, whereas \(q>2\) gives the algebraic rate \(\|v(t)-v_*\|_2=O(t^{-1/(q-2)})\). If, in addition, the cell density is eventually bounded in some finite \(L^p\)-space with \(p>\max\{n,2\}\), then the decay propagates to the strong norms \(L^\infty\times W^{1,\infty}\). In the quadratic case the full stabilization is exponential; in the superquadratic case every rate
\[
0<\mu<\frac1{q-2}\min\left\{1,\frac{2(p-n)}{pn}\right\}
\]
is admissible. The stabilization argument uses only positivity of the motility on the attained signal range and no monotonicity assumption on \(\varphi\). Applications include the production--consumption model of Qin and Zheng and superlinear consumption \(v_t=\Delta v-u v^m\), for which the signal exponent \(1/(m-1)\) is attained by spatially homogeneous solutions.

**Keywords.** Chemotaxis; signal-dependent motility; production and consumption; nonlinear damping; stabilization; algebraic decay; Neumann problem.

**MSC 2020.** 35B40; 35K57; 35Q92; 92C17.

---

## 1. Introduction and main results

Signal-dependent motility provides a convenient formulation of density-suppressed migration in which the diffusivity of the cell population depends on the chemical concentration. We consider
\[
\begin{cases}
 u_t=\Delta(\varphi(v)u),\\[2mm]
 v_t=\Delta v+uF(v),
\end{cases}
\qquad x\in\Omega,\ t>0,
\tag{1.1}
\]
with homogeneous no-flux boundary conditions
\[
\partial_\nu(\varphi(v)u)=0,
\qquad
\partial_\nu v=0
\qquad\text{on }\partial\Omega\times(0,\infty),
\tag{1.2}
\]
where \(\Omega\subset\mathbb R^n\) is smooth, bounded and connected. Throughout the paper, \((u,v)\) denotes a nonnegative global classical solution with
\[
 m:=\int_\Omega u_0>0,
 \qquad
 \bar u_0:=\frac{m}{|\Omega|}.
\tag{1.3}
\]
The first equation conserves the cell mass,
\[
\int_\Omega u(x,t)\,dx=m
\qquad(t>0).
\tag{1.4}
\]

The recent work of Qin and Zheng studies the production--consumption law
\[
F(s)=1-\alpha s,
\tag{1.5}
\]
and establishes global uniform boundedness for (1.1) under an explicit structural condition on the motility. The same signal reaction appears, with a different cell flux, in the T-cell model of Tao and Winkler. On the other hand, for the direct consumption law \(F(s)=-s\), exponential stabilization in signal-dependent-motility systems was already obtained by Li and Zhao, and related stabilization results are available in the presence of logistic terms and in weak-solution settings. Thus the point of the present paper is not that stabilization is new in itself. Our aim is instead to isolate a quantitative mechanism which applies to a class of signal kinetics, to identify the transition from exponential to algebraic damping, and to show that an eventual finite \(L^p\)-bound on the cell density is enough to propagate this signal decay to uniform stabilization.

The mechanism is an elementary mass-weighted coercivity estimate. It is useful here because the reaction term naturally controls a quantity of the form
\[
\int_\Omega u|v-v_*|^q,
\]
while the cell density need not possess an eventual pointwise positive lower bound. The total mass of \(u\), together with an \(L^2\)-bound, is enough to recover coercivity.

We first state this estimate in a form which will also be used for the degenerate case. Let \(C_P\) be a Poincare constant of \(\Omega\), so that
\[
\|f-f_\Omega\|_2\le C_P\|\nabla f\|_2,
\qquad
f_\Omega:=\frac1{|\Omega|}\int_\Omega f.
\]

### Lemma 1.1 (nonlinear mass-weighted coercivity)
Let \(q\ge2\), \(\rho\ge0\),
\[
\int_\Omega\rho=m>0,
\qquad
\|\rho\|_2\le K.
\]
Then every \(f\in H^1(\Omega)\) satisfies
\[
\|f\|_2^2
\le
A\|\nabla f\|_2^2
+B_q\left(\int_\Omega\rho|f|^q\right)^{2/q},
\tag{1.6}
\]
where one may take
\[
A=C_P^2\left(1+\frac{2|\Omega|K^2}{m^2}\right),
\qquad
B_q=2|\Omega|m^{-2/q}.
\tag{1.7}
\]

The estimate (1.6) is deliberately not presented as a new functional inequality; its role is to expose the damping structure of the problem in a form that is independent of pointwise positivity of \(\rho\).

We next separate the signal mechanism from the chemotaxis equation for \(u\).

### Theorem 1.2 (mass-weighted damping rate dichotomy)
Let \(T\ge0\), \(q\ge2\), and let \(z\) solve
\[
 z_t=\Delta z+\rho(x,t)F(z),
 \qquad \partial_\nu z=0,
\tag{1.8}
\]
on \(\Omega\times(T,\infty)\). Assume that the range of \(z\) is contained in a compact interval \(I\),
\[
\rho\ge0,
\qquad
\int_\Omega\rho(\cdot,t)=m>0,
\qquad
\sup_{t\ge T}\|\rho(t)\|_2\le K,
\tag{1.9}
\]
and that, for some \(z_*\in I\) and \(\beta>0\),
\[
F(z_*)=0,
\qquad
(s-z_*)F(s)\le-\beta|s-z_*|^q
\quad(s\in I).
\tag{1.10}
\]
Then the following alternatives hold.

(i) If \(q=2\), there exist \(C,c>0\) such that
\[
\|z(t)-z_*\|_2\le Ce^{-c(t-T)}
\qquad(t\ge T).
\tag{1.11}
\]

(ii) If \(q>2\) and \(z(T)\not\equiv z_*\), then there exists \(c_q>0\), depending only on the quantities in (1.6)--(1.10) and on the compact range \(I\), such that
\[
\|z(t)-z_*\|_2
\le
\Bigl(
\|z(T)-z_*\|_2^{-(q-2)}
+(q-2)c_q(t-T)
\Bigr)^{-1/(q-2)}.
\tag{1.12}
\]
If the \(L^2\)-energy reaches zero at some time, then \(z\equiv z_*\) afterwards.

A noteworthy feature is that Theorem 1.2 does not use an evolution equation for \(\rho\). Only nonnegativity, positive mass and an \(L^2\)-bound enter the argument.

We now return to (1.1). Let \(I\) be a compact invariant interval for \(v\), and assume
\[
\varphi\in C^1(I),
\qquad
\varphi_*:=\min_I\varphi>0,
\qquad
F\in C^1(I).
\tag{1.13}
\]
No sign condition on \(\varphi'\) will be imposed in the stabilization stage.

### Theorem 1.3 (full stabilization from eventual finite \(L^p\)-control)
Assume that for some finite exponent
\[
p>\max\{n,2\}
\tag{1.14}
\]
there exist \(T\ge0\) and \(U_p>0\) such that
\[
\sup_{t\ge T}\|u(t)\|_{L^p(\Omega)}\le U_p.
\tag{1.15}
\]
Let \(v_*\in I\), \(\beta>0\), and suppose
\[
F(v_*)=0.
\tag{1.16}
\]

(a) **Quadratic damping.** If
\[
(s-v_*)F(s)\le-\beta|s-v_*|^2
\qquad(s\in I),
\tag{1.17}
\]
then there exist \(C,\lambda>0\) such that
\[
\|u(t)-\bar u_0\|_\infty
+\|v(t)-v_*\|_{W^{1,\infty}}
\le Ce^{-\lambda(t-T)}
\tag{1.18}
\]
for all \(t\ge T+2\).

(b) **Superquadratic damping.** If, for some \(q>2\),
\[
(s-v_*)F(s)\le-\beta|s-v_*|^q
\qquad(s\in I),
\tag{1.19}
\]
then
\[
\|v(t)-v_*\|_2=O\bigl((1+t-T)^{-1/(q-2)}\bigr),
\tag{1.20}
\]
and for every
\[
0<\mu<
\frac1{q-2}
\min\left\{1,\frac{2(p-n)}{pn}\right\}
\tag{1.21}
\]
one has
\[
\|u(t)-\bar u_0\|_\infty
+\|v(t)-v_*\|_{W^{1,\infty}}
=O\bigl((1+t-T)^{-\mu}\bigr).
\tag{1.22}
\]

The theorem separates assumptions needed to produce a bounded solution from assumptions needed to force relaxation. In particular, monotonicity of \(\varphi\) may be useful in a global-existence or boundedness theorem, but it is not needed in (1.17)--(1.22) once (1.13)--(1.15) are available.

Two consequences illustrate the scope of the statement.

### Corollary 1.4 (Qin--Zheng production--consumption model)
For
\[
F(s)=1-\alpha s,
\qquad \alpha>0,
\]
one has
\[
v_*=\frac1\alpha,
\qquad
(s-v_*)F(s)=-\alpha|s-v_*|^2.
\]
Hence every global classical solution of the Qin--Zheng model which satisfies their uniform boundedness conclusion converges exponentially:
\[
\|u(t)-\bar u_0\|_\infty
+\left\|v(t)-\frac1\alpha\right\|_{W^{1,\infty}}
\le Ce^{-\lambda t}
\tag{1.23}
\]
for all sufficiently large \(t\). The sign condition on \(\varphi'\) used in their boundedness theorem is not used in deriving (1.23) from boundedness.

### Corollary 1.5 (superlinear consumption)
Consider
\[
 v_t=\Delta v-u v^m,
 \qquad m>1,
\tag{1.24}
\]
on a nonnegative signal range. Then \(v_*=0\) and
\[
 vF(v)=-v^{m+1},
\]
so \(q=m+1\). Consequently,
\[
\|v(t)\|_2=O\bigl((1+t)^{-1/(m-1)}\bigr),
\tag{1.25}
\]
and under (1.14)--(1.15), for every
\[
0<\mu<
\frac1{m-1}
\min\left\{1,\frac{2(p-n)}{pn}\right\},
\tag{1.26}
\]
\[
\|u(t)-\bar u_0\|_\infty
+\|v(t)\|_{W^{1,\infty}}
=O\bigl((1+t)^{-\mu}\bigr).
\tag{1.27}
\]

The exponent in (1.25) is optimal within this class in the elementary sense that spatially homogeneous solutions attain it exactly; see Section 4.

---

## 2. Weighted coercivity and the signal rate dichotomy

We prove Lemma 1.1 first. Since
\[
\|f\|_2^2=\|f-f_\Omega\|_2^2+|\Omega||f_\Omega|^2,
\tag{2.1}
\]
it remains to control the mean. We write
\[
m f_\Omega
=\int_\Omega \rho f
+\int_\Omega\rho(f_\Omega-f).
\]
Weighted Holder and Cauchy--Schwarz give
\[
\left|\int_\Omega\rho f\right|
\le m^{1-1/q}
\left(\int_\Omega\rho|f|^q\right)^{1/q}
\tag{2.2}
\]
and
\[
\left|\int_\Omega\rho(f_\Omega-f)\right|
\le K\|f-f_\Omega\|_2
\le KC_P\|\nabla f\|_2.
\tag{2.3}
\]
Using \((a+b)^2\le2a^2+2b^2\) in (2.2)--(2.3) and then (2.1) yields exactly (1.6)--(1.7).

We next prove Theorem 1.2. Let
\[
w=z-z_*,
\qquad
E(t):=\|w(t)\|_2^2,
\]
and set
\[
G(t):=\|\nabla w(t)\|_2^2,
\qquad
D(t):=\int_\Omega\rho|w|^q.
\]
Testing (1.8) by \(w\) and using (1.10),
\[
\frac12E'(t)+G(t)+\beta D(t)\le0.
\tag{2.4}
\]
Lemma 1.1 yields
\[
E(t)\le A G(t)+B_qD(t)^{2/q}.
\tag{2.5}
\]
For \(q=2\), (2.5) immediately implies
\[
G+\beta D\ge cE
\]
with a positive constant \(c\), and (1.11) follows from (2.4).

Assume now \(q>2\). Because \(w\) ranges in a fixed compact interval, \(E(t)\) is uniformly bounded. Combining this bound with (2.5), one obtains a constant \(c_q>0\) such that
\[
G(t)+\beta D(t)\ge c_q E(t)^{q/2}.
\tag{2.6}
\]
Indeed, after replacing \(D^{2/q}\) by \(\beta^{-2/q}(\beta D)^{2/q}\), one compares separately the regimes in which \(G+\beta D\) is below or above one; the uniform upper bound on \(E\) absorbs the linear part. Hence
\[
E'(t)+2c_qE(t)^{q/2}\le0.
\tag{2.7}
\]
On intervals where \(E>0\), integration of (2.7) gives
\[
E(t)^{-(q-2)/2}
\ge
E(T)^{-(q-2)/2}
+(q-2)c_q(t-T),
\]
which is equivalent to (1.12). If \(E\) vanishes, (2.4) shows that it cannot increase again.

---

## 3. From finite \(L^p\)-control to strong signal decay

Assume (1.14)--(1.15). Since \(p>2\) and \(\Omega\) is bounded,
\[
\sup_{t\ge T}\|u(t)\|_2\le C(\Omega,p)U_p.
\tag{3.1}
\]
Thus Theorem 1.2 applies with \(\rho=u\).

Let \(w=v-v_*\). Because \(F(v_*)=0\) and \(F\in C^1(I)\),
\[
|F(v)|\le L_F|w|
\qquad\text{on }I
\tag{3.2}
\]
for \(L_F:=\max_I|F'|\). Fix \(r\in(n,p)\) and let \(s\) be determined by
\[
\frac1r=\frac1p+\frac1s.
\tag{3.3}
\]
Whenever \(s>2\), interpolation between \(L^2\) and the uniform bound furnished by the compact signal range gives
\[
\|w(t)\|_s
\le C\|w(t)\|_2^{2/s}.
\tag{3.4}
\]
Hence
\[
\|u(t)F(v(t))\|_r
\le C U_p\|w(t)\|_s.
\tag{3.5}
\]

For \(t\ge T+1\), Duhamel's formula on a fixed unit time interval and the classical Neumann heat-semigroup estimate
\[
\|\nabla e^{\tau\Delta}f\|_\infty
\le C\left(1+\tau^{-\frac12-\frac n{2r}}\right)\|f\|_r,
\qquad r>n,
\tag{3.6}
\]
yield a strong decay estimate for \(\nabla w\). The singularity in (3.6) is integrable precisely because \(r>n\).

In the quadratic case, (1.11), (3.4) and (3.5) are exponentially decaying, and therefore
\[
\|w(t)\|_{W^{1,\infty}}\le Ce^{-\lambda(t-T)}.
\tag{3.7}
\]

For \(q>2\), Theorem 1.2 gives
\[
\|w(t)\|_2\le C(1+t-T)^{-1/(q-2)}.
\tag{3.8}
\]
Equations (3.3)--(3.5) then transfer the exponent
\[
\frac{2}{(q-2)s}
=
\frac{2(p-r)}{(q-2)pr}.
\tag{3.9}
\]
Consequently, every
\[
0<\mu<\frac{2(p-r)}{(q-2)pr}
\tag{3.10}
\]
is inherited by the semigroup estimate. Optimizing the choice of \(r\) and combining this with the direct \(L^2\)-rate gives (1.21). In one space dimension, the same conclusion is obtained by the standard cylinder-lifting device, which replaces the endpoint restriction by an effective two-dimensional choice of exponents.

Finally, the spatial mean is controlled by \(\|w(t)\|_2\), and a \(W^{1,\infty}\)-Poincare estimate converts the gradient bound into the full \(W^{1,\infty}\)-bound. This proves the signal part of Theorem 1.3.

---

## 4. Cell-density stabilization and sharpness

Set
\[
q_u:=u-\bar u_0,
\qquad
\int_\Omega q_u=0.
\tag{4.1}
\]
Expanding the cell equation in divergence form gives
\[
(q_u)_t
=\nabla\cdot\bigl(\varphi(v)\nabla q_u
+u\varphi'(v)\nabla v\bigr).
\tag{4.2}
\]
Testing by \(q_u\), using \(\varphi(v)\ge\varphi_*>0\), and applying Young's inequality yields
\[
\frac12\frac d{dt}\|q_u\|_2^2
+\frac{\varphi_*}{2}\|\nabla q_u\|_2^2
\le
\frac{1}{2\varphi_*}
\|u\varphi'(v)\nabla v\|_2^2.
\tag{4.3}
\]
Since \(p>2\), (1.15) implies a uniform \(L^2\)-bound for \(u\); therefore
\[
\|u\varphi'(v)\nabla v\|_2
\le C\|\nabla v\|_\infty.
\tag{4.4}
\]
Poincare's inequality for the zero-mean function \(q_u\) then converts (4.3) into
\[
\frac d{dt}\|q_u\|_2^2+c\|q_u\|_2^2
\le C\|\nabla v\|_\infty^2.
\tag{4.5}
\]
Thus \(q_u\) inherits the exponential rate in case (a), and every algebraic rate \(\mu\) admitted in (1.21) in case (b).

To pass from \(L^2\) to \(L^\infty\), write
\[
(q_u)_t-\nabla\cdot(a(x,t)\nabla q_u)=\nabla\cdot B(x,t),
\tag{4.6}
\]
where
\[
a(x,t)=\varphi(v(x,t)),
\qquad
B(x,t)=u(x,t)\varphi'(v(x,t))\nabla v(x,t).
\tag{4.7}
\]
The boundary condition is the associated conormal condition
\[
(a\nabla q_u+B)\cdot\nu=0.
\tag{4.8}
\]
Because \(v\in I\), the coefficient \(a\) is uniformly elliptic. Choose a spatial exponent \(p_1>n\) below the available \(p\), and then a finite time exponent \(q_1>2\) such that
\[
\frac n{p_1}+\frac2{q_1}<1.
\tag{4.9}
\]
The boundary local boundedness estimate of Choi for divergence-form parabolic equations with Neumann boundary conditions applies to (4.6). On any fixed backward cylinder \(Q_R\), it gives
\[
\|q_u\|_{L^\infty(Q_{R/2})}
\le C\|q_u\|_{L^2(Q_R)}
+C\|B\|_{L^{p_1,q_1}(Q_R)},
\tag{4.10}
\]
where the powers of the fixed radius are absorbed into \(C\). The first term has the decay provided by (4.5), while the second has the same decay as \(\|\nabla v\|_\infty\) because of (1.15). A finite covering of \(\overline\Omega\) therefore yields the \(L^\infty\)-part of (1.18) and (1.22).

We close the proof section with the sharp homogeneous profile underlying (1.20). Let
\[
F(s)=-\kappa(s-v_*)|s-v_*|^\theta,
\qquad \kappa>0,
\quad \theta>0.
\tag{4.11}
\]
For spatially homogeneous data
\[
u(x,0)\equiv\bar u_0,
\qquad
v(x,0)-v_*=w_0\ne0,
\]
the pair
\[
u(x,t)\equiv\bar u_0,
\qquad
v(x,t)=v_*+w(t)
\]
solves (1.1), where
\[
w'(t)=-\kappa\bar u_0\,w(t)|w(t)|^\theta.
\]
Hence
\[
|w(t)|
=
\left(
|w_0|^{-\theta}
+\theta\kappa\bar u_0 t
\right)^{-1/\theta}.
\tag{4.12}
\]
Thus the exponent \(1/\theta\) in the signal \(L^2\)-decay cannot, in general, be improved under an order-\(2+\theta\) damping condition. For (1.24), \(\theta=m-1\), which gives the exponent in (1.25).

---

## 5. Discussion of the two principal applications

For the production--consumption model of Qin and Zheng, the invariant range is
\[
0\le v(x,t)\le
\max\left\{\|v_0\|_\infty,\frac1\alpha\right\},
\]
and their boundedness theorem provides much more than (1.15). Corollary 1.4 therefore supplies the asymptotic state and an exponential rate for the same model. The distinction between the two parts of the argument is useful: the structural assumptions on \(\varphi\) used to establish global boundedness need not reappear in the conditional stabilization mechanism. In particular, after boundedness is known, only positivity of \(\varphi\) and boundedness of \(\varphi'\) on the attained compact signal interval are used.

The direct consumption case \(F(s)=-s\) lies in the quadratic branch and overlaps with the well-developed large-time theory for signal-dependent motility. The results of Li and Zhao already include exponential convergence for this setting, and Li, Wang and Pan obtained stabilization in a logistic variant. Accordingly, the present theorem should be read as a unifying conditional principle rather than as a first stabilization theorem for signal-dependent motility.

The superlinear law (1.24) belongs to a different branch. Recent work on signal-dependent motility with superlinear consumption has concentrated primarily on global existence and weak-solution theory. Here the damping order itself determines a quantitative large-time scale, and (4.12) shows that the signal exponent appearing in (1.25) is intrinsic to the kinetics. This provides a natural interpretation of the dichotomy: a nondegenerate linearization at equilibrium produces a spectral-gap regime, while a degenerate equilibrium produces a nonlinear Bihari regime.

---

## References

1. J. Choi, *Note on local estimates for weak solution of boundary value problem for second order parabolic equation*, Bull. Korean Math. Soc. **53** (2016), 1123--1148. https://doi.org/10.4134/BKMS.b150567.

2. Y. Ke, J. Li and Y. Wang, *Chemotaxis--Fluid System*, in: **Analysis of Reaction-Diffusion Models with the Taxis Mechanism**, Springer, 2022, pp. 1--76. See in particular the standard Neumann heat-semigroup estimates collected in Lemma 1.1.

3. D. Li and J. Zhao, *Global boundedness and large time behavior of solutions to a chemotaxis--consumption system with signal-dependent motility*, Z. Angew. Math. Phys. **72** (2021), Art. 57. https://doi.org/10.1007/s00033-021-01493-y.

4. X. Li, L. Wang and X. Pan, *Boundedness and stabilization in the chemotaxis consumption model with signal-dependent motility*, Z. Angew. Math. Phys. **72** (2021), Art. 170. https://doi.org/10.1007/s00033-021-01601-y.

5. G. Li and M. Winkler, *Relaxation in a Keller--Segel-consumption system involving signal-dependent motilities*, Commun. Math. Sci. **21** (2023), 299--322.

6. W. Qin and P. Zheng, *Boundedness in a production--consumption chemotaxis model with signal-dependent motility*, Appl. Math. Lett. **180** (2026), 109995. https://doi.org/10.1016/j.aml.2026.109995.

7. Y. Tao and M. Winkler, *Stabilization in a chemotaxis system modelling T-cell dynamics with simultaneous production and consumption of signals*, Eur. J. Appl. Math. **36** (2025), 570--583. https://doi.org/10.1017/S0956792524000299.

8. Z. Zhang and Y. Li, *Global solutions to a chemotaxis system with singular density-suppressed motility and superlinear consumption*, J. Math. Anal. Appl. **541** (2025), 128711. https://doi.org/10.1016/j.jmaa.2024.128711.

---

## Editorial notes for the next manuscript pass

- Keep the contribution language structural: do not claim the first stabilization result for signal-dependent motility.
- Lead with Theorems 1.2 and 1.3, not with the Qin--Zheng corollary.
- Preserve the exact root assumption \(F(v_*)=0\) in addition to the one-sided dissipativity inequality.
- In the final AML-length version, compress Sections 2--4 but keep the proof of Lemma 1.1 explicit; it is the shortest way to make the mechanism transparent.
- The finite-\(L^p\) threshold and the algebraic exponent should remain visible in the abstract and theorem statement because they are stronger and more distinctive than the earlier boundedness-only formulation.
- Before submission freeze, perform one final forward-citation and same-author search for the 2026 Qin--Zheng article and one theorem-level comparison with the direct-consumption literature.
