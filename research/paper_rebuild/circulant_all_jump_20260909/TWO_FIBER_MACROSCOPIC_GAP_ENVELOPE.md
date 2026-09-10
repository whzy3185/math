# Macroscopic two-fiber gap envelope and balanced geometry

Date: 2026-09-10

Status: **Proved**. This is a consequence of the periodic and antiperiodic Dirichlet laws.

## 1. Setup

Let

\[
L=2(N+m),\qquad h=2m,
\]

and suppose

\[
N,m\to\infty,
\qquad
\frac hL=\frac m{N+m}\to\alpha\in(0,1).
\]

For any odd multiplier define the full Bloch gap

\[
\Gamma_{N,m,q}
:=8-\max_{|z|=1}\rho(H_{N,m,q}(z))^2.
\]

Let

\[
e^+_{N,m}:=8-\rho(H_{N,m,q}(1))^2,
\]

\[
e^-_{N,m}:=8-\rho(H_{N,m,q}(-1))^2.
\]

The two endpoint theorems give

\[
L^2e^+_{N,m}\to\frac{\pi^2}{(1-\alpha)^2},
\tag{1.1}
\]

and

\[
L^2e^-_{N,m}\to\frac{\pi^2}{\alpha^2}.
\tag{1.2}
\]

## Theorem A — two-fiber upper envelope

Under the above assumptions,

\[
\boxed{
\limsup L^2\Gamma_{N,m,q}
\le
\frac{\pi^2}{\max\{\alpha,1-\alpha\}^2}.
}
\tag{2.1}
\]

The bound is uniform with respect to the choice of odd multiplier along the sequence.

### Proof

Because the full Bloch edge is the maximum over every phase, it is at least each of the two special-fiber edges. Hence

\[
\Gamma_{N,m,q}\le e^+_{N,m}
\]

and

\[
\Gamma_{N,m,q}\le e^-_{N,m}.
\]

Therefore

\[
L^2\Gamma_{N,m,q}
\le\min\{L^2e^+_{N,m},L^2e^-_{N,m}\}.
\]

Taking the limsup and using (1.1)--(1.2),

\[
\limsup L^2\Gamma_{N,m,q}
\le
\min\left\{
\frac{\pi^2}{(1-\alpha)^2},
\frac{\pi^2}{\alpha^2}
\right\},
\]

which is exactly (2.1).

---

## Corollary B — balanced geometry uniquely maximizes the envelope

Define

\[
E(\alpha):=
\frac{\pi^2}{\max\{\alpha,1-\alpha\}^2},
\qquad0<\alpha<1.
\]

Then

\[
\boxed{
E(\alpha)\le4\pi^2,
}
\tag{3.1}
\]

with equality if and only if

\[
\boxed{\alpha=\frac12.}
\tag{3.2}
\]

Thus among macroscopic separation ratios, the only geometry not ruled out from achieving the largest possible leading full-Bloch gap is the balanced geometry

\[
h\sim\frac L2.
\]

### Proof

The quantity `max{alpha,1-alpha}` is minimized uniquely at `alpha=1/2`, where it equals `1/2`. Substitution gives (3.1)--(3.2).

---

## 4. Interpretation

The two complementary arcs play dual roles:

- the periodic fiber `z=1` sees the complementary alternating bulk `N` as the soft Dirichlet length;
- the antiperiodic fiber `z=-1` sees the defect block `m` as the soft Dirichlet length.

Consequently an unbalanced geometry always has one short soft length, and that endpoint produces a larger spectral edge, hence a smaller full-Bloch gap.

The balanced ratio equalizes the two Dirichlet obstructions. The remaining strengthening problem is to prove a matching lower bound for the full Bloch edge, which would upgrade (2.1) to an exact macroscopic gap law.