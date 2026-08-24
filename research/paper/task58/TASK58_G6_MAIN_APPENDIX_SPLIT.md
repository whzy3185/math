# Task 58 G6 Main-Appendix-Supplement Split

## 1. Purpose and governing rule

This document fixes the publication split for the canonical G6 edge proof.
It is subordinate to the locked Task 58 manuscript blueprint and to the
canonical package
`research/paper/proof_completion/05_g6_edge/`.

The main paper must contain enough mathematics to make the implication

```text
bilateral G6 operator
  -> discrete physical matching problem above eta
  -> realized level c_6
  -> no higher physical level
  -> global rank-two squared edge
```

readable and logically complete. Appendix A supplies the exhaustive exact
algebra behind the finite matching audit. The separate supplement supplies
reproducibility records, not missing proof logic.

Throughout, `c_6` is the squared spectral value defined as the unique root of
the registered degree-ten polynomial in its exact rational isolating interval.
It is not defined by a decimal.

## 2. Section 4: material that stays in the main text

### 2.1 Bilateral model and essential-spectrum gate

Section 4 defines both orientations and both lifts of the bilateral G6
operator `A_6`, sets `H_6=A_6^2`, and proves bounded self-adjointness. It then
gives the finite-rank decoupling into two periodic half-lines and a finite
core, including the argument that each periodic half-line has the same
essential spectrum as its whole-line bulk operator. The main-text conclusion
is

```text
sigma_ess(H_6)=sigma(H_ref),
sup sigma_ess(H_6)=eta.
```

The cutoff Bloch-wave and Fredholm-parametrix reasoning must remain visible at
theorem-proof depth. It may be compressed, but it may not be replaced by a
certificate reference.

### 2.2 Discreteness and physical matching gate

Section 4 explicitly deduces that every spectral point above `eta` is an
isolated eigenvalue of finite multiplicity. It states the reciprocal Floquet
quartic, the `2+2` hyperbolic splitting for every `y>eta`, and the resulting
exponential decay of physical modes.

The coordinate-free matching criterion stays in the main text: after the left
unstable plane is transported through the exact G6 core, a level is physical
if and only if the transported plane meets the right stable plane
nontrivially. Grassmann coordinates are local representations of this
intersection, not its definition.

### 2.3 Algebraic candidate and realization gate

Section 4 prints the full degree-ten polynomial defining `c_6` and its exact
rational isolating interval before using the symbol. It states, with a concise
proof based on the certified unsquared Evans determinant, that the local
interval contains exactly one simple positive physical root and that the
square of this already realized root is `c_6`.

The order of logic must be visible:

```text
unsquared physical zero exists and is unique
  -> exact elimination identifies its square
  -> the realized squared level equals c_6.
```

### 2.4 Candidate completeness and maximality gate

Section 4 states the exact finite candidate-completeness lemma and explains
why it applies on the whole interval from the upper endpoint for `c_6` to the
row-sum ceiling `16`. It cites Appendix A for the complete chart and Sturm
audit, but retains the mathematical consequence: every possible physical
level above `c_6` lies in the certified candidate intervals, and the genuine
unsquared matching determinant is nonzero on each of them.

Combining this exclusion with realization and the symmetry between the two
unsquared branches, Section 4 proves, for both orientations and both lifts,

```text
sup sigma(H_6)=c_6.
```

This is the maximality gate. Essential-spectrum equality alone does not prove
existence of `c_6`, and algebraic isolation alone does not prove maximality.

### 2.5 Rank-two gate

Section 4 gives the analytic symmetry argument in full. In the forward tree
gauge it defines

```text
(Ku)_i=(-1)^i u_(9-i)
```

and proves

```text
K^2=-I,    KA_6=-A_6 K,    KH_6=H_6 K.
```

It then combines the simple positive physical eigenvalue at `+sqrt(c_6)`, its
simple negative partner at `-sqrt(c_6)`, and the orthogonal spectral
decomposition of `A_6^2` to conclude

```text
dim ker(H_6-c_6)=2.
```

This analytic deduction stays in the main text. Appendix A may repeat the
identities as part of its audit, but it does not replace the main-text proof.

## 3. Appendix A: exact mathematical certification

Appendix A contains the detailed finite algebra that justifies the two
main-text certification lemmas. It includes:

1. The exact period-eight monodromy and reciprocal characteristic polynomial
   needed for bulk hyperbolicity, together with exact exclusions of unit-circle
   multipliers above `eta`.
2. The exact G6 core transfer and the exterior-product form of the physical
   matching condition.
3. The complete Grassmann atlas, all chart transitions, and proofs that the
   stable and unstable planes remain covered throughout the audited energy
   interval.
4. The elimination leading to the degree-ten factor, the exact rational
   isolation of its relevant root, and the separation of genuine factors from
   denominator, squaring, chart-section, and nonphysical-sheet artifacts.
5. Exact Sturm counts proving that the resultant candidate list is complete.
6. The unsquared Evans sign and derivative audit that proves local physical
   existence, uniqueness, and simplicity before algebraic identification.
