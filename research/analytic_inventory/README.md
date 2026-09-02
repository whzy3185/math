# Analytic-first inventory

## Purpose and baseline

This directory starts the analytic-first rewrite on branch
`analytic-proof-first`, from commit
`44ff33a89294056907d0b909d68a8db27371c4f0`.

It is an inventory, not a proof certificate.  Status labels below describe
the current *proof form found in the repository*; they do not certify that a
claim is correct.  A claim becomes usable in a new manuscript only after its
definition, quantifiers, dependencies, and proof (or minimal exact finite
check) have been independently reviewed.

## Writing rule

The future manuscript is analytic-first.  A computation may remain only when
it closes a finite, explicitly defined residue after the mathematical
reduction proves why that residue is complete.  Code, raw certificates, and
large enumeration tables belong in a reproducibility archive rather than the
main narrative.

## Current analytic core

| ID | Candidate result | Current repository form | Intended role |
|---|---|---|---|
| A1 | Switching preserves spectrum | diagonal-sign conjugacy | Main-text lemma |
| A2 | Hamilton gauge and cycle coordinates | cycle-space algebra | Main-text definitions and lemma |
| A3 | Twisted benchmark formula | Fourier block calculation | Main-text proposition |
| A4 | Phase-slip charge arithmetic | endpoint/residue arithmetic | Main-text combinatorial lemma |
| A5 | Discrete IMS identity | finite-range commutator expansion | Main-text analytic tool |

These are the only modules presumed suitable for the first analytic outline.
Every other result must earn its place through the reduction programme below.

## High-value reduction targets

| Priority | Target | Present obstacle | Desired replacement |
|---|---|---|---|
| R1 | Period-eight spectral edge | determinant/positivity currently CAS-audited | hand-derived fiber determinant and elementary positivity argument |
| R2 | G6 physical spectral edge | resultant/Sturm plus chart exclusions | scalar Weyl/Evans or block-Jacobi matching criterion |
| R3 | Residue-two failure family | final cyclic response is only finitely checked | uniform positivity of the fixed six-by-six response matrix |
| R4 | Residues four and six | finite LDL bridge and IMS threshold | all-length two-/three-interface theorem |
| R5 | Equality at 34 and 36 | local-window enumeration | forbidden-pattern or sum-of-squares rigidity lemma |
| R6 | Equality at 38, 42, 44, 46 | finite automaton and terminal certificates | recurrent-core/holonomy obstruction |

The initial research order is R1 -> R2 -> R3 -> R4.  R5 and R6 are pursued
only after the failure side has a coherent analytic story, because an
analytic all-even classification is not a prerequisite for a strong theorem
paper.

## Modules that are computational until replaced

- the complete quotient exhaustion through order 30;
- local-window/de Bruijn closure at the recovered equality orders;
- the 96-row finite failure bridge;
- global G6 branch selection by atlas or interval exclusion;
- the all-even order partition.

They may support exploratory decisions and later finite verification.  They
must not be described as analytic proofs merely because their arithmetic is
exact.

## Candidate article routes

### Route A — analytic classification

Use only if R1--R4 yield uniform residue theorems and the remaining equality
orders admit a small human-checkable closure.  The main theorem may then be
an all-even truth-pattern theorem with a genuinely small finite base.

### Route B — analytic counterexample mechanism

Default fallback.  Prove the period-eight and phase-slip mechanism, derive
an infinite analytic counterexample family, and treat explicit small
counterexamples as applications.  Do not assert the full truth pattern.

### Route C — finite counterexample note

Use only if the analytic programme stalls.  Its theorem is limited to exact
counterexamples and rigorously stated finite ranges; it is not the preferred
submission route.

## Immediate next artifacts

1. `proof_map.md`: one dependency graph with every edge labelled analytic,
   exact-finite, or unverified.
2. `period8_derivation.md`: a clean direct derivation target for R1.
3. `g6_scalar_problem.md`: precise scalarization problem and rejection
   criteria for R2.
4. A new English manuscript outline only after Route A or Route B is chosen.
