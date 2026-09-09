# Global defect-separation hierarchy for fixed even defect width

Date: 2026-09-09

Status: **Proved**. This note belongs only to Paper I.

This theorem upgrades `DEFECT_SEPARATION_ROBIN_HIERARCHY.md` from the periodic fiber `z=1` to the full continuous Bloch edge for every fixed even defect separation. It also proves eventual exact phase selection uniformly over the odd multiplier of the jump.

## 1. Setup

Fix an integer

\[
h\ge1
\]

and place the two positive local flux defects at separation `2h` in a period-`2L` word, all other local fluxes being negative. Let

\[
s=L(2q+1),\qquad q\ge0,
\]

and write

\[
R^{(h)}_{L,q}
:=\max_{|z|=1}\rho(H^{(h)}_{L,q}(z))^2,
\qquad
\Gamma^{(h)}_{L,q}:=8-R^{(h)}_{L,q}.
\]

Set

\[
C_h:=T_h(3),
\qquad
\alpha_h:=\arccos\frac1{C_h}.
\tag{1.1}
\]

The endpoint theorem gives

\[
L^2e_{L,h}\to4\alpha_h^2,
\]

where `e_(L,h)` is the gap at `z=1`.

## Theorem A — global sharp fixed-separation gap

For every fixed `h>=1`, for every sequence of even `L->infinity`, and for every arbitrary sequence `q=q(L)>=0`,

\[
\boxed{
L^2\Gamma^{(h)}_{L,q}
\longrightarrow
4\alpha_h^2
=4\arccos^2\!\frac1{T_h(3)}.
}
\tag{1.2}
\]

Thus the convergence is uniform in the odd multiplier in the same sequential sense as in the separation-two compressed theorem.

### Theorem B — phase rigidity

If `z_(L,q)` is any maximizing Bloch phase and

\[
d=z^{2q+1}+z^{-(2q+1)},
\qquad
e=z+z^{-1},
\]

then

\[
\boxed{e\to2,}
\tag{1.3}
\]

and

\[
\boxed{L^2(2-d)\to0.}
\tag{1.4}
\]

Hence the odd part of the jump disappears from the leading global edge for every fixed defect separation.

### Theorem C — multiplier-uniform eventual endpoint locking

For every fixed `h>=1`, there exists an even threshold `L_0(h)` such that for every even

\[
L\ge L_0(h)
\]

and every `q>=0`,

\[
\boxed{
R^{(h)}_{L,q}
=\rho(H^{(h)}_{L,q}(1))^2.
}
\tag{1.5}
\]

Moreover `z=1` is the unique maximizing Bloch phase.

The threshold is not optimized here.

---

## 2. Folded transfer form at a general phase

Choose `eta^2=z` and put

\[
\omega=z^q\eta=e^{i\beta}.
\]

Write

\[
c=\cos\beta,
\qquad
r_\beta=\sin\beta,
\qquad
\mu:=4r_\beta^2=2-d.
\tag{2.1}
\]

After folding by the half-period and applying the same Pauli gauge as in the separation-two compression theorem, the fiber becomes an `L`-site two-component block Jacobi problem.

Outside the defect interval the onsite block is

\[
V_g=2c\,\sigma_x,
\]

while on the `2h` consecutive defect sites it is

\[
V_d=2r_\beta\,\sigma_y.
\]

The transfer coefficients are therefore

\[
A_g=\lambda\sigma_z-2ic\sigma_y,
\qquad
A_d=\lambda\sigma_z+2ir_\beta\sigma_x.
\tag{2.2}
\]

They satisfy the scalar-square identities

\[
A_g^2=(\lambda^2-4c^2)I,
\qquad
A_d^2=(\lambda^2-4r_\beta^2)I.
\tag{2.3}
\]

The monodromy has the form

\[
M=T(A_g)^{L-2h-1}T(A_d)^{2h}T(A_g),
\tag{2.4}
\]

with the same `4 x 4` Bloch closing condition as in the compressed theorem. Since `h` is fixed, the defect transfer is a fixed-size factor; all large-`L` behavior lies in the generic power.

---

## 3. Universal fixed-defect transfer limit

Put

\[
y=8-g
\]

and suppose

\[
g=O(L^{-2}),
\qquad
\mu=O(L^{-2}).
\]

Write `L=2r`.

The generic paired transfer has soft parameter

\[
t_g=1+\frac{\mu-g}{2}.
\tag{3.1}
\]

