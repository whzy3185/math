# Line audit: general periodic defect obstruction

## Verdict

The theorem in general_period_defect_obstruction.md is valid as a mixed
analytic/finite-combinatorial result.  Its algebraic implications are
analytic; the 430 closed-word collection is an explicitly displayed finite
integer catalogue, not a numerical calculation.

## Checks

| Link | Verdict | Reason |
|---|---|---|
| \(Q_i=\tau_i\tau_{i+1}\) is legal | PASS | Its cyclic product is automatically one for every periodic \(\tau\). |
| Floquet moment interpretation | PASS | Fiber phases record net cell displacement; the circle average keeps exactly zero-displacement closed walks. |
| Local square formula | PASS | Direct multiplication of the four local transitions yields the nine displayed coefficients. |
| Fourth moment | PASS | Summing squares of the local-square row gives the displayed \(M_2\). |
| Sixth moment | PASS, finite | The complete 20-row integer monomial table sums to 430 and groups to (4). |
| Conversion to \(d,a,b\) | PASS | Substitute \(Q_i=2I_i-1\) in the three translation sums. |
| Spectral implication | PASS | If \(R_p(\tau)\le8\), each nonnegative squared fiber eigenvalue satisfies \(y^{k+1}\le8y^k\); integrate its trace. |

## Article classification

The theorem may appear in the main text as a general structural consequence,
provided it is called an exact closed-walk calculation.  It must not be
described as a numerical experiment, a signing enumeration, or an
all-period optimizer classification.
