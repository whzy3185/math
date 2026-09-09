# Theorem ledger

Status vocabulary is strict:

- **Proved**: a complete analytic proof, possibly with an explicitly delimited exact finite certificate.
- **Verified**: exact finite computation over the stated finite population only.
- **Observed**: numerical/experimental evidence.
- **Published/Established**: external public literature.

| ID | Statement | Status | Evidence / audit note |
|---|---|---|---|
| F0 | `rho(A_sigma)>=2` for every signing of `C_N(1,s)` | **Proved** | `tr A^2=4N`; equality iff `A^2=4I`. This is also a special case of the standard average-degree/weighing-matrix bound. |
| F1 | `m(N,s)=2 iff N=2s+2` | **Proved** | Necessity from the `(0,2)` common-neighbor channel; outside the flat line it has odd multiplicity 1 or 3. Sufficiency from an explicit alternating Hamilton-gauge signing. |
| F2 | If `N!=2s+2`, then `m(N,s)>=sqrt(5)` | **Proved** | `B=A^2-4I` is integral symmetric, zero diagonal, nonzero. A nonzero off-diagonal integer entry gives a `2x2` principal block with top eigenvalue at least 1. |
| F3 | On `N=2s+2`, `s!=3`, equality has exactly two labelled switching classes, interchanged by translation | **Proved** | `A^2=4I` forces `tau_i+tau_{i-1}=0`, hence `tau_i=epsilon(-1)^i` and `alpha=(-1)^(s+1)`. Small exact enumeration rechecked `s=2,4,5,6`. |
| F4 | At `(8,3)=K_{4,4}`, equality signings are order-4 Hadamard matrices | **Proved** | `A=[[0,H],[H^T,0]]`, so equality iff `HH^T=4I`. There are six normalized labelled switching classes after row/column-sign normalization; switching plus graph automorphisms gives one orbit. |
| F5 | Defect-energy inequality: `rho(A)^2 >= 4 + tr((A^2-4I)^2)/(4N)` | **Proved (new in rebuild)** | Put `B=A^2-4I` and `M=lambda_max(B)`. Since `A^2>=0`, every eigenvalue `mu` of `B` lies in `[-4,M]`; `(M-mu)(mu+4)>=0` gives `mu^2 <= (M-4)mu+4M`. Sum and use `tr B=0` to obtain `tr B^2<=4MN`. |
| F6 | Sharp first off-flat equality: `m(N,s)=sqrt(5) iff (N,s) in {(5,2),(10,3)}` | **Proved (new in rebuild)** | If `rho(A)^2=5`, then `lambda_max(B)=1`. Integrality forces `B_ij in {0,+-1}`; `I-B>=0` implies every nontrivial component of the support of `B` is a negative clique up to switching. Mod 2, the forced support is the Cayley graph determined by `(x+x^-1+x^s+x^-s)^2=x^2+x^-2+x^(2s)+x^(-2s)` in `F_2[Z_N]`. It is empty on `N=2s+2`, 2-regular on `N=4s`, and otherwise 4-regular with one component for odd `N` and two for even `N`; clique components force `N=5` or `10`. At `N=10`, `s=4` is flat, `s=2` is ruled out by alternating triangle-flux cancellation versus the required negative `K_5` defect triangle, and `s=3` is attained. Explicit conference-core signings attain `sqrt(5)` at `(5,2)` and `(10,3)`. |
| F7 | Universal second gap: outside the flat line and the two `sqrt(5)` parameter pairs, `m(N,s)^2 >= 4+sqrt(2)` | **Proved (new in rebuild)** | Integral-defect lemma: below `sqrt(2)`, every support component of `B` must be a clique and switch to an all-negative clique, hence `lambda_max(B)=1`. Combine F1/F6. |
| F8 | Exact second-gap equality: `m(N,s)^2=4+sqrt(2) iff (N,s)=(8,2)` | **Proved (new in rebuild)** | If `lambda_max(B)<=sqrt(2)`, any induced signed `P_3` already has top eigenvalue `sqrt(2)`. Equality in Rayleigh/interlacing forces the middle vertex to have no third support neighbor. Hence every support component with degree at least 3 is a clique; its triangles must all be negative, so its top eigenvalue is 1. The fixed parity support of `B` is empty on the flat line, two cycles on `N=4s`, and 4-regular otherwise. The only non-clique case at top eigenvalue `sqrt(2)` is therefore an unbalanced cycle of length `2s=4`, giving `(8,2)`. |
| PDEF | Parity-defect trichotomy: `supp((A^2-4I) mod 2)` is empty for `N=2s+2`, `Cay(Z_N,{+-2})` for `N=4s`, and `Cay(Z_N,{+-2,+-2s})` otherwise | **Proved (new in rebuild)** | Over `F_2[Z_N]`, Frobenius gives `(x+x^-1+x^s+x^-s)^2=x^2+x^-2+x^(2s)+x^(-2s)`. The parameter range permits exactly the two collision patterns stated. This unifies the flat line, the exact `k=4` resonance, and the generic four-direction defect regime. |
| K4 | For every `s>=2`, `m(4s,s)^2 = 4+2 cos(pi/(2s))`; minimizers are exactly two labelled switching classes, exchanged by one-step rotation | **Proved (new in rebuild)** | Lower bound: if `lambda_max(B)>=2` it is trivial; below 2, integrality plus PDEF forces `B` to be exactly two signed cycles of length `2s`, whose least possible top eigenvalue is `2 cos(pi/(2s))`, attained only when both are unbalanced. Upper bound: finite anti-periodic signed shift `T^(4s)=-I` and alternating diagonal `D` give `A^2=4I+T^2+T^-2`. Rigidity: vanishing of the mixed displacement `s+1` forces `D` alternating, and vanishing of the `2s` channel forces Hamilton holonomy `alpha=-1`, leaving two signs of `D`. |
| E1 | If `N` is even, `m(N,s)^2 <= 6+2 cos(2pi/N)<8` | **Proved (new in rebuild)** | Finite signed shift `T^N=-I`, `D=diag((-1)^i)`, alternating chord signs; direct square and finite Fourier diagonalization. No continuous Bloch theorem is used. |
| R1 | `m(9,3)<sqrt(8)` | **Proved** | Explicit `tau=(-1,1,-1,-1,1,-1,1,-1,1)`, `alpha=1`. Exact Sylvester minors recomputed: `4,16,60,209,722,2508,5746,15993,47304`. |
| R2 | `m(15,5)<sqrt(8)` | **Proved** | Explicit one-defect near-alternating word. Exact Sylvester minors recomputed; final determinant `8636544`, all leading minors positive. |
| L9 | Nine-column signed-triangle local rule at excess `2/139` | **Proved, exact finite lemma** | Exact integer pruning rerun. Survivor counts `8,56,152,440,488,1016,656,1064,128`; all 128 survivors have `B_{j+1}=-B_j` for middle transitions `j=1,...,6`. Floating eigensolvers only propose integer witnesses; acceptance is `139 w^T(M^2-8I)w >= 2 w^Tw`. |
| B7 | Every signing of `C_21(1,7)` has squared radius at least `8+18/131` | **Proved, exhaustive exact certificate** | Full rerun: `49,940` admissible Q-necklaces, `199,760` representatives. Weakest generated exact witness `36/262=18/131`. Completeness uses Hamilton gauge plus translation necklaces. |
| B9 | Every signing of `C_27(1,9)` has squared radius at least `8+2/139` | **Proved, exhaustive exact certificate** | Stronger-margin rerun. Prefix survivors through length 8: `8,56,152,440,488,1016,656,1064`; all `2*1064*8=17,024` cyclic finals certified exactly. Prefix compression covers `2*8^9` gauge representatives. |
| R3 | For odd `s>=7`, `m(3s,s)^2 >= 8+2/139` | **Proved, computer-assisted local lemma + analytic propagation** | `s=7,9` are B7/B9. For odd `s>=11`, every 9-column window satisfies L9. Absence of a witness forces global alternation of signed triangles; seam straightening would require `S B S^T=-B`, impossible because `tr B^3=+-6`. |
| R4 | `m(3s,s)<sqrt8 iff s even or s in {3,5}` | **Proved** | Even `s` follows from E1 because `3s` is even; `s=3,5` are R1/R2; odd `s>=7` is R3. |
| P8 | Earlier period-8 paper determines the global finite minimum for all `C_{8L}(1,2)` | **Rejected historical overclaim / not a theorem here** | `proof/period8-conclusion-correction` explicitly states that the global minimum and minimizing switching classes remain open there. Fixed-phase dispersion is excluded from this paper. |
| Ksmall | For small `N=ks<=15`, exhaustive switching-gauge search found sub-threshold examples at `(k,s)=(4,2),(4,3),(5,2),(5,3),(6,2),(7,2)` | **Observed** | Numerical enumeration over `2^(N+1)` Hamilton-gauge representatives. These data motivate odd-order resonance work but are not used as theorem evidence. |
| Kodd | All odd resonance ratios `k>=5` are sub-threshold | **Open / not claimed** | `(k,s)=(5,3)` is Observed sub-threshold; no all-parameter proof yet. |
| Lit1 | Fixed-underlying-graph signature minimizing spectral radius is an established general problem | **Published/Established** | Belardo--Cioaba--Koolen--Wang, *Art Discrete Appl. Math.* 1 (2018), Problem 3.18. This is the natural broad framing for `m(N,s)`. |
| Lit2 | General classification of signed graphs with all eigenvalues in `[-2,2]` | **Published/Established** | McKee--Smyth, *J. Algebra* 317 (2007), 260--290. The present flat theorem is only a family-specific exact classification. |
| Lit3 | Connected signed graphs of maximum degree at most 4 with two adjacency eigenvalues are classified | **Published/Established** | Hou--Tang--Wang, *Discrete Math.* 342 (2019), 111615. This overlaps the ambient `A^2=4I` phenomenon; our flat result contributes a direct step-circulant parameter classification and finer labelled switching accounting. |
| Lit4 | The 4-regular toral tessellation `T_{2k}` with spectrum `{+-2}` is established and was revisited/generalized in 2026 | **Published/Established** | McKee--Smyth classify it among maximal cyclotomic signed graphs; Stanić, *Discrete Math. Lett.* 17 (2026), 70--74, generalizes the repeating-pattern construction. Do not advertise existence of 4-regular `A^2=4I` signings as new. |

