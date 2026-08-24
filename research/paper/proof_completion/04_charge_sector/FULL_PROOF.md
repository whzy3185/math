# Full Proof

## 1. Flux lifts

Let `Q_i in {+1,-1}`. Once `tau_0` is chosen, the relation

```text
tau_(i+1)=Q_i tau_i                                  (1)
```

determines `tau` uniquely. Iterating (1) around a cycle gives

```text
tau_n=(product_(i=0)^(n-1) Q_i) tau_0.
```

Thus a cyclic lift exists if and only if `product_i Q_i=1`; when it exists,
the two choices `tau_0=+1` and `tau_0=-1` give the two lifts.

## 2. Gap and charge identities

Assume `D(Q)` is nonempty and list its `d>=1` elements cyclically as
`x_1,...,x_d`. Define `g_j` to be the number of forward steps from `x_j` to
`x_(j+1)`, with `x_(d+1)=x_1+n` after choosing integer representatives. The
corresponding half-open arcs form a disjoint partition of a cycle of length
`n`; hence

```text
sum_j g_j=n.                                         (2)
```

With `q_j=g_j-4`, equation (2) immediately gives

```text
sum_j q_j=sum_j g_j-4d=n-4d.                         (3)
```

The word has `d` positive and `n-d` negative entries, so

```text
product_i Q_i=(-1)^(n-d).                            (4)
```

If `n` is even and a cyclic lift exists, (1) and (4) imply that `n-d` is
even, and therefore `d` is even. Write `d=2h`. Equation (3) becomes

```text
sum_j q_j=n-8h,
```

which proves `sum_j q_j=n mod 8`.

No Hamilton holonomy occurs in (1)-(4). The holonomy is the independent sign
on the step-one Hamilton cycle and therefore cannot change the charge law.

## 3. The four reference sectors

For `s in Z/4Z`, define `B_s` by

```text
(B_s)_i=+1 iff i=s mod 4,
(B_s)_i=-1 otherwise.                                (5)
```

These are the four translates of the reference `Q` word. Choosing either
value of `tau_0` in (1) gives the two triangle-flux lifts of each sector.
Because a four-site cell contains one positive and three negative `Q`
entries, its product is `-1`; hence a lift is antiperiodic over four sites
and periodic over eight. This explains why there are four `Q` sectors but
the canonical triangle-flux background has period eight.

## 4. One oriented gap

Suppose an oriented gap begins at a positive site `x` of `B_s`; thus
`x=s mod 4`. If its length is `g`, the next positive site is `x+g`, and a
reference bulk continued to the right has positive sites

```text
x+g+4Z.
```

It is therefore the sector `B_(s+g)`. Since `q=g-4`,

```text
g=q mod 4.
```

Consequently the intrinsic sector shift is

```text
sigma_sec(q)=q mod 4,
B_s -> B_(s+sigma_sec(q)).                            (6)
```

This argument concerns only the positions of positive `Q` sites. Replacing
`tau` by its other lift or changing the Hamilton holonomy leaves (5)-(6)
unchanged.

## 5. Composition

Let consecutive interfaces have gaps `g_1,...,g_k` and charges
`q_j=g_j-4`. Starting in `B_s`, repeated use of (6) ends in

```text
B_(s+g_1+...+g_k)=B_(s+q_1+...+q_k)                 (7)
```

with indices reduced modulo four. This proves

```text
sigma_sec(q_1+...+q_k)=sum_j sigma_sec(q_j) mod 4.    (8)
```

In particular, a G6 gap has `q=2`. For `r=1,2,3`, the total charges are
`2,4,6`, giving the three nonzero even residues modulo eight, while their
sector shifts are respectively `2,0,2` modulo four. The modulo-eight and
modulo-four statements must not be conflated. This completes the proof.
