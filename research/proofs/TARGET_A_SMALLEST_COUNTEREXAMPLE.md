# Target A: Smallest Counterexample

Date: 2026-08-15

Status: **SMALLEST_COUNTEREXAMPLE_VERIFIED**

## Theorem

Conjecture 3 first fails at `n=32`.

The proof has two computationally checkable parts: exhaustive exact finite
verification at every smaller admissible order, and an explicit exact
counterexample certificate at order 32.

## Domain

The conjecture applies exactly when `n` is even and `n>=8`. Therefore the
admissible orders below 32, generated from this rule rather than assumed as a
list, are

```text
8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30.
```

Odd orders and orders below 8 are outside the conjecture's domain.

## No smaller counterexample

The checker reads each machine-readable source directly and verifies its
completion and exact-decision fields. Floating eigenvalues were used only to
propose rational Rayleigh vectors, never for the final decision.

| n | verification method | switching classes represented | counterexamples | exact certificate |
|---:|:---|---:|---:|:---|
| 8 | raw switching-class exhaustion | 512 | 0 | 510 Rayleigh + 2 optimizer equalities |
| 10 | raw switching-class exhaustion | 2,048 | 0 | 2,046 Rayleigh + 2 optimizer equalities |
| 12 | raw switching-class exhaustion | 8,192 | 0 | 8,190 Rayleigh + 2 optimizer equalities |
| 14 | raw switching-class exhaustion | 32,768 | 0 | 32,766 Rayleigh + 2 optimizer equalities |
| 16 | raw switching-class exhaustion | 131,072 | 0 | 131,070 Rayleigh + 2 optimizer equalities |
| 18 | raw switching-class exhaustion | 524,288 | 0 | 524,286 Rayleigh + 2 optimizer equalities |
| 20 | raw switching-class exhaustion | 2,097,152 | 0 | 2,097,150 Rayleigh + 2 optimizer equalities |
| 22 | full `(Q,alpha)/D_22` quotient | 8,388,608 | 0 | 97,467 Rayleigh + distinguished threshold equality |
| 24 | direct-bracelet production quotient | 33,554,432 | 0 | 353,811 Rayleigh + exact optimizer check |
| 26 | direct-bracelet production quotient | 134,217,728 | 0 | 1,299,063 Rayleigh + exact optimizer check |
| 28 | direct-bracelet production quotient | 536,870,912 | 0 | 4,810,471 Rayleigh + exact optimizer check |
| 30 | direct-bracelet production quotient | 2,147,483,648 | 0 | 17,929,599 Rayleigh + exact optimizer check |

For `n=24,26,28,30`, read-only replay independently reproduces chunk
completeness, defect-shell counts, the terminal generator cursor, represented
space totals, input and certificate digests, the optimizer record, zero
fallbacks, zero counterexamples, and the final checkpoint hash chain.

## Explicit n=32 counterexample

The frozen signing has all step-1 edge signs positive and step-2 signs equal
to the following triangle-flux pattern:

```text
tau   = (+,+,-,+,-,-,+,-)^4
Q     = (+,-,-,-)^8
alpha = +1.
```

The independent checker reconstructs the signed adjacency matrix directly
from the two edge-sign lists. It verifies dimension 32, symmetry, zero
diagonal, support exactly `C_32(1,2)`, all edge signs in `{+1,-1}`, and the
displayed flux and holonomy.

For this matrix, independent fraction-free Bareiss elimination and rational
`LDL^T` decomposition both certify that all 32 pivots of

```text
1561 I - 200 A^2
```

are positive. Hence

```text
rho(A)^2 < 1561/200.
```

An exact real-algebraic comparison, also checked against the saved certified
rational interval, gives

```text
1561/200 < rho_-(32)^2.
```

Therefore `rho(A)<rho_-(32)`, so the signing is a strict counterexample.

## Minimality conclusion

Every admissible order below 32 has been exhaustively excluded, and 32 has an
explicit exact counterexample. Since 32 is the next even integer after 30,
it is the smallest admissible counterexample order.

This is an exhaustive-computation theorem with an exact witness, not a
computation-free proof. It makes no claim that the order-32 counterexample is
unique, that its switching class is unique, or that every even order above 32
fails.

## Reproducibility

Run the independent witness checker:

```text
PYTHONPATH=<sympy-path> .venv/bin/python \
  research/scripts/verify_target_a_n32_certificate.py
```

Run the total certificate checker:

```text
PYTHONPATH=<sympy-path> .venv/bin/python \
  research/scripts/verify_target_a_minimality_certificate.py
```

Success outputs are respectively `N32_CERTIFICATE_PASS` and
`TARGET_A_MINIMALITY_CERTIFICATE_PASS`.

## Evidence hashes

```text
1f20469033876569292de247344ba88eb0831c163e01c1441f1b75aa8bca95c7  research/counterexamples/target_a_minimality_certificate.json
5bb4a6c39039bb76e41945c0c1f0dffd545b778c0230ce85d3f905bc197b284f  research/audit/TARGET_A_MINIMALITY_DEPENDENCIES.json
bcfcb67f6b1e67f7d7ec36552c99aeebfcd8811a46ef697de7314b4ad2311d57  research/audit/target_a_minimality_checkpoint_replay.json
c5ecd532da469092ef98fe2385dfb69b8da542595f942cd88b881d985b72bc10  research/counterexamples/target_a_n32_period8.json
db1378c6a7e5ab8526890be41c929a60ee17675d920a5ca0c501f49d888e46b4  research/counterexamples/target_a_n32_period8_certificate.json
48997c791be70f7f2cb5287981dea361494a589034b6e72f78dbcfddf102dbb1  research/scripts/verify_target_a_minimality_certificate.py
cc61bdb44c29c5b415b155f4d8da0f25cb729b628a1dba79d86353b374b27de2  research/scripts/verify_target_a_n32_certificate.py
```

The dependency manifest records the SHA-256 of every finite result JSON,
production checkpoint manifest, domain specification, checker, and exact
order-32 input used by this theorem.
