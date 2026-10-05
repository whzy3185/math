# C029 raw alpha-minus graph bridge: verified extension

**Status: PASS.** Completed 5 October 2026, 08:33:48 UTC.

This extension closes the raw-graph-to-antiperiodic-cell gap explicitly identified in the earlier 08:13 verification report. That earlier 165-theorem bundle is preserved unchanged as a checkpoint. The present bundle contains four extension modules, of which two are newly added here, and audits 196 theorem declarations in total.

## Final theorem

The checked declaration is:

```lean
theorem TargetA.period8_alpha_minus_main_theorem (L : ℕ) (hL : 0 < L) :
    ∀ i : Fin (8 * L),
      ((TargetA.period8_target_matrix_isHermitian L (-1)).eigenvalues i)^2
        < TargetA.period8Edge
```

Here `period8Edge = 4 + Real.sqrt (10 + 2 * Real.sqrt 5)`.

Thus every real Hermitian eigenvalue of the **raw, explicitly defined alpha-minus signed adjacency matrix** on `8L` vertices has squared modulus strictly below the exact continuous endpoint. The only assumptions are `L > 0` and the eigenvalue index. The conclusion includes `L=1` (eight vertices) and consequently every `L>=4` covered by the conjecture's stated range. There is no assumed Fourier decomposition, seam equivalence, nonzero-mode condition, or spectral bound in this final theorem.

The eigenvalue statement implies that the finite spectral radius is below `sqrt(period8Edge)`. The formal endpoint is expressed using Mathlib's Hermitian eigenvalue list rather than a separately defined graph spectral-radius object.

## The graph and the proved bridge

The pre-existing definitions are retained exactly:

- `period8TargetTau = ![1, 1, -1, 1, -1, -1, 1, -1]`
- Its period-eight lift supplies the step-two signs
- `period8TargetMatrix L alpha` is the symmetric sum of the forward step-one and step-two edge contributions and their reverses
- A forward edge crossing the cut is multiplied by `alpha`

Changing alpha from `+1` to `-1` therefore reverses the wrap edges `{8L-1,0}`, `{8L-2,0}`, and `{8L-1,1}`. The proof works directly with those original cut-coefficient definitions, including the eight-vertex case.

Set `low(i)=i` and `high(i)=8L+i` inside the periodic cover on `16L` vertices. The checked integer matrix identity is

```text
A_minus(L)[i,j]
  = A_plus(2L)[low(i),low(j)] - A_plus(2L)[low(i),high(j)].
```

The proof also verifies equal diagonal blocks and equal cross blocks. These identities give the explicit injective lift `J(u)=[u,-u]` and the exact operator intertwining

```text
A_plus(2L) J(u) = J(A_minus(L) u).
```

`J` is intentionally unnormalised; the proof uses injectivity for eigenvector transfer. It does not identify unequal-dimensional spaces by an unsupported unitary map.

Half-period raw translation sends `J(u)` to `-J(u)`. The existing raw-to-cell permutation is separately proved injective and exactly operator-intertwining; under it, the raw half-period shift becomes translation by `L` cells on `ZMod (2L)`. The previously verified antiperiodic-cell theorem then applies. Finally, the existing Hermitian eigenvector basis supplies every raw eigenvalue.

## Fresh checks

| Command from `formal/` | Completed UTC | Exit | Result |
|---|---|---:|---|
| `lake build TargetA.Period8DoubleCover` | 08:33:00 | 0 | Passed, 8,716 dependency/build jobs |
| `lake env lean RawBridgeAxiomAudit.lean` | 08:33:48 | 0 | All 196 theorem declarations audited |

The full axiom union is exactly `propext`, `Classical.choice`, and `Quot.sound`. No `sorryAx` or project-specific axiom appears. Source scans found no `sorry`, `admit`, axiom declaration, `unsafe`, `native_decide`, or kernel-skipping directive. Existing and new non-fatal style/unused-variable warnings are retained in the logs. Job counts are not theorem counts.

`Period8AntiperiodicBridge.lean` adds six theorems. `Period8DoubleCover.lean` adds 25, including the explicit index equivalence, lift, seam identities, operator transfer, and raw eigenvalue conclusion. Together with the prior 16-theorem increment, there are 47 new theorems beyond the frozen baseline.

## Reproduction and integrity

- Baseline: `whzy3185/math` at `7b6a351cc5f8f83f5527b7fc547f0a865ea50cf2`
- Lean: official 4.33.1, commit `819816b2e0a3bf405af45ae5c7af2491d8f5bee6`
- Official Linux release archive SHA-256: `890afd185370f85666025b883914ab4f4b339136f8c96167b69cfb62aecaf235`
- Mathlib: `0df444a360eaa60ab8c11dca51a86af692955474`
- All tracked baseline theorem sources, plus the earlier sharp-edge and antiperiodic-cell modules, remain byte-identical to their checked versions

Apply `c029_raw_bridge.patch` to the frozen baseline, or copy the files under this package's `formal/` into its `formal/`. If the earlier two modules are already installed, keep their identical bytes and add only the two new modules plus `RawBridgeAxiomAudit.lean`. Use the pinned Lean/dependencies and run the two commands above. The parent `AllTheorems.lean` need not be edited; the extension is built by its explicit module target.

The verification copy uses the official upstream Mathlib URL in place of the original SJTU mirror, with all dependency revisions unchanged. Its exact configuration files are in `reproduction/`. The earlier full frozen-baseline build is recorded in the preceding verification bundle. The logs here are fresh terminal output for this extension. `source_sha256.json` gives all current source/configuration hashes; `SHA256SUMS` covers this deliverable.

## Remaining scope limits

The raw matrix bridge and strict edge bound are now verified. This does not additionally formalize the exact finite-size radical formula for the attained radius, the integer n=32 certificate, the R2 tail argument, unrestricted minimization over all signings, or any literature-wide novelty claim. Those remain separate claims with their own analytic or computational evidence.
