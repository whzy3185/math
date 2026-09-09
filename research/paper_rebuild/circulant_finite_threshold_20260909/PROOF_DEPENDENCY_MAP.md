# Proof dependency map

This paper is self-contained and has no dependency on `paper/circulant-periodic-gap-20260909`.

## A. Finite signed-graph preliminaries

`switching invariance`
→ Hamilton-path gauge for `C_N(1,s)`
→ completeness of finite enumeration (`alpha` plus the remaining chord signs).

`tr(A^2)=4N`
→ `rho(A)>=2`
→ equality iff `A^2=4I`.

Throughout the structural sections put

`B=A^2-4I`, so `rho(A)^2=4+lambda_max(B)`.

## B. The parity-defect engine

Over `F_2[Z_N]`, with

`p=x+x^-1+x^s+x^-s`,

Frobenius gives

`p^2=x^2+x^-2+x^(2s)+x^(-2s)`.

The parameter range permits exactly two collision patterns, hence

```text
supp(B mod 2) = empty                         if N=2s+2,
                 Cay(Z_N,{+-2})               if N=4s,
                 Cay(Z_N,{+-2,+-2s})          otherwise.
```

This one lemma feeds four branches of the paper.

### B1. Flat line

`B=0`
→ parity defect must be empty
→ `N=2s+2`.

`explicit alternating Hamilton-gauge signing`
→ `B=0`
→ `m(N,s)=2`.

`mixed two-walk channel`
→ two labelled equality switching classes except `(8,3)`.

`(8,3)=K4,4`
→ Hadamard block condition
→ six labelled switching classes, one switching-isomorphism orbit.

### B2. First two discrete spectral gaps

Outside the flat line `B!=0` and is integral, symmetric, zero diagonal.

`nonzero 2x2 principal block`
→ `lambda_max(B)>=1`
→ `rho(A)^2>=5`.

If `lambda_max(B)=1`:

`I-B>=0 + integrality`
→ every nontrivial support component is a negative clique up to switching
→ parity defect forces `N=5` or `10`
→ exact exclusions/constructions
→ `m=sqrt(5)` exactly at `(5,2),(10,3)`.

If `0<lambda_max(B)<sqrt(2)`:

`induced P3 interlacing`
→ every support component is a clique
→ triangle signs force negative clique blocks
→ `lambda_max(B)=1`.

Hence, away from the flat and `sqrt(5)` parameters,

`m(N,s)^2>=4+sqrt(2)`.

Equality analysis plus the parity support
→ unique parameter `(8,2)`
→ exact characteristic polynomial `(x^4-8x^2+14)^2`.

### B3. Exact `N=4s` resonance

On `N=4s`, below defect index 2, integrality plus parity forces `B` to be exactly two signed cycles of length `2s`.

`signed-cycle spectrum`
→ each component has largest eigenvalue at least `2 cos(pi/(2s))`
→ global lower bound.

`finite anti-periodic signed shift T^(4s)=-I`
+ `alternating D`, `DT=-TD`
→ `A^2=4I+T^2+T^-2`
→ finite roots `z^(4s)=-1`
→ exact upper bound

`m(4s,s)^2=4+2 cos(pi/(2s))`.

Mixed displacement `s+1`
→ `D` must alternate.

Vanishing displacement `2s`
→ Hamilton holonomy `alpha=-1`
→ exactly two labelled minimizing switching classes.

### B4. Sub-six arithmetic obstruction

Assume hypothetically `rho(A)^2<6`, so `M=lambda_max(B)<2`.

`2x2 interlacing + integrality`
→ every off-diagonal entry is `0,+-1`
→ `supp B = supp(B mod 2)`.

Thus in the generic case `B` is a signing of the fixed 4-regular parity graph

`Gamma_Ns=Cay(Z_N,{+-2,+-2s})`.

Cubic-moment lemma:

`tr X=tr X^3=0`
→ from `(M-mu)(mu+M)^2/M>=0`
→ `lambda_max(X)^2>=tr(X^2)/n`.

