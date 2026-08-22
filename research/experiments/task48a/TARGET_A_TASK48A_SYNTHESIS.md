# Target A Task 48A: Q1-Theorem Signal Synthesis

## 1. Exact frontier

The exact frontier through displayed period 24 is closed.  Of 370,100 legal
dihedral orbits at periods 17 through 24, 369,916 are excluded by an exact
`F_k>0` obstruction, 183 survivors have exact `R>eta` certificates, and one
survivor is the repeated period-8 equality.  There are no lower or unresolved
classes.  `P24_BOUNDED_OPTIMALITY` is ready for independent proof audit and
formal integration.

## 2. Single interface

The gap-6 and gap-10 constants are

- `c6 = 7.905369311620327011976279279804273987486348974350953...`
- `c10 = 7.977104370400546515362821583215693131572428742299712...`

Both lie strictly below 8.  Two-exponential convergence is preferred over a
power law by BIC and hold-out behavior.  The eigenvectors are exponentially
localized, and their cell-decay multipliers match the slow stable multipliers
of the analytically continued period-8 bulk transfer matrix.  A
four-dimensional Evans matching determinant is operational.  Its stable
subspaces have not yet been eliminated symbolically, so the interface result
is a strong theorem signal, not a theorem.

The gap-6 constant has a validated degree-10 algebraic candidate; gap 10 has
no accepted polynomial under the reconnaissance bounds.  Neither status is
`EXACTLY_PROVED`.

## 3. Two interfaces and mod 16

Two gap-6 states split exponentially around the single-interface level.  The
4-mod-16 family uses a symmetric split, while the 12-mod-16 family shifts one
period-8 cell away from symmetry.  The small-order minima use `alpha=-1`.
This gives a coherent hybridization, parity, and holonomy explanation of the
old mod-16 observation.

## 4. Residue 12

Order 44 is not a counterexample in the prescribed structures.  Every tested
order `60,76,...,508` is an exact counterexample in a fixed two-gap-6 family;
all 29 certificates pass.  The family tends to `c6<8`.  The residue-12 signal
is therefore strong.

## 5. Eventual failure at all even orders

Verified structural signals now cover all even residues:

- `0 mod 8`: the Task 47 truncated period-8 family, exact at 32 through 128;
- `2 mod 8`: the single gap-6 family;
- `4 mod 16`: symmetric two-gap-6 splitting;
- `12 mod 16`: shifted two-gap-6 splitting, exact from 60 in this scan;
- `6 mod 8`: the single gap-10 family.

Thus “all sufficiently large even orders admit a counterexample” is a
`STRONG` theorem target.  No residue class lacks a structural candidate, but
every family still needs a uniform analytic finite-size bound before this can
be stated as a theorem.

## 6. Moment matrix

The exact Hankel pilot excludes 183 of 184 `F16` survivors by depth 5 and
leaves only the repeated target.  Its value is `HIGH`.  It offers a compact
route to the p<=24 proof and may become a structural theorem if an
arbitrary-period implication is found.

## 7. Q1 theory triage

1. **ALL_SUFFICIENTLY_LARGE_EVEN_N_THEOREM**
   Scientific value is highest and would materially strengthen a JCTB case.
   Feasibility is now plausible because every residue has an explicit family.
   Required work is a period-8 transfer/interface proof with uniform finite
   ring error bounds in all five residue families.  Risk remains high because
   the current evidence is computational and asymptotic.

2. **PHASE_SLIP_INTERFACE_THEOREM**
   This is the foundational analytic result and the most feasible immediate
   proof.  It requires exact stable-subspace elimination or a rigorous
   transfer contraction argument.  Its publication impact is high and it is
   the necessary engine for priority 1.

3. **P24_BOUNDED_OPTIMALITY_THEOREM**, with the moment hierarchy as the proof
   presentation.  The exact certificate chain is already complete and risk
   is low after independent audit.  It strengthens the paper decisively but
   has less reach than an infinite-family theorem.

`MOMENT_MATRIX_THEOREM` ranks next: the pilot is unexpectedly strong, but a
general statement has not yet emerged.  Generic computational expansion
should stop.

## Decision

Task 48A follows the BLUE path.  The recommended next task is a single proof
program: derive rigorous period-8 interface bounds and use them to prove
eventual counterexamples in every even residue class.  P24 should be audited
and integrated in parallel only after that proof program's first gate.

Current strongest scientific identity: localized phase-slip states in a
period-8 defect crystal, with a credible route to eventual failure at every
even order.  A JCTB-level theorem pursuit is justified; the present evidence
alone is not yet the theorem.
