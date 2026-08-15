# Target A: Complete n=26 Result

Date: 2026-08-15

Status: **VERIFIED_NO_COUNTEREXAMPLE_AT_N26**

## Mathematical conclusion

Conjecture 3 holds at `n=26`.  The exhaustive quotient search processed all
1,299,064 spectral states `(Q,alpha)` and found no signing with
`rho(A_sigma) < rho_-(26)`.

Together with the previous finite checks, the conjecture is now strictly
verified for every even `n=8,10,...,26`.  This does not establish that the
known `n=32` counterexample is minimal because `n=28,30` remain unchecked.

## Search space

The production driver used only the audited constant-memory
`target_a_bracelets.enumerate_direct_q_orbits` stream.  Before spectral work,
an independent fixed-weight Burnside pass enforced:

| quantity | expected | completed |
|:---|---:|---:|
| Q-bracelets | 649,532 | 649,532 |
| `(Q,alpha)` spectral states | 1,299,064 | 1,299,064 |
| represented Q-vectors | 33,554,432 | 33,554,432 |
| represented switching classes | 134,217,728 | 134,217,728 |

The completed Q-bracelet shells exactly matched:

```text
d=0:1, 2:13, 4:328, 6:4576, 8:30415, 10:102817, 12:186616,
  14:186616, 16:102817, 18:30415, 20:4576, 22:328, 24:13, 26:1
```

Every streamed state passed the exact reconstruction check
`(Q_reconstructed,alpha_reconstructed)=(Q,alpha)`.

## Exact decision

The certified rational interval used for the threshold was

```text
28526207898435/3698556147368
< rho_-(26)^2 <
26903365670087/3488147069469 = U_26.
```

For the optimizer `d=0`, Q-code `0`, `alpha=-1`, exact minimal-polynomial
divisibility and root isolation confirmed that the largest root of the
`A^2` characteristic polynomial equals `rho_-(26)^2`, with multiplicity 4.

For each of the other 1,299,063 states, a floating symmetric
eigendecomposition only proposed an integer vector `v`.  Exact integer
arithmetic then proved

```text
rho(A)^2 >= ||Av||^2/||v||^2 >= U_26 > rho_-(26)^2.
```

All 1,299,063 non-optimizer states were `RAYLEIGH_CERTIFIED`; exact fallbacks
were 0 and counterexamples were 0.  Floating values made no mathematical
PASS/FAIL decision.

## Period-4 diagnostic

For diagnostics only, each numeric top-100 state records the minimum Hamming
distance from Q to the truncated pattern `(+,-,-,-,...)`, minimized over
cyclic rotations and reflections.  This field did not affect enumeration,
ranking, or exact decisions.

The numerically lowest non-optimizer was

```text
canonical Q-code: 1118481
defect count:      6
defect positions:  0,4,8,12,16,20
cyclic gaps:       4,4,4,4,4,6
alpha:             +1
dihedral orbit:    26
distance to period-4 Q pattern: 1
numeric rho:       2.809699881345048
numeric gap:       0.03250783070135421
Rayleigh bound:    7894413426004722080/1000000000351431941
trace(A^4,A^6,A^8): 616, 4076, 28392
```

Thus the lowest observed state is a one-bit finite-size deviation from the
period-4 Q structure seen at `n=24` and in the known period-8 tau family.
The top-100 ordering and this structural interpretation are
**OBSERVED_NUMERIC_ORDER_ONLY**; no exact second-minimum claim is made.

## Regression and checkpoints

The diagnostic/provenance extension did not change the search or exact
decision algorithms.  Before the `n=26` run:

- full production searches at `n=8,10,12` reproduced the reference bracelet
  counts, exact optimizer checks, zero fallbacks, and zero counterexamples;
- a read-only replay of all 28 committed `n=24` chunks reproduced the complete
  generator cursor, 353,812-state input digest, certificate digest, final
  chain, optimizer record, and zero-counterexample result.

The `n=26` run wrote 76 immutable chunks.  A subsequent read-only resume
replay regenerated the complete input cursor and reproduced every aggregate
digest and the final chain.

```text
baseline git commit:
  35df4857f55f47a616049c33381a3e62b79d06be
generator source SHA-256:
  2a972d97c1c72e2f12140336c3328362de531507b5931c0f4b442beb7ac1f5d7
search script SHA-256:
  7a211049e8fa541cbb594389caaff79d1597f942e43dc20ee37b382979ed93e1
ordered input SHA-256:
  079e8230fcba59bd090dba07af2ed754f7f3116ac6acfd2b789b405d010d2f66
ordered certificate SHA-256:
  9780c3030bb1dfdc1562162e11117b6ebb50de97fa43cc1c6b7c6dea58c73669
final checkpoint chain SHA-256:
  c515350b8bea840c04448086fbc98523615364c05ca837553c93efb933bc0c4e
checkpoint manifest SHA-256:
  59d106f91ff5bd457e25c1676233970ee46382e4ace7c8e41b7769b85d5b140d
result JSON SHA-256:
  9cb022a9bc7ba5e2ad7d8d1d0427ec3073a64aae60a09ef032f0a2286875f815
```

Command:

```text
PYTHONPATH=/Users/muelsyse/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/lib/python3.12/site-packages \
.venv/bin/python research/scripts/target_a_minimality_search.py \
  --n 26 --chunk-size 20000 \
  --checkpoint-dir research/logs/checkpoints/n26 \
  --output research/logs/target_a_search_n26.json
```

Environment: Python 3.12.13, NumPy 2.3.5, SymPy 1.14.0,
macOS 26.5.2 arm64.  Wall time was 92.94 seconds and peak RSS was
92,471,296 bytes.

## Next gate

Task 35 is the complete `n=28` exhaustive spectral search.  No `n=28` or
`n=30` search was started in Task 34.
