# Symmetric integer edge scaling across the Pell transition

Date: 2026-09-10

Status: **Proved**. This is a sharp corollary of the Pell critical crossover profile.

## 1. Exact safe and unsafe boundary integers

Put

\[
U_N:=U_{N-1}(3),
\qquad
T_N:=T_N(3),
\]

and define the largest safe defect parameter

\[
\boxed{
M_N:=\frac{T_N-1}{2}.
}
\tag{1.1}
\]

The Pell identity gives

\[
\boxed{M_N(M_N+1)=2U_N^2.}
\tag{1.2}
\]

Thus `m=M_N` is the last sub-eight integer geometry and `m=M_N+1` is the first super-eight geometry.

Let

\[
\lambda^-_{N,m}:=\rho(H_{N,m,q}(-1))^2.
\]

## Theorem A — last safe integer

As `N->infinity`,

\[
\boxed{
8-\lambda^-_{N,M_N}
\sim
\frac{3}{4\sqrt2\,U_N^3}.
}
\tag{2.1}
\]

## Theorem B — first unsafe integer

As `N->infinity`,

\[
\boxed{
\lambda^-_{N,M_N+1}-8
\sim
\frac{3}{4\sqrt2\,U_N^3}.
}
\tag{2.2}
\]

Hence the two adjacent integer geometries approach the spectral threshold from opposite sides with the same leading constant.

Since

\[
U_N
\sim\frac{(3+2\sqrt2)^N}{4\sqrt2},
\]

both statements are equivalently

\[
\boxed{
|\lambda^-_{N,m}-8|
\sim96(3+2\sqrt2)^{-3N}
}
\tag{2.3}
\]

for `m=M_N` or `m=M_N+1`, with the sign determined by the side of the transition.

---

## 2. Safe-side critical ratio

Set

\[
c_N^-:=\frac{M_N}{U_N}.
\]

Using

\[
T_N^2=8U_N^2+1,
\]

we have

\[
T_N
=2\sqrt2\,U_N
+\frac{1}{4\sqrt2\,U_N}
+O(U_N^{-3}).
\tag{3.1}
\]

Therefore

\[
\begin{aligned}
c_N^-
&=\frac{T_N-1}{2U_N}\\
&=\sqrt2-\frac1{2U_N}
+O(U_N^{-2}).
\end{aligned}
\tag{3.2}
\]

Write

\[
c_N^-=\sqrt2(1-\varepsilon_N^-).
\]

Then

\[
\boxed{
\varepsilon_N^-
=\frac{1}{2\sqrt2\,U_N}
+O(U_N^{-2}).
}
\tag{3.3}
\]

The subcritical crossover theorem gives a parameter `x_N` satisfying

\[
x_N\cot x_N=1-\varepsilon_N^-,
\]

and

\[
M_N^2\bigl(8-\lambda^-_{N,M_N}\bigr)
\sim x_N^2.
\]

Since

\[
x\cot x
=1-\frac{x^2}{3}+O(x^4),
\]

we obtain

\[
\boxed{
x_N^2
=3\varepsilon_N^-+O((\varepsilon_N^-)^2)
=\frac{3}{2\sqrt2\,U_N}+O(U_N^{-2}).}
\tag{3.4}
\]

From (1.2),

\[
M_N^2=2U_N^2+O(U_N),
\]

so division yields

\[
8-\lambda^-_{N,M_N}
=\frac{3}{4\sqrt2\,U_N^3}(1+o(1)),
\]

proving Theorem A.

---

## 3. Unsafe-side critical ratio

Similarly put

\[
c_N^+:=\frac{M_N+1}{U_N}.
\]

Equation (3.1) gives

\[
\boxed{
c_N^+
=\sqrt2+\frac1{2U_N}+O(U_N^{-2}).}
\tag{4.1}
\]

Write

\[
c_N^+=\sqrt2(1+\varepsilon_N^+).
\]

Then

\[
\varepsilon_N^+
=\frac{1}{2\sqrt2\,U_N}+O(U_N^{-2}).
\]

The supercritical crossover theorem gives `kappa_N` with

\[
\kappa_N\coth\kappa_N=1+\varepsilon_N^+,
\]

and

\[
(M_N+1)^2\bigl(\lambda^-_{N,M_N+1}-8\bigr)
\sim\kappa_N^2.
\]

Since

\[
\kappa\coth\kappa
=1+\frac{\kappa^2}{3}+O(\kappa^4),
\]

we obtain

\[
\kappa_N^2
=\frac{3}{2\sqrt2\,U_N}+O(U_N^{-2}).
\]

Also

\[
(M_N+1)^2=2U_N^2+O(U_N).
\]

Hence

\[
\lambda^-_{N,M_N+1}-8
=\frac{3}{4\sqrt2\,U_N^3}(1+o(1)),
\]

proving Theorem B.

---

## 4. Conversion to the Pell fundamental unit

Let

\[
\Lambda=3+2\sqrt2.
\]

Then

\[
U_N=U_{N-1}(3)
=\frac{\Lambda^N-\Lambda^{-N}}{4\sqrt2}
\sim\frac{\Lambda^N}{4\sqrt2}.
\]

Therefore

\[
\frac{3}{4\sqrt2}U_N^{-3}
\sim
\frac{3}{4\sqrt2}(4\sqrt2)^3\Lambda^{-3N}
=96\Lambda^{-3N},
\]

which proves (2.3).

## 5. Interpretation

The exact integer phase diagram has no geometry with spectral edge exactly equal to `8`, because `T_N(3)` is odd while `2m` is even. Nevertheless the two integers adjacent to the Pell boundary become asymptotically symmetric about the threshold:

\[
M_N\quad\text{safe},
\qquad
M_N+1\quad\text{unsafe},
\]

with the same exponentially small displacement `96 Lambda^{-3N}`.

Thus the discrete arithmetic transition has a sharply resolved spectral boundary layer one exponential order thinner than the natural defect scale `m^{-2} ~ Lambda^{-2N}`.