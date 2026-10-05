# Independent audit of the residue-six finite completion

Date: 2026-10-05. Exact graph replay and mathematical exposition audit: **PASS**.

## Audited result

For every integer k>=6, let N=8k+6 and

    j_0=floor(k/3), j_1=floor((k+1)/3), j_2=floor((k+2)/3).

Concatenate the three triangle-sign cells

    w_j=(1,1,-1,1,-1,-1,1,-1)^j||(1,-1),

give every step-one edge sign +1, and use the resulting triangle word as the step-two edge signs. The corresponding real signed adjacency satisfies

    rho(A_N)^2 <198/25 <rho_tw(N)^2.

The result concerns an explicit family. It does not determine global minima, classify minimizing signings, or establish the smaller-order equality cases. It is finite-certificate-assisted, not Lean-formalized. The proof does not depend on numerical eigenvalues or an interface-mode count.

The reviewed source is ../R6_FINITE_COMPLETION.md. The uniform unequal-cell theorem and its dependencies were already independently audited; the new obligations here are the construction, exact finite completion, threshold coverage and benchmark comparison.

## Construction and floor identities

Write k=3q+s, 0<=s<3. The three displayed floor values are, in nondecreasing order,

    q repeated (3-s) times, followed by q+1 repeated s times.

They sum to k, differ by at most one, and are at least two when k>=6. Consequently the three legal lengths 8j_i+2 sum to N=8k+6 and differ by at most eight. The full graph has exactly the simple cycle-square support: N>=54, all step-one/step-two edge pairs are distinct, and each vertex has degree four. All step-one signs are positive, so the Hamilton holonomy is +1.

Within each cell, the positive quadrilateral fluxes are at local positions 0,4,...,8j-4. Their successive cyclic gaps are four except for exactly three gaps of six, one at each cell boundary. There are 2k positive-flux positions. The independent implementation builds this quadrilateral-flux pattern first, recovers the triangle signs from it, and then verifies that the recovered word equals the stated concatenation.

For k divisible by three the cells are equal. Otherwise this construction need not be the older balanced-gap signing. The finite graphs were reconstructed directly from the new specification; no certificate for another placement was substituted.

## Analytic coverage and finite bases

The audited unequal-cell theorem gives squared radius below 198/25 for any number of the prescribed legal cells, with either holonomy, provided every cell has length at least 106.

For k>=39,

    min j_i=floor(k/3)>=13,
    min h_i>=8*13+2=106.

Thus its hypotheses hold for all three cells and the positive holonomy. The first analytic order is N=8*39+6=318.

The remaining integers are exactly k=6,...,38, hence exactly 33 graph orders N=54,62,...,310. All 33 matrices pass an independently written rational LDL test. The final finite order 310 and first analytic order 318 are consecutive admissible orders, so there is no uncovered case.

The independent checker forms the normalized matrix (198/25)I-A^2 from integer two-edge walks and uses natural vertex order. The primary verifier instead uses the denominator-cleared matrix 198I-25A^2 and an interior-first ordering. Every independent pivot is strictly positive. The scalar Schur criterion and the spectral theorem therefore prove rho(A_N)^2<198/25 at every finite base.

The complete mathematical conclusion comes from these finite certificates plus the uniform theorem, not from extrapolating the test range.

## Exact twisted-benchmark comparison

Using cos(x)>1-x^2/2 for x>0 and pi^2<10,

    rho_tw(N)^2
      =4+2cos(2pi/N)+2cos(4pi/N)
      >8-200/N^2.

For N>=54 this is at least

    8-200/54^2=5782/729.

The exact difference from the witness cap is

    5782/729-198/25=208/18225>0.

Thus the strict comparison holds at the first graph and throughout the full range. The older target 5782/729 has not been enlarged.

## The all-even witness corollary

The consequence for every even N>=48 is valid at the stated witness-only scope:

- N congruent to 0 modulo 8 starts at 48 and uses the already audited period-eight family
- Residue 2 starts at 50 and uses the audited R2 family
- Residue 4 starts at 52 and uses the audited changed R4 family
- Residue 6 starts at 54 and uses the present theorem

For clarity, the first branch can be compared without relying on an unstated numerical gap. Its positive-holonomy squared radius is 4+sqrt(10+2sqrt(5)). Since sqrt(5)<5/2 and sqrt(15)<39/10, this is below 79/10. Meanwhile 8-200/48^2>79/10, and the benchmark lower bound increases with N. Thus the period-eight witness beats the benchmark throughout its part of this range. The other branches retain their previously proved endpoint comparisons.

This completes only the failure-of-optimality direction for these orders. It does not provide any lower bound over all signings at smaller orders or identify the actual optimum after the twisted signing fails.

## Independent implementation and results

The standalone replay_r6.py imports no primary verifier or previous audit module. It uses:

1. Quotient/remainder cell allocation, independently matched to the floor formulas
2. Quadrilateral-gap construction followed by triangle-sign recovery
3. Fresh edge-set reconstruction and support/degree checks
4. Sparse upper-triangle exact Schur elimination in natural order
5. Comparison of cell/gap metadata with the primary file, without using its positivity flags
6. Exact endpoint, coverage and all-even-corollary checks

The final run passes 139 checks and all 33 full-graph positivity tests. Results are in independent_replay.json; verification_stdout.txt is the actual execution output. The result includes the independently produced rational pivot-list hashes, counts and endpoint pivots. The checks use exact Python integers and Fraction arithmetic throughout acceptance; elapsed runtime is diagnostic only.

Reproduce with:

    python replay_r6.py

Only Python's standard library is required. Source hashes and artifact checksums accompany this report. No frozen sibling proof or certificate was altered.

No blocking mathematical discrepancy was found.
