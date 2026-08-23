# Exact Discrete IMS Lemma

Let `A` be any signed step-one/step-two cyclic adjacency and put `H=A^2`.
For real diagonal cutoffs `chi_j` with `sum_j chi_j^2=I`, direct expansion
gives

```text
H=sum_j chi_j H chi_j +(1/2)sum_j[chi_j,[chi_j,H]].
```

Entrywise,

```text
[chi,[chi,H]]_ab=(chi(a)-chi(b))^2 H_ab.
```

This proves the identity without a limiting argument.

Each row of `A` has four entries of absolute value one. Thus

```text
sum_b |H_ab|
 <= sum_c |A_ac| sum_b |A_cb| <=16.
```

This estimate includes all cancellations and all short-order collisions.
Moreover, an `A^2` path consists of two steps of length at most two, so
`H_ab=0` at cyclic distance greater than four. The generic distinct-offset
formula is collision-free for `n>=9`; the row-sum proof itself is valid for
every order for which the original signed graph is defined.

For an integer `R>=4`, define the cyclic tent

```text
f_R(k)=max(0,1-dist(k,0)/R)
```

and take every cyclic translate, normalized by

```text
C_R=sum_k f_R(k)^2=(2R^2+1)/(3R),
chi_j(a)=f_R(a-j)/sqrt(C_R).
```

When `n>2R+4`, these functions form an exact partition of unity. For cyclic
distance `d<=4`, at most `2R+d<=3R` raw terms change and each changes by at
most `d/R`. Since `C_R>=2R/3`,

```text
sum_j(chi_j(a)-chi_j(b))^2 <= 9d^2/(2R^2).
```

The Schur row bound for the IMS remainder is therefore

```text
||E_IMS||
 <= (1/2)(9/(2R^2)) 4^2 sup_a sum_b|H_ab|
 <=576/R^2.
```

All translates are cyclic, so there is no omitted boundary cutoff.

Status: `GATE_B1_PASS` / PROVED.
