# Physical G6 Matching Condition

Fix the tree gauge used in Tasks 50-52. The forward G6 interface has positive
`Q` defects at `4Z` on the left through zero and at `6+4Z` on the right from
six onward. Its left bulk sector is `B_0`; the exact translation-charge rule
gives the right sector `B_2` because `6-4=2 mod 4`.

Take the left bulk cell `[-16,-8)`, defect cut `[-8,14)`, and right bulk cell
`[14,22)`. Let `U_L(y)` be the two-dimensional unstable plane of the left
cell, `S_R(y)` the stable plane of the right cell, and `D_6(y)` the ordered
defect transfer from `-8` to `14`. The unsquared physical equation is

```text
(Lambda^2 D_6(y) U_L(y)) wedge S_R(y)=0.
```

Equivalently, any oriented bases `u1,u2` and `s1,s2` satisfy

```text
det[D_6 u1,D_6 u2,s1,s2]=0.
```

Changing a basis multiplies this determinant by a nonzero determinant and
does not change its zero set. The Grassmann atlas therefore supplies a
basis-free condition over the whole future exclusion interval.

Reflection is the unitary permutation `x_i -> x_{-i}` followed, when needed,
by a diagonal tree-gauge. It reverses the cut and exchanges the left
unstable and right stable planes. The exterior pairing changes by a nonzero
orientation sign, so forward and reflected G6 interfaces have identical
spectra. Simultaneously translating both bulk sectors is likewise a
permutation conjugacy.

Elimination requires four operations that may create extraneous branches:
cofactor sections can vanish, denominators are cleared, `lambda` is squared,
and the nonphysical root of the `P` equation is retained. Consequently a
degree-ten resultant zero is only a candidate. In particular the root near
`8.080985802104273` is physical for gap2 but not for G6; its G6 unsquared
matching determinant is rigorously nonzero.

Status: physical branch globally defined on `[c6_upper,16]`.
