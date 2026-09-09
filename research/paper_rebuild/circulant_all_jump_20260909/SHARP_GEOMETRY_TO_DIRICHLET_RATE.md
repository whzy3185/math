# Sharp exponential convergence of the defect-geometry constants to `pi^2`

Date: 2026-09-09

Status: **Proved**. This note belongs only to Paper I.

For fixed even defect separation `2h`, the global defect-separation theorem gives the quadratic Bloch-gap constant

\[
\kappa_h
:=4\arccos^2\!\frac1{T_h(3)}.
\]

The constants increase to `pi^2`. The present theorem gives the sharp convergence rate and the first correction terms.

## Theorem A — expansion in the Robin denominator

Put

\[
C_h:=T_h(3).
\]

Then, as `h->infinity`,

\[
\boxed{
\pi^2-\kappa_h
=\frac{4\pi}{C_h}
-\frac4{C_h^2}
+\frac{2\pi}{3C_h^3}
-\frac4{3C_h^4}
+O(C_h^{-5}).
}
\tag{1.1}
\]

In particular,

\[
\boxed{
\pi^2-\kappa_h
\sim\frac{4\pi}{T_h(3)}.
}
\tag{1.2}
\]

### Proof

Set

\[
z_h=C_h^{-1}.
\]

Since `z_h->0`,

\[
\arccos z_h
=\frac\pi2-\arcsin z_h
\]

with

\[
\arcsin z
=z+\frac{z^3}{6}+\frac{3z^5}{40}+O(z^7).
\]

Writing `a=arcsin z_h`,

\[
\kappa_h
=4\left(\frac\pi2-a\right)^2
=\pi^2-4\pi a+4a^2.
\]

Hence

\[
\pi^2-\kappa_h
=4\pi a-4a^2.
\]

Substitution of the Taylor series gives

\[
4\pi z-4z^2+\frac{2\pi}{3}z^3-\frac43z^4+O(z^5),
\]

which is (1.1).

---

## Theorem B — exact exponential rate

Let

\[
\lambda=3+2\sqrt2,
\qquad
q=\lambda^{-1}=3-2\sqrt2.
\]

Since

\[
T_h(3)=\frac{\lambda^h+\lambda^{-h}}2,
\]

we have

\[
\frac1{T_h(3)}
=\frac{2q^h}{1+q^{2h}}.
\]

Therefore

\[
\boxed{
\pi^2-\kappa_h
=8\pi q^h
-16q^{2h}
-\frac{8\pi}{3}q^{3h}
+O(q^{4h}).
}
\tag{2.1}
\]

In particular,

\[
\boxed{
\lim_{h\to\infty}
\frac{\pi^2-\kappa_h}{(3-2\sqrt2)^h}
=8\pi.
}
\tag{2.2}
\]

Thus the approach to the Dirichlet constant is exponentially fast with exact ratio `3-2sqrt2`.

### Proof

Use

\[
C_h^{-1}=2q^h-2q^{3h}+O(q^{5h})
\]

in (1.1). Keeping terms through order `q^(3h)` gives

\[
4\pi(2q^h-2q^{3h})
-4(4q^{2h})
+\frac{2\pi}{3}(8q^{3h})
+O(q^{4h}),
\]

which simplifies to (2.1).

---

## Corollary C — logarithmic width needed for a prescribed accuracy

For every sufficiently small `epsilon>0`, it is enough to choose

\[
\boxed{
h
\ge
\frac{\log(16\pi/\epsilon)}{|\log(3-2\sqrt2)|}}
\tag{3.1}
\]

(up to an absolute additive constant) to ensure

\[
\boxed{
\kappa_h>\pi^2-\epsilon.
}
\tag{3.2}
\]

Thus only logarithmic growth of the fixed defect-width parameter is required to approximate the Dirichlet constant to a prescribed accuracy at the level of the limiting geometry constant.

## Interpretation

The same hyperbolic number

\[
3-2\sqrt2
\]

now appears in two opposite parts of the theory:

1. the Robin constants approach `pi^2` at rate `(3-2sqrt2)^h` as the fixed defect width increases;
2. the above-edge bound-state excess for a fixed generic complement decays at the faster squared rate `(3-2sqrt2)^(2k)`.

This common rate is the stable multiplier of the hard transfer channel at the squared edge `8`, and gives a unified transfer-theoretic explanation of both hierarchies.