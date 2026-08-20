# 9. Computer-Assisted Verification

Several principal results combine human arguments with finite exact
computation. This section states precisely what is proved by computation, what
is proved analytically, and how the two layers interact.

## 9.1 Proof classification

The Floquet direct sum, determinant identity, sharp positivity expansion,
operator equivalences, cancellation baseline, moment barrier, first three
moment formulas, defect inequalities, and chiral reduction are algebraic
proofs presented in Sections 2 and 4-7.

The following assertions are finite computer-assisted theorems:

1. every switching class at each even order `8<=n<=30` satisfies the
   conjectured bound;
2. the 2,626 legal flux/dihedral orbit representatives through displayed
   period 16 form a complete finite phase space;
3. the exact certificate partition used in Theorem F covers every one of those
   representatives;
4. the stated closed-walk first-positive indices and five residual Rayleigh
   quotients are the exact outputs of integer or rational arithmetic.

Independent re-execution and independently written checkers strengthen
confidence but are not additional hypotheses of the theorems.

## 9.2 Exactness of finite decisions

Floating-point eigenvalues are used only to locate likely maximizing fibers or
to propose small rational vectors. A finite decision enters the proof only
through one of the following exact forms:

- a rational Rayleigh inequality computed from an integer matrix and integer
  vector;
- a positive-definiteness certificate from fraction-free or rational
  elimination;
- a Sturm root-isolation certificate for an integer polynomial;
- an exact integer closed-walk excess;
- an exact orbit count and orbit-size sum.

Thus no strict theorem inequality depends on a floating tolerance.

## 9.3 Minimality computation

At `n=8,...,20`, direct enumeration covers all `2^(n+1)` switching classes.
At `n=22,...,30`, the computation enumerates canonical quadrilateral-flux
bracelets, retains both holonomies, and attaches the exact dihedral orbit
multiplicity. The represented switching-class total is checked against
`2^(n+1)`. The largest order therefore represents 2,147,483,648 switching
classes by 17,929,600 canonical spectral states; it does not run 2.147 billion
independent test cases.

Fresh deterministic regeneration was performed for the production orders:

| `n` | canonical spectral states | chunks |
|---:|---:|---:|
| 24 | 353,812 | 28 |
| 26 | 1,299,064 | 76 |
| 28 | 4,810,472 | 250 |
| 30 | 17,929,600 | 908 |

The regenerated ordered input digests, ordered certificate digests, shell
counts, represented totals, and terminal checkpoint chains agree with the
original computations; the mathematical mismatch count is zero. Integrity
replay of committed checkpoints is distinguished from this regeneration: it
authenticates stored execution records but does not recreate every per-state
inequality.

## 9.4 Low-period computation

For each `1<=p<=16`, one route explicitly partitions all legal flux words into
dihedral orbits. A second route uses Burnside's lemma and permutation-cycle
parities. The representative set, not merely its cardinality, is compared with
an independently generated canonical set; deterministic orbit identifiers are
bound to lexicographic order. Each stored row is then checked for legal parity,
canonicality, orbit size, `tau` lift, primitive periods, operator equivalences,
and an exact certificate.

The resulting 2,626-row table has no missing or duplicate canonical
representative. The exact exclusion partition (8.7) has no overlap and no
unresolved row.

## 9.5 Reproducible environment and trust limits

The reference environment is Python 3.12.13 with NumPy 2.3.5, SymPy 1.14.0,
and pytest 9.1.1. A machine-readable requirements file pins the Python
packages. The default suite and the three explicitly enabled slow generator
audits can therefore be run from a clean Python 3.12 environment using
repository-relative commands listed in Appendix C.

Two residual trust boundaries remain and are disclosed rather than hidden.
For orders through 22, the compact canonical minimality artifact authenticates
aggregate historical records; a fresh exact rerun has also been performed, but
the repository does not archive an independently replayable vector for every
historical state. For orders 26, 28, and 30, independent generator audits check
Burnside totals, shell totals, represented-size sums, order, and parity, while
recordwise equality against a separately implemented generator has been
carried through order 24. These are execution-trust limits of the exhaustive
part, not unreported numerical tolerances.
