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

## Exact reproduction

Run from this directory with Python 3. The analytic verifier and direct-graph finite replay use the standard library; the symbolic checks also require SymPy (the recorded runs used version 1.14.0). NumPy is optional and used only for labeled numerical illustrations.

```sh
python certificates/analytic/verify_r2_certificate.py
python certificates/audit/replay_direct_graph_seed.py
python certificates/audit/replay_local_from_direct_graph.py
python certificates/new_conjecture/verify_antiperiodic_counterexample.py
python certificates/audit/replay_antiperiodic.py
```

The programs write their output certificates alongside their source. Exact graph construction, rational/integer positive-definiteness checks, and symbolic identities provide the mathematical evidence. Floating-point previews do not supply proof premises. The full infinite-family arguments are in the manuscript and separate proof reports.

For the PDF, run `pdflatex -interaction=nonstopmode -halt-on-error manuscript.tex` twice from `manuscript/`. See [build instructions](manuscript/README.md) for the local TeX format fallback used in this environment.

## Formal verification boundary

The fresh Lean extension rebuild is separate and pending. This snapshot includes no new Lean extension sources or new formal-PASS claim. The existing `formal/TargetA` baseline is preserved unchanged in the repository. In particular, the raw negative-holonomy adjacency-to-cell bridge and the residue-two Schur argument remain outside the formalized scope. Verified partial extension results may be added in a later commit, with precise theorem coverage.

## Provenance and file integrity

The research workspace was replaced during preparation. Delivered certificates were rerun and the manuscript rebuilt; source restoration/reconstruction and historical evidence are labeled explicitly in the individual recovery records. Third-party papers are linked, not redistributed.

`MANIFEST.json` records the SHA-256 and Git blob SHA for every delivered package file except the manifest itself. The repository commit independently fixes all file contents. Source and result files under `certificates/`, `literature/`, and `manuscript/` form the complete review package. This branch is a research delivery, not a journal submission.

