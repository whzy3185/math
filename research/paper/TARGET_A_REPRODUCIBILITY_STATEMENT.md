# Target A Reproducibility Statement

Status: **TARGET_A_REPRODUCIBILITY_STATEMENT_COMPLETE**

The finite minimality computation was independently regenerated from the
frozen commit `c5cadf3ec7e160fc994453907fe83c579dc89646` in an isolated detached
worktree. Fresh searches completed:

| n | Canonical spectral states | Chunks |
|---:|---:|---:|
| 24 | 353,812 | 28 |
| 26 | 1,299,064 | 76 |
| 28 | 4,810,472 | 250 |
| 30 | 17,929,600 | 908 |

The total is 1,262 fresh chunks. All expected and observed bracelet, shell,
state, represented-vector, and represented-switching-class counts agree.
Final checkpoint chains and ordered input/certificate hashes agree with the
committed evidence. Exact fallbacks and counterexamples are both zero;
reproduction mismatch count is zero.

At `n=30`, the 17,929,600 canonical `(Q,alpha)` spectral states represent
2,147,483,648 switching classes by the proved switching/flux/dihedral quotient
and two retained holonomy values. This does not mean that 2.147 billion
independent pytest cases were executed.

The committed checkpoint integrity replay passed every recorded cursor,
count, and hash-chain check for `n=24,26,28,30`. It does not recompute
per-state Rayleigh vectors and is not described as an independent mathematical
certificate replay. The fresh full regeneration is the mathematical rerun.
The three generator/Burnside audits skipped by the default suite were
separately enabled and passed. The historical and paper-rendered statuses are:

```text
FULL_FINITE_SEARCH_REGENERATION_PASS
FULL_CERTIFICATE_REPLAY_PASS
FULL_CHECKPOINT_INTEGRITY_REPLAY_PASS
FULL_SLOW_REGRESSION_PASS
```

Commands, environments, timings, memory peaks, result hashes, manifest hashes,
chain hashes, and operational incidents are preserved in
`research/reproducibility/target_a_full_slow_reproduction_summary.json`.
The original production checkpoint chunks are committed to Git. The separate
fresh-regeneration chunks and full runtime logs remain external; only their
compact manifests and hashes are committed.
