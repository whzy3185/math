# Hostile Computer-Assisted Proof Review

## Verdict

`PASS_WITH_EXPLICIT_INDEPENDENCE_DISCLOSURE`.

## Orders 34--46

The finite-state proof is referee-credible. The local interlacing lemma maps a
forbidden window to a rigorous spectral lower bound. The parity-lifted de
Bruijn graph is sound and complete for all surviving cyclic words. Both
holonomies are checked. The implementation-independent verifier rebuilds
57,344 windows, the closed walks, canonical terminal classes, and all 64
`(Q,alpha)` records, obtaining zero unresolved terminals. No floating-point
comparison accepts a case.

## Finite counterexample bridge

The order-40 and `48<=n<240` witnesses use exact full-matrix LDL certificates.
The tail starts from a finite four-residue endpoint check plus monotonicity,
not an unbounded computation. This correctly separates finite exhaustive work
from analytic continuation.

## Periodic frontier

The `p<=24` scope is exact and finite. The primary `c6` checker reconstructs
recordwise exact inequalities but shares canonical/Bloch helpers with the
producer. An implementation-disjoint bracelet audit independently validates
the period-17--24 orbit partition, but its stored endpoint is weaker than
`c6`. The publication appendix must describe this as layered independence,
not as one fully disjoint checker.

## Uniform single-gap corollary

All seven comparisons are exact. The smallest margin is the `g=8` value

```text
174815250030533/310875000000000000>0.
```

Hence the strict `c6+1/250` statement does not depend on rounded decimals.

## Reproducibility finding

The checker commands and certificate paths are documented. Before a frozen
submission, the currently local proof-completion and uniform-gap artifacts
must be included in the submission commit and their reported outputs rerun on
that exact commit. This task intentionally performs no commit or push.
