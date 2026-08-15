# Target A: Complete n=30 Result

Date: 2026-08-15

Status: **FINITE_RANGE_COMPLETE_THROUGH_N30**

## Mathematical conclusion

Conjecture 3 holds at `n=30`. The exhaustive quotient search processed all
17,929,600 spectral states `(Q,alpha)` and found no signing with
`rho(A_sigma) < rho_-(30)`.

The conjecture is now strictly verified for every even `n=8,10,...,30`.
Together with the existing exact `n=32` witness, the computational ingredients
for a smallest-counterexample result are present, but this task does not
assemble or claim that certificate. That is the separate Task 36A gate.

## Search-space closure

The production driver used the audited constant-memory direct bracelet stream.
Before spectral work, an independent fixed-weight Burnside pass enforced:

| quantity | expected | completed |
|:---|---:|---:|
| Q-bracelets | 8,964,800 | 8,964,800 |
| `(Q,alpha)` spectral states | 17,929,600 | 17,929,600 |
| represented Q-vectors | 536,870,912 | 536,870,912 |
| represented switching classes | 2,147,483,648 | 2,147,483,648 |

The completed Q-bracelet shells exactly matched:

```text
d=0:1, 2:15, 4:511, 6:10133, 8:98254, 10:502303,
  12:1444147, 14:2427036, 16:2427036, 18:1444147,
  20:502303, 22:98254, 24:10133, 26:511, 28:15, 30:1
```

Every state passed exact `(Q,alpha)` reconstruction.

## Exact decision

The certified rational threshold interval was

```text
57389579899591/7373343560082
< rho_-(30)^2 <
46620424917345/5989735600679 = U_30.
```

For the optimizer `d=0`, Q-code `0`, `alpha=-1`, exact minimal-polynomial
divisibility and largest-root isolation confirmed
`rho(A)^2=rho_-(30)^2`, with multiplicity 4.

For each of the other 17,929,599 states, a floating symmetric
eigendecomposition only proposed an integer vector `v`. Exact arithmetic then
proved

```text
rho(A)^2 >= ||Av||^2/||v||^2 >= U_30 > rho_-(30)^2.
```

All 17,929,599 non-optimizer states were `RAYLEIGH_CERTIFIED`; exact fallbacks
were 0 and counterexamples were 0. Floating values made no mathematical
PASS/FAIL decision.

## Period-4 diagnostics

The reference is the exact length-30 truncation of `(+,-,-,-,...)`, beginning
at index 0. Its defect count is 8, so every admissible Q-vector must have even
dihedral Hamming distance from it. The production run checked that parity on
the full stream and observed distances `0,2,...,22` only.

The numerically lowest non-optimizer was

```text
canonical Q-code: 17843217
defect count:      6
defect positions:  0,4,10,14,20,24
cyclic gaps:       4,6,4,6,4,6
alpha:             +1
dihedral orbit:    10
distance to period-4 Q pattern: 6
numeric rho:       2.808701937599131
numeric gap:       0.01882987659833768
Rayleigh bound:    1577761314313743796/199999999931437297
trace(A^4,A^6,A^8): 696, 4548, 31608
```

Distance 0 is admissible at `n=30`; its best observed state was Q-code
`71582789`, `d=8`, `alpha=+1`, with numeric gap `0.05226293955131567`.
Thus period-4 distance alone does not order the near minimizers.

All ordering and structural statements in this section are
**OBSERVED_NUMERIC_DIAGNOSTIC**, not exact extremal theorems.

## n=24/26/28/30 observed table

The table was generated directly from the saved result logs by
`research/scripts/target_a_period4_diagnostic.py`.

| n | best observed Q-code | distance | numeric gap |
|---:|---:|---:|---:|
| 24 | 1,118,481 | 0 | 0.009082775843246349 |
| 26 | 1,118,481 | 1 | 0.03250783070135421 |
| 28 | 4,460,817 | 5 | 0.026312737092294647 |
| 30 | 17,843,217 | 6 | 0.01882987659833768 |

This records finite-size parity and commensurability behavior only. It does
not support a monotonicity or general-family theorem.

## Checkpoints and provenance

Before the search, default and focused tests passed and the committed
`n=24,26,28` evidence chains were replayed read-only. After the search, the
reusable replay tool independently checked all 908 immutable `n=30` chunks and
reproduced the shell counts, direct-stream terminal cursor, represented-space
counts, input digest, certificate digest, optimizer record, zero-fallback and
zero-counterexample counts, and final hash chain.

```text
baseline git commit:
  dce3da9a875c40f969352870c7e3b61f281c900e
generator source SHA-256:
  2a972d97c1c72e2f12140336c3328362de531507b5931c0f4b442beb7ac1f5d7
search script SHA-256:
  5653c6d6b086ba00d70a3ab7d6692445334f4f0009d4400274959f74a53fd6fc
checkpoint replay script SHA-256:
  462958ba80e121f42b8e0c58e071cff8d7ec993f7177982f58a9a2b0eb1fef4b
ordered input SHA-256:
  377d4a4747bbab72436c3620d2e0f035dc4e63e5f99eef6e0b67968f197d6f8d
ordered certificate SHA-256:
  87cda7ab65d68c2141174cc7643bbf4f7ecf42e359d7240026e85f35a9e15dde
final checkpoint chain SHA-256:
  b7fd264eece645eead187424152ae810a9ff940e37ffc5649b5ddf65aa31d59d
checkpoint manifest SHA-256:
  56b0cc2c8d12da9d99ca49d66d136d7b40a517cb4211f8fed5eb7b69c83ec7d4
result JSON SHA-256:
  34bbeba4b07723eff94eb8cc7b19f640ea2c07674e72cb5b91b3c74ba1a0b449
structural diagnostic JSON SHA-256:
  1d5975b4649759c3ae979d188bceeb27af15d4088520f85fc4fa5efce37a8e3b
```

Command:

```text
PYTHONPATH=/Users/muelsyse/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/lib/python3.12/site-packages \
.venv/bin/python research/scripts/target_a_minimality_search.py \
  --n 30 --chunk-size 20000 \
  --checkpoint-dir research/logs/checkpoints/n30 \
  --output research/logs/target_a_search_n30.json
```

Environment: Python 3.12.13, NumPy 2.3.5, SymPy 1.14.0,
macOS 26.5.2 arm64. Wall time was 1,498.36 seconds and peak RSS was
122,224,640 bytes.

## Next gate

Task 36A assembles and independently audits the smallest-counterexample
certificate from the complete even range `8<=n<=30` and the existing exact
`n=32` witness. It performs no new spectral search.
