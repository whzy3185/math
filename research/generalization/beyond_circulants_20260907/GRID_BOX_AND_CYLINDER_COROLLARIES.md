# Grid boxes and cylindrical products

Date: 2026-09-07.

Let `P_m` denote a path on `m` vertices.  Since a tree has only one switching
class, every signed `P_m` is switching-equivalent to the positive path and

\[
\rho(P_m)=2\cos\frac\pi{m+1}.
\]

Combining paths with antiperiodically signed even cycles in the Clifford
product theorem gives explicit formulas for boxes, cylinders and mixed
Cartesian grids.

## Theorem GBC

Let

\[
G=\left(\square_{i=1}^p P_{m_i}\right)
\square
\left(\square_{j=1}^q C_{n_j}\right),
\]

where every `n_j>=4` is even.  There is an explicit signing of `G` with

\[
\boxed{
\rho(G,\sigma)^2=
4\sum_{i=1}^p\cos^2\frac\pi{m_i+1}
+4\sum_{j=1}^q\cos^2\frac\pi{n_j}.}
\tag{1}
\]

The signing is obtained by taking the positive path adjacency in each path
coordinate, an antiperiodic signing in every cycle coordinate, and inserting
bipartition parity strings in all earlier tensor coordinates.

### Examples

1. Rectangle `P_m square P_n`:
   \[
   \rho^2=4\cos^2\frac\pi{m+1}+4\cos^2\frac\pi{n+1}.
   \]
2. Cylinder `P_m square C_n`, `n` even:
   \[
   \rho^2=4\cos^2\frac\pi{m+1}+4\cos^2\frac\pi n.
   \]
3. Three-dimensional box `P_a square P_b square P_c`:
   \[
   \rho^2=4\sum_{x\in\{a,b,c\}}\cos^2\frac\pi{x+1}.
   \]

These are constructive upper bounds on the minimum signed spectral radius;
no general optimality claim is made except in flat factor cases covered by
`GENERAL_CLIFFORD_PRODUCT_THEOREM.md`.

## Asymptotic form

When all dimensions grow,

\[
\rho^2=4(p+q)
-4\pi^2\left(
\sum_i(m_i+1)^{-2}+\sum_j n_j^{-2}
\right)
+O\left(\sum_i(m_i+1)^{-4}+\sum_jn_j^{-4}\right).
\]

Thus the same `pi^2` constant that appeared in the one-dimensional circulant
boundary layer reappears additively, coordinate by coordinate, in Cartesian
product geometry.
