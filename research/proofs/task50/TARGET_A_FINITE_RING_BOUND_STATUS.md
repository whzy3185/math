# Target A Finite-Ring Bound Status

## Exact Closure

In the tree gauge, the finite ring has the twisted boundary condition

\[
X_{i+n}=\alpha X_i,qquad \alpha\in\{-1,+1\}.
\]

If `M_n(lambda)` is the ordered product of the one-step transfer matrices,
the exact finite-ring eigenvalue equation is

\[
\det(M_n(\lambda)-\alpha I_4)=0.
\]

For G6 write `n=8k+2`; for G10 write `n=8k+6`.  In both cases `k` is the
number of intact period-eight bulk cells between the defect support and the
closure in the convention used by Task 49.  The legal cyclic gap words are

\[
[6,4^{,2k-1}],\qquad [10,4^{,2k-1}],
\]

respectively.  Both contain `2k` quadrilateral defects and hence satisfy the
exact legality condition.

## Exterior-Power Recurrence

Let `f_k(y,alpha)` denote the closure determinant after replacing
`lambda^2` by `y`.  The determinant expansion into exterior powers shows that
`f_k` is a linear combination of powers of:

- the four eigenvalues of the bulk monodromy;
- the four nontrivial pair products;
- the constant product one.

Consequently `f_k` satisfies a universal order-nine recurrence.  Its exact
characteristic polynomial is stored in
`certificates/finite_ring_recurrence.json`.  It is obtained as

\[
\frac{\chi_{M_8}(t)\chi_{\Lambda^2M_8}(t)}{t-1}.
\]

The derivation is exact and covers both holonomies.  Direct symbolic initial
data for G6 and G10 verify the recurrence in both cases.

## What Is Still Missing

After the shift `y=8+u`, the nine recurrence coefficients have strict
alternating signs.  The first nine closure polynomials have one strict
coefficient sign for both families and both holonomies.  However, the
alternating recurrence does not preserve the naive coefficientwise positive
cone.  No replacement invariant cone, total-positivity representation, or
uniform resolvent estimate has yet been proved.

This matters because the infinite localized state only produces a nearby
finite eigenvalue.  It does not exclude another finite eigenvalue of larger
modulus.  Therefore the Task 49 empirical estimates

\[
|R_n-c_6|\le C_6q_6^k,
\qquad
|R_n-c_{10}|\le C_{10}q_{10}^k
\]

cannot be upgraded from the present argument.

## Gate Decision

`SINGLE_INTERFACE_BOUND_INCOMPLETE`

The exact recurrence is a proof reduction, not a numerical extrapolation.
The next proof should construct an invariant cone for the nine-dimensional
closure recurrence or an equivalent block-Riccati/Schur-complement bound.
