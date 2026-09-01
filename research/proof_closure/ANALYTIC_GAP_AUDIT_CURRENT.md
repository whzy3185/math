# Current Analytic Proof Gap Audit

## Executive verdict

The truth-value classification

```text
m_n < rho_-(n) iff n=32, n=40, or n is even and n>=48
```

is complete as an exact computer-assisted theorem. Its dependency chain is
closed by exact switching coverage, rational LDL certificates, exact local
interlacing/finite closure, and the certified IMS tail.

The pure analytic classification is not complete. The three most serious
analytic gaps are:

1. the residue-two cyclic boundary Schur closure; the bulk Riccati part is
   now analytic and uniform, but the final fixed six-by-six response matrix
   has not been shown positive for every length;
2. no corresponding all-length finite-interface theorem exists for residues
   four and six;
3. universal optimality at equality orders remains computer-assisted: the
   `8..30` proof is exhaustive, while the `34..46` proof still needs exact
   local-window tables and a de Bruijn closure.

The G6 scalarization problem is mathematically important but is not a P0
blocker for replacing the finite failure bridge: the current exact G6 edge is
already sufficient for the rigorous classification and for the IMS theorem.

## Module audit

| Module | Current theorem | Current rigorous proof | Analytic status | Exact missing implication | Best candidate route | Risk |
|---|---|---|---|---|---|---|
| Switching/gauge | spectrum is switching invariant; `Q,tau,alpha` coordinates exist | diagonal conjugacy and cycle-space algebra | ANALYTIC_CLOSED | none | retain | low |
| Twisted benchmark | exact formula for `rho_-(n)` | Fourier two-plane calculation | ANALYTIC_CLOSED | none | retain | low |
| Period-8 fiber | `sup rho^2=eta=4+sqrt(10+2sqrt(5))` | exact Floquet polynomial, positivity identity, endpoint root ordering | ANALYTIC_NEAR_CLOSED | derive the displayed fiber determinant directly rather than treating the coefficient map as a CAS audit input | hand multiplication / determinant expansion followed by existing positivity identity | low |
| Period-8 finite family | every `8|n`, `n>=32` fails | exact band theorem plus elementary benchmark comparison | ANALYTIC_CLOSED once the fiber identity is accepted | same fiber derivation provenance only | incorporate the direct determinant derivation above | low |
| G6 local root | a unique positive physical root lies in the stored interval | exact transfer, interval Evans signs/derivative, cofactor nondegeneracy | EXACT_COMPUTER_ASSISTED_ONLY | replace interval cofactor calculation by a scalar physical equation | scalar Weyl/Evans or block-Jacobi matching | medium/high |
| G6 global edge | `sup sigma(H6)=c6`; squared multiplicity two | resultant/Sturm candidate list plus two unsquared Grassmann charts and `K` symmetry | EXACT_COMPUTER_ASSISTED_ONLY | identify physical branch without chart-by-chart exclusion | scalar physical Evans/Weyl monotonicity | high |
| G6 localization | `|psi_j|<=Cq^|j|` | matching lemma and exact stable multiplier enclosures | ANALYTIC_NEAR_CLOSED relative to the exact G6 root | compress interval multiplier bookkeeping to an explicit discriminant inequality | palindromic bulk quartic with one displayed rational `q<1` | medium |
| Abnormal single gaps | G6 uniquely attains `c6` among abnormal positive single gaps | finite-support integer Rayleigh witnesses plus exact G6 edge | ANALYTIC_NEAR_CLOSED relative to G6 | independent analytic G6 edge | retain variational proof; do not use recurrence ordering | low/medium |
| Residue 2 bulk | all repeated bulk pivots of `198I-25A^2` are positive | exact block-Schur recurrence, two rational Loewner boxes, four-step entry, fixed-energy `q_slow<1/3` | ANALYTIC_CLOSED | none for the bulk propagation | retain `F_+`,`F_-` box proof | low |
| Residue 2 boundary | `198I-25A_(8k+2)^2>0` for all `k>=6` | exact finite rows and a fixed response reduction | ANALYTIC_NEAR_CLOSED | uniform positivity of the final 6x6 cyclic boundary Schur matrix | response LMI, limiting response plus geometric error, or Woodbury cone | high |
| Residues 4 and 6 | structured signings beat twisted at all orders | exact finite LDL bridge plus IMS from 166/240 onward | ANALYTIC_OPEN | all-length finite-interface theorem with two/three interfaces | block Riccati/Woodbury theorem parameterized by interface count | high |
| Auxiliary periods | periods 10,12,14,18,22 give exact counterexample subfamilies | exact Floquet positivity certificates | ANALYTIC_CLOSED but AUXILIARY | no mainline implication | retain only as bridge reduction | low |
| Failure bridge | 96 rows, now 25 not covered by periodic/IMS analytic families | exact rational LDL | EXACT_COMPUTER_ASSISTED_ONLY for the remaining 25 rows | residue theorems for `2,4,6` | P0-1 then P0-2 | high |
| Equality `8..30` | no signing beats twisted | exhaustive switching/orbit certificates | EXACT_COMPUTER_ASSISTED_ONLY | universal lower bound without exhaustive coverage | minimizer rigidity or growing-degree polynomial/trace certificate | very high |
| Equality `34,36` | no signing beats twisted | local Rayleigh exclusions plus exact closed-walk closure | ANALYTIC_NEAR_CLOSED | prove local language is exactly reference loop plus `1000` cycle without the 13/14-bit table | local forbidden-pattern/SOS certificate | high |
| Equality `38,42,44,46` | no signing beats twisted | same local table plus 18/28-state recurrent core and terminal certificates | EXACT_COMPUTER_ASSISTED_ONLY | rigidity of all surviving recurrent cores | SCC/primitive-cycle and parity-holonomy spectral obstruction | very high |
| Complete classification | stated truth set | disjoint union of all closed exact modules | ANALYTIC_WITH_FINITE_BASE_CASES | replacement of the remaining failure/equality finite modules | assemble P0 results | high |

