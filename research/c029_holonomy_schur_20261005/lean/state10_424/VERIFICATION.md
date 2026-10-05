# R2 exact recurrence through state 10

PASS, 2026-10-05T13:17:47Z. Four successive bounded official-Lean compilation runs certify states 7–10, adding 48 theorems to the unchanged 376-declaration source checkpoint. The final aggregate audit checks exactly 424 unique expected declarations.

## Exact statements

For each j in 7, 8, 9, 10, the increment proves the inverse at state j−1, every X/R/W/G/H/C transition field at open index j−1, and closed rational/real actual-orbit equalities. The final statements are:

```lean
r2_tenth_actual_orbit : r2Orbit ℚ 10 = r2StepState10
r2_tenth_actual_real_orbit : r2Orbit ℝ 10 = r2RealState r2StepState10
```

No numerical identity remains a premise of these conclusions. Each stage checks 16 inverse-product entries and 68 transition entries using explicit denominator-cleared scalar identities. Couplings alternate EPlus at open indices 6 and 8, and EMinus at 7 and 9. The genuine matrix inverse follows from a right-inverse multiplication identity; rational-to-real transport reuses the earlier generic recurrence bridge.

## Resource evidence

| State reached | Compile wall, s | CPU user+system, s | Sampled peak RSS, GiB | Inverse numerator/denominator digits | Outgoing state numerator/denominator digits | Source bytes |
|---:|---:|---:|---:|---:|---:|---:|
| 7 | 149.806 | 94.921 | 4.829 | 25/26 | 27/27 | 154,102 |
| 8 | 118.914 | 78.666 | 4.780 | 56/56 | 58/57 | 204,105 |
| 9 | 129.244 | 86.381 | 4.826 | 32/32 | 34/33 | 186,829 |
| 10 | 126.652 | 83.235 | 4.822 | 71/72 | 73/73 | 250,500 |

Each compile had a hard 180-second wall limit and used the source's 300,000-heartbeat cap per statement. The controller would stop after a 150-second successful compile, as well as on any failed check, before starting another stage. No such stop occurred. The four stages ran sequentially. No extra numerical profiling rerun was performed. The final aggregate import/axiom audit took 78.659 seconds with a 120-second hard limit and exited 0.

Only the standard axiom union propext, Classical.choice, Quot.sound appears. All 12 new declaration names were uniquely matched at each stage, before advancing. The final 424-name audit also rejects missing/extra/duplicate names and unexpected axioms. It accepts both Lean's empty-axiom format and wrapped axiom lists, with tested rejection cases. No sorryAx, new axiom, native oracle, unsafe proof or kernel-skipping directive is used.

## Build and import integrity

Official Lean 4.33.1, commit 819816b2e0a3bf405af45ae5c7af2491d8f5bee6; Mathlib 0df444a360eaa60ab8c11dca51a86af692955474. Each run used the canonical full-artifact argument shape, source plus -o/-i/-c/--setup/--json, with -j 1 and fresh isolated outputs. It generated olean, ilean and C source, without native C object compilation or linking.

Each explicit compiler-input setup derives from the preceding verified setup: preserve options/package/module mode/plugins/dynlibs and all nonproject imports, redirect project paths to byte-identical complete overlay objects, and add the immediately preceding verified module. These are compiler inputs, never fabricated Lake success traces. Before advancing, source/setup/project-import hashes and fresh artifact timestamps/hashes were verified. Each stage's complete TargetA overlay preserves the previous artifacts and compiled sidecars. The final audit prints the resolved state 10 object path. The exact theorem sources, pinned project configuration, complete normalized audit output and selected compile evidence are included. The archived run metadata and its hashes are available in the separately frozen local archive.

The preceding default Lake normalization timeout remains disclosed. This successful isolated serial route does not establish its cause. This source snapshot preserves the 424 checkpoint. The archived run used absolute paths; the public log normalizes workspace paths and records the unmodified log hash. The incremental patch adds only the four modules and the new audit source; the original AllTheorems module is unchanged.

## Remaining obligations

The actual recurrence now reaches state 10. Before identifying the recorded S26 seed, there remain 30 finite assertions: 15 inverse identities, 14 six-field transitions and one terminal match, equivalent to 1,228 scalar equalities. Positive eliminated pivots, raw graph/block correspondence, contraction, response decay, infinite tails and all-length R2 positivity remain separate. No full S26 or R2-family claim follows from this prefix. This is the frozen state10 validation snapshot completed on 2026-10-05 at 13:17:47 UTC. Its recorded validation run ended at state10; later research is outside this snapshot. Depositing this snapshot in the repository does not extend its theorem scope.
