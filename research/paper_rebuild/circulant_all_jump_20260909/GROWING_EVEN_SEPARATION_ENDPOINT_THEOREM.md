# Growing defect separation and the Dirichlet endpoint law

Date: 2026-09-10

Status: **Proved**. This note belongs only to Paper I.

This result extends the fixed-separation Robin constants to separations that grow with the compressed period.

## 1. Setup

Let `L_j` be even and let

\[
h_j=2m_j,
\qquad 2\le h_j<L_j,
\]

be even defect separations. Define

\[
N_j:=\frac{L_j-h_j}{2}.
\]

Use the two-defect flux word

\[
Q_0=Q_{h_j}=1,
\qquad Q_\ell=-1\quad(\ell\ne0,h_j),
\]

and any jump

\[
s_j=L_j(2q_j+1).
\]

At `z=1` the fiber is independent of `q_j`. Let

\[
e_{L_j,h_j}:=8-\rho(H_{L_j,q_j,h_j}(1))^2.
\]

Assume

\[
\boxed{m_j\to\infty,
\qquad N_j\to\infty.}
\tag{1.1}
\]

### Theorem A — universal bulk-length law

Under (1.1),

\[
\boxed{
N_j^2 e_{L_j,h_j}
\longrightarrow\frac{\pi^2}{4}.}
\tag{1.2}
\]

Thus, once both alternating arcs are asymptotically long, the Robin constant from a fixed defect block converges to the Dirichlet value in the effective bulk coordinate.

### Corollary A.1 — proportional separation

If in addition

\[
\frac{h_j}{L_j}\longrightarrow\alpha
\qquad(0\le\alpha<1),
\]

then

\[
\boxed{
L_j^2e_{L_j,h_j}
\longrightarrow
\frac{\pi^2}{(1-\alpha)^2}.}
\tag{1.3}
\]

In particular, if

\[
h_j\to\infty,
\qquad h_j=o(L_j),
\]

then

\[
\boxed{L_j^2e_{L_j,h_j}\to\pi^2.}
\tag{1.4}
\]

---

## 2. Exact quantization equation

Write `h=2m`, `N=(L-h)/2`. From the general even-separation endpoint theorem, the top endpoint root can be written

\[
y=6+2\cos\theta,
\qquad 0<\theta<\frac\pi N,
\]

and satisfies

\[
\begin{aligned}
&T_m(2+\cos\theta)
\frac{\cos((N-\tfrac12)\theta)}{\cos(\theta/2)}\\
&\qquad-
\bigl[U_m(2+\cos\theta)+U_{m-1}(2+\cos\theta)\bigr]
\tan(\theta/2)\sin(N\theta)
=1.
\end{aligned}
\tag{2.1}
\]

The interval `0<theta<pi/N` follows from the transfer trace: at `theta=0` the left side is `T_m(3)>1`, while at `theta=pi/N` its first term is negative and the second term vanishes, so the first crossing occurs in the first oscillatory cell.

Put

\[
a=2+\cos\theta.
\]

Divide (2.1) by `T_m(a)`:

\[
\frac{\cos((N-\tfrac12)\theta)}{\cos(\theta/2)}
-
R_m(a)\tan(\theta/2)\sin(N\theta)
=\frac1{T_m(a)},
\tag{2.2}
\]

where

\[
R_m(a):=\frac{U_m(a)+U_{m-1}(a)}{T_m(a)}.
\tag{2.3}
\]

---

## 3. Uniform control of the hyperbolic defect ratio

Because `theta<pi/N` and `N->infinity`,

\[
theta\to0,
\qquad a\to3.
\]

For all sufficiently large indices, say `a>=5/2`. Write

\[
a=\cosh\eta,
\qquad \eta\ge\eta_*:=\operatorname{arcosh}(5/2)>0.
\]

Then

\[
T_m(a)=\cosh(m\eta)
\]

and

\[
U_m(a)=\frac{\sinh((m+1)\eta)}{\sinh\eta}.
\]

Hence there is an absolute constant `C_*` such that

\[
\boxed{0<R_m(a)\le C_*}
\tag{3.1}
\]

uniformly in `m>=1` and `a>=5/2`.

Moreover, since `m->infinity`,

\[
\boxed{T_m(a)\to\infty}
\tag{3.2}
\]

uniformly along the sequence.

---

## 4. Limiting quantization

Set

\[
x_j=N_j\theta_j.
\]

By the first-cell localization,

\[
0<x_j<\pi.
\]

Take any convergent subsequence,

\[
x_j\to x\in[0,\pi].
\]

The second term in (2.2) is bounded by

\[
C_*\tan(\theta_j/2)=O(\theta_j)\to0,
\]

and the right side tends to zero by (3.2). Also

\[
\frac{\cos((N_j-\tfrac12)\theta_j)}{\cos(\theta_j/2)}
\longrightarrow\cos x.
\]

Thus (2.2) gives

\[
\cos x=0.
\]

Since the root lies in the first oscillatory cell,

\[
\boxed{x=\frac\pi2.}
\tag{4.1}
\]

Every subsequence has the same limit, so

\[
\boxed{N_j\theta_j\to\frac\pi2.}
\tag{4.2}
\]

---

## 5. Gap scaling

Since

\[
e_{L_j,h_j}=2-2\cos\theta_j,
\]

we obtain

\[
N_j^2e_{L_j,h_j}
=(N_j\theta_j)^2
\frac{2-2\cos\theta_j}{\theta_j^2}
\longrightarrow\frac{\pi^2}{4},
\]

proving (1.2).

If `h_j/L_j->alpha<1`, then

\[
N_j=\frac{L_j-h_j}{2}
\]

gives

\[
\frac{L_j}{N_j}\to\frac{2}{1-\alpha}.
\]

Multiplying (1.2) by `(L_j/N_j)^2` yields (1.3). The sublinear-separation case `alpha=0` gives (1.4).

---

## 6. Interpretation

The fixed-separation theorem and the growing-separation theorem fit into one scattering picture:

- a fixed zero-potential defect block produces a Robin phase shift
  \[
  \cos\alpha_m=1/T_m(3);
  \]
- as the defect block itself becomes long, `T_m(3)->infinity`, so the Robin condition converges to Dirichlet,
  \[
  \alpha_m\to\pi/2;
  \]
- the natural geometric length controlling the endpoint gap is the number `N=(L-h)/2` of alternating bulk pairs, not the total half-period `L`.

This creates a two-parameter endpoint theory in which defect separation controls both the effective length and the boundary phase.