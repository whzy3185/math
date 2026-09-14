# Exact quarter-period optimality in the `v_2(s)=5` minimal layer

Date: 2026-09-14

Status: **Proved** with exact rational Bernstein and derivative certificates.

## 1. Minimal cell and separator

For

\[
2^5\Vert s,
\]

the minimal compatible half-period is `L=32` and the primitive coefficient period is

\[
p=64.
\]

Write

\[
N+m=L/2=16.
\]

The quarter-period geometry is

\[
\boxed{N=m=8,\qquad h=16=p/4.}
\]

Choose

\[
\boxed{
g_0=\frac1{32},
\qquad
y_0=8-g_0=\frac{255}{32}.}
\tag{1.1}
\]

Every unbalanced geometry has

\[
M:=\max\{N,m\}\ge9.
\]

The universal endpoint Dirichlet bound gives

\[
\Gamma_{N,m,q}<D_M\le D_9,
\qquad
D_9=2-2\cos\frac\pi{18}.
\]

Since `cos x>1-x^2/2` and `pi^2<10`,

\[
D_9<\frac{\pi^2}{324}<\frac{10}{324}=\frac5{162}<\frac1{32}.
\tag{1.2}
\]

Hence every unbalanced competitor has gap smaller than `1/32`.

---

## 2. Relaxed balanced determinant

Use `ALL_ENERGY_SINGLE_SQUARE_IDENTITY.md` with `N=m=8` and `y=255/32`.  After substituting

\[
d=4t-2,
\qquad0\le t\le1,
\]

the relaxed polynomial

\[
P_{8,8}(255/32;4t-2,2)
\]

has degree `32` in `t`.

Its exact degree-32 Bernstein representation has **33 strictly positive rational coefficients**.  The smallest is the endpoint coefficient

\[
\boxed{
\frac{
2118132998931575580037811628419985641741174001788817920001
}{
1461501637330902918203684832716283019655932542976
}
>1.4\times10^9.
}
\tag{2.1}
\]

Therefore

\[
\boxed{
P_{8,8}(255/32;d,2)>0
\qquad(-2\le d\le2).
}
\tag{2.2}
\]

For a physical phase `e=z+z^{-1}<=2`, the all-energy characteristic identity gives

\[
P_{8,8,q,z}(255/32)
=P_{8,8}(255/32;d,2)+(2-e)>0.
\tag{2.3}
\]

---

## 3. Reference-fiber inertia

At `z=1`, the balanced squared characteristic polynomial factors into two monic degree-16 integer polynomials,

\[
P_{8,8,1}(y)=f_-(y)f_+(y).
\tag{3.1}
\]

Exact evaluation at `y_0=255/32` gives

\[
f_-(y_0)>0,
\qquad
f_+(y_0)>0.
\]

More strongly, for each factor all derivatives of orders `0,1,...,16` are strictly positive at `y_0`. The exact first values are, for one factor,

\[
f_-(y_0)=
\frac{46020769141928035260625135617}
{1208925819614629174706176}>0,
\]

\[
f_-'(y_0)=
\frac{75018525778873397975043243391}
{2361183241434822606848}>0,
\]

and

\[
f_-''(y_0)=
\frac{40941183979113520462714345743}
{73786976294838206464}>0.
\]

The second factor has the same positive derivatives from order one onward and a positive zeroth value.

Since the top derivative is a positive constant, downward induction shows that every derivative, and hence both factors themselves, remain positive on `[y_0,infinity)`. Thus the reference fiber has no squared eigenvalue at or above `y_0`.

By (2.3), no Bloch fiber can cross `y_0`; inertia is constant around the circle. Consequently

\[
\boxed{
R_{8,8,q}<\frac{255}{32},
\qquad
\Gamma_{8,8,q}>\frac1{32}.
}
\tag{3.2}

---

## Theorem — exact `k=5` optimizer

Combining (1.2) and (3.2), for every odd multiplier,

\[
\boxed{
\Gamma_{8,8,q}
>
\Gamma_{N,m,q}
\qquad
(N+m=16,\ (N,m)\ne(8,8)).
}
\]

Therefore every jump

\[
s=32(2q+1)
\]

has, inside the minimal primitive period `64`, a unique gap-maximizing even-separation reflection-chiral two-defect geometry:

\[
\boxed{h=16=p/4.}
\]

The accompanying verifier reconstructs the all-energy polynomial, converts it to the Bernstein basis with exact rational arithmetic, and checks the endpoint derivative certificate.
