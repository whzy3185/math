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

The labelled minimizing switching-class counts are `2,32,32,2`, and the switching-isomorphism orbit counts are `1,2,2,1`. At order 16 the 32 classes split into two size-16 Hamilton-holonomy sectors; every minimizing defect has exactly two repeated-root pairs.

### Strictly above six

Every other admissible pair satisfies

\[
\boxed{m(N,s)>\sqrt6.}
\]

## 2. Six-boundary mechanism

With `B=A^2-4I` and `K=6I-A^2=2I-B`, root quotienting plus parity-defect support localizes every generic `rho(A)^2<=6` candidate to

\[
t=2,\qquad q=2t+1,\qquad q=2t+2,\qquad q=3t,
\]

where `q=N/gcd(N,2)` and `t=min(s,q-s)`. All four loci are closed, yielding the complete equality theorem above.

## 3. Exact low-end and rigidity results

- `m(N,s)=2` iff `N=2s+2`.
- `m(N,s)=sqrt(5)` iff `(N,s)=(5,2)` or `(10,3)`.
- Outside those cases, `m(N,s)^2>=4+sqrt(2)`; equality occurs exactly at `(8,2)`.
- On `N=4s`, `m(4s,s)^2=4+2 cos(pi/(2s))`, with exactly two labelled minimizing switching classes.
- On the flat line `N=2s+2`, `s!=3`, there are exactly two labelled equality switching classes; `(8,3)=K_(4,4)` has six labelled classes and one switching-isomorphism orbit.
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

### Vertical fixed-step theorems

\[
\boxed{m(3k,3)<\sqrt8\qquad(k\ge3),}
\]

\[
\boxed{m(5k,5)<\sqrt8\qquad(k\ge3),}
\]

and, for every

\[
s\in\{7,9,11,13\},
\]

\[
\boxed{m(sk,s)<\sqrt8\iff k\ge4\qquad(k\ge3).}
\]

Thus for the four consecutive odd steps `7,9,11,13`, the unique non-sub-threshold member of the vertical family is exactly the chord-triangle point `k=3`.  The step-eleven and step-thirteen `k=5` cases require small local modifications of the alternating chord word; they are certified by exact rational LDL.

## 5. General odd seam-defect framework

For every odd resonance

\[
N=ks,\qquad k\ge3\text{ odd},\qquad s\ge5\text{ odd},
\]

use Hamilton seam `-1` and alternating chord signs. After multiplication-by-two reindexing there is an exact identity

\[
\boxed{
8I-A^2=L_{\Sigma_{N,s}}+E_-+E_+,
}
\]

where `L_Sigma` is a signed Laplacian on `C_N(1,s)` and the only two non-Laplacian entries are

\[
E_-:\ \left\{0,N-\frac{s+1}{2}\right\}\text{ with coefficient }-2,
\]

\[
E_+:\ \left\{\frac{N-s}{2},\frac{N-1}{2}\right\}\text{ with coefficient }+2.
\]

So the remaining odd positive-side problem has been reduced from an unconstrained signing search to a two-defect energy-absorption problem.  Steps `5,7,9,11,13` are obtained by fixed local positive-definite absorbers after finitely many small bases; step `3` is the special collision case where only one genuine non-Laplacian defect remains.

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

New `sqrt(8)` files:

- `ODD_RESONANCE_STEP3_SUBSQRT8.md`
- `ODD_RESONANCE_STEP5_SUBSQRT8.md`
- `ODD_RESONANCE_STEP7_THRESHOLD.md`
- `ODD_RESONANCE_STEP9_THRESHOLD.md`
- `ODD_RESONANCE_STEP11_THRESHOLD.md`
- `ODD_RESONANCE_STEP13_THRESHOLD.md`
- `ODD_RESONANCE_SEAM_DEFECT_FRAMEWORK.md`

Exact reproducibility scripts include the corresponding `verify_step3_*`, `verify_step5_*`, `verify_step7_*`, `verify_step9_*`, `verify_step11_*`, `verify_step13_*`, and `verify_odd_resonance_seam_defect.py` audits, in addition to the six-boundary scripts.

# Current frontier

The `sqrt(6)` parameter classification and minimizer rigidity are complete. At `sqrt(8)`, the horizontal `k=3` line and vertical fixed steps `3,5,7,9,11,13` are now classified. The main open problem is the general odd `(k,s)` phase boundary. The seam-defect identity gives a concrete route: quantify how much signed-Laplacian energy is available to absorb the two explicit seam bilinear terms as `s/k` varies. Step `15` is the next boundary test: the unmodified alternating signing is sub-threshold from odd `k=9` onward, a two-flip modification handles `k=7`, while the global status of `(75,15)` remains under active audit.