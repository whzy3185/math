# Task 58 Hostile Manuscript Review

Verdict: `READY_FOR_FINAL_SUBMISSION_AUDIT`.

Review checkpoint: `96efe50c55df82feb9e58f3fc71009f4292d1652` plus the
repairs recorded below. Review posture: Journal of Graph Theory editor and
hostile referee. The review covered mathematical logic, computer-assisted
proof boundaries, publication focus, bibliography, LaTeX, and all rendered
pages of the main paper and supplement.

```text
Open MAJOR: 0
Open MINOR: 0
Open EDITORIAL: 2 external metadata items
```

## 1. Headline and scope

PASS. Page 1 defines the independently signed cycle square and the exact
minimization problem. Pages 1--3 state the complete nonmonotone classification
and the structural single-gap theorem. The paper reads as an all-order
classification with a phase-slip explanation, not as a single-counterexample
note.

The Introduction credits Suvagiya's direct preprint before stating novelty.
The novelty sentence is restricted to all `{+1,-1}` edge signings of the fixed
family `C_n(1,2)`. JGT and exhaustive-generation references are used as proof
presentation precedents, not as direct novelty evidence.

## 2. Mathematical logic audit

PASS. The following points were checked against the canonical proof-completion
inventory.

- `m_n` and `rho_-(n)` are unsquared; `theta_n` and spectra of `A^2` are
  squared. No cross-type comparison remains.
- Equality uses both the analytic candidate-attainment direction and the
  universal exact lower-bound direction.
- The twisted attaining candidate and period-eight reference bulk remain
  different objects everywhere.
- The global mod-eight charge law and local mod-four sector law are proved and
  used separately.
- `c_6` is defined by its polynomial and rational isolating interval before a
  decimal is given.
- Essential-spectrum equality establishes discreteness and tail matching, not
  existence of `c_6`.
- A genuine unsquared physical zero is established before elimination
  identifies its square. Resultant roots remain candidates until an unsquared
  physical check accepts or excludes them.
- The G6 squared eigenspace has rank two; the two unsquared partners are
  simple. Exact separated-interface dimension is `2r`.
- Residue conclusions are limsup upper bounds only.
- IMS proves the analytic tail for all even `n>=240`; the finite bridge is
  separately required to place continuous failure at `48`.
- The finite classification determines the isolated failures at `32` and
  `40`; the G6 mechanism is not offered as their conceptual explanation.

## 3. Four-channel attack review and repairs

Four read-only attack reviews were run in parallel. No attack falsified a
theorem. Their actionable findings were repaired as follows.

### 3.1 Main-chain quantifiers

- The negative unsquared matching branch is now written at
  `lambda=-sqrt(y)` and related by the explicit `K` symmetry.
- The order-40 binary word now declares `1` as positive `Q` and `0` as
  negative `Q`.
- Residue zero now has its own monotonic propagation sentence rather than an
  undefined `D_0` notation.
- The novelty sentence now says `{+1,-1}` edge signings rather than the
  potentially ambiguous phrase "real edge signings."

### 3.2 G6 certification

- Appendix A now fixes the multiplier order, signed cofactor convention,
  Vandermonde quotient, column order, and continuous Evans orientation before
  using endpoint and derivative signs.
- It gives a finite exact construction of `E_0,E_1` from the printed transfer
  matrices and symmetric reduction.
- It proves the cross-chart implication "physical zero implies resultant
  zero," including the section zero and confluent repeated-multiplier point.
- The unique multiplier collision on the audit interval is separated by exact
  inequalities, not a floating root statement.
- Task 50 local matching and Task 51 elimination certificates and checkers are
  now included in the supplement inventory.
- The supplement discloses that some symbolic routines are shared; it no
  longer overstates every checker as a clean-room implementation. Two
  coordinate reconstructions still separately audit the global unsquared
  exclusions.

### 3.3 Finite classification and reproducibility

- All pytest files are invoked through `python3 -m pytest -q`; no inert
  `python3 test_*.py` command remains.
- The Task 56 checker is bound to the printed single-gap integer vectors and
  full images. The Task 55 structure certificate is described only for the
  transfer and recurrence data it actually contains.
