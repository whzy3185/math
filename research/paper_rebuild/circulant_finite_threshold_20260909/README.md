# Finite spectral extrema in signed step circulants

Working branch: `paper/circulant-finite-threshold-20260909`.

This directory develops the finite-global extremal problem
\[
m(N,s)=\min_\sigma\rho(A_\sigma),\qquad 2\le s<N/2,
\]
for signed adjacency matrices of `C_N(1,s)`.

## Scope boundary

This paper is completely independent of the separate periodic/Bloch project.  It concerns finite graphs, minimization over **all** signings, exact equality, threshold classification, and switching/flux rigidity.  No theorem from the periodic-family paper is used.

# Current main theorem package

## 1. Complete classification through `sqrt(6)`

Let `beta` be the largest root of `x^3-7x+7=0`.

Exactly the following pairs satisfy `m(N,s)^2<6`:

```text
N=2s+2:                         m^2=4;
(N,s)=(5,2),(10,3):             m^2=5;
N=4s:                           m^2=4+2 cos(pi/(2s));
N=14, s=3,4,5:                  m^2=4+beta.
```

The equality boundary is also complete:
\[
\boxed{m(N,s)^2=6\iff (N,s)\in\{(12,4),(16,3),(16,5),(20,8)\}.}
\]
Every other admissible pair satisfies `m(N,s)>sqrt(6)`.

At the four equality pairs, the labelled minimizing switching-class counts are respectively
\[
2,32,32,2,
\]
and the switching-isomorphism orbit counts are
\[
1,2,2,1.
\]
The order-16 boundary is the repeated-root case; the order-12 and order-20 cases are duplicate-free.

Other exact low-end results include
\[
m(N,s)=2\iff N=2s+2,
\]
\[
m(N,s)=\sqrt5\iff (N,s)=(5,2),(10,3),
\]
and
\[
m(12,2)^2=5+\sqrt3.
\]

## 2. `sqrt(8)`: complete horizontal triangle resonance

Every even order has a finite sub-threshold signing:
\[
m(N,s)^2\le6+2\cos\frac{2\pi}{N}<8.
\]

On `N=3s`,
\[
\boxed{m(3s,s)<\sqrt8\iff s\text{ is even or }s\in\{3,5\}.}
\]
For every odd `s>=7`, the current quantitative obstruction is
\[
\boxed{m(3s,s)^2\ge8+\frac{24}{1667}.}
\]
The `s=7` exact base is stronger (`18/131`).  The `s=9` base and the nine-column local rule are certified at the common margin `24/1667`; the local survivor counts are

```text
8, 56, 152, 440, 488, 1016, 656, 1064, 128.
```

## 3. Odd positive-side seam-response framework

For odd `N=ks`, odd `k>=3`, odd `s>=5`, the Hamilton-seam / alternating-chord signing satisfies, after multiplication-by-two reindexing,
\[
\boxed{8I-A^2=L_\Sigma+E_-+E_+,}
\]
where `L_Sigma` is a signed Laplacian on `C_N(1,s)` and the only remaining non-Laplacian terms are two rank-two seam defects.

After moving the favorable rank-one pieces into a positive matrix `H`,
\[
8I-A^2=H-UU^T,
\]
with two-column `U`, hence
\[
\boxed{8I-A^2\succ0\iff I_2-U^TH^{-1}U\succ0.}
\]
A finite-absorber theorem further reduces every fixed odd step to two fixed local positive-definiteness certificates plus finitely many small odd chord-cycle lengths.

## 4. Complete and near-complete vertical thresholds

The fully classified vertical families now are
\[
\boxed{m(3k,3)<\sqrt8\quad(k\ge3),}
\]
\[
\boxed{m(5k,5)<\sqrt8\quad(k\ge3),}
\]
\[
\boxed{m(sk,s)<\sqrt8\iff k\ge4\quad(s=7,9,11,13),}
\]
and, after the new all-signing width-five obstruction,
\[
\boxed{m(15k,15)<\sqrt8\iff k=4\text{ or }k\ge6,}
\]
\[
\boxed{m(17k,17)<\sqrt8\iff k=4\text{ or }k\ge6.}
\]
In particular the previously open points are now proved non-sub-threshold:
\[
\boxed{m(75,15)\ge\sqrt8,\qquad m(85,17)\ge\sqrt8.}
\]

## 5. All-signing width-five theory on `N=5s`

Reorder `C_(5s)(1,s)` into `s` chord-pentagon columns.  The five elementary square fluxes between adjacent columns form an intrinsic transition mask.  A transition is **complement** when all five square fluxes are negative; otherwise it is a defect.

The current exact local rules are:

1. **13-column complement rule.** Two adjacent defect transitions cannot occur in the middle of a sub-`sqrt(8)` strip.  The 320-action quotient has prefix survivor counts
   ```text
   1, 7, 33, 130, 548, 1867, 3870, 10080,
   ```
   and the central double-defect branch closes as `204 -> 135 -> 1 -> 0` after exact integer pruning.

2. **14-column single-defect rule.** A unique defect with five complement transitions on one side and seven on the other has squared radius at least eight.  The seven `D_5` defect-mask representatives have exact integer Rayleigh excesses
   ```text
   660, 312, 310, 120, 98, 11, 8.
   ```

3. **Embedded gap 2/4 rule.** Two defects separated by two or four complement transitions are impossible once two arbitrary context transitions are supplied on one side and one on the other.  Exact survivor chains are
   ```text
   g=2: 12 -> 61 -> 8 -> 0,
   g=4: 12 -> 57 -> 1 -> 0.
   ```

4. **Even gaps 6--14.** With one arbitrary context transition on each side, every even gap `g in {6,8,10,12,14}` is impossible.  After the common 12 central survivors, the left-context survivor counts are `53,40,35,19,14`, and every right extension is exactly rejected.

These rules reduce the odd cycles `s=15,17` to only six wrap-around gap patterns.  The full helical seam, both Hamilton holonomies, and every initial pentagon state are then retained in a cyclic exact audit:

```text
s=15 residual gaps: (12,1), (10,3), (10,1,1);
s=17 residual gaps: (14,1), (12,3), (12,1,1).
```

Each two-defect residual has exactly 1,920 full cyclic candidates after seam compatibility.  The three-defect residuals reduce to 100 candidates at `s=15` and 40 at `s=17`.  Every candidate has an exact integer Rayleigh witness for `A^2-8I`.

The proof is `N5S_BASE_15_17_GLOBAL_OBSTRUCTION.md`; the verifier is `verify_n5s_15_17_global_obstruction.py`.

## 6. Exact-computation trust boundary

Finite computations are used only in explicitly delimited certificates.  Floating eigensolvers may propose an integer direction, but a branch is rejected only after an exact integer inequality such as
\[
w^T(M^2-8I)w\ge0
\]
is checked.  Floating error can therefore retain extra branches but cannot create a false exclusion.  Exact PSD/PD assertions elsewhere use symbolic characteristic polynomials, Sylvester minors, or rational `LDL^T` pivots.

# Current frontier

The `sqrt(6)` theory is complete.  At `sqrt(8)`, `N=3s` is complete; the first six odd vertical steps through 13 are complete; steps 15 and 17 are now also complete after the new all-signing `N=5s` base obstruction.

The highest-value next target is a uniform width-five **even-gap theorem**: current exact finite-state data show that the local exclusion continues for every tested even complement-gap beyond 14 and stabilizes to a small boundary-state family.  Proving that transfer statement would reduce the full odd `N=5s` problem to three parametric helical-seam residual families and is the most direct route to a general second horizontal threshold theorem.