# C029: holonomy and Schur-tail research increment

Research snapshot: 5 October 2026. This standalone increment is based on `analytic-proof-first` at commit `7b6a351cc5f8f83f5527b7fc547f0a865ea50cf2`. It preserves that branch's existing paper and formal sources and does not merge another manuscript line. The inherited registry and research log remain unchanged historical records; the claim ledger in this package records the current increment.

## Start here

- [Current integrated18-page paper](manuscript_integrated/manuscript.pdf), [editable source](manuscript_integrated/manuscript.tex), and [Chinese handoff](manuscript_integrated/HANDOFF.zh-CN.md)
- [Independent integration review](manuscript_integrated_review/INTEGRATION_REVIEW.md)

The earlier11-page paper below is preserved as the first snapshot. The integrated paper consolidates both caps, unequal-cell assembly and all R2/R4/R6 witness ranges at the237-declaration formal checkpoint.

- [Complete English manuscript (PDF)](manuscript/manuscript.pdf)
- [English reading copy](manuscript/manuscript.md) and [editable LaTeX](manuscript/manuscript.tex)
- [中文交接与证明边界](manuscript/HANDOFF.zh-CN.md)
- [Claim ledger](manuscript/CLAIM_LEDGER.md) and [proof dependencies](manuscript/PROOF_DEPENDENCY_MAP.md)
- [Primary-source literature audit](literature/LITERATURE_AUDIT.md)

## Supported results

