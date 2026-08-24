# Task 58 Novelty Positioning

Status: `VERIFIED_FOR_BLUEPRINT`; search date 2026-08-24.

## Direct Answer

The closest and only high-risk direct prior work located is Suvagiya's 2026
preprint *Signed circulants at the Ramanujan bound* (`arXiv:2607.18334`). It
studies the same fixed graphs `C_n(1,2)=C_n^2`, the same minimization over all
edge signings, the same twisted candidate and value `rho_-(n)`, and formulates
the all-even-order assertion as Conjecture 3.

The present work must therefore be positioned as the **complete resolution
and disproof of that conjecture**, not as the introduction of the problem,
candidate, flux coordinates, or twisted spectral formula.

## Answers To The Required Questions

### 1. Is there a previous complete study of the minimum spectral radius over all signings of fixed `C_n^2`?

No second complete study was located in the verified search. The direct
preprint proves the candidate formula and finite checks through order 18, then
states the all-order conjecture. Target A determines the exact validity and
failure sets. This negative search is evidence for cautious novelty wording,
not a proof of global nonexistence.

### 2. Is there a corresponding extremal classification for signed powers of cycles?

No adjacency-spectral-radius classification over all signings of cycle powers
was located. Existing neighbors concern signed cycles themselves, gain-cycle
spectra, unsigned cycle-square spectra, or non-spectral parity parameters of
cycle powers. These prevent broad “first spectral study of cycle powers”
claims but do not duplicate Target A.

### 3. What is different about the complete even-order classification?

The direct preprint conjectures equality at every even order. Target A proves
instead the nonmonotone exact pattern

```text
failure exactly at n=32, n=40, and every even n>=48,
equality at every other even n>=8.
```

It combines explicit candidate attainment, exact finite lower/strict
classification, an analytic phase-slip tail, and a finite exact bridge that
places the continuous onset at 48.

### 4. Does the phase-slip framework have a direct graph-theoretic predecessor?

No direct predecessor for the G6 single-gap hierarchy or separated-defect
mechanism was located. Periodic magnetic/Floquet operators, flux trace
formulas, and Lieb's flux-phase theorem are conceptual/methodological
background only. They do not imply the single-gap optimality theorem or the
finite-ring residue construction. The manuscript should not claim “the first
phase-slip theorem in signed graphs”; it should simply present the mechanism
and state the exact scope.

### 5. Is there a direct neighbor for the single-gap hierarchy?

No verified paper was found that compares all positive single-gap interfaces
over this period-eight bulk and proves the unique G6 minimizer with a uniform
`1/250` separation. Signed unicyclic/bicyclic extremal classifications are
nearby in genre but vary the underlying graph and do not use this interface
model.

### 6. How should the computer-assisted component be described?

It is proof infrastructure, not the novelty claim. The manuscript should say
that mathematical reductions leave finite exact objects, independently
verified with algebraic, integer, interval, or rational arithmetic. It should
distinguish exhaustive decisions, explicit witnesses, and analytic
propagation. It should not advertise test counts, JSON, hashes, or software
engineering in the main narrative.

### 7. May the Introduction say “we are not aware of ...”?

Only with a narrow object and preferably a dated or “to the best of our
knowledge” qualification. The safe sentence is:

> To the best of our knowledge, no previous work gives an all-order
> classification of the minimizing behavior over all real edge signings of
> the fixed circulant family `C_n(1,2)`.

This sentence must follow explicit acknowledgment of Suvagiya's preprint and
must not be expanded to signed graphs, signed cycles, cycle powers, spectral
extremal graph theory, or computer-assisted classifications generally.

## Recommended Introduction Positioning

Use wording of the following form:

> Suvagiya identified four distinguished switching classes on `C_n(1,2)`,
> computed the spectra of the two twisted classes, verified their global
> optimality through order 18, and conjectured optimality for every even
> order. We determine the exact truth set of that conjecture: the twisted
> signing fails to minimize precisely at orders 32 and 40 and at every even
> order at least 48.

Then place the work in three broader contexts:

1. the fixed-graph signature-minimization problem of Belardo et al.;
2. general signing/2-lift bounds of Bilu–Linial and MSS;
3. signed spectral extremal classifications where the underlying graph may
   vary.

JGT complete-classification and exhaustive-generation papers may guide proof
presentation, but they are not evidence for novelty.

## Safe Claims

- “We resolve and disprove Conjecture 3 of Suvagiya.”
- “We determine exactly when the distinguished twisted signing is globally
  minimizing.”
- “The problem is a concrete instance of the fixed-graph signature-minimization
  problem formulated by Belardo et al.”
- “The classification is accompanied by a structural explanation through a
  period-eight bulk and elementary single-gap interfaces.”
- “The finite verification closes explicitly reduced finite exact objects.”

## Claims To Avoid

- “We introduce spectral-radius minimization for signed `C_n^2`.”
- “We first derive the twisted signing spectrum.”
- “This is the first signed spectral-radius extremal classification.”
- “No one has studied signed powers of cycles.”
- “We prove Conjecture 3.” The conjecture is false; it is resolved and
  disproved.
- “Phase slips have no precedent.”
- “Lieb's theorem applies to `C_n^2`.”
- “MSS solve the two-sided signing problem for every regular graph.”
- “The computation itself is the novelty.”

## Novelty-Risk Summary

| Component | Risk | Positioning response |
|---|---|---|
| Same graph/object/candidate as `arXiv:2607.18334` | HIGH | Name it first and frame Target A as the complete resolution/disproof. |
| General fixed-graph signing minimization | MEDIUM | Cite the survey problem; do not claim to originate the program. |
| Parity/flux coordinates | MEDIUM | Credit the direct preprint and broader parity/flux background. |
| Twisted Fourier spectrum | LOW–MEDIUM | Treat as known input/candidate attainment, not headline novelty. |
| Complete all-order truth set | LOW direct duplication risk | Make this the headline mathematical novelty. |
| G6/single-gap hierarchy | LOW direct duplication risk | Present as the structural contribution, with scope kept exact. |
| Computer-assisted closure | MEDIUM methodological precedent | Disclose rigorously, but do not market as novelty. |

## Watchlist

The 2025 Waterloo seminar “Symmetric and Skew-Symmetric Signing for Graphs”
concerns minimum spectral radius among signings of a fixed graph, but no
public theorem paper was located. Recheck this item immediately before
submission. Also rerun targeted searches for `C_n(1,2)`, `cycle square`, and
`signed circulant minimum spectral radius` at the final submission audit.
