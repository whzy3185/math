# CORE_THEOREM_PROOF — boundedness implies exponential stabilization

Date: 2026-09-09

## Theorem A (current proved form)

Let \(\Omega\subset\mathbb R^n\) be a smooth bounded connected domain, let \(\alpha>0\), and let \(\varphi\in C^1([0,\infty))\) satisfy \(\varphi(s)>0\) for all \(s\ge0\). Suppose that \((u,v)\) is a nonnegative global classical solution of
\[
\begin{cases}
 u_t=\Delta(\varphi(v)u),\\
 v_t=\Delta v+u-\alpha uv,
\end{cases}
\]
with homogeneous Neumann boundary conditions, nonnegative initial data, and \(u_0\not\equiv0\). Assume only that
\[
U:=\sup_{t>0}\|u(\cdot,t)\|_{L^\infty(\Omega)}<\infty.
\]
Define
\[
\bar u_0:=\frac1{|\Omega|}\int_\Omega u_0>0.
\]
Then for every \(p\in[1,\infty)\) there exist \(C_p,\lambda_p>0\) such that
\[
\|u(\cdot,t)-\bar u_0\|_{L^p(\Omega)}
+\left\|v(\cdot,t)-\frac1\alpha\right\|_{W^{1,\infty}(\Omega)}
\le C_p e^{-\lambda_p t}
\]
for all \(t\ge1\).

In particular, the stabilization argument requires no monotonicity assumption on \(\varphi\).

## Proof

### Step 1. Mass conservation and invariant signal range

Set
\[
m:=\int_\Omega u_0>0.
\]
Integration of the first equation gives
\[
\int_\Omega u(\cdot,t)=m\qquad(t>0).
\]
Since
\[
v_t=\Delta v+u(1-\alpha v),
\]
the maximum principle yields
\[
0\le v(x,t)\le M:=\max\left\{\|v_0\|_\infty,\frac1\alpha\right\}.
\]
Hence
\[
\varphi_*:=\min_{0\le s\le M}\varphi(s)>0,
\qquad
L_\varphi:=\max_{0\le s\le M}|\varphi'(s)|<\infty.
\]

### Step 2. A uniform weighted Poincaré inequality

Let \(C_P\) be the Poincaré constant for \(\Omega\). We claim that there exists \(C_*>0\), depending only on \(\Omega,m,U\), such that for every \(t>0\) and \(f\in H^1(\Omega)\),
\[
\|f\|_2^2\le C_*\left(\|\nabla f\|_2^2+\int_\Omega u(x,t)f(x)^2\,dx\right).
\]
Indeed, with \(f_\Omega=|\Omega|^{-1}\int_\Omega f\),
\[
\begin{aligned}
m|f_\Omega|
&=\left|\int_\Omega u f_\Omega\right|\\
&\le \left|\int_\Omega u f\right|
 +\left|\int_\Omega u(f_\Omega-f)\right|\\
&\le \sqrt m\left(\int_\Omega u f^2\right)^{1/2}
 +\|u\|_2\|f-f_\Omega\|_2\\
&\le \sqrt m\left(\int_\Omega u f^2\right)^{1/2}
 +\sqrt{Um}\,C_P\|\nabla f\|_2,
\end{aligned}
\]
because \(\int u^2\le U\int u=Um\). Combining this with
\[
\|f\|_2^2\le2\|f-f_\Omega\|_2^2+2|\Omega||f_\Omega|^2
\]
proves the claim. One possible explicit choice is obtained from
\[
\|f\|_2^2
\le
\left(2C_P^2+\frac{4|\Omega|UC_P^2}{m}\right)\|\nabla f\|_2^2
+\frac{4|\Omega|}{m}\int_\Omega u f^2.
\]

### Step 3. Exponential \(L^2\)-decay of the signal

Let
\[
w:=v-\frac1\alpha.
\]
Then the second equation becomes exactly
\[
w_t=\Delta w-\alpha u w.
\]
Testing by \(w\) gives
\[
\frac12\frac d{dt}\|w\|_2^2
+\|\nabla w\|_2^2
+\alpha\int_\Omega u w^2=0.
\]
With \(\delta:=\min\{1,\alpha\}\), Step 2 gives
\[
\|\nabla w\|_2^2+\alpha\int u w^2
\ge \frac{\delta}{C_*}\|w\|_2^2.
\]
Therefore there are \(C,\lambda_0>0\) such that
\[
\|w(\cdot,t)\|_2\le Ce^{-\lambda_0t}.
\]

### Step 4. Exponential \(W^{1,\infty}\)-decay of the signal