If `Gamma_Ns` is triangle-free:

`tr B^2=4N`, `tr B^3=0`
→ `lambda_max(B)>=2`
→ contradiction
→ `m(N,s)>=sqrt(6)`.

Reduce each parity component to `C_q(1,t)`, where

`d=gcd(N,2)`, `q=N/d`, and `t` is the reduced step.

Three-increment classification:

`C_q(1,t)` has a triangle iff

`t=2` or `q=2t+1` or `q=3t`.

Consequences:

```text
N odd, s!=2, N!=2s+1, N!=3s  =>  m(N,s)>=sqrt(6).

k odd >=5, s>=3               =>  m(ks,s)>=sqrt(6).
```

This is the general odd-resonance lower theorem.

## C. All-even-order sub-`sqrt(8)` theorem

For `N` even choose anti-periodic signed shift `T^N=-I` and alternating diagonal `D`.

`DT=-TD`
→
`A^2=4I+T^2+T^-2+(-1)^s(T^(2s)+T^(-2s))`.

Finite Fourier on `z^N=-1`
→
`rho(A)^2<=6+2 cos(2pi/N)<8`.

Therefore every even-order two-step circulant has a finite signing below `sqrt(8)`.

For `N=ks`, the unresolved `sqrt(8)` obstruction can occur only when both `k` and `s` are odd.

## D. Exact `N=3s` threshold transition

### D1. Positive side

`N=3s` and `s` even
→ `N` even
→ Section C gives `m(3s,s)<sqrt8`.

For `s=3,5`:

`explicit finite signing`
+ exact positivity of all leading principal minors of `8I-A^2`
→ `m(9,3),m(15,5)<sqrt8`.

### D2. Odd obstruction

Hamilton gauge and reorder `i=j+as`
→ width-three cyclic strip whose column states are signed triangles.

Exact nine-column finite lemma at excess `2/139`:

- complete finite state space;
- exact integer Rayleigh acceptance;
- survivor counts `8,56,152,440,488,1016,656,1064,128`;
- all 128 final survivors satisfy the six middle alternations.

Base cases:

- `s=7`: exact exhaustive Q-necklace certificate gives excess `18/131`;
- `s=9`: exact cyclic prefix certificate gives excess `2/139`.

For odd `s>=11`:

`every nine-column window below threshold`
→ local alternation propagates around the cycle
→ seam straightening would force `S B_0 S^T=-B_0`
→ impossible because `tr(B_0^3)=+-6` is preserved by similarity and changes sign under negation.

Hence

`m(3s,s)^2>=8+2/139` for all odd `s>=7`.

Combine D1/D2:

`m(3s,s)<sqrt8 iff s is even or s in {3,5}`.

## E. Exact-computation trust boundary

The computer-assisted statements are only the finite `N=3s` certificate lemmas/base cases. Floating eigensolvers may be used to propose integer Rayleigh witnesses, but no branch is accepted from floating output. Acceptance uses exact integer inequalities, e.g.

`139 w^T(M^2-8I)w >= 2 w^T w`.

Thus floating error can cause failure to find a certificate but cannot create a false positive proof.

The parity-defect results, low-end hierarchy, exact `N=4s` theorem, arithmetic `sqrt(6)` theorem, all-even construction, and analytic propagation are independent of floating arithmetic.

## F. Remaining resonance frontier

The current `N=ks` picture is now:

```text
k=3: exact sub-sqrt(8) classification; odd s>=7 obstructed above 8+2/139.
k=4: exact global formula m(4s,s)^2=4+2 cos(pi/(2s)).
ks even: explicit all-signing minimum upper bound <8.
k odd >=5, s>=3: global lower bound m(ks,s)>=sqrt(6).
```

The main unresolved finite-global question is the `sqrt(8)` behavior for **odd `k>=5` and odd `s`**. Small exact/numerical data include sub-threshold examples, but no general classification is claimed.