1. For the prescribed period-eight triangle signs, the negative-Hamilton-holonomy signing has exact radius `R(2 cos(pi/m)) < R(2)`, where `R(s)=sqrt(4+sqrt(8+s+sqrt(26-3s)))`. This refutes Conjecture 28 of [arXiv:2607.17343v2](https://arxiv.org/html/2607.17343v2#S12.SS3) for every `m>=4`. The exact finite formula is inherited from the [earlier project manuscript](https://github.com/whzy3185/math/blob/085ea698475b7b32e0ae57457ec903a922248f69/research/paper_strengthening/manuscript_period8_jgt/sections_en/04_period8_exact.tex), freshly reverified here and applied to the revised conjecture. No first-discovery or publication-priority claim is made.
2. An explicit residue-two signing satisfies `(198/25)I-A_n^2 > 0` for every `n=8k+2>=50`. The increment is a finite-certificate-assisted analytic Schur-tail closure: seven finite bases `50,58,66,74,82,90,98`, one normalized six-dimensional seed at `106`, and an explicit all-length tail estimate. It is a proof-method upgrade of an inherited family.

These results do not determine unrestricted spectral minima, classify every minimizing signing, or freshly certify the historical all-even classification. The old unnormalized eight-dimensional `9/20` seed margin must not be used for the normalized six-dimensional core. The correct seed margin here is `1/50`.

## Verified strengthening supplement

The [uniform one-G6 supplement](certificates/strengthening/UNIFORM_ONE_G6_CAP.md) sharpens the explicit residue-two family to `rho(A_(8k+2))^2 < 7.90537` for every `k>=1`, including the exceptional order `n=10`. A separately checked order-202 obstruction gives `rho(A_202)^2 > 7.905369`, placing the supremum of this prescribed family in `(7.905369, 7.90537]`. The upper endpoint is closed. No global optimizer, exact supremum or limiting monotonicity is claimed.

The complete supplement has new exact finite premises, 24 smaller bases, one seed, and an independent direct-graph/analytic audit. The 11-page manuscript remains the first snapshot; this stronger theorem is supplied as a separate proof supplement. See the additional C6 entry in the claim ledger.

## Phase-uniform and balanced R4 supplement

The [phase-uniform assembly proof](certificates/r4_pilot/PHASE_UNIFORM_R4_ASSEMBLY.md) extends the one-G6 cap to every unit complex phase for cell length `h=8j+2>=202`. Repeating an identical cell any positive number of times, with either Hamilton holonomy, preserves the squared-radius cap `7.90537`.

For the balanced negative-holonomy R4 family at `N=16j+4`, the cap holds for every `j>=1`, with 24 exact finite bases completing the small orders. It strictly improves the twisted benchmark for `j>=3` (`N>=52`). This covers the even-k subsequence of `N=8k+4`; an exact negative-pivot certificate at `N=60` disproves deletion of that parity restriction. Arbitrary defect arrangements and the odd-k R4 theorem are outside this result. See [independent audit](certificates/r4_pilot/audit/INDEPENDENT_R4_PHASE_AUDIT.md).

## Unequal-cell assembly and all-even witness completion

The [unequal-cell Schur theorem](certificates/unequal_cells/UNEQUAL_CELL_SCHUR_THEOREM.md) allows any positive number of unequal legal cells and either holonomy. If every cell has length at least106, the squared spectral radius is below7.92; at length at least202, it is below7.90537. A degree-two bound controls the full6r-dimensional retained matrix with error independent of the cell count.

For every `N=8k+4>=52`, the near-balanced two-cell construction has `rho^2<7.92<rho_tw(N)^2`. Odd k uses a changed unequal-cell word;20 exact finite bases join the analytic tail. The sharper7.90537 cap fails for some short changed examples, so it is not substituted into this full-range theorem.

The [residue-six completion](certificates/r6_completion/R6_FINITE_COMPLETION.md) uses three legal cells and positive Hamilton holonomy to prove the same strict7.92 comparison for every `N=8k+6>=54`. Its33 exact bases end at310, immediately before the analytic range beginning at318.

Together with the period-eight and R2 results, these constructions give explicit witnesses beating the twisted benchmark at every even `N>=48`. This completes the witness direction, not the smaller-order equality cases, actual global minima or minimizer classification. All new Schur-family results remain outside the Lean formalization.

## Exact reproduction

Run from this directory with Python 3. The analytic verifier and direct-graph finite replay use the standard library; the symbolic checks also require SymPy (the recorded runs used version 1.14.0). NumPy is optional and used only for labeled numerical illustrations.

```sh
python certificates/analytic/verify_r2_certificate.py
python certificates/audit/replay_direct_graph_seed.py
python certificates/audit/replay_local_from_direct_graph.py
python certificates/new_conjecture/verify_antiperiodic_counterexample.py
python certificates/audit/replay_antiperiodic.py
python certificates/strengthening/verify_uniform_cap.py
python certificates/strengthening/audit/replay_stronger_cap.py
python certificates/r4_pilot/verify_r4_pilot.py
python certificates/r4_pilot/audit/replay_r4_phase.py
python certificates/unequal_cells/verify_unequal_cells.py
python certificates/unequal_cells/audit/independent_assembly.py
python certificates/r6_completion/verify_r6_completion.py
python certificates/r6_completion/audit/replay_r6.py
```

The programs write their output certificates alongside their source. Exact graph construction, rational/integer positive-definiteness checks, and symbolic identities provide the mathematical evidence. Floating-point previews do not supply proof premises. The full infinite-family arguments are in the manuscript and separate proof reports.

For the PDF, run `pdflatex -interaction=nonstopmode -halt-on-error manuscript.tex` twice from `manuscript/`. See [build instructions](manuscript/README.md) for the local TeX format fallback used in this environment.

## Exact finite-radius Lean checkpoint

The [exact-radius verification report](lean/exact_radius/EXACT_RADIUS_VERIFICATION_REPORT.md) proves, for every L>0, the precise negative-holonomy finite radius `sqrt(4+sqrt(8+2*cos(pi/L)+sqrt(26-6*cos(pi/L))))` for the original raw matrix: every Hermitian eigenvalue modulus is at most this number, and a positive eigenvalue attains it. No radius equality, seam equivalence or Fourier decomposition is assumed.

The full audit covers237 declarations (149 baseline and88 extension theorems), using only propext, Classical.choice and Quot.sound. Sources and audit drivers are installed under formal/; inherited source and configuration files remain unchanged. Earlier165/196 bundles remain preserved checkpoints. See [current status](lean/CURRENT_STATUS.md).

At this checkpoint, identification with the largest root of the separate paper-naming quartic, finite-size asymptotics, the integer n32 certificate, the Riccati/Schur families and unrestricted minima remain outside formal scope. The integrated18-page article records this precise237 checkpoint; subsequent verified addenda may be linked separately.

## Provenance and file integrity

The research workspace was replaced during preparation. Delivered certificates were rerun and the manuscript rebuilt; source restoration/reconstruction and historical evidence are labeled explicitly in the individual recovery records. Third-party papers are linked, not redistributed.

`MANIFEST.json` records the SHA-256 and Git blob SHA for every delivered package file except the manifest itself. The repository commit independently fixes all file contents. Source and result files under `certificates/`, `literature/`, `manuscript/`, and `lean/` form the complete review package. This branch is a research delivery, not a journal submission.

