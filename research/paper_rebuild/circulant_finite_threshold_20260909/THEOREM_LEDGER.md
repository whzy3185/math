# Theorem ledger

Status vocabulary is strict:

- **Proved**: complete analytic proof, possibly with an explicitly delimited exact finite certificate.
- **Verified**: exact finite computation only over the stated finite population.
- **Observed**: numerical/experimental evidence.
- **Published/Established**: external public literature.

No result from the separate periodic/Bloch project is used.

| ID | Statement | Status | Evidence / audit note |
|---|---|---|---|
| F0 | `rho(A_sigma)>=2` for every signing of `C_N(1,s)` | **Proved** | `tr A^2=4N`; equality iff `A^2=4I`. |
| F1 | `m(N,s)=2 iff N=2s+2` | **Proved** | Two-walk parity necessity plus explicit equality signing. |
| F3 | On `N=2s+2`, `s!=3`, equality has exactly two labelled switching classes, interchanged by translation | **Proved** | Hamilton holonomy and alternating chord signs are forced. |
| F4 | At `(8,3)=K_(4,4)`, flat equality is the order-4 Hadamard case | **Proved** | Six labelled switching classes; one orbit after graph automorphisms. |
| F5 | `rho(A)^2 >= 4 + tr((A^2-4I)^2)/(4N)` | **Proved** | Defect-energy inequality. |
| F6 | `m(N,s)=sqrt(5) iff (N,s) in {(5,2),(10,3)}` | **Proved** | Index-one integral defect components are negative cliques; liftability closes the parameters. |
| F7 | Outside the flat line and the two `sqrt(5)` pairs, `m(N,s)^2>=4+sqrt(2)` | **Proved** | Integral zero-diagonal defect rigidity. |
| F8 | `m(N,s)^2=4+sqrt(2) iff (N,s)=(8,2)` | **Proved** | Signed `P_3` rigidity plus exact characteristic polynomial. |
| PDEF | Exact support of `(A^2-4I) mod 2` | **Proved** | Frobenius squaring in `F_2[Z_N]`; empty on `N=2s+2`, `+-2` on `N=4s`, generic `+-2,+-2s` otherwise. |
| K4 | `m(4s,s)^2=4+2 cos(pi/(2s))` for every `s>=2`; exactly two labelled minimizers | **Proved** | Signed-cycle defect lower bound plus finite anti-periodic construction and rigidity. |
| S6B | If symmetric `X` has `tr X=tr X^3=0`, then `lambda_max(X)^2>=tr(X^2)/n` | **Proved** | Cubic-moment inequality. |
| S6D | Reduced component `C_q(1,t)` contains a triangle iff `t=2`, `q=2t+1`, or `q=3t` | **Proved** | Three-increment arithmetic classification. |
| S6G | A connected 4-regular edge-signed graph with least eigenvalue `>-2` has order at most 8, unless the underlying graph is `K_5` | **Proved from published classification + internal audit** | Greaves--Koolen--Munemasa--Sano--Taniguchi, JCTB 110 (2015); doubled-edge degree identity corrected to `d(a)+d(b)=7`. |
| S6H | On `overline(C_7)`, the minimum largest eigenvalue is `beta=maxroot(x^3-7x+7)<2`; one labelled sub-2 class | **Proved** | Exact flux reduction and characteristic polynomials. |
| S6FULL | Complete strict sub-`sqrt(6)` classification | **Proved, complete** | `m^2<6` iff `N=2s+2`, `(5,2),(10,3)`, `N=4s`, or `N=14,s=3,4,5`; exact values known. |
| ODD6 | Every odd `N>=7` satisfies `m(N,s)>=sqrt(6)` | **Proved** | Consequence of S6FULL. |
| EQ6Q | Root-quotient lemma at `rho^2<=6` | **Proved** | `6I-A^2` is an integral PSD Gram matrix with diagonal 2; `+-2` entries are repeated/antipodal roots. |
| EQ6LOC | Four-locus arithmetic localization for generic `rho(A)^2<=6` | **Proved** | Only `t=2`, `q=2t+1`, `q=2t+2`, `q=3t` can occur. |
| T2COMP | For `q>=7`, a signing of `C_q(1,2)` has index `<=2` iff `q in {7,8,9,10,12}`; one labelled class for each | **Proved** | Five-vertex Gram rule plus finite Fourier. |
| EQ63TCOMP | For every `t>=3`, every signing of `C_(3t)(1,t)` has largest eigenvalue `>2` | **Proved** | Nine-vertex local strip plus the `t=3` Gram-kernel argument. |
| EQ6ALL | `m(N,s)^2=6 iff (N,s) in {(12,4),(16,3),(16,5),(20,8)}` | **Proved, complete** | All four localized equality mechanisms closed; exact constructions attain the four pairs. |
| SIXTRI | Complete trichotomy through six | **Proved, complete** | S6FULL below six; EQ6ALL at six; every other pair strictly above six. |
| EQ6RIG | Labelled minimizer counts at the four `m^2=6` pairs are `2,32,32,2` | **Proved** | Exact integer-witness rejection and exact survivor characteristic polynomials. |
| EQ6ISO | Switching-isomorphism orbit counts at the four `m^2=6` pairs are `1,2,2,1` | **Proved** | Short-cycle counts force the relevant automorphism groups; order-16 holonomy sectors remain distinct. |
| N12S2 | `m(12,2)^2=5+sqrt(3)`; exactly two labelled minimizers | **Proved, exact finite certificate** | All 8192 Hamilton-gauge classes tested in `Q(sqrt(3))`. |
| E1 | If `N` is even, `m(N,s)^2<=6+2 cos(2pi/N)<8` | **Proved** | Finite anti-periodic signed shift and alternating chord signs; finite Fourier only. |
| ODDSEAM8 | For odd `N=ks`, odd `k>=3`, odd `s>=5`, the alternating-seam signing gives `8I-A^2=L_Sigma+E_-+E_+` with exactly two seam defects | **Proved** | Direct exact two-walk expansion after multiplication-by-two reindexing. |
| RESP8 | ODDSEAM8 positivity is exactly a `2x2` seam-response test `I-U^T H^-1 U>0` | **Proved** | Rank-one decomposition and Schur complement. |
| ABSORB8 | Fixed positive-definite local absorbers certify an entire sufficiently-large-`k` vertical family | **Proved** | Exact seam separation plus signed-edge-square decomposition. |
| STEP3K8 | `m(3k,3)<sqrt(8)` for every `k>=3` | **Proved** | Even `k`: E1; odd `k`: collided seam defect absorbed analytically. |
| STEP5K8 | `m(5k,5)<sqrt(8)` for every `k>=3` | **Proved** | Finite bases plus fixed absorbers. |
| STEP7K8 | `m(7k,7)<sqrt(8) iff k>=4` | **Proved** | `k=3` global obstruction; all `k>=4` finite constructions. |
| STEP9K8 | `m(9k,9)<sqrt(8) iff k>=4` | **Proved** | Same threshold mechanism. |
| STEP11K8 | `m(11k,11)<sqrt(8) iff k>=4` | **Proved** | Modified exact `k=5` base plus absorber theorem. |
| STEP13K8 | `m(13k,13)<sqrt(8) iff k>=4` | **Proved** | Modified exact `k=5` base plus absorber theorem. |
| STEP15K8 | `m(15k,15)<sqrt(8) iff k=4 or k>=6` | **Proved, complete** | `k=3` by N=3s obstruction; `k=5` by all-signing N=5s obstruction; even `k` by E1; odd `k>=7` by exact constructions/absorbers. |
| STEP17K8 | `m(17k,17)<sqrt(8) iff k=4 or k>=6` | **Proved, complete** | Same closure; `(85,17)` is no longer open. |
| R1 | `m(9,3)<sqrt(8)` | **Proved** | Exact Sylvester certificate. |
| R2 | `m(15,5)<sqrt(8)` | **Proved** | Exact Sylvester certificate. |
| L9 | Nine-column triangle-strip rule at excess `24/1667` | **Proved, exact finite lemma** | Survivor counts `8,56,152,440,488,1016,656,1064,128`; all final survivors alternate in the six middle transitions. |
| B7 | `m(21,7)^2>=8+18/131` | **Proved, exhaustive exact certificate** | 49,940 Q-necklaces and 199,760 Hamilton-gauge representatives. |
| B9 | `m(27,9)^2>=8+24/1667` | **Proved, exhaustive exact certificate** | 1,064 surviving length-8 prefixes; all 17,024 final cyclic candidates exactly rejected. |
| R3 | For odd `s>=7`, `m(3s,s)^2>=8+24/1667` | **Proved** | Exact bases plus local-to-global alternation and seam contradiction. |
| R4 | `m(3s,s)<sqrt8 iff s` is even or `s in {3,5}` | **Proved, complete** | E1 + R1/R2 + R3. |
| N5LOCAL13 | In a sub-`sqrt8` 13-column width-five strip, the two central transitions cannot both be defects | **Proved, exact finite lemma** | 320-action quotient; exact survivor chain closes at zero. |
| N5SINGLE14 | A 14-column width-five strip with one defect and complement context `5/7` has `rho^2>=8` | **Proved, exact finite lemma** | Seven D5 defect types, each with explicit integer Rayleigh witness. |
| N5GAP24 | Positive even defect gaps `g=2,4` are excluded with the stated three external context transitions | **Proved, exact finite lemma** | Exact chains `12->61->8->0` and `12->57->1->0`. |
| N5GAP6_14 | Even gaps `g=6,8,10,12,14` are excluded with one arbitrary transition on each side | **Proved, exact finite lemma** | 121 central orbits ->12; all contextual extensions exactly close. |
| N5GAP16_30 | Even gaps `g=16,18,20,22,24,26,28,30` are excluded with one arbitrary transition on each side | **Proved, exact finite lemma** | Stable chain `121->12`, `336->6`, `168->0`; six one-sided boundary states identified. |
| N5HALF19 | If `(*,d,31^19)` is sub-threshold then, up to D5, it is `(31,15,31^19)` | **Proved, exact finite lemma** | 128 one-sided orbit candidates -> one survivor. |
| N5LONGEVEN | Every even defect gap `g>=20` is excluded with one arbitrary transition on each side | **Proved** | N5HALF19 reduces to three relative defect types; explicit parametric witnesses satisfy `w^T(M^2-8I)w=4`, `w^Tw=485g+2177` for every even `g>=14`. |
| N5CLUSTER | Fixed odd-gap clusters `31^9 d 31 e 31^9`, `31^7 d 31^3 e 31^7`, `31^6 d 31 e 31 f 31^6` are impossible below `sqrt8` | **Proved, exact finite lemmas** | D5 orbit counts respectively `121->0`, `121->0`, `3151->0`. |
| N5BASE1517 | `m(75,15)>=sqrt8` and `m(85,17)>=sqrt8` | **Proved, all-signing exact certificate** | Local gap reduction plus complete helical-seam residual audit. |
| N5BASE1921 | `m(95,19)>=sqrt8` and `m(105,21)>=sqrt8` | **Proved, all-signing exact certificate** | Residual patterns `(16,1),(14,3),(14,1,1)` and `(18,1),(16,3),(16,1,1)` all exactly closed. |
| N5FULL | `m(5s,s)<sqrt8 iff s` is even or `s in {3,5,7,9,11,13}` | **Proved, complete** | Uniform even-gap theorem + fixed cluster rules + four cyclic bases `s=15,17,19,21`; positive side from E1 and vertical constructions. |
| L9CRIT | Numerical transition for the nine-column `N=3s` local rule is near excess `0.014397239...` | **Observed** | Reconnaissance only; not used in a theorem. |
| Kodd8 | Complete `sqrt8` classification for all odd resonances `N=ks` | **Open** | Horizontal lines `k=3` and `k=5` are now complete.  General odd `k>=7` remains open; the seam-response framework controls a large positive region. |
| P8 | A fixed period-8 phase determines the global finite minimum for all `C_(8L)(1,2)` | **Rejected historical overclaim** | Historical correction branch withdraws the global conclusion; excluded from this paper. |
| Lit1 | Fixed-underlying-graph signature minimization is an established general problem | **Published/Established** | Belardo--Cioabă--Koolen--Wang (2018), Problem 3.18. |
| Lit2 | Signed/integer symmetric matrices with spectrum in `[-2,2]` are classified | **Published/Established** | McKee--Smyth, J. Algebra 317 (2007). |
| Lit3 | Signed graphs with two adjacency eigenvalues are established | **Published/Established** | Hou--Tang--Wang, Discrete Math. 342 (2019). |
| Lit4 | Connected edge-signed graphs with least eigenvalue `>-2` are structurally classified | **Published/Established** | Greaves et al., JCTB 110 (2015). |
| Lit5 | Connected signed graphs with least eigenvalue `>=-2` have signed-line-graph/star-complement structure | **Published/Established** | Rowlinson--Stanić, Appl. Math. Comput. 423 (2022); relevant only after root quotient. |

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

