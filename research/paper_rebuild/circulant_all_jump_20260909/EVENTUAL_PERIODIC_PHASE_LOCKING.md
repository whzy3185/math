# Eventual exact phase locking for the compressed two-defect family

Date: 2026-09-09

Status: **Proved**. This note strengthens the sharp and first-correction asymptotic results. It does not claim an explicit smallest locking threshold in `L`.

Let `L>=6` be even, `q>=0`, and let `H_{L,q}(z)` be the period-`2L` compressed two-defect Bloch fiber. Put

\[
R_{L,q}=\max_{|z|=1}\rho(H_{L,q}(z))^2.
\]

---

## Theorem A — eventual periodic-phase locking

There exists an absolute even integer `L_0` such that for every even

\[
L\ge L_0
\]

and every `q>=0`, the global Bloch edge is attained uniquely at

\[
\boxed{z=1.}
\tag{A1}
\]

Consequently, for all such `L` and all `q`,

\[
\boxed{
R_{L,q}=6+2\cos\theta_L,
}
\tag{A2}
\]

where `theta_L` is independent of `q` and is the unique solution in

\[
0<\theta_L<\frac\pi L
\]

of

\[
\boxed{
3\cos\left(\frac{L\theta_L}{2}\right)
+2\tan\left(\frac{\theta_L}{2}\right)
 \sin\left(\frac{L\theta_L}{2}\right)
=1.}
\tag{A3}
\]

Thus the odd part of the jump eventually disappears not only from the leading asymptotics but from the exact continuous Bloch edge of the compressed family.

---

## 1. Local edge as a function of independent phase variables

Let

\[
a=\arccos(1/3),
\qquad
\Gamma_0=4a^2.
\]

Near the periodic edge introduce the scaled variables

\[
y=8-\frac\gamma{L^2},
\qquad
d=2-\frac D{L^2},
\qquad
e=2-E.
\tag{1.1}
\]

Here `d` and `e` are temporarily treated as independent real variables. The exact transfer formula

\[
P(y,d,e)=0
\]

defines, for `L` sufficiently large, a unique simple top root

\[
\gamma=\gamma_L(D,E)
\]

through a fixed neighborhood of

\[
(D,E,\gamma)=(0,0,\Gamma_0).
\]

The simplicity is uniform because the limiting derivative

\[
\frac{\partial}{\partial\gamma}
\left[32-36\sin^2\left(\frac{\sqrt\gamma}{2}\right)\right]_{\gamma=\Gamma_0}
=-\frac{2\sqrt2}{a}
\]

is nonzero.

The first-correction analysis gives the uniform local expansion

\[
\boxed{
\begin{aligned}
\gamma_L(D,E)
={}&\Gamma_0+D+\frac{a}{2\sqrt2}E
+\frac{16a^2}{3L}\\
&+O\left(L^{-2}+D^2+E^2+\frac{D+E}{L}\right).
\end{aligned}}
\tag{1.2}
\]

Because the exact transfer expression and its Chebyshev representation are analytic in this neighborhood, the same expansion holds in `C^1`. Hence

\[
\boxed{
\partial_D\gamma_L(D,E)
=1+O(L^{-1}+D+E),}
\tag{1.3}
\]

and

\[
\boxed{
\partial_E\gamma_L(D,E)
=\frac{a}{2\sqrt2}+O(L^{-1}+D+E).}
\tag{1.4}
\]

Choose a fixed neighborhood

\[
0\le D,E\le\varepsilon
\]

and then choose `L_1` large enough that throughout this neighborhood

\[
\partial_D\gamma_L>\frac12,
\qquad
\partial_E\gamma_L>\frac{a}{4\sqrt2}>0.
\tag{1.5}
\]

Thus the local gap is strictly increasing in each nonnegative phase cost.

---

## 2. Global maximizers enter the monotone neighborhood

Let `z_L=e^{it_L}` be any global maximizing phase and define its physical phase variables

\[
d_L=2\cos((2q+1)t_L),
\qquad
e_L=2\cos t_L,
\]

\[
D_L=L^2(2-d_L),
\qquad
E_L=2-e_L.
\tag{2.1}
\]

The phase-rigidity theorem in `FIRST_CORRECTION_COMPRESSED_GAP.md` gives, uniformly in `q`,

\[
L D_L\to0,
\qquad
L E_L\to0.
\tag{2.2}
\]

In particular

\[
D_L\to0,
\qquad
E_L\to0.
\]

Hence every global maximizing phase lies in the monotone neighborhood (1.5) once `L` is sufficiently large, uniformly in `q`.

---

## 3. The periodic point is the unique local and global optimum

At `z=1`,

\[
d=e=2,
\qquad D=E=0.
\]

For a physical Bloch phase, always

\[
D\ge0,
\qquad E\ge0.
\]

If `z\ne1`, then `e<2`, hence

\[
E>0.
\]

Therefore, inside the neighborhood (1.5), monotonicity gives

\[
\gamma_L(D,E)>\gamma_L(0,0)
\qquad(z\ne1).
\tag{3.1}
\]

Since the squared edge is `8-gamma/L^2`, (3.1) means every nonperiodic phase has strictly smaller spectral edge than `z=1`.

But Section 2 shows that every global maximizer must lie in this neighborhood for all sufficiently large `L`. Therefore the only global maximizing phase is

\[
z=1.
\]

This proves (A1).

At `z=1`, the exact factorization and Chebyshev reduction from `QUADRATIC_COMPRESSED_GAP_THEOREM.md` give the unique top root (A2), with quantization law (A3). This proves the rest of Theorem A.

---

## 4. Consequences

### 4.1 Exact independence of the odd multiplier at large scale

For all even `L>=L_0`,

\[
R_{L,q}=R_{L,0}
\qquad\text{for every }q>=0.
\]

The compressed edge is therefore eventually a function only of the even half-period `L`.

### 4.2 Full asymptotic expansion

Equation (A3) is analytic in `1/L`. Hence the exact global gap has a complete asymptotic expansion. Writing

\[
a=\arccos(1/3),
\]

the first terms are

\[
\boxed{
8-R_{L,q}
=\frac{4a^2}{L^2}
+\frac{16a^2}{3L^3}
+\frac{4a^2(12+\sqrt2 a-3a^2)}{9L^4}
+O(L^{-5}),}
\tag{4.1}
\]

uniformly in `q`, for all sufficiently large even `L`.

Indeed the Robin variable `a_r=(L/2)theta_L` has expansion

\[
a_r
=a+\frac{a}{3r}
+\frac{a(\sqrt2 a+8)}{72r^2}
+O(r^{-3}),
\qquad r=L/2,
\]

and substitution into

\[
8-R_{L,q}=4\sin^2\left(\frac{a_r}{2r}\right)
\]

gives (4.1).

### 4.3 Contrast with the old even family

The older period-`4s` antipodal family has a genuine nonzero phase slip at its first nontrivial correction scale. The compressed two-defect family behaves differently: the periodic phase is eventually exactly selected. This gives a second structural distinction between the two mechanisms, in addition to the different leading constants

\[
\pi^2
\qquad\text{and}\qquad
4\arccos^2(1/3).
\]