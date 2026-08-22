# Target A Finite Phase-Slip Report

Date: 2026-08-22

Status: **FINITE EXPERIMENT COMPLETE; NEW EXACT INSTANCES; NO THEOREM CHANGE**

## Protocol

The experiment tests all 49 even orders `32<=n<=128` in residue classes
0, 2, 4, and 6 modulo 8. Six deterministic near-period-eight seed mechanisms
are evaluated for both holonomies, followed by legality-preserving pair moves
through Hamming radius four. The complete best-by-order table is stored in
`finite_phase_slips/best_by_n.csv`.

For every numerical candidate below the conjectured threshold, an exact
Bareiss-Sylvester certificate proves a rational matrix inequality
`rho(A)^2<bound`, and a separate elementary rational lower bound proves
`bound<rho_-(n)^2`. Thus certification does not depend on floating spectral
accuracy.

## Results

| residue modulo 8 | certified orders | count |
|:---:|:---|---:|
| 0 | `32,40,...,128` | 13 |
| 2 | `50,58,...,122` | 10 |
| 4 | `52,68,84,100,116` | 5 |
| 6 | `94,102,110,118,126` | 5 |

There are 33 numerical candidates and all 33 are exactly certified. Twenty
lie outside `8Z`; the smallest is `n=50`. Sixteen certified orders are
divisible by neither 8 nor 10, beginning at `n=52`.

The first newly informative example beyond the already known `8Z` and
period-10 directions is `n=52`, with two gap-6 phase slips, `alpha=-1`, and
canonical `Q` word

```text
1000100010001000100010000010001000100010001000100000.
```

Its JSON certificate records a strict rational upper bound on `rho(A)^2`, a
strict rational lower bound on `rho_-(52)^2`, and their positive exact margin.

## Interpretation

The finite data provide a strong **FINITE FAMILY EXTENSION CANDIDATE** signal.
The three nonzero-residue sequences have simple gap descriptions and stable
holonomy choices. They are substantially more structured than random local
minima. Nevertheless, only the displayed finite instances are proved here.
No residue-class infinite theorem is asserted, and failed smaller orders in
the residue-4 and residue-6 classes caution against extrapolating from a short
tail.

The positive controls at every multiple of eight are recovered, satisfying
the required sanity check. Families B4 and B5 do not produce a certified best
order in this range and are recorded as failed primary families, although
they remain part of the deterministic robustness search.

## Evidence Labels

- `PROVED CURRENT THEOREM`: the period-eight controls already covered by the
  existing theorem.
- `NEW EXACT CANDIDATE`: each newly stored finite certificate outside the
  current period-eight theorem, with overlap against older period-10 artifacts
  explicitly disclosed.
- `NUMERICAL EVIDENCE`: best rows without a negative threshold gap.
- `FAILED FAMILY`: B4/B5 as primary winning mechanisms in this scan.

The formal manuscript, abstract, discussion, and theorem statements are not
modified by this report.
