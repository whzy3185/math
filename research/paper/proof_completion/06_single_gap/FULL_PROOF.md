# Full Proof

## 1. Symmetry reductions

Let `(Dv)_i=(-1)^i v_i`. Direct substitution gives

```text
A_(-tau)=-D A_tau D,
A_(-tau)^2=D A_tau^2 D.                               (1)
```

Thus the two lifts have the same squared spectrum. Reflection of `Z` maps a
forward single gap to the reverse orientation and is unitary. It therefore
suffices to prove all lower bounds for the canonical forward lift with
`tau_0=1`.

For a finitely supported vector `v`, extend it by zero and compute `A_gv` on
the entire support enlarged by two sites at each end. Since `H_g=A_g^2` and
`A_g` is self-adjoint,

```text
<v,H_gv>/<v,v>=||A_gv||^2/||v||^2.                   (2)
```

If the quotient is `N/D`, the variational principle gives
`sup sigma(H_g)>=N/D`.

Put

```text
T=988671163952541/125000000000000.                    (3)
```

The certified root interval gives `T>c6+1/250`. Hence it is enough to produce
`N/D>T` in every case.

## 2. Exact witnesses for the six small gaps

Coordinates are listed in increasing order on the indicated interval `I`.
Every displayed image is obtained by the four-term formula for `A_g` and is
listed on `J=I+[-2,2]`.

### Gap 1

```text
I=[-2,3]
v=(2,0,4,4,6,5)
A_1v=(-2,2,4,2,12,15,13,10,11,-5)
D=||v||^2=97,   N=||A_1v||^2=812.
```

### Gap 2

```text
I=[-4,6]
v=(1,-1,-2,-1,-4,-5,-6,-2,1,4,2)
A_2v=(-1,0,1,0,-7,0,-14,-11,-12,-14,10,5,5,-2,2)
D=109,   N=866.
```

### Gap 3

```text
I=[-5,8]
v=(0,1,-1,-3,0,-6,-8,-6,-10,-6,-8,-6,1,-3)
A_3v=(0,-1,0,2,-2,-8,0,-17,-22,-18,-28,-18,-23,-16,
      -1,-5,-4,3)
D=393,   N=3114.
```

### Gap 5

```text
I=[-2,7]
v=(2,0,4,4,4,4,1,3,3,3)
A_5v=(-2,2,4,2,10,12,11,12,0,11,5,6,6,-3)
D=96,   N=764.
```

### Gap 7

```text
I=[-2,9]
v=(2,0,3,4,4,4,1,3,2,3,2,3)
A_7v=(-2,2,3,1,10,11,10,12,1,10,3,10,4,5,5,-3)
D=97,   N=768.
```

### Gap 8

```text
I=[-8,16]
v=(4,4,4,3,-3,3,9,1,19,22,21,22,4,16,8,12,5,6,0,-4,
   -1,1,0,1,0)
A_8v=(4,0,8,11,14,8,-7,8,26,3,53,61,59,63,9,46,19,35,
      10,21,-4,-8,-3,4,1,1,1,1,0)
D=2487,   N=19672.
```

For a row `N/D`, direct cross-multiplication against (3) uses the integer

```text
Delta(N,D)=125000000000000 N-988671163952541 D.
```

The complete calculation is:

| gap | `N/D` | raw integer `Delta(N,D)` | exact value of `N/D-T` |
|---:|---:|---:|---:|
| 1 | `812/97` | `5598897096603523` | `5598897096603523/12125000000000000` |
| 2 | `866/109` | `484843129173031` | `484843129173031/13625000000000000` |
| 3 | `3114/393` | `702232566651387` | `234077522217129/16375000000000000` |
| 5 | `764/96` | `587568260556064` | `18361508142377/375000000000000` |
| 7 | `768/97` | `98897096603523` | `98897096603523/12125000000000000` |
| 8 | `19672/2487` | `174815250030533` | `174815250030533/310875000000000000` |

All numerators and denominators in the last column are positive. Thus (2)
proves `sup sigma(H_g)>c6+1/250` for every abnormal `g<9` other than six.

## 3. One fixed witness for every `g>=9`

On `I=[-2,11]`, use

```text
v_*=(4,0,7,8,8,9,1,7,3,6,1,4,1,2),
||v_*||^2=391.                                        (4)
```

Only coefficients `tau_i` with `-4<=i<=11` enter the nonzero image. Hence the
right defect can affect the calculation only for `g=9` or `g=10`; all
`g>=11` have the same local pattern. On `J=[-4,13]`, direct calculation gives

```text
g=9:
A_gv_*=(-4,4,7,3,20,24,23,24,5,19,11,15,6,10,5,5,3,-2),
||A_gv_*||^2=3102;

g=10:
A_gv_*=(-4,4,7,3,20,24,23,24,5,19,11,15,6,10,5,5,1,-2),
||A_gv_*||^2=3094;

g>=11:
A_gv_*=(-4,4,7,3,20,24,23,24,5,19,11,15,6,10,5,5,1,2),
||A_gv_*||^2=3094.                                    (5)
```

Therefore every `g>=9` satisfies

```text
sup sigma(H_g)>=3094/391=182/23.
```

The exact comparison is the final raw cross-multiplication

```text
Delta(182,23)=10563229091557>0,
182/23-T=10563229091557/2875000000000000>0.           (6)
```

Equations (4)-(6) prove the strict uniform bound for the entire tail.

## 4. Equality, exclusion of gap four, and completion

The global G6 edge theorem gives

```text
sup sigma(H_6)=c6,
dim ker(H_6-c6)=2.                                    (7)
```

For `g=4`, the defect lattice is `4Z`, so the operator is the reference
period-eight bulk and

```text
sup sigma(H_4)=eta<c6.                                (8)
```

The six vectors in Section 2, the fixed vector in Section 3, and (7) exhaust
all positive abnormal gaps. Equations (1) and reflection transfer every
conclusion to both lifts and orientations. The smallest positive margin in
the complete comparison table is the gap-eight value

```text
174815250030533/310875000000000000.
```

Thus the endpoint is strict in every case, proving
`sup sigma(H_g)>c6+1/250` for all positive `g not in {4,6}` and completing
the theorem.
