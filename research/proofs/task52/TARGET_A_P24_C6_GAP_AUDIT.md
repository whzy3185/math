# p<=24 Audit Relative to c6

The Task 51 atlas contains 13 primitive numerical sub-eight phases: one
period-eight target and 12 non-target phases. None of the 12 displayed
non-target values is below `c6`.

The closest non-target is the period-ten `[4,6]` phase. Its exact Floquet
polynomial is `P(y,c)`, `c in [-2,2]`. At `c=-2`, exact rational evaluation
gives

```text
P(c6,-2)<0,  P(8,-2)>0.
```

Moreover `partial P/partial y` is positive at the lower endpoint of the c6
interval and has no root between that endpoint and 8, by exact Sturm count.
Hence this Bloch block has a root strictly in `(c6,8)`, proving that the
period-ten band edge is strictly above `c6`.

The other 11 comparisons remain deterministic numerical atlas evidence.
This audit is bounded to primitive periods at most 24 and is not an
arbitrary-period crystallization theorem.

Artifact: `../../experiments/task52/p24_c6_audit.json`.

Status: `PERIOD10_BAND_EDGE_GT_C6_PROVED_P24_REMAINDER_EXPERIMENTAL`.
