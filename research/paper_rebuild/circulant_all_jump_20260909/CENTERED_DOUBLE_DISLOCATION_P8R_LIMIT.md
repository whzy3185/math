# Centered double-dislocation family for periods `8r`

Date: 2026-09-15

Status: **Proved**.

This theorem gives the asymptotic counterpart of the exact period-24, 32, and 40 multi-defect constructions.  It shows that the complementary `p=8r` staircase converges to the same algebraic `DDGG` dislocation constant as the infinite `p=8r+4` family.

---

## 1. Explicit family

Let

\[
p=8r,\qquad s=4r,\qquad r\ge3.
\]

Put

\[
\ell_r=
\begin{cases}
r,&r\text{ odd},\\
r-1,&r\text{ even},
\end{cases}
\]

and define the legal flux word by

\[
\boxed{
Q_j=+1
\iff
j\in\{0,2,4,\ldots,4r-4\}\setminus\{2\ell_r\}.
}
\tag{1.1}
\]

Thus the word has

\[
\boxed{2r-2}
\]

positive flux defects.

Let

\[
a_r=\left\lceil\frac{r-2}{2}\right\rceil,
\qquad
b_r=\left\lfloor\frac{r-2}{2}\right\rfloor.
\tag{1.2}
\]

After folding by the half-period and applying the standard local Pauli gauge, the onsite word is exactly

\[
\boxed{
W_r
=G(DDGG)^{a_r}\,DDDD\,GG\,(DDGG)^{b_r}G.
}
\tag{1.3}
\]

For `r=3,4,5`, (1.1) gives respectively the already proved period-24, 32, and 40 constructions.

The cyclic positive-site gap sequence has one unique gap of length `4r+4`, so the flux word has primitive period exactly `8r`.

---

## 2. Two separated dislocations

The cyclic word (1.3) consists of the uniformly hyperbolic `DDGG` bulk with two local defects:

1. the seam produces a `GGGG` dislocation;
2. the central block produces the dual `DDDD` dislocation.

Their bulk separations are `a_r` and `b_r` motifs, and

\[
\min\{a_r,b_r\}\to\infty.
\tag{2.1}
\]

The `GGGG` isolated dislocation is exactly the one analyzed in `DDGG_DISLOCATION_ALGEBRAIC_LIMIT.md`.  Its top squared bound-state edge is

\[
\boxed{
R_\infty
=7.70074090635371823740834037867\ldots,
}
\tag{2.2}
\]

namely the unique root of the degree-18 polynomial `P_18` in `(7.7007,7.7008)`.

The corresponding compressed phase is

\[
d_\infty
=1.99290373256884878015491534997\ldots.
\tag{2.3}
\]

---

## 3. D/G duality of the isolated defects

Replace

\[
\beta\mapsto\beta+\frac\pi2.
\]

Then

\[
\cos\beta\mapsto-\sin\beta,
\qquad
\sin\beta\mapsto\cos\beta,
\]

and hence, after a fixed Pauli rotation and harmless local signs,

\[
G\longleftrightarrow D.
\]

At the same time

\[
d=2\cos(2\beta)\longmapsto-d.
\]

Therefore a `DDDD` dislocation in `DDGG` bulk is unitarily equivalent to a `GGGG` dislocation at the reflected compressed phase.  In particular its isolated top edge is the same number `R_infty`, attained at `-d_infty`.

Thus the two separated local defects in (1.3) have identical isolated spectral edges but at opposite phase wells.

---

## 4. Exact exponential dichotomy of the bulk transfer

For general squared energy `y` and compressed phase `d`, the four-site bulk transfer `B(y,d)` satisfies

\[
B^2-\mathcal A(y,d)B+I_4=0,
\qquad
\mathcal A(y,d)=y^2-8y+10-d^2.
\tag{4.1}
\]

On a sufficiently small compact neighborhood `K` of either isolated maximizing point

\[
(R_\infty,\pm d_\infty),
\]

one has

\[
\mathcal A\ge2+\delta_0
\]

for some `delta_0>0`.  Define

\[
\rho(y,d)=
\frac{\mathcal A-\sqrt{\mathcal A^2-4}}2.
\]

