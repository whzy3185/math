# Finite Phase-Slip Pattern Families

Status: **CONJECTURAL FAMILY CANDIDATES; FINITE INSTANCES EXACTLY CERTIFIED**

## Controls and Search Boundary

All even orders `32<=n<=128` are scanned. Multiples of eight use the exact
period-eight repetition as a positive control. The remaining seeds represent
truncation and repair, one or two phase slips, distributed or localized
mismatch, and local defect mutation. A deterministic beam search applies
legal `Q`-pair flips through Hamming radius four. No random restart is used.

Every reported negative numerical gap is followed by an exact finite-matrix
certificate. Positivity of `qI-pA^2` proves `rho(A)^2<q/p`; the threshold is
bounded below by `1561/200` at `n=32` and by `8-200/n^2` for `n>=34`.

## Observed Families

### Single gap 6, residue 2

For `n=50,58,...,122`, the certified word has an even number of defects with
gap sequence

```text
4,4,...,4,6.
```

All ten tested instances use `alpha=+1`. This is a candidate family for
`n congruent to 2 (mod 8)` from 50 onward. The experiment does not prove the
infinite continuation.

### Two gaps 6, residue 4

For `n=52,68,84,100,116`, the certified word has two separated gaps 6 and all
remaining gaps 4. All five instances use `alpha=-1`. The observed spacing is
16, so the narrow data-supported formulation is `n congruent to 52 (mod 16)`.

### Single gap 10, residue 6

For `n=94,102,110,118,126`, the certified word has one gap 10 and all
remaining gaps 4, with `alpha=+1`. This suggests a delayed residue-6 family,
but smaller tested orders in the same residue do not all work.

## Relation to Existing Artifacts

The scan independently recovers the proved period-eight positive controls and
overlaps the repository's earlier period-10 family at some orders divisible by
10. Sixteen certified orders are divisible by neither 8 nor 10:

```text
52, 58, 66, 68, 74, 82, 84, 94,
98, 102, 106, 114, 116, 118, 122, 126.
```

These finite examples are exact. Any claim that one of the displayed gap
patterns continues indefinitely requires a separate Floquet or finite-family
proof and is deliberately deferred.