7. The unsquared nonvanishing checks that reject every positive-branch
   candidate interval above `c_6` in all required charts; the negative branch
   is covered analytically by the main-text `K` symmetry.
8. The row-sum closure at `16`, showing that no spectral region remains
   outside the exact audit.
9. A short audit of the symmetry identities and the passage from the two
   simple unsquared partners to the rank-two squared eigenspace.

Appendix A must explain why its finite algebraic object is exhaustive. It must
not merely list a polynomial, resultant factors, or checker outcomes.

## 4. Separate reproducibility supplement

The supplement contains only the removable reproducibility layer for this
proof:

- certificate schemas and machine-readable certificate payloads;
- manifests, immutable hashes, file sizes, and provenance paths;
- producer and independent-checker commands, software versions, and expected
  outputs;
- raw rational isolating intervals, chart records, cofactor rows, sign records,
  and full resultant factorizations when these are too large for Appendix A;
- tamper tests, negative controls, resource notes, and reconstruction logs;
- independent-coordinate cross-check records.

The supplement may carry expanded tables supporting Appendix A, but removal
of the supplement must leave the logical proof in Section 4 plus Appendix A
complete. A command that prints `PASS` is evidence that a specified finite
object was checked; it is not a substitute for the mathematical reduction,
the exhaustiveness argument, or the theorem statement.

The exact-`2r` finite-ring package belongs elsewhere in this same separate
supplement under the locked Task 58 plan. It is not part of the bilateral G6
edge proof and must not be imported into Section 4 or Appendix A merely to
strengthen the presentation.

## 5. Mandatory logic gates

The final Section 4 and Appendix A must make the following five gates
independently auditable.

| Gate | Required input | Required conclusion | Forbidden shortcut |
|---|---|---|---|
| Existence framework | Bounded self-adjoint `H_6`, exact tails, and physical matching | A spectral level above `eta` must arise from an `l^2` stable/unstable intersection | Inferring a physical level from an elimination factor |
| Discreteness | Essential-spectrum identity with upper edge `eta` | Every spectral point above `eta` is isolated with finite multiplicity and has exponentially decaying tails | Treating essential-spectrum equality as existence of `c_6` |
| Realization | A genuine unsquared Evans zero in the isolating interval | A simple physical eigenvalue `+sqrt(c_6)` exists, and its square is `c_6` | Declaring a resultant root physical without an unsquared check |
| Maximality | Exhaustive chart cover, complete candidate list, unsquared exclusions, and row-sum closure | No physical spectral point of `H_6` lies above `c_6` | Replacing global exclusion by local root isolation |
| Rank two | Simple unsquared positive root, `K^2=-I`, `KA_6=-A_6K`, and self-adjointness | Simple partners at `+sqrt(c_6)` and `-sqrt(c_6)` give `dim ker(H_6-c_6)=2` | Calling the squared edge simple or assigning one squared mode per G6 |

The dependency order is

```text
essential-spectrum identity
  -> discreteness and hyperbolic matching framework
  -> physical realization of c_6
  -> exhaustive exclusion above c_6
  -> global edge
  -> rank-two squared eigenspace.
```

None of these arrows may be reversed or silently collapsed.

## 6. Prohibited wording and inferences

The following formulations are forbidden in Section 4, Appendix A, captions,
and the supplement:

- "The resultant proves that `c_6` is a physical eigenvalue."
- "Every root of the degree-ten polynomial is a G6 level."
- "Root isolation alone proves the G6 global edge."
- "The essential-spectrum calculation produces the eigenvalue `c_6`."
- "`c_6` is a simple eigenvalue of `H_6`."
- "The G6 squared edge is simple."
- "One G6 interface contributes one squared mode."
- "The exact-`2r` theorem is needed to prove the bilateral G6 edge."
- "A numerical Evans zero establishes realization or maximality."

The allowed multiplicity wording is:

```text
The unsquared operator A_6 has one simple physical eigenvalue at each of
+sqrt(c_6) and -sqrt(c_6). Consequently c_6 is an isolated eigenvalue of
H_6=A_6^2 with multiplicity two.
```

The allowed resultant wording is:

```text
Elimination supplies a complete finite list of algebraic candidates. A
candidate is accepted as physical only after the genuine unsquared matching
condition is verified in a covered Grassmann chart.
```

## 7. Final placement checklist

- Section 4 contains the theorem, the five logic gates, and the analytic
  rank-two deduction.
- Appendix A contains the complete exact mathematical audit proving candidate
  completeness, physical realization, and global exclusion.
- The supplement contains raw records and reproducibility metadata only.
- The polynomial and exact isolating interval appear before the first theorem
  that uses `c_6`.
- Every orientation and both lifts are covered.
- Positive and negative unsquared branches are distinguished from the squared
  eigenspace.
- No resultant zero is called physical without an unsquared matching check.
- No sentence calls `c_6` simple for `H_6`.
