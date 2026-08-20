# Appendix A. Quotient and Orbit Completeness

This appendix supplies the finite coverage arguments used in Theorems A and F.

## A.1 Switching coordinates

For `G_n=C_n(1,2)`, the `n` triangle cycles together with the step-one
Hamilton cycle form a basis of the `(n+1)`-dimensional cycle space. Hence each
switching class is represented uniquely by

```text
(tau_0,...,tau_(n-1),alpha) in {+1,-1}^(n+1).                   (A.1)
```

For even `n`, global negation of every edge negates every triangle flux and
preserves `alpha`; it also replaces `A` by `-A`, so spectral radius is
unchanged. The adjacent products `Q_i=tau_i tau_(i+1)` are unchanged by this
negation. Legal `Q` words have product `+1`, and each has exactly the two lifts
`tau` and `-tau`. Therefore a pair `(Q,alpha)` represents precisely this
spectrally equivalent pair of switching classes.

The dihedral group acts by graph automorphisms. If a canonical `Q` orbit has
size `s`, retaining both values of `alpha` represents `4s` switching classes:
`s` geometric words, two `tau` lifts, and two holonomies. Summing over all
legal `Q` orbits gives

```text
sum_orbits 4s = 4*2^(n-1)=2^(n+1),                              (A.2)
```

which is exactly the switching-class count. Thus the quotient loses no class.

## A.2 Burnside count for legal flux words

Let a permutation `g` of the `p` cyclic positions have cycle lengths
`ell_1,...,ell_c`. A word fixed by `g` is constant on each cycle, so it is
specified by signs `epsilon_1,...,epsilon_c`. Its total product is

```text
product_(j=1)^c epsilon_j^(ell_j).                               (A.3)
```

If at least one `ell_j` is odd, exactly half of the `2^c` assignments make
(A.3) positive, so `g` fixes `2^(c-1)` legal words. If every `ell_j` is even,
then (A.3) is always positive and `g` fixes all `2^c` assignments. Burnside's
lemma therefore gives

```text
N_p=(1/(2p)) sum_(g in D_p)
    {2^(c(g)-1), if g has an odd cycle;
     2^c(g),     if all cycles of g are even}.                  (A.4)
```

Evaluating the cycle decompositions of the `p` rotations and `p` reflections
gives:

| `p` | legal words | dihedral orbits |
|---:|---:|---:|
| 1 | 1 | 1 |
| 2 | 2 | 2 |
| 3 | 4 | 2 |
| 4 | 8 | 4 |
| 5 | 16 | 4 |
| 6 | 32 | 8 |
| 7 | 64 | 9 |
| 8 | 128 | 18 |
| 9 | 256 | 23 |
| 10 | 512 | 44 |
| 11 | 1,024 | 63 |
| 12 | 2,048 | 122 |
| 13 | 4,096 | 190 |
| 14 | 8,192 | 362 |
| 15 | 16,384 | 612 |
| 16 | 32,768 | 1,162 |

Their orbit total is 2,626.

## A.3 Explicit representative-set equality

The bounded frontier uses more than the counts in (A.4). For each `p`, form
all `2^(p-1)` legal words by choosing the first `p-1` entries and forcing the
last entry to make the product positive. Replace each word by the
lexicographically least of its rotations and reflected rotations. The set of
resulting canonical words is compared exactly with the stored table's
`(p,Q)` set, and the table identifiers are required to follow that
lexicographic order. Equality of the sets excludes both an omitted orbit and a
duplicate orbit hidden under a new identifier.

For every stored representative, a second check recomputes its dihedral image
set, orbit size, periodic lift, primitive `Q` period, and primitive `tau`
period. This proves that the two target rows in periods 8 and 16 are related by
cell repetition and that no genuinely different primitive phase is removed.

## A.4 Finite minimality coverage

At orders through 20, direct iteration over (A.1) covers every switching
class. At the larger orders, canonical `(Q,alpha)` records are generated in
defect shells. Each record stores its dihedral orbit size and therefore its
represented multiplicity from (A.2). For every shell, the sum of these
multiplicities is compared with the binomial parity count of legal words; the
sum over shells is compared with `2^(n+1)`. A terminal cursor proves that the
canonical generator has exhausted its ordered domain.

At `n=24`, a separately implemented visited-set generator and a fixed-weight
necklace generator agree record for record on all 176,906 canonical flux
records. At `n=26,28,30`, independent Burnside and shell totals, represented
size sums, ordering, and parity checks agree with production. This establishes
the stated finite coverage subject to the execution-trust boundary disclosed
in Section 9.
