# Period-eight article route

## Proposed contribution

The main article should be built around a theorem package that is already
separate from the unresolved all-even classification:

> The antipodal two-defect phase is the unique legal eight-periodic flux
> phase with squared Bloch spectral edge below eight.  Its edge is
> \(\eta=4+\sqrt{10+2\sqrt5}\).  For every \(n\equiv0\pmod8\),
> \(n\ge32\), its finite signing strictly beats the twisted candidate.

This gives an infinite analytic counterexample family to the original
twisted-optimality conjecture.  It does not claim the exact minimum over all
signings, a classification at arbitrary period, or the full all-even truth
pattern.

## Main theorem package

1. **Switching and flux coordinates.**  State the gauge reduction and the
   cycle-flux parametrization used to define the periodic phases.
2. **Period-eight trichotomy.**  The unique sub-eight phase theorem from
   `period8_trichotomy_analytic_proof.md`.
3. **Chiral Floquet theorem.**  The target phase reduces from an eight by
   eight fiber to a two by two determinant and has edge \(\eta\).
4. **Finite-holonomy corollary.**  The uniform rational bound
   \(\rho(A)^2<1561/200<\rho_-(n)^2\) for every \(8\mid n\), \(n\ge32\).

## Honest finite component

The only non-symbolic finite component in this route is the three-row exact
closed-walk sublemma for the non-antipodal two-defect period-eight cases.
It consists of integer transition counts through length twenty, not a search
over signings or a floating-point spectrum.  It should appear either as a
short appendix table with the recurrence or in a small supplementary proof
note.

## Explicit exclusions

The following existing materials are not imported into the first article:

- all-even classification claims;
- R2 tail drafts pending line audit;
- residue-four/six cap programmes;
- global G6 physical-edge atlas;
- numerical multi-interface splitting studies;
- exhaustive switching enumeration at low orders.

They may appear only as clearly marked future work if needed for context.

## Reference roles

The bibliography should remain short and source-bound:

| Role | Needed source type | Permitted use |
|---|---|---|
| Direct predecessor | original signed-circulant conjecture | exact attribution of its definitions, candidate, and stated finite evidence |
| Switching | foundational signed-graph source | switching equivalence notation only |
| Signing context | Bilu--Linial/two-lift source | historical context, not proof of this theorem |
| Periodic operators | authoritative Floquet graph source | terminology and method context, not the specific determinant |
| Related extremal signed spectra | published fixed-family result | scope comparison only |

No source may be cited as support for the new period-eight trichotomy or
counterexample family; those are the article's own results.

## Venue logic

This route is judged by the clarity and novelty of its analytic spectral
mechanism, not by the size of a computational archive.  It is suitable for
an eventual graph-theory or linear-algebra submission only after direct
literature verification and an independent mathematical audit of the two
period-eight proof files.