Then there is `0<rho_0<1` such that `rho<=rho_0` on `K`, and the exact spectral projectors

\[
P_u=\frac{B-\rho I}{\rho^{-1}-\rho},
\qquad
P_s=\frac{\rho^{-1}I-B}{\rho^{-1}-\rho}
\tag{4.2}
\]

satisfy

\[
\boxed{
B^n=\rho^{-n}P_u+\rho^nP_s.
}
\tag{4.3}
\]

After division by the expanding factor `rho^{-n}`, every long bulk segment therefore differs from the unstable projector `P_u` by

\[
O(\rho_0^{2n})
\tag{4.4}
\]

with all fixed derivatives in `(y,d)`.

---

## 5. Decoupling of the two dislocations

Write the full transfer matching determinant of (1.3) as

\[
\mathcal E_{a,b}(y,d).
\]

Insert (4.3) in the two bulk powers `B^a,B^b` and normalize by the two expanding factors.  Since every remaining transfer factor belongs to the fixed finite word

\[
G\,DDDD\,GG\,G,
\]

the normalized determinant is analytic and has the form

\[
\boxed{
\widetilde{\mathcal E}_{a,b}(y,d)
=
\mathcal E_G(y,d)\,C_D(y,d)
+O(\rho_0^{2a}+\rho_0^{2b})
}
\tag{5.1}
\]

near `(R_infty,d_infty)`.  Here

- `mathcal E_G=0` is the isolated `GGGG` Evans equation, identical to `F_infty=0` from `DDGG_DISLOCATION_ALGEBRAIC_LIMIT.md` up to a nonzero analytic factor;
- `C_D(R_infty,d_infty) != 0`, because the isolated `DDDD` defect resonates at the reflected phase `-d_infty`, not at `d_infty`.

The same formula with `G,D` interchanged holds near `(R_infty,-d_infty)`.

The isolated root is simple and its phase maximum is nondegenerate.  Therefore analytic root perturbation applied to (5.1) gives two conjugate/reflected finite-ring wells whose top values differ from `R_infty` by at most

\[
O(\rho_0^{2\min(a,b)}).
\]

---

## Theorem A — common algebraic limit

Let

\[
R_r^{(8)}
=\max_{|z|=1}\rho(H_{Q^{(r)}}(z))^2
\]

for the period-`8r` flux word (1.1).  Then

\[
\boxed{
R_r^{(8)}\longrightarrow R_\infty,
}
\tag{6.1}
\]

and in fact

\[
\boxed{
R_r^{(8)}-R_\infty
=O\!\left(\rho_0^{\,2\min(a_r,b_r)}\right).
}
\tag{6.2}
\]

Every maximizing compressed phase approaches one of

\[
\boxed{\pm d_\infty.}
\tag{6.3}
\]

Thus the `p=8r` and `p=8r+4` staircases have the same infinite-volume dislocation edge.

---

## Corollary B — eventual strict improvement over every two-defect phase

Since

\[
R_\infty<31/4,
\]

there exists an integer `r_0` such that for every `r>=r_0`,

\[
R_r^{(8)}<31/4.
\tag{7.1}
\]

On the other hand the best two-defect gap at period `8r` is at most the universal Dirichlet quantity associated with soft length `r`; hence its edge tends to `8`.  In particular, for all sufficiently large `r`,

\[
R_{2\rm def}^{(8r)}>31/4.
\]

Therefore

\[
\boxed{
R_r^{(8)}<31/4<R_{2\rm def}^{(8r)}
}
\tag{7.2}
\]

for every sufficiently large `r`.

Together with the exact period-24, 32, and 40 theorems, this proves that the complementary staircase is not a finite-period accident and persists for an infinite tail.

---

## 8. Interpretation

The defect-number staircase now has a single infinite-volume explanation.

- `p=8r+4`: one `GGGG` dislocation in `DDGG` bulk;
- `p=8r`: a `GGGG/DDDD` dual pair separated by two growing hyperbolic bulk segments.

Both converge to the same algebraic spectral constant `R_infty`.  The period parity changes only the number and interaction of dislocations, not the isolated bound-state energy.