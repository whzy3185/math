# Enhanced theorem package for Paper I

Date: 2026-09-09

Branch: `paper/circulant-periodic-gap-20260909`

Status: current headline theorem package. This file supersedes the earlier three-layer conjectural hierarchy. The general compression theorem and its sharp global asymptotics are now proved.

The paper remains completely independent of the finite-global extremal paper. No statement below uses the minimum over all finite signings.

---

# 1. Central object

For a fixed periodic Hamilton-gauge word `tau` and jump `s`, let

\[
R_s(\tau)=\max_{|z|=1}\rho(H_{s,\tau}(z))^2
\]

be the continuous squared Bloch edge.

The paper now answers three questions:

1. what is optimal in the smallest periodic sector;
2. how short a periodic word suffices to force `R_s(tau)<8`;
3. what is the sharp gap law for the compressed arithmetic family.

---

# Theorem A — complete period-two variational theory

Among all words of period dividing two, the alternating word is the unique minimizer up to translation.

For odd `s`,

\[
\min_{\operatorname{per}(\tau)\mid2}R_s(\tau)
=8-g_s<8,
\]

where

\[
g_s=4\min_\theta
\bigl(\sin^2\theta+\cos^2(s\theta)\bigr).
\]

For even `s`,

\[
\min_{\operatorname{per}(\tau)\mid2}R_s(\tau)=8.
\]

For odd `s>=3`, the minimizing phase is unique and satisfies

\[
\sin(2\theta_s)=s\sin(2s\theta_s).
\]

Moreover

\[
g_s\downarrow0,
\qquad
s^2g_s\uparrow\pi^2.
\]

Proof: `PERIOD_TWO_VARIATIONAL_THEORY.md`.

---

# Theorem B — high-order odd asymptotics

As odd `s` tends to infinity,

\[
\theta_s=
\frac\pi{2s}-\frac\pi{2s^3}
+\frac{\pi(6+\pi^2)}{12s^5}
-\frac{\pi(\pi^4+100\pi^2+120)}{240s^7}
+O(s^{-9}),
\]

and

\[
\begin{aligned}
g_s={}&\frac{\pi^2}{s^2}
-\frac{\pi^2(\pi^2+12)}{12s^4}\\
&+\frac{\pi^2(\pi^4+120\pi^2+360)}{360s^6}\\
&-\frac{\pi^2(\pi^6+896\pi^4+18480\pi^2+20160)}{20160s^8}
+O(s^{-10}).
\end{aligned}
\]

---

# Theorem C — exact fixed period eight on `v_2(s)=1`

For every

\[
s\equiv2\pmod4,
\]

the fixed period-eight word

\[
(1,1,-1,1,-1,-1,1,-1)
\]

has the exact Bloch edge

\[
\boxed{4+\sqrt{10+2\sqrt5}<8.}
\]

Thus the whole congruence class has the uniform squared gap

\[
4-\sqrt{10+2\sqrt5}.
\]

Proof: `UNIFORM_PERIOD8_MOD4_THEOREM.md`.

---

# Theorem D — general two-defect compression

Let `L>=4` be even. On period `2L`, take the two-defect flux word

\[
Q_0=Q_2=1,
\qquad Q_j=-1\quad(j\ne0,2).
\]

For every

\[
s=L(2q+1),
\qquad q\ge0,
\]

the resulting periodic phase satisfies

\[
\boxed{R_{L,q}<8.}
\]

A completely explicit bound is

\[
\boxed{
8-R_{L,q}\ge\frac{16}{8^{L-1}}.}
\]

The proof folds the `2L`-dimensional Bloch problem to an `L`-site two-component chain and then to a fixed `4 x 4` transfer monodromy. The threshold determinant becomes

\[
P_{L,q,z}(8)=F_L(d)+d-e,
\]

and a Chebyshev monotonicity argument proves

\[
F_L(d)\ge20
\qquad(-2\le d\le2).
\]

Proof: `GENERAL_TWO_DEFECT_COMPRESSION_THEOREM.md`.

### 2-adic corollary

If

\[
2^k\Vert s,
\qquad k\ge2,
\]

choose

\[
L=2^k.
\]

Then a period

\[
\boxed{2^{k+1}}
\]

phase has Bloch edge below `8`, independently of the odd part of `s`.

Thus the period depends only on the `2`-adic scale, not on the full jump.

---

# Theorem E — signed-reflection chirality

The general two-defect lift satisfies

\[
\tau_{3-j}=-\tau_j.
\]

For every jump `s=L(2q+1)`, alternating sign times reflection gives a chiral symmetry. Fiberwise, after combining reflection with complex conjugation,

\[
\operatorname{spec}H_{L,q}(z)
=-\operatorname{spec}H_{L,q}(z).
\]

Hence

\[
\det(\lambda I-H_{L,q}(z))
=P_{L,q,z}(\lambda^2).
\]

Proof: `TWO_DEFECT_REFLECTION_CHIRAL_THEOREM.md`.

---

# Theorem F — exact two-phase characteristic equation

Put

\[
d=z^{2q+1}+z^{-(2q+1)},
\qquad
e=z+z^{-1},
\]

\[
m=\frac{L-4}{2},
\qquad
t=\frac{y-d-4}{2},
\]

\[
u=U_m(t),
\qquad
w=U_{m-1}(t).
\]

Then the full degree-`L` squared characteristic polynomial is

