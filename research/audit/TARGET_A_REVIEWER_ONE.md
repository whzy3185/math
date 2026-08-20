# Reviewer One Report

## Review metadata

- Role: independent, adversarial Reviewer One
- Intended venue standard: *Journal of Graph Theory* / *SIAM Journal on Discrete Mathematics*
- Manuscript: `TARGET_A_MANUSCRIPT_V1.md`
- Manuscript SHA-256: `d95e22a2a8028988402aa964bf95a143cf29136502398d7c50e59c7467105ba8`
- Reviewed UTC: `2026-08-20T07:27:59Z`
- Verdict: **MAJOR REVISION**
- Gate pass: **false**

## Overall assessment

The manuscript appears to contain a substantial and genuinely new response to Suvagiya's Conjecture 3. Relative to the original paper, which derives the alternating-flux family and its two spectral-radius values and reports numerical exhaustive verification only through order 18, the present draft adds an exact order-32 counterexample, a rigorous infinite family for multiples of eight, an exact period-eight band edge, a structural period-eight classification, general moment obstructions, and a bounded low-period classification. These are significant advances if the exhaustive claims are supplied in an auditable form.

I found no internal mathematical contradiction in the analytic core. In particular, the manuscript correctly distinguishes the finite Floquet set `z^L=alpha` from the infinite unit circle; consistently uses `R(Q)` as a squared spectral radius; supplies the positive-branch hypotheses needed in the radical comparison; and uses the moment barrier only in the valid direction `F_k>0 => R(Q)>8`. The claims are carefully bounded: the draft does not claim failure at every even order, optimality over all periods or all signings, or absolute priority. The dated public-status language is appropriately qualified.

The decisive readiness defect is evidentiary. The two most consequential exhaustive results, Theorems A and F, are supported in the manuscript by aggregate descriptions of computations and references to repository-relative commands, but the submission neither includes the decisive per-state proof objects nor identifies a stable, public, immutable supplement containing them. This prevents an independent referee from checking the claimed exhaustive coverage and exact decisions from the submitted materials.

The three separate appendix files merge faithfully. Their SHA-256 values exactly equal the hashes of the corresponding manuscript blocks: Appendix A `1235f1a916d471dfe7d4d3c776d14b1c51782aff717ca7deb43247b7c59555f4`, Appendix B `d67d5e7c8fee9ca157dc791b88d9239d59e7795ef099b86a426b713053ec6235`, and Appendix C `54754865236fc784211f617ee6356bae3b09d79dee48d7f0e736334255a49572`.

## Scores

| Dimension | Score (1-5) | Assessment |
|---|---:|---|
| Correctness | 3 | Analytic arguments appear sound, but core exhaustive conclusions are not independently auditable from the submission. |
| Novelty | 5 | The counterexample, infinite family, sharp edge, and structural classifications go well beyond the original paper. |
| Significance | 4 | Refuting the conjecture at its first failure and explaining the period-eight mechanism are journal-relevant contributions. |
| Clarity | 4 | Scope and key distinctions are unusually careful; several computational and period conventions still need definition. |
| Proof flow | 3 | The analytic flow is strong, but several finite enumerations are reported rather than exhibited as proof bodies. |
| Computer-assisted acceptability | 2 | Exact arithmetic and trust limits are described well, but the decisive artifacts are not supplied or stably cited. |

## Findings

### R1-001 - MAJOR - Computer-assisted proof

**Title:** The core exhaustive theorems lack an accessible submitted proof artifact

**Exact manuscript lines:** 541-569; 1193-1273; 1292-1378; 1640-1704.

**Consequence:** The smallest-counterexample assertion in Theorem A and the uniqueness assertion in Theorem F depend on millions of exact decisions and complete representative sets that are not present in the manuscript. Aggregate counts, claimed digests, and descriptions of external checkpoints do not let a referee verify either the per-state inequalities or the absence of an omitted/duplicated state. Appendix C gives repository-relative commands but no repository URL, immutable commit, archival DOI, artifact manifest, or submitted certificate bundle. The disclosed limitation that recordwise independent generator agreement stops at order 24 is especially material because minimality depends on orders 26, 28, and 30. As submitted, these headline claims are not auditable computer-assisted proofs.

**Required revision:** Deposit the complete checker source, canonical representative manifests, exact certificate/checkpoint data needed for every decisive state, pinned dependencies, and regeneration instructions in a stable public archive; cite its immutable identifier in the paper and bind the paper to artifact hashes. Include a compact machine-checkable manifest in the supplement and explain precisely which independent checks cover each order. Theorem A and Theorem F should not be presented as proved until that supplement is part of the submission and can be rerun by a referee.

### R1-002 - MODERATE - Proof completeness

**Title:** The displayed order-32 LDL^T certificate is described but not displayed

**Exact manuscript lines:** 473-513; 1616-1625.

**Consequence:** Proposition 3.1 says that 32 pivots or leading principal minors are positive, while Appendix B says those values constitute the exact certificate, but none is given. Thus the proof at the point where Theorem A invokes it is not checkable from the manuscript. This does not appear fatal to the mathematics because Sections 4.1-4.3 later provide a separate, explicit Floquet-polynomial positivity proof of the stronger uniform bound.

