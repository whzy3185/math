# Current research state: authoritative, superseded, and excluded material

## Authority rule

For the strengthening paper, this file and `strengthening_results.md` are the current editorial authority.  `current_verified_kernel.md` remains the immutable Phase-0 snapshot of what was known before strengthening; its “open questions” section is historical and has been resolved by the later Task 1A/1B/2A reports.

Mathematical statements are authoritative only when they are backed by the named analytic note and its independent verifier or by the frozen Lean kernel within its exact scope.

## Current conclusions

| ID | current conclusion | status | authoritative source | manuscript role |
|---|---|---|---|---|
| N1 | switching gives Hamilton-gauge coordinates ((\tau,\alpha)) | analytic; (\alpha=+1) route Lean checked | `current_verified_kernel.md`, K1 | setup |
| N2 | the target period-eight word has a finite (8\times8) Hermitian Bloch fiber and a chiral (8\to4\to2) reduction | analytic; core reduction Lean checked | K2–K5 | proof mechanism |
| N3 | the squared-fiber polynomial is (P(y,c)) and its top branch is (r(c)=4+\sqrt{8+c+\sqrt{26-3c}}) | analytic + independent symbolic audit | `task1B_alpha_negative_sector.md` | exact spectral theorem |
| N4 | for every (L\ge1), (\rho(A_{8L,+})^2=\eta=4+\sqrt{10+2\sqrt5}) | analytic + independent symbolic audit | `task1A_exact_finite_edge.md` | Main Theorem A |
| N5 | for every (L\ge1), the negative-holonomy sector has the exact (L)-dependent formula in Task 1B and lies strictly below (\eta) | analytic + independent symbolic audit | `task1B_alpha_negative_sector.md` | secondary theorem |
| N6 | for every (L\ge4), the positive-holonomy witness strictly beats the twisted signing | analytic; frozen (\alpha=+1) comparison Lean checked | K7 + Task 1A | main consequence |
| N7 | no legal displayed period below eight has squared Bloch edge below eight | moment reduction + nine exact certificates + independent audit | `task2A_minimal_period.md` | Main Theorem B |
| N8 | at period eight, the antipodal two-defect class is the unique sub-eight class modulo the stated symmetries | analytic + finite exact | K8–K9 | rigidity theorem |
| N9 | arbitrary periodic low-edge words satisfy the (M_1,M_2,M_3) density/clustering inequalities | analytic + finite closed-walk expansion | K10 | structural extension |

## Superseded claims and proof routes

| former item | current treatment | reason |
|---|---|---|
| (\rho(A_{8L,+})^2<1561/200) as the headline result | replace by exact equality (\rho(A_{8L,+})^2=\eta) | the finite phase grid contains the unique maximizing fiber (z=1) |
| a full “uniform polynomial certificate” section centered on (1561/200) | delete; at most one optional separator remark | (1561/200) is artificial once the exact edge is known |
| “period-eight is special” as informal commentary | replace by the minimal-period theorem plus period-eight trichotomy | now rigorously proved |
| an unexplained finite/infinite edge transition | replace by the finite direct-sum theorem and phase-grid attainment argument | exact finite spectral radius requires this bridge |
| alpha-negative holonomy as merely a uniform bound | replace by its exact closed formula | the top branch is explicit and monotone |
| one recent conjecture as the origin of the research question | remove from main narrative | fixed-graph signing optimization, switching, periodic graph spectra, and magnetic flux provide an independent mature context |
| broad claims that the chiral mechanism is general | remove | no general chiral classification was pursued or proved |
| claims that Lean checks the exact edge, negative sector, or minimal-period theorem | remove | frozen Lean scope is only the (\alpha=+1) L1–L7 comparison kernel |

## Material excluded from the paper

- R2/R4/R6/G6 and all-even classification projects;
- old exhaustive switching-class enumerations;
- stored certificates for abandoned scopes;
- global claims about (m_n) or all minimizers;
- M4/M5 exploration and a general defect classification;
- general chiral periodic-word classification;
- period 16/24/(8k) searches;
- quantitative second-best period-eight gap;
- repository history, failed approaches, and discovery chronology.

These items are not “future sections.”  They are out of scope unless a later referee asks for a mathematically specific addition.

## Formal-verification boundary

The frozen public endpoint is `TargetA.period8_alpha_plus_main_theorem`.  It checks the strict (\alpha=+1) comparison through the rational separator and does not contain placeholders or new axioms according to the frozen L1–L7 build record.

The strengthened exact equality, negative-holonomy formula, and minimal-period theorem are analytic/finite-exact and have independent SymPy verifiers.  They are not Lean-checked.  No manuscript sentence may merge these provenance categories.

## Construction now authorized

The next stage is not further theorem search.  It is the creation of a clean manuscript source from the architecture in `recommended_final_architecture.md`.

Required new construction:

1. a neutral notation ledger for (s,t,\tau,Q,\alpha,z,c,y,r,\eta);
2. final theorem statements with exact equivalence and quantifier language;
3. a manuscript-only proof of finite Bloch decomposition;
4. a manuscript-only derivation of the chiral polynomial and exact branch;
5. a compact exact-certificate presentation for the minimal-period theorem;
6. a precise period-eight trichotomy proof with only the necessary recurrence;
7. two vector figures (period-eight cell and finite cell decomposition), plus an optional dispersion plot;
8. a curated 13–18 item bibliography drawn from the literature landscape, not the whole venue corpus;
9. synchronized English and Chinese sources;
10. an integrity audit and independent JGT/LAA reviewer simulations before polishing.

## Current venue decision

- **JGT:** credible first target if the minimal-period and rigidity results organize the story.
- **LAA:** strongest direct fit and safer fallback because the exact matrix formulas are the most immediately recognizable contribution.
- **SIGMA:** unsuitable under the predefined corpus and general-mechanism gates.
