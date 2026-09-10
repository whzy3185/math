# Theorem ledger

Status vocabulary is strict:

- **Proved**: complete analytic proof, possibly using an explicitly delimited exact finite certificate.
- **Verified**: exact finite computation only over the stated finite population.
- **Observed**: numerical/experimental evidence.
- **Published/Established**: external public literature.

No result from the separate periodic/Bloch project is used.

| ID | Statement | Status | Evidence / audit note |
|---|---|---|---|
| F0 | `rho(A_sigma)>=2` for every signing of `C_N(1,s)` | **Proved** | `tr A^2=4N`; equality iff `A^2=4I`. |
| F1 | `m(N,s)=2 iff N=2s+2` | **Proved** | Two-walk parity necessity plus explicit equality signing. |
| F3 | On `N=2s+2`, `s!=3`, equality has exactly two labelled switching classes, interchanged by translation | **Proved** | Equality forces the Hamilton holonomy and alternating chord signs. |
| F4 | At `(8,3)=K_(4,4)`, equality signings are order-4 Hadamard blocks | **Proved** | Six labelled switching classes; one orbit after graph automorphisms. |
| F5 | `rho(A)^2 >= 4 + tr((A^2-4I)^2)/(4N)` | **Proved** | Defect-energy inequality for `B=A^2-4I`. |
| F6 | `m(N,s)=sqrt(5) iff (N,s) in {(5,2),(10,3)}` | **Proved** | Index-one integral defect components are negative cliques; liftability closes the parameters. |
| F7 | Outside the flat line and the two `sqrt(5)` pairs, `m(N,s)^2>=4+sqrt(2)` | **Proved** | Integral zero-diagonal defect below `sqrt(2)` has only negative-clique support. |
| F8 | `m(N,s)^2=4+sqrt(2) iff (N,s)=(8,2)` | **Proved** | Signed `P_3` rigidity plus exact characteristic polynomial. |
| PDEF | `supp((A^2-4I) mod 2)` is empty for `N=2s+2`, `Cay(Z_N,{+-2})` for `N=4s`, and `Cay(Z_N,{+-2,+-2s})` otherwise | **Proved** | Frobenius squaring in `F_2[Z_N]`. |
| K4 | For every `s>=2`, `m(4s,s)^2=4+2 cos(pi/(2s))`; exactly two labelled minimizing switching classes | **Proved** | Signed-cycle defect lower bound plus finite anti-periodic construction and mixed-channel rigidity. |
| S6A | If `rho(A_sigma)^2<6`, the integral defect has exactly the forced parity support and entries `+-1` | **Proved** | `lambda_max(B)<2` plus `2x2` interlacing. |
| S6B | If symmetric `X` has `tr X=tr X^3=0`, then `lambda_max(X)^2>=tr(X^2)/n` | **Proved** | Cubic-moment inequality. |
| S6C | Generic triangle-free forced parity support implies `m(N,s)>=sqrt(6)` | **Proved** | `tr B^2=4N`, `tr B^3=0`, then S6B. |
| S6D | Reduced component `C_q(1,t)` contains a triangle iff `t=2`, `q=2t+1`, or `q=3t` | **Proved** | Three-increment arithmetic classification. |
| KSQ6 | For odd `k>=5`, `s>=3`, `m(ks,s)>=sqrt(6)` | **Proved** | Elementary triangle-free parity route. |
| S6G | A connected 4-regular edge-signed graph with smallest eigenvalue `>-2` has order at most 8, unless its underlying graph is `K_5` | **Proved from published classification + analytic audit** | Greaves--Koolen--Munemasa--Sano--Taniguchi, JCTB 110 (2015), Thms. 6,19; corrected double-edge degree sum is 7. |
| S6H | On `overline(C_7)`, the minimum largest eigenvalue is `beta=maxroot(x^3-7x+7)<2`; exactly one labelled sub-2 switching class | **Proved** | Exact triangle-flux reduction and characteristic polynomials. |
| S6N14 | `m(14,s)^2=4+beta` for `s=3,4,5`; `m(14,2)^2>=6` | **Proved** | Mixed-channel rigidity plus exact finite shift factorization. |
| S6R14 | For `s=3,4,5`, the `N=14` minimizers are exactly two labelled switching classes | **Proved** | Alternating diagonal sign `epsilon=+-1`; exact audit. |
| S6FULL | Complete strict sub-`sqrt(6)` classification | **Proved** | `m^2<6` iff `N=2s+2`, `(5,2),(10,3)`, `N=4s`, or `N=14,s=3,4,5`; exact values known. |
| ODD6 | Every odd `N>=7` satisfies `m(N,s)>=sqrt(6)` | **Proved** | Immediate from S6FULL. |
| EQ6Q | Root-quotient lemma at `rho^2<=6` | **Proved** | `K=6I-A^2` is integral PSD Gram with diagonal 2; `+-2` entries are repeated/antipodal roots; quotient gives a signed graph with least eigenvalue `>=-2`. |
| EQ6LOC | Four-locus arithmetic localization for generic `rho(A)^2<=6` | **Proved** | With `q=N/gcd(N,2)`, `t=min(s,q-s)`, only `t=2`, `q=2t+1`, `q=2t+2`, `q=3t` can occur. |
| EQ6ODDLOC | For odd `N`, `m(N,s)<=sqrt(6)` implies `s=2`, `N=2s+1`, or `N=3s` | **Proved** | Odd-order specialization of EQ6LOC. |
| N12S2 | `m(12,2)^2=5+sqrt(3)`; exactly two labelled minimizers | **Proved, exact finite certificate** | All `8192` Hamilton-gauge classes tested in `Q(sqrt(3))`. |
| T2COMP | For `q>=7`, a signing of `C_q(1,2)` has index `<=2` iff `q in {7,8,9,10,12}`; one labelled switching class for each | **Proved** | Five-vertex Gram obstruction plus finite Fourier. |
| EQ6T2 | Complete generic `t=2` locus | **Proved** | Equality only `(12,4),(20,8)`; all at/below-six cases classified. |
| EQ62T1 | Complete `q=2t+1` locus | **Proved** | Multiplier reduction to T2COMP plus exact lift obstructions; no equality. |
| EQ6TWIN | On `N=4r,s=r+-1`, equality occurs iff `(12,4),(16,3),(16,5)` | **Proved** | Repeated-root exclusion for `r>=5`, then flux/antipodal two-walk contradiction. |
| EQ63TCOMP | For every `t>=3`, every signing of `C_(3t)(1,t)` has largest eigenvalue `>2` | **Proved** | 9-vertex local strip for `t>=4`; Gram-kernel argument for `t=3`. |
| EQ6ALL | `m(N,s)^2=6 iff (N,s) in {(12,4),(16,3),(16,5),(20,8)}` | **Proved, complete** | S6FULL plus all four equality loci; exact constructions give attainment. |
| SIXTRI | Complete trichotomy through six | **Proved, complete** | S6FULL below six; EQ6ALL at six; every other pair strictly above six. |
| EQ6RIG | Labelled minimizer counts at the four `m^2=6` pairs are `2,32,32,2` | **Proved** | Exact integer-witness rejection and exact survivor characteristic polynomials. |
| EQ6ISO | Switching-isomorphism orbit counts at the four `m^2=6` pairs are `1,2,2,1` | **Proved** | Short-cycle counts force dihedral automorphism groups; order-16 holonomy sectors remain distinct. |
| E1 | If `N` is even, `m(N,s)^2<=6+2 cos(2pi/N)<8` | **Proved** | Finite anti-periodic signed shift and alternating chord signs; finite Fourier only. |
| ODDSEAM8 | For odd `N=ks`, odd `k>=3`, odd `s>=5`, the alternating seam signing satisfies `8I-A^2=L_Sigma+E_-+E_+` with exactly two rank-two seam defects | **Proved** | Direct exact two-walk channel expansion after multiplication-by-two reindexing. |
| RESP8 | The ODDSEAM8 positivity problem is exactly a `2x2` seam-response test `I-U^T H^-1 U>0` | **Proved** | Rank-one decomposition and Schur complement / matrix determinant lemma. |
| ABSORB8 | Fixed positive-definite local absorbers imply an entire large-`k` vertical family is sub-`sqrt(8)` | **Proved** | Exact seam separation `dist(D_-,D_+)=(k-1)/2`; disjoint local forms plus remaining signed-edge squares. |
| STEP3K8 | For every `k>=3`, `m(3k,3)<sqrt(8)` | **Proved** | Even `k`: E1; odd `k`: one collided defect absorbed by three negative two-edge paths. |
| STEP5K8 | For every `k>=3`, `m(5k,5)<sqrt(8)` | **Proved** | Even `k`: E1; odd large `k`: fixed absorbers; finite exact bases close the rest. |
| STEP7K8 | `m(7k,7)<sqrt(8) iff k>=4` | **Proved** | `k=3` has exact obstruction `18/131`; all `k>=4` have finite constructions. |
| STEP9K8 | `m(9k,9)<sqrt(8) iff k>=4` | **Proved** | `k=3` is obstructed; all `k>=4` have exact/absorber constructions. |
| STEP11K8 | `m(11k,11)<sqrt(8) iff k>=4` | **Proved** | Horizontal obstruction at `k=3`; even-order theorem; exact modified `k=5`; finite bases and fixed absorbers. |
| STEP13K8 | `m(13k,13)<sqrt(8) iff k>=4` | **Proved** | Horizontal obstruction at `k=3`; exact modified `k=5`; finite bases and fixed absorbers. |
| STEP15K8 | For step 15: `m(45,15)>sqrt(8)` and `m(15k,15)<sqrt(8)` for `k=4` or `k>=6`; only `(75,15)` remains open | **Proved on stated range** | `k=7` two-chord-flip exact LDL; odd `k>=9` exact bases/absorbers; even `k` by E1. Search failure at `k=5` is only Observed. |
| STEP17K8 | For step 17: `m(51,17)>sqrt(8)` and `m(17k,17)<sqrt(8)` for `k=4` or `k>=6`; only `(85,17)` remains open | **Proved on stated range** | `k=7` modified exact LDL; odd `k>=9` exact bases/absorbers; even `k` by E1. `k=5` remains Open. |
| R1 | `m(9,3)<sqrt(8)` | **Proved** | Exact Sylvester certificate. |
| R2 | `m(15,5)<sqrt(8)` | **Proved** | Exact Sylvester certificate. |
| L9 | Nine-column signed-triangle local rule at excess `24/1667` | **Proved, exact finite lemma** | Exact integer pruning counts `8,56,152,440,488,1016,656,1064,128`; all final survivors alternate in six middle transitions. |
| B7 | Every signing of `C_21(1,7)` has squared radius at least `8+18/131` | **Proved, exhaustive exact certificate** | `49,940` Q-necklaces and `199,760` gauge representatives. |
| B9 | Every signing of `C_27(1,9)` has squared radius at least `8+24/1667` | **Proved, exhaustive exact certificate** | 1,064 surviving length-8 prefixes; all `17,024` final cyclic candidates have exact integer witnesses at the stronger margin. |
| R3 | For every odd `s>=7`, `m(3s,s)^2>=8+24/1667` | **Proved, computer-assisted local lemma + analytic propagation** | B7 + upgraded B9 + upgraded L9; seam contradiction for odd `s>=11`. |
| R4 | `m(3s,s)<sqrt8 iff s` is even or `s in {3,5}` | **Proved** | E1 + R1/R2 + R3. |
| N5LOCAL13 | Any 13-column open width-five strip with `rho^2<8` has at least one complement among its two central transitions | **Proved, exact finite lemma** | 320-action switching/dihedral/complement quotient. Prefix survivors `1,7,33,130,548,1867,3870,10080`; 7,392 central-double-bad length-9 candidates reduce to 71, then extensions `204 -> 135 -> 1 -> 0`. Every rejection uses an exact integer Rayleigh witness. |
| L9CRIT | Nine-column finite-state transition is numerically near excess `0.014397239...` | **Observed** | Reconnaissance only; not used in any theorem. |
| Kodd8 | Exact sub-`sqrt8` classification for all odd resonances | **Open** | Horizontal `k=3` is complete; vertical `s=3,5,7,9,11,13` are complete; steps 15 and 17 each have only the `k=5` base unresolved. N5LOCAL13 is the first all-signing rigidity lemma for the next horizontal line `N=5s`; isolated non-complement transitions remain to be classified. |
| P8 | A fixed period-8 phase determines the global finite minimum for all `C_{8L}(1,2)` | **Rejected historical overclaim** | Historical correction branch withdraws the global conclusion; excluded from this paper. |
| Lit1 | Fixed-underlying-graph signature minimization is an established general problem | **Published/Established** | Belardo--Cioabă--Koolen--Wang (2018), Problem 3.18. |
| Lit2 | Signed/integer symmetric matrices with spectrum in `[-2,2]` are classified | **Published/Established** | McKee--Smyth, J. Algebra 317 (2007). |
| Lit3 | Signed graphs with just two adjacency eigenvalues, including degree-at-most-4 phenomena, are established | **Published/Established** | Hou--Tang--Wang, Discrete Math. 342 (2019). |
| Lit4 | Connected edge-signed graphs with least eigenvalue `>-2` are structurally classified | **Published/Established** | Greaves et al., JCTB 110 (2015). |
| Lit5 | Connected signed graphs with least eigenvalue `>=-2` have signed-line-graph/star-complement structure | **Published/Established** | Rowlinson--Stanić, Appl. Math. Comput. 423 (2022); used only after root quotient when relevant. |

