# Proof dependency map

This map deliberately contains no dependency on `paper/circulant-periodic-gap-20260909`.

## A. Structural preliminaries

`Switching invariance`
→ switch a connected signing to Hamilton gauge: first `N-1` step-one edges positive, seam holonomy `alpha=+-1`.

`Hamilton-gauge completeness`
→ remaining data consist of `alpha` and `N` chord signs, i.e. `2^(N+1)` representatives; in the `N=3s` strip representation these are `alpha` plus `s` arbitrary signed-triangle states.

`Rayleigh/interlacing`
→ any principal window whose squared norm exceeds a threshold forces the full graph above that threshold.

## B. Flat theorem and the sharp off-flat gap

`tr(A^2)=4N`
→ `rho(A)>=2`
→ equality iff `A^2=4I`.

`two-step displacement 2`
→ outside `N=2s+2`, vertices `0,2` have an odd number of common neighbors
→ `(A^2)_{0,2}` is a nonzero integer
→ `A^2 != 4I`.

`B=A^2-4I` integral symmetric, diagonal zero
+ `B!=0`
→ a nonzero off-diagonal entry has absolute value at least 1
→ `lambda_max(B)>=1`
→ `rho(A)^2>=5`.

`alternating finite construction on N=2s+2`
→ `A^2=4I`
→ `m(N,s)=2`.

`mixed channel s-1` (except `s=3`)
→ equality forces `tau_i=-tau_{i-1}`
→ exactly two labelled Hamilton-gauge switching classes.

`(8,3)=K4,4`
→ bipartite block `H`
→ equality iff `HH^T=4I`
→ six normalized labelled switching classes; one orbit after row/column permutations.

### B.1 Defect-energy refinement

Put `B=A^2-4I`, `M=lambda_max(B)`.

`A^2 >= 0`
→ every eigenvalue `mu(B)` lies in `[-4,M]`
→ `(M-mu)(mu+4)>=0`
→ `mu^2 <= (M-4)mu+4M`.

Sum over the spectrum and use `tr B=0`:
`tr B^2 <= 4MN`
→
`rho(A)^2 = 4+M >= 4 + tr(B^2)/(4N)`.

This packages the size of all two-step cancellation defects into a quantitative spectral lower bound.

### B.2 Classification of equality in the sqrt(5) bound

Assume `rho(A)^2=5`, hence `lambda_max(B)=1`.

`2x2 interlacing + integrality`
→ every off-diagonal entry of `B` belongs to `{0,+-1}`.

`I-B >= 0`
→ Gram representation by unit vectors.
If `B_ij=+-1`, the corresponding unit vectors are parallel or antiparallel.
Along each nontrivial connected component all vectors are parallel up to sign; two vertices in that component therefore cannot have `B_ij=0`.
→ every nontrivial component of the support graph of `B` is complete.
Moreover its edge signs switch to all negative.

The parity of `(A^2)_{ij}` depends only on the underlying graph. In the group algebra `F_2[Z_N]`, with
`p=x+x^-1+x^s+x^-s`,
we have
`p^2=x^2+x^-2+x^(2s)+x^(-2s)`.
Therefore the forced support graph of `B` is:

- empty if `N=2s+2`;
- `Cay(Z_N,{+-2})` if `N=4s`;
- `Cay(Z_N,{+-2,+-2s})` otherwise.

On `N=4s`, its components are cycles of length `2s>=4`, hence cannot be clique components.
Otherwise it is 4-regular; because `2s` is a multiple of `2`, its connected components are exactly the cosets of `<2>`. Thus it is connected for odd `N` and has two components for even `N`. Clique components must be `K_5`, forcing `N=5` or `N=10`.

- `N=5`: necessarily `s=2`; an explicit 5-by-5 conference core `W` with `W^2=5I-J` gives `rho(W)=sqrt(5)`.
- `N=10`: `s=4` is the flat case; `s=2` and `s=3` remain.
- `(10,2)` exclusion: equality forces all even two-walk channels to cancel. If `t_i` is the signed flux of the triangle `(i,i+1,i+2)`, the cancellation equations give `t_{i+1}=-t_i`. But a mandatory defect triangle on vertices `(i,i+2,i+4)` has sign `t_i t_{i+2}=+1`, contradicting the fact that every defect `K_5` must switch to an all-negative clique, whose triangles are negative.
- `(10,3)` attainment: after ordering the two parity classes, `C_10(1,3)=K_{5,5}` minus a perfect matching. The block signing `A=[[0,W],[W,0]]` has `A^2=diag(5I-J,5I-J)` and spectral radius `sqrt(5)`.

Therefore `m(N,s)=sqrt(5)` iff `(N,s)=(5,2)` or `(10,3)`.

## C. New all-even-order theorem

`N even`, signed shift `T^N=-I`, `D=diag((-1)^i)`
→ `DT=-TD`
→ for the alternating chord signing,
`A^2=4I+T^2+T^-2+(-1)^s(T^(2s)+T^(-2s))`.

`finite Fourier: z^N=-1`
→ squared eigenvalues
`4+2 cos(2 theta)+2(-1)^s cos(2s theta)`, `theta=(2k+1)pi/N`
→ `cos(2 theta)<=cos(2pi/N)`
→ `rho(A)^2<=6+2cos(2pi/N)<8`.

This theorem supplies the even-`s` direction of the `N=3s` classification and simultaneously treats every admissible even order.

## D. Resonance line N=3s

### Positive side

`E1 all-even-order theorem`
→ every even `s` has `m(3s,s)<sqrt8`.

`explicit C9 and C15 signings`
+ exact Sylvester criterion for `8I-A^2`
→ `s=3,5` are sub-threshold.

### Odd obstruction

`Hamilton gauge + column reorder i=j+as`
→ width-three cyclic strip with arbitrary signed triangle `B_j` in each column and identity intercolumn matchings except one signed-permutation seam.

`exact nine-column lemma at 2/139`
→ every 9-column open strip either has squared norm at least `8+2/139`, or its six middle transitions alternate `B_{j+1}=-B_j`.

For odd `s>=11`:
`all nine-column windows below threshold`
→ sliding local rule forces all ordinary transitions to alternate
→ because `s` is odd, `B_{s-1}=B_0`
→ straighten a seam-crossing middle window
→ local rule forces `S_alpha B_0 S_alpha^T=-B_0`
→ impossible since `tr B_0^3=+-6` changes sign under negation but not orthogonal similarity.

Base cases:
- `s=7`: complete Q-necklace / anchor / holonomy exact certificate, stronger excess `18/131`.
- `s=9`: exact prefix-pruned strip certificate at excess `2/139`.

Therefore odd `s>=7` obey `m(3s,s)^2>=8+2/139`.

## E. Computational trust boundary

The finite verifiers use floating eigensolvers only to propose an integer vector `w`. A branch is accepted/pruned only after an integer inequality is checked exactly. Thus floating error can cause a failed run (failure to find a witness) but cannot create a false positive certificate.

The analytic propagation from the nine-column lemma to all odd `s>=11` is independent of floating arithmetic.

## F. General N=ks frontier

`all-even-order theorem`
→ all pairs with `ks` even are sub-threshold.

Hence any new obstruction on `N=ks` must have both `k` and `s` odd.

Observed finite data include a sub-threshold example at `(k,s)=(5,3)`, while `(k,s)=(3,s)` is obstructed for odd `s>=7`. This points to the chord-cycle length `k=N/gcd(N,s)` as a structural parameter. No general odd-`k>=5` classification is currently proved.
