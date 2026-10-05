# C029 Lean verification, 5 October 2026

## Result

**PASS for the precise statements below.** Fresh checks completed at 08:13:01 UTC. The new sources contain 16 theorems (11 sharp-edge and 5 antiperiodic-cell theorems). All 165 theorem/lemma declarations in the baseline plus the extension were inspected with `#print axioms`.

| Command, run from `formal/` | Completed UTC | Exit | Result |
|---|---|---:|---|
| `lake build TargetA.AllTheorems` | 08:10:04 | 0 | Baseline passed, 8,716 jobs |
| `lake build TargetA.Period8SharpEdge` | 08:10:52 | 0 | Sharp edge passed, 8,707 jobs |
| `lake build TargetA.Period8AntiperiodicCells` | 08:11:39 | 0 | Antiperiodic cells passed, 8,714 jobs |
| `lake env lean AxiomAudit.lean` | 08:12:22 | 0 | Eight key results audited and final statement printed |
| `lake env lean AllAxiomAudit.lean` | 08:13:01 | 0 | All 165 theorem declarations audited |

The axiom union is exactly `propext`, `Classical.choice`, and `Quot.sound`. There is no `sorryAx` or project-specific axiom. One theorem uses no axioms. Source scans also found no `sorry`, `admit`, axiom declarations, `unsafe`, `native_decide`, or kernel-skipping directives. Existing style/linter warnings and informational tactic suggestions are present; every check exited successfully. Job counts include imported dependency targets, not newly proved theorem counts.

## Exact verified scope

Write

- `p(y,c) = y^4 - 16y^3 + (80-2c)y^2 + (-128+16c)y + c^2 - 13c + 38`
- `E = 4 + sqrt(10 + 2 sqrt(5))`, the squared continuous endpoint (`period8Edge`)

The new scalar results prove:

1. If `c <= 2` and `p(y,c) = 0`, then `y <= E`
2. If `c < 2` and `p(y,c) = 0`, then `y < E`
3. For `c <= 2`, `p(E,c) = 0` if and only if `c = 2`

These scalar statements quantify over real `y,c` and need no additional nonnegativity assumption on `y`.

The antiperiodic phase result proves that if `L != 0`, `xi^2 = z`, and `z^L = -1`, then `Re(xi^2 + xi^(-2)) < 2`. Every real eigenvalue `lambda` of the corresponding explicitly defined eight-dimensional fiber, with a nonzero eigenvector, consequently satisfies `lambda^2 < E`.

The final theorem is `TargetA.period8_antiperiodic_cell_eigen_square_lt_edge`. Its assumptions are precisely:

- Natural numbers `N,L` with `[NeZero N]` and `L != 0`
- A nonzero state `F : ZMod N -> Fin 8 -> Complex`
- Antiperiodicity `period8CellTranslation (L : ZMod N) F = -F`
- A real `lambda` satisfying `period8CellAction F = (lambda : Complex) * F` (pointwise scalar multiplication)

Its conclusion is `lambda^2 < period8Edge`. The cell action is the already defined block operator with intra-cell, forward-cell and backward-cell matrices, and the proof uses its finite DFT decomposition.

The unchanged baseline theorem `TargetA.period8_alpha_plus_main_theorem` was also rebuilt and audited. For `L >= 4` it bounds every Hermitian eigenvalue of the explicit alpha-plus graph witness in squared modulus by
`4 + 2 cos(pi/(4L)) + 2 cos(pi/(2L))`.

## Explicit boundary

This extension does **not** prove the seam/reindexing bridge from the raw alpha-minus signed graph adjacency matrix to the finite antiperiodic cell sector. Therefore these Lean checks are not a complete formal proof of the raw-graph antiperiodic counterexample, the exact finite-size radical spectral-radius formula, the n=32 integer certificate, the R2 analytic tail proof, or an unrestricted spectral minimum. Those mathematical claims require their separate analytic/computational evidence. No claim of literature-wide novelty follows from these checks.

## Provenance and reproduction

- Baseline: `whzy3185/math`, `analytic-proof-first` frozen at `7b6a351cc5f8f83f5527b7fc547f0a865ea50cf2`
- Lean: official 4.33.1, commit `819816b2e0a3bf405af45ae5c7af2491d8f5bee6`
- Official release: <https://github.com/leanprover/lean4/releases/tag/v4.33.1>
- Linux release archive SHA-256: `890afd185370f85666025b883914ab4f4b339136f8c96167b69cfb62aecaf235`, verified against the official release metadata and downloaded bytes
- Mathlib: `0df444a360eaa60ab8c11dca51a86af692955474`; all other dependency revisions unchanged
- All 8,690 official Mathlib cache entries were restored successfully before compiling the project sources
- Every tracked baseline Lean theorem file was verified byte-identical to the frozen commit

The only verification-copy configuration edit replaces the SJTU Mathlib mirror URL with `https://github.com/leanprover-community/mathlib4` in `lakefile.lean` and `lake-manifest.json`. It does not change any revision. The exact verification configurations are in `reproduction/`; they need not replace the repository configuration if the mirror is available.

Copy the four files under this package's `formal/` into the baseline's `formal/`, or apply `c029_lean_increment.patch` at the repository root. Use Lean 4.33.1 and the pinned dependencies. From `formal/`, restore the cache with `lake exe cache get`, then run the five commands in the table. Set `MATHLIB_CACHE_DIR` to a writable directory if the default cache directory is unavailable. No change to the baseline `AllTheorems.lean` imports is needed because the new module is built explicitly.

The five logs are fresh terminal output, not reconstructed historical evidence. `verification_summary.json` records timings and theorem names. `source_sha256.json` records all verified project-source/configuration hashes; `SHA256SUMS` covers every file delivered in this bundle except itself.
