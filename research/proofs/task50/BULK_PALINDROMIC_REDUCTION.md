# Bulk Palindromic Reduction

Put `y=lambda^2` and write the exact period-eight monodromy as

\[
M_8(\lambda)=T_7(\lambda)\cdots T_0(\lambda)
\]

for the triangle-flux cell `(1,1,-1,1,-1,-1,1,-1)`.  Direct multiplication
over `Z[lambda]` gives

\[
\chi(z;y)=z^4+a(y)z^3+b(y)z^2+a(y)z+1,
\]

where

\[
a(y)=-2y^2+16y-13,
\quad
b(y)=y^4-16y^3+80y^2-128y+40.
\]

Since the constant coefficient is one, `z=0` is not a root.  Dividing by
`z^2` and setting `w=z+z^{-1}` gives

\[
\frac{\chi(z;y)}{z^2}
=w^2+a(y)w+b(y)-2.
\]

The discriminant of this quadratic is

\[
\Delta(y)=a(y)^2-4(b(y)-2)=-12y^2+96y+17.
\]

Thus the two exact `w` branches are

\[
w_\mp(y)=\frac{2y^2-16y+13\mp\sqrt{-12y^2+96y+17}}2.
\]

For either branch, the corresponding reciprocal multiplier pair is

\[
z_s(w)=\frac{w-\sqrt{w^2-4}}2,
\qquad
z_u(w)=\frac{w+\sqrt{w^2-4}}2=z_s(w)^{-1}.
\]

All displayed identities are checked by exact symbolic expansion in
`research/scripts/target_a_task50_bulk.py`; the full monodromy entries are in
`certificates/bulk_symbolic.json`.
