# Auxiliary Periodic Counterexample Families

The following five periodic signed families have exact Floquet certificates.
For every allowed finite Bloch phase, their squared spectrum lies strictly
below the listed rational cap.

| period | valid orders | cap on `rho(A)^2` | proof mechanism |
|---:|---|---:|---|
| 10 | `10 divides n`, `n>=50` | `198/25` | concavity in `c=z+z^-1`; both endpoint shifts have positive coefficients |
| 12 | `12 divides n`, `n>=60` | `143/18` | convexity in `c`, vertex strictly to the right of 2, and positive `c=2` shift |
| 14 | `14 divides n`, `n>=112` | `399/50` | concavity in `c`; both endpoint shifts have positive coefficients |
| 18 | `18 divides n`, `n>=54` | `5782/729` | concavity in `c`; both endpoint shifts have positive coefficients |
| 22 | `22 divides n`, `n>=66` | `8662/1089` | concavity in `c`; both endpoint shifts have positive coefficients |

For each row, the cap is at most `8-200/n_0^2` at its stated initial order
`n_0`, while the twisted benchmark is strictly larger than that elementary
lower bound and increases with `n`. Thus each is a genuine analytic
counterexample family, not a finite spectral scan.

## Consequence for the old finite bridge

Together with the period-eight family and the residue-specific IMS ranges,
the analytic families now cover 71 of the old 96 rows between 48 and 238. The
remaining finite orders are exactly

```text
52, 58, 62, 68, 74, 76, 78, 82, 86, 92, 94, 102, 116,
118, 124, 134, 142, 148, 158, 164, 166, 174, 206, 214, 222.
```

The number 25 is a current accounting statement, not a claim that these
orders are inherently exceptional. The uniform Riccati program still aims to
remove them all.

## Role boundary and stop rule

These are auxiliary analytic families. They may shorten a future finite
bridge and reveal features of the spectral landscape, but they do not form
the main proof architecture: divisibility by finitely many periods cannot
establish a full residue-class theorem.

No additional low-period family is to be sought for bridge coverage unless it
directly supplies a lemma for the fixed-energy residue-two, residue-four, or
residue-six Riccati theorem. The active analytic task resumes with the
`K`-symmetry reduction for residue two and the all-length Schur/Riccati
positivity certificate.

Exact symbolic verification is in
`research/scripts/verify_target_a_periodic_counterexample_families.py`.
