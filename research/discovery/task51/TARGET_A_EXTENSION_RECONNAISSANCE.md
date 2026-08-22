# Target A Extension Reconnaissance

## Odd order

For odd `n`, legality `(-1)^(n-d)=1` forces an odd number `d` of positive-Q
sites.  Total charge `n-4d` is odd, so odd charge species such as gap3/gap5
become arithmetically elementary.  The deterministic interface atlas shows
gap3 (`q=-1`) below 8 and gap5 (`q=+1`) above 8.  A small-order minimization was
not expanded because it is a separate parity problem.

Status: `PROMISING_NEW_PARITY_PROBLEM`, outside the current theorem program.

## Nearby circulants

For `C_n(1,3)`, a scalar eigenvalue recurrence naturally has order six rather
than four and its square has a wider local stencil.  No comparably short
periodic cancellation cell was identified at Level 0.  The portability route
was stopped before search.

Status: `WEAK_NOT_APPLICABLE_WITH_REASON`.

## Continuous magnetic relaxation

Allowing arbitrary unit phases changes a finite sign optimization into a
continuous magnetic variational problem and requires a new gauge quotient and
Hessian analysis.  No claim follows from the signed data.

Status: `NOT_APPLICABLE_WITH_REASON: formulation broadens beyond Task 51`.
