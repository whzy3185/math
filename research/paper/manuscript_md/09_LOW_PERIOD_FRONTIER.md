# 8. The Low-Period Spectral Frontier

We prove Theorem F by combining complete orbit enumeration with a compressed
set of exact spectral exclusions. The theorem concerns phases of primitive
Hamilton-gauge period at most 16; it does not extrapolate beyond that domain.

## 8.1 Complete phase space

For each displayed cell length `1<=p<=16`, consider the legal flux words

```text
Q in {+1,-1}^p,       product_i Q_i=1,                          (8.1)
```

modulo rotations and reflections. Explicit orbit partition and the independent
Burnside calculation of Appendix A give the counts

```text
1,2,2,4,4,8,9,18,23,44,63,122,190,362,612,1162,                (8.2)
```

whose sum is 2,626. Every periodic phase of primitive `tau` period at most 16
appears in the list when written in its primitive cell. Translation,
reflection, global negation, and cell repetition have the spectral
equivalences proved in Lemmas 2.1-2.2.

## 8.2 Exact exclusion scheme

For every representative compute the moments (2.9). Lemma 2.3 supplies the
valid implication

```text
F_k>0 ==> R(Q)>8>eta.                                            (8.3)
```

An adaptive exact closed-walk calculation through `F_64` finds a first
positive excess for 2,611 representatives. The first-positive indices range
from 1 to 64; in particular, two near-barrier classes are first detected only
at `F_48` and `F_64`. This calculation uses integer closed-walk sums, so the
sign of every excess is exact.

Fifteen representatives remain. Eight are displayed even-period repetitions
of the all-negative phase. Equation (6.1) proves `R=8>eta` for all of them.
Two are

```text
p=8:  Q=00010001,
p=16: Q=0001000100010001,                                      (8.4)
```

where zero denotes negative flux and one positive flux. Lemma 2.2 shows that
the second row is the doubled-cell representation of the first, not a second
phase; Section 5 gives their common value `R=eta`.

The remaining five representatives are

| `p` | canonical `Q` |
|---:|---|
| 10 | `0000010001` |
| 12 | `000000010001` |
| 14 | `00000000010001` |
| 14 | `00010010001001` |
| 16 | `0000000000010001` |

For each row choose `z in {+1,-1}` and a stored nonzero integer vector `v`.
Let `H=H_Q(z)` and

```text
r=(v^T H^2 v)/(v^T v).                                         (8.5)
```

All arithmetic in (8.5) is integral before the final rational division. The
five certificates first verify `r>4`. Put

```text
u=((r-4)^2-10)/2.
```

They then verify `u>0` and `u^2>5`. Since `r-4>0`, these inequalities select
the positive square-root branch and give

```text
(r-4)^2>10+2sqrt(5),
r>4+sqrt(10+2sqrt(5))=eta.                                     (8.6)
```

The condition `r>4` is indispensable: the two inequalities involving `u`
alone can also hold on the lower branch. Rayleigh's principle and (8.5)-(8.6)
give `R(Q)>=r>eta` for each residual representative.

## 8.3 Completeness accounting

The exact partition is

```text
2611  moment-detected representatives,
   8  repeated all-negative representatives,
   5  endpoint-certified residual competitors,
   2  displayed target representations,
----
2626  total representatives.                                   (8.7)
```

The sets in (8.7) are disjoint, and Appendix A proves that the 2,626
representatives are the full legal orbit space. Every non-target phase in the
domain therefore has `R(Q)>eta`, while the two target rows are one primitive
period-eight phase with `R(Q)=eta`. This proves Theorem F. `square`

The nearest observed competitor occurs at period ten, but numerical ordering
within a non-target period is not part of the theorem. What is proved exactly
is the strict comparison of every competitor with `eta`.
