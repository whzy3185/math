# Hamilton-gauge realization on \(C_n(1,2)\)

This elementary lemma supplies the finite-graph entry point for the
period-eight Floquet argument.  It is stated independently of the repository
enumeration and is sufficient both to construct the counterexample family and
to identify its two holonomy sectors.

## Lemma

Let \(n\ge8\).  Give \(C_n(1,2)\) a signing, and write \(a_i\) for the sign
on \(\{i,i+1\}\) and \(b_i\) for that on \(\{i,i+2\}\), with indices modulo
\(n\).  Define

\[
\alpha=\prod_{i=0}^{n-1}a_i,\qquad
\tau_i=a_i a_{i+1}b_i.
\tag{1}
\]

After switching, its signed adjacency operator is unitarily equivalent to
the operator on sequences satisfying \(x_{i+n}=\alpha x_i\),

\[
(A_\tau x)_i=x_{i-1}+x_{i+1}
  +\tau_{i-2}x_{i-2}+\tau_i x_{i+2}.
\tag{2}
\]

Conversely, every pair \((\tau,\alpha)\in\{\pm1\}^n\times\{\pm1\}\)
defines a signing through (2).  In particular, a periodic word \(\tau\) of
period dividing \(n\), together with either choice of \(\alpha\), gives a
valid finite signing of \(C_n(1,2)\).

## Proof

Set \(d_0=1\) and, for \(0\le i\le n-2\), define

\[
d_{i+1}=d_i a_i.
\]

Switching by \(D=\operatorname{diag}(d_0,\ldots,d_{n-1})\) makes the first
\(n-1\) step-one signs equal to \(+1\).  The remaining step-one sign is

\[
d_{n-1}a_{n-1}d_0=\prod_{i=0}^{n-1}a_i=\alpha.
\]

Triangle signs are switching invariant.  Therefore, away from the seam, the
new step-two sign at \(\{i,i+2\}\) is exactly \(\tau_i\).  Unroll the cycle
at the seam and impose \(x_{i+n}=\alpha x_i\).  The step-one edge crossing
the seam then has coefficient \(+1\) in the lifted formula and contributes
the finite coefficient \(\alpha\).  Likewise, a step-two edge crossing the
seam obtains precisely the same factor from the boundary condition; this is
the factor required by (1), because the corresponding triangle contains the
seam step-one edge.  This gives (2) on every row of the finite matrix.

Conversely, reduce (2) modulo \(n\).  Its step-one edges have signs \(+1\)
except for the seam, whose sign is \(\alpha\); the step-two coefficients,
including the boundary factors just described, are signs in \(\{\pm1\}\).
Thus it is a signing of \(C_n(1,2)\).  The two constructions reverse one
another up to switching. \(\square\)

## Scope

The lemma is a coordinate statement only.  It neither minimizes spectral
radius nor asserts that the local triangle word records every finite-cycle
invariant.  The condition \(n\ge8\) avoids the edge coincidences outside the
problem's stated domain.