The maximum principle from Step 1 gives a uniform \(L^\infty\)-bound for \(w\). Hence, for every \(r\ge2\), interpolation yields
\[
\|w(t)\|_r
\le \|w(t)\|_\infty^{1-2/r}\|w(t)\|_2^{2/r}
\le C_r e^{-\frac{2\lambda_0}{r}t}.
\]
Choose \(r>n\). For \(t\ge1\), Duhamel's formula on \([t-1/2,t]\) gives
\[
w(t)=e^{\frac12\Delta}w(t-1/2)
-\alpha\int_{t-1/2}^t e^{(t-s)\Delta}(u(s)w(s))\,ds.
\]
The standard Neumann heat-semigroup gradient estimate
\[
\|\nabla e^{\tau\Delta}f\|_\infty
\le C\left(1+\tau^{-\frac12-\frac n{2r}}\right)e^{-\lambda_1\tau}\|f\|_r
\]
has an integrable singularity at \(\tau=0\) because \(r>n\). Since \(\|uw\|_r\le U\|w\|_r\), it follows that
\[
\|\nabla w(t)\|_\infty\le Ce^{-\lambda_1' t}
\]
for some \(\lambda_1'>0\). Also
\[
|w_\Omega(t)|\le |\Omega|^{-1/2}\|w(t)\|_2\le Ce^{-\lambda_0t}.
\]
The \(W^{1,\infty}\)-Poincaré inequality then gives
\[
\|w(t)\|_\infty\le C\bigl(|w_\Omega(t)|+\|\nabla w(t)\|_\infty\bigr)
\le Ce^{-\lambda_vt}.
\]
Thus
\[
\left\|v(t)-\frac1\alpha\right\|_{W^{1,\infty}}
\le Ce^{-\lambda_vt}.
\]

### Step 5. Exponential \(L^2\)-decay of the cell density

Set
\[
q:=u-\bar u_0,
\qquad \int_\Omega q=0.
\]
Since \(\nabla q=\nabla u\), integration by parts gives
\[
\begin{aligned}
\frac12\frac d{dt}\|q\|_2^2
&=\int_\Omega q\,\Delta(\varphi(v)u)\\
&=-\int_\Omega\varphi(v)|\nabla q|^2
 -\int_\Omega u\varphi'(v)\nabla q\cdot\nabla v.
\end{aligned}
\]
Using Step 1 and Young's inequality,
\[
\frac12\frac d{dt}\|q\|_2^2
\le -\frac{\varphi_*}{2}\|\nabla q\|_2^2
+\frac{U^2L_\varphi^2}{2\varphi_*}\|\nabla v\|_2^2.
\]
By Step 4,
\[
\|\nabla v(t)\|_2^2\le Ce^{-2\lambda_vt}.
\]
Poincaré's inequality for the zero-mean function \(q\) therefore implies
\[
\frac d{dt}\|q\|_2^2+c\|q\|_2^2\le Ce^{-2\lambda_vt}
\]
with \(c>0\), and an ODE comparison yields
\[
\|q(t)\|_2\le Ce^{-\lambda_ut}
\]
for some \(\lambda_u>0\).

### Step 6. Every finite \(L^p\)

The assumed uniform \(L^\infty\)-bound for \(u\) gives a uniform \(L^\infty\)-bound for \(q\). Hence for every \(p\in[2,\infty)\),
\[
\|q(t)\|_p
\le \|q(t)\|_\infty^{1-2/p}\|q(t)\|_2^{2/p}
\le C_p e^{-\frac{2\lambda_u}{p}t}.
\]
For \(p\in[1,2)\), Hölder's inequality on the bounded domain gives the same conclusion with a possibly different rate/constant. This completes the proof.

## Source for the heat-semigroup estimate

A directly accessible formulation is Lemma 1.1(ii) in the Springer chapter **Chemotaxis–Fluid System** (2022): for the Neumann heat semigroup on a smooth bounded domain,
\[
\|\nabla e^{t\Delta}\omega\|_{L^p}
\le c\left(1+t^{-\frac12-\frac N2(\frac1q-\frac1p)}\right)e^{-\lambda_1t}\|\omega\|_{L^q}.
\]
That lemma cites Winkler (2010), Lemma 1.3, and Cao (2015), Lemma 2.1.

## Immediate corollary for Qin–Zheng (AML 2026)

Under the hypotheses of Qin–Zheng's boundedness theorem, their corresponding global classical solution satisfies, for every finite \(p\ge1\),
\[
\|u(t)-\bar u_0\|_{L^p}
+\left\|v(t)-\frac1\alpha\right\|_{W^{1,\infty}}
\le C_p e^{-\lambda_p t}.
\]
Their monotonicity assumption \(\varphi'<0\) is used to obtain boundedness, but is not needed by the stabilization mechanism once boundedness is available.

## Remaining optional strengthening

Upgrade \(u\)-convergence from every finite \(L^p\) to \(L^\infty\) with exponential rate. This is not needed for Theorem A above. The likely route is uniform parabolic Hölder regularity on unit time slabs plus interpolation with the proved exponential \(L^2\)-decay.
