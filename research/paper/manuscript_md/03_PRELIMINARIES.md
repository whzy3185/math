# 2. Signed Circulants and Flux Coordinates

## 2.1 Signed adjacency matrices and switching

For an integer `n>=8`, let `G_n=C_n(1,2)` have vertex set `Z/nZ` and edges

```text
{i,i+1}, {i,i+2}    (i in Z/nZ).
```

A signing is a map `sigma:E(G_n)->{+1,-1}`. Its signed adjacency matrix
`A_sigma` is the real symmetric matrix whose `ij` entry is the sign of
`{i,j}` when this is an edge and zero otherwise. We write

```text
rho(A_sigma)=max{|lambda|: lambda in spec(A_sigma)}.
```

For a vertex-sign function `d:Z/nZ->{+1,-1}`, let `D=diag(d_i)`. Replacing
`sigma_ij` by `d_i sigma_ij d_j` replaces `A_sigma` by `D A_sigma D` and
therefore preserves the spectrum. This operation is switching.

Because `G_n` is connected and has `2n` edges, its cycle space has dimension
`2n-n+1=n+1`. Hence there are exactly `2^(n+1)` switching classes. We use a
cycle-flux coordinate system adapted to the Hamilton cycle of step-one edges.

## 2.2 Hamilton gauge, triangle flux, and quadrilateral flux

Let `a_i` be the sign of the step-one edge `{i,i+1}` and `b_i` the sign of
the step-two edge `{i,i+2}`. Define the triangle flux and Hamilton holonomy by

```text
tau_i=a_i a_(i+1) b_i,
alpha=product_(i=0)^(n-1) a_i.
```

The `n` triangle cycles together with the step-one Hamilton cycle form a cycle
basis, so `(tau_0,...,tau_(n-1),alpha)` determines the switching class.

Switch so that all step-one edges are positive except possibly the edge
crossing the cut from `n-1` to `0`. Equivalently, extend a vector to the
integer lattice with twisted boundary condition

```text
x_(i+n)=alpha x_i.
```

The signed operator then has the local form

```text
(A_tau x)_i=x_(i-1)+x_(i+1)+tau_(i-2)x_(i-2)+tau_i x_(i+2).       (2.1)
```

The quadrilateral flux word is

```text
Q_i=tau_i tau_(i+1).                                             (2.2)
```

For a `p`-periodic word `tau`, equation (2.2) implies
`product_(i=0)^(p-1) Q_i=1`. Conversely, any word
`Q in {+1,-1}^p` with product `+1` has exactly two periodic lifts, obtained by
choosing `tau_0=+1` or `-1` and recursing via
`tau_(i+1)=Q_i tau_i`.

We call

```text
D(Q)={i:Q_i=+1}
```

the defect set and write `d=|D(Q)|`. We also use the cyclic local statistics

```text
a=#{i:Q_i=Q_(i+1)=+1},
b=#{i:Q_i=Q_(i+2)=+1}.                                          (2.3)
```

## 2.3 Floquet matrices

Suppose `tau` has displayed period `p`. Write an integer index as `mp+r`,
where `0<=r<p`, and seek Bloch vectors of the form

```text
x_(mp+r)=z^m v_r.
```

Substitution in (2.1) gives a `p x p` Laurent matrix `H_tau(z)`. More
explicitly, for each transition from output residue `r` to an absolute source
index `j`, write `j=mp+s`, `0<=s<p`, and add the transition coefficient times
`z^m` to entry `(r,s)`. This convention automatically adds coefficients when
different transitions collide in short cells.

The identity

```text
H_tau(z)^T=H_tau(z^(-1))                                        (2.4)
```

follows by reversing each undirected transition. Thus `H_tau(z)` is Hermitian
on the unit circle.

For an infinite periodic phase, define

```text
R(Q)=sup_(|z|=1) rho(H_tau(z))^2.                                (2.5)
```

The two lifts of `Q` have the same value, so this notation is unambiguous.
Notice that `R(Q)` is always a **squared** spectral radius.

If a finite graph has order `n=pL` and Hamilton holonomy `alpha`, its cell
sequence satisfies `u_(m+L)=alpha u_m`. The unitary cell shift has eigenvalues
exactly

