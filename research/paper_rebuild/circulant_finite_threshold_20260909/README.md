# Finite spectral extrema in signed step circulants

Working branch: `paper/circulant-finite-threshold-20260909`.

This directory develops the finite-global extremal problem

\[
m(N,s)=\min_\sigma\rho(A_\sigma),\qquad 2\le s<N/2,
\]

for signed adjacency matrices of `C_N(1,s)`.

## Scope boundary

This paper is completely independent of the separate periodic/Bloch project.  It concerns finite graphs, minimization over **all** signings, exact equality, threshold classification, and switching/flux rigidity.  No continuous Bloch optimum, phase-slip asymptotic, or theorem from the other paper is used.

# Main proved theorem package

## 1. Complete classification through `sqrt(6)`

Let `beta` be the largest root of

\[
x^3-7x+7=0.
\]

The first spectral threshold is now completely classified.

### Strictly below six

\[
m(N,s)^2<6
\]

if and only if one of the following holds:

```text
N=2s+2:                         m^2=4;
(N,s)=(5,2),(10,3):             m^2=5;
N=4s:                           m^2=4+2 cos(pi/(2s));
N=14, s=3,4,5:                  m^2=4+beta.
```

### Exactly six

\[
\boxed{
 m(N,s)^2=6
 \iff
 (N,s)\in\{(12,4),(16,3),(16,5),(20,8)\}.
}
\]

The labelled minimizing switching-class counts at the four equality pairs are now also complete:

\[
\boxed{
\begin{array}{c|cccc}
(N,s)&(12,4)&(16,3)&(16,5)&(20,8)\\ \hline
\#\text{ minimizer classes}&2&32&32&2.
\end{array}}
\]

At order 16 the 32 classes all have the same characteristic polynomial

\[
x^2(x-2)(x+2)(x^2-6)^4(x^2-2)^2,
\]

and every minimizing defect has exactly two repeated-root pairs (`|B_ij|=2` above the diagonal).  Thus the order-16 equality mechanism is much less rigid than the duplicate-free order-12 and order-20 cases.

### Strictly above six

Every other admissible pair satisfies

\[
\boxed{m(N,s)>\sqrt6.}
\]

In particular the previous odd-order floor strengthens to

\[
\boxed{
N\ge7\text{ odd}\Longrightarrow m(N,s)>\sqrt6
}
\]

for every admissible `s`.

## 2. How the equality theorem is proved

Put

\[
B=A^2-4I,
\qquad
K=6I-A^2=2I-B,
\]

and, in the generic case,

\[
d=\gcd(N,2),\qquad q=N/d,\qquad t=\min(s,q-s).
\]

If `rho(A)^2<=6`, then `K` is an integral positive-semidefinite Gram matrix with diagonal `2`.  A defect entry of magnitude `2` therefore corresponds to repeated/antipodal roots.  This forces twin vertices in the parity-defect graph.  Combining this root argument with the exact parity support and the cubic boundary identity localizes every non-strict six candidate to only

\[
t=2,
\qquad q=2t+1,
\qquad q=2t+2,
\qquad q=3t.
\]

All four loci are now closed:

- `t=2`: equality only at `(12,4),(20,8)`;
- `q=2t+1`: no equality;
- `q=2t+2`: equality only at `(12,4),(16,3),(16,5)`;
- `q=3t`: no signed reduced component has index at most `2` for `t>=3`; `t=2` returns `(12,4)`.

The final `q=3t` exclusion is local: positive chord triangles are impossible; after switching all chord triangles negative, three adjacent columns form a 9-vertex signed strip.  For `t>=4` its 64 signings reduce to five exact switching/permutation types, every one having index `>2`.  The remaining `C_9(1,3)` case is excluded analytically by a singular Gram-kernel argument.

## 3. Exact low-end and rigidity results

- `m(N,s)=2` iff `N=2s+2`.
- `m(N,s)=sqrt(5)` iff `(N,s)=(5,2)` or `(10,3)`.
- Outside those cases, `m(N,s)^2>=4+sqrt(2)`; equality occurs exactly at `(8,2)`.
- On `N=4s`,
  \[
  m(4s,s)^2=4+2\cos\frac{\pi}{2s},
  \]
  with exactly two labelled minimizing switching classes.
- On the flat line `N=2s+2`, `s!=3`, there are exactly two labelled equality switching classes.  At `(8,3)=K_(4,4)` there are six labelled switching classes and one orbit after graph automorphisms.
- A separately audited small value is
  \[
  m(12,2)^2=5+\sqrt3,
  \]
  with exactly two labelled minimizing switching classes.
- At the `sqrt(6)` boundary the exact minimizer counts are `2,32,32,2` on `(12,4),(16,3),(16,5),(20,8)` respectively.

## 4. `sqrt(8)` results

For every even `N`,

\[
m(N,s)^2\le6+2\cos\frac{2\pi}{N}<8.
\]

On the triangle resonance `N=3s`,

\[
\boxed{m(3s,s)<\sqrt8\iff s\text{ is even or }s\in\{3,5\}.}
\]

For odd `s>=7`,

\[
\boxed{m(3s,s)^2\ge8+\frac{2}{139}.}
\]

The negative half uses exact `s=7,9` base certificates, an exact nine-column local rule, and analytic propagation.

# Proof files added in the current strengthening pass

- `SIX_BOUNDARY_ROOT_QUOTIENT.md`
- `SIX_BOUNDARY_ARITHMETIC_LOCALIZATION.md`
- `SIX_BOUNDARY_TWIN_LINE.md`
- `SIX_BOUNDARY_TRIANGLE_T2.md`
- `SIX_BOUNDARY_TRIANGLE_2TPLUS1.md`
- `SIX_BOUNDARY_TRIANGLE_3T.md`
- `SIX_BOUNDARY_MINIMIZER_RIGIDITY.md`

Exact reproducibility scripts include:

- `verify_low_end_exact.py`
- `verify_sub_sqrt6_exact.py`
- `verify_six_boundary_exact.py`
- `verify_six_boundary_arithmetic.py`
- `verify_twin_line_base_exact.py`
- `verify_t2_component_local.py`
- `verify_3t_local_strip.py`
- `verify_six_boundary_minimizer_rigidity.py`

All theorem labels in `THEOREM_LEDGER.md` distinguish **Proved**, **Verified**, **Observed**, and **Published/Established**.

# Current frontier

The `sqrt(6)` parameter classification **and** minimizer switching-class rigidity are no longer open.  The highest-value remaining finite-global directions are now:

1. extend the exact `sqrt(8)` classification beyond `N=3s`, especially odd resonances `N=ks`, `k>=5`;
2. seek quantitative lower gaps above `sqrt(6)` on arithmetic families outside the complete exceptional list;
3. determine whether the odd-resonance `sqrt(8)` behavior admits a finite-state classification analogous to the completed `k=3` triangle-strip theorem.
