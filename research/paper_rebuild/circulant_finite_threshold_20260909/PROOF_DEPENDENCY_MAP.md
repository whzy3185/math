# Proof dependency map

This paper is self-contained with respect to `paper/circulant-periodic-gap-20260909`: no theorem, notation, construction, or asymptotic statement from that project is used.

The main external structural input is Greaves--Koolen--Munemasa--Sano--Taniguchi (JCTB 110 (2015)) in the strict sub-`sqrt(6)` theorem.  Rowlinson--Stanić is contextual for the non-strict `-2` boundary; the actual root-quotient reduction used here is proved internally.

## A. Basic finite reduction

`switching invariance`
→ Hamilton-path gauge on `C_N(1,s)`
→ one normalized representative per labelled switching class.

`tr(A^2)=4N`
→ `rho(A)>=2`
→ equality iff `A^2=4I`.

Define

`B=A^2-4I`, so `rho(A)^2=4+lambda_max(B)`.

Over `F_2[Z_N]`, Frobenius squaring gives

```text
supp(B mod 2) = empty                         if N=2s+2,
                 Cay(Z_N,{+-2})               if N=4s,
                 Cay(Z_N,{+-2,+-2s})          otherwise.
```

This parity-defect identity drives both the low spectrum and the `sqrt(6)` classification.

## B. Flat line and first gaps

`B=0`
→ parity support empty
→ `N=2s+2`.

Explicit alternating signing
→ attainment
→ `m(N,s)=2 iff N=2s+2`.

Mixed-channel rigidity
→ two labelled equality classes except `(8,3)`.

`(8,3)=K_(4,4)`
→ Hadamard block condition
→ six labelled switching classes, one switching-isomorphism orbit.

Off the flat line, nonzero integral zero-diagonal `B`
→ a nonzero `2x2` principal block
→ `lambda_max(B)>=1`
→ `m>=sqrt(5)`.

Index-one equality
→ negative-clique defect components
→ liftability
→ `m=sqrt(5)` exactly at `(5,2),(10,3)`.

Next integral defect threshold
→ `m^2>=4+sqrt(2)` outside prior cases
→ equality exactly `(8,2)`.

## C. Exact `N=4s` family

Parity support on `N=4s`
→ two signed cycles of length `2s` below defect index two.

Signed-cycle extremum
+ anti-periodic finite shift construction
→

`m(4s,s)^2=4+2 cos(pi/(2s))`.

Mixed-channel equations
→ exactly two labelled minimizing switching classes.

## D. Complete classification through `sqrt(6)`

Assume a generic pair has `rho(A)^2<6`.

`lambda_max(B)<2`
+ integrality
+ `2x2` interlacing
→ `B` is exactly a `+-1` signing of the forced 4-regular parity graph.

Each connected parity component `C` has `lambda_max(C)<2`
→ `-C` has least eigenvalue `>-2`.

Greaves et al. classification
+ internal 4-regular representation-graph degree audit
→ component order at most eight, apart from the order-five `K_5` case.

Exact orders `5,6,7,8`
→ only `K_5` and the unique sub-2 class on `overline(C_7)` survive.

Liftability
→ complete strict theorem:

```text
m^2<6 iff
  N=2s+2; or
  (N,s)=(5,2),(10,3); or
  N=4s; or
  N=14 and s in {3,4,5}.
```

For equality, `K=6I-A^2` is an integral PSD Gram matrix with diagonal two.

`|K_ij|=2`
↔ repeated/antipodal roots
→ root quotient.

Parity support + twin analysis + cubic boundary identity
→ every generic `rho^2<=6` candidate lies on

```text
t=2,
q=2t+1,
q=2t+2,
q=3t,
```

where `q=N/gcd(N,2)`, `t=min(s,q-s)`.

The four loci are closed by:

- `t=2`: five-vertex Gram rule + finite Fourier on signed `C_q(1,2)`;
- `q=2t+1`: multiplier reduction to the same component problem + lift obstruction;
- `q=2t+2`: flat-defect rigidity + flux/antipodal contradiction;
- `q=3t`: exact 9-vertex local strip for `t>=4`, Gram-kernel argument for `t=3`.

Hence

```text
m^2=6 iff (N,s)=(12,4),(16,3),(16,5),(20,8).
```

Exact finite minimizer audit
→ labelled class counts `2,32,32,2`.

Underlying short-cycle counts
→ full automorphism groups are dihedral in the relevant cases
→ switching-isomorphism orbit counts `1,2,2,1`.

Therefore every other admissible pair is strictly above `sqrt(6)`.

## E. Universal even-order positive theorem at `sqrt(8)`

For even `N`:

