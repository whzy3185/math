# Finite spectral extrema in signed step circulants

Working branch: `paper/circulant-finite-threshold-20260909`.

This directory rebuilds and strengthens the finite-global extremal problem

\[
m(N,s)=\min_\sigma\rho(A_\sigma),\qquad 2\le s<N/2,
\]

for signed adjacency matrices of `C_N(1,s)`.

## Scope boundary

This paper is completely independent of the separate periodic/Bloch project.  It concerns finite graphs, minimization over **all** signings, exact equality, threshold classification, and switching/flux rigidity.  No continuous Bloch optimum, phase-slip asymptotic, or theorem from the other paper is used.

## Current proved theorem package

### 1. Exact low end

- `m(N,s)=2` iff `N=2s+2`.
- Off the flat line, `m(N,s)>=sqrt(5)`.
- `m(N,s)=sqrt(5)` iff `(N,s)=(5,2)` or `(10,3)`.
- Outside those cases, `m(N,s)^2>=4+sqrt(2)`.
- Equality `m^2=4+sqrt(2)` occurs exactly at `(8,2)`.
- On `N=4s`,
  \[
  m(4s,s)^2=4+2\cos\frac{\pi}{2s},
  \]
  with exactly two labelled minimizing switching classes.

Flat rigidity is also classified: on `N=2s+2`, `s!=3`, there are exactly two labelled equality switching classes; at `(8,3)=K_(4,4)` there are six labelled switching classes, one orbit after graph automorphisms.

### 2. Complete strict sub-`sqrt(6)` classification

Let `beta` be the largest root of

\[
x^3-7x+7=0.
\]

Then

```text
m(N,s)^2 < 6 iff

N=2s+2:                         m^2=4;
(N,s)=(5,2),(10,3):             m^2=5;
N=4s:                           m^2=4+2 cos(pi/(2s));
N=14, s=3,4,5:                  m^2=4+beta.
```

Every other pair has `m(N,s)^2>=6`.  In particular every odd `N>=7` satisfies `m(N,s)>=sqrt(6)`.

### 3. New arithmetic localization at the non-strict six boundary

Put

\[
d=\gcd(N,2),\qquad q=N/d,\qquad t=\min(s,q-s),
\]

and exclude the already separated lines `N=2s+2` and `N=4s`.

If **any** signing satisfies

\[
\rho(A)^2\le6,
\]

then the reduced parity component must lie on one of only four arithmetic loci:

\[
\boxed{
 t=2,
 \qquad q=2t+1,
 \qquad q=2t+2,
 \qquad q=3t.
}
\]

The proof is analytic.  For `K=6I-A^2>=0`, a defect entry of magnitude `2` forces repeated/antipodal Gram roots and hence twin vertices in the parity graph.  A connected `C_q(1,t)` has twins iff `q=2t+2`.  Away from that twin line the defect is an honest signing of the parity graph.  If that graph is triangle-free, the boundary cubic-moment identity forces the defect component to satisfy `C^2=4I`, and the already proved flat theorem again forces `q=2t+2`.  The remaining alternative is precisely the elementary triangle list `t=2`, `q=2t+1`, `q=3t`.

Consequently, for odd order,

\[
m(N,s)\le\sqrt6
\Longrightarrow
s=2\text{ or }N=2s+1\text{ or }N=3s.
\]

Every odd pair outside these three loci therefore satisfies the **strict** bound `m(N,s)>sqrt(6)`.

### 4. Complete twin-resonance analysis

The twin locus `q=2t+2` translates to

\[
N=4r,\qquad s=r\pm1.
\]

It is now completely classified:

\[
\boxed{
 m(N,s)^2=6
 \iff
 (N,s)\in\{(12,4),(16,3),(16,5)\}
}
\]

within this locus.  Moreover

\[
\boxed{m(12,2)^2=5+\sqrt3,}
\]

with exactly two labelled minimizing switching classes, certified by an exhaustive **exact** `Q(sqrt(3))` PSD computation over all `2^13=8192` Hamilton-gauge switching classes.

For every `r>=5`,

\[
 m(4r,r-1)^2>6,
 \qquad
 m(4r,r+1)^2>6.
\]

The exclusion is analytic: repeated roots cannot occur at the available mixed two-walk displacements; the defect must therefore be flat on `C_(2r)(1,r-1)`.  For odd `r`, induced chord-cycle fluxes are equal whereas flat rigidity forces them to be opposite.  For even `r`, flat holonomy plus mixed cancellation forces a defect whose antipodal two-walk entry equals `-4`, contradicting `C^2=4I`.

### 5. `sqrt(8)` results

For every even `N`,

\[
m(N,s)^2\le6+2\cos\frac{2\pi}{N}<8.
\]

On the triangle resonance `N=3s`,

\[
\boxed{m(3s,s)<\sqrt8\iff s\text{ is even or }s\in\{3,5\}.}
\]

For odd `s>=7`, the audited all-signing obstruction has been strengthened to

\[
\boxed{m(3s,s)^2\ge8+\frac{2}{139}.}
\]

The proof uses exact `s=7,9` base certificates and the exact nine-column local rule followed by analytic propagation.

## Exact verification scripts

- `verify_low_end_exact.py`
- `verify_sub_sqrt6_exact.py`
- `verify_six_boundary_exact.py`
- `verify_six_boundary_arithmetic.py`
- `verify_twin_line_base_exact.py`

All theorem labels in `THEOREM_LEDGER.md` distinguish **Proved**, **Verified**, **Observed**, and **Published/Established**.  Finite computations are explicitly delimited and never promoted beyond their quantified range.

## Current frontier

The equality problem `m(N,s)^2=6` is no longer unconstrained.  The twin locus is closed completely; the only remaining possible equality mechanisms lie on the three **triangle loci**

\[
t=2,
\qquad q=2t+1,
\qquad q=3t.
\]

This is now the highest-value finite-global target.  Beyond six, the other major open direction is the `sqrt(8)` classification for odd resonances `N=ks`, `k>=5`.