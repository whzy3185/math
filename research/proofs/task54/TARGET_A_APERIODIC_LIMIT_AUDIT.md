# Aperiodic Limit Audit

Pointed compactness does not imply periodicity. The cyclic product constraint,
holonomy, and total charge modulo eight can all be repaired outside any fixed
rooted window, so they impose no effective restriction on an arbitrary
bi-infinite pointed limit.

The existing 105-state, 164-edge overlap grammar branches and does not force
every limit into a bulk-plus-finitely-many-G6 language. Likewise, complete
periodic classification through period 24 controls no aperiodic word.

The current common-liminf blockers are therefore:

- `TIGHT_CLUSTER_BLOCKER`: a bounded but non-elementary charge cluster may
  survive and is not covered by separated-G6 theory;
- `DICHOTOMY_BLOCKER`: separated components need not individually be G6 and
  may carry cancelling signed charges;
- `VANISHING_BLOCKER`: all ordinary local limits may be pure bulk while
  globally sparse charge escapes;
- `APERIODIC_LIMIT_BLOCKER`: a positive-complexity limit need not be periodic
  or a finite interface.

No unrestricted statement
`liminf m_(8k+r)^2>=c6` follows until these cases receive a general spectral
cost theorem.

Status: OPEN for common liminf; blocker classification PROVED.
