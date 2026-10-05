# C029: holonomy and Schur-tail research increment

Research snapshot: 5 October 2026. This standalone increment is based on `analytic-proof-first` at commit `7b6a351cc5f8f83f5527b7fc547f0a865ea50cf2`. It preserves that branch's existing paper and formal sources and does not merge another manuscript line. The inherited registry and research log remain unchanged historical records; the claim ledger in this package records the current increment.

## Start here

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
```

The programs write their output certificates alongside their source. Exact graph construction, rational/integer positive-definiteness checks, and symbolic identities provide the mathematical evidence. Floating-point previews do not supply proof premises. The full infinite-family arguments are in the manuscript and separate proof reports.

For the PDF, run `pdflatex -interaction=nonstopmode -halt-on-error manuscript.tex` twice from `manuscript/`. See [build instructions](manuscript/README.md) for the local TeX format fallback used in this environment.

## Verified partial Lean extension

The [fresh formal verification report](lean/VERIFICATION_REPORT.md) records successful baseline, sharp-edge and antiperiodic-cell builds plus two axiom audits, completed at 08:13:01 UTC. The extension adds 16 theorems; all 165 baseline-plus-extension theorem declarations were audited. Their axiom union is exactly `propext`, `Classical.choice`, and `Quot.sound`, with no `sorryAx` or project-specific axiom.

The exact extension sources and audit drivers are installed under the repository's `formal/` directory and also preserved with the report, pinned reproduction configuration and fresh logs in `lean/`. Existing baseline sources and configuration are unchanged. From `formal/`, run the five commands in the report; the new modules are built explicitly without editing `AllTheorems.lean`.

The results cover scalar polynomial endpoint bounds, antiperiodic phase exclusion, fiber eigenvalues, and the stated finite cell-eigenstate theorem. The raw negative-holonomy signed-graph adjacency-to-cell bridge, exact radical graph formula, integer n32 certificate and both R2 Schur theorems remain outside this formal extension. This is not an end-to-end Lean proof of either graph theorem.

## Provenance and file integrity

The research workspace was replaced during preparation. Delivered certificates were rerun and the manuscript rebuilt; source restoration/reconstruction and historical evidence are labeled explicitly in the individual recovery records. Third-party papers are linked, not redistributed.

`MANIFEST.json` records the SHA-256 and Git blob SHA for every delivered package file except the manifest itself. The repository commit independently fixes all file contents. Source and result files under `certificates/`, `literature/`, `manuscript/`, and `lean/` form the complete review package. This branch is a research delivery, not a journal submission.

