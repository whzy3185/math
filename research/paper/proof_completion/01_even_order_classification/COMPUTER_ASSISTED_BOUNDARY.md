# Computer-Assisted Boundary

## Formal pattern

Every computational component has the form

    mathematical reduction
      -> explicitly finite exact object
      -> independent verification
      -> mathematical consequence.

No program proves the theorem by plotting spectra or accepting
floating-point eigenvalues.

## Boundary by region

### Even orders 8 through 30

The human argument identifies the switching quotient and proves that an exact
Rayleigh lower certificate or optimiser equality excludes a counterexample.
The machine exhausts the quotient and verifies completion.  At orders 24
through 30 it also replays generator cursors, chunks, represented totals,
digests, and optimiser records.  Floating arithmetic may propose a vector;
only exact integer quadratic forms and algebraic comparisons are accepted.

### Order 32

The checker reconstructs $A$, forms $1561I-200A^2$, and verifies positive
definiteness by Bareiss minors and rational LDL.  It independently checks a
strict rational isolating interval for $\theta_{32}$.

### Orders 34, 36, 38, 42, 44, 46

The written proof establishes local compression and graph completeness.  The
machine checks:

- all $57,344=2^{13}+2^{14}+2^{15}$ local windows;
- exact root isolation for every $\theta_n$;
- exact window classification with no unresolved window;
- every rooted cyclic walk and its dihedral quotient;
- both holonomies for every terminal $Q$-class;
- 64 exact terminal records and zero unresolved records.

The checker does not import the producer and has no floating number on an
accepting path.  Its fail-closed suite contains 23 tamper cases.  The old
number 84 is a documentation sum error; the six counts total 64.

### Order 40

The checker rebuilds the normal-form signing, the integer matrix
$15541I-2000A^2$, and all forty exact rational LDL pivots.  The threshold
comparison is the exact inequality $63/8<\theta_{40}$.

### Even orders 48 through 238

The finite object has 96 rows.  Each records a deterministic gap word,
holonomy, canonical $Q$-code, rational $t_n$, and matrix digest.  The checker
rebuilds each full matrix and repeats exact sparse rational LDL in a different
ordering.  Acceptance requires

$$
t_nI-A_n^2\succ0,\qquad t_n<8-\frac{200}{n^2}.
$$

### Even orders at least 240

The tent summation, patch condition, and monotonicity are analytic.  The finite
machine part consists of exact rational evaluation at
$240,242,244,246$.  Monotonicity, not sampling, gives the infinite tail.

## Independent entry points

    PYTHONPATH=research/scripts python3 research/scripts/verify_target_a_minimality_certificate.py
    PYTHONPATH=research/scripts python3 research/scripts/verify_target_a_n32_certificate.py
    PYTHONPATH=research/scripts python3 research/scripts/verify_target_a_task55_small_order_exact.py
    PYTHONPATH=research/scripts python3 research/scripts/verify_target_a_task55_orders_34_46.py
    PYTHONPATH=research/scripts python3 research/scripts/verify_target_a_task54_threshold.py

Expected markers are TARGET_A_MINIMALITY_CERTIFICATE_PASS,
N32_CERTIFICATE_PASS, TARGET_A_TASK55_SMALL_ORDER_EXACT_VERIFY_PASS,
TARGET_A_TASK55_ORDERS_34_46_VERIFY_PASS, and
TARGET_A_TASK54_THRESHOLD_VERIFY_PASS.

The certificates do not classify minimisers, compute every exact $m_n$, or
prove unrestricted multi-gap or arbitrary-period theorems.