anti-periodic signed shift `T^N=-I`
+ alternating diagonal `D`, `DT=-TD`
→ finite square identity
→ finite Fourier grid
→

`m(N,s)^2<=6+2 cos(2pi/N)<8`.

This is a finite construction only; it does not reduce the global signing domain to periodic signings.

## F. Horizontal triangle resonance `N=3s`

`s even`
→ Section E.

`s=3,5`
→ explicit finite signings
→ exact Sylvester positivity of `8I-A^2`.

For odd `s>=7`:

Hamilton gauge + width-three reordering
→ cyclic strip of signed triangle states.

Strengthened exact nine-column lemma at excess `24/1667`
→ survivor counts

`8,56,152,440,488,1016,656,1064,128`

→ every survivor has forced middle alternation.

Base `s=7`
→ exhaustive stronger certificate `18/131`.

Base `s=9`
→ exact prefix pruning + `17,024` cyclic final certificates at `24/1667`.

Odd `s>=11`
→ sliding local alternation
→ global alternating triangle blocks
→ seam relation `S B_0 S^T=-B_0`
→ cubic trace contradiction `tr(B_0^3)=+-6`.

Thus

`m(3s,s)^2>=8+24/1667` for odd `s>=7`,

and

`m(3s,s)<sqrt8 iff s is even or s in {3,5}`.

## G. Odd positive-side seam framework

For odd `N=ks`, odd `k>=3`, odd `s>=5`, choose Hamilton seam `-1` and alternating chord signs.

Exact two-walk channel expansion + multiplication-by-two reindexing
→

`8I-A^2=L_Sigma+E_-+E_+`,

where `L_Sigma` is a signed Laplacian on `C_N(1,s)` and only two rank-two seam defects remain.

Rank-one identities
→ `8I-A^2=H-UU^T`, with `H>0` and `U` having two columns
→ exact response criterion

`8I-A^2>0 iff I_2-U^T H^-1 U>0`.

Graph-metric seam separation
→ finite absorber principle:
if two fixed local absorber matrices are positive definite, every sufficiently large odd `k` for that fixed `s` is sub-`sqrt(8)`; only finitely many small odd `k` remain.

Applications:

```text
s=3,5:       sub-sqrt8 for every k>=3;
s=7,9,11,13: sub-sqrt8 iff k>=4;
s=15,17:     k=3 obstructed; all k=4 or k>=6 proved sub-sqrt8;
             k=5 remains open in each family.
```

The modified small-base constructions are accepted only by exact rational LDL certificates.

## H. First all-signing width-five rigidity for `N=5s`

Reorder `C_(5s)(1,s)` into `s` chord-pentagon columns and switch an open interval so inter-column matchings are identity.

Each column is one of 32 signed `C_5` states.

Common row switching (`16` edge-mask actions)
× dihedral row symmetry (`10`)
× global column-state complement (`2`)
→ a 320-action spectral-radius-preserving quotient.

Exact prefix search, rejecting only when an integer vector proves

`w^T(M^2-8I)w>=0`,

→ prefix survivor counts through length eight

`1,7,33,130,548,1867,3870,10080`.

Restrict length nine to two central non-complement transitions
→ `7392` orbit candidates
→ `71` exact survivors.

Add context alternately on the two sides
→ survivor counts

`204 -> 135 -> 1 -> 0`.

Therefore a thirteen-column sub-`sqrt(8)` strip must have at least one complement transition among its two central transitions.

`N5LOCAL13`
→ in a long cyclic width-five strip, non-complement transitions are locally isolated away from the helical seam.

This is not yet a global obstruction: the current frontier is to classify the allowed isolated non-complement transition types and their seam compatibility.

## I. Computational trust boundary

Exact symbolic/rational computations are used for finite characteristic polynomials, Sylvester/LDL certificates, equality minimizer enumeration, and local finite-state lemmas.

In Rayleigh-pruning scripts a floating eigensolver may propose an integer vector.  A branch is rejected only after an exact integer inequality certifies the claimed threshold.  Floating error can therefore retain extra branches but cannot create a false proof.

Search failure for `(75,15)` or `(85,17)` is only **Observed** and is not used as a lower bound.

## J. Current frontier

```text
sqrt(6):                complete global classification and minimizer rigidity.
N=3s at sqrt(8):        complete, with odd excess 24/1667.
all even N:             explicit finite sub-sqrt8 signing.
odd vertical steps:     structural seam-response/absorber framework;
                        s<=13 classified, s=15,17 each leave only k=5.
N=5s all-signing side:  exact thirteen-column complement-isolation rule proved;
                        isolated defect classification remains open.
```

The highest-value next theorem is a second width-five local rule strong enough to propagate isolated non-complement defects around the cyclic seam, potentially resolving the first open points `(75,15)` and `(85,17)`.