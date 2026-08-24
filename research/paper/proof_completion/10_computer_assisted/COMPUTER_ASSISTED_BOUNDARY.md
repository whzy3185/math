# Final Computer-Assisted Proof Boundary

## Governing rule

Every machine-assisted statement is presented in the order

```text
mathematical reduction
  -> finite exact object
  -> machine verification
  -> mathematical consequence.
```

A program status string is not evidence by itself. An accepted theorem must
identify the finite domain, prove coverage of that domain, use an exact or
certified accepting arithmetic, and state the independence boundary of its
checker.

## Types of machine assistance

| Type | Mathematical role | Endpoint arithmetic |
|---|---|---|
| Finite exhaustive enumeration | consume every switching/orbit/window state in a proved finite domain | integers and exact set accounting |
| Exact rational arithmetic | Rayleigh quotients, Schur/IMS constants, threshold comparisons | integer cross-multiplication or `Fraction` |
| Sturm/root isolation | select and order real algebraic roots | integer polynomials and rational isolating intervals |
| Interval arithmetic | certify Evans signs, derivatives, pivots, and stable branches | outward exact rational intervals |
| Symbolic determinant identity | transfer, resultant, and matching equations | polynomial identities over exact domains |
| LDL/Bareiss | prove a full finite matrix inequality | exact rational or fraction-free pivots |
| Finite graph reachability | de Bruijn closure, parity lift, canonical terminals | exact states, edges, and destructive accounting |
| Hash verification | bind a checker to immutable source artifacts | SHA-256; provenance only, never a spectral argument |

## Logical endpoint policy

Floating point may locate roots or propose integer witness vectors. It cannot
accept a theorem endpoint. The accepted endpoint is always one of:

- a strict integer/rational inequality;
- a sign-stable rational interval;
- a Sturm count in a rational interval;
- a complete exact state partition;
- a full exact LDL/Bareiss certificate.

If a displayed decimal is present, it is explanatory and follows an exact
definition.

## Main theorem families

### Complete even-order truth classification

The domain is partitioned into finite exact orders `8<=n<=46`, a 96-order
finite LDL bridge `48<=n<240`, and an analytic IMS tail `n>=240`. Enumeration
proves the finite no-counterexample regions; exact matrix inequalities prove
the counterexample orders. The parts are disjoint and exhaustive.

### Elementary G6 edge

The algebraic eliminant gives only a finite candidate list. The actual
theorem also uses a global Grassmann chart cover, exact root isolation, and
unsquared physical matching to accept `c6` and reject every higher candidate.
The resultant alone is never used as a physical-spectrum certificate.

### Separated G6 cluster

The computer-assisted inputs are finite rational interval bounds on the
period-eight monodromy and the certified single-interface edge/isolation.
The `2r` quasimode count, complement gap, and Feshbach estimate then follow by
finite-dimensional analysis. The checker rejects all legacy exact-`r`
contracts.

### Abnormal single gaps

The six small gaps and the three locality classes for `g>=9` are closed by
exact integer Rayleigh quotients. The all-`g` step is mathematical locality,
not a finite scan to a large cutoff. The uniform `1/250` corollary is seven
integer cross-multiplications against the certified upper endpoint for `c6`.

### Bounded periodic frontier

Only periods at most 24 are finite by hypothesis. Exact orbit accounting and
Rayleigh/moment certificates consume every record. Periods 25 and 26 are not
silently included.

## Evidence labels

- `PROVED`: a human proof is complete; machine checks are optional audits.
- `COMPUTER_ASSISTED_PROVED`: a finite exact/interval lemma is logically
  essential and has the stated checker boundary.
- `EXACT_FINITE_READ_ONLY`: arithmetic is exact but a publication-grade
  producer/checker or completeness bridge is missing.
- `HIGH_PRECISION`: numerical evidence only.
- `FALSIFIED` or `WITHDRAWN`: must not be a dependency.
- `OPEN`: no theorem.
