# Appendix C. Computational Protocol

## C.1 Reference environment

The reference interpreter and packages are:

```text
Python 3.12.13
NumPy 2.3.5
SymPy 1.14.0
pytest 9.1.1
```

From a clean checkout with Python 3.12 available, a portable environment is
created by

```bash
python3.12 -m venv .venv-target-a
.venv-target-a/bin/python -m pip install --upgrade pip
.venv-target-a/bin/python -m pip install \
  -r research/reproducibility/requirements-target-a.txt
```

All commands below are repository-relative.

## C.2 Fast verification

The complete default regression suite is run by

```bash
.venv-target-a/bin/python -m pytest -q research/scripts
```

The principal theorem checkers may also be run separately:

```bash
.venv-target-a/bin/python research/scripts/verify_target_a_minimality_certificate.py
.venv-target-a/bin/python research/scripts/verify_target_a_period8_infinite_family.py
.venv-target-a/bin/python research/scripts/verify_target_a_period8_sharp_constant.py
.venv-target-a/bin/python research/scripts/verify_target_a_period8_structural_mechanism.py
.venv-target-a/bin/python research/scripts/verify_target_a_general_period_moments.py
.venv-target-a/bin/python research/scripts/verify_target_a_low_period_spectral_frontier.py
.venv-target-a/bin/python research/scripts/verify_target_a_low_period_structural_frontier.py
.venv-target-a/bin/python research/scripts/verify_target_a_periodic_operator_equivalences.py
```

Each command fails closed on a mismatched dependency, count, exact
certificate, scope flag, or source digest.

## C.3 Slow generator audits

The three generator audits skipped by the default suite are enabled explicitly:

```bash
TARGET_A_RUN_SLOW_GENERATOR_TESTS=1 \
.venv-target-a/bin/python -m pytest -q \
  research/scripts/test_target_a_direct_bracelets.py::DirectBraceletTests::test_direct_generator_burnside_n26 \
  research/scripts/test_target_a_direct_bracelets.py::DirectBraceletTests::test_direct_generator_burnside_n28 \
  research/scripts/test_target_a_direct_bracelets.py::DirectBraceletTests::test_direct_generator_burnside_n30
```

These tests independently check shell totals, Burnside counts, represented
class totals, ordering, and parity. They are audits, not fresh spectral
regeneration.

## C.4 Regeneration versus integrity replay

Fresh regeneration starts from the canonical generator, reconstructs every
spectral state, recomputes its exact decision, and writes a new checkpoint
chain. Integrity replay reads an existing chain and verifies its hashes,
counts, cursor, and aggregate records. Both are useful, but only the former
re-executes the mathematical decision for every state.

The production checkpoints are committed. The fresh regeneration chunks and
full runtime logs are retained outside the repository; their compact manifest
records state counts, chunk counts, ordered input and certificate digests, and
terminal chain digests. Agreement of these logical fingerprints, rather than
byte equality of timing metadata, defines mismatch zero.

## C.5 Negative tests

Regression tests alter one logical field at a time and require rejection.
They cover, among other faults, missing orbit representatives, duplicated
canonical words, nondeterministic orbit identifiers, dependency digest drift,
false primitive periods, altered Rayleigh numerators, the lower radical branch,
incorrect moment direction, numeric previews promoted to proof, and forbidden
all-period scope. This adversarial layer is important because many positive
checks share the same exact arithmetic primitives.
