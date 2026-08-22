# Target A Task 51 Synthesis

## 1. Baseline

HEAD: `82895863a59f8014d547544a7b3bb18aaa0cc8e5` at entry  
branch: `agent/target-a-discovery-snapshot`  
tests: entry `345 passed, 3 skipped, 20 subtests` plus one stale freeze-guard failure; guard repaired  
manuscript freeze: English tree `59e3a8f...`, Chinese tree `57ae03f...`, unchanged

## 2. Largest New Discoveries

1. `c6` is the unique interval root of an exact irreducible degree-ten Evans polynomial. Evidence: PROVED. Old PSLQ-only status changed. Theorem value: very high.
2. The order-nine closure recurrence factors exactly as `1+4+4`, with Bezout projectors and reciprocal `4->2` reductions. Evidence: PROVED. Theorem value: high.
3. Exact charge conservation is `sum q_i=n-4d`, hence total charge is `n mod 8` for even rings. Evidence: PROVED. Theorem value: very high.
4. Gap2/`q=-2` has a localized level `8.0809858021>8`; it does not beat G6. Evidence: deterministic two-width interface calculation. Theorem value: high after interval certification.
5. Three separated G6 levels beat G10 by about `0.07173` at `n=262` and converge toward c6 at `n=510`. Evidence: deterministic structured rings. Old G10-core story changed. Theorem value: very high.
6. All nonzero even residues are strongly supported to share limit c6 via one/two/three G6 slips. Evidence: structured FP64 plus proved c6. Theorem value: very high.
7. The p<=24 dangerous frontier contains 13 primitive numerical sub-eight phases, including mixed motifs. Evidence: exact eta classification plus deterministic Bloch refinement. Theorem value: high.
8. Exact M4/M5/M6 local motif expansions have 10/27/76 translation classes; M4 explicitly detects spacing four. Evidence: PROVED. Theorem value: high.
9. Current local Rayleigh windows are insufficient: 108 strongest windows and 30 primitive cycles through period 16 survive. Evidence: EXACT_FINITE. This redirects crystallization work.
10. Charged interfaces are not finite-rank perturbations of one global bulk gauge; neutralized cores have exact ranks/inertias. Evidence: PROVED for compact cores. Theorem value: medium-high.

## 3. Falsified Assumptions

- G10 is the fundamental residue-six excitation: rejected by three G6.
- Pure positive-cosh closure representation: rejected by unequal reciprocal weights.
- Closure-Hankel positivity: rejected in all 24 diagnostics.
- Naive positive generating-function weights: rejected by modal signs.
- A lone charged interface is finite rank relative to one global bulk: rejected.
- The sub-eight atlas is only the simple `[4,g]` branch: rejected by mixed motifs.
- The current local-Rayleigh survivor graph has only the target cycle: rejected.
- A topological bulk-index jump protects G6/G10: no signal found.

## 4. Finite-Ring Route Bake-Off

Order-nine factorization: STRONG  
Chebyshev: WEAK  
Dominant mode: PROMISING  
Polyhedral cone: WEAK  
Generating function: FALSIFIED_POSITIVITY  
Closure Hankel: FALSIFIED  
Symplectic trace: STRONG_REDUCTION  
Finite Evans/Rouche: EXACT_FINITE through k=32 / uniform OPEN  
Riccati: WEAK  
Birman-Schwinger: naive charged form FALSIFIED; piecewise form PROMISING  
Inertia: STRONG for neutral cores  
Green comparison: one finite check PASS; finite/infinite comparison OPEN  
Matrix SOS: WEAK  
Best route: dominant algebraic mode plus exact finite prefix  
Second-best route: piecewise finite Evans/Green counting

## 5. Charge Conservation

Exact law: `sum_i(g_i-4)=n-4d`, and even-ring legality forces even `d`.  
Residue table: `0,2,4,6 mod 8` have minimal nonnegative decompositions `[]`, `[+2]`, `[+2,+2]`, `[+2,+2,+2]`; nearest negative totals are `-8,-6,-4,-2`.  
Consequences: the residue-six negative alternative is exactly the mandatory gap2 test; spectral optimality remains separate from bookkeeping.

## 6. Single-Charge Spectrum

q=-2: localized, squared level `8.080985802104290`, above 8  
q=+2: G6, exact interval theorem, `c6=7.905369311620327...`  
all sub-eight charges: numerical `q=-1,+2,+4,+6,+8`; odd `q=-1` cannot occur alone on an even ring  
cheapest positive charge: `+2`  
cheapest negative charge: numerical `-1`, while the even alternative `-2` is above 8  
elementary excitation conclusion: `UNIQUE_CHEAPEST_POSITIVE_EVEN_CHARGE_SUPPORTED`

## 7. Multi-Slip Theory

