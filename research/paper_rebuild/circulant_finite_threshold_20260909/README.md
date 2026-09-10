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

The equality boundary is complete:
\[
\boxed{m(N,s)^2=6\iff (N,s)\in\{(12,4),(16,3),(16,5),(20,8)\}.}
\]
Every other admissible pair satisfies
\[
\boxed{m(N,s)>\sqrt6.}
\]

At the four equality pairs, labelled minimizing switching-class counts are
\[
2,32,32,2,
\]
and switching-isomorphism orbit counts are
\[
1,2,2,1.
\]
The order-16 cases are the repeated-root boundary mechanism; orders 12 and 20 are duplicate-free.

Other exact low-end results include
\[
m(N,s)=2\iff N=2s+2,
\]
\[
m(N,s)=\sqrt5\iff (N,s)=(5,2),(10,3),
\]
\[
m(12,2)^2=5+\sqrt3,
\]
and the exact global family
\[
m(4s,s)^2=4+2\cos\frac{\pi}{2s}.
\]

## 2. Universal even-order theorem at `sqrt(8)`

Every even order admits an all-finite explicit signing with
\[
\boxed{
m(N,s)^2\le6+2\cos\frac{2\pi}{N}<8.
}
\]
The proof uses an anti-periodic signed shift and finite Fourier diagonalization only after the explicit signing is chosen; it does not reduce the global signing domain to translation-invariant signings.

## 3. First horizontal threshold: `N=3s`

The triangle resonance is completely classified:
\[
\boxed{
m(3s,s)<\sqrt8
\iff
s\text{ is even or }s\in\{3,5\}.
}
\]
For every odd `s>=7`,
\[
\boxed{
m(3s,s)^2\ge8+\frac{24}{1667}.
}
\]
The negative proof consists of exact `s=7,9` bases, a nine-column exact local rule with survivor counts

```text
8, 56, 152, 440, 488, 1016, 656, 1064, 128,
```

and an analytic seam contradiction after local alternation propagates globally.

## 4. Second horizontal threshold: `N=5s`

This line is now also completely classified:
\[
\boxed{
m(5s,s)<\sqrt8
\iff
s\text{ is even or }s\in\{3,5,7,9,11,13\}.
}
\]
Equivalently,
\[
\boxed{
s\ge15\text{ odd}\Longrightarrow m(5s,s)\ge\sqrt8.
}
\]

This is an **all-signing** theorem.  Its negative side does not come from the explicit seam construction.

### Width-five proof mechanism

Reorder `C_(5s)(1,s)` into `s` chord-pentagon columns.  The five elementary square fluxes across each adjacent-column boundary form an intrinsic transition mask.  Mask `31` is a **complement transition**; every other mask is a **defect**.

The proof now has the following exact local ingredients.

1. **Adjacent-defect exclusion.** A 13-column sub-threshold strip cannot have two central defect transitions.

2. **Single-defect exclusion.** A 14-column strip with one defect and complement context `5/7` has squared radius at least eight.

3. **Small even gaps.** Gaps `2,4` are exactly excluded with the stated three outside transitions; gaps `6,8,10,12,14,16,18` are excluded with one arbitrary transition on each side.

4. **Half-line rigidity.** Among the 128 `D_5` orbits of
   \[
   (*,d,31^{19}),
   \]
   exact pruning leaves only
   \[
   (31,15,31^{19}).
   \]

5. **Uniform long-even-gap witness.** Applying the half-line rule from both ends reduces every even gap `g>=20` to three relative defect types.  For all three there is an explicit parameterized integer vector with
   \[
   w^T(M^2-8I)w=4,
   \qquad
   w^Tw=485g+2177.
   \]
   Hence all long even gaps are ruled out analytically.

6. **Fixed residual-cluster rules.** The three open patterns
   \[
   31^9d31e31^9,
   \qquad
   31^7d31^3e31^7,
   \qquad
   31^6d31e31f31^6
   \]
   have exact `D_5` survivor counts `121->0`, `121->0`, and `3151->0`.

