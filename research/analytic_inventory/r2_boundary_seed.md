# Residue-two boundary seed

The exact fixed-width Schur reduction at \(n=250\) gives an eight-by-eight
rational final core \(S_{250}\).  Fraction-LDL elimination verifies

\[
S_{250}-\frac25I_8\succ0.
\]

This is a finite exact seed, not an all-length proof.  Its role is to provide
a fixed positive margin for the final step of the analytic boundary argument.

The remaining theorem is:

\[
\|S_{8k+2}-S_{250}\|<\frac1{50}
\qquad(k\ge31),
\]

or any stronger rational tail bound.  The local response-transfer contraction
from `r2_response_transfer.md` is intended to supply this estimate after the
fixed wrap-around couplings are inserted into the response recurrence.

Once that tail inequality is proved, the displayed seed margin implies
\(S_{8k+2}\succ0\) for every later residue-two order, leaving only the
finite interval below \(250\) for exact verification.

Verify the seed with:

```text
python research/scripts/verify_target_a_r2_boundary_seed.py
```