At the four equality pairs the labelled minimizer counts are `2,32,32,2`, and the switching-isomorphism orbit counts are `1,2,2,1`.

### II. Two complete horizontal thresholds at `sqrt(8)`

```text
N even => m(N,s)^2 <= 6+2 cos(2pi/N) < 8.

N=3s:
  m(3s,s)<sqrt8 iff s is even or s in {3,5};
  odd s>=7 => m(3s,s)^2 >= 8+24/1667.

N=5s:
  m(5s,s)<sqrt8 iff s is even or s in {3,5,7,9,11,13};
  odd s>=15 => m(5s,s)>=sqrt8.
```

### III. Current general resonance frontier

The first two odd horizontal resonance lines `k=3,5` are fully classified.  The next target is a structural theorem for odd `k>=7`, ideally coupling the all-signing strip/flux obstructions with the two-port seam-response construction on the positive side.

## Hostile-audit corrections and upgrades

1. The historical odd `N=3s` excess `1/70` was strengthened first to `2/139` and then to `24/1667`.
2. `(8,3)` has six labelled switching classes, not one.
3. The fixed period-8 dispersion/global-minimum overclaim is excluded.
4. Strict sub-six and equality at six are distinct: `+-2` defect entries genuinely occur at equality, requiring root quotienting.
5. The formerly open `m^2=6` boundary is completely classified.
6. The formerly open step-15/17 `k=5` bases are closed by the all-signing width-five theorem.
7. The `N=5s` horizontal threshold is now complete; its negative side is not inferred from the explicit seam construction but proved over all signings.