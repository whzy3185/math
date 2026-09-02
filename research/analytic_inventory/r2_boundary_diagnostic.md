# Residue-two boundary diagnostic (not a proof)

## Purpose

This numerical experiment guides the analytic boundary programme.  It is not
evidence for a theorem and must not be cited in a manuscript.

Using the exact local block-Schur recurrence and only converting the final
eight by eight rational Schur core to floating point for orientation gives:

| n | smallest eigenvalue of final core | largest eigenvalue |
|---:|---:|---:|
| 50 | 0.467683643468 | 155.558796314810 |
| 58 | 0.460626417615 | 155.544805594716 |
| 66 | 0.458314267246 | 155.540235330254 |
| 74 | 0.457557815748 | 155.538741526004 |
| 90 | 0.457229617139 | 155.538093627073 |
| 130 | 0.457190500066 | 155.538016414026 |
| 410 | 0.457190353588 | 155.538016124895 |

The data are consistent with a positive period-two limiting boundary core,
and with an error contraction close to the pre-existing bulk scale \(1/3\).
They do not prove either fact.

## Concrete analytic target

The useful target is stronger and simpler than merely \(S_k\succ0\):

\[
S_k\succeq \frac25I_8\qquad(k\ge6).
\]

The observed limiting margin is about \(0.45719\), leaving a margin of about
\(0.057\) above \(2/5\).  A proof can therefore be organised as follows.

1. Construct a rational period-two limit response \(S_\infty^{(i)}\).
2. Prove \(S_\infty^{(i)}-2I_8/5\succ0\) by an exact LDL certificate.
3. Prove an explicit induced-norm bound
   \(\|S_k-S_\infty^{(k\bmod2)}\|<1/20\) beyond a stated finite index.
4. Check the finite initial interval by exact rational LDL only.

This would leave a short, understandable finite base and replace the
unbounded residue-two LDL list by a uniform theorem.

## Required caution

The apparent convergence ratio is not a proof of response contraction.
The stable transfer multiplier estimate and the Riccati-box invariance must
be connected to the actual response coordinates by a separate norm or
Loewner argument.
