# Odd-divisor hierarchy and the universal period-gap law

Date: 2026-09-09

Status: **Proved**. This note belongs only to Paper I.

## 1. Arithmetic family of compatible compressed periods

Let

\[
s=2^k n,
\qquad k\ge2,
\qquad n\text{ odd}.
\]

For every odd divisor

\[
d\mid n,
\]

put

\[
L_d=2^k d
\]

and

\[
m_d=n/d.
\]

Then `m_d` is odd and

\[
s=L_d m_d.
\]

Writing

\[
m_d=2q_d+1,
\]

the general two-defect compression theorem applies with half-period `L_d`.

### Theorem A — odd-divisor hierarchy

For every odd divisor `d|n`, there is an explicit primitive two-defect phase of period

\[
\boxed{
p_d=2^{k+1}d}
\tag{1.1}
\]

whose continuous squared Bloch edge satisfies

\[
\boxed{R_{d}<8.}
\tag{1.2}
\]

Thus a single jump `s` carries a whole divisor-indexed family of sub-eight periodic phases.

### Proof

Since

\[
s=L_d(n/d)
\]

and `n/d` is odd, the compatibility criterion

\[
s\equiv L_d\pmod{2L_d}
\]

holds. The general compression theorem gives (1.2). The two-defect word has primitive period `2L_d`, giving (1.1).

---

## 2. The shortest member

The divisor `d=1` gives

\[
p_{\min}=2^{k+1}.
\]

By the period-optimality theorem, no shorter period is possible inside the reflection-chiral two-defect ansatz.

The other odd divisors give the nested arithmetic periods

\[
2^{k+1}d,
\qquad d\mid n.
\]

Hence the compatible compressed periods reproduce the odd-divisor lattice of the jump after removing its fixed 2-adic part.

---

## 3. Universal period-gap law

For the phase corresponding to `d`, let

\[
\Gamma_d=8-R_d.
\]

The global sharp compressed-gap theorem is uniform in the odd multiplier and gives, whenever

\[
L_d\to\infty,
\]

\[
L_d^2\Gamma_d
\longrightarrow
4\arccos(1/3)^2.
\tag{3.1}
\]

Since

\[
p_d=2L_d,
\]

we obtain the period-normalized form

\[
\boxed{
p_d^2\Gamma_d
\longrightarrow
16\arccos(1/3)^2.}
\tag{3.2}
\]

The constant in (3.2) is universal: it is independent of

- the 2-adic valuation `k`;
- the odd part `n`;
- the chosen odd divisor `d`;
- the residual odd multiplier `n/d`.

Thus the leading gap is controlled by the actual compressed period rather than by the original jump itself:

\[
\boxed{
8-R_d
\sim
\frac{16\arccos(1/3)^2}{p_d^2}.}
\tag{3.3}
\]

---

## 4. Leading-order period/gap optimality

Consider two compatible odd divisors

\[
d_1<d_2.
\]

Their periods satisfy

\[
\frac{p_{d_2}}{p_{d_1}}=\frac{d_2}{d_1}.
\]

By (3.3), along any regime in which the corresponding half-periods tend to infinity,

\[
\boxed{
\frac{\Gamma_{d_1}}{\Gamma_{d_2}}
\longrightarrow
\left(\frac{d_2}{d_1}\right)^2.}
\tag{4.1}
\]

Hence, to leading order inside the compatible two-defect hierarchy, shortening the period increases the spectral gap quadratically.

In particular the minimal-period member `d=1` is also the asymptotically strongest member of the divisor hierarchy.

This is a leading-order statement; no claim of exact finite-`L` ordering between different divisors is made here.

---

## 5. Interpretation

The arithmetic structure is therefore richer than a single 2-adic construction:

\[
\boxed{
\text{odd divisors of }s/2^{v_2(s)}
\longleftrightarrow
\text{compatible primitive compressed periods}.}
\]

All of these phases lie below the squared edge `8`, and all share one universal period-normalized Robin constant

\[
\boxed{16\arccos(1/3)^2.}
\]

This gives the paper a genuine period-gap scaling law, not merely an existence theorem for one preferred period.
