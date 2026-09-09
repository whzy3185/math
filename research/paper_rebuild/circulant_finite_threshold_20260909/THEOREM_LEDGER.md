# Theorem ledger

Status vocabulary is strict:

- **Proved**: complete analytic proof, possibly using an explicitly delimited exact finite certificate.
- **Verified**: exact finite computation only over the stated finite population.
- **Observed**: numerical/experimental evidence.
- **Published/Established**: external public literature.

| ID | Statement | Status | Evidence / audit note |
|---|---|---|---|
| F0 | `rho(A_sigma)>=2` for every signing of `C_N(1,s)` | **Proved** | `tr A^2=4N`; equality iff `A^2=4I`. |
| F1 | `m(N,s)=2 iff N=2s+2` | **Proved** | Parity/two-walk necessity and explicit alternating signing. |
| F3 | On `N=2s+2`, `s!=3`, equality has exactly two labelled switching classes, interchanged by translation | **Proved** | Equality forces alternating chord signs and the Hamilton holonomy. |
| F4 | At `(8,3)=K_{4,4}`, equality signings are order-4 Hadamard blocks | **Proved** | Six labelled switching classes; one orbit only after graph automorphisms. |
| F5 | `rho(A)^2 >= 4 + tr((A^2-4I)^2)/(4N)` | **Proved** | Defect-energy inequality for `B=A^2-4I`. |
| F6 | `m(N,s)=sqrt(5) iff (N,s) in {(5,2),(10,3)}` | **Proved** | Index-one defect components are negative cliques; parity/liftability closes the parameters. |
| F7 | Outside the flat line and the two `sqrt(5)` pairs, `m(N,s)^2>=4+sqrt(2)` | **Proved** | Integral zero-diagonal defect below `sqrt(2)` has only negative-clique support components. |
| F8 | `m(N,s)^2=4+sqrt(2) iff (N,s)=(8,2)` | **Proved** | Signed `P_3` rigidity plus exact characteristic polynomial. |
| PDEF | `supp((A^2-4I) mod 2)` is empty for `N=2s+2`, `Cay(Z_N,{+-2})` for `N=4s`, and `Cay(Z_N,{+-2,+-2s})` otherwise | **Proved** | Frobenius squaring in `F_2[Z_N]`. |
| K4 | For every `s>=2`, `m(4s,s)^2=4+2 cos(pi/(2s))`; exactly two labelled minimizing switching classes | **Proved** | Signed-cycle defect lower bound plus finite anti-periodic shift construction and mixed-channel rigidity. |
| S6A | If `rho(A_sigma)^2<6`, then `supp(A_sigma^2-4I)=supp((A_sigma^2-4I) mod 2)` | **Proved** | `lambda_max(B)<2`; integrality and `2x2` interlacing force entries `0,+-1`. |
| S6B | If symmetric `X` has `tr X=tr X^3=0`, then `lambda_max(X)^2>=tr(X^2)/n` | **Proved** | Cubic-moment inequality. |
| S6C | Generic triangle-free forced parity support implies `m(N,s)>=sqrt(6)` | **Proved** | `tr B^2=4N`, `tr B^3=0`, then S6B. |
| S6D | The reduced generic parity component `C_q(1,t)` contains a triangle iff `t=2`, `q=2t+1`, or `q=3t` | **Proved** | Three-increment arithmetic classification. |
| KSQ6 | For odd `k>=5`, `s>=3`, `m(ks,s)>=sqrt(6)` | **Proved** | Elementary triangle-free parity proof; retained as classification-free route. |
| S6G | A connected 4-regular edge-signed graph with smallest eigenvalue `>-2` has order at most 8, unless its underlying graph is `K_5` | **Proved from published classification + analytic audit** | Greaves--Koolen--Munemasa--Sano--Taniguchi, JCTB 110 (2015), Thms. 6,19; corrected double-edge degree sum is 7. |
| S6H | On `overline(C_7)`, the minimum largest eigenvalue is `beta=maxroot(x^3-7x+7)<2`; exactly one labelled switching class is sub-2 | **Proved, exact finite lemma** | Two all-negative-triangle tree-gauge classes; exact characteristic polynomials. |
| S6N14 | `m(14,s)^2=4+beta` for `s=3,4,5`; `m(14,2)^2>=6` | **Proved** | Sub-six lift forces `DT=-TD`; exact finite shift factorization. |
| S6R14 | For `s=3,4,5`, the `N=14` minimizers are exactly two labelled switching classes | **Proved** | Alternating diagonal sign `epsilon=+-1`, unique holonomy; exhaustive gauge audit agrees. |
| S6FULL | Complete strict sub-`sqrt(6)` classification | **Proved** | `m^2<6` iff `N=2s+2`, or `(5,2),(10,3)`, or `N=4s`, or `N=14,s=3,4,5`; exact values `4`, `5`, `4+2cos(pi/(2s))`, `4+beta`. |
| ODD6 | Every odd `N>=7` satisfies `m(N,s)>=sqrt(6)` for all admissible `s` | **Proved** | Immediate from S6FULL. Thus all odd resonance pairs `N=ks` with odd `k,s>=3` have the same universal floor. |
| EQ6Q | Root-quotient lemma at the non-strict six boundary | **Proved** | If `rho(A)^2<=6`, then `K=6I-A^2` is an integral PSD Gram matrix with diagonal 2. Entries `+-2` are exactly repeated/antipodal roots; quotienting yields a signed graph with smallest eigenvalue `>=-2`. |
| EQ6LOC | Four-locus arithmetic localization for `rho(A)^2<=6` | **Proved (new)** | With `q=N/gcd(N,2)`, `t=min(s,q-s)`, away from `N=2s+2,4s`, one must have `t=2`, `q=2t+1`, `q=2t+2`, or `q=3t`. A size-2 defect entry forces twins; `C_q(1,t)` has twins iff `q=2t+2`; triangle-free duplicate-free equality collapses to the flat theorem. |
| EQ6ODDLOC | For odd `N`, `m(N,s)<=sqrt(6)` implies `s=2`, `N=2s+1`, or `N=3s` | **Proved (new)** | Odd-order specialization of EQ6LOC. Every other odd pair satisfies the strict bound `m(N,s)>sqrt(6)`. |
| EQ6EX | `m(12,4)^2=m(16,3)^2=m(16,5)^2=m(20,8)^2=6` | **Proved** | Exact finite constructions; `(16,3)` has repeated-root defect and `(16,5)` follows by multiplier isomorphism. |
| EQ6TWIN | On the twin locus `N=4r, s=r+-1`, equality `m^2=6` occurs iff `(N,s)` is `(12,4),(16,3),(16,5)` | **Proved (new)** | For `r>=5`, duplicate roots are excluded by displacement; flat defect rigidity then contradicts induced flux for odd `r` and an antipodal `-4` two-walk entry for even `r`. |
| N12S2 | `m(12,2)^2=5+sqrt(3)` and there are exactly two labelled minimizing switching classes | **Proved, exact finite certificate (new)** | All `2^13=8192` Hamilton-gauge switching classes are tested by exact PSD arithmetic in `Q(sqrt(3))`; exactly two survive and have `chi_A=(x^2-2)^2(x^4-10x^2+22)^2`. |
| T2COMP | For `q>=7`, a signing of `C_q(1,2)` has index `<=2` iff `q in {7,8,9,10,12}`; for each such `q` exactly one labelled switching class exists | **Proved (new)** | A `5x5` Gram determinant table forces every consecutive triangle negative. Then `C=T+T^-1-T^2-T^-2`; finite Fourier gives the exact order/holonomy list. |
| EQ6T2 | Complete generic `t=2` locus at and below six | **Proved (new)** | Away from `N=2s+2,4s`, `m^2<=6` iff `(N,s)` is `(5,2),(10,3),(12,4),(14,5),(20,8)`; equality occurs only at `(12,4),(20,8)`. Uses T2COMP plus exact lift equations. |
| EQ6ALL | Complete classification of all pairs with `m(N,s)^2=6` | **Open, sharply reduced** | EQ6LOC + EQ6TWIN + EQ6T2 reduce every unclassified equality pair to only `q=2t+1` or `q=3t`. |
| E1 | If `N` is even, `m(N,s)^2<=6+2 cos(2pi/N)<8` | **Proved** | Finite anti-periodic signed shift and alternating chord signs; finite Fourier only. |
| R1 | `m(9,3)<sqrt(8)` | **Proved** | Exact Sylvester certificate; leading minors `4,16,60,209,722,2508,5746,15993,47304`. |
| R2 | `m(15,5)<sqrt(8)` | **Proved** | Exact Sylvester certificate; final determinant `8636544`. |
| L9 | Nine-column signed-triangle local rule at excess `2/139` | **Proved, exact finite lemma** | Exact integer pruning counts `8,56,152,440,488,1016,656,1064,128`; all final survivors alternate in the six middle transitions. |
| B7 | Every signing of `C_21(1,7)` has squared radius at least `8+18/131` | **Proved, exhaustive exact certificate** | `49,940` Q-necklaces and `199,760` representatives. |
| B9 | Every signing of `C_27(1,9)` has squared radius at least `8+2/139` | **Proved, exhaustive exact certificate** | `17,024` final cyclic candidates after exact prefix pruning. |
| R3 | For odd `s>=7`, `m(3s,s)^2>=8+2/139` | **Proved, computer-assisted local lemma + analytic propagation** | Exact bases `s=7,9`; nine-column alternation plus seam contradiction for `s>=11`. |
| R4 | `m(3s,s)<sqrt8 iff s` is even or `s in {3,5}` | **Proved** | E1 + R1/R2 + R3. |
| P8 | A fixed period-8 phase determines the global finite minimum for all `C_{8L}(1,2)` | **Rejected historical overclaim** | Historical correction branch withdraws the global conclusion; fixed-phase dispersion is excluded. |
| Kodd8 | Exact sub-`sqrt8` classification for odd `k>=5` | **Open** | ODD6 gives the `sqrt6` floor; general `sqrt8` behavior is unresolved outside `k=3`. |
| Lit1 | Fixed-underlying-graph signature minimizing spectral radius is an established general problem | **Published/Established** | Belardo--Cioabă--Koolen--Wang (2018), Problem 3.18. |
| Lit2 | Signed graphs with all eigenvalues in `[-2,2]` are classified | **Published/Established** | McKee--Smyth, *J. Algebra* 317 (2007). |
| Lit3 | Degree-at-most-4 signed graphs with two adjacency eigenvalues are classified | **Published/Established** | Hou--Tang--Wang, *Discrete Math.* 342 (2019). |
| Lit4 | 4-regular `A^2=4I` toral/two-eigenvalue phenomena are established | **Published/Established** | McKee--Smyth; Stanić (2026). |
| Lit5 | Connected edge-signed graphs with smallest eigenvalue `>-2` are structurally classified | **Published/Established** | Greaves et al., *JCTB* 110 (2015), 90--111. |
| Lit6 | Connected signed graphs with smallest eigenvalue `>=-2` have a signed-line-graph/star-complement classification | **Published/Established** | Rowlinson--Stanić, *Appl. Math. Comput.* 423 (2022), 126991. Relevant only after EQ6Q root quotient. |

