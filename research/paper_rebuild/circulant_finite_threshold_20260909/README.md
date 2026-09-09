# Finite spectral extrema in signed step circulants

Working branch: `paper/circulant-finite-threshold-20260909`.

This directory develops the finite-global extremal problem

\[
m(N,s)=\min_\sigma\rho(A_\sigma),\qquad 2\le s<N/2,
\]

for signed adjacency matrices of `C_N(1,s)`.

## Scope boundary

This paper is completely independent of the separate periodic/Bloch project. It concerns finite graphs, minimization over **all** signings, exact equality, threshold classification, and switching/flux rigidity.

# Main proved theorem package

## 1. Complete classification through `sqrt(6)`

Let `beta` be the largest root of `x^3-7x+7=0`.

### Strictly below six

```text
N=2s+2:                         m^2=4;
(N,s)=(5,2),(10,3):             m^2=5;
N=4s:                           m^2=4+2 cos(pi/(2s));
N=14, s=3,4,5:                  m^2=4+beta.
```

These are exactly the pairs with `m(N,s)^2<6`.

### Exactly six

\[
\boxed{
 m(N,s)^2=6
 \iff
 (N,s)\in\{(12,4),(16,3),(16,5),(20,8)\}.
}
\]

The labelled minimizing switching-class counts are

\[
\boxed{2,32,32,2}
\]

and the switching-isomorphism orbit counts are

\[
\boxed{1,2,2,1}.
\]

At order 16 the 32 classes split into two size-16 Hamilton-holonomy sectors; every minimizing defect has exactly two repeated-root pairs.

### Strictly above six

Every other admissible pair satisfies

\[
\boxed{m(N,s)>\sqrt6.}
\]

In particular every odd order `N>=7` is strictly above `sqrt(6)` outside the explicitly listed sub-six exceptions, and there is no odd equality case.

## 2. How the six-boundary theorem is proved

Put `B=A^2-4I` and `K=6I-A^2=2I-B`. If `rho(A)^2<=6`, then `K` is an integral PSD Gram matrix with diagonal `2`; entries of magnitude `2` correspond to repeated/antipodal roots. Combining root quotienting, parity-defect support, and the cubic equality identity localizes every generic candidate to

\[
t=2,\qquad q=2t+1,\qquad q=2t+2,\qquad q=3t,
\]

where `q=N/gcd(N,2)` and `t=min(s,q-s)`. All four loci are closed:

- `t=2`: equality only `(12,4),(20,8)`;
- `q=2t+1`: no equality;
- `q=2t+2`: equality only `(12,4),(16,3),(16,5)`;
- `q=3t`: no component at index at most `2` for `t>=3`; `t=2` returns `(12,4)`.

## 3. Exact low-end and rigidity results

- `m(N,s)=2` iff `N=2s+2`.
- `m(N,s)=sqrt(5)` iff `(N,s)=(5,2)` or `(10,3)`.
- Outside those cases, `m(N,s)^2>=4+sqrt(2)`; equality occurs exactly at `(8,2)`.
- On `N=4s`,
  \[
  m(4s,s)^2=4+2\cos\frac{\pi}{2s},
  \]
  with exactly two labelled minimizing switching classes.
- On the flat line `N=2s+2`, `s!=3`, there are exactly two labelled equality switching classes. At `(8,3)=K_(4,4)` there are six labelled classes and one switching-isomorphism orbit.
- `m(12,2)^2=5+sqrt(3)`, with exactly two labelled minimizing switching classes.

## 4. `sqrt(8)` results: horizontal and vertical resonances

For every even `N`,

\[
m(N,s)^2\le6+2\cos\frac{2\pi}{N}<8.
\]

### Horizontal triangle resonance

On `N=3s`,

\[
\boxed{m(3s,s)<\sqrt8\iff s\text{ is even or }s\in\{3,5\}.}
\]

For odd `s>=7`,

\[
\boxed{m(3s,s)^2\ge8+\frac{2}{139}.}
\]

### New vertical resonance theorems

The positive side now contains complete fixed-step families:

\[
\boxed{m(3k,3)<\sqrt8\qquad(k\ge3),}
\]

\[
\boxed{m(5k,5)<\sqrt8\qquad(k\ge3),}
\]

and the exact step-seven threshold

\[
\boxed{m(7k,7)<\sqrt8\iff k\ge4\qquad(k\ge3).}
\]

Thus `(21,7)` is the unique non-sub-threshold member of the step-seven vertical family. The odd-order positive constructions use Hamilton seam `-1`, alternating chord signs, and a decomposition of `8I-A^2` into a signed Laplacian plus finitely many seam defects. For step three one exceptional `-2` edge is absorbed analytically by three negative two-edge paths; for steps five and seven the defects are absorbed by fixed exact local positive-definite blocks, with a finite set of exact Sylvester base cases.

These results show that the `N=3s` obstruction depends on relative resonance geometry, not merely odd order or odd chord-cycle length.

# Proof files added in the current strengthening pass

Six-boundary files:

- `SIX_BOUNDARY_ROOT_QUOTIENT.md`
- `SIX_BOUNDARY_ARITHMETIC_LOCALIZATION.md`
- `SIX_BOUNDARY_TWIN_LINE.md`
- `SIX_BOUNDARY_TRIANGLE_T2.md`
- `SIX_BOUNDARY_TRIANGLE_2TPLUS1.md`
- `SIX_BOUNDARY_TRIANGLE_3T.md`
- `SIX_BOUNDARY_MINIMIZER_RIGIDITY.md`
- `SIX_BOUNDARY_SWITCHING_ISOMORPHISM.md`

New `sqrt(8)` vertical files:

- `ODD_RESONANCE_STEP3_SUBSQRT8.md`
- `ODD_RESONANCE_STEP5_SUBSQRT8.md`
- `ODD_RESONANCE_STEP7_THRESHOLD.md`

Exact reproducibility scripts include:

- `verify_low_end_exact.py`
- `verify_sub_sqrt6_exact.py`
- `verify_six_boundary_exact.py`
- `verify_six_boundary_arithmetic.py`
- `verify_twin_line_base_exact.py`
- `verify_t2_component_local.py`
- `verify_3t_local_strip.py`
- `verify_six_boundary_minimizer_rigidity.py`
- `verify_six_boundary_orbits.py`
- `verify_step3_subsqrt8_decomposition.py`
- `verify_step5_subsqrt8_local.py`
- `verify_step7_subsqrt8_local.py`

# Current frontier

The `sqrt(6)` parameter classification and minimizer rigidity are complete. At `sqrt(8)`, both the horizontal `k=3` transition and the first three vertical fixed-step families are now controlled. The highest-value next direction is to determine the general odd-resonance phase boundary in

\[
N=ks,
\qquad k,s\text{ odd},
\]

using the same signed-Laplacian seam-defect framework; the next test cases are fixed steps `s=9,11,...` and the regime where `s` becomes comparable to `k`.