## Arrow-level dependency graph

```text
switching + Fourier
    -> twisted benchmark                         [ANALYTIC_CLOSED]

period-8 determinant + positivity identity
    -> eta and 8-divisible failures              [ANALYTIC_NEAR_CLOSED]

transfer + physical Evans + Grassmann/Sturm
    -> G6 edge and localization                  [EXACT_COMPUTER_ASSISTED_ONLY]
G6 edge + charge constructions + IMS
    -> large-order failures                      [EXACT_COMPUTER_ASSISTED_ONLY]

R2 block templates + Loewner boxes
    -> all R2 bulk pivots                        [ANALYTIC_CLOSED]
R2 bulk pivots + boundary response closure
    -> residue-two all-length failure theorem    [ANALYTIC_NEAR_CLOSED]
R2/R4/R6 finite-interface theorems
    -> no finite failure bridge                  [ANALYTIC_OPEN]

switching coverage + local obstruction theorem
    -> finite language/rigidity                  [ANALYTIC_OPEN]
finite language/rigidity + terminal lower bound
    -> equality orders                           [EXACT_COMPUTER_ASSISTED_ONLY]

failure side + equality side
    -> complete classification                   [ANALYTIC_WITH_FINITE_BASE_CASES]
```

## Analytic routes already ruled out or bounded

1. Fixed fourth moment gives only

   ```text
   tr(A^4)=20n+16d(Q),
   ```

   which is far below the required spectral edge. More generally a fixed
   moment ratio cannot certify equality at the twisted signing itself: unless
   all lower squared eigenvalues vanish, the ratio is strictly below the top
   squared eigenvalue.
2. Enlarging the existing local Gram window does not improve the surviving
   language in the tested equality orders; it is not a path to an immediate
   forbidden-pattern theorem.
3. The order-nine exterior-power recurrence has alternating shifted
   coefficients; its naive positive cone is not invariant.
4. The degree-ten G6 polynomial cannot select a physical root, because it
   contains the gap-two root and nonphysical resultant branches.
5. The `K` reduction halves the one-G6 dimension but leaves a complex
   four-band block with four cross-end links. It does not simplify the
   propagation relative to the real block-Schur recurrence, so it is not a
   second main route.
6. Periodic Floquet families are now frozen as auxiliary bridge results.
   Searching further periods is prohibited unless it directly proves a
   residue theorem.

## Minimal analytic closure task set

### P0-1: residue-two boundary response closure

**Statement.** For every `k>=6`, the response recurrence induced by the
standard one-G6 `M_k=198I-25A_(8k+2)^2` has final boundary matrix

```text
S_k=[G_k C_k; C_k^T H_k] > 0.
```

Together with the established bulk invariant boxes this proves
`rho(A_(8k+2))^2<198/25<rho_-(8k+2)^2` for every `k>=6`.

**Best route.** Prove a two-step common quadratic metric or a limiting
response theorem on the existing Loewner boxes; use the exact `q_slow<1/3`
bulk bound to control the cross-boundary response. The response system and
the boundary matrix are fixed dimensional.

