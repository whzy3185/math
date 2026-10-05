# C029 named-constant alignment: final Lean verification checkpoint

**PASS**, completed 5 October 2026 at 09:20:25 UTC.

This checkpoint closes the remaining algebraic constant-identification gap in the preceding 237-theorem exact-radius report. All previous sources and checkpoint bundles remain unchanged. The new module adds nine theorems; the complete audit covers 246 theorem declarations.

## What is now proved

Define

```text
f(x) = x^4 - 2x^3 - 6x^2 + 12x - 4,
R = sqrt(4 + sqrt(10 + 2sqrt(5))).
```

`TargetA.period8_conjecture_constant_largest_real_root` proves

```text
f(R) = 0, and for every real x, f(x) = 0 implies x <= R.
```

This is a global largest-real-root characterization. It is not restricted to roots above a threshold, and no root property is assumed as a hypothesis.

`TargetA.period8_alpha_minus_eigenvalue_abs_lt_conjecture_constant` proves, for every natural `L>0` and every index `i : Fin (8L)`,

```text
abs(eigenvalue_i(period8TargetMatrixC L (-1))) < R.
```

The combined theorem `TargetA.period8_conjecture28_strict_family` states, explicitly for every `L>=4`, the largest-root characterization of `R` together with the strict inequality for every eigenvalue of that same raw alpha-minus matrix. The matrix definitions are the original period-eight Hamilton-gauge construction with the three cut-edge reversals.

The preceding exact finite-radius theorem remains available unchanged:

```text
R_L = sqrt(4 + sqrt(8 + 2cos(pi/L) + sqrt(26 - 6cos(pi/L)))).
```

For every `L>=1`, every eigenvalue modulus of the raw matrix is at most `R_L`, and an eigenvalue equals the positive number `R_L`. The eight-vertex endpoint is included.

## Constant-identification argument

The new proof verifies the polynomial identity

```text
p(x^2, 2) = f(x) f(-x).
```

The already proved endpoint identity gives `p(R^2,2)=0`. The inequality `R^2>=15/2` and `R>=0` give `f(-R)>0` by a direct polynomial inequality, so `f(R)=0`. For any real root `x` of `f`, the same factorization yields `p(x^2,2)=0`; the sharp scalar bound gives `x^2<=R^2`, hence `x<=R`. The strict raw spectral bound then transfers from squared eigenvalues to their absolute values.

## Fresh checks

| Command from `formal/` | Completed UTC | Exit | Result |
|---|---|---:|---|
| `lake build TargetA.Period8ConjectureConstant` | 09:19:13 | 0 | Passed, 8,722 dependency/build jobs |
| `lake env lean ConjectureConstantAxiomAudit.lean` | 09:20:25 | 0 | All 246 theorem declarations audited |

The exact axiom union is `propext`, `Classical.choice`, and `Quot.sound`. No `sorryAx`, project-specific axiom, or native-computation oracle appears. Source scans found no `sorry`, `admit`, axiom declaration, `unsafe`, `native_decide`, or kernel-skipping directive. Non-fatal style and unused-argument/tactic diagnostics remain visible in the logs. Build-job counts are not theorem counts.

The audited total comprises 149 baseline theorems and 97 extension theorems across ten modules. The constant-alignment module itself compiled without a new warning.

## Scope and interpretation

The formal chain now includes the raw graph-to-cell bridge, exact finite-radius formula with lower attainment, maximal antiperiodic phase, and the global largest-root definition of the algebraic constant. These are the mathematical ingredients of the explicit counterexample family.

The Lean theorem does not parse or formally import the arXiv text, and it does not introduce a universal formal type of all signings or an optimization statement over that type. The correspondence between the explicitly displayed matrix/constant and the paper's wording remains a transparent semantic comparison. There is no conclusion about the actual unrestricted minimum.

The n=32 integer principal-minor certificate, R2/R4/R6 Schur and tail arguments, finite-size asymptotic coefficient, and literature-wide novelty claims remain outside this Lean checkpoint. The finite-radius formula and its analytic provenance were already stated before this formalization; no new analytic-discovery claim is made here.

## Reproduction and integrity

- Baseline repository: `whzy3185/math` at `7b6a351cc5f8f83f5527b7fc547f0a865ea50cf2`
- Lean: official 4.33.1, commit `819816b2e0a3bf405af45ae5c7af2491d8f5bee6`
- Official Linux archive SHA-256: `890afd185370f85666025b883914ab4f4b339136f8c96167b69cfb62aecaf235`
- Mathlib: `0df444a360eaa60ab8c11dca51a86af692955474`; all other dependency revisions unchanged

Copy this bundle's `formal/` into the frozen baseline's `formal/`, or apply `c029_constant_alignment.patch`. From the 237 checkpoint, retain its nine identical modules and add `Period8ConjectureConstant.lean` and `ConjectureConstantAxiomAudit.lean`. Run the two commands above. The original root `AllTheorems.lean` remains unchanged; use the explicit extension target.

The exact verification configuration is under `reproduction/`; it changes only the original Mathlib mirror URL to the official upstream URL, preserving revisions. The logs are fresh execution output. `source_sha256.json` records all verified source/configuration hashes. `SHA256SUMS` covers the delivered files, and the patch is dry-run checked against the frozen baseline.
