# Dependencies

## Mathematical dependency graph

```text
Q_i=tau_i tau_(i+1)
  -> lift recurrence tau_(i+1)=Q_i tau_i
  -> cyclic lift condition product Q_i=1
  -> even defect count
  -> total charge modulo eight.

positive-Q locations
  -> cyclic gaps
  -> four translated reference bulks B_s
  -> endpoint displacement g mod 4
  -> sector shift sigma_sec(q)=q mod 4
  -> additive composition law.
```

## Upstream mathematical input

- The reference `Q` phase has positive sites on one residue class modulo
  four.
- Quadrilateral flux is `Q_i=tau_i tau_(i+1)`.

No spectral theorem or interface matching result is used.

## Exact provenance

- Flux and lift convention:
  `research/paper/manuscript_tex_pub/sections/03_preliminaries.tex`.
- Charge conservation:
  `research/proofs/task51/TARGET_A_EXACT_CHARGE_AND_MOMENT_RESULTS.md`.
- Correct translation-sector law:
  `research/proofs/task52/TARGET_A_TRANSLATION_CHARGE_THEOREM.md`.
- Optional exact artifact:
  `research/proofs/task52/certificates/translation_charge.json`.

The theorem and proof in this package do not depend on research-task labels;
the paths above are an audit trail.

## Downstream use

- `q=0` identifies gap four with the reference bulk.
- `q=2` identifies G6 as a `B_0 -> B_2` phase slip.
- Additivity explains the one-, two-, and three-slip residue constructions.