The defect paired transfer has parameter

\[
t_d=3-\frac{g+\mu}{2}
\longrightarrow3.
\tag{3.2}
\]

Consequently its fixed-width scattering coefficient tends to

\[
\boxed{C_h=T_h(3).}
\tag{3.3}
\]

A direct multiplication of the fixed defect transfer with the Chebyshev representation of the generic power gives the following limiting characteristic laws. The calculation is uniform on compact scaled sets and, after one derivative, in the scaled phase variable.

### Lemma D — elliptic/hyperbolic limiting determinant

If

\[
r^2(g-\mu)\to x^2\ge0,
\qquad e\to e_*,
\]

then in the elliptic regime

\[
\boxed{
P^{(h)}_{L,q,z}(8-g)
\longrightarrow
4C_h^2\cos^2x-(2+e_*).
}
\tag{3.4}
\]

If instead

\[
r^2(\mu-g)\to\kappa^2\ge0,
\]

then in the hyperbolic regime

\[
\boxed{
P^{(h)}_{L,q,z}(8-g)
\longrightarrow
4C_h^2\cosh^2\kappa-(2+e_*).
}
\tag{3.5}
\]

For `h=1`, `C_1=3`; (3.4) becomes

\[
36\cos^2x-(2+e_*)
=34-e_*-36\sin^2x,
\]

which is exactly the limiting Robin law in `GLOBAL_COMPRESSED_SHARP_GAP.md`.

#### Proof of Lemma D

The scalar-square identities (2.3) reduce the generic and defect transfer powers to Chebyshev continuants. For fixed `h`, the defect factor is a polynomial of bounded degree in `(g,mu)` and therefore converges to its endpoint value. Its trace/scattering invariant is `2C_h` by the endpoint transfer calculation.

In the generic block, the standard soft scaling gives

\[
U_{r+O(1)}(t_g)/r
\to\sin x/x
\]

in the elliptic regime and

\[
U_{r+O(1)}(t_g)/r
\to\sinh\kappa/\kappa
\]

in the hyperbolic regime. Substituting these into the fixed `4 x 4` closing determinant, the two chiral channels contribute the factors

\[
2C_h\cos x\pm\sqrt{2+e_*}
\]

or

\[
2C_h\cosh\kappa\pm\sqrt{2+e_*},
\]

whose products are (3.4)--(3.5). The same calculation is valid after one differentiation in a bounded scaled phase variable because all defect factors have fixed degree.

---

## 4. Proof of the global sharp theorem

The endpoint is an admissible Bloch phase, so

\[
0<\Gamma^{(h)}_{L,q}\le e_{L,h}=O(L^{-2}).
\tag{4.1}
\]

Choose a maximizing phase and set

\[
g=\Gamma^{(h)}_{L,q}.
\]

### Hyperbolic roots are impossible

Suppose first that `mu>=g` along a subsequence.

If `r^2(mu-g)` remains bounded, pass to a limit `kappa>=0`. Equation (3.5) and the root condition give

\[
4C_h^2\cosh^2\kappa=2+e_*\le4.
\]

But `C_h>=3`, so the left side is at least `36`, a contradiction.

If

\[
r^2(\mu-g)\to\infty,
\]

the generic transfer is hyperbolic with growing Chebyshev factor. The fixed defect transfer cannot cancel its leading expanding channel: the coefficient is the positive endpoint scattering invariant `C_h>1`. Thus the characteristic determinant diverges in modulus and cannot vanish. This is the same large-hyperbolic exclusion used in the separation-two proof, with only a fixed finite defect factor inserted.

Hence every maximizing near-edge root is eventually elliptic:

\[
0\le\mu<g.
\tag{4.2}
\]

### Elliptic rigidity

Define

\[
h_s=g-\mu=2-2\cos\theta,
\qquad x=r\theta.
\]

Because `h_s<=g<=e_(L,h)`, the endpoint theorem gives

\[
0\le x\le\alpha_h+o(1).
\tag{4.3}
\]

Take a subsequential limit `x->x_*` and `e->e_*`. Lemma D and the root condition yield

\[
4C_h^2\cos^2x_*=2+e_*\le4.
\tag{4.4}
\]

Thus

\[
\cos x_*\le1/C_h.
\]

On the other hand, (4.3) and `alpha_h<pi/2` give

\[
\cos x_*\ge\cos\alpha_h=1/C_h.
\]

Therefore equality is forced:

