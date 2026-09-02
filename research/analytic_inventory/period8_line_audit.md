# Line audit of the period-eight main theorem

This is a proof audit, not a replacement for the proof.  It records the
logical bridges that a referee is most likely to test in the analytic
counterexample theorem.

| Link | Check | Result |
|---|---|---|
| finite graph to periodic operator | Switching removes the first \(n-1\) step-one signs; quasi-periodicity supplies exactly the two seam factors | PASS |
| finite ring to Floquet fibers | Translation by eight is diagonalizable under \(x_{i+n}=\alpha x_i\); its eigenvalues satisfy \(z^L=\alpha\) | PASS |
| chiral symmetry | Direct eigenspace basis yields zero diagonal blocks and the stated \(BC\) matrix | PASS |
| determinant | The two-by-two block determinant expands to \(P(y,z+z^{-1})\) | PASS |
| uniform spectral bound | \(P_c<0\) for \(y\ge1561/200\), \(c\in[-2,2]\), and the explicit expansion of \(P(B_0+u,2)\) is positive | PASS |
| strictness | A squared eigenvalue is a root of \(P\); positivity on \(y\ge B_0\) excludes equality as well as excess | PASS |
| comparison threshold | The alternating Taylor lower bound is valid for both angles; the signs of the \(\pi^2,\pi^4,\pi^6\) terms justify the \(9<\pi^2<10\) substitutions | PASS |
| propagation in \(n\) | Both angles \(2\pi/n\) and \(4\pi/n\) lie in \((0,\pi/2]\) for \(n\ge8\), and decrease strictly with \(n\); cosine is strictly decreasing in its argument there | PASS |

## Expanded checks

### The polynomial comparison

For \(y\ge B_0=1561/200\),

\[
\partial_cP(y,c)
=2\!\left(c-y^2+8y-\frac{13}{2}\right).
\]

The function \(y^2-8y+13/2\) is increasing for \(y>4\), and at \(B_0\)
it equals \(199121/40000>2\).  Hence \(c\le2\) makes
\(\partial_cP(y,c)<0\).  Thus \(P(y,c)\ge P(y,2)\), and the displayed
positive-coefficient expansion in \(u=y-B_0\) proves \(P(y,c)>0\).
No reality-root ordering or numerical approximation is being used here.

### The Taylor comparison

For \(0<t<1\), the magnitudes \(t^{2k}/(2k)!\) decrease.  The alternating
series remainder after the negative sixth-degree term is therefore positive:

\[
\cos t>1-\frac{t^2}{2}+\frac{t^4}{24}-\frac{t^6}{720}.
\]

At \(t=\pi/16\) and \(t=\pi/8\), replace the negative \(\pi^2\) and
\(\pi^6\) contributions by their bounds using \(\pi^2<10\), and the
positive \(\pi^4\) contribution by \(\pi^4>81\).  The resulting rational
quantity is \(1178731111/150994944\), which exceeds \(1561/200\).

## Remaining human reading task

The audit finds no unresolved logical bridge in the main theorem.  A final
coauthor-level reading should nevertheless independently reproduce the
displayed eight-by-eight fiber from the operator convention, rather than
only read the symbolic audit output.  This is a review-quality safeguard,
not an identified defect.
