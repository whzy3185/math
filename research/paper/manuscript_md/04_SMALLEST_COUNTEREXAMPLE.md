# 3. The Smallest Counterexample

We now prove Theorem A. The proof has two logically separate parts. First, an
explicit order-32 signing is certified by exact matrix inequalities. Second, a
complete finite enumeration excludes every admissible order below 32. The
first part is short enough to give here; the quotient and certificate coverage
for the second part is proved in Appendix A.

## 3.1 The order-32 signing

Let `n=32`, choose Hamilton holonomy `alpha=+1`, and repeat the triangle-flux
word

```text
tau=(+,+,-,+,-,-,+,-)                                           (3.1)
```

four times. In Hamilton gauge all step-one signs are positive and the step-two
sign at `{i,i+2}` is `tau_i`. The resulting quadrilateral flux is

```text
Q=(+,-,-,-)^8.                                                   (3.2)
```

Let `A_32` denote the resulting signed adjacency matrix.

**Proposition 3.1.** The matrix `A_32` satisfies

```text
rho(A_32)^2 < 1561/200 < rho_-(32)^2.                            (3.3)
```

**Proof.** The eight-site Floquet calculation in Section 4 gives the explicit
polynomial `P(y,c)` in (4.5). Put `B=1561/200`, `u=y-B`, and `t=2-c`.
Equation (4.6) displays `P(B+u,2-t)` as a polynomial whose coefficients are
nonnegative and whose constant term is
`84332641/1600000000>0`. Hence `P(y,c)>0` for every `y>=B` and
`c in [-2,2]`. Every squared eigenvalue of a unit-circle fiber is a
nonnegative root of `P`; therefore every fiber has squared radius strictly
less than `B`. The finite decomposition (4.3), with `L=4` and `alpha=+1`,
gives `rho(A_32)^2<1561/200`.

For the other inequality, equation (2.12) gives

```text
rho_-(32)^2
 =4+sqrt(2+sqrt(2))+sqrt(2+sqrt(2+sqrt(2))).                     (3.4)
```

This algebraic number is the unique real root in `(7809/1000,781/100)` of

```text
X^8-32X^7+432X^6-3216X^5+14456X^4
 -40224X^3+67736X^2-63184X+25022.                               (3.5)
```

A Sturm sequence has variation difference one at the two endpoints, and
exact substitution of the nested radical identifies the isolated root.
Since

```text
1561/200 < 7809/1000,
```

the second inequality in (3.3) follows. `square`

The witness is not gauge-dependent. For example, choosing step-one signs

```text
(+,-,+,-,-,+,-,+)^4
```

and solving `b_i=tau_i a_i a_(i+1)` gives step-two signs

```text
(-,-,+,+,+,+,-,-)^4.
```

The diagonal switching vector
`(+,+,-,-,+,-,-,+)^4` conjugates this matrix to `A_32`. This supplies an
independent reconstruction from flux data rather than from the stored edge
list.

## 3.2 Exhaustive exclusion below 32

The conjecture is posed exactly for even `n>=8`; hence the admissible orders
below 32 are

```text
8,10,12,14,16,18,20,22,24,26,28,30.                             (3.6)
```

**Proposition 3.2 (finite exclusion).** For every order in (3.6) and every
signing `sigma` of `C_n(1,2)`,

```text
rho(A_sigma)>=rho_-(n).                                          (3.7)
```

This is a finite computer-assisted proposition.

**Proof.** Switching classes are represented in the cycle coordinates
`(tau,alpha)`. Global edge-sign negation and the dihedral action are used only after
their spectral invariance has been proved. For `n<=20`, all `2^(n+1)` classes
are enumerated directly. For `n=22`, and for the production orders
`24,26,28,30`, the legal quadrilateral words are partitioned into dihedral
bracelets, with both holonomies retained. Appendix A proves that the orbit
sizes sum to `2^(n+1)` and gives an independent Burnside count.

For every representative other than the distinguished optimizer, the
enumeration stores a nonzero rational vector `v` and verifies exactly

```text
(v^T A_sigma^2 v)/(v^T v) >= rho_-(n)^2.                         (3.8)
```

The trigonometric threshold in (3.8) is compared as a real algebraic number;
floating eigenvalues are used only to propose `v`. The distinguished class is
checked by its exact known spectrum. Thus every switching class satisfies
(3.7). The state counts and certificate totals in Table 3.1 agree with the
complete quotient counts, and there are no unresolved representatives. `square`

| `n` | represented switching classes | exact nonoptimizer certificates |
|---:|---:|---:|
| 8 | 512 | 510 |
| 10 | 2,048 | 2,046 |
| 12 | 8,192 | 8,190 |
| 14 | 32,768 | 32,766 |
| 16 | 131,072 | 131,070 |
| 18 | 524,288 | 524,286 |
| 20 | 2,097,152 | 2,097,150 |
| 22 | 8,388,608 | 97,467 quotient certificates |
| 24 | 33,554,432 | 353,811 quotient certificates |
| 26 | 134,217,728 | 1,299,063 quotient certificates |
| 28 | 536,870,912 | 4,810,471 quotient certificates |
| 30 | 2,147,483,648 | 17,929,599 quotient certificates |

The last column counts spectral representatives, not switching classes. The
quotient multiplicities in Appendix A account exactly for the difference.

## 3.3 Proof of Theorem A

Proposition 3.2 excludes every admissible order below 32. Proposition 3.1
gives a strict counterexample at 32. Since the domain consists of even integers
at least eight, no admissible order lies between 30 and 32. Therefore 32 is the
smallest counterexample order. `square`

The theorem does not assert that the order-32 witness is unique, nor does it
assert failure at every even order above 32.
