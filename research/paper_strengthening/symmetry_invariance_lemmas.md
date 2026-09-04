# Symmetry invariance and primitive-period hygiene

**Status:** analytic proofs closed; independent exact matrix audit passed.  These
lemmas complete the orbit-reduction justification used by the minimal-period
and period-eight rigidity theorems.  They are not new Lean claims.

## 1. Periodic operator and Bloch edge

Let `tau` be a sign word of displayed period `p`.  On bi-infinite sequences,
write

```text
(A_tau x)_i
 = x_(i-1)+x_(i+1)
   +tau_(i-2)x_(i-2)+tau_i x_(i+2).
```

For `|z|=1`, let `B_z^(p)` be the `p`-dimensional space of sequences satisfying

```text
x_(i+p)=z x_i.
```

The restriction of `A_tau` to this space is the Hermitian Bloch fiber
`H_tau^(p)(z)`.  Define

```text
R_p(tau)=sup_(|z|=1) rho(H_tau^(p)(z))^2.
```

## 2. The two lifts of a defect word

Let

```text
Q_i=tau_i tau_(i+1).
```

When `prod_i Q_i=1`, fixing `tau_0` determines a periodic lift, and the only
two lifts are `tau` and `-tau`.

### Proposition 2.1 — lift invariance

For every displayed period `p`,

```text
R_p(-tau)=R_p(tau).
```

More precisely, if `D x_i=(-1)^i x_i`, then

```text
D A_tau D = -A_(-tau).
```

Moreover, `D` maps `B_z^(p)` unitarily onto
`B_(((-1)^p)z)^(p)`.  Consequently

```text
spec H_(-tau)^p(((-1)^p)z) = - spec H_tau^p(z).
```

The phase map `z -> ((-1)^p)z` is a bijection of the unit circle, so the
squared Bloch edges agree.

### Proof

Conjugation by `D` changes the sign of every displacement-one term and leaves
every displacement-two term unchanged.  Negating `A_(-tau)` has exactly the
same effect.  Also

```text
(Dx)_(i+p)=(-1)^(i+p) z x_i=((-1)^p z)(Dx)_i.
```

The fiber spectral identity and the equality of the suprema follow.  This
also records the odd-period phase shift that is invisible if one writes only
the even-period case.

## 3. Cyclic and reflection invariance

For an integer `k`, put

```text
(rot_k tau)_i=tau_(i+k).
```

Let `(S_k x)_i=x_(i+k)`.  Then `S_k` preserves `B_z^(p)` and a direct
substitution gives

```text
A_(rot_k tau) S_k = S_k A_tau.
```

Thus every cyclic translate has the same fiber spectrum at the same phase
and, in particular, the same squared Bloch edge.

For reflection, put

```text
(ref tau)_i=tau_(-i-2),
(R x)_i=x_(-i).
```

The index offset in `ref tau` is forced by the convention that `tau_i`
multiplies the edge from `i` to `i+2`.  Direct substitution gives

```text
A_(ref tau) R = R A_tau.
```

The reflection maps `B_z^(p)` unitarily onto `B_(z^(-1))^(p)`.  Hence

```text
spec H_(ref tau)^p(z^(-1))=spec H_tau^p(z)
```

and reflection preserves the squared Bloch edge.

### Corollary 3.1 — dihedral reduction for `Q`

The induced transformations are

```text
Q(rot_k tau)_i = Q(tau)_(i+k),
Q(ref tau)_i   = Q(tau)_(-i-3).
```

Any lift of a rotated or reflected `Q` word differs from the corresponding
transformed lift by at most a global minus sign.  Proposition 2.1 and the two
conjugacies therefore prove that `R_p` is constant on the dihedral orbits of
legal `Q` words.  This is the missing mathematical justification for the
orbit tables in the existing period-eight and `p<8` arguments.

## 4. Displayed period, primitive period, and cell repetition

A word may be displayed in a cell larger than its least period.  Let `q` be
the primitive period of `tau`, let `p=kq`, and regard the same coefficient
word as `p`-periodic.

### Proposition 4.1 — zone folding does not change the Bloch edge

For every repetition,

```text
R_p(tau repeated k times)=R_q(tau).
```

Indeed, for fixed `z` the `p`-cell fiber decomposes under translation by `q`
as

```text
spec H_tau^p(z)
 = union_(w^k=z) spec H_tau^q(w),
```

with algebraic multiplicities.  Taking the union over all unit `z` is the
same as taking the union over all unit `w`, which proves the claim.

This identity distinguishes a genuinely new periodic phase from a repeated
description of a shorter one.

### Corollary 4.2 — primitive form of the minimal-period theorem

The existing theorem excludes every displayed period `p<8`.  Therefore it
also excludes every primitive period below eight.  The target word

```text
tau_*=(1,1,-1,1,-1,-1,1,-1)
```

has primitive period eight: its second half is the negative of its first,
so it is not four-periodic, and inspection of the first four entries excludes
periods one and two.  Since its squared Bloch edge is `eta<8`, the natural
statement is valid:

> Eight is the smallest primitive period of a legal Hamilton-gauge signing
> whose squared Bloch edge is strictly below eight.

Repeated cells remain useful for finite rings, but they do not create new
primitive phases.

## 5. Independent audit

Run

```text
uv run --with sympy python \
  research/paper_strengthening/verifiers/verify_symmetry_and_chiral.py
```

The audit reconstructs the fibers from the operator formula, checks the lift,
translation, and reflection matrix identities, and checks the later half-cell
criterion for every sign word through displayed period twelve.  It does not
replace the index proofs above.
