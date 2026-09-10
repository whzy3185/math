# Exponential convergence of the defect-separation Robin constants

Date: 2026-09-10

Status: **Proved**. This note belongs only to Paper I.

For fixed even defect separation `h=2m`, the sharp endpoint theorem gives the leading constant

\[
C_m:=4\alpha_m^2,
\qquad
\alpha_m=\arccos\frac1{T_m(3)}.
\]

The constants increase to `pi^2`. This note gives the exact exponential scale of that convergence.

## Theorem

Let

\[
\Lambda:=3+2\sqrt2.
\]

Then as `m->infinity`,

\[
\boxed{
\pi^2-C_m
=8\pi\Lambda^{-m}
-16\Lambda^{-2m}
+O(\Lambda^{-3m}).
}
\tag{1}
\]

In particular,

\[
\boxed{
\pi^2-C_m\sim8\pi(3+2\sqrt2)^{-m}.}
\tag{2}
\]

Thus the approach to the Dirichlet constant is exponentially fast in half the defect separation.

## Proof

Since

\[
T_m(3)=\cosh(m\,\operatorname{arcosh}3)
=\frac{\Lambda^m+\Lambda^{-m}}2,
\]

we have

\[
\varepsilon_m:=\frac1{T_m(3)}
=\frac{2\Lambda^{-m}}{1+\Lambda^{-2m}}
=2\Lambda^{-m}-2\Lambda^{-3m}+O(\Lambda^{-5m}).
\tag{3}
\]

Now

\[
\alpha_m=\arccos\varepsilon_m
=\frac\pi2-\arcsin\varepsilon_m.
\]

Put

\[
u_m:=\arcsin\varepsilon_m.
\]

Since

\[
u_m=\varepsilon_m+\frac{\varepsilon_m^3}{6}+O(\varepsilon_m^5),
\]

we obtain

\[
\begin{aligned}
\pi^2-C_m
&=\pi^2-4\left(\frac\pi2-u_m\right)^2\\
&=4\pi u_m-4u_m^2\\
&=4\pi\varepsilon_m-4\varepsilon_m^2+O(\varepsilon_m^3).
\end{aligned}
\]

Substituting (3) yields

\[
\pi^2-C_m
=8\pi\Lambda^{-m}-16\Lambda^{-2m}+O(\Lambda^{-3m}),
\]

which is (1).

## Consequence

The first constants are

\[
C_1=4\arccos(1/3)^2,
\]

\[
C_2=4\arccos(1/17)^2,
\]

\[
C_3=4\arccos(1/99)^2,
\]

and so on, because

\[
T_1(3)=3,\quad T_2(3)=17,\quad T_3(3)=99,\quad T_4(3)=577,\ldots
\]

The rapid growth of `T_m(3)` explains why even modest defect separations already produce endpoint constants very close to `pi^2`.