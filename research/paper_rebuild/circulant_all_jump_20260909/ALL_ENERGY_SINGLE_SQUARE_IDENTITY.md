# Single-square all-energy characteristic identity

Date: 2026-09-14

Status: **Proved**. This is the arbitrary-energy analogue of `SQUARE_FORM_THRESHOLD_IDENTITY.md`.

## 1. Setup

Use the general even-separation notation

\[
L=2(N+m),\qquad h=2m,
\]

and define

\[
x=\frac{y-d-4}{2},
\qquad
a=\frac{y+d-4}{2}.
\]

Put

\[
u=U_{N-1}(x),\qquad X=T_N(x),
\]

\[
p=U_{m-1}(a),\qquad Y=T_m(a).
\]

The all-energy characteristic formula is

\[
P(y;d,e)
=A u^2p^2-2KXYup+Bp^2+Cu^2-e+2,
\]

with the coefficients in `GENERAL_SEPARATION_ALL_ENERGY_CHARACTERISTIC.md`.

## Theorem — exact single-square collapse

Define

\[
\boxed{
Z_{N,m}(y,d)
:=XY+(ax-3)up.
}
\tag{1.1}
\]

Then for every complex `y`, every Bloch phase, and every `N,m>=1`,

\[
\boxed{
P(y;d,e)
=4\Bigl[Z_{N,m}(y,d)^2-1+(d-2)p^2\Bigr]+(2-e).
}
\tag{1.2}

Equivalently, at the relaxed seam value `e=2`,

\[
\boxed{
P(y;d,2)
=4\Bigl[Z_{N,m}(y,d)^2-1-(2-d)U_{m-1}(a)^2\Bigr].
}
\tag{1.3}

Thus positivity at a test energy reduces to the scalar comparison

\[
\boxed{
Z_{N,m}(y,d)^2
>1+(2-d)U_{m-1}(a)^2.
}
\tag{1.4}

---

## 2. Proof

Rewrite the all-energy coefficients in the variables `(x,a)`. Since

\[
y=x+a+4,
\qquad
d=a-x,
\]

a direct substitution gives

\[
K=-4(ax-3),
\]

\[
A=4\bigl(2a^2x^2-a^2-x^2-6ax+10\bigr),
\]

\[
B=4(a^2+a-x-3),
\qquad
C=4(x^2-1).
\tag{2.1}
\]

The Chebyshev identities are

\[
X^2-1=(x^2-1)u^2,
\qquad
Y^2-1=(a^2-1)p^2.
\tag{2.2}
\]

Expanding the square in (1.1),

\[
\begin{aligned}
Z^2-1
={}&2(ax-3)XYup+(x^2-1)u^2+(a^2-1)p^2\\
&+\Bigl[(x^2-1)(a^2-1)+(ax-3)^2\Bigr]u^2p^2.
\end{aligned}
\tag{2.3}
\]

The mixed coefficient satisfies

\[
(x^2-1)(a^2-1)+(ax-3)^2
=2a^2x^2-a^2-x^2-6ax+10.
\tag{2.4}
\]

Also

\[
(a^2-1)+(d-2)
=a^2+a-x-3,
\tag{2.5}
\]

because `d=a-x`. Multiplying (2.3) by four and using (2.4)--(2.5) reproduces exactly the four all-energy coefficients in (2.1). Finally restore the seam term `2-e`. This proves (1.2).

---

## 3. Checks

At `y=8`,

\[
x=\frac{4-d}{2},
\qquad a=\frac{4+d}{2},
\]

and

\[
d-2=-2(x-1).
\]

Equation (1.2) becomes

\[
P(8;d,e)
=4Z^2-8(x-1)p^2-4+(2-e),
\]

which is exactly the previously proved threshold square identity.

At `d=2`, the negative term in (1.3) disappears, so the test-energy determinant is simply

\[
P(y;2,2)=4(Z^2-1).
\]

---

## 4. Balanced quarter-period reduction

For the balanced geometry `N=m=r` and the comparison energy

\[
y_r^*=6+2\cos\frac\pi{2(r+1)},
\]

write

\[
c_r=\cos\frac\pi{2(r+1)}.
\]

Then

\[
x=1+c_r-\frac d2,
\qquad
a=1+c_r+\frac d2,
\qquad x+a=2+2c_r.
\]

Hence all-layer quarter-period optimality for `r>=2` is reduced to proving

\[
\boxed{
\left[
T_r(x)T_r(a)+(ax-3)U_{r-1}(x)U_{r-1}(a)
\right]^2
>
1+(2-d)U_{r-1}(a)^2
}
\tag{4.1}
\]

for every `d in [-2,2]` (with `r=2` handled separately by the exact `k=3` certificate if desired).

No matrix-valued quantity remains in (4.1).
