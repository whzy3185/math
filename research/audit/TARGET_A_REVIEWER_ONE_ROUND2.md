# Reviewer One, Round 2

## Review basis

This is an independent, adversarial review restricted to the revised manuscript, the current-status check, the submission artifact manifest, the manifest verifier, and the public source paper [Suvagiya, arXiv:2607.18334v1](https://arxiv.org/html/2607.18334). I did not inspect research notes, prior reviews or responses, claim inventories, unrelated repository files, or Git history.

- Manuscript: `TARGET_A_MANUSCRIPT_V2.md`
- Manuscript SHA-256: `7371fb31dbba160fb8c91a967952cf00a20357a743a12a72339aaad67aacf556`
- Public source version reviewed: arXiv:2607.18334v1, dated 19 July 2026
- Verdict: **REVISION REQUESTED; READINESS GATE PASSES**
- Gate rule: pass iff `CRITICAL=0` and `MAJOR=0`
- `gate_pass`: **true**

There are explicitly **no CRITICAL findings and no MAJOR findings**. The counterexample, its smallest-order conclusion subject to the disclosed exhaustive computation, the infinite period-eight family, the sharp band edge, the period-eight trichotomy, and the bounded low-period classification are mathematically coherent on the reviewed record.

## Scores

| Category | Score |
|---|---:|
| Mathematical correctness | 9.0/10 |
| Novelty positioning relative to source | 9.0/10 |
| Proof completeness | 8.0/10 |
| Notation and scope control | 8.5/10 |
| Computer-assisted proof acceptability | 7.5/10 |
| Overall | 8.4/10 |

## Findings

### 1. MODERATE: The proof-classification section understates the computational dependence of the moment results

**Lines 1132-1147, 1194-1198, 1337-1351.** Section 7 correctly says that collecting the 4, 36, and 430 closed words, and the longer period-eight excesses used in Theorem D, is a finite computer-assisted symbolic calculation. Section 9.1 then places the “first three moment formulas” among algebraic proofs presented in the text, while its list of computer-assisted assertions mentions outputs but does not clearly identify Theorem E's coefficient collection as computer-assisted. The recurrence and grouped result make the mathematics auditable, so this is not a correctness failure, but the proof boundary should be internally consistent.

**Required revision:** State explicitly in Section 9.1 that the coefficient collection underlying (7.4)-(7.6), and the `F_4`, `F_6`, and `F_9` values used in Theorem D, are exact computer-assisted symbolic identities verified by the named checker. Alternatively, supply a complete hand derivation of the grouped coefficients.

### 2. MODERATE: The central finite-minimality theorem lacks a documented end-to-end regeneration command and fully archived replay at every order

**Lines 572-583, 1372-1396, 1421-1447, 1776-1829.** Proposition 3.2 says that every nonoptimizer representative receives an exact rational Rayleigh certificate. The artifact discussion then discloses that the compact data through order 22 are aggregate attestations, recordwise independent generator equality stops at order 24, and fresh-regeneration chunks and full logs are outside the repository. Appendix C documents fast integrity/certificate checks and generator audits, but not an exact command line, resource estimate, expected terminal digest, or retained output path for a fresh end-to-end spectral regeneration through order 30.

This does not invalidate the theorem: the manuscript gives the quotient argument, exact decision form, deterministic source, committed checkpoint integrity, and explicit trust limits. It does, however, leave the strongest computational claim harder to reproduce independently than the paper's submission-ready framing suggests.

**Required revision:** Add repository-relative commands for fresh regeneration at each production order, expected state/chunk totals and terminal digests, and realistic runtime/RAM/disk estimates. Preferably archive the regeneration summaries and certificate-chain outputs needed to compare a fresh run without relying on off-repository logs.

### 3. MINOR: The asserted minimal polynomial is not proved irreducible

**Lines 811-817.** Equation (5.7) is called the minimal polynomial of `eta`, but the text only establishes that `eta` is a root. The claim is true, but minimality needs irreducibility over the rationals.

**Required revision:** Add the short irreducibility argument after translating `Y=X+4`: `X^4-20X^2+80` admits neither a factorization into quadratics with zero linear terms nor one with opposite nonzero linear terms over `Q`.

### 4. MINOR: `H_Q(z)` is used without a formal definition

**Lines 303-340, 413-418, 1652-1659.** The Floquet matrix is defined as `H_tau(z)`, after which the manuscript writes `H_Q(z)`. Although the canonical lift convention and Lemma 2.1 make all squared-spectral conclusions unambiguous, the matrix itself depends on a chosen lift and fiber reparametrization.

**Required revision:** Define `H_Q(z)` explicitly to mean the matrix formed from the canonical lift `tau_0=+1`, or retain `H_tau(z)` throughout and reserve `R(Q)` and `M_k(Q)` for lift-invariant quantities.

### 5. MINOR: “Global gauge negation” is misleading terminology

**Lines 125-127, 363-385.** The map `tau -> -tau` is induced here by negating all edge signs and sends `A` to a conjugate of `-A`; it is not ordinary vertex switching (gauge transformation), which preserves the spectrum rather than negating it.

**Required revision:** Replace “global gauge negation” with “global edge-sign negation” or “triangle-lift negation,” consistently with Lemma 2.1.

## Mathematical and novelty assessment

The public source paper proves the alternating-triangle family, its four switching classes, the holonomy-dependent value `rho_-(n)`, and exhaustive numerical verification only through `n=18`; it states the all-even global minimum as Conjecture 3. The revised manuscript clearly attributes those inherited ingredients at lines 43-60. Nothing in the reviewed source anticipates the order-32 counterexample, the infinite period-eight family, the exact value `eta`, the period-eight structural trichotomy, or the period-at-most-16 classification. The dated status language at lines 202-205 and 1481-1484 is appropriately bounded and does not overclaim absolute priority.

The analytic proofs are sound at paper-draft level. In particular, the positive-coefficient expansions at lines 692-721 and 781-809 correctly exclude larger squared fiber roots; the finite Floquet decomposition distinguishes discrete holonomy fibers from the full unit circle; the moment barrier is used only in its valid one-way direction; and the five residual Rayleigh certificates select the correct radical branch.

## Checker replay

The manifest verifier passed and authenticated all 20 named files from the pinned commit. Under the available system Python 3.9.6, the general-period moment checker, low-period structural-frontier checker, and periodic-operator-equivalence checker also passed. The literal Appendix C commands could not be run because `.venv-target-a` is absent. The minimality checker was blocked by missing NumPy, and the infinite-family, sharp-constant, period-eight structural, low-period spectral, and order-32 certificate checkers were blocked by missing SymPy. I did not create an environment or alter dependencies because the review instructions permit only the two requested new files.

The slow generator audits and a fresh full spectral regeneration were not run. These unexecuted checks are residual verification risk, not evidence of a mathematical failure.

## Severity counts

| Severity | Count |
|---|---:|
| CRITICAL | 0 |
| MAJOR | 0 |
| MODERATE | 2 |
| MINOR | 3 |

`gate_pass: true`
