# C029 exact finite antiperiodic radius: Lean verification

**PASS**, completed 5 October 2026 at 09:12:30 UTC.

This increment formally verifies the already stated analytic finite-radius formula. It is a formal-verification contribution, not a claim of a newly discovered analytic formula or literature-wide novelty. The earlier 165- and 196-theorem bundles are preserved unchanged.

## Exact result

For every natural `L > 0`, define

```text
R_L = sqrt(4 + sqrt(8 + 2 cos(pi/L) + sqrt(26 - 6 cos(pi/L)))).
```

For the original raw Hamilton-gauge matrix `period8TargetMatrixC L (-1)` on `8L` vertices, the checked theorem `TargetA.period8_alpha_minus_exact_finite_radius` proves both:

1. Every Hermitian eigenvalue has absolute value at most `R_L`
2. An eigenvalue has absolute value exactly `R_L`

The stronger attainment lemma `period8_alpha_minus_finite_radius_attained_index` finds an eigenvalue equal to the positive number `R_L` itself. The theorem `period8_finite_radius_radical` verifies the displayed expanded radical exactly. These results give the finite spectral radius through its maximum-eigenvalue-modulus characterization; no finite-radius equality is assumed.

The statement includes `L=1` (eight vertices), where the phase parameter is `-2`. Positivity is proved on the closed interval `-2 <= c <= 2`; neither that endpoint nor odd `L` is omitted.

The matrix definitions and the three wrap-edge reversals are the same as in the preceding raw-graph bridge report. All original baseline sources and all four previous extension modules remain byte-identical.

## Proof chain

- **Scalar root (10 theorems):** rewrite the quartic as `((y-4)^2-(8+c))^2-(26-3c)`. Prove that `4+sqrt(8+c+sqrt(26-3c))` is an actual root on the phase interval, bounds every real root, and is strictly increasing there
- **Fiber attainment (7):** prove the actual characteristic determinant of the 4-by-4 squared chiral block. A zero determinant supplies a nonzero eigenvector; an explicit chiral lift and the invertible chiral basis turn it into a fiber eigenvector. Prove the exact pointwise upper bound and attainment at its positive square root
- **Maximal phase (5):** bound the real part of every nonzero phase of the doubled cycle by `cos(pi/L)`. Every antiperiodic mode is nonzero, and the first phase both attains the bound and satisfies `z^L=-1`
- **Reverse Bloch transfer (10):** prove the inverse raw-to-cell permutation, recover the explicit `[u,-u]` range, and construct an actual raw alpha-minus eigenvector from the first allowed fiber mode
- **Finite assembly (9):** combine upper bound and attainment, locate the attained eigenvalue in the complete Hermitian eigenvalue list, and prove the expanded radical formula

These are 41 new theorems beyond the 196-theorem checkpoint. The full audit covers 237 theorem declarations: 149 from the frozen baseline and 88 across the nine extension modules.

## Fresh execution and axiom audit

| Command from `formal/` | Completion UTC | Exit | Result |
|---|---|---:|---|
| `lake build TargetA.Period8ExactFiniteRadius` | 09:11:46 | 0 | Passed, 8,721 dependency/build jobs |
| `lake env lean ExactRadiusAxiomAudit.lean` | 09:12:30 | 0 | All 237 theorem declarations audited |

The axiom union is exactly `propext`, `Classical.choice`, and `Quot.sound`. No `sorryAx`, project-specific axiom, or native-computation oracle appears. Source scans found no `sorry`, `admit`, axiom declaration, `unsafe`, `native_decide`, or kernel-skipping directive. Non-fatal style and unused-variable/tactic warnings remain visible in the logs. The job count includes dependency targets and is not a theorem count.

## Reproduction

- Baseline: `whzy3185/math` at `7b6a351cc5f8f83f5527b7fc547f0a865ea50cf2`
- Lean: official 4.33.1, commit `819816b2e0a3bf405af45ae5c7af2491d8f5bee6`
- Official Linux release archive SHA-256: `890afd185370f85666025b883914ab4f4b339136f8c96167b69cfb62aecaf235`
- Mathlib: `0df444a360eaa60ab8c11dca51a86af692955474`, with all other dependency revisions unchanged

Copy this package's `formal/` into the frozen baseline's `formal/`, or apply `c029_exact_radius.patch` at its root. When continuing from the 196 checkpoint, retain the four identical previous extension modules and add the five new modules and `ExactRadiusAxiomAudit.lean`. Run the two commands in the table. The root `AllTheorems.lean` is intentionally unchanged; build the explicit extension target.

The `reproduction/` configuration files replace only the original SJTU Mathlib mirror URL with the official upstream URL, preserving every revision. The official Mathlib cache was restored before local compilation. `source_sha256.json` records all verified source/configuration bytes; `SHA256SUMS` covers every delivered file except itself. The patch was dry-run checked against the frozen baseline.

## Remaining boundaries

The raw graph bridge, pointwise fiber radius, maximal antiperiodic phase, lower attainment, and complete finite-radius formula are now formalized. This bundle does not yet formalize identification of the continuous endpoint with the largest real root of the separate quartic used to name the constant in Conjecture 28. That identification is covered by the analytic argument. The n=32 integer principal-minor certificate, R2 tail argument, finite-size asymptotic coefficient, and unrestricted minimization over all signings remain separate claims. No claim about literature-wide novelty follows from the Lean checks.
