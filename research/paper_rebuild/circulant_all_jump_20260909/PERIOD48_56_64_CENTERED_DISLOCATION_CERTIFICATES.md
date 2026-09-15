# Exact centered-dislocation certificates at periods 48, 56, and 64

Date: 2026-09-15

Status: **Proved by exact finite certificates**.

This note closes the next three finite layers of the centered `p=8r` double-dislocation family from `CENTERED_DOUBLE_DISLOCATION_P8R_LIMIT.md`.

---

## 1. Family

For `r=6,7,8`, take the period `p=8r` flux word

\[
Q_j=+1
\iff
j\in\{0,2,\ldots,4r-4\}\setminus\{2\ell_r\},
\]

where `ell_r` is the largest odd integer not exceeding `r`.

The folded words are

\[
\begin{aligned}
r=6:&\quad G(DDGG)^2DDDDGG(DDGG)^2G,\\
r=7:&\quad G(DDGG)^3DDDDGG(DDGG)^2G,\\
r=8:&\quad G(DDGG)^3DDDDGG(DDGG)^3G.
\end{aligned}
\]

Let `R_r` denote the continuous squared Bloch edge.

## Theorem

For each

\[
r\in\{6,7,8\},
\]

one has

\[
\boxed{R_r<31/4.}
\tag{1.1}
\]

Consequently these period-48, 56, and 64 phases also strictly beat the complete two-defect family, whose optimal edge is already above `31/4` at these periods.

---

## 2. Exact no-crossing certificates

At the squared test energy

\[
y_0=31/4,
\]

use the exact folded `4 x 4` transfer recurrence in the quadratic algebra `lambda^2=31/4`.  After eliminating `lambda` and writing

\[
c=z+z^{-1},
\]

the chiral characteristic determinant becomes a polynomial `f_r(c)` of degree equal to the folded length `4r`.

Exact Sturm root counts give

\[
\boxed{
\#\{c\in[-2,2]:f_r(c)=0\}=0
}
\tag{2.1}
\]

for all three layers, with degrees

\[
\boxed{24,\ 28,\ 32}
\]

for `r=6,7,8`, respectively.

Thus no Bloch fiber crosses the energy `31/4`.

---

## 3. Exact reference-fiber inertia

At the reference phase `z=1`, the folded matrices have integer entries.  Form

\[
M_r=31I-4H_r(1)^2.
\]

An exact fraction-free `LDL^T` decomposition gives strictly positive diagonal pivots in every layer.  In particular the smallest pivots are

\[
\begin{array}{c|c|c}
r&p&\min D_i\\ \hline
6&48&>0.7501\\
7&56&>0.7495\\
8&64&>0.7491.
\end{array}
\]

The decimal numbers only summarize exact positive rational pivots; positivity itself is checked with exact rational arithmetic.

Hence

\[
31I-4H_r(1)^2>0
\]

for all three reference fibers.  Combined with the no-crossing statement (2.1) and connectedness of the Bloch circle, this gives (1.1).

---

## 4. Place in the staircase

The analytically/exactly proved `p=8r` layers now include

\[
\boxed{r=3,4,5,6,7,8}
\]

or

\[
\boxed{p=24,32,40,48,56,64.}
\]

All use the same centered `GGGG/DDDD` double-dislocation mechanism.  Together with `CENTERED_DOUBLE_DISLOCATION_P8R_LIMIT.md`, this leaves only the task of making the hyperbolic tail threshold effective in order to obtain the statement for every `r>=3` in one theorem.