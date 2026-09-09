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
| F6 | `m(N,s)=sqrt(5) iff (N,s) in {(5,2),(10,3)}` | **Proved** | `lambda_max(B)=1` forces negative-clique defect components; the parity support reduces the parameters to `N=5,10`; `(10,2)` is excluded by triangle-flux signs and `(5,2),(10,3)` are attained by a conference core. |
| F7 | Outside the flat line and the two `sqrt(5)` pairs, `m(N,s)^2>=4+sqrt(2)` | **Proved** | Integral zero-diagonal defect below `sqrt(2)` has only negative-clique support components. |
| F8 | `m(N,s)^2=4+sqrt(2) iff (N,s)=(8,2)` | **Proved** | Induced signed `P_3` rigidity plus the fixed parity support; exact `C_8(1,2)` certificate has characteristic polynomial `(x^4-8x^2+14)^2`. |
| PDEF | `supp((A^2-4I) mod 2)` is empty for `N=2s+2`, `Cay(Z_N,{+-2})` for `N=4s`, and `Cay(Z_N,{+-2,+-2s})` otherwise | **Proved** | Frobenius squaring in `F_2[Z_N]`: `(x+x^-1+x^s+x^-s)^2=x^2+x^-2+x^(2s)+x^(-2s)`. |
| K4 | For every `s>=2`, `m(4s,s)^2=4+2 cos(pi/(2s))`; exactly two labelled minimizing switching classes, exchanged by one-step rotation | **Proved** | Below defect index 2, PDEF forces two signed `2s`-cycles. The optimum is attained by two unbalanced cycles and by a finite anti-periodic signed-shift construction. Rigidity comes from the mixed `s+1` and `2s` channels. |
| S6A | If `rho(A_sigma)^2<6`, then `supp(A_sigma^2-4I)=supp((A_sigma^2-4I) mod 2)` | **Proved** | `M=lambda_max(B)<2`; every `2x2` principal block gives `|b_ij|<2`, so integrality leaves only `0,+-1`; parity therefore fixes the support exactly. |
| S6B | If a nonzero symmetric `X` has `tr X=tr X^3=0`, then `lambda_max(X)^2>=tr(X^2)/n` | **Proved** | Sum `(M-mu)(mu+M)^2/M>=0` over the eigenvalues. Equality iff `X^2=M^2I`. |
| S6C | Away from `N=2s+2,4s`, if `Cay(Z_N,{+-2,+-2s})` is triangle-free, then `m(N,s)>=sqrt(6)` | **Proved** | A hypothetical sub-six signing has defect a signing of this 4-regular support, so `tr B^2=4N` and triangle-freeness gives `tr B^3=0`; S6B forces `lambda_max(B)>=2`. |
| S6D | Let `d=gcd(N,2)`, `q=N/d`, and let `t` be the reduced step in a parity component. Generically the forced parity graph contains a triangle iff `t=2`, `q=2t+1`, or `q=3t` | **Proved** | Classify three increments from `{+-1,+-t}` summing to zero modulo `q`, using `2<=t<q/2`. |
| S6E | For odd `N`, `s!=2`, `N!=2s+1`, `N!=3s` implies `m(N,s)>=sqrt(6)` | **Proved** | Odd-order specialization of S6C/S6D. |
| KSQ6 | For every odd `k>=5` and every `s>=3`, `m(ks,s)>=sqrt(6)` | **Proved** | The reduced parity support is triangle-free in both parities of `s`; this is the first uniform theorem covering all odd chord-cycle lengths `k>=5`. |
| E1 | If `N` is even, `m(N,s)^2<=6+2 cos(2pi/N)<8` | **Proved** | Finite anti-periodic signed shift and alternating chord signs; finite Fourier diagonalization only. |
| R1 | `m(9,3)<sqrt(8)` | **Proved** | Explicit signing; exact Sylvester minors `4,16,60,209,722,2508,5746,15993,47304`. |
| R2 | `m(15,5)<sqrt(8)` | **Proved** | Explicit signing; exact Sylvester certificate, final determinant `8636544`. |
| L9 | Nine-column signed-triangle local rule at excess `2/139` | **Proved, exact finite lemma** | Exact integer pruning survivor counts `8,56,152,440,488,1016,656,1064,128`; all final survivors obey the six middle alternations. |
| B7 | Every signing of `C_21(1,7)` has squared radius at least `8+18/131` | **Proved, exhaustive exact certificate** | `49,940` Q-necklaces and `199,760` Hamilton-gauge representatives; exact Rayleigh certificates. |
| B9 | Every signing of `C_27(1,9)` has squared radius at least `8+2/139` | **Proved, exhaustive exact certificate** | `17,024` final cyclic candidates after exact prefix pruning. |
| R3 | For odd `s>=7`, `m(3s,s)^2>=8+2/139` | **Proved, computer-assisted local lemma + analytic propagation** | `s=7,9` are exact bases; for odd `s>=11`, nine-column alternation propagates to the seam and contradicts `SBS^T=-B` via `tr B^3=+-6`. |
| R4 | `m(3s,s)<sqrt8 iff s` is even or `s in {3,5}` | **Proved** | Even `s` from E1; exceptions R1/R2; odd `s>=7` from R3. |
| P8 | A fixed period-8 phase determines the global finite minimum for all `C_{8L}(1,2)` | **Rejected historical overclaim** | Historical correction branch explicitly withdraws the global conclusion; fixed-phase dispersion is excluded from this paper. |
| Ksmall | Small exhaustive searches contain sub-`sqrt8` examples at `(k,s)=(5,3)` and other low parameters | **Observed** | Motivation only; not used as theorem evidence. |
| Kodd8 | Exact sub-`sqrt8` classification for odd `k>=5` | **Open** | KSQ6 supplies a universal `sqrt6` floor, but no general all-signing sub-`sqrt8` upper construction or obstruction is yet proved for odd order. |
| Lit1 | Fixed-underlying-graph signature minimizing spectral radius is an established general problem | **Published/Established** | Belardo--Cioaba--Koolen--Wang, *Art Discrete Appl. Math.* 1 (2018), Problem 3.18. |
| Lit2 | Signed graphs with all eigenvalues in `[-2,2]` are classified | **Published/Established** | McKee--Smyth, *J. Algebra* 317 (2007), 260--290. |
| Lit3 | Connected signed graphs of maximum degree at most 4 with two adjacency eigenvalues are classified | **Published/Established** | Hou--Tang--Wang, *Discrete Math.* 342 (2019), 111615. |
| Lit4 | 4-regular toral tessellations with `A^2=4I` belong to established two-eigenvalue/weighing-matrix theory | **Published/Established** | McKee--Smyth; later toral-tessellation work including Stanić (2026). |

