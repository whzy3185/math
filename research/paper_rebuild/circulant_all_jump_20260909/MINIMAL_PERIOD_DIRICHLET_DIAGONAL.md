# Minimal-period compressed phases approaching the Dirichlet constant

Date: 2026-09-09

Status: **Proved**. This note belongs only to Paper I.

This result combines the `2`-adic period-optimality theorem with the global defect-separation hierarchy.

## 1. Primitive period for a general two-defect word

Let the local flux word have period `2L` and exactly two positive entries, at positions `0` and `2h`, with

\[
1\le h<L/2.
\]

All other local fluxes are negative.

### Lemma A

The local flux word has primitive period exactly

\[
\boxed{2L.}
\tag{1.1}
\]

### Proof

If a proper period `p` existed, translation by `p` would preserve the two-point defect set

\[
\{0,2h\}\subset\mathbb Z/(2L)\mathbb Z.
\]

A nontrivial translation preserving a two-point set must interchange the two points. Hence

\[
p\equiv2h\pmod{2L},
\qquad
2p\equiv0\pmod{2L}.
\]

The second relation forces `p=L`; then the first forces `2h=L`, contrary to `h<L/2`. Therefore no proper period exists.

The Hamilton-gauge lift has the same primitive period because its local flux word does.

---

## 2. Minimal period at a prescribed `2`-adic jump

Suppose

\[
2^k\Vert s,
\qquad k\ge2.
\]

The reflection-chiral compatibility condition for a two-defect phase is

\[
s=L(2q+1).
\]

Hence `v_2(L)=k`. The smallest admissible half-period is

\[
L=2^k,
\]

and the smallest possible period within this reflection-chiral two-defect mechanism is

\[
\boxed{p_{\min}=2^{k+1}.}
\tag{2.1}
\]

For any fixed `h` and all sufficiently large `k`, one has `h<L/2`, so Lemma A shows that the separation-`2h` phase actually realizes this minimal primitive period.

---

## 3. Near-Dirichlet gaps at the minimal period

For fixed `h`, the global separation theorem gives

\[
L^2\Gamma^{(h)}_{L,q}
\longrightarrow
\kappa_h,
\qquad
\kappa_h=4\arccos^2\!\frac1{T_h(3)},
\tag{3.1}
\]

uniformly in the odd multiplier `2q+1`. Moreover

\[
\kappa_h\nearrow\pi^2.
\tag{3.2}
\]

### Theorem B — epsilon form

For every `epsilon>0`, there exists an integer `h_epsilon` such that for every sufficiently large `k`, every jump

\[
s=2^k(2q+1),
\]

admits an explicit two-defect periodic phase with

\[
\boxed{\operatorname{per}(\tau)=2^{k+1}}
\tag{3.3}
\]

and

\[
\boxed{
2^{2k}\bigl(8-R_s(\tau)\bigr)
>\pi^2-\epsilon.
}
\tag{3.4}
\]

Thus one can approach the Dirichlet quadratic constant arbitrarily closely without paying any extra period beyond the minimum allowed by the `2`-adic reflection mechanism.

### Proof

Choose `h_epsilon` so large that

\[
\kappa_{h_\epsilon}>\pi^2-\epsilon/2.
\]

By the uniform global sharp theorem for this fixed separation, for all sufficiently large `L`, uniformly in `q`,

\[
L^2\Gamma^{(h_\epsilon)}_{L,q}
>\kappa_{h_\epsilon}-\epsilon/2
>\pi^2-\epsilon.
\]

Now set `L=2^k`. For all sufficiently large `k`, `h_epsilon<L/2`, so the phase has primitive period `2L=2^(k+1)` by Lemma A. This proves the theorem.

---

## 4. A diagonal exact-limit theorem

### Theorem C

There exists an integer-valued function

\[
h(k)\longrightarrow\infty
\]

with

\[
h(k)=o(2^k)
\]

such that for every arbitrary sequence of odd integers `n_k`, the jumps

\[
s_k=2^k n_k
\]

admit explicit two-defect phases of primitive period

\[
\boxed{2^{k+1}}
\]

satisfying

\[
\boxed{
2^{2k}\bigl(8-R_{s_k}(\tau^{(k)})\bigr)
\longrightarrow\pi^2.
}
\tag{4.1}
\]

### Proof

For each integer `j>=1`, choose a fixed separation parameter `h_j` so large that

\[
\pi^2-\kappa_{h_j}<1/j.
\]

For this fixed `h_j`, the global sharp-gap theorem is uniform in the odd multiplier. Hence choose `K_j` so large that for every `k>=K_j`, every odd multiplier, and `L=2^k`,

\[
\left|L^2\Gamma^{(h_j)}_{L,q}-\kappa_{h_j}\right|<1/j,
\]

and also

\[
h_j<2^{k-1}.
\]

Increase the `K_j` if necessary so that `K_j` is strictly increasing. Define

\[
h(k)=h_j
\qquad(K_j\le k<K_{j+1}).
\]

Then `h(k)->infinity`, and by enlarging `K_j` once more one may ensure `h_j/2^k<1/j` on the corresponding block, giving `h(k)=o(2^k)`.

For `K_j<=k<K_(j+1)`,

\[
\left|2^{2k}\Gamma^{(h(k))}_{2^k,q}-\pi^2\right|
\le
\left|2^{2k}\Gamma-\kappa_{h_j}\right|
+|\kappa_{h_j}-\pi^2|
<\frac2j.
\]

Thus (4.1) follows. The primitive period is `2^(k+1)` by Lemma A and the `2`-adic compatibility theorem.

---

## 5. Interpretation

The paper now has two distinct routes to the constant `pi^2`:

1. the original long antipodal family reaches `pi^2` through a period growing linearly with the full jump;
2. the separation hierarchy reaches the same constant while using the shortest period permitted by the `2`-adic reflection mechanism.

Therefore the sharp constant `pi^2` is not tied to the old period-`4s` construction. It is a limiting Dirichlet constant of the broader periodic-flux geometry, and it can coexist with optimal `2`-adic period compression.