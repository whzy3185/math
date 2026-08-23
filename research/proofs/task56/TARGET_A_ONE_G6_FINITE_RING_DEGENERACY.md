# Symmetry-Protected Double Level On The One-G6 Ring

Status: algebraic symmetry `PROVED`; large-distance spectral conclusion
`COMPUTER_ASSISTED_PROVED` through the Task 55 exact-`2r` theorem.

## Theorem

Let `n=8k+2`, `k>=1`. In the `alpha=+1` tree gauge, take the cyclic Q word
whose positive entries are

```text
D={0,4,8,...,n-6} subset Z/nZ.                       (1)
```

Its cyclic gap word is a rotation of

```text
(6,4,...,4),
```

with one gap 6 and `2k-1` gaps 4. Thus it is the standard residue-two,
one-G6 construction. Set `tau_0=1` and

```text
tau_(i+1)=Q_i tau_i                                  (2)
```

cyclically. On `R^(Z/nZ)`, define

```text
(K_n u)_i=(-1)^i u_(n-3-i).                          (3)
```

Then

```text
K_n^2=-I,
K_n A_n=-A_n K_n,
K_n H_n=H_n K_n,       H_n=A_n^2.                    (4)
```

Consequently every nonzero eigenvalue of `H_n` has even multiplicity, and
the spectrum of `A_n` is symmetric under `lambda -> -lambda` with matching
multiplicities.

If in addition `n>=1042`, the Task 55 exact-`2r` theorem applies with `r=1`
and `D=n`. There is then a single distinct eigenvalue `Lambda_n` in

```text
[c6-1/400,c6+1/400],                                 (5)
```

it has multiplicity exactly two as an eigenvalue of `H_n`, and

```text
|Lambda_n-c6|<3505(9/25)^ell,
ell=floor((floor(n/4)-12)/8).                         (6)
```

It is the spectral top of `H_n`. The two corresponding eigenvalues of `A_n`
are `+sqrt(Lambda_n)` and `-sqrt(Lambda_n)`, each simple.

## Cyclic Coefficient Identity

The involution

```text
i -> n-6-i                                             (7)
```

preserves `D`. Indeed `n-6=8k-4` is divisible by four, so (7) preserves the
residue class zero modulo four; it permutes exactly the `2k` elements in
(1). Therefore

```text
Q_(n-6-i)=Q_i                                         (8)
```

for every cyclic index `i`.

There are `2k` positive Q entries and `6k-3` negative Q entries among the
indices `0,...,n-6`. Since `6k-3` is odd, (2) gives the anchor

```text
tau_(n-5)=-tau_0.                                     (9)
```

Suppose `tau_(n-5-i)=-tau_i`. Using (2), (8), and `Q_j^2=1`,

```text
tau_(n-5-(i+1))
 =tau_(n-6-i)
 =Q_(n-6-i) tau_(n-5-i)
 =-Q_i tau_i
 =-tau_(i+1).                                         (10)
```

Starting from (9), cyclic induction proves

```text
tau_(n-5-i)=-tau_i                                    (11)
```

for every `i in Z/nZ`. This is an all-order identity, not a sampled finite
calculation.

## Anticommutation Proof

Because `alpha=+1`, every step-one sign is positive and

```text
(A_nu)_i=u_(i-1)+u_(i+1)
          +tau_(i-2)u_(i-2)+tau_i u_(i+2).            (12)
```

Put `a=n-3`. Since `a` is odd, applying (3) twice gives

```text
(K_n^2u)_i=(-1)^i(-1)^(a-i)u_i=-u_i.                 (13)
```

Directly from (12),

```text
(A_nK_nu)_i=(-1)^i[-u_(a-i+1)-u_(a-i-1)
                    +tau_(i-2)u_(a-i+2)
                    +tau_i u_(a-i-2)].               (14)
```

On the other hand,

```text
(K_nA_nu)_i=(-1)^i[u_(a-i-1)+u_(a-i+1)
                    +tau_(a-i-2)u_(a-i-2)
                    +tau_(a-i)u_(a-i+2)].             (15)
```

Identity (11) says

```text
tau_(a-i-2)=tau_(n-5-i)=-tau_i,
tau_(a-i)=tau_(n-3-i)=-tau_(i-2).                    (16)
```

Substituting (16) into (15) gives `K_nA_n=-A_nK_n`. Squaring this identity
gives `K_nH_n=H_nK_n`, proving (4).

## Multiplicity Consequences

If `A_nu=lambda u`, anticommutation gives

```text
A_n(K_nu)=-lambda(K_nu).                              (17)
```

The invertibility of `K_n` preserves multiplicity. If `y>0` is an eigenvalue
of `H_n=A_n^2`, its eigenspace is the orthogonal direct sum of the `A_n`
eigenspaces at `+sqrt(y)` and `-sqrt(y)`. Equation (17) identifies those two
spaces isomorphically, so the `H_n` multiplicity is even.

For `n>=1042`, the exact-`2r` theorem gives total rank two in (5). Evenness
therefore forces that rank to belong to one distinct eigenvalue `Lambda_n`,
with multiplicity exactly two. The codimension-two complement theorem puts
every other eigenvalue below `c6-1/200`, while (5) lies above that cap. Hence
`Lambda_n=sup sigma(H_n)`. Its positive and negative `A_n` multiplicities are
equal and sum to two, so both are one. Bound (6) is the `r=1` instance of the
Task 55 estimate.

## Boundary

The global symmetry proved here uses the standard residue-two representative
and `alpha=+1`. It does not assert the same degeneracy for `alpha=-1`, for
arbitrary orientations of several interfaces, or for the residue-four and
residue-six families. It proves a protected double squared level, not
individual simplicity of the squared spectrum. Those broader interaction
questions remain open.
