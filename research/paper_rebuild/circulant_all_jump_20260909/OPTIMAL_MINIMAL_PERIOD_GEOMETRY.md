# Asymptotically optimal geometry inside the minimal 2-adic period

Date: 2026-09-10

Status: **Proved**. This combines the period-optimality theorem with the full-Bloch macroscopic gap law.

## 1. Minimal compatible period for a prescribed jump

Let

\[
s=2^k n,
\qquad n\text{ odd},
\qquad k\ge2.
\]

Inside the reflection-chiral even-separation two-defect ansatz, compatibility requires

\[
s=L(2q+1).
\]

The shortest possible half-period is therefore

\[
\boxed{L_k=2^k,}
\]

and the shortest primitive coefficient period is

\[
\boxed{p_k=2L_k=2^{k+1}.}
\tag{1.1}
\]

Write

\[
S_k:=\frac{L_k}{2}=2^{k-1}.
\]

Every even defect separation inside this minimal cell can be written as

\[
h=2m,
\qquad
N+m=S_k,
\qquad
1\le m\le S_k-1.
\tag{1.2}
\]

Let

\[
\Gamma_{k,m,n}
:=8-\max_{|z|=1}\rho(H_{k,m,n}(z))^2
\]

be the full Bloch squared gap of that minimal-period geometry.

## Theorem A — macroscopic gap law inside the minimal period

Let `k->infinity` and choose integers `m_k` with

\[
\frac{m_k}{S_k}\longrightarrow\alpha\in(0,1).
\]

Then, uniformly with respect to the odd part `n` of the jump,

\[
\boxed{
L_k^2\Gamma_{k,m_k,n}
\longrightarrow
\frac{\pi^2}{\max\{\alpha,1-\alpha\}^2}.
}
\tag{2.1}
\]

Equivalently, in terms of the actual primitive period `p_k=2L_k`,

\[
\boxed{
p_k^2\Gamma_{k,m_k,n}
\longrightarrow
\frac{4\pi^2}{\max\{\alpha,1-\alpha\}^2}.
}
\tag{2.2}
\]

### Proof

Here

\[
N_k=S_k-m_k,
\qquad
\frac{h_k}{L_k}
=\frac{m_k}{S_k}\to\alpha.
\]

Because `alpha in (0,1)`, both `N_k` and `m_k` tend to infinity. The full-Bloch macroscopic gap theorem therefore applies and gives (2.1). Multiplying by `p_k^2/L_k^2=4` gives (2.2).

---

## Theorem B — balanced minimal-period phase is uniquely asymptotically optimal

Among all macroscopic defect geometries in the minimal primitive period,

\[
\boxed{
\limsup p_k^2\Gamma_{k,m_k,n}\le16\pi^2,
}
\tag{3.1}
\]

and equality is possible if and only if

\[
\boxed{
\frac{m_k}{S_k}\longrightarrow\frac12.
}
\tag{3.2}
\]

For the exactly balanced choice

\[
\boxed{
N_k=m_k=2^{k-2},
\qquad
h_k=2^{k-1}=\frac{L_k}{2},
}
\tag{3.3}
\]

one has

\[
\boxed{
p_k^2\Gamma_{k,2^{k-2},n}\longrightarrow16\pi^2.}
\tag{3.4}
\]

### Proof

The right side of (2.2) is

\[
\frac{4\pi^2}{\max\{\alpha,1-\alpha\}^2}.
\]

It is maximized uniquely at `alpha=1/2`, where it equals `16pi^2`. The rigidity statement follows from the quantitative balanced-geometry theorem.

---

## Corollary C — quantitative loss from an unbalanced minimal cell

If for some fixed `epsilon>0`,

\[
\left|\frac{m_k}{S_k}-\frac12\right|\ge\epsilon
\]

for all sufficiently large `k`, then

\[
\boxed{
\limsup p_k^2\Gamma_{k,m_k,n}
\le
\frac{16\pi^2}{(1+2\epsilon)^2}
<16\pi^2.
}
\tag{4.1}
\]

Thus asymptotic optimality inside the shortest possible period forces geometric balance.

---

## 5. Comparison with the original short two-defect construction

The original compressed construction used the shortest defect separation `h=2`. In the same minimal half-period `L_k`, its sharp normalized gap constant is

\[
4\arccos(1/3)^2.
\]

The balanced minimal-period geometry instead has limiting constant

\[
4\pi^2
\]

in `L_k^2 Gamma` normalization. Therefore the asymptotic improvement factor is

\[
\boxed{
\frac{4\pi^2}{4\arccos(1/3)^2}
=\left(\frac{\pi}{\arccos(1/3)}\right)^2.
}
\tag{5.1}
\]

This factor is approximately `6.51`.

Thus period compression and gap optimization are compatible: one does not need to enlarge the minimal `2`-adic period in order to obtain the asymptotically best macroscopic two-defect geometry.

## 6. Paper-level significance

For large `v_2(s)`, the explicit even-jump theorem can now be stated in an optimized form:

> the shortest reflection-chiral two-defect period is `2^{v_2(s)+1}`, and within that shortest period the balanced defect geometry uniquely maximizes the leading full-Bloch gap, with period-normalized constant `16pi^2`.

This replaces the earlier use of the shortest-separation word as the natural canonical compressed phase.