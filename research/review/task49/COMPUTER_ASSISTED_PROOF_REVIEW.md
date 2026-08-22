# Task 49 Independent Computer-Assisted-Proof Review

## Findings

### MODERATE 1: floating point still proposes exact certificate vectors

The p<=24 audit independently computes a floating endpoint eigenvector before
rounding it to an integer vector.  Acceptance is nevertheless exact: the
integer Rayleigh quotient is recomputed and compared rationally with
`1561/200`.  This is sound, but future supplementary material should emphasize
the proposer/verifier split and, if artifacts are packaged, archive the
integer vectors rather than only the recomputed quotients.

### MODERATE 2: high-precision Evans evidence is not interval arithmetic

Agreement across 80, 120, and 160 digits and with two full-matrix checks is
strong numerical verification, not a proof certificate.  The next task needs
directed rounding, root isolation, and independently checkable intervals.

### MINOR 1: software and resource bounds should accompany the final package

The baseline records Python and core library versions.  A publication archive
should additionally record per-script wall times, peak memory for the p24
audit, and the exact command manifest.  This affects packaging, not the
mathematical partition.

## Positive Checks

The p<=24 second implementation does not import canonicalization, moment, or
matrix helpers from the production path.  Exact destructive accounting has no
missing or duplicate class.  The 183 strict quotients are recomputed rather
than hash-compared.  The Hankel audit uses an independent exact principal-minor
search and checks all 184 inputs, with no floating witness reuse.  Threshold
counterexamples are accepted only after exact sparse LDL positivity and a
rational threshold lower bound.  Rows lacking a rigorous non-counterexample
comparison are honestly labeled numerical.

## Verdict

- BLOCKER: 0
- MAJOR: 0
- MODERATE: 2
- MINOR: 1

`P24_AUDIT_PASS` and `HANKEL_AUDIT_PASS` are supported.  The numerical
interface computation is ready to become, but is not yet, a computer-assisted
theorem.
