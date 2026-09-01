# Lean Build Status

## Current status

`FORMALIZATION_OPEN`, with a verified foundational project.

On 2026-09-01, Lean was installed through the SJTUG mirror route: `glean` verified its Darwin ARM64 archive checksum, installed `elan v4.2.4`, and then installed `leanprover/lean4:v4.33.1`. `lake --version` reports Lake 5.0.0 for Lean 4.33.1. Mathlib `v4.33.1` and its pinned dependencies were obtained from the SJTUG Git mirror where available; Lake's package cache then completed.

The pinned `formal/` project now contains `TargetA.Definitions` and `TargetA.PhaseSlip`, proving residue-zero divisibility/evenness/admissibility and the one-gap sector congruence without any axiom, `sorry`, or `admit`. A bare `lake build` and `lake build TargetA.AllTheorems` both passed. The complete classification remains unformalized because its equality and nonzero-residue analytic mechanisms are not yet stable.

## Hard gate when the toolchain is available

1. Create a pinned Lean 4/mathlib project under `formal/`.
2. Add declarations in the order listed in `LEAN_THEOREM_MAP.md`.
3. Run `lake build`.
4. Reject any `sorry`, `admit`, or custom axiom encoding a target conclusion.
5. Mark a theorem `LEAN_PROVED` only after the build succeeds.

Current audited count under `formal/TargetA`: `lake build = PASS`, `sorry = 0`, `admit = 0`, and `custom axioms = 0`. `completeClassification` remains `FORMALIZATION_OPEN` rather than being represented by a placeholder axiom.
