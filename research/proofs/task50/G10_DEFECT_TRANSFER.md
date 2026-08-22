# Exact Gap-Ten Defect Transfer

Use the same convention as for G6, replacing the right defect lattice by

\[
Q_i=+1\iff i\ge10\text{ and }i\equiv10\pmod4.
\]

Together with the left lattice `4Z` through zero, this defines `tau` exactly
from `tau_0=1`.  With cuts at `-8` and `18`, put

\[
P_{10}(\lambda)=T_{17}(\lambda)\cdots T_{-8}(\lambda).
\]

Every entry is an integer polynomial in `lambda`, the maximum degree is 15,
and direct exact calculation gives

\[
\det P_{10}(\lambda)=1.
\]

The complete symbolic matrix and orientation data are stored in
`certificates/g10_defect_transfer.json`.
