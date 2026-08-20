# 7. General-Period Closed-Walk Obstructions

The local square identity in Section 6 does not depend on the period. We now
derive the first three moments for every legal periodic phase and prove
Theorem E.

## 7.1 From closed walks to flux monomials

The possible steps of (2.1) are `-2,-1,+1,+2`. A step of length one has
weight one. A `+2` step from `j` has weight `tau_j`, and a `-2` step from
`j` has weight `tau_(j-2)`.

Consider a closed step word and cancel repeated `tau` factors modulo two.
The remaining indices occur in even number; write them as

```text
r_1<r_2<...<r_(2s).
```

Using `Q_h=tau_h tau_(h+1)` and telescoping,

```text
product_j tau_(r_j)
 =product_(ell=1)^s product_(h=r_(2ell-1))^(r_(2ell)-1) Q_h.    (7.1)
```

Thus every signed closed walk becomes a monomial in interval products of `Q`.
The identity is on the integer lattice, before reduction modulo a period, so
it also handles short-cell collisions once cyclic indices are imposed.

## 7.2 Exact closed-word collection

There are respectively 4, 36, and 430 closed step words of lengths two, four,
and six. Collecting their flux monomials up to translation gives

| length | contribution from one starting residue |
|---:|---|
| 2 | `4` |
| 4 | `28+8Q_i` |
| 6 | `238+156Q_i+24Q_iQ_(i+1)+12Q_iQ_(i+2)` |

We briefly justify the collection. At length two, each of the four steps is
followed by its reverse. At length four, the 36 zero-sum words reduce via
(7.1) to 28 constant terms and eight translates of a single `Q_i`. At length
six, applying (7.1) to the 430 zero-sum words and grouping equal translated
interval products leaves only the four displayed monomial types. This is a
finite symbolic identity in the free `Q` variables, not a period-by-period
numerical observation.

Summing over the `p` starting residues yields

```text
M_1=4p,
M_2=28p+8 sum_i Q_i,
M_3=238p+156 sum_i Q_i
         +24 sum_i Q_iQ_(i+1)+12 sum_i Q_iQ_(i+2).              (7.2)
```

Let `I_i=(1+Q_i)/2`. Then

```text
d=sum_i I_i,       a=sum_i I_iI_(i+1),       b=sum_i I_iI_(i+2).
```

Substitute `Q_i=2I_i-1` in (7.2) and collect. The result is

```text
M_1=4p,
M_2=20p+16d,
M_3=118p+168d+96a+48b.                                         (7.3)
```

Because all sums are cyclic, (7.3) remains valid for `p=1,2,3,4`, even when
the offsets one and two coincide modulo `p`; multiplicities are retained by
the Laurent-matrix construction.

## 7.3 Necessary conditions at the eight-barrier

From (7.3),

```text
F_1=M_2-8M_1=16d-12p,
F_2=M_3-8M_2=-42p+40d+96a+48b.                                 (7.4)
```

If `R(Q)<=8`, Lemma 2.3 requires `F_1<=0` and `F_2<=0`. Therefore

```text
d<=3p/4,
40d+96a+48b<=42p.                                               (7.5)
```

This proves Theorem E. `square`

The first inequality limits defect density. The second also penalizes local
clustering, assigning greater weight to adjacent pairs than to distance-two
pairs. The converse is false in general: satisfying (7.5), or observing
finitely many nonpositive `F_k`, does not establish `R(Q)<=8`.

## 7.4 Relation to the period-eight mechanism

At `p=8`, equations (7.3)-(7.4) specialize to (6.3)-(6.6). For high defect
density the first two excesses already cross the barrier. Low-density phases
can evade these short tests, and the two-defect separation hierarchy in
Section 6 shows that progressively longer closed walks are then required.
This motivates the adaptive hierarchy used in the bounded low-period theorem.
