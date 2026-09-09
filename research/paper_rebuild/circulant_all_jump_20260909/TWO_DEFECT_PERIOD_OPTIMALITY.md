# Period optimality inside the reflection-chiral two-defect family

Date: 2026-09-09

Status: **Proved**. This note belongs only to Paper I.

## 1. Structural family

For an even half-period `L>=4`, consider the period-`2L` two-defect flux word

\[
Q_0=Q_2=1,
\qquad
Q_j=-1\quad(j\ne0,2).
\]

Its Hamilton-gauge lift satisfies the reversal identity

\[
\tau_{3-j}=-\tau_j.
\]

The signed-reflection chiral theorem applies to a jump `s` precisely through the congruence

\[
\boxed{s\equiv L\pmod{2L}.}
\tag{1.1}
\]

Indeed this is the condition used when reflection sends a chord back to the reversed defect pattern.

---

## Theorem A — compatibility criterion

For positive integers `s,L`,

\[
\boxed{
s\equiv L\pmod{2L}
\quad\Longleftrightarrow\quad
L\mid s\ \text{ and }\ s/L\text{ is odd}.}
\tag{2.1}
\]

### Proof

The congruence is equivalent to

\[
s=L+2Lq=L(2q+1)
\]

for some integer `q>=0`, which is exactly the right-hand condition.

---

## Theorem B — exact 2-adic lower bound on the compatible period

Let `s` be even and write

\[
2^k\Vert s,
\qquad k\ge2.
\]

Suppose a member of the reflection-chiral two-defect family with half-period `L` is compatible with jump `s`. Then

\[
\boxed{v_2(L)=k.}
\tag{3.1}
\]

Consequently

\[
\boxed{L\ge2^k}
\tag{3.2}
\]

and its period satisfies

\[
\boxed{2L\ge2^{k+1}.}
\tag{3.3}
\]

Equality is achieved by

\[
\boxed{L=2^k.}
\tag{3.4}
\]

### Proof

By Theorem A,

\[
s=Lm
\]

with `m` odd. Therefore

\[
v_2(s)=v_2(L)+v_2(m)=v_2(L).
\]

Since `v_2(s)=k`, equation (3.1) follows. Every positive integer of 2-adic valuation `k` is at least `2^k`, proving (3.2)--(3.3). Taking `L=2^k` makes `s/L` odd, so equality is compatible.

---

## Proposition C — the two-defect word is primitive

For every

\[
L\ge4,
\]

the flux word

\[
Q=(1,-1,1,-1,-1,\ldots,-1)
\]

of length `2L` has primitive period exactly `2L`.

### Proof

The set of positive positions modulo `2L` is exactly

\[
\{0,2\}.
\]

If `Q` had a proper period `p<2L`, translation by `p` would preserve this two-point set. Thus

\[
\{p,p+2\}\equiv\{0,2\}\pmod{2L}.
\]

Either `p=0 mod 2L`, contradicting `0<p<2L`, or translation swaps the two points, forcing simultaneously

\[
p\equiv2,
\qquad
p+2\equiv0\pmod{2L}.
\]

The latter gives `2L=4`, impossible for `L>=4`. Hence no proper period exists.

---

## Corollary D — period optimality of the 2-adic compressed construction

Let

\[
2^k\Vert s,
\qquad k\ge2.
\]

The general compression theorem chooses

\[
L=2^k
\]

and hence the primitive period

\[
\boxed{p_s=2^{k+1}.}
\]

By Theorem B and Proposition C, this is the **smallest possible primitive period inside the reflection-chiral two-defect ansatz** compatible with jump `s`.

Thus the 2-adic construction has two simultaneous optimal features within its natural structural class:

1. it removes the odd part of `s` from the period completely;
2. it uses the shortest period permitted by the signed-reflection compatibility condition.

This is an internal structural optimality statement only. It does not claim that no unrelated signing of shorter period can have Bloch edge below `8`.