```text
z^L=alpha,                                                       (2.6)
```

and the finite matrix decomposes as

```text
A_(pL,alpha)  ~=  direct_sum_(z^L=alpha) H_tau(z).               (2.7)
```

Equation (2.6) is a discrete finite set. Equation `|z|=1` in (2.5) describes
the infinite-volume spectrum. We will not substitute one for the other.

## 2.4 Operator equivalences

We record the equivalences used in classifying periodic phases.

**Lemma 2.1 (translation, reflection, and negation).**  Translating `tau`,
reflecting it by `tau_i -> tau_(-i-2)`, or replacing `tau` by `-tau` preserves
`R(Q)`. On flux words reflection is `Q_i -> Q_(-i-3)`.

**Proof.** Let `(T_r x)_i=x_(i-r)` and `(Jx)_i=x_(-i)`. Direct substitution in
(2.1) gives

```text
T_r A_tau T_r^(-1)=A_(translated tau),
J A_tau J=A_(reflected tau).
```

Both are unitary conjugacies. For negation let `(Dx)_i=(-1)^i x_i`. The
endpoints of a step-one edge have opposite `D` signs while those of a step-two
edge have equal signs. Therefore

```text
A_(-tau)=-D A_tau D.
```

The spectrum is negated and its square is unchanged. In an odd displayed cell
the fiber coordinate changes from `z` to `-z`, but the full unit circle is
preserved. `square`

**Lemma 2.2 (zone folding).**  If `tau` has primitive period `q` and is
displayed in a repeated cell `p=mq`, then

```text
H_p(z) ~= direct_sum_(w^m=z) H_q(w).                            (2.8)
```

In particular repetition of the unit cell preserves `R(Q)`.

**Proof.** Write a residue in the repeated cell as `r+kq`, where
`0<=r<q` and `0<=k<m`. Decompose the `mq`-dimensional fiber according to the
unitary internal translation by `q`. On its `w`-eigenspace vectors have the
form

```text
x_(r+kq)=w^k v_r.
```

The repeated boundary condition is equivalent to `w^m=z`. Since all
coefficients in (2.1) are `q`-periodic, every transition factors out `w^k`
and the remaining action on `v` is exactly `H_q(w)`. The `m` roots of
`w^m=z` give mutually orthogonal eigenspaces and their dimensions sum to
`mq`. This proves (2.8), including multiplicities. `square`

## 2.5 Closed-walk moments

For a periodic phase define

```text
M_k(Q)=CT_z tr(H_Q(z)^(2k)),
F_k(Q)=M_(k+1)(Q)-8M_k(Q).                                      (2.9)
```

Constant-term extraction equals normalized integration around the unit circle:

```text
M_k(Q)=(1/(2pi)) integral_0^(2pi)
       sum_j lambda_j(e^(i theta))^(2k) dtheta.                  (2.10)
```

It is also the signed sum of closed walks of length `2k` per period cell.

**Lemma 2.3 (moment barrier).** If `R(Q)<=8`, then
`M_(k+1)(Q)<=8M_k(Q)` for every `k>=1`. Equivalently,

```text
F_k(Q)>0  ==>  R(Q)>8.                                          (2.11)
```

**Proof.** Under `R(Q)<=8`, every
`y_j(theta)=lambda_j(e^(i theta))^2` lies in `[0,8]`. Hence
`y_j^(k+1)<=8y_j^k`. Sum over `j` and integrate using (2.10). `square`

We emphasize that (2.11) is one-way. A nonpositive excess, or any finite list
of nonpositive excesses, does not prove `R(Q)<=8`.

## 2.6 Distinguished constants

For even `n>=8`, the conjectured threshold is

```text
rho_-(n)=2 sqrt(cos^2(pi/n)+cos^2(2pi/n)),
rho_-(n)^2=4+2cos(2pi/n)+2cos(4pi/n).                            (2.12)
```

The target period-eight squared spectral edge is

```text
eta=4+sqrt(10+2sqrt(5)),
rho_*=sqrt(eta).                                                  (2.13)
```

These quantities play different roles: `rho_-(n)` is the finite conjectured
lower bound, while `eta` is the exact infinite-volume squared radius of the
counterexample phase.
