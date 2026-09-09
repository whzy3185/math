# Theorem ledger

Status vocabulary is strict:

- **Proved**: complete analytic proof, possibly using an explicitly delimited exact finite certificate.
- **Verified**: exact finite computation only over the stated finite population.
- **Observed**: numerical/experimental evidence.
- **Published/Established**: external public literature.

| ID | Statement | Status | Evidence / audit note |
|---|---|---|---|
| F0 | `rho(A_sigma)>=2` for every signing of `C_N(1,s)` | **Proved** | `tr A^2=4N`; equality iff `A^2=4I`. This is the 4-regular case of the standard average-degree/weighing-matrix bound. |
| F1 | `m(N,s)=2 iff N=2s+2` | **Proved** | Outside the flat line the displacement-2 two-walk channel has odd multiplicity; on the flat line an explicit alternating Hamilton-gauge signing has `A^2=4I`. |
| F3 | On `N=2s+2`, `s!=3`, equality has exactly two labelled switching classes, interchanged by translation | **Proved** | Equality forces `tau_i=-tau_(i-1)` and the Hamilton holonomy. |
| F4 | At `(8,3)=K_{4,4}`, equality signings are order-4 Hadamard blocks | **Proved** | Six labelled switching classes; one orbit only after graph automorphisms. |
| F5 | `rho(A)^2 >= 4 + tr((A^2-4I)^2)/(4N)` | **Proved** | Defect-energy inequality for `B=A^2-4I`. |
| F6 | `m(N,s)=sqrt(5) iff (N,s) in {(5,2),(10,3)}` | **Proved** | `lambda_max(B)=1` forces negative-clique defect components; parity reduces to `N=5,10`; `(10,2)` is excluded by triangle flux and the two stated pairs are attained by conference-core constructions. |
| F7 | Outside the flat line and the two `sqrt(5)` pairs, `m(N,s)^2>=4+sqrt(2)` | **Proved** | Integral zero-diagonal defect below `sqrt(2)` has only negative-clique support components. |
| F8 | `m(N,s)^2=4+sqrt(2) iff (N,s)=(8,2)` | **Proved** | Induced signed `P_3` rigidity plus fixed parity support; exact characteristic polynomial `(x^4-8x^2+14)^2`. |
| PDEF | `supp((A^2-4I) mod 2)` is empty for `N=2s+2`, `Cay(Z_N,{+-2})` for `N=4s`, and `Cay(Z_N,{+-2,+-2s})` otherwise | **Proved** | Frobenius squaring in `F_2[Z_N]`. |
| K4 | For every `s>=2`, `m(4s,s)^2=4+2 cos(pi/(2s))`; exactly two labelled minimizing switching classes | **Proved** | Below defect index 2, PDEF forces two signed `2s`-cycles. The optimum is two unbalanced cycles; finite anti-periodic signed-shift construction attains it. |
| S6A | If `rho(A_sigma)^2<6`, then `supp(A_sigma^2-4I)=supp((A_sigma^2-4I) mod 2)` | **Proved** | `M=lambda_max(B)<2`; every `2x2` principal block and integrality force entries to `0,+-1`, so parity fixes support exactly. |
| S6B | If symmetric `X` has `tr X=tr X^3=0`, then `lambda_max(X)^2>=tr(X^2)/n` | **Proved** | Sum `(M-mu)(mu+M)^2/M>=0`; equality iff `X^2=M^2I`. |
| S6C | Away from `N=2s+2,4s`, if `Cay(Z_N,{+-2,+-2s})` is triangle-free, then `m(N,s)>=sqrt(6)` | **Proved** | Under sub-six, the defect is a signing of this 4-regular graph; `tr B^2=4N`, triangle-freeness gives `tr B^3=0`, and S6B gives `lambda_max(B)>=2`. |
| S6D | Generically the reduced parity component contains a triangle iff its reduced step `t` satisfies `t=2`, `q=2t+1`, or `q=3t` | **Proved** | Direct classification of three increments from `{+-1,+-t}` summing to zero mod `q`. |
| S6E | For odd `N`, the triangle-free arithmetic criterion supplies many `sqrt(6)` lower bounds | **Proved** | Odd-order specialization of S6C/S6D. Retained as an elementary proof route even though ODD6 below is stronger. |
| KSQ6 | For every odd `k>=5` and `s>=3`, `m(ks,s)>=sqrt(6)` | **Proved** | Elementary triangle-free parity-defect proof. Superseded in range by ODD6, but useful because it avoids the external classification theorem. |
| S6G | A connected 4-regular edge-signed graph with smallest eigenvalue `>-2` has order at most 8, unless its underlying graph is `K_5` | **Proved from published classification + analytic degree audit** | Greaves--Koolen--Munemasa--Sano--Taniguchi, JCTB 110 (2015), Thms. 6 and 19. Exceptional classes have order 6--8. In the integral representation cases, 4-regularity reduces the tree/unicyclic/double-edge representation to `L(K_{1,5})=K_5`; the double-edge degree formula is audited with the parallel edge counted once, giving endpoint-degree sum 7. |
| S6H | On the forced order-7 component `C_7(1,2)cong overline(C_7)`, the minimum possible largest eigenvalue is `beta`, the largest root of `x^3-7x+7`; exactly one labelled switching class attains a value below 2 | **Proved, exact finite lemma** | Sub-2 forces all seven triangles negative. Tree gauge gives two classes with charpolys `(x+4)(x^3-2x^2-x+1)^2` and `x(x^3-7x+7)^2`; only the latter is sub-2. |
| S6N14 | `m(14,s)^2=4+beta` for `s=3,4,5`, whereas `m(14,2)^2>=6` | **Proved** | Any sub-six lift forces `DT=-TD`. Finite signed-shift diagonalization gives `chi_B=x^2(x^3-7x+7)^4` exactly for `(s,alpha)=(3,-1),(4,-1),(5,+1)`; all other holonomies have defect index at least 2. |
| S6R14 | For each `s in {3,4,5}`, the `N=14` minimizers are exactly two labelled switching classes, exchanged by one-step rotation | **Proved** | Anticommutation gives `D=epsilon diag((-1)^i)`, `epsilon=+-1`; S6N14 fixes the holonomy uniquely. Full `2^15` Hamilton-gauge enumeration independently confirms the count. |
| S6FULL | Complete strict sub-`sqrt(6)` classification | **Proved** | `m(N,s)^2<6` iff: `N=2s+2`; or `(5,2),(10,3)`; or `N=4s`; or `N=14, s in {3,4,5}`. Exact values are `4`, `5`, `4+2cos(pi/(2s))`, and `4+beta`. All other pairs have `m(N,s)^2>=6`. See `SUB_SQRT6_CLASSIFICATION.md`. |
| ODD6 | For every odd `N>=7` and every admissible `s`, `m(N,s)>=sqrt(6)` | **Proved** | Immediate from S6FULL: every strict sub-six family has even order except `(5,2)`. Hence for odd `k,s>=3`, `m(ks,s)>=sqrt(6)` for every odd `k>=3`, including the `k=3` resonance line. |
| E1 | If `N` is even, `m(N,s)^2<=6+2 cos(2pi/N)<8` | **Proved** | Finite anti-periodic signed shift and alternating chord signs; finite Fourier diagonalization only. |
| R1 | `m(9,3)<sqrt(8)` | **Proved** | Explicit signing; exact Sylvester minors `4,16,60,209,722,2508,5746,15993,47304`. |
| R2 | `m(15,5)<sqrt(8)` | **Proved** | Explicit signing; exact Sylvester certificate, final determinant `8636544`. |
| L9 | Nine-column signed-triangle local rule at excess `2/139` | **Proved, exact finite lemma** | Exact integer pruning survivor counts `8,56,152,440,488,1016,656,1064,128`; all final survivors obey the six middle alternations. |
| B7 | Every signing of `C_21(1,7)` has squared radius at least `8+18/131` | **Proved, exhaustive exact certificate** | `49,940` Q-necklaces and `199,760` Hamilton-gauge representatives; exact Rayleigh certificates. |
| B9 | Every signing of `C_27(1,9)` has squared radius at least `8+2/139` | **Proved, exhaustive exact certificate** | `17,024` final cyclic candidates after exact prefix pruning. |
| R3 | For odd `s>=7`, `m(3s,s)^2>=8+2/139` | **Proved, computer-assisted local lemma + analytic propagation** | `s=7,9` exact bases; for odd `s>=11`, nine-column alternation propagates to the seam and contradicts signed-triangle similarity via `tr B^3=+-6`. |
| R4 | `m(3s,s)<sqrt8 iff s` is even or `s in {3,5}` | **Proved** | Even `s` from E1; exceptions R1/R2; odd `s>=7` from R3. |
| P8 | A fixed period-8 phase determines the global finite minimum for all `C_{8L}(1,2)` | **Rejected historical overclaim** | Historical correction branch explicitly withdraws the global conclusion; fixed-phase dispersion is excluded from this paper. |
| Ksmall | Small exhaustive searches contain sub-`sqrt8` examples at `(k,s)=(5,3)` and other low parameters | **Observed** | Motivation only; not theorem evidence. |
| Kodd8 | Exact sub-`sqrt8` classification for odd `k>=5` | **Open** | ODD6 gives the full odd-order `sqrt6` floor, but no general all-signing `sqrt8` classification is known outside `k=3`. |
| Lit1 | Fixed-underlying-graph signature minimizing spectral radius is an established general problem | **Published/Established** | Belardo--Cioaba--Koolen--Wang, *Art Discrete Appl. Math.* 1 (2018), Problem 3.18. |
| Lit2 | Signed graphs with all eigenvalues in `[-2,2]` are classified | **Published/Established** | McKee--Smyth, *J. Algebra* 317 (2007), 260--290. |
| Lit3 | Connected signed graphs of maximum degree at most 4 with two adjacency eigenvalues are classified | **Published/Established** | Hou--Tang--Wang, *Discrete Math.* 342 (2019), 111615. |
| Lit4 | 4-regular toral tessellations with `A^2=4I` belong to established two-eigenvalue/weighing-matrix theory | **Published/Established** | McKee--Smyth; later toral-tessellation work including Stanić (2026). |
| Lit5 | Connected edge-signed graphs with smallest eigenvalue `>-2` have a complete structural classification | **Published/Established** | Greaves--Koolen--Munemasa--Sano--Taniguchi, *J. Combin. Theory Ser. B* 110 (2015), 90--111, Thms. 6 and 19. This is the only external classification theorem used in S6FULL. |

