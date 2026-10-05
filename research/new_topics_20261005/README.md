# Independent graph-theory results — 5 October 2026

This branch is an additive research snapshot based on `main` at `c3e4460929c38d10f0b3a0e878267142303c9675`. Existing repository files are unchanged. The C029 holonomy/Schur work remains on its separate research branch.

## Two independently audited results

### Sharp unique domination at n = 3γ + 1

For every integer `γ>=2`, the maximum edge count of a finite simple bipartite graph without isolated vertices, of order `3γ+1` and with a unique minimum dominating set of size γ, is

`γ(γ+7)/2`.

The maximum is attained by a connected graph. For `γ>=4`, the extremizer is unique up to isomorphism. At `γ=4`, a connected 13-vertex graph with 22 edges has a unique minimum dominating four-set and exceeds the proposed bound 21 in Koch–Narayan, arXiv:2511.01719v1, Conjecture 1. This comparison is unaffected by a separate printed summation-cutoff issue.

- [Complete sharp theorem and equality proof](unique_domination_pilot/SHARP_BOUNDARY_THEOREM.md)
- [Explicit counterexample family and source comparison](unique_domination_pilot/COUNTEREXAMPLE_FAMILY.md)
- [Independent proof audit](unique_domination_pilot/audit/PROOF_AUDIT.md)
- [Current scope and status](unique_domination_pilot/STATUS.md)

The general result is elementary and analytically proved; exhaustive local/finite checks corroborate it. No smallest-counterexample claim across the source's whole parameter domain, equality classification for γ=2,3, publication novelty or Lean formalization is asserted.

### Hall ratio of the six-chromatic Mycielski graph

With `M2=K2` and ordinary Mycielski iteration, `M6` has 47 vertices and Hall ratio exactly `10/3`. The lower witness has 20 vertices and independence number six. The complete upper certificate has 273 nodes (130 binary splits, 143 rational-dual leaves), checked using exact integers and fractions with an independently regenerated list of 857 maximal independent sets.

- [Structural proof and exact certificate argument](mycielski_pilot/PROOF.md)
- [Reproduction entry point](mycielski_pilot/README.md)
- [Independent exact audit](mycielski_pilot/audit/PROOF_AUDIT.md)

This first snapshot certifies the finite invariant and one extremal witness. Complete extremal classification, an all-order asymptotic result and literature-wide novelty are outside this snapshot.

## Source-led topic selection

[TOPIC_SCREENING.md](TOPIC_SCREENING.md) records the primary-source screen, including why some older arithmetic-packing and tournament-forcing conjectures were rejected as research targets. It preserves the earlier proposals with a dated outcome update. The current audited results above supersede the initial pilot questions. Third-party source papers and inspection screenshots are linked or cited, not redistributed.

## Reproduce the exact checks

Python 3 suffices for the verification commands below; no optimization solver is used by the exact checkers.

```sh
python mycielski_pilot/verify_structure.py
python mycielski_pilot/check_exact_certificate.py
python mycielski_pilot/audit/independent_check.py
python unique_domination_pilot/check_counterexample_independent.py
python unique_domination_pilot/check_local_cells.py
python unique_domination_pilot/check_small_family.py
python unique_domination_pilot/audit/independent_check.py
python check_domination_formula.py
```

The optional numerical discovery scripts in the Mycielski folder require SciPy/NumPy and are labeled exploratory. They are not proof premises. `mycielski_profile.cpp` supplies the exact M2–M5 baseline; compile it with a C++17 compiler. `VERIFICATION.json` records fresh package-level replay, and `MANIFEST.json` records delivered file hashes. The broad project registry and historical research log are preserved unchanged; this directory's status and claim ledger govern these new results.

