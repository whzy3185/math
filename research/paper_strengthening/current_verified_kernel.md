# Current verified kernel

**Frozen source branch:** `analytic-proof-first`  
**Strengthening branch:** `period8-paper-strengthening`  
**Rule:** later exploration may cite this file but must not silently enlarge
or rewrite the status of any frozen claim.

## Status vocabulary

| Label | Meaning |
|---|---|
| `ANALYTIC` | A human-readable mathematical proof is closed in the repository. |
| `FINITE_EXACT` | A finite symbolic/integer calculation is part of the proof and is explicitly disclosed. |
| `LEAN_CHECKED` | The stated alpha = +1 theorem kernel is checked by the frozen Lean project. |
| `COMPUTATIONAL_BACKGROUND_ONLY` | Useful for discovery or regression, but not a theorem dependency of the strengthening paper. |
| `EXCLUDED` | Outside the strengthening project unless the user explicitly reopens it. |

## Frozen mathematical results

| ID | Result | Status | Exact scope and boundary |
|---|---|---|---|
| K1 | Hamilton-gauge realization | `ANALYTIC`, `LEAN_CHECKED` for the alpha = +1 witness | Switching is spectral conjugacy. Local step-one couplings are normalized on the cut-open lift; finite holonomy is carried by the seam/quasi-periodic boundary. |
| K2 | Period-eight Floquet fiber | `ANALYTIC`, `LEAN_CHECKED` | For `tau=(1,1,-1,1,-1,-1,1,-1)`, the eight-site cell gives the displayed Hermitian fiber on the unit circle. |
| K3 | Chiral involution | `ANALYTIC`, `LEAN_CHECKED` | With `xi^2=z`, the signed half-period translation satisfies `J_z^2=I` and anticommutes with the fiber. The final characteristic data depend on z, not on the choice of xi. |
| K4 | `8 by 8 -> 4 by 4 -> 2 by 2` reduction | `ANALYTIC`, `LEAN_CHECKED` | The fiber is off-diagonal in chiral coordinates; the squared problem reduces to `BC`, then to a direct two-by-two determinant identity. |
| K5 | Squared-fiber polynomial | `ANALYTIC`, `LEAN_CHECKED` | `P(y,c)=y^4-16y^3+(80-2c)y^2+(-128+16c)y+c^2-13c+38`, with `c=z+z^(-1)`. |
| K6 | Exact infinite-volume squared edge | `ANALYTIC` | `sup_(|z|=1) rho(H(z))^2=eta=4+sqrt(10+2sqrt(5))<8`, with equality only at `z=1`. This exact edge is not part of the frozen Lean theorem statement. |
| K7 | Infinite finite-counterexample family | `ANALYTIC`, `LEAN_CHECKED` in rational-separator Hermitian eigenvalue form | For every `n=8L`, `L>=4`, the explicit alpha = +1 witness strictly beats the twisted signing. The frozen Lean theorem proves every Hermitian eigenvalue squared is below the twisted squared benchmark. |
| K8 | Period-eight sub-eight trichotomy | `ANALYTIC` plus `FINITE_EXACT` | Among legal period-eight local-flux words, modulo cyclic translation, reflection, and lift ambiguity, the antipodal two-defect phase is the unique class below squared edge 8; the balanced phase is at 8; all others are above 8. |
| K9 | Three non-antipodal two-defect cases | `FINITE_EXACT` | The exact recurrence gives first positive excesses `E_4=5504`, `E_6=64336`, and `E_9=2872096`. It is not an exhaustive signing search or floating-point spectral calculation. |
| K10 | General-period moment obstruction | `ANALYTIC` plus finite symbolic closed-walk expansion | `M1=4p`, `M2=20p+16d`, `M3=118p+168d+96a+48b`; edge at most 8 implies `d<=3p/4` and `40d+96a+48b<=42p`. These are necessary conditions, not a classification. |

## Frozen formal-verification scope

The public Lean endpoint is
`TargetA.period8_alpha_plus_main_theorem`. Its scope is the explicit
alpha = +1 witness. The formal chain includes finite Hamilton cells, ZMod
DFT, nonzero fiber extraction, the polynomial certificate at `1561/200`, the
Hermitian eigenbasis, and strict comparison with the twisted squared
benchmark.

The frozen Lean kernel does **not** claim:

- exact finite equality `rho(A_(8L,+))^2=eta`;
- alpha = -1 finite-sector formalization;
- the period-eight trichotomy;
- the general moment obstruction;
- R2/R4/R6/G6 or any all-even classification.

## Computational background only

The following may guide conjecture formation and regression checks but are not
dependencies of K1--K10:

- exhaustive switching-class enumerations at small orders;
- dense numerical eigensystems;
- stored LDL/Bareiss certificates for other paper scopes;
- bounded-period orbit tables beyond the finite exact recurrence K9;
- historical production/checker logs.

## Excluded projects

The strengthening phase does not reopen:

- R2, R4, R6, or G6 classification/tail programmes;
- the former exact-r/Feshbach corpus;
- all-even truth classification;
- global determination of `m_n` or all minimizers;
- large brute-force searches for new periods.

## Open strengthening questions

These are not frozen results:

1. independent proof of exact finite alpha = +1 radius `eta`;
2. the exact alpha = -1 finite edge;
3. a minimal-period-below-eight theorem;
4. a quantitative period-eight isolation gap;
5. M4 and any resulting general rigidity;
6. a general chiral-periodic-word criterion;
7. genuinely new primitive low-edge families.
