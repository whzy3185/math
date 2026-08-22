# Target A Two-Interface Bound Status

## Exact Families

For `n=16r+4`, the symmetric two-G6 word is

\[
[6,4^{,2r-1},6,4^{,2r-1}].
\]

For `n=16r+12`, the one-cell-shifted word is

\[
[6,4^{,2r-1},6,4^{,2r+1}].
\]

Both words have an even number of quadrilateral defects, have the stated
total order, and are legal for each integer `r>=1`.  The two finite holonomies
remain the twisted closures `alpha=+1` and `alpha=-1`.

If `B(y)` is a complete target bulk cell and `D_6(y)` is the oriented G6
defect transfer, the exact two-defect monodromy has the form

\[
B(y)^L D_6(y) B(y)^{M-L}D_6'(y),
\]

up to an invertible change of cut.  The second defect transfer `D6'` records
its orientation.  Thus both propagation arcs and the finite holonomy enter
the matching equation; the positive sign of the slow multiplier alone cannot
produce the mod16 branch selection.

## Missing Uniform Estimate

The desired inequality is

\[
|R_{L,M}-c_6|\le C
\left((9/25)^L+(9/25)^{M-L}\right).
\]

The infinite G6 state and its `9/25` decay rate are proved.  What remains is
the same global finite-spectrum exclusion encountered in the single-interface
case, now for a two-arc closure.  Without it, a matching root near `c6` does
not prove that the root is the squared spectral radius.

No signed leading expansion is claimed.  The Task 49 mod16 mechanism remains
partial.

## Gate Decision

`TWO_INTERFACE_BOUND_INCOMPLETE`

`MOD16_FINE_BRANCH_MECHANISM_PARTIAL`
