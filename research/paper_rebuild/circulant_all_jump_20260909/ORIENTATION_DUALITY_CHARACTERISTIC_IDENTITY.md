# Exact orientation-duality identity for the all-energy characteristic

Date: 2026-09-14

Status: **Proved**.

This identity compares the two orientations obtained by interchanging the generic and defect arcs.  It is the natural algebraic tool for the remaining `p=8r+4` orientation problem.

## 1. Setup

For a geometry `(N,m)` define

\[
P_{N,m}(y;d,e)
\]

by the all-energy single-square identity

\[
P_{N,m}(y;d,e)
=4\left[Z_{N,m}(y,d)^2-1+(d-2)U_{m-1}(a)^2\right]+(2-e),
\]

where

\[
x=\frac{y-d-4}{2},
\qquad
a=\frac{y+d-4}{2},
\]

and

\[
Z_{N,m}(y,d)
=T_N(x)T_m(a)+(ax-3)U_{N-1}(x)U_{m-1}(a).
\]

Interchanging the two arcs sends

\[
(N,m,d)\longmapsto(m,N,-d).
\]

## Theorem — exact duality defect

For every `N,m>=1`, every complex squared energy `y`, and all phase coordinates `(d,e)`,

\[
\boxed{
\begin{aligned}
&P_{N,m}(y;d,e)-P_{m,N}(y;-d,e)\\
&\qquad=4\left[
(d-2)U_{m-1}(a)^2
+(d+2)U_{N-1}(x)^2
\right].
\end{aligned}}
\tag{1.1}

Equivalently,

\[
\boxed{
P_{N,m}(y;d,e)-P_{m,N}(y;-d,e)
=4\left[(d+2)u^2-(2-d)p^2\right],
}
\tag{1.2}

where

\[
u=U_{N-1}(x),
\qquad p=U_{m-1}(a).
\]

Thus the entire orientation asymmetry is carried by one explicit difference of Chebyshev squares.

---

## 2. Proof

For the swapped geometry evaluated at `-d`, the two energy arguments are

\[
x'=\frac{y-(-d)-4}{2}=a,
\qquad
a'=\frac{y+(-d)-4}{2}=x.
\]

Therefore

\[
T_m(x')T_N(a')
=T_m(a)T_N(x),
\]

and

\[
(a'x'-3)U_{m-1}(x')U_{N-1}(a')
=(ax-3)U_{m-1}(a)U_{N-1}(x).
\]

Hence

\[
\boxed{
Z_{m,N}(y,-d)=Z_{N,m}(y,d).
}
\tag{2.1}

The seam term `2-e` is also unchanged.  Subtracting the two single-square formulas therefore cancels the complete square, the constant term, and the seam term.  Only the orientation terms remain:

\[
4(d-2)U_{m-1}(a)^2
-4((-d)-2)U_{N-1}(x)^2,
\]

which is exactly (1.1).

---

## 3. Endpoint checks

At

\[
d=2,
\]

formula (1.2) becomes

\[
P_{N,m}(y;2,e)-P_{m,N}(y;-2,e)
=16U_{N-1}\!\left(\frac{y-6}{2}\right)^2\ge0.
\]

At

\[
d=-2,
\]

it becomes

\[
P_{N,m}(y;-2,e)-P_{m,N}(y;2,e)
=-16U_{m-1}\!\left(\frac{y-6}{2}\right)^2\le0.
\]

Thus the two orientations exchange their endpoint advantage exactly as expected.

---

## 4. Near-balanced specialization

For the two nearest-balanced orientations in a period `p=8r+4`, take

\[
(N,m)=(r+1,r)
\]

and its swap `(r,r+1)`. Then

\[
\boxed{
P_{r+1,r}(y;d,e)-P_{r,r+1}(y;-d,e)
=4\left[(d+2)U_r(x)^2-(2-d)U_{r-1}(a)^2\right].
}
\tag{4.1
}

This reduces the finite orientation comparison to the relative growth of two consecutive Chebyshev channels.  In particular, in the periodic boundary layer `d=2-O(r^-4)` the first term is algebraically dominant, while the paired compressed-antiperiodic channel lies at `-d=-2+O(r^-4)`.

The remaining physical-seam mismatch between paired Bloch phases is beyond the algebraic scale and is controlled by `ANTIPERIODIC_SEAM_TUNNELING_ASYMPTOTIC.md`.

## 5. Significance

The identity explains why the orientation splitting is a fourth-order effect near balance.  The large common scattering square cancels exactly; only the small imbalance between the two soft-channel Chebyshev amplitudes survives.

It is also suitable for an effective `r>=9` proof of the `p=8r+4` orientation theorem, because the sign problem has been reduced from two full characteristic determinants to one explicit scalar difference.