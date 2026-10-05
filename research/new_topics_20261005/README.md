# Independent graph-theory results — 5 October 2026

This branch is an additive research snapshot based on `main` at `c3e4460929c38d10f0b3a0e878267142303c9675`. Existing repository files are unchanged. The C029 holonomy/Schur work remains on its separate research branch.

## Two independently audited results

### Sharp unique domination at n = 3γ + 1 and 3γ + 2

For every integer `γ>=2`, the maximum edge count of a finite simple bipartite graph without isolated vertices, of order `3γ+1` and with a unique minimum dominating set of size γ, is

`γ(γ+7)/2`.

The maximum is attained by a connected graph. The equality graph is unique up to isomorphism for every `γ>=2`: the [audited low-γ supplement](unique_domination_pilot/extension/LOW_GAMMA_EQUALITY.md) completes the two small cases beyond the first paper’s `γ>=4` rigidity proof. At `γ=4`, a connected 13-vertex graph with 22 edges has a unique minimum dominating four-set and exceeds the proposed bound 21 in Koch–Narayan, arXiv:2511.01719v1, Conjecture 1. This comparison is unaffected by a separate printed summation-cutoff issue. The same n13 counterexample and the cutoff issue were already reported by John Erlbacher; the emphasis here is the all-γ sharp maximum and equality structure. See the [prior-work attribution and exact isomorphism check](unique_domination_pilot/extension/prior_work/PRIOR_WORK_ADDENDUM.md).

- [Current ten-page integrated article](unique_domination_pilot/paper_v2/manuscript.pdf) and [Chinese handoff](unique_domination_pilot/paper_v2/HANDOFF.zh-CN.md)
- [Preserved seven-page article with corrected prior-work attribution](unique_domination_pilot/paper/manuscript.pdf) and [Chinese handoff](unique_domination_pilot/paper/HANDOFF.zh-CN.md)
- [Complete sharp theorem and equality proof](unique_domination_pilot/SHARP_BOUNDARY_THEOREM.md)
- [Explicit counterexample family and source comparison](unique_domination_pilot/COUNTEREXAMPLE_FAMILY.md)
- [Independent proof audit](unique_domination_pilot/audit/PROOF_AUDIT.md)
- [Current scope and status](unique_domination_pilot/STATUS.md)

At order `3γ+2`, the sharp maximum is `ceil(γ²/2)+5γ` for every `γ>=2`, with connected attainment. At least two nonisomorphic connected extremals exist for every even `γ>=4`; a complete equality classification for this second boundary is not claimed. See the [complete analytic proof](unique_domination_pilot/extension/two_extra/CANDIDATE_BOUNDARY_THEOREM.md), [independent audit](unique_domination_pilot/extension/two_extra/audit/PROOF_AUDIT.md), and [precise prior overlap](unique_domination_pilot/extension/two_extra/SOURCE_COMPARISON.md).

The general result is elementary and analytically proved; exhaustive local/finite checks corroborate it. No smallest-counterexample claim across the source's whole parameter domain, publication novelty or Lean formalization is asserted.

### Hall ratio of the six-chromatic Mycielski graph

With `M2=K2` and ordinary Mycielski iteration, `M6` has 47 vertices and Hall ratio exactly `10/3`. The lower witness has 20 vertices and independence number six. The complete upper certificate has 273 nodes (130 binary splits, 143 rational-dual leaves), checked using exact integers and fractions with an independently regenerated list of 857 maximal independent sets.

- [Structural proof and exact certificate argument](mycielski_pilot/PROOF.md)
- [Reproduction entry point](mycielski_pilot/README.md)
- [Independent exact audit](mycielski_pilot/audit/PROOF_AUDIT.md)

The [complete classification supplement](mycielski_strengthening/CLASSIFICATION.md) now gives exactly1,990 labelled maximizing subsets in199 ambient-automorphism orbits, all of size20 and independence number6. The three original/clone/apex layer types have109,83,7 orbits. These are embedded-subset orbits, not abstract graph-isomorphism types. Two different exact enumerations reproduce the same complete list.

Read the [revised six-page note including Chinese abstract](mycielski_manuscript/output/pdf/mycielski_hall_note.pdf), [general compression theorem](mycielski_strengthening/GENERAL_THEOREM.md), and [independent completeness audit](mycielski_strengthening/audit/PROOF_AUDIT.md). The [reviewed presentation correction](mycielski_positioning_revision/audit/POSITIONING_REVIEW.md) adds the classical output-sensitive enumeration comparison and makes branch-certificate complexity conditional on an independently established complete constraint system. No general algorithmic efficiency improvement, all-order asymptotic or publication-novelty claim is made.

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
python mycielski_strengthening/test_general_module.py
python mycielski_strengthening/check_strengthening.py
python mycielski_strengthening/audit/independent_check.py
python unique_domination_pilot/extension/prior_work/check_prior_isomorphism.py
python unique_domination_pilot/extension/check_low_gamma.py
python unique_domination_pilot/extension/audit/independent_low_gamma.py
python unique_domination_pilot/extension/two_extra/check_two_extra.py
python unique_domination_pilot/extension/two_extra/audit/independent_two_extra.py
```

The optional numerical discovery scripts in the Mycielski folder require SciPy/NumPy and are labeled exploratory. They are not proof premises. `mycielski_profile.cpp` supplies the exact M2–M5 baseline; compile it with a C++17 compiler. `VERIFICATION.json` records fresh package-level replay, and `MANIFEST.json` records delivered file hashes. The broad project registry and historical research log are preserved unchanged; this directory's status and claim ledger govern these new results.