- The manifest now includes the orders 8--30, order 32, six recovery orders,
  order 40, and 96-order bridge certificates and independent checkers.
- Appendix B now requires strictly positive leading principal minors and
  counts the two `tau_0` lifts explicitly when recovering `2^(n+1)` switching
  classes.

### 3.4 Publication package

- Nine visible literal `qquad` typos in the supplement were repaired.
- The anonymous PDF suppresses repository and source-SHA identity.
- Both main PDFs now carry title metadata; the anonymous author metadata is
  `Anonymous`.
- Figures 2 and 3 were relaid out after 100-percent-scale inspection to remove
  label collisions.

## 4. Computer-assisted proof boundaries

PASS. Each machine-assisted component exposes all four required stages:

| Component | Reduction | Finite exact object | Verification | Consequence |
|---|---|---|---|---|
| G6 edge | hyperbolic plane matching | transfers, atlas, candidates, intervals | exact signs, Sturm counts, two coordinate exclusions | physical global edge and rank two |
| Even 8--30 | switching/flux quotient | complete terminal decisions | exact independent reconstruction | universal lower bound, equality by attainment |
| Orders 32 and 40 | explicit signing plus PD criterion | exact matrices and rational bounds | Bareiss/rational LDL | strict counterexamples |
| Recovery orders | local exclusion and parity-lifted closure | all windows, walks, 64 terminals | exact rebuild, none unresolved | universal lower bounds |
| Even 48--238 | deterministic residue families | 96 rational PD records | full-matrix rational LDL rebuild | strict finite bridge |
| Even `n>=240` | patch identification and IMS | four rational endpoint comparisons | exact arithmetic | analytic monotone tail |

The supplement manifest names real repository artifacts only. Every listed
certificate and checker path was checked for existence.

## 5. Stale, draft, and workflow scans

PASS. Active manuscript and supplement prose contain none of the following:

```text
rank-one squared G6
exact-r cluster
codimension-r complement
r x r G6 Feshbach
p<=24 or period-25/26 frontier
common limit or common liminf theorem
interaction coefficient or three-body theorem
arbitrary multi-gap optimality
Task 52--57 workflow prose
TASK58_DRAFT_STUB, TODO, TBD, FIXME, PLACEHOLDER
```

Necessary terms in explicit nonclaims, such as the open multi-gap question,
were manually classified and are not active stale assertions. Author
footnotes are zero.

## 6. Length and visual audit

PASS. The identified paper is 38 pages: 23 narrative pages, 14 appendix
pages, and one bibliography page. The anonymous paper is 38 pages. The
separate supplement is 13 pages. No font, margin, or line-spacing compression
was used.

The main text has exactly three monochrome figures. Each is explicitly cited,
mathematically functional, grayscale-safe, and readable at 100 percent. All
main and supplement pages were rendered and inspected. No overlap, clipping,
orphaned heading, unexplained blank page, serious box warning, decorative
theorem container, or report/slide styling remains.

## 7. Literature and novelty

PASS. The direct prior-art search is dated 2026-08-24 and identifies
Suvagiya's preprint as the high-overlap predecessor. General signed-graph,
Floquet, extremal, and computer-assisted neighbors are distinguished by
scope. The cautious novelty sentence is supported by the recorded search and
does not claim the first signed spectral extremal classification.

The unpublished fixed-graph signing seminar remains a final-submission
watchlist item, not a cited theorem.

## 8. External metadata

These are not internal proof-package defects, but they remain mandatory
before an identified submission is uploaded:

1. replace author, affiliation, corresponding-author email, and ORCID
   placeholders with user-supplied metadata; and
2. create the promised immutable release/archive and insert its real DOI or
   persistent identifier.

The anonymous review PDF is usable without item 1 and contains neither the
repository owner nor the source commit. No DOI has been invented.

## 9. Review verdict

All internal MAJOR and MINOR findings are closed. The mathematical article,
appendices, anonymous review build, and supplement are ready for the final
submission audit. External author and archive metadata remain explicitly
pending.
