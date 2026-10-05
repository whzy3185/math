# A synthetic demonstration of the method

This example contains no actual research project, manuscript, author, referee or venue. Its mathematics is an elementary identity with no novelty claim. Its administrative fixture deliberately invents every approval and therefore cannot support a real submission.

## Separate a finite check from a proof

Consider the identity

sum of the first n positive odd integers = n squared, for every integer n ≥ 0.

Run `python3 examples/odd_sum_check.py`. It uses exact integer arithmetic to test n = 0 through 20 inclusive. Its output is finiteVerified and explicitly says that this run does not prove the unbounded claim.

The analytic proof is short. At n = 0, both sides are zero. If the identity holds for n, adding the next odd integer 2n + 1 gives n² + 2n + 1 = (n + 1)². Induction proves the statement for every nonnegative integer n. This argument is analyticProved; the exact finite run provides a separate implementation check.

A claim ledger should therefore have two rows:

- A finite assertion with its exact domain, arithmetic, command and output
- The universal identity with its nonnegative-integer hypothesis, induction proof, base case and induction step

No negative literature search is needed to advertise this as novel; it is being used only as an elementary illustration. If a formalization is added, record the exact Lean statement, toolchain, declaration and actual axiom/build results. This package does not claim that the example was formalized.

## Apply the stage contracts

1. Define the question and domain before writing an abstract
2. Separate the finite assertion from the universal claim in the ledger
3. Record the induction base and step as distinct proof obligations
4. Check the zero case and exact finite arithmetic
5. Write a short explanation of why the induction step matches the next odd term
6. Have an independent reader check the quantifier and base case before seeing an author's defense
7. Use a different editor to repair any issue and preserve the assessed version
8. Re-review exact changes and retire a reviewer context after two rounds
9. Record any formalization as performed or not performed, rather than assuming it
10. For a genuine manuscript, compile/inspect the final PDF and verify the exact release package
11. Obtain real author, policy and submission decisions only from authentic sources

The full S00–S15 workflow supplies the detailed input/output and stopping rules for these steps.

## Exercise the administrative records

Generate a complete synthetic fixture:

```sh
python3 scripts/make_synthetic_example.py /tmp/generic_math_example
python3 scripts/workflow_check.py readiness /tmp/generic_math_example/record.json
```

The positive fixture can satisfy the administrative consistency checks because its invented records agree with one another. That result authenticates none of the fictional statements. Its minimal PDF is only a byte-identity fixture and is not a rendered mathematical paper.

The unit tests also demonstrate failure conditions: altered evidence bytes, missing obligations, deleted issues, mismatched source fingerprints, reused retired contexts, contradictory latest receipts, incomplete typed consent, and exposed review contexts. A disclosed continuation may close issues while the pristine-initial-review gate remains blocked.

For your own work, replace every synthetic field with genuine evidence in a separate local directory. Never publish a private record, manuscript identifier, source path or hash merely because it can be represented by a schema. The generic toolkit does not grant permission to share the inputs used with it.
