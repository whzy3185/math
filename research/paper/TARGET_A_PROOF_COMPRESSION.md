# Target A Proof Compression

Status: **TARGET_A_PROOF_COMPRESSION_COMPLETE**

The paper package has six main results. Internal Task numbers do not appear in
their statements.

## Theorem A: Smallest Counterexample

**Statement.** The explicit order-32 failure and exact exclusion of every
admissible smaller even order imply that the smallest counterexample order is
`n=32`.

Main text keeps: the `(Q,alpha)/D_n` quotient lemma, exact search-space counts,
the finite exclusion conclusion for `8<=n<=30`, and the explicit exact `n=32`
inequality. Checkpoint chains, chunk layouts, runner details, and full hash
tables move to the computational appendix or supplement.

## Theorem B: Infinite Counterexample Family

**Statement.** For every `n=8L`, `L>=4`, the explicit period-8 signing is a
counterexample for both holonomies.

Main text keeps: construction, finite Bloch decomposition, uniform spectral
bound, exact threshold comparison, and monotonicity in `n`. The independent
reconstruction and positivity implementations are audit/supplement material.

## Theorem C: Exact Period-8 Spectral Edge

**Statement.** The target has squared radius
`eta=4+sqrt(10+2sqrt(5))`, attained uniquely at `z=1`.

Main text keeps: `P(y,c)`, endpoint factorization, algebraic isolation,
positivity around the endpoint, top-band monotonicity, and finite `alpha=+-1`
corollaries. Coefficient snapshots and duplicate determinant routes move to
the appendix.

## Theorem D: Period-8 Flux Classification

**Statement.** Among infinite-volume 8-periodic Hamilton-gauge phases,
`R(Q)<8` exactly for antipodal two-defect phases,
`R(Q)=8` exactly for `Q=(-)^8`, and `R(Q)>8` otherwise; hence the target is
the unique minimizer and the all-negative phase the unique runner-up.

Main text prioritizes the local square formula, moment barrier, high-defect
combinatorics, two-defect separation hierarchy, cancellation baseline, and
sharp target theorem. This is not a finite-size or all-signings optimum. The
18-orbit table is an appendix cross-check rather
than the conceptual proof.

## Theorem E: General-Period Moment Obstruction

**Statement.** For every `p>=1`,

```text
M_1=4p,
M_2=20p+16d,
M_3=118p+168d+96a+48b,
```

and `R(Q)<=8` forces `d<=3p/4` and
`40d+96a+48b<=42p`.

Main text derives the local formula and signed closed-walk monomials, explains
short-period multiplicities, and proves the one-way moment inequality. Large
enumeration tables remain checker evidence.

## Theorem F: Low-Period Frontier

**Statement.** The target is the unique minimizer among periodic
Hamilton-gauge phases of primitive `tau` period at most 16, under the stated
equivalences.

Main text uses orbit completeness, primitive normalization, the unified
moment hierarchy, the all-negative cancellation lemma, and five residual
endpoint certificates. It reports the exact partition
`2611+8+5+2=2626`; it does not list 2624 witnesses. The full orbit table,
Burnside fixed-point data, and residual vectors belong in appendices/data.

## Reproducibility Placement

Fresh `n=24,26,28,30` regeneration verifies the implementation and evidence
chain. It belongs in a reproducibility section and supplement, not as a second
logical proof. Novelty and priority evidence is similarly separated from
mathematical dependencies.

## Frozen Omissions

No theorem asserts all-period optimality, optimality among all signings, or
finite-order global optimality for every `n`. Period 17+ exploration remains
paused.
