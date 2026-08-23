# General B0-to-B2 Interface Program

## Current Theorem Boundary

The universal statement

```text
every finite-core B0-to-B2 interface has sup sigma(A^2)>=c6
```

remains `OPEN`. Task 55 proves two strict subclasses.

First, let `g=(g_1,...,g_m)` be a reflection-canonical primitive multi-gap
word with `m>=2` and

```text
sum(g_i) in {2,6,10,14,18}.
```

For every one of the 31,008 such words, an explicitly stored integer vector
has finite support and exact Rayleigh quotient strictly larger than the
certified upper endpoint for `c6`. Hence every interface in this bounded
class satisfies

```text
sup sigma(A^2)>c6.
```

This is `COMPUTER_ASSISTED_PROVED`. The producer emits the complete canonical
word stream and integer witnesses; the checker independently enumerates the
same class, rebuilds the open-interface `Q` and `tau`, computes the full
outgoing `Av`, and verifies each strict integer comparison.

Second, every finite core containing consecutive gaps `(3,3)` satisfies the
uniform analytic bound

```text
sup sigma(A^2)>=419/53>c6.
```

The proof uses one of three explicit integer vectors according to whether the
preceding gap is `1`, `2`, or at least `3`. The succeeding gap can alter only
the sign of one outgoing coordinate, and the other `tau` lift is obtained by
the alternating unitary. This result has no support-sum restriction.

## Classification And Equivalences

Primitivity is combinatorial: no nonempty contiguous subword has zero total
charge `sum(g_i-4)`. It does not authorize deletion of a zero-charge block
from a spectral problem. Reflection and translation are the only word-level
normalizations used in the bounded certificate; diagonal switching supplies
the corresponding operator equivalence.

Insertion or deletion of a complete reference cell is not a spectral
equivalence. It multiplies boundary data by a non-scalar period-eight bulk
monodromy and can change the matching determinant. Any universal proof must
retain that propagation.

## Remaining Scope

The certificate does not cover primitive words with support sum greater than
18 unless they contain `(3,3)`. It also does not prove an equality
classification, a replacement principle reducing every core to G6, or a
uniform lower gap above `c6` for all non-G6 cores. In particular, the absence
of a below-`c6` competitor in 31,008 cases is not an exhaustion of all finite
interfaces.

The next useful theorem would be a local replacement lemma that preserves the
`B0-to-B2` sector jump and does not increase the spectral top. A terminating
replacement system with G6 as its only minimal core would prove the universal
statement. Until such a mechanism or a complete transfer-boundary invariant
is supplied, the universal result remains `OPEN`.

## Artifacts

- `certificates/multigap_support18.jsonl`
- `certificates/multigap_support18_manifest.json`
- `TARGET_A_MULTIGAP_SUPPORT18_THEOREM.md`
- `TARGET_A_THREE_THREE_LOCAL_LEMMA.md`
- `research/scripts/target_a_task55_multigap.py`
- `research/scripts/verify_target_a_task55_multigap.py`
- `research/scripts/verify_target_a_task55_multigap_alt.py`
- `research/scripts/test_target_a_task55_multigap.py`