two-slip: two-level G6 cluster; late splitting below double resolution  
three-slip: three-level G6 cluster approaching c6  
four-slip: four-level cluster reconstructed by projected effective matrix  
three-G6 vs G10: three G6 decisively lower in tested rings  
pairwise interaction: BELOW_DOUBLE_RESOLUTION  
many-body correction: UNRESOLVED  
mod16 explanation: two-path/holonomy/orientation PROMISING, not derived

## 8. Sub-Eight Periodic Atlas

number primitive R<8: 13 in the bounded numerical refinement  
important motifs: `[4,6]`, `[4,8]`, `[4,10]`, `[4,4,4,6]`, `[4,6,4,8]`, and odd-gap mixed cells  
new exact families: none beyond previously proved period 8/10; new values remain numerical  
period10 role: lowest non-target bounded phase and simplest positive-density crystal  
period12/14 role: first simple `[4,g]` branch members, promising exact-family targets

## 9. Commensurate Phase Diagram

status: STRONG_BOUNDED_SIGNAL  
main density trend: period eight is density-zero ground phase; period ten starts the observed nonzero envelope, but mixed motifs create additional branches  
defect-crystal hypothesis: SUPPORTED_WITH_MULTIPLE_COMMENSURATE_BRANCHES

## 10. Arbitrary-Period Crystallization

M4: PROVED, ten local classes  
higher moments: M5/M6 PROVED as data; no positivity decomposition  
Hankel-local: WEAK  
window Rayleigh: PROMISING_BUT_INSUFFICIENT  
de Bruijn: 30 cycles through primitive period 16  
cycle polytope: PROMISING_NOT_BUILT  
SDP: WEAK_STOPPED  
multicone: PROMISING_OPEN  
subadditive optimization: CONCEPTUAL_OPEN  
Peierls gap: positive bounded-support signal  
transparent defects: none in the exhaustive stated alphabet/support  
overall status: ARBITRARY_PERIOD_REMAINS_OPEN

## 11. Asymptotic m_n

residue 0: candidate/proved-family limit eta  
residue 2: candidate limit c6 via one G6  
residue 4: candidate limit c6 via two G6  
residue 6: candidate limit c6 via three G6  
common nonzero limit: SUPPORTED  
leading corrections: OPEN; matrix-valued, holonomy-dependent, several rows below double resolution

## 12. Algebraic Structure

c6 polynomial: PROVED, irreducible degree 10 from exact Evans resultant  
c10 polynomial: OPEN_SYMBOLIC_GROWTH_STOP  
charge recurrence: PROMISING period-eight insertion relation  
trace map: PROMISING_NOT_CLOSED

## 13. Chiral / Topological Audit

result: exact chiral `4+4` bulk reduction remains useful; no invariant jump or topological protection signal for G6/G10/gap2  
should enter final story: NO

## 14. Extensions

odd n: odd `d`, odd total charges, gap3/gap5 become relevant; separate project  
nearby circulant: order-six transfer for `C_n(1,3)` and no cheap cancellation signal  
continuous magnetic: formulation too broad; stopped

## 15. Complete Route Checklist

1. order-nine factorization STRONG
2. `9->4+4` STRONG
3. `4->2` STRONG
4. Chebyshev/cosh WEAK
5. shifted coefficients STRONG_FINITE
6. modal decomposition PROMISING
7. dominant mode PROMISING
8. dominant mode + prefix STRONGEST_OPEN_ROUTE
9. polyhedral cone WEAK
10. generating-function positivity FALSIFIED
11. closure Hankel FALSIFIED
12. symplectic/exterior trace STRONG_REDUCTION
13. finite Evans EXACT_FINITE
14. Rouche WEAK
15. argument principle NOT_APPLICABLE_WITH_REASON
16. Schur/Riccati WEAK
17. Birman-Schwinger PROMISING_PIECEWISE
18. rank/inertia STRONG_NEUTRAL
19. infinite Green WEAK
20. finite-ring Green comparison OPEN
21. matrix Fejer-Riesz/SOS WEAK
22. charge conservation PROVED
23. complete single-charge spectrum DETERMINISTIC_NUMERICAL
24. q=-2 STRONG_NUMERICAL_ABOVE_8
25. charge recurrence PROMISING
26. charge algebraic family PROVED_TEMPLATE/OPEN_GENERAL
27. two-slip theory PROMISING
28. three-slip theory STRONG_NUMERICAL
29. four-slip theory PROMISING
30. three-G6 vs G10 STRONG_NUMERICAL_REFRAME
31. effective interaction matrix STRONG_RECONSTRUCTION
32. genuine many-body interaction UNRESOLVED
33. two-path mod16 PROMISING
34. mixed charge decomposition STRONG_NUMERICAL
35. sub-eight atlas STRONG_BOUNDED
36. defect-crystal mining STRONG
37. density phase diagram PROMISING
38. M4 PROVED
39. M5/M6 PROVED_DATA
40. Hankel local certificate WEAK
41. local Rayleigh PROMISING_BUT_INSUFFICIENT
42. de Bruijn graph EXACT_BOUNDED_WEAK
43. cycle polytope PROMISING_NOT_BUILT
44. SDP/SOS WEAK
45. transfer multicone PROMISING
46. subadditive optimization CONCEPTUAL_OPEN
47. Peierls gap PROMISING_BOUNDED
48. transparent-defect search NO_COUNTEREXAMPLE_BOUNDED
49. asymptotic constants STRONGLY_SUPPORTED
50. finite-size corrections OPEN
51. c6 exact polynomial PROVED
52. c10 polynomial OPEN_GROWTH_STOP
53. general charge Evans algebra PROMISING
54. trace map PROMISING
55. topological audit NO_PROTECTION_SIGNAL
56. odd n PROMISING_SEPARATE
57. nearby circulant NOT_APPLICABLE_WITH_REASON
58. continuous relaxation NOT_APPLICABLE_WITH_REASON