**Kill criterion.** Stop this particular contraction/LMI route if an exact
evaluation of the two-step response differential on the invariant boxes has
spectral radius at least one, or if the certified limiting boundary response
is not positive. In either case move to a finite Evans/Woodbury determinant
proof rather than widening the box or adding orders.

### P0-2: common finite-interface theorem for residues four and six

**Statement.** For the prescribed two- and three-G6 gap words, construct
fixed block templates and prove, for every admissible `k`,

```text
2679/338 I-A_(8k+4)^2 > 0,
5782/729 I-A_(8k+6)^2 > 0.
```

The theorem must explicitly account for interface number, both cyclic arcs,
charge closure, and the final boundary core; it may share a parameterized
proof with P0-1 but cannot assume that it does.

**Best route.** Generalize the block-Schur/Riccati plus finite response core
to `r=1,2,3`, retaining all interface channels in the response state.

**Kill criterion.** Stop the shared theorem route if the two/three-interface
template introduces a non-decaying boundary mode or if the fixed cap fails
for any admissible symbolic core. Then split the theorem by residue; do not
restore row-by-row LDL as the claimed analytic result.

### P0-3: analytic local obstruction for equality at 34 and 36

**Statement.** Prove directly that every legal cyclic `Q` word satisfying
`rho(A)^2<rho_-(n)^2` has every local word in the two-factor language

```text
0-infinity or (1000)-infinity.
```

The latter is excluded by length at 34 and by cyclic `Q` parity at 36.

**Best route.** Find a small symbolic collection of local quadratic-form or
sum-of-squares identities whose forbidden factors replace the 13/14-bit
Rayleigh table.

**Kill criterion.** Stop this local-rigidity route if a legal local word
outside the two-factor language survives every candidate symbolic obstruction
while extending to an admissible cyclic word. Then retain the finite-language
certificate and move effort to P0-4.

### P0-4: recurrent-core rigidity for equality at 38,42,44,46

**Statement.** Every even-parity cyclic word in the surviving 18/28-state
core either reduces to the reference/twisted equality class or has a
uniform exact spectral obstruction above `rho_-(n)^2`.

**Best route.** Work on the SCCs symbolically: decompose all closed walks into
primitive cycles, then use length modulo, parity, holonomy, and a bounded
spectral obstruction for each primitive type.

**Kill criterion.** Stop the SCC-rigidity route if the core contains an
unbounded primitive family with legal lengths and holonomies that avoids all
available local spectral obstructions. That would show a new global
transfer/variational lower theorem is required.

## P1 and P2

**P1.** Give a hand-derived period-eight fiber determinant and retain the
existing positivity identity. This removes a presentation/provenance gap but
does not reduce the finite proof burden.

**P1.** Compress G6 localization to a direct discriminant-to-multiplier
estimate, while retaining the exact physical Evans certification.

**P2.** Seek a scalar physical G6 equation. It is valuable for exposition and
formalization but is not required before P0-1 through P0-4.

**P2.** Investigate equality `8..30` only after the recovered equality orders
have either acquired rigidity theorems or have been shown resistant to them.
The current evidence supplies no credible one-step universal theorem there.

## Claims that must remain qualified

1. Do not call the global G6 edge a pure analytic theorem; its accepted proof
   is exact computer-assisted physical-branch exclusion.
2. Do not call the residue-two cap theorem closed. Only the bulk part is
   analytic; the cyclic boundary closure is open.
3. Do not treat periods 10,12,14,18,22 as a residue-class proof. They are
   auxiliary divisibility families.
4. Do not call the `34,36` result analytic until the local language itself is
   derived without the Rayleigh table.
5. Do not use unrestricted nonzero-residue limits, multi-gap interactions,
   splitting simplicity, or universal finite-core lower bounds as main-theorem
   dependencies.

## Non-mainline open questions

| Question | Status | Why it does not block classification |
|---|---|---|
| unrestricted common nonzero-residue limit | OPEN | the classification asks only for an explicit counterexample, not the asymptotic minimum |
| multi-gap interaction coefficients | OPEN | no coefficient enters the finite witness or IMS argument |
| finite-ring simplicity and splitting | OPEN | multiplicity is not needed for strict witness inequalities |
| universal multi-gap/core lower theorem | OPEN | relevant to minimizer structure and equality generalization, not to the existing truth-value proof |
| complete Lean formalization | OPEN | formal project is operational, but full human statements remain unsettled |
