# Direct Bracelet Generator Audit

Date: 2026-08-15

Status: **PASS**

## Scope

This audit validates the production Q-bracelet stream required before the
Target A minimality searches at `n=24,26,28,30`.  It performs no signed
adjacency construction, eigendecomposition, Rayleigh certification, or other
spectral search.

The reference implementation scans all `2^n` Q-codes and stores a
`bytearray(2^n)` visited table.  The production implementation is
`target_a_bracelets.enumerate_direct_q_orbits`.  It uses fixed-weight
Fredricksen-Kessler-Maiorana necklace recursion, keeps the smaller orientation
under reflection, and emits only even-weight binary bracelets.  The recursion
array and bit operations use `O(n)` working memory; no output list or
exponential visited table is retained.

For a necklace of minimal period `p`, reflection equivalence gives bracelet
orbit size `p`; otherwise the reflected pair gives orbit size `2p`.  Shells
are emitted in increasing even defect count and canonical codes are strictly
increasing within each shell.

## Exact reference comparison

For every even `n=8,10,...,22`, the complete ordered production stream was
compared with the old visited-array generator.  Equality includes defect
count, canonical Q-code, and dihedral orbit size, not merely aggregate counts.

| n | Q-bracelets | represented Q-vectors | result |
|---:|---:|---:|:---|
| 8 | 18 | 128 | PASS |
| 10 | 44 | 512 | PASS |
| 12 | 122 | 2,048 | PASS |
| 14 | 362 | 8,192 | PASS |
| 16 | 1,162 | 32,768 | PASS |
| 18 | 3,914 | 131,072 | PASS |
| 20 | 13,648 | 524,288 | PASS |
| 22 | 48,734 | 2,097,152 | PASS |

For each row, the ordered SHA-256 digest of the old and new records is
identical, all fixed-weight Burnside counts match, and the sum of orbit sizes
is exactly `2^(n-1)`.

## Production-scale Burnside audit

| n | Q-bracelets | spectral states | switching classes represented | peak traced memory | elapsed | result |
|---:|---:|---:|---:|---:|---:|:---|
| 24 | 176,906 | 353,812 | 33,554,432 | 16,840 B | 15.61 s | PASS |
| 26 | 649,532 | 1,299,064 | 134,217,728 | 18,992 B | 63.66 s | PASS |
| 28 | 2,405,236 | 4,810,472 | 536,870,912 | 20,464 B | 254.11 s | PASS |
| 30 | 8,964,800 | 17,929,600 | 2,147,483,648 | 21,968 B | 1,020.00 s | PASS |

The peak values are Python allocations observed by `tracemalloc` during each
stream and exclude interpreter/runtime baseline memory.  Their slow linear
growth with `n`, despite a 50-fold increase in output count from `n=24` to
`n=30`, is consistent with the proved `O(n)` working-memory design.

Every row independently passed all of the following checks:

- total and per-shell bracelet counts equal the fixed-weight Burnside values;
- the two alpha values give exactly twice the bracelet count;
- orbit sizes sum to `2^(n-1)` represented Q-vectors;
- those Q-vectors represent all `2^(n+1)` switching classes;
- output order is strictly shell-then-code and every record has even parity.

Observed defect-shell Q-bracelet totals (equal to the independent Burnside
targets):

```text
n=24: 0:1, 2:12, 4:256, 6:2920, 8:15581, 10:41272, 12:56822,
      14:41272, 16:15581, 18:2920, 20:256, 22:12, 24:1
n=26: 0:1, 2:13, 4:328, 6:4576, 8:30415, 10:102817, 12:186616,
      14:186616, 16:102817, 18:30415, 20:4576, 22:328, 24:13, 26:1
n=28: 0:1, 2:14, 4:413, 6:6916, 8:56021, 10:235378, 12:544802,
      14:718146, 16:544802, 18:235378, 20:56021, 22:6916, 24:413,
      26:14, 28:1
n=30: 0:1, 2:15, 4:511, 6:10133, 8:98254, 10:502303, 12:1444147,
      14:2427036, 16:2427036, 18:1444147, 20:502303, 22:98254,
      24:10133, 26:511, 28:15, 30:1
```

Ordered stream SHA-256 digests:

```text
n=24  3765a71c19eb42fc00e8a090b74c32681110962023947d6d4022a3a4fd359c13
n=26  9d743ad176719a0683ee91b349fd44bf5b82323093cf64442ee543b38ca2fc5c
n=28  086757e0b7d19a4e4f55618dbc92a7d3b6a70ea3c6f2bc1770a9ee1c0f7f6792
n=30  1ed92d7a5279e4bc53f82225f70740150dfbf41cfd74680b95c96b83383b508c
```

The complete shell totals, individual checks, environment, hashes, timings,
and memory measurements are preserved in
`research/audit/direct_bracelet_generator_audit.json`.  The full audit took
1,354.73 seconds.

## Conclusion

The direct generator is an exact, deterministic, constant-output-storage
replacement for the visited-array generator at all audited sizes.  It is
approved as the production Q-bracelet source for Task 33B.  The next gate is
the complete `n=24` spectral search; no claim about `n=24` minimality has been
made by this audit.