## Consolidated low-end theorem

The proved statements F1, F6, F7, F8 combine into the exact hierarchy

```text
m(N,s) = 2                        iff N=2s+2;
m(N,s) = sqrt(5)                  iff (N,s)=(5,2) or (10,3);
m(N,s) = sqrt(4+sqrt(2))          iff (N,s)=(8,2);
m(N,s) > sqrt(4+sqrt(2))          otherwise.
```

The `N=4s` theorem K4 then refines the third line to an entire exact resonance sequence

`m(4s,s)^2 = 4+2 cos(pi/(2s))`, `s>=2`,

which increases from `4+sqrt(2)` to `6`.

## Hostile-audit corrections

1. The uniform odd `N=3s` constant has been strengthened from the historical `1/70` to `2/139` after rerunning both the local certificate and the `s=9` cyclic base case.
2. The exceptional flat case `(8,3)` must not be called a unique labelled switching class. There are six labelled switching classes; uniqueness holds only after graph automorphisms are allowed.
3. Period-8 fixed-phase spectral formulas are not evidence for a finite global minimum and are excluded from this paper unless they quantify over all competing signings.
4. No statement about general odd `N=ks`, `k>=5`, is promoted above Observed without a proof.
5. The old question whether the universal `sqrt(5)` lower bound is sharp is closed: equality occurs only at `(5,2)` and `(10,3)`.
6. The universal second gap is also completely sharp: equality occurs only at `(8,2)`.
7. The `N=4s` resonance line is now solved exactly for all `s>=2`; it is a finite-global theorem and should replace the old framing in which `N=3s` was the only substantial resonance family.
