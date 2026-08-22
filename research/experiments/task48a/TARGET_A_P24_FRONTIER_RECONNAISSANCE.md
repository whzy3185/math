# Target A p<=24 Exact Frontier Reconnaissance

The Task 47 survivor and handled sets were subtracted mechanically.  The
remaining counts are exactly 11 at period 22, 14 at period 23, and 34 at
period 24.  There are no duplicates, previously consumed states, or canonical
mismatches.

All 59 remaining states have exact integer endpoint Rayleigh certificates
strictly above `1561/200`, which is itself strictly above `eta`.  Rebuilding
the full partition gives 369,916 moment-excluded orbits, 183 certified strict
survivors, one equality survivor, no lower class, and no unresolved class.

| Period | Closed | Moment class | Strict certificate | Equality | Unresolved |
|---:|:---:|---:|---:|---:|---:|
| 17 | YES | 2,049 | 7 | 0 | 0 |
| 18 | YES | 3,904 | 10 | 0 | 0 |
| 19 | YES | 7,145 | 10 | 0 | 0 |
| 20 | YES | 13,629 | 19 | 0 | 0 |
| 21 | YES | 25,463 | 19 | 0 | 0 |
| 22 | YES | 48,703 | 31 | 0 | 0 |
| 23 | YES | 92,171 | 34 | 0 | 0 |
| 24 | YES | 176,852 | 53 | 1 | 0 |

The unique equality is displayed period 24 with primitive Q period 4 and
primitive tau period 8: the three-cell repetition of the existing period-8
target.  Thus `P24_EXACT_FRONTIER_CLOSED` and the bounded-optimality extension
is a theorem candidate.  The formal theorem remains unchanged.
