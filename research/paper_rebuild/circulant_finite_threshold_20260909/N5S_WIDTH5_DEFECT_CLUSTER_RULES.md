# Fixed defect-cluster exclusions in width-five strips

This note complements the even-gap rules by controlling the short **odd** gaps that survive the cyclic parity reduction on `N=5s`.  Transition masks are intrinsic square-flux masks; `31` denotes a complement transition and `0,...,30` denote defects.

## Theorem 1 (two defects with gap one)

No open width-five strip with squared spectral radius below eight contains

\[
\boxed{31^9,d,31,e,31^9,\qquad d,e\ne31.}
\tag{1}
\]

Thus two defects separated by a single complement transition cannot have nine complement transitions available on both exterior sides.

## Theorem 2 (two defects with gap three)

No sub-threshold open strip contains

\[
\boxed{31^7,d,31^3,e,31^7,\qquad d,e\ne31.}
\tag{2}
\]

## Theorem 3 (three-defect cluster)

No sub-threshold open strip contains

\[
\boxed{31^6,d,31,e,31,f,31^6,\qquad d,e,f\ne31.}
\tag{3}
\]

### Exact proof of all three statements

Normalize the initial pentagon state to zero.  Transition masks are unchanged by common row switching and global complementation; the remaining simultaneous row symmetry is `D_5`.

For (1) and (2), the `31^2=961` labelled defect pairs have exactly 121 `D_5` orbits.  For every orbit representative the complete fixed-context strip admits an integer vector `w` satisfying

\[
w^T(M^2-8I)w\ge0,
\qquad w\ne0.
\tag{4}
\]

Hence the exact survivor counts are

\[
\boxed{121\to0}
\]

for both fixed words (1) and (2).

For (3), the `31^3` labelled triples reduce to exactly

\[
\boxed{3151}
\]

simultaneous `D_5` orbits.  Again every orbit representative has an exact integer witness (4), so

\[
\boxed{3151\to0.}
\tag{5}
\]

Interlacing then excludes all three configurations from every larger sub-threshold strip. `square`

The verifier `verify_n5s_width5_defect_cluster_rules.py` reconstructs all 121, 121 and 3151 orbit representatives and verifies (4) in integer arithmetic.  Floating eigenvectors are used only to propose integer directions.

---

## Corollary 3.1 (large residual patterns are locally impossible)

Consider an odd cyclic width-five word with defect-gap pattern `(G,1)`.  If

\[
G\ge20,
\]

then nine complement transitions can be taken from each end of the long gap while leaving at least one unused transition, so (1) occurs in a proper open interval.  Hence such a residual is impossible below `sqrt(8)`.

Likewise:

- a residual `(G,3)` is impossible for `G>=16` by (2);
- a residual `(G,1,1)` is impossible for `G>=14` by (3).

The strict inequalities relative to the displayed context lengths ensure that the chosen interval is a proper principal strip rather than the whole cyclic graph.

Consequently, once a uniform theorem excludes all embedded even complement gaps, the only genuinely cyclic base cases needed on the odd horizontal line `N=5s` occur at finitely many small `s`.  In particular every one of the three standard residual templates

\[
(s-3,1),\qquad(s-5,3),\qquad(s-5,1,1)
\]

is locally impossible for every odd `s>=23`.