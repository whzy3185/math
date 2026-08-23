# Single-G6 Spectral Isolation

Let `H6` be either orientation of the infinite G6 squared operator. Then `c6`
is the only physical discrete eigenvalue in `(eta,c6]`, with Riesz rank
two. Task 53, supplemented by the exact anticommuting symmetry recorded in
Task 55, proves that no spectrum lies above `c6`.

Set `delta6=1/100`. The exact rational chain

```text
c6_lower-1/100 > 1561/200 > eta
```

puts `[c6-delta6,c6)` strictly above the essential bulk edge. The complete
candidate classification excludes every physical level there. Therefore

```text
sigma(H6)\{c6} intersect [c6-delta6,c6+delta6] = empty.
```

Reflection is a unitary equivalence, so the statement holds for both G6
orientations.

Status: `TASK54_GATE_A_PASS` / COMPUTER_ASSISTED_PROVED.