## 16. Strongest Candidate Theorems

| Rank | Program | Novelty | Generality | Proximity | Difficulty | Clarity | JCTB | Computer dependence | Unification |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | B Elementary charged slip | 5 | 4 | 4 | 3 | 5 | 5 | 3 | 5 |
| 2 | C Fixed-r multi-slip | 5 | 4 | 3 | 4 | 5 | 5 | 4 | 5 |
| 3 | E Asymptotic residue phase diagram | 5 | 5 | 3 | 5 | 5 | 5 | 4 | 5 |
| 4 | A Eventual all-even | 4 | 4 | 4 | 4 | 4 | 4 | 3 | 4 |
| 5 | F Sub-eight phase classification | 4 | 4 | 3 | 4 | 4 | 4 | 4 | 3 |
| 6 | H Commensurate phase theorem | 5 | 4 | 2 | 5 | 4 | 4 | 4 | 4 |
| 7 | D Arbitrary-period crystallization | 5 | 5 | 1 | 5 | 5 | 5 | 4 | 5 |
| 8 | G General finite-defect theorem | 4 | 5 | 2 | 5 | 3 | 4 | 4 | 4 |

## 17. Recommended Scientific Direction

Primary direction: elementary charged-slip and fixed-r multi-slip theory  
Secondary direction: dominant-mode finite-ring theorem  
Reason: the first uses the exact c6 theorem and explains every nonzero residue; the second is the closest fallback proof and now has an exact k<=32 prefix.

## 18. Recommended Paper Story

Choose B: period-eight crystal -> exact elementary `+2` slip -> fixed-r multi-slip systems -> all nonzero even residues.  Do not edit manuscript.

## 19. Recommended Next Task

`TARGET_A_TASK52_ELEMENTARY_SLIP_THEORY`

Manuscript integration is not allowed yet because fixed-r counting and global lower bounds can still reframe the main theorem.

## 20. Evidence Inventory

PROVED: previous hard inputs; charge law; `1+4+4` and `4->2`; M4-M6 expansions; neutral core ranks/inertias; c6 degree-ten theorem  
COMPUTER_ASSISTED_PROVED: Task 50 G6/G10 interface theorems and bounded frontiers  
EXACT_FINITE: closure root exclusion through k=32; local Rayleigh windows; de Bruijn cycles through period 16  
HIGH_PRECISION: inherited Task 49 two-interface data  
EXPERIMENTAL: new charge spectrum, multi-slip clusters, sub-eight values, bounded Peierls costs, asymptotic candidates  
FALSIFIED: G10 fundamental role; pure cosh/positive moment closure; naive charged finite-rank model; present local-window uniqueness; topological protection story  
OPEN: uniform finite rings; fixed-r lower/counting theorem; arbitrary crystallization; exact new periodic families; common-limit theorem

## 21. Reviewer Verdicts

Spectral: piecewise bulk comparison is mandatory; three-G6 reframe is credible but not global  
Floquet: dominant mode plus exact prefix is best finite-ring route  
Combinatorial: charge law exact; odd/even charge legality must remain explicit  
Computer-assisted: labels and bounded scopes are sound; no PSLQ acceptance  
Hostile editor: Story B is the first genuinely theory-forward route; keep manuscript frozen

## 22. Verification

Full tests: `373 passed, 3 skipped, 20 subtests passed`  
Task51: 27 passed; verifier PASS  
Task50: verifier PASS  
Task49: verifier PASS  
Task48A: verifier PASS  
Task47: verifier PASS  
minimality: PASS  
computational evidence: PASS  
submission artifact: PASS  
manuscript freeze: PASS at Task 51 verifier

## 23. Git

Commits: baseline; recurrence reduction; proof bake-off; charge/multi-slip; periodic/crystallization; algebra/asymptotics; matrix/reviews; final synthesis  
Remote HEAD: to be verified equal to final local HEAD after push  
ahead/behind: target `0/0` after push  
working tree: target clean after final verification  
PR: NO

Final status: `TARGET_A_TASK51_STRUCTURAL_EXPLORATION_COMPLETE_MAJOR_REFRAME`
