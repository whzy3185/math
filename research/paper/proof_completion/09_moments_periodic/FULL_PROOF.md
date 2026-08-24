# Full Proof: General Moments and the Period-24 Frontier

## 1. The local operator and closed walks

[APPENDIX_REQUIRED]

In the Hamilton-cycle gauge,

```text
(A_tau x)_i=x_(i-1)+x_(i+1)
             +tau_(i-2)x_(i-2)+tau_i x_(i+2).          (4)
```

A step of length one has weight one. A step `+2` from `j` has weight
`tau_j`, and a step `-2` from `j` has weight `tau_(j-2)`. The trace of
`A_tau^(2k)` counts closed step words of length `2k` with these weights.

For a closed word, cancel repeated `tau` factors modulo two. If the remaining
indices are

```text
r_1<r_2<...<r_(2s),
```

then

```text
product_j tau_(r_j)
 =product_(h=1)^s product_(i=r_(2h-1))^(r_(2h)-1) Q_i. (5)
```

Thus every closed-walk weight is a translation of a finite `Q` monomial.
The argument is on the infinite lattice and remains valid after imposing any
period; coincident residues are automatically combined in the cyclic sum.

## 2. Exact moment identities

[APPENDIX_REQUIRED]

There are respectively 4, 36, and 430 closed step words of lengths 2, 4,
and 6. Collecting (5) up to translation gives

```text
length 2:  4,
length 4:  28+8Q_i,
length 6:  238+156Q_i+24Q_iQ_(i+1)+12Q_iQ_(i+2).
```

After summing over the `p` starting positions,

```text
M_1=4p,
M_2=28p+8 sum_i Q_i,
M_3=238p+156 sum_i Q_i
         +24 sum_i Q_iQ_(i+1)+12 sum_i Q_iQ_(i+2).    (6)
```

Let `I_i=(1+Q_i)/2`. Then `d=sum I_i`,
`a=sum I_iI_(i+1)`, and `b=sum I_iI_(i+2)`. Substitution in (6) proves

```text
M_1=4p,
M_2=20p+16d,
M_3=118p+168d+96a+48b.
```

## 3. The eight-barrier implication

[APPENDIX_REQUIRED]

Constant-term extraction is normalized Bloch averaging. If
`lambda_j(theta)` are the Hermitian fiber eigenvalues, then

```text
M_k=(1/(2pi)) integral sum_j lambda_j(theta)^(2k) dtheta.
```

Under `R(Q)<=8`, set `y_j=lambda_j^2`; then `0<=y_j<=8` and
`y_j^(k+1)<=8y_j^k`. Therefore `M_(k+1)<=8M_k`. The first two excesses are

```text
F_1=M_2-8M_1=16d-12p,
F_2=M_3-8M_2=-42p+40d+96a+48b.
```

Their nonpositivity proves (2). Only the contrapositive is used: a positive
excess proves `R(Q)>8`. A nonpositive excess supplies no upper bound.

## 4. Exact finite phase space through period 24

[APPENDIX_REQUIRED]

For a fixed cell length `p`, the lift condition is `product Q=1`, leaving
`2^(p-1)` words. Translation and reflection act through the finite dihedral
group. A canonical representative is chosen for every orbit. Primitive
`Q` and `tau` periods are recomputed from the words; repeated cells are
identified by primitive normalization, and their Bloch fibers are related by
zone folding. Global `tau` negation does not change the infinite spectral
radius.

For `p<=16`, direct orbit enumeration and Burnside counting both give 2,626
records. Their exact partition relative to `c6` is

```text
1,787  moment exclusions with R(Q)>8>c6,
  832  inherited exact Rayleigh witnesses with quotient >c6,
    5  strengthened exact Rayleigh witnesses with quotient >c6,
    2  repeated-cell records of the reference phase.
```

For `17<=p<=24`, the complete closures contain 370,100 dihedral orbits:

```text
369,916  exact moment exclusions,
    183  exact integer Rayleigh witnesses above c6,
      1  reference-phase repetition,
      0  unresolved records.
```

The period-by-period orbit counts are

```text
p=17:   2,056     p=18:   3,914
p=19:   7,155     p=20:  13,648
p=21:  25,482     p=22:  48,734
p=23:  92,205     p=24: 176,906.
```

Each moment exclusion uses the proved implication `F_k>0 => R(Q)>8`.
Each endpoint exclusion stores a nonzero Gaussian-integer or integer vector
`v` and verifies exactly that

```text
||A_Q(z)v||^2/||v||^2 > c6_upper > c6
```

at `z in {1,-1,i,-i}`. Rayleigh's principle then gives `R(Q)>c6`.
Floating eigensolvers may propose `z` and `v`, but do not accept a record.

The three target cell records reduce to one primitive period-eight phase,
whose exact edge is `eta<c6`. All non-target records are strictly excluded,
which proves the bounded frontier theorem.

## 5. Why no case is lost

[APPENDIX_REQUIRED]

Soundness is immediate: every accepted orbit representative comes from a
legal `Q` word and every exclusion is a valid spectral lower bound.

Completeness has four parts.

1. The product constraint enumerates every periodic lift.
2. Dihedral canonicalization selects exactly one record per translation and
   reflection orbit; Burnside or independent bracelet counts verify the
   totals.
3. Primitive normalization and zone folding identify repetitions without
   removing any genuinely different infinite phase.
4. Destructive accounting partitions every canonical record into exactly one
   of moment exclusion, endpoint exclusion, or target repetition, with zero
   remainder.

Thus the finite computation covers the theorem's whole bounded domain.

## 6. Material retained or omitted

[MAIN_TEXT_REQUIRED]

`M_1,M_2,M_3` are the only moment formulas retained as mathematical
statements because they expose defect density and the first local clusters.
The exact `M_4,M_5,M_6` expansions are not used symbolically by the final
main proof. Higher moments remain legitimate finite filters inside the
bounded certificate, but their long expansions are `REPRODUCIBILITY_ONLY`.

The `p<=24` theorem is `APPENDIX_REQUIRED`. Periods 25 and 26 and all
arbitrary-period extrapolations are omitted.
