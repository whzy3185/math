# Finite spectral extrema in signed step circulants

Working branch: `paper/circulant-finite-threshold-20260909`.

This directory develops the finite-global extremal problem
\[
m(N,s)=\min_\sigma\rho(A_\sigma),\qquad 2\le s<N/2,
\]
for signed adjacency matrices of `C_N(1,s)`.

## Scope boundary

This paper is completely independent of the separate periodic/Bloch project. It concerns finite graphs, minimization over **all** signings, exact equality, threshold classification, and switching/flux rigidity. No theorem from the periodic-family paper is used.

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
\boxed{m(N,s)^2=6\iff (N,s)\in\{(12,4),(16,3),(16,5),(20,8)\}.}
\]

The labelled minimizing switching-class counts are `2,32,32,2`, and the switching-isomorphism orbit counts are `1,2,2,1`. At order 16 the 32 classes split into two size-16 Hamilton-holonomy sectors; every minimizing defect has exactly two repeated-root pairs.

### Strictly above six

Every other admissible pair satisfies
\[
\boxed{m(N,s)>\sqrt6.}
\]

The equality proof uses the integral Gram matrix `6I-A^2`, root quotienting, parity-defect support, and a four-locus arithmetic localization. All four loci are closed.

## 2. Exact low-end results

- `m(N,s)=2` iff `N=2s+2`.
- `m(N,s)=sqrt(5)` iff `(N,s)=(5,2)` or `(10,3)`.
- Outside those cases, `m(N,s)^2>=4+sqrt(2)`; equality occurs exactly at `(8,2)`.
- On `N=4s`,
  \[
  m(4s,s)^2=4+2\cos\frac{\pi}{2s},
  \]
  with exactly two labelled minimizing switching classes.
- `m(12,2)^2=5+sqrt(3)`, with exactly two labelled minimizers.

## 3. `sqrt(8)`: horizontal triangle resonance

Every even order has a finite sub-threshold signing:
\[
m(N,s)^2\le6+2\cos\frac{2\pi}{N}<8.
\]

On `N=3s`,
\[
\boxed{m(3s,s)<\sqrt8\iff s\text{ is even or }s\in\{3,5\}.}
\]

The quantitative odd obstruction has been strengthened twice during the audit. The current proved form is
\[
\boxed{m(3s,s)^2\ge8+\frac{24}{1667}\qquad(s\ge7\text{ odd}).}
\]

The `s=7` exhaustive certificate is stronger (`18/131`). At `s=9`, exact prefix pruning leaves 1,064 length-eight prefixes and checks 17,024 final cyclic candidates. The strengthened nine-column local rule at `24/1667` has survivor counts

```text
8, 56, 152, 440, 488, 1016, 656, 1064, 128,
```

and all 128 final survivors satisfy the same forced middle alternation used in the analytic odd-seam contradiction. The floating eigensolver only proposes integer vectors; every accepted certificate is an exact integer cross-multiplication.

## 4. `sqrt(8)`: vertical odd-step theorems

The fully classified fixed steps are
\[
\boxed{m(3k,3)<\sqrt8\quad(k\ge3),}
\]
\[
\boxed{m(5k,5)<\sqrt8\quad(k\ge3),}
\]
and
\[
\boxed{m(sk,s)<\sqrt8\iff k\ge4\quad\text{for }s\in\{7,9,11,13\}.}
\]

The next two steps are classified except for a single `k=5` base each:

```text
s=15: k=3 is above sqrt(8); every k=4 or k>=6 is below sqrt(8);
      (N,s)=(75,15) remains open.

s=17: k=3 is above sqrt(8); every k=4 or k>=6 is below sqrt(8);
      (N,s)=(85,17) remains open.
```

Search failures at these two open points are recorded only as **Observed** and are not lower bounds.

## 5. General odd seam-defect and response framework

For odd
\[
N=ks,\qquad k\ge3,\qquad s\ge5,
\]
with both `k,s` odd, take Hamilton seam `-1` and alternating chord signs. After multiplication-by-two reindexing,
\[
\boxed{8I-A^2=L_{\Sigma}+E_-+E_+,}
\]
where `L_Sigma` is a signed Laplacian on `C_N(1,s)` and `E_-,E_+` are exactly two rank-two seam defects.

The positivity problem has an exact two-port reduction. After moving two favorable rank-one terms into a positive matrix `H`, one has
\[
8I-A^2=H-UU^T,
\]
with two-column `U`, and hence
\[
\boxed{8I-A^2\succ0\iff I_2-U^TH^{-1}U\succ0.}
\]

A complementary finite-absorber theorem shows that, for any fixed odd step, two fixed positive-definite local absorber matrices certify every sufficiently large odd chord-cycle length; only finitely many small odd `k` then remain. This is the common finite mechanism behind the fixed-step results above.

# Current proof/certificate additions

Important strengthening files include:

- `SIX_BOUNDARY_ROOT_QUOTIENT.md`
- `SIX_BOUNDARY_ARITHMETIC_LOCALIZATION.md`
- `SIX_BOUNDARY_TRIANGLE_3T.md`
- `SIX_BOUNDARY_MINIMIZER_RIGIDITY.md`
- `SIX_BOUNDARY_SWITCHING_ISOMORPHISM.md`
- `ODD_RESONANCE_SEAM_DEFECT_FRAMEWORK.md`
- `ODD_RESONANCE_SEAM_RESPONSE.md`
- `ODD_RESONANCE_FINITE_ABSORBER_PRINCIPLE.md`
- `ODD_RESONANCE_STEP3_SUBSQRT8.md`
- `ODD_RESONANCE_STEP5_SUBSQRT8.md`
- `ODD_RESONANCE_STEP7_THRESHOLD.md`
- `ODD_RESONANCE_STEP9_THRESHOLD.md`
- `ODD_RESONANCE_STEP11_THRESHOLD.md`
- `ODD_RESONANCE_STEP13_THRESHOLD.md`
- `ODD_RESONANCE_STEP15_NEAR_CLASSIFICATION.md`
- `ODD_RESONANCE_STEP17_NEAR_CLASSIFICATION.md`
- `N3S_MARGIN_UPGRADE_24_1667.md`

The corresponding `verify_*.py` files use exact symbolic, integer, or rational acceptance checks. `THEOREM_LEDGER.md` is the authoritative status table.

# Current frontier

The `sqrt(6)` classification and its minimizer rigidity are complete. At `sqrt(8)`, the horizontal `N=3s` line is complete and the quantitative odd gap is now `24/1667`. The odd positive side is governed by a universal two-seam response problem rather than an unconstrained signing search.

The most important unresolved finite-global problem visible from current data is the next horizontal resonance `N=5s`: the cases `s=3,5,7,9,11,13` have sub-`sqrt(8)` signings, while `(75,15)` and `(85,17)` are the first unresolved odd points. Current width-five local-strip reconnaissance suggests strong central complement structure, but no all-signing obstruction has yet been proved and no such statement is promoted above **Observed** status.