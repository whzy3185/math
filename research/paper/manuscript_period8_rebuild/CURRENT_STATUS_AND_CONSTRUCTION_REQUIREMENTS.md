# Period-eight article: current-status and construction control

**Date:** 2026-09-04  
**Article scope:** the analytic period-eight counterexample family only.  
**Scope rule:** an explicit alpha = +1 signing on `C_(8L)(1,2)`, for `L >= 4`,
strictly beats the twisted benchmark.  This article does not attempt an
all-even classification.

## 1. Source hierarchy for this article

| Class | Meaning for the new article | Approved sources |
|---|---|---|
| A. Frozen main kernel | The current source for every theorem in Sections 1--5 | `formal/TargetA/`, `research/analytic_inventory/period8_complete_analytic_proof.md`, `twisted_benchmark_derivation.md`, `hamilton_gauge_realization.md`, `period8_article_dependency_audit.md`, `analytic_claim_registry.md` |
| B. Current analytic structural extension | Current source for Sections 6--7, but not part of the Lean claim | `period8_trichotomy_analytic_proof.md`, `period8_two_defect_closed_walk_lemma.md`, `general_period_defect_obstruction.md`, `periodic_moment_lemma.md` |
| C. Current editorial/literature material | Use only after claim-by-claim verification in the new bibliography | `research/related_work/reports/current_reference_audit.md`, `literature_review.md`, `venue_architecture.md`, individual source notes |
| D. Current for a different paper scope | May be mathematically current for the repository's all-order/classification package, but is excluded from this concise period-eight paper | `research/paper/proof_completion/`, `research/paper/task58/`, `research/paper/task59/`, associated complete-classification manuscript trees |
| E. Historical or superseded | Do not import theorem wording, formulas, or proof prose into the new article | `research/paper/manuscript_tex_pub/`, `research/paper/manuscript_tex_pub_zh/`, old manuscript versions, historical exact-r corpus listed in `TARGET_A_MANUSCRIPT_IMPORT_SAFETY.md` |
| F. Exploratory or incomplete | Retain only as research provenance; do not use in theorem prose | `research/analytic_inventory/r2_*`, `r4_*`, `r46_*`, `g6_*`, residue-tail programmes, unclosed all-even routes |

## 2. What is currently established

### 2.1 Main analytic conclusion

For every integer `L >= 4`, the explicit period-eight word

`tau=(1,1,-1,1,-1,-1,1,-1)`

with alpha = +1 produces a signing of `C_(8L)(1,2)` satisfying

`rho(A)^2 < 1561/200 < rho_minus(8L)^2`.

Permitted interpretation: the twisted signing is not spectrally optimal on
every multiple of eight at least 32.  Forbidden interpretation: this does
not determine the global minimum, all minimizers, all even orders, or any
nonzero residue class modulo eight.

### 2.2 Analytic package

1. Hamilton gauge and the finite cell relation `z^L=alpha`.
2. The explicit eight-site fiber and chiral involution.
3. The `8 by 8 -> 4 by 4 -> 2 by 2` determinant reduction.
4. The polynomial
   `P(y,c)=y^4-16y^3+(80-2c)y^2+(-128+16c)y+c^2-13c+38`.
5. The exact infinite-volume squared edge
   `4+sqrt(10+2sqrt(5))`.
6. The rational positivity certificate at `1561/200`.
7. The analytic shifted-grid formula for the twisted benchmark.

### 2.3 Formal verification status

The frozen Lean scope is **only the explicit alpha = +1 witness**.  The
formal chain is

```text
finite Hamilton matrix
  -> finite cells
  -> ZMod cell action
  -> nonzero DFT fiber
  -> chiral fiber polynomial
  -> lambda^2 < 1561/200
  -> every Hermitian eigenvalue beats the twisted squared benchmark.
```

The public entry theorem is `TargetA.period8_alpha_plus_main_theorem`.
`lake build` passes at freeze commit `c1c4600` and again after the draft
commit `4034a6d`; `TargetA` contains no `sorry`, `admit`, or author-added
`axiom`.

The generic ENNReal `spectralRadius` wrapper is not frozen: Mathlib's matrix
normed-algebra elaboration timed out.  This is an API packaging gap, not a
gap in the Hermitian all-eigenvalue comparison theorem.  Until it is resolved,
the Lean disclosure must say *Hermitian eigenvalue form*, not imply a separate
generic spectral-radius API theorem.

## 3. Material that is not current for this article

| Material | Reason for exclusion |
|---|---|
| Old `TARGET_A_MANUSCRIPT_V1/V2` and publication LaTeX trees | They blend period-eight results with low-order enumeration, bounded-period frontiers, and broader classification claims. |
| `manuscript_tex_pub/` and `manuscript_tex_pub_zh/` | Explicitly marked historical in the repository import-safety manifest. |
| `proof_completion/` classification package | It serves a different all-order/finite-computation editorial programme. Its status does not enlarge the present article's scope. |
| R2, R4, R6, G6 notes | Incomplete, conditional, or intentionally excluded from the analytic period-eight theorem. |
| Old exact-r/Feshbach corpus | Explicitly historical or barred by the repository import-safety manifest. |
| Finite enumeration through order 30 and smallest-counterexample assertions | Computation-only background; excluded by the chosen analytic story. |
| Numerical eigensystem evidence and certificate archives | Not needed for the Sections 1--5 theorem and should not enter the main text. |

## 4. Required construction inputs before drafting a submission manuscript

| Need | Why it is needed | Current state |
|---|---|---|
| Author-approved contribution sentence | ARS requires the author, not the system, to choose the article's central contribution wording | missing |
| Target venue decision | Determines length, citation style, introduction balance, and whether the compact structural Sections 6--7 stay in main text | provisional only: JGT/LAA have been discussed |
| Verified reference shortlist | Direct predecessor, fixed-graph signing context, periodic/Floquet precedent, and one or two editorial architecture precedents | candidates exist; final source verification pending |
| Author list, affiliations, corresponding author, funding | Required for a submission package; placeholders are acceptable during anonymous drafting | missing / placeholders permitted |
| Decision on Sections 6--7 | Determines whether the paper is a concise six-section mechanism article or the requested eight-section structural article | user requested eight sections; word-budget decision still needed |
| Exact notation and theorem labels | Prevents conflict between the new article and historical manuscript trees | dependency map exists; journal draft labels pending |
| Lean disclosure wording | Must state alpha = +1 and Hermitian eigenvalue-form coverage precisely | draft wording exists |

## 5. Construction rules after article work begins

1. Draft by mathematical dependency, never by repository discovery order.
2. Use the new directory `manuscript_period8_rebuild/` only; do not overwrite
   frozen publication trees.
3. Keep computer material out of Sections 1--5.  In Section 6, retain only
   the explicit integer closed-walk recurrence and its displayed values.
4. Do not call any finite enumeration, numerical eigenvalue calculation, or
   certificate archive an analytic proof.
5. Keep alpha = -1 out of the Lean verification statement.  The analytic
   theorem may discuss both holonomies only after its own proof is checked
   independently from the formal disclosure.
6. Before adding every citation, verify its bibliographic identity and the
   exact claim it is being used to support.
7. Do not introduce R2/R4/R6/G6, low-order minimality, or all-even claims in
   the abstract, theorem statements, conclusion, or reference framing.

## 6. Immediate next work

1. Resolve the author-owned configuration questions below.
2. Build a verified reference matrix and choose the target journal.
3. Expand Sections 1 and 6--8 from the approved contribution statement.
4. Perform a human line audit of the displayed fiber, chiral reduction, and
   polynomial expansion before calling the manuscript ready for review.
