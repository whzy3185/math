# Interaction Symmetry Night Report

Status: `HOSTILE_AUDIT_PASS` for
`TARGET_A_ONE_G6_FINITE_RING_DEGENERACY.md`.

## 1. Audit scope and verdict

The audit independently checked the all-`k` cyclic coefficient identity, the
finite-ring anticommutation relation, and every deduction made from the Task
55 exact-`2r` theorem. No counterexample or unsupported implication was
found. The one-G6 theorem is valid as stated for `alpha=+1`.

This verdict does not promote a symmetry theorem for arbitrary multi-interface
rings. The proof uses one global cyclic reflection of the complete finite
coefficient word, not merely the local infinite-interface symmetry near G6.

## 2. Independent all-`k` coefficient check

Write `n=8k+2` and

```text
D={4j:0<=j<=2k-1}={0,4,...,n-6}.
```

For `d=4j in D`,

```text
n-6-d=4(2k-1-j) in D.
```

Thus the cyclic involution `i -> n-6-i` maps `D` onto itself; because it is a
bijection, it also maps the complement onto itself. Hence

```text
Q_(n-6-i)=Q_i                                         (1)
```

for every cyclic index. This direct set calculation removes any possible
ambiguity about residues modulo four on `Z/nZ`.

The interval of representatives `0,...,n-6` contains `n-5=8k-3` sites and
exactly `2k` members of `D`. It therefore contains `6k-3` negative entries,
an odd number. With `tau_0=1` and `tau_(i+1)=Q_i tau_i`, this gives

```text
tau_(n-5)=-tau_0.                                     (2)
```

If `tau_(n-5-i)=-tau_i`, then (1) and `Q_i^2=1` give

```text
tau_(n-6-i)
 =Q_(n-6-i) tau_(n-5-i)
 =-Q_i tau_i
 =-tau_(i+1).
```

Starting at (2) and taking `n` cyclic steps proves

```text
tau_(n-5-i)=-tau_i                                    (3)
```

for all `i`. The closure is consistent because the complete Q word has
`6k+2` negative entries and therefore product `+1`. The theorem's coefficient
argument is consequently an all-order proof, not a finite sample inference.

## 3. Independent anticommutation check

Set `a=n-3` and `(K_nu)_i=(-1)^i u_(a-i)`. Since `a` is odd,

```text
K_n^2=(-1)^a I=-I.                                   (4)
```

For the periodic `alpha=+1` tree-gauge operator,

```text
(A_nu)_i=u_(i-1)+u_(i+1)
          +tau_(i-2)u_(i-2)+tau_i u_(i+2),
```

the coefficient of `u_(a-i-2)` in `K_nA_n` is `tau_(a-i-2)` and the
coefficient of `u_(a-i+2)` is `tau_(a-i)`. Equation (3), first with index
`i` and then with index `i-2`, gives

```text
tau_(a-i-2)=-tau_i,
tau_(a-i)=-tau_(i-2).                                (5)
```

The step-one terms acquire the opposite sign from `(-1)^(i+/-1)`, while
(5) supplies the opposite sign for both step-two terms. Therefore every
matrix entry satisfies

```text
K_nA_n=-A_nK_n,       K_nH_n=H_nK_n.                 (6)
```

This is a finite-ring identity. The infinite G6 operator has an analogous
local formula, but that local formula alone does not define a symmetry on a
general finite ring; the global cyclic identity (3) is essential here.

## 4. Multiplicity and top-level deductions

For every `lambda`, (6) is an isomorphism from `ker(A_n-lambda)` to
`ker(A_n+lambda)`. If `y>0`, self-adjointness gives

```text
ker(H_n-y)
 =ker(A_n-sqrt(y)) direct_sum ker(A_n+sqrt(y)),
```

and the two summands have equal dimension. Every positive squared level thus
has even multiplicity.

For `n>=1042`, the Task 55 certificate uses exactly the residue-two convention

```text
r=1,       D=n,       ell=floor((floor(n/4)-12)/8).
```

Its independently checked conclusion is rank two in
`[c6-1/400,c6+1/400]`. This interval is positive, so even multiplicity forces
the entire rank to be one distinct squared eigenvalue `Lambda_n` of
multiplicity two. The same certificate gives

```text
|Lambda_n-c6|<3505(9/25)^ell.                         (7)
```

The codimension-two complement has spectral top at most `c6-1/200`, whereas
the cluster window begins at `c6-1/400`. Hence at most two eigenvalues counted
with multiplicity can lie above the complement cap, and the two already in
the cluster exhaust them. Therefore `Lambda_n=sup sigma(H_n)`. Its two
unsquared summands have equal positive integer dimension and total dimension
two, so `+sqrt(Lambda_n)` and `-sqrt(Lambda_n)` are each simple. Every stated
multiplicity and top deduction is valid.

## 5. Interaction consequence and boundary

For this one-G6 family the two squared modes cannot split: symmetry protects
one double finite-ring level. Thus full-H "individual simplicity" is false in
this subclass; the simple objects are the two unsquared levels of opposite
sign.

No universal `2r -> r` interaction reduction follows for several interfaces.
Such a reduction would first require a global finite-ring operator preserving
the complete coefficient word and an equivariant Feshbach projection. Local
copies of the infinite-interface `K` do not supply either condition. General
multi-interface simplicity, leading interaction coefficients, and genuine
three-body interaction remain `OPEN`.

## 6. Independent controls

As non-probative regression controls, a fresh implementation checked (1)--(3)
for every `1<=k<=128`, constructed the integer matrices and verified (4)--(6)
for `k=1,2,3,4`, and computed exact characteristic polynomials at orders
`10,18,26,34`. In all four cases the `A_n` characteristic polynomial was even
and the `H_n` characteristic polynomial was a perfect square. These checks
agree with, but are not substitutes for, the all-`k` proof above.