## Consolidated finite-global package

### I. Complete classification through `sqrt(6)`

Let `beta` be the largest root of `x^3-7x+7`.

```text
m(N,s)^2 < 6 iff
  N=2s+2,                         m^2=4; or
  (N,s)=(5,2),(10,3),             m^2=5; or
  N=4s,                           m^2=4+2 cos(pi/(2s)); or
  N=14 and s=3,4,5,               m^2=4+beta.

m(N,s)^2 = 6 iff
  (N,s)=(12,4),(16,3),(16,5),(20,8).

Every other admissible pair has m(N,s)>sqrt(6).
```

At the four equality pairs, labelled minimizer counts are `2,32,32,2` and switching-isomorphism orbit counts are `1,2,2,1`.

### II. `sqrt(8)` threshold

```text
N even => m(N,s)^2 <= 6+2 cos(2pi/N) < 8.

N=3s:
  m(3s,s)<sqrt8 iff s is even or s in {3,5};
  odd s>=7 => m(3s,s)^2 >= 8+24/1667.

Vertical fixed odd steps:
  s=3,5: sub-sqrt8 for every k>=3;
  s=7,9,11,13: sub-sqrt8 iff k>=4;
  s=15,17: k=3 is obstructed and every k>=4 except k=5 is proved sub-sqrt8; k=5 remains open.

N=5s local rigidity:
  in every sub-sqrt8 13-column open width-five strip, the two central transitions cannot both be non-complement.
```

For odd `k,s`, the positive construction is reduced to a signed-Laplacian plus two seam defects, equivalently to a `2x2` response matrix; fixed local absorbers reduce any fixed step to finitely many small chord-cycle lengths.

## Hostile-audit corrections and upgrades

1. Historical odd `N=3s` excess `1/70` was first strengthened to `2/139` and is now strengthened further to `24/1667`.
2. The stronger margin requires an enlarged exact integer-witness search; merely editing the denominator in the historical script is not a proof.
3. `(8,3)` has six labelled switching classes, not one.
4. Fixed period-8 dispersion/global-minimum claims are excluded after the historical correction branch.
5. The doubled-edge representation-graph degree identity in the Greaves reduction is `d(a)+d(b)=7`.
6. Strict sub-six and equality at six are distinct: `+-2` defect entries occur at equality, so root quotienting is mandatory.
7. The formerly open `m^2=6` boundary is completely classified.