## Consolidated finite-global package

### I. Complete strict spectrum below `sqrt(6)`

Let `beta` be the largest root of `x^3-7x+7`.

```text
m(N,s)^2 < 6 iff

N=2s+2:                         m^2=4;
(N,s)=(5,2),(10,3):             m^2=5;
N=4s:                           m^2=4+2 cos(pi/(2s));
N=14, s=3,4,5:                  m^2=4+beta.
```

Every other pair has `m(N,s)^2>=6`.

### II. Non-strict boundary progress

Away from the already separated flat and `N=4s` families,

```text
m(N,s)^2 <= 6
=> reduced (q,t) lies on
   t=2, q=2t+1, q=2t+2, or q=3t.
```

The twin line `q=2t+2` is completely closed, and the full `t=2` locus is completely closed. Therefore any still-unclassified equality pair `m^2=6` must satisfy

```text
q=2t+1 or q=3t.
```

Known equality pairs remain

```text
(12,4), (16,3), (16,5), (20,8).
```

No claim is yet made that this list is complete.

### III. `sqrt(8)` threshold

```text
N even  =>  m(N,s)^2 <= 6+2 cos(2pi/N)<8.

m(3s,s)<sqrt8  iff  s is even or s in {3,5}.

odd s>=7  =>  m(3s,s)^2>=8+2/139.
```

## Hostile-audit corrections

1. Historical `1/70` on odd `N=3s` is strengthened to `2/139`.
2. `(8,3)` has six labelled switching classes, not one.
3. Fixed period-8 dispersion is excluded from the finite-global theorem package.
4. The corrected doubled-edge line-graph count in the Greaves reduction is `d(a)+d(b)=7`.
5. Strict sub-six and equality at six are distinct: at equality, defect entries `+-2` genuinely occur (already at `(16,3)`), so quotienting repeated roots is mandatory.
6. Equality at six is now localized arithmetically; the twin and `t=2` loci are no longer open.