For odd `s`, cyclic gap parity forces some even complement gap.  The uniform even-gap theorem reduces the only possible wrap-around patterns to
\[
(s-3,1),\qquad(s-5,3),\qquad(s-5,1,1).
\]
For every odd `s>=23` these contain one of the fixed forbidden clusters in a proper principal strip.  The four small bases
\[
s=15,17,19,21
\]
are closed by exact full-helical-seam cyclic certificates.  In particular
\[
\boxed{
m(75,15),m(85,17),m(95,19),m(105,21)\ge\sqrt8.
}
\]

The complete proof is `N5S_COMPLETE_THRESHOLD_CLASSIFICATION.md`.

## 5. Odd positive-side seam-response framework

For odd
\[
N=ks,\qquad k,s\text{ odd},\quad k\ge3,\ s\ge5,
\]
the Hamilton-seam / alternating-chord signing satisfies, after multiplication-by-two reindexing,
\[
\boxed{8I-A^2=L_\Sigma+E_-+E_+,}
\]
where `L_Sigma` is a signed Laplacian on `C_N(1,s)` and only two seam defects remain.

After a rank-one rearrangement,
\[
8I-A^2=H-UU^T,
\]
with `H>0` and two-column `U`, so
\[
\boxed{8I-A^2\succ0\iff I_2-U^TH^{-1}U\succ0.}
\]
A finite-absorber principle reduces any fixed odd step to two finite local positive-definiteness certificates and finitely many small odd chord-cycle lengths.

This framework proves the vertical classifications
\[
m(3k,3)<\sqrt8\quad(k\ge3),
\]
\[
m(5k,5)<\sqrt8\quad(k\ge3),
\]
\[
m(sk,s)<\sqrt8\iff k\ge4\quad(s=7,9,11,13),
\]
and
\[
m(sk,s)<\sqrt8\iff k=4\text{ or }k\ge6\quad(s=15,17).
\]
The former open `k=5` cases at steps 15 and 17 are now excluded by the complete horizontal `N=5s` theorem.

## 6. Exact-computation trust boundary

Finite computation is used only in explicitly delimited certificates.  A floating eigensolver may propose an integer direction, but a branch is rejected only after an exact integer inequality such as
\[
w^T(M^2-8I)w\ge0
\]
is checked.  Floating error can therefore retain extra candidates but cannot create a false exclusion.  Positive-definiteness certificates elsewhere use exact characteristic polynomials, Sylvester minors, or rational `LDL^T` pivots.

Important current files include:

- `THEOREM_LEDGER.md`
- `PROOF_DEPENDENCY_MAP.md`
- `N5S_COMPLETE_THRESHOLD_CLASSIFICATION.md`
- `N5S_BASE_15_17_GLOBAL_OBSTRUCTION.md`
- `N5S_BASE_19_21_GLOBAL_OBSTRUCTION.md`
- `N5S_WIDTH5_LOCAL_COMPLEMENT_RULE.md`
- `N5S_WIDTH5_EVEN_GAP_24_RULE.md`
- `N5S_WIDTH5_EVEN_GAP_6_14_RULE.md`
- `N5S_WIDTH5_EVEN_GAP_16_30_RULE.md`
- `N5S_WIDTH5_DEFECT_CLUSTER_RULES.md`
- `ODD_RESONANCE_SEAM_DEFECT_FRAMEWORK.md`
- `ODD_RESONANCE_SEAM_RESPONSE.md`
- `ODD_RESONANCE_FINITE_ABSORBER_PRINCIPLE.md`
- `N3S_MARGIN_UPGRADE_24_1667.md`

and their corresponding `verify_*.py` files.

# Current frontier

The `sqrt(6)` classification and equality rigidity are complete.  At `sqrt(8)`, the first two odd horizontal resonance lines
\[
N=3s,\qquad N=5s
\]
are now completely classified, and every even order is sub-threshold.

The highest-value next mathematical target is therefore the next horizontal resonance `N=7s`: determine whether its all-signing transition admits a finite-state/local-to-global description analogous to the triangle and pentagon lines, and combine it with the existing seam-response construction on the positive side.  A second priority is to compress the complete `N=5s` proof into manuscript-quality theorem/lemma form and update the paper architecture around the two horizontal threshold transitions.