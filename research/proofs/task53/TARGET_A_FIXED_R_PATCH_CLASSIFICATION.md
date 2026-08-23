# Fixed-r Patch Classification

Consider a legal cyclic gap word made from gaps four and exactly `r` gaps
six, where `r=1,2,3`. Let `D` be the minimum cyclic site distance between
the G6 cores, with `D=n` for one core, and put

```text
R=floor((D-9)/4).
```

For `D>=26`, `2(R+4)<D`. Hence the range-four enlargement of every IMS
support contains at most one non-four gap.

If it contains none, all consecutive defect gaps are four. The local `Q`
word is one of the four translated period-eight sectors `B_s`. Translation
by `-s`, followed by the diagonal tree-gauge, maps it to the canonical pure
bulk model.

If it contains one gap six, translate its left endpoint to zero. Reading the
oriented arc gives the canonical forward G6 word or its reversal. In the
latter case apply `i -> -i`; a final diagonal gauge restores the canonical
tree signs. These are respectively the forward and reflected G6 models.

The Hamilton holonomy `alpha` is represented by one step-one cut. On every
proper arc, multiply vertices successively by diagonal signs to move that
cut outside the range-four enlarged support. This operation is unitary and
does not change `Q`. Thus the classification is identical for
`alpha=+1,-1`, including supports crossing the originally displayed cut.
The same explicit gauge handles cyclic wraparound.

No fourth class exists: the range-four margin permits zero or one non-four
gap, and the two orientations of the latter are related exactly as above.
The argument applies separately to `r=1,2,3` and does not infer a local model
from numerical spectra.

Status: `GATE_B2_PASS` / PROVED.
