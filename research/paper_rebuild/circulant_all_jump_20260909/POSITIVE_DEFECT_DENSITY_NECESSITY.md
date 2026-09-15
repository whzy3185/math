# Positive defect density is necessary for an order-one spectral gap

Date: 2026-09-15

Status: **Proved**.

This theorem applies to the **complete periodic flux class**, not only to the two-defect or `DDGG` constructions.  It gives a quantitative obstruction to producing a fixed gap below `8` with a sparse number of positive flux defects.

---

## 1. Setup

Let the coefficient period be

\[
p=2L
\]

and take the half-period jump

\[
s=L.
\]

Let

\[
Q=(Q_0,\ldots,Q_{p-1})\in\{\pm1\}^p
\]

be any legal periodic flux word, and write

\[
\boxed{
d(Q)=\#\{j:Q_j=+1\}.}
\tag{1.1}
\]

Let

\[
R(Q)=\max_{|z|=1}\rho(H_Q(z))^2
\]

be its continuous squared Bloch edge.

---

# Theorem A — sparse-defect lower bound

If `d=d(Q)>=1`, then there exists an integer

\[
\ell\ge \frac{L}{d}
\]

such that

\[
\boxed{
R(Q)
\ge
4+4\cos^2\frac{\pi}{\ell+1}.
}
\tag{2.1}
\]

Consequently

\[
\boxed{
8-R(Q)
\le
16\pi^2\left(\frac{d}{p}\right)^2.
}
\tag{2.2}
\]

For `d=0`, the folded type is constant on the whole half-cell and the same argument gives

\[
R(Q)\ge4+4\cos^2\frac{\pi}{L+1},
\]

while the standard all-negative periodic phase in fact has edge `8`.

---

## 2. Folded type sequence

Choose a Hamilton-gauge lift

\[
\tau_{j+1}=Q_j\tau_j,
\qquad \tau_0=1.
\]

For the half-period folding define

\[
\boxed{
\varepsilon_j:=\tau_j\tau_{j+L}\in\{\pm1\},
\qquad 0\le j<L.
}
\tag{3.1}
\]

Then

\[
\begin{aligned}
\varepsilon_j\varepsilon_{j+1}
&=(\tau_j\tau_{j+L})(\tau_{j+1}\tau_{j+L+1})\\
&=(\tau_j\tau_{j+1})(\tau_{j+L}\tau_{j+L+1})\\
&=\boxed{Q_jQ_{j+L}.}
\end{aligned}
\tag{3.2}
\]

Thus the folded type changes between sites `j` and `j+1` exactly when the pair

\[
(Q_j,Q_{j+L})
\]

contains one positive and one negative flux.

Let `C` be the number of changes of the cyclic binary sequence `epsilon`.  Every changing pair uses exactly one positive flux site, and the `L` pairs partition the `p` original sites. Therefore

\[
\boxed{C\le d.}
\tag{3.3}
\]

If `C=0`, the folded type is constant on all `L` sites.  If `C>0`, the cyclic sequence consists of `C` constant runs, so its longest run has length

\[
\boxed{
\ell\ge\left\lceil\frac{L}{C}\right\rceil
\ge\frac{L}{d}.
}
\tag{3.4}
\]

---

## 3. Uniform local chain inside a constant run

Fold the Bloch fiber into the standard two-component chain.  On a constant `epsilon` run, after a local unitary gauge the onsite blocks are all of one of the two forms

\[
G:\quad 2\cos\beta\,\sigma_x,
\]

or

\[
D:\quad 2\sin\beta\,\sigma_y,
\]

and the nearest-neighbor block can be gauged to `sigma_z` along the interval.

Choose the compressed phase according to the type of the longest run:

- for a `G` run take `beta=0`;
- for a `D` run take `beta=pi/2`.

In either case the restriction to the run is unitarily equivalent to the length-`ell` Dirichlet block chain

\[
K_\ell
=
2\sigma_x\otimes I_\ell
+\sigma_z\otimes A(P_\ell)
\]

(up to replacing `sigma_x` by the unitarily equivalent `sigma_y`), where `A(P_ell)` is the path adjacency matrix.

Because `sigma_x` and `sigma_z` anticommute,

\[
K_\ell^2
=4I+A(P_\ell)^2.
\tag{4.1}
\]

The largest path eigenvalue is

\[
2\cos\frac{\pi}{\ell+1},
\]

so

\[
\boxed{
\rho(K_\ell)^2
=4+4\cos^2\frac{\pi}{\ell+1}.
}
\tag{4.2}
\]

---

## 4. Embedding the Dirichlet test vector

Let `psi` be a top eigenvector of `K_ell`, extended by zero outside the constant folded run.

For the full fiber `H`, the internal part of `H psi` is exactly `K_ell psi`.  Couplings across the two interval boundaries only add extra components outside the support.  Hence

\[
\|H\psi\|^2
\ge
\|K_\ell\psi\|^2.
\]

Therefore the Rayleigh principle for `H^2` gives

\[
\rho(H)^2
\ge
\frac{\|H\psi\|^2}{\|\psi\|^2}
\ge
\rho(K_\ell)^2,
\]

which proves (2.1).

Finally

\[
8-R(Q)
\le
4\sin^2\frac{\pi}{\ell+1}
\le
\frac{4\pi^2}{(\ell+1)^2}
\le
\frac{4\pi^2d^2}{L^2}
=16\pi^2\left(\frac dp\right)^2,
\]

proving (2.2).

---

# Corollary B — an order-one gap forces positive defect density

Let `Q_p` be any sequence of legal half-period-jump periodic flux words with `p->infinity`.  If

\[
\boxed{
d(Q_p)=o(p),}
\]

then

\[
\boxed{
\liminf_{p\to\infty}R(Q_p)\ge8.
}
\tag{5.1}
\]

In particular no sparse-defect sequence can maintain a fixed positive gap below `8`.

More quantitatively, if for some `delta>0`

\[
R(Q_p)\le8-\delta
\]

for all sufficiently large `p`, then

\[
\boxed{
\frac{d(Q_p)}p
\ge
\frac{\sqrt\delta}{4\pi}.
}
\tag{5.2}
\]

Thus a uniform spectral gap requires a defect density bounded away from zero.

---

## 5. Application to the `DDGG` staircase

`MULTIDEFECT_STAIRCASE_UNIFORM_GAP_THEOREM.md` constructs words with

\[
\frac{d(p)}p\to\frac14
\]

and

\[
R(Q_p)\to R_\infty<8.
\]

The present theorem proves that the transition from the optimized two-defect family to this positive-density regime is not optional: **some positive density of flux defects is mathematically necessary for an order-one gap**.

Hence the paper now has a structural dichotomy over the complete periodic class:

\[
\boxed{
\text{sparse defects}\Rightarrow R\to8,
\qquad
\text{positive-density `DDGG` order}\Rightarrow R\to R_\infty<8.
}
\]
