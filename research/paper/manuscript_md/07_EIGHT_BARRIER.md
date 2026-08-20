# 6. The Eight-Barrier and Structural Optimum

We now prove Theorem D without relying on the list of 17 individual
competitor certificates. The proof begins with an exact local identity for the
squared operator and ends with a finite four-case analysis of two-defect
geometry.

## 6.1 Squaring the operator

Starting from (2.1), multiply the four transitions twice. The complete row of
`A_tau^2` from residue `i` is

| displacement | coefficient |
|---:|---|
| `-4` | `Q_(i-4)Q_(i-3)` |
| `-3` | `tau_(i-3)(1+Q_(i-3))` |
| `-2` | `1` |
| `-1` | `tau_(i-2)(1+Q_(i-2))` |
| `0` | `4` |
| `+1` | `tau_(i-1)(1+Q_(i-1))` |
| `+2` | `1` |
| `+3` | `tau_i(1+Q_i)` |
| `+4` | `Q_iQ_(i+1)` |

For completeness, consider for example displacement `+3`. It arises from the
two paths `+1,+2` and `+2,+1`, with weights `tau_(i+1)` and `tau_i`.
Since `tau_(i+1)=tau_i Q_i`, their sum is `tau_i(1+Q_i)`. The other odd
displacements follow by translation and reversal. Displacement `+4` has the
single path `+2,+2`, of weight `tau_i tau_(i+2)=Q_iQ_(i+1)`. The diagonal
has four immediate reversals, the `+-2` displacements have their surviving
unit coefficient after cancellation of the remaining routes, and reversal
gives the negative displacements.

Thus a negative flux `Q_i=-1` cancels the associated odd-displacement
couplings, while a positive flux opens them with absolute amplitude two. This
is the defect mechanism behind the theorem.

## 6.2 The all-negative baseline

If `Q_i=-1` for every `i`, choose the lift `tau_i=(-1)^i`. Let `S` be the
bilateral shift and set

```text
C=S+S^(-1),       E=S^2+S^(-2),       D=diag((-1)^i).
```

Then `A=C+DE`, while `CD=-DC` and `ED=DE`. Hence the cross terms cancel:

```text
A^2=C^2+E^2=4I+S^2+S^(-2)+S^4+S^(-4).                          (6.1)
```

On the Fourier mode `S=e^(i theta)`, the symbol of (6.1) is

```text
4+2cos(2theta)+2cos(4theta)<=8.                                 (6.2)
```

Equality holds at `theta=0`. Therefore the all-negative phase has `R=8`.

## 6.3 The first three moments at period eight

For an eight-periodic word, equations (2.9)-(2.10) give the signed closed-walk
moments. The diagonal of `A^2` is four at each of eight residues, so

```text
M_1=32.                                                         (6.3)
```

Since `A^2` is Hermitian,

```text
M_2=tr(A^4)=sum_(i,j)|(A^2)_(i,j)|^2.
```

The diagonal and even-displacement terms contribute 160. Each positive flux
opens four oriented odd-displacement entries, each of square four, so

```text
M_2=160+16d.                                                    (6.4)
```

For `M_3=tr((A^2)^3)`, collect the local closed products according to whether
they use no activated site, one activated site, an adjacent activated pair, or
a distance-two activated pair. Direct multiplication of the displayed
`A^2` row gives respectively the coefficients `944`, `168`, `96`, and `48`:

```text
M_3=944+168d+96a+48b.                                           (6.5)
```

An independent derivation of (6.5), valid for every period, is given in
Section 7 by enumerating the 430 closed step words of length six. Thus no
spectral approximation enters (6.3)-(6.5).

The second excess is

```text
F_2=M_3-8M_2=-336+40d+96a+48b.                                 (6.6)
```

## 6.4 Four or more defects

Because `product_i Q_i=1`, the defect count `d` is even.

Suppose `d=4`. Write the four positive cyclic gaps as positive integers
summing to eight. If at least two gaps are one, then `2a>=4`. If none is one,
all four gaps equal two and `b=4`. If exactly one is one, the other gaps are
`2,2,3`, so again `2a+b=4`. Hence always `2a+b>=4`, and (6.6) gives

```text
F_2=-176+48(2a+b)>=16>0.
```

If `d=6`, the two negative positions destroy at most four of the eight
adjacent positive-positive edges, so `a>=4`; then `F_2>=288>0`. If `d=8`,
(6.3)-(6.4) give

```text
F_1=M_2-8M_1=32>0.
```

By Lemma 2.3, every phase with at least four defects has `R(Q)>8`.

## 6.5 Two defects

Let `d=2` and let `s in {1,2,3,4}` be the smaller cyclic separation of the
two defects. Translation and reflection make `s` a complete orbit invariant.
Exact closed-walk enumeration gives the following first positive excesses:

| separation `s` | first positive excess | value |
|---:|---:|---:|
| 1 | `F_4` | 5,504 |
| 2 | `F_6` | 64,336 |
| 3 | `F_9` | 2,872,096 |

We indicate how these are certified. Starting at each of the eight residues,
enumerate all words of length `2k` over steps `{-2,-1,+1,+2}` whose total
displacement is zero, multiply the corresponding signs from (2.1), and sum.
This produces the integer `M_k`; subtraction gives `F_k`. For `s=1,2,3`, the
first positive values are exactly those in the table, so Lemma 2.3 gives
`R(Q)>8`.

For `s=4`, the word is a translate of

```text
Q_*=(+,-,-,-,+,-,-,-).
```

Section 5 proves `R(Q_*)=eta<8`. No conclusion is drawn from the negative
values of its first nine excesses.

## 6.6 Proof of the trichotomy

The legal defect counts are `0,2,4,6,8`. Section 6.2 proves `R=8` when
`d=0`. Section 6.4 proves `R>8` for `d>=4`. Section 6.5 proves `R>8` for
two-defect separations one, two, and three, while separation four is exactly
the target orbit and has `R=eta<8`. These cases are disjoint and exhaustive,
which proves Theorem D. `square`

The orbit of `Q_*` contains four flux words, corresponding to the four
antipodal pairs. Thus the minimizer is unique modulo translation and
reflection. The all-negative word is the only equality case at eight and is
therefore the unique runner-up orbit.

## 6.7 Chiral structure of the target

The target lift may be written

```text
tau=(+,-,+,-,-,+,-,+),       tau_(i+4)=-tau_i.                  (6.7)
```

Let `T_4(z)` be translation by four sites on the Bloch fiber and let
`D=diag((-1)^i)`. On a general fiber,

```text
(D T_4(z))^2=zI.
```

Choose `xi` with `xi^2=z` and define `J_z=xi^(-1)D T_4(z)`. Substitution of
(6.7) in the four transitions gives

```text
J_z^2=I,       J_z H(z)J_z^(-1)=-H(z).                          (6.8)
```

Both eigenspaces of `J_z` have dimension four. In a chiral basis,

```text
H(z)=[0 B; C 0],       H(z)^2=[BC 0; 0 CB].                     (6.9)
```

On the unit circle `C=B*`. Equation (6.9) explains the even characteristic
polynomial and the four-dimensional squared-band reduction. It does not by
itself prove optimality: the legal chiral words form two dihedral orbits, one
with two defects and one with six, and the latter lies above eight by Section
6.4.
