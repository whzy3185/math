# Discrete one-lattice-step transition across balanced defect geometry

Date: 2026-09-14

Status: **Proved**. This sharpens the macroscopic phase diagram in the near-balanced integer regime.

## 1. Setup

Write

\[
L=2(N+m),\qquad h=2m,
\]

and fix an integer offset

\[
j:=m-N\in\mathbb Z.
\]

Let

\[
N\to\infty,
\qquad m=N+j,
\]

with `j` fixed. For any compatible odd multiplier let

\[
\Gamma_{N,N+j,q}
:=8-\max_{|z|=1}\rho(H_{N,N+j,q}(z))^2.
\]

The endpoint/high-order results established earlier give two competing local wells:

- the periodic well near `z=1`, whose optimized gap has the expansion
  \[
  \Gamma_+(N)
  =\frac{\pi^2}{4N^2}
  -\frac{\sqrt2\pi^2}{4N^3}
  +\frac{\pi^2(66-\pi^2)}{192N^4}
  +O(N^{-5});
  \tag{1.1}
  \]
- the antiperiodic endpoint at `z=-1`, whose gap for soft length `m=N+j` is
  \[
  e_-(N+j)
  =\frac{\pi^2}{4(N+j)^2}
  -\frac{\sqrt2\pi^2}{4(N+j)^3}
  +\frac{\pi^2(72-\pi^2)}{192(N+j)^4}
  +O_j(N^{-5}).
  \tag{1.2}
  \]

The periodic formula already includes its algebraic phase-slip gain. The antiperiodic well is analytic and has no algebraic phase slip.

---

## Theorem A — exact side selection for every fixed integer offset

For every fixed integer `j`, the following holds for all sufficiently large `N`.

### (i) Negative side: `j<=-1`

If

\[
m=N+j<N,
\]

then every global maximizing phase lies in the periodic well and

\[
\boxed{
\Gamma_{N,N+j,q}=\Gamma_+(N).
}
\tag{2.1}
\]

In particular the maximizing compressed phase has the periodic phase-slip expansion.

### (ii) Balanced point: `j=0`

If

\[
m=N,
\]

then the two endpoint gaps agree to every algebraic order, but the periodic cusp lowers the global gap by

\[
\frac{\pi^2}{32N^4}+O(N^{-5}).
\]

Hence the true global optimizer is the periodic off-endpoint phase and

\[
\boxed{
\Gamma_{N,N,q}=\Gamma_+(N).
}
\tag{2.2}
\]

### (iii) Positive side: `j>=1`

If

\[
m=N+j>N,
\]

then the global maximizing phase is exactly antiperiodic:

\[
\boxed{z=-1,}
\tag{2.3}
\]

and

\[
\boxed{
\Gamma_{N,N+j,q}=e_-(N+j).
}
\tag{2.4}
\]

Thus the physical integer model changes from a phase-slipped periodic maximizer at `j=0` to exact antiperiodic locking already at the next lattice point `j=1`.

---

## 2. Gap splitting between the two wells

Expanding (1.2) in inverse powers of `N` gives

\[
\boxed{
\Gamma_+(N)-e_-(N+j)
=
\frac{\pi^2j}{2N^3}
-
\frac{\pi^2(24j^2+24\sqrt2\,j+1)}{32N^4}
+O_j(N^{-5}).
}
\tag{3.1}
\]

This single formula contains all three regimes.

If `j>=1`, the leading term in (3.1) is positive, so

\[
e_-(N+j)<\Gamma_+(N)
\]

for all large `N`. Since a smaller gap corresponds to a larger squared spectral edge, the antiperiodic well wins by order `N^-3`. The antiperiodic local locking theorem then makes `z=-1` the exact global maximizer.

If `j<=-1`, the leading term is negative, so

\[
\Gamma_+(N)<e_-(N+j).
\]

The periodic well wins by order `N^-3`; its local phase slip therefore determines the global edge.

At `j=0`, equation (3.1) becomes

\[
\Gamma_+(N)-e_-(N)
=-\frac{\pi^2}{32N^4}+O(N^{-5}),
\tag{3.2}
\]

which is exactly the periodic phase-slip gain. Hence the periodic well wins only at fourth order at the balanced lattice point.

---

## 3. Why there is no physical continuous crossover window

Suppose formally that `m=N+delta` with a real interpolation parameter `delta=o(1)`. Then (3.1) gives, at the first relevant scales,

\[
\Gamma_+(N)-e_-(N+\delta)
=
\frac{\pi^2\delta}{2N^3}
-
\frac{\pi^2}{32N^4}
+o(N^{-4}).
\tag{4.1}
\]

The formal equality of the two wells occurs at

\[
\boxed{
\delta_{\mathrm c}(N)
\sim\frac1{16N}.
}
\tag{4.2}
\]

But in the actual graph problem `delta=m-N` is an integer. For all sufficiently large `N`, the only integer inside this `O(N^-1)` crossover window is

\[
\delta=0.
\]

Thus the continuous crossover is invisible on the physical lattice: the model exhibits a one-lattice-step transition

\[
\boxed{
 j=0\;\longrightarrow\;j=1.
}
\tag{4.3}
\]

The scale separation is

\[
\text{integer imbalance cost}=\Theta(N^{-3}),
\qquad
\text{periodic cusp gain}=\Theta(N^{-4}).
\]

This is why the balanced point is isolated rather than sitting inside a broad physical crossover region.

---

## 4. Structural interpretation

The macroscopic transition is symmetric at leading Dirichlet order, but the integer lattice resolves it asymmetrically:

- on the `m<N` side the periodic avoided crossing survives;
- at `m=N` the periodic cusp wins an otherwise degenerate competition;
- on the `m>N` side a one-site excess in the defect arc already creates an `N^-3` antiperiodic advantage and destroys the periodic phase-slip competition.

Thus balance is an isolated codimension-one lattice geometry with a fourth-order spectral anomaly.