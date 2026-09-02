# Residue-two finite boundary base

For every residue-two order

\[
50\le n<410,
\qquad n\equiv2\pmod8,
\]

the exact six-by-six cyclic response core is positive definite.  There are
45 such orders.  The verifier does not repeat an \(n\)-dimensional spectral
calculation: it uses the exact block-Schur recurrence, whose open bulk
positivity has a separate analytic proof, then applies Fraction-LDL to the
fixed boundary core.

This finite base is acceptable in an analytic-first proof only because:

1. the domain is explicitly stated and finite;
2. the block reduction proves why the six-by-six core is equivalent to the
   original positivity question once bulk pivots are known positive;
3. every terminal test uses exact rational arithmetic.

It is not a substitute for the still-open tail lemma at orders \(n\ge410\).

Run:

```text
python research/scripts/verify_target_a_r2_finite_base.py
```
