# Task 54 Eventual-Threshold Sharpening

## Analytic tail

For the normalized cyclic tent, direct summation gives the exact translation
differences for offsets one through four. In fact, for `1<=d<=R`,

```text
S_d(R)=3(2d^2 R-d(d^2-1))/(R(2R^2+1)).
```

Thus

```text
S_1=6/(2R^2+1),
S_2=6(4R-3)/(R(2R^2+1)),
S_3=18(3R-4)/(R(2R^2+1)),
S_4=12(8R-15)/(R(2R^2+1)).
```

Using the exact path-count bounds `2,1,2,1` for
`|H_(a,a+d)|`, the IMS error is

```text
E(R)=(240R-342)/(R(2R^2+1)) <=120/R^2.
```

Moreover

```text
E(R)-E(R+1)
=6(160R^3-102R^2-262R-171)
 /(R(R+1)(2R^2+1)(2R^2+4R+3)) >0
```

for `R>=4`. This proves the infinite-tail monotonicity algebraically rather
than by a finite table.

The range-four enlarged support contains at most one interface under the
clean sufficient condition `2(R+4)<D`; the largest integer allowed by this
condition is
`R=floor((D-9)/2)`. For the explicit residue constructions,

```text
D_2=n,
D_4=n/2,
D_6=6+4 floor((2k-3)/3),  n=8k+6.
```

Exact endpoint checks at `n=240,242,244,246`, followed by residue-wise
monotonicity, prove that every even `n>=240` is a counterexample. Thus
`N_tail=240`, replacing Task 53's deliberately crude `2500`.

## Certified finite tail

For every even `48<=n<240`, use period-eight repetition in residue zero and
the balanced one-, two-, or three-G6 word in residues two, four, or six. The
holonomy is `-1` for `n=0 mod4` and `+1` for `n=2 mod4`.

For each row the certificate chooses a rational `t` satisfying

```text
t < 8-200/n^2 < rho_-(n)^2
```

and proves `tI-A^2` positive definite by exact rational sparse LDL. An
independent checker rebuilds every signing and uses a different elimination
ordering. All 96 rows pass.

Therefore every even `n>=48` has an explicit certified counterexample.
This is the proved contiguous explicit-witness threshold `N_star=48`; it is
not asserted to be the globally minimal counterexample onset.

Status: `TASK54_EVENTUAL_THRESHOLD_N_STAR_48_PROVED` /
COMPUTER_ASSISTED_PROVED.
