# Computer-Assisted Boundary

## Human mathematics before computation

The proof first reduces the spectral question to:

1. the reciprocal quartic (1) in `FULL_PROOF.md`;
2. the geometric intersection condition (5);
3. an exact finite interface transfer;
4. finitely many algebraic candidate intervals.

The symmetry and rank-two argument are entirely analytic.

## Exact finite objects verified by machine

- The `4 x 4` period-eight monodromy and its reciprocal characteristic
  polynomial.
- Rational isolating intervals for bulk degeneracies and roots of `p_6`.
- The exact G6 defect transfer and cofactor sections.
- A three-chart cover of the stable and unstable Grassmann planes on the
  compact interval from the upper `c6` endpoint to `16`.
- Resultant factorizations and exact Sturm counts proving candidate
  completeness.
- Outward rational interval signs for the unsquared physical determinant and
  its derivative.

No floating-point sign decision is accepted.

## Producer and independent verification

The principal certificates are:

```text
research/proofs/task50/certificates/g6_interface_certificate.json
research/proofs/task51/certificates/c6_exact_evans_elimination.json
research/proofs/task53/certificates/bulk_global_hyperbolicity.json
research/proofs/task53/certificates/g6_grassmann_atlas.json
research/proofs/task53/certificates/g6_global_edge.json
```

The reconstruction/checker chain is provided by:

```text
research/scripts/verify_target_a_task50_interface.py
research/scripts/verify_target_a_task51.py
research/scripts/verify_target_a_task53_a1.py
research/scripts/verify_target_a_task53_a2.py
research/scripts/verify_target_a_task53_a3.py
```

Independent coordinate checks use different cofactor rows for the local
root and the two global exclusion intervals.

## Why the verification proves the theorem

Hyperbolicity gives a complete geometric matching criterion. The atlas proves
that this criterion is represented on every point of the compact energy
interval. Elimination supplies a necessary finite candidate list; Sturm
counts prove the list complete; unsquared interval evaluation rejects each
candidate. The local interval separately contains one and only one physical
root. The row-sum bound closes the spectrum at `16`. These statements leave
no unverified energy region.

## Boundary and nonclaims

- Resultant zeros are never declared physical without an unsquared check.
- The theorem concerns one G6 interface, not arbitrary finite cores.
- Rank two refers to `H_6=A_6^2`; the two unsquared eigenvalues are simple.
- No general finite-ring simplicity statement is made.