## Consolidated finite-global package

### Low-end hierarchy

```text
m(N,s) = 2                        iff N=2s+2;
m(N,s) = sqrt(5)                  iff (N,s)=(5,2) or (10,3);
m(N,s) = sqrt(4+sqrt(2))          iff (N,s)=(8,2);
m(N,s) > sqrt(4+sqrt(2))          otherwise.
```

### Exact resonance and arithmetic obstruction

```text
m(4s,s)^2 = 4+2 cos(pi/(2s)),  s>=2.

odd k>=5, s>=3  =>  m(ks,s)>=sqrt(6).
```

For odd `N`, the parity-defect theorem gives the broader criterion

```text
s!=2, N!=2s+1, N!=3s  =>  m(N,s)>=sqrt(6).
```

Thus the parity defect identifies the arithmetic triangle families where sub-`sqrt6` behavior can survive.

### `sqrt(8)` threshold

```text
N even  =>  m(N,s)^2 <= 6+2 cos(2pi/N)<8.

m(3s,s)<sqrt8  iff  s is even or s in {3,5}.

odd s>=7  =>  m(3s,s)^2>=8+2/139.
```

## Hostile-audit corrections

1. The historical odd `N=3s` constant `1/70` has been strengthened to `2/139` after exact re-verification.
2. `(8,3)` has six labelled switching classes at the flat minimum, not one; only switching isomorphism collapses them to one orbit.
3. Fixed period-8 dispersion is not a finite-global minimization theorem and is excluded.
4. The old question whether `sqrt(5)` is sharp is closed exactly by F6.
5. The universal second gap is exact and uniquely attained at `(8,2)`.
6. `N=4s` is now solved exactly for all `s>=2`.
7. The general `N=ks` program now has a genuine odd-ratio theorem: all odd `k>=5`, `s>=3` obey the global lower bound `sqrt(6)`. The remaining open issue there is the larger `sqrt8` threshold, not the existence of any nontrivial global obstruction.
