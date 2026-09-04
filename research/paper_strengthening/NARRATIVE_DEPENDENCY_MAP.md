# Narrative Dependency Map

| section | previous question | current answer | next natural question |
|---|---|---|---|
| 1. Introduction | Why optimize spectra over signings of a fixed graph? | switching leaves spectra invariant but cycle fluxes remain; cycle squares provide a tractable fixed family with nontrivial local cycles | Which invariant coordinates and finite spectral decomposition make the problem exact? |
| 2. Switching coordinates and periodic fibers | Raw edge signs are gauge-dependent; how should a periodic signing be represented and diagonalized? | triangle flux and Hamilton holonomy give the coordinates; cell periodicity yields finite Hermitian Bloch fibers | Which periodic flux patterns force a structural spectral simplification? |
| 3. Half-cell chiral symmetry | Can a signed half-cell translation force symmetry about zero? | exactly within the natural monomial class: half-periodic `Q` with negative half-cell flux is equivalent to an anticommuting involution and dimension halving | Does the first low-edge phase satisfy this condition, and can its reduced block be solved exactly? |
| 4. Exact period-eight phase | The general theorem halves dimension but does not solve a general block | the target period-eight word reduces further, giving all four bands, exact finite radii, and the twisted comparison | Is period eight a selected example, or is it the first possible low-edge period? |
| 5. First occurrence and rigidity | Could a shorter phase work, and are there many phases at the first feasible period? | moments plus exact survivors exclude all shorter periods; the period-eight trichotomy gives a unique sub-eight orbit | What local feature makes low-edge words scarce beyond period eight? |
| 6. Periodic defect obstructions | Are minimality and rigidity isolated finite facts? | the first three moments impose defect-density and clustering constraints for every periodic word | What exact global minimization problem remains after this structural picture? |
| 7. Concluding remarks | What does the combined mechanism establish, and what remains genuinely open? | summarize the closed chain and isolate the true-minimum/equality-class problem | none; the paper closes on a precise mathematical question |

## Theorem dependency order

```text
switching conjugacy
 -> (tau, alpha) coordinates
 -> finite Bloch decomposition

Q half-periodic + negative half-cell flux
 <-> tau half-antiperiodic
 <-> normalized monomial chiral involution
 -> even characteristic polynomial and 2m -> m reduction

period-eight word
 -> chiral 8 -> 4 block
 -> 4 -> 2 determinant identity
 -> P(y,c)
 -> four exact branches
 -> positive/negative finite radii
 -> twisted comparison

lift/dihedral/repetition invariance + M1--M3
 -> short-period survivor lemma
 -> exact certificate table
 -> smallest primitive period

period-eight exact phase + short recurrence
 -> period-eight trichotomy
 -> unique first sub-eight phase
```

## Deletion test

- Section 3 cannot be deleted: without it, the period-eight reduction is an
  isolated calculation and the main conceptual contribution disappears.
- Section 6 can remain only in its present compact form: it answers the local
  geometry question raised by Section 5.  Any further moment catalogue is
  deleted.
- A separate related-work section is deleted: it would break the motivation
  chain and is not supported by the JGT corpus.
- A separate computer-verification section is deleted: exact finite material
  belongs inside the theorem it closes.
- A separate negative-holonomy section is deleted: it is one phase-grid
  consequence of the same dispersion.
