# Why the manuscript has this structure

The final manuscript uses six sections rather than the nine-section
mathematical inventory.  A ten-paper full-text audit of 2024--2025 JGT
articles found four to seven main sections to be the normal range for nearby
spectral, structural, exact-extremal, and counterexample papers.  General tools
receive their own sections when they explain several later results; secondary
consequences remain inside the proof arc that produces them.

Accordingly, the article contains three principal arcs.

1. **Coordinates and mechanism.**  Switching first forces the passage from
   raw edge signs to local triangle flux and global holonomy.  Periodicity then
   gives finite Bloch fibers.  This makes the general half-cell chiral theorem
   a natural answer to a question already raised by the setup.
2. **Exact solution.**  The general theorem halves dimension but does not solve
   an arbitrary fiber.  The period-eight word is then introduced as the first
   sub-eight realization and is solved completely.  The four bands, two
   holonomy sectors, and twisted comparison remain in one section because they
   are consecutive consequences of the same polynomial.
3. **Why period eight.**  Once the exact family is known, the natural questions
   are whether a shorter phase works and whether the first feasible period is
   unique.  Moment reduction, the exact certificate table, and the
   period-eight recurrence answer those questions in one section.  Its final
   subsection returns the same moments to arbitrary periods, avoiding a second
   statement and proof of the same formulas.

There is no separate literature review, computation section, negative-sector
section, or formal-verification section.  Each would break a mathematical
dependency chain or overstate a secondary component.  Three vector figures
introduce the signed cell, finite phase grid, and period-eight defect orbits at
the precise points where prose alone would impose extra notation.  The
equation-only half-cell schematic was removed.  The single table appears
only after the moment and symmetry reductions have proved that its rows are
complete.

The resulting sequence is

```text
fixed-graph optimization
 -> switching-invariant flux
 -> finite periodic fibers
 -> general half-cell chiral mechanism
 -> exact period-eight spectrum
 -> finite-ring comparison
 -> smallest primitive period
 -> rigidity at first occurrence
 -> general defect obstruction.
```

This organization is JGT-first: the graph problem and structural phase are
foregrounded, while the matrix calculation is a complete proof engine.  An LAA
conversion can promote the chiral theorem and four-band formula without
altering the proof kernel.
