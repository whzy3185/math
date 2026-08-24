# Task 60.0-60.1 Hostile Audit

## Attacks and resolutions

| Attack | Result |
|---|---|
| Raw seam-gauge chord signs were confused with invariant `tau` | REPAIRED: `tau_i=b_i product a_(i+r)` is now explicit |
| `(Q,alpha)` was treated as a complete switching coordinate | FALSIFIED: a lift bit is required |
| Mixed-channel cancellation was interpreted as a zero finite matrix entry | FALSIFIED: modular collisions can leave another contribution |
| Distinct `A^2` displacements were assumed for all `s,N` | REPAIRED: complete collision table and aggregation law added |
| Ordinary periodic shift was used in the antiperiodic sector | REJECTED: every formula uses `T^N=alpha I` |
| The proposed `2s` sign was copied from `s=2` | REPAIRED: the sign is `(-1)^s` |
| The finite maximum was assumed to occur at the smallest angle | FALSIFIED for odd `s` and for some small even-`s` rings |
| One holonomy was assumed uniformly best | PROVED only for even `s`; FALSIFIED for odd `s` |
| Alternating `Q=-1` was assumed for odd `N` | FALSIFIED: cyclic lift requires even `N` |
| Fourier evidence was treated as a global minimization theorem | REJECTED: no optimality claim beyond the frozen `s=2` result |

## Independent verification

- General words: 288 exact integer matrix checks.
- Alternating words in the Task 60.0 verifier: 200 checks.
- Dedicated Task 60.1 exact identities: 180 sector checks and 360 lift checks.
- Symbolic checks: 9 Chebyshev derivatives, the exact `s=3` critical point
  and maximum, and the even-`s` expansion through `N^-4`.
- Flat-collision identities `N=2s+2`: 9 checks.
- Tamper tests: diagonal-coefficient and parity-sign mutations both rejected.
- Focused tests: 23 passed across the two stages.

## Surviving claims

1. Hamilton gauge, invariant `tau`, and `Q` lift theory are universal.
2. Mixed `1+Q` cancellation is universal at path level.
3. The alternating-flux squared operator and finite Fourier maximum are exact.
4. Even and odd chord lengths have genuinely different continuous spectral
   geometry.

No periodic-bulk optimality, elementary-defect, charge, IMS, or eventual
failure claim is active at this checkpoint.
