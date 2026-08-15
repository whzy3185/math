# Target A: Complete n=24 Result

Date: 2026-08-15

Status: **VERIFIED_NO_COUNTEREXAMPLE_AT_N24**

## Mathematical conclusion

Conjecture 3 holds at `n=24`.  The exhaustive quotient search processed all
353,812 spectral states `(Q,alpha)` and found no signing with
`rho(A_sigma) < rho_-(24)`.

This is a finite, exact verification at `n=24`.  It does not establish that
the known `n=32` counterexample is minimal because `n=26,28,30` remain
unchecked.

## Search space

The production driver used only
`target_a_bracelets.enumerate_direct_q_orbits`.  Before constructing any
matrix it independently recomputed the fixed-weight Burnside targets and
streamed the complete generator once to enforce the following gate:

| quantity | expected | completed |
|:---|---:|---:|
| Q-bracelets | 176,906 | 176,906 |
| `(Q,alpha)` spectral states | 353,812 | 353,812 |
| represented Q-vectors | 8,388,608 | 8,388,608 |
| represented switching classes | 33,554,432 | 33,554,432 |

Every shell also completed at exactly twice its Q-bracelet target after the
two alpha values were included:

```text
d=0:1, 2:12, 4:256, 6:2920, 8:15581, 10:41272, 12:56822,
  14:41272, 16:15581, 18:2920, 20:256, 22:12, 24:1
```

Every streamed state passed the exact reconstruction check
`(Q_reconstructed,alpha_reconstructed)=(Q,alpha)`.

## Exact decision

The certified rational isolating interval for `rho_-(24)^2` was

```text
73849452861677/9636011581006
< rho_-(24)^2 <
77065035293260/10055586653667 = U_24.
```

The state `d=0`, Q-code `0`, `alpha=-1` was treated separately.  Exact
minimal-polynomial divisibility and root isolation confirmed that the largest
root of its `A^2` characteristic polynomial equals `rho_-(24)^2`, with
multiplicity 4.

For each of the other 353,811 states, one floating symmetric
eigendecomposition proposed an integer vector `v`.  Exact integer arithmetic
then proved

```text
rho(A)^2 >= ||Av||^2/||v||^2 >= U_24 > rho_-(24)^2.
```

All 353,811 non-optimizer states were `RAYLEIGH_CERTIFIED`; exact fallbacks
were 0 and counterexamples were 0.  Floating values made no PASS/FAIL
decision.

## Near-minimizer observation

The numerically lowest non-optimizer in the retained top-100 queue was

```text
canonical Q-code: 1118481
defect count:      6
defect positions:  0,4,8,12,16,20
alpha:             -1
dihedral orbit:    4
numeric rho:       2.7774581947752623
numeric gap:       0.009082775843246349
Rayleigh bound:    1285712336688441453/166666666589027047
trace(A^4,A^6,A^8): 576, 3840, 26784
```

The top-100 ordering is **OBSERVED_NUMERIC_ORDER_ONLY**.  No exact claim is
made that this is the exact second minimum or the exact first 100.

## Checkpoint and provenance

The run wrote 28 immutable chunks with atomic temporary-file replacement.
Resume validation re-generated all completed inputs and reproduced the final
cursor, input digest, certificate digest, and chain without spectral work.

```text
baseline git commit:
  9058177fd158ffbecf82798e247f3e0510243973
generator source SHA-256:
  2a972d97c1c72e2f12140336c3328362de531507b5931c0f4b442beb7ac1f5d7
search script SHA-256:
  4e9c39e4eda4f0fc479ae32f6ec0c8438781520d0dab2c7a603ee01f7f55936c
ordered input SHA-256:
  dfa6610b99a23f077dfa63fc49135cd79ddb038b206dc21f15f925e9aa2a06e2
ordered certificate SHA-256:
  994d2bf09913841c868db0d54f7ae912fe0c5925a5d35cb1a945e3e8101707e9
final checkpoint chain SHA-256:
  2dde869aea5da4f040e67a4fef3e93b5f35f5fb42d75f6d48820439f418c83c1
checkpoint manifest SHA-256:
  978b38db75ccf8d05bd7bae76b28373d5a0b56655299ea2a65cc25722514a98b
result JSON SHA-256:
  3fea700914b3c2d8a08a26bbaf490432123ed1a877c231f0d53ddbdf8f394a51
```

Command:

```text
PYTHONPATH=/Users/muelsyse/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/lib/python3.12/site-packages \
.venv/bin/python research/scripts/target_a_minimality_search.py \
  --n 24 --chunk-size 20000 \
  --checkpoint-dir research/logs/checkpoints/n24 \
  --output research/logs/target_a_search_n24.json
```

Environment: Python 3.12.13, NumPy 2.3.5, SymPy 1.14.0,
macOS 26.5.2 arm64.  Wall time was 21.16 seconds and peak RSS was
79,593,472 bytes.  The complete machine-readable result is
`research/logs/target_a_search_n24.json`.

## Next gate

Task 34 is the complete `n=26` exhaustive spectral search.  No `n=26,28,30`
search was started in Task 33B.
