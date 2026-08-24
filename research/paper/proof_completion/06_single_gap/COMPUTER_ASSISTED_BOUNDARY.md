# Computer-Assisted Boundary

## Analytic part

The strict separation theorem is a finite-support variational proof. Every
vector, image, norm, quotient, and rational margin is printed in
`FULL_PROOF.md`. A referee can check it with integer arithmetic alone.

The passage from a witness quotient to the spectral lower bound is the
standard variational principle. The coverage of all `g>=9` is mathematical:
finite propagation shows that the local coefficient word has only the three
cases printed in equation (5).

## Inherited computer-assisted input

The equality `sup sigma(H_6)=c6` and the certified upper endpoint for `c6`
come from the global G6 proof package. That is the only logically essential
computer-assisted upstream theorem.

## Exact verification of the corollary

The certificate

```text
research/proofs/task57/certificates/uniform_single_gap_separation.json
```

stores the exact threshold, all seven quotient comparisons, and the minimum
row. The independent checker

```text
research/scripts/verify_target_a_task57_uniform_single_gap.py
```

reconstructs the comparisons using rational arithmetic. Its focused test
suite

```text
research/scripts/test_target_a_task57_uniform_single_gap.py
```

contains 12 passing tests, including tamper rejection. The strict comparison
symbol is part of the accepted contract.

## Mathematical consequence

The checker does not infer a spectral theorem from samples. It verifies the
finite arithmetic after finite propagation has reduced infinitely many gaps
to six small cases and three tail coefficient patterns. That reduction plus
the variational principle is what proves the all-`g` statement.

## Nonclaims

- No multi-gap or arbitrary finite-core minimization is asserted.
- No simplicity theorem is asserted for the strict competitors.
- The bound `1/250` is convenient and certified, not claimed optimal.