## Consolidated finite-global package

### I. Complete spectrum below `sqrt(6)`

Let `beta` be the largest root of `x^3-7x+7`. Then

```text
m(N,s)^2 < 6 iff one of:

(1) N=2s+2:                    m^2=4;
(2) (N,s)=(5,2),(10,3):        m^2=5;
(3) N=4s:                      m^2=4+2 cos(pi/(2s));
(4) N=14, s=3,4,5:             m^2=4+beta.
```

Every other pair has `m(N,s)^2>=6`.

In particular,

```text
N odd, N>=7  =>  m(N,s)>=sqrt(6), for every admissible s.
```

This is now the first main structural theorem of the paper.

### II. `sqrt(8)` threshold

```text
N even  =>  m(N,s)^2 <= 6+2 cos(2pi/N)<8.

m(3s,s)<sqrt8  iff  s is even or s in {3,5}.

odd s>=7  =>  m(3s,s)^2>=8+2/139.
```

Thus `k=3` is no longer presented as the only resonance with any global obstruction: all odd orders already have a universal `sqrt6` floor, while the triangle resonance `N=3s` produces the stronger jump through `sqrt8`.

## Hostile-audit corrections

1. Historical `1/70` on odd `N=3s` is strengthened to `2/139` after exact re-verification.
2. `(8,3)` has six labelled switching classes at the flat minimum; only switching isomorphism collapses them to one orbit.
3. Fixed period-8 dispersion is not a finite-global minimization theorem and is excluded.
4. The `sqrt(5)` equality problem and second gap are now completely closed.
5. `N=4s` is solved exactly for all `s>=2`.
6. The first draft of the Greaves-based double-edge degree audit incorrectly wrote endpoint-degree sum `6`; the corrected line-graph count is `d(a)+d(b)=7`, because the parallel edge is otherwise double-counted. The corrected proof still forces `K_5` and is recorded in `SUB_SQRT6_CLASSIFICATION.md`.
7. The previous KSQ6 theorem for odd `k>=5` remains valid by an elementary triangle-free proof, but ODD6 now supersedes it with all odd orders `N>=7`.