**Required revision:** Either list the 32 pivots/minors in Appendix B or rewrite Proposition 3.1 to invoke the explicit determinant and positivity argument of Sections 4.1-4.3, moving that argument before Theorem A if necessary for a clean proof order.

### R1-003 - MODERATE - Exact certificates and notation

**Title:** H_Q(z) is not defined at the lift level needed by the five Rayleigh certificates

**Exact manuscript lines:** 268-272; 311-318; 1231-1255; 1581-1614.

**Consequence:** A legal `Q` has two lifts, `tau` and `-tau`. The manuscript establishes that their squared spectral radii agree, which makes `R(Q)` unambiguous, but an explicit matrix-vector quotient depends on which lift and fiber basis are used. The five vectors are therefore not formally reconstructible from the stated notation `H_Q(z)`. Under the natural convention `tau_0=+1` followed by `tau_(i+1)=Q_i tau_i`, all five displayed quotients do reproduce exactly, so this appears to be a specification defect rather than a false calculation.

**Required revision:** Define a canonical lift and fiber ordering for every explicit certificate, preferably `tau_0=+1` with the recursion already given, or list the full `tau` word for each row. State how the certificate transforms under the other lift.

### R1-004 - MODERATE - Proof completeness

**Title:** Closed-walk enumerations closing Theorems D and E are asserted without an auditable derivation

**Exact manuscript lines:** 943-954; 987-1002; 1092-1107; 1285-1301.

**Consequence:** The coefficients in `M_3`, the collection of 430 length-six words, and the first positive excesses `F_4=5504`, `F_6=64336`, and `F_9=2872096` are essential to the period-eight trichotomy and general moment theorem. The manuscript states the enumeration rule and outputs but does not provide the grouped count table, a recurrence, or an included checker. The values are internally consistent and the three excesses can be independently reconstructed, but the proof body is thinner than the manuscript's classification of these results as fully algebraic.

**Required revision:** Add a short dynamic-programming or Laurent-polynomial recurrence, the grouped monomial counts, and a compact exact checker or supplementary table reproducing the stated moments and excesses. State explicitly whether these steps are hand-verifiable finite algebra or computer-assisted calculations.

### R1-005 - MINOR - Citation and novelty positioning

**Title:** The source conjecture and inherited spectral formula are not cited in the body

**Exact manuscript lines:** 43-53; 421-439; 1725-1728.

**Consequence:** The introduction attributes results to Suvagiya and repeatedly invokes “the source paper,” but no in-text citation points to reference 5. This weakens the boundary between inherited material and the manuscript's new contribution and leaves most of the bibliography orphaned.

**Required revision:** Cite the original paper at the first definition of the distinguished family, the formula for `rho_-(n)`, and Conjecture 3; cite the companion work where relevant; and add a concise related-work paragraph explaining which propositions are borrowed and which results are new.

### R1-006 - MINOR - Terminology at order eight

**Title:** Quadrilateral flux word is potentially misleading for n=8

**Exact manuscript lines:** 213-217; 262-285; 534-545.

**Consequence:** At order eight the graph has two additional step-two quadrilaterals beyond the local cycles encoded by `Q_i=tau_i tau_(i+1)`. The manuscript's coordinate system remains complete because `(tau,alpha)` is used for finite signings, but the unqualified term “the quadrilateral flux word” can be read as encoding every quadrilateral flux at `n=8`.

**Required revision:** Call the `Q_i` the distinguished/local quadrilateral fluxes and add a sentence noting the two exceptional order-eight quadrilaterals and why they do not affect the complete `(tau,alpha)` parametrization or the all-signings enumeration.

### R1-007 - MINOR - Scope definition

**Title:** The primitive-period domain in Theorem F should be stated self-containedly

**Exact manuscript lines:** 146-149; 1167-1191; 1208-1219; 1270-1277.

**Consequence:** “Primitive Hamilton-gauge period” is not formally defined in the theorem statement, and the enumeration mixes displayed `Q` cells with primitive `tau` periods and repeated cells. The later discussion makes the intended infinite-volume domain recoverable, but the headline theorem can be misread as minimizing over primitive `Q` periods or over finite holonomy sectors.

**Required revision:** State directly that the domain consists of infinite operators whose Hamilton-gauge triangle word `tau` has primitive period at most 16, that the minimized quantity is the squared infinite-volume radius `R`, and that repeated displayed cells are retained only for complete certificate accounting and then identified by zone folding.

## Severity counts and gate

| Severity | Count |
|---|---:|
| CRITICAL | 0 |
| MAJOR | 1 |
| MODERATE | 3 |
| MINOR | 3 |
| **Total** | **7** |

`gate_pass = false` because `MAJOR=1`.

## Recommendation

**Major revision.** The manuscript's central analytic contribution is promising and, on the material available, appears mathematically coherent. The exact counterexample family, sharp period-eight edge, moment direction, branch conditions, squared-radius notation, and bounded scope are handled responsibly. Publication readiness turns on converting the exhaustive claims from descriptions of an unavailable computation into a stable, rerunnable, submission-linked computer-assisted proof, together with the smaller certificate and notation repairs above.
