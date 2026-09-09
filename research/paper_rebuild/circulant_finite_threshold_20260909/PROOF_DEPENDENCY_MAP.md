# Proof dependency map

This map deliberately contains no dependency on `paper/circulant-periodic-gap-20260909`.

## A. Structural preliminaries

`Switching invariance`
→ switch a connected signing to Hamilton gauge: first `N-1` step-one edges positive, seam holonomy `alpha=±1`.

`Hamilton-gauge completeness`
→ remaining data consist of `alpha` and `N` chord signs, i.e. `2^(N+1)` representatives; in the `N=3s` strip representation these are `alpha` plus `s` arbitrary signed-triangle states.

`Rayleigh/interlacing`
→ any principal window whose squared norm exceeds a threshold forces the full graph above that threshold.

## B. Flat theorem

`tr(A^2)=4N`
→ `rho(A)>=2`
→ equality iff `A^2=4I`.

`two-step displacement 2`
→ outside `N=2s+2`, vertices `0,2` have an odd number (1 or 3) of common neighbors
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
→ impossible since `tr(B_0^3)=±6` changes sign under negation but not orthogonal similarity.

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
