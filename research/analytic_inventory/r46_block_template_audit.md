# Residues four and six: block-template audit

## Objective

The standard constructions use two G6 slips for \(n=8k+4\) and three G6
slips for \(n=8k+6\).  The goal is to decide whether they admit the same
*method* as residue two: fixed defect core, periodic bulk Riccati map, and a
fixed cyclic Schur boundary.  This audit does not claim the resulting cap
theorems.

## Exact structural findings

At the fixed rational caps

\[
T_4=\frac{2679}{338},\qquad T_6=\frac{5782}{729},
\]

direct block extraction from the standard gap words gives:

| Residue | Natural blocks | Interfaces | Bulk behaviour | Consequence |
|---|---|---:|---|---|
| \(4\) | cyclic four-site blocks | 2 | only finitely many diagonal/link blocks differ from the repeating bulk pattern | a fixed two-interface core plus variable bulk arcs is plausible |
| \(6\) | one two-site boundary block plus four-site blocks | 3 | finitely many defect blocks and links, with a repeating bulk away from them | a fixed three-interface core plus variable bulk arcs is plausible |

The statement was checked at two different admissible orders in each residue:
\(52,60\) and \(54,62\).  The locations of the finite defect patterns vary
with the balanced gap placement, but their matrix types do not proliferate.

### Blocking correction

A naive four-site blocking is unsuitable for residue four: the bulk has
period eight, so the apparent number of non-modal four-site blocks grows with
the order.  Reblocking as one four-site boundary block followed by eight-site
cells exposes the correct structure:

\[
\text{fixed boundary/interface data}
\; + \;
\text{period-eight arc I}
\; + \;
\text{period-eight arc II}.
\]

The arcs can carry different translates of the same period-eight bulk.  Their
lengths vary with the balanced placement of the two G6 slips.  Hence the
right analytic object is a **two-arc response system**, not a single bulk
Riccati orbit with two isolated exceptional blocks.  This was checked by
direct exact block extraction at orders 52 and 60.

The exact template verifier now checks at orders 52, 60, 68, and 76 that the
partition consisting of one four-site block followed by eight-site cells
covers every vertex and makes \(T_4I-A^2\) cyclic block-tridiagonal.  This
establishes the algebraic reduction input, not the required positive cap.

## What cannot be shared blindly

The residue-two proof does not transfer verbatim.

1. The caps \(T_4,T_6\) change the bulk diagonal blocks and hence the
   Riccati maps.
2. Residue four has no distinguished two-site boundary block in its natural
   four-site blocking, whereas residue six does.
3. Two and three interface channels create a larger terminal matching core.
4. The two bulk arcs must be controlled separately; a single-interface
   response recurrence does not account for their interaction automatically.

## Proposed work order

1. **R4 template.**  Fix the symmetric two-G6 word, derive its four-site
   boundary plus eight-site two-arc matrix at \(T_4\), and isolate the
   finite two-interface core.
2. **R4 bulk.**  Search for a rational invariant two-cycle and local
   Lyapunov metric, as in residue two.
3. **R4 boundary.**  Derive a response recurrence with two arc responses and
   a fixed terminal core.  Stop if a non-decaying channel appears.
4. Repeat for R6 only after R4 yields a clean template; R6 then tests whether
   a parameterized multi-interface theorem is genuinely viable.

## Kill criterion

Abandon a shared R4/R6 theorem if the exact block template yields a neutral
or expanding response channel at the proposed cap, or if the limiting
terminal core fails a rational positive-margin test.  In that case split the
residues and retain only the strongest analytically closed family.

## Evidence boundary

Existing finite LDL rows and multi-interface numerical spectra are useful
diagnostics only.  They do not prove a spectral-radius upper bound because a
near-\(c_6\) interface eigenvalue does not exclude a larger finite-ring
eigenvalue.
