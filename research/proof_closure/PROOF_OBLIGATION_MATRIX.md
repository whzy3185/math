# Proof Obligation Matrix

Status vocabulary is restricted to `CLOSED_ANALYTIC`, `CLOSED_EXACT_COMPUTER_ASSISTED`, `UNDER_EXPLAINED`, `OPEN`, `CLAIM_TOO_STRONG`, and `OBSOLETE`. A row may support the Main Classification only in one of the two `CLOSED_*` states.

| ID | Claim | Quantifier | Current proof and dependency | Computer dependency | Status |
|---|---|---|---|---|---|
| SW-1 | switching preserves signed spectrum | all signings | diagonal `+-1` conjugacy | none | CLOSED_ANALYTIC |
| SW-2 | Hamilton gauge / `Q,tau,alpha` normalization is achievable | all signings | cycle-basis recursion and gauge lemma | finite encoders cross-check it | CLOSED_ANALYTIC |
| SW-3 | quotient coverage used below is surjective | stated finite orders | canonical orbit/replay proofs | exact checkers | CLOSED_EXACT_COMPUTER_ASSISTED |
| TW-1 | twisted class is defined | even `n>=8` | Suvagiya Proposition 2 and rederivation below | none | CLOSED_ANALYTIC |
| TW-2 | `rho_-(n)^2=4+2cos(2pi/n)+2cos(4pi/n)` | even `n>=8` | Fourier two-by-two blocks | none | CLOSED_ANALYTIC |
| P8-1 | period-eight fiber polynomial | target phase | direct Floquet calculation | independent symbolic audit | CLOSED_EXACT_COMPUTER_ASSISTED |
| P8-2 | bulk edge `eta=4+sqrt(10+2sqrt5)` | all Bloch parameters | exact positivity/Sturm argument | independent checker | CLOSED_EXACT_COMPUTER_ASSISTED |
| CH-1 | phase/translation charge is `g-4 mod 4` | concatenated gap words | endpoint-residue proof | certificate only cross-checks | CLOSED_ANALYTIC |
| CH-2 | residue constructions close cyclically | `n mod 8=2,4,6` | explicit gap-word sum and charge proof | exact arithmetic cross-check | CLOSED_EXACT_COMPUTER_ASSISTED |
| G6-1 | G6 transfer operator is exactly specified | bilateral G6 | integral four-by-four transfer product | transfer checker | CLOSED_EXACT_COMPUTER_ASSISTED |
| G6-2 | degree-ten algebraic equation and isolated root `c6` | stated rational interval | elimination plus Sturm count | independent exact checker | CLOSED_EXACT_COMPUTER_ASSISTED |
| G6-3 | physical root exists and is simple | G6 positive branch | interval Evans signs and derivative | independent cofactor chart | CLOSED_EXACT_COMPUTER_ASSISTED |
| G6-4 | `c6` is globally the G6 squared spectral edge | both orientations | Grassmann atlas, resultant candidate list, unsquared exclusion | two exact charts | CLOSED_EXACT_COMPUTER_ASSISTED |
| G6-5 | multiplicity of `c6` for `A^2` is two | G6 | anticommuting symmetry maps `+/-sqrt(c6)` | rank correction checker | CLOSED_EXACT_COMPUTER_ASSISTED |
| G6-6 | associated state is exponentially localized | G6 | stable/unstable matching and `q<=9/25` | exact multiplier enclosure | CLOSED_EXACT_COMPUTER_ASSISTED |
| SG-1 | G6 uniquely minimizes among abnormal positive single gaps | `g>=1`, `g!=4` | six finite exact witnesses, one uniform witness, and G6 edge | certified endpoint for `c6` | CLOSED_EXACT_COMPUTER_ASSISTED |
| SG-2 | uniform gap `1/250` away from G6 for other abnormal gaps | `g not in {4,6}` | rational witness comparison | independent verifier | CLOSED_EXACT_COMPUTER_ASSISTED |
| IMS-1 | discrete IMS identity and range-four error bound | every signed cycle-square operator | direct commutator expansion | none | CLOSED_ANALYTIC |
| IMS-2 | globally admissible cutoff/placement construction | every even `n>=240` | exact tent geometry and patch separation | threshold checker | CLOSED_EXACT_COMPUTER_ASSISTED |
| TAIL-1 | explicit witness for every `48<=n<240` | finite interval | 96 structured signings and full `tI-A^2` LDL certificates | independent natural-order reconstruction | CLOSED_EXACT_COMPUTER_ASSISTED |
| TAIL-2 | explicit witness for every even `n>=240` | infinite tail | G6 edge + IMS + residue constructions | threshold checker | CLOSED_EXACT_COMPUTER_ASSISTED |
| FAIL-1 | exact witness semantics | any witness row | positive definiteness of `tI-A^2`, `t<rho_-^2` | rational LDL / algebraic comparison | CLOSED_ANALYTIC |
| LOW-1 | no counterexample through order 30 | `8,10,...,30` | complete switching-class/orbit coverage and exact terminal lower certificates | replay and minimality checker | CLOSED_EXACT_COMPUTER_ASSISTED |
| LOW-2 | explicit order-32 counterexample | `n=32` | two independent exact positive-definiteness decompositions | independent checker | CLOSED_EXACT_COMPUTER_ASSISTED |
| REC-1 | local-window pruning is sound | 34,36,38,42,44,46 | strict exact local Rayleigh test excludes every completion containing a rejected window | independent reconstruction | CLOSED_EXACT_COMPUTER_ASSISTED |
| REC-2 | parity-lifted de Bruijn closure is complete | same six orders | exact overlap, wrap-around, parity and dihedral construction | independent checker | CLOSED_EXACT_COMPUTER_ASSISTED |
| REC-3 | accepted terminals satisfy lower bound | same six orders | threshold eigenvalue or full-ring exact Rayleigh certificate in both holonomies | independent checker | CLOSED_EXACT_COMPUTER_ASSISTED |
| N40 | explicit order-40 counterexample | `n=40` | fraction-free/rational LDL of `15541I-200A^2` | independent reconstruction | CLOSED_EXACT_COMPUTER_ASSISTED |
| ORD-1 | every admissible order is covered exactly once | all even `n>=8` | order ledger below | automated closure checker | CLOSED_EXACT_COMPUTER_ASSISTED |
| CLASS | complete truth-value classification | all even `n>=8` | `LOW-1 + LOW-2 + REC-1..3 + N40 + TAIL-1..2` | full verifier chain | CLOSED_EXACT_COMPUTER_ASSISTED |

## Explicitly excluded research claims

| Claim | Reason it does not support `CLASS` | Status |
|---|---|---|
| every finite-core `B0 -> B2` interface has edge at least `c6` | only bounded/motif subclasses are proved | OPEN |
| all physical single-gap levels have a transfer-ordering proof | variational theorem suffices; proposed recurrence ordering is unnecessary | UNDER_EXPLAINED |
| unrestricted nonzero-residue common liminf/limit | tight, dichotomy, vanishing, and aperiodic blockers remain | OPEN |
| universal interaction coefficients / finite-ring simplicity | exact `2r` norm bound is not an entrywise asymptotic theorem | OPEN |
| old exact-`r` cluster and `r x r` Feshbach statement | G6 has rank two after squaring | OBSOLETE |

## Main-classification audit decision

Every incoming dependency of `CLASS` is currently `CLOSED_ANALYTIC` or `CLOSED_EXACT_COMPUTER_ASSISTED`. The open rows are mathematically valuable, but belong to stronger asymptotic/interface programs and do not enter the truth-value theorem.
