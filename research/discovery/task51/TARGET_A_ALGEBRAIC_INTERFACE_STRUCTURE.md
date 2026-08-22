# Target A Algebraic Interface Structure

The G6 constant now has an exact, irreducible degree-ten polynomial derived
from the transfer/Evans equations, not accepted from PSLQ.  The exact theorem
and elimination are in `research/proofs/task51/TARGET_A_C6_ALGEBRAIC_THEOREM.md`.

The two stable bulk roots admit symmetric coordinates `(S,P)`, reducing the
matching algebra to one quartic relation in `P` plus one Evans equation.  This
is the useful general charge algebraic template.

For G10, the exact transfer and symmetric-Evans construction are available,
but Task 48A found no validated low-degree candidate.  A larger unbounded
resultant was stopped by rule.  Inserting eight sites relates charge-transfer
matrices through one bulk monodromy, so a recurrence in `g mod 8` is promising;
it has not yet been converted into a closed Evans recurrence.  Exterior traces
similarly give useful word coordinates without a closed low-dimensional trace
map.

| Item | Status |
|---|---|
| c6 polynomial | PROVED, irreducible degree 10 |
| c10 polynomial | OPEN_SYMBOLIC_GROWTH_STOP |
| General charge recurrence | PROMISING |
| Unified charge algebraic family | OPEN |
| Trace map | PROMISING_NOT_CLOSED |