\[
\boxed{x_*=\alpha_h,\qquad e_*=2.}
\tag{4.5}
\]

Every subsequence has the same limit, so

\[
x\to\alpha_h,
\qquad e\to2.
\]

Since

\[
r^2(g-\mu)\to\alpha_h^2
\]

and the endpoint upper bound gives

\[
\limsup r^2g\le\alpha_h^2,
\]

we must have

\[
\boxed{r^2\mu\to0}
\tag{4.6}
\]

and

\[
\boxed{r^2g\to\alpha_h^2.}
\tag{4.7}
\]

Multiplying by `4` because `L=2r` proves (1.2), while (4.5)--(4.6) give the phase-rigidity statements.

---

## 5. Universal comparison profile at the endpoint energy

Let

\[
y_{L,h}=8-e_{L,h}
\]

be the endpoint top squared eigenvalue. Relax the basic Bloch coordinate to its maximal value `e=2` and put

\[
M=r^2\mu.
\]

The differentiated version of Lemma D gives, locally uniformly in `C^1` on compact `M` intervals,

\[
P^{(h)}_{L}(y_{L,h};M/r^2,e=2)
\longrightarrow\mathcal F_h(M),
\]

where

\[
\boxed{
\mathcal F_h(M)=
\begin{cases}
4C_h^2\cos^2\!\sqrt{\alpha_h^2-M}-4,
&0\le M\le\alpha_h^2,\\[1mm]
4C_h^2\cosh^2\!\sqrt{M-\alpha_h^2}-4,
&M\ge\alpha_h^2.
\end{cases}}
\tag{5.1}
\]

This function has

\[
\boxed{\mathcal F_h(0)=0}
\]

and is strictly increasing for `M>0`. Indeed, on the elliptic side,

\[
\mathcal F_h'(M)
=2C_h^2\frac{\sin(2x)}x>0,
\qquad x=\sqrt{\alpha_h^2-M},
\tag{5.2}
\]

while on the hyperbolic side,

\[
\mathcal F_h'(M)
=2C_h^2\frac{\sinh(2\kappa)}\kappa>0.
\tag{5.3}
\]

At zero,

\[
\boxed{
\mathcal F_h'(0)
=4C_h\frac{\sin\alpha_h}{\alpha_h}>0.
}
\tag{5.4}
\]

Thus the endpoint remains the unique zero of the universal fixed-separation comparison profile.

---

## 6. Proof of eventual exact endpoint locking

Assume by contradiction that there are `L_j->infinity` and positive `mu_j` for which the relaxed endpoint determinant is nonpositive. Put

\[
M_j=r_j^2\mu_j.
\]

If `M_j` has a positive finite limit, (5.1) gives a strictly positive limiting determinant. If `M_j->0`, the `C^1` convergence and (5.4) make the determinant positive for all sufficiently large `j`. If `M_j->infinity`, the hyperbolic expanding-channel estimate makes the determinant diverge positively. Every case is impossible.

Hence for all sufficiently large `L`, depending only on the fixed separation `h`, the relaxed determinant is strictly positive whenever `mu>0`.

For a physical phase,

\[
e\le2,
\]

so the actual determinant is at least the relaxed one. If `d=2` but `z\ne1`, the difference `2-e` is strictly positive. Therefore the endpoint energy can be a Bloch root only at `z=1`.

The endpoint top root is simple. On the punctured Bloch circle the number of squared roots above the endpoint energy is locally zero near `z=1` and cannot change without a crossing of the endpoint energy or of `8`; both are excluded. The punctured circle is connected, so this number is identically zero.

Thus `z=1` uniquely attains the global edge for every `L>=L_0(h)` and every odd multiplier, proving Theorem C.

---

## 7. Hierarchy of global sharp constants

Combining Theorem A with the monotonicity of `T_h(3)` gives

\[
\boxed{
4\arccos^2\frac13
<4\arccos^2\frac1{17}
<4\arccos^2\frac1{99}
<\cdots<\pi^2,
}
\tag{7.1}
\]

now as **global continuous Bloch gap constants**, not merely periodic-fiber constants.

Therefore the paper contains two independent arithmetic/geometric hierarchies:

1. `2`-adic compression controls how short a period can be chosen for a given jump;
2. even defect separation controls the sharp quadratic gap constant within a fixed compressed period scale.

As the fixed defect separation grows, the global Robin constant approaches the Dirichlet value `pi^2` exponentially fast.