\[
\boxed{
P_{L,q,z}(y)
=u^2A(y,d)+uwB(y,d)+C(y,d)-e,}
\]

where

\[
A(y,d)=
(y^2-9y+14-d^2-d)
(y^2-7y+6-d^2+d),
\]

\[
B(y,d)=
-(d+y-4)(y^2-8y+4-d^2),
\]

and

\[
C(y,d)=d^2+2dy-4d+y^2-8y+6.
\]

Thus the growing Bloch matrix is reduced exactly to a two-phase Chebyshev equation.

Proof: `GENERAL_TWO_PHASE_CHARACTERISTIC_EQUATION.md`.

---

# Theorem G — exact endpoint Robin law

At `z=1`, put `r=L/2`. The top squared eigenvalue is

\[
\rho(H_{L,q}(1))^2
=6+2\cos\frac{x_r}{r},
\]

where `x_r in (0,pi/2)` is the unique solution of

\[
\boxed{
3\cos x_r+2\tan\frac{x_r}{2r}\sin x_r=1.}
\]

If

\[
x_0=\arccos(1/3),
\]

then

\[
\boxed{
L^2\bigl(8-\rho(H_{L,q}(1))^2\bigr)
\to4x_0^2.}
\]

The endpoint gap has the expansion

\[
\begin{aligned}
e_L={}&\frac{4x_0^2}{L^2}
+\frac{16x_0^2}{3L^3}\\
&+\frac{4x_0^2}{9L^4}
(-3x_0^2+\sqrt2\,x_0+12)
+O(L^{-5}).
\end{aligned}
\]

Proof: `COMPRESSED_ENDPOINT_SHARP_GAP.md`.

---

# Theorem H — uniform global sharp compressed gap

Let

\[
\Gamma_{L,q}=8-R_{L,q}.
\]

For **every** sequence of even `L->infinity` and **every** sequence `q=q(L)>=0`,

\[
\boxed{
L^2\Gamma_{L,q}
\longrightarrow
4\arccos(1/3)^2.}
\]

Thus the sharp compressed gap is uniform in the odd multiplier.

If `z_{L,q}` is any maximizing phase and

\[
d_{L,q}=z_{L,q}^{2q+1}+z_{L,q}^{-(2q+1)},
\qquad
e_{L,q}=z_{L,q}+z_{L,q}^{-1},
\]

then

\[
\boxed{e_{L,q}\to2,}
\]

and

\[
\boxed{L^2(2-d_{L,q})\to0.}
\]

The proof excludes hyperbolic near-edge roots and shows that every elliptic near-edge root satisfies the universal limiting Robin equation

\[
36\sin^2x=34-e.
\]

The endpoint upper bound then forces

\[
x=\arccos(1/3),\qquad e=2.
\]

Proof: `GLOBAL_COMPRESSED_SHARP_GAP.md`.

### 2-adic sharp-gap corollary

For `2^k || s`, `k>=2`, choose `L=2^k`. Then, as `k->infinity`, uniformly in the odd part of `s`,

\[
\boxed{
8-R_s
\sim
\frac{4\arccos(1/3)^2}{4^k}.}
\]

This is the sharp arithmetic compression law.

---

# Theorem I — eventual endpoint locking for a fixed odd multiplier

Fix `q`, equivalently fix the odd multiplier `n=2q+1`. Then there exists `L_0(q)` such that for every even `L>=L_0(q)`,

\[
\boxed{
R_{L,q}=\rho(H_{L,q}(1))^2.}
\]

Thus the global gap eventually equals the endpoint gap exactly and inherits the full expansion in Theorem G.

The proof combines global phase rigidity with a rescaled local `C^2` law

\[
r^2(8-y(\psi/r))
=x_0^2+n^2\psi^2+O(r^{-1}),
\]

which gives strict endpoint convexity for large `L`.

Proof: `FIXED_ODD_MULTIPLIER_ENDPOINT_DOMINANCE.md`.

---

# Theorem J — old all-jump family remains as an asymptotic comparison family

The previously proved parity-dependent family remains mathematically useful:

- period two for odd `s`;
- period `4s` antipodal phase for even `s`.

For that family,

\[
s^2\widehat g_s\to\pi^2,
\]

and the audited even phase-slip theorem remains valid.

However, it is no longer the strongest existence theorem for even jumps. The compressed family is strictly shorter and has the sharper arithmetic gap scale controlled by `v_2(s)`.

The old family should therefore be presented as a comparison/asymptotic model rather than the headline even-jump construction.

---

# Current paper-level thesis

The strongest current thesis is:

> periodic spectral improvement in signed step circulants is governed by an arithmetic compression mechanism. Period two exhibits an exact parity bifurcation; a two-defect signed-reflection phase compresses every even jump to a period controlled only by its 2-adic scale; the compressed Bloch problem has an exact two-phase transfer equation and a sharp universal Robin gap constant; and the older long-period family exhibits a different phase-slip asymptotic mechanism.

The manuscript now contains four distinct kinds of mathematics:

1. exact variational classification;
2. structural chirality and transfer compression;
3. arithmetic/2-adic period reduction;
4. sharp global asymptotics and endpoint locking.

---

# Main remaining strengthening target

The strongest numerically supported finite statement still open is:

\[
\boxed{
L\ge6
\quad\Longrightarrow\quad
z=1\text{ is globally maximizing for every odd multiplier}.}
\]

The exact two-phase characteristic equation reduces this to a one-variable positivity problem at the endpoint root. This is now the main finite-strengthening target.
