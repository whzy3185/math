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

## 6. First all-signing rigidity on the next horizontal resonance `N=5s`

Write a consecutive open portion of `C_(5s)(1,s)` as a width-five strip of signed pentagon columns, after switching the inter-column matchings to the identity. A transition is called **complement** when the next pentagon state is the edgewise negative of the previous one; equivalently all five elementary square fluxes across that transition are negative.

An exact finite-state theorem now gives:
\[
\boxed{
\rho(M)^2<8\text{ on a 13-column open strip}
\Longrightarrow
\eta_6=-\eta_5\text{ or }\eta_7=-\eta_6.
}
\]

Thus two adjacent non-complement transitions cannot occur in the middle of a sub-`sqrt(8)` width-five strip once five columns of context are present on each side.

The proof quotients by 320 spectral-radius-preserving switching/dihedral/global-complement actions. Exact prefix survivor counts through length eight are

```text
1, 7, 33, 130, 548, 1867, 3870, 10080.
```

Among length-nine words with both central transitions non-complement, 7,392 orbit candidates reduce by exact integer Rayleigh certificates to 71; extending context gives survivor counts

```text
204 -> 135 -> 1 -> 0.
```

Every branch rejection is justified by an exact integer inequality `w^T(M^2-8I)w >= 0`. This is an all-signing local rigidity lemma, not a statement about the explicit seam construction.

It is not yet a global `N=5s` obstruction: isolated non-complement transitions remain possible, so their type and seam compatibility must still be classified.

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
- `N5S_WIDTH5_LOCAL_COMPLEMENT_RULE.md`

The corresponding `verify_*.py` files use exact symbolic, integer, or rational acceptance checks. In particular `verify_n5s_width5_local_complement.py` reproduces the 13-column local theorem. `THEOREM_LEDGER.md` is the authoritative status table.

# Current frontier

The `sqrt(6)` classification and minimizer rigidity are complete. At `sqrt(8)`, the horizontal `N=3s` line is complete and the quantitative odd gap is `24/1667`. The odd positive side is governed by a universal two-seam response problem rather than an unconstrained signing search.

For `N=5s`, the first exact all-signing local rigidity theorem is now proved: adjacent non-complement transitions are forbidden in the interior of a sufficiently contextualized sub-threshold strip. The next mathematical target is to classify the surviving isolated non-complement transition types and derive a second propagation rule. The global statuses of `(75,15)` and `(85,17)` remain open until either a finite signing with exact `8I-A^2>0` or an all-signing obstruction is proved.