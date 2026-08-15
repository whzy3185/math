# N32 Witness Reconstruction Audit

Date: 2026-08-15

Status: **N32_WITNESS_INDEPENDENTLY_RECONSTRUCTED**

## Purpose

This audit reconstructs the Target A order-32 counterexample with a second
implementation. The construction begins only with the mathematical flux data
and deliberately uses a nontrivial gauge. Its result is frozen before the
previous witness is opened for comparison.

## Mathematical input

```text
n = 32
tau = (+,+,-,+,-,-,+,-)^4
alpha = +1
```

No edge-sign vector from the frozen witness is an input to the construction.

## Independent gauge

The deterministic step-1 gauge is

```text
a = (+,-,+,-,-,+,-,+)^4.
```

It contains 16 negative signs and has product `+1`. It is therefore visibly
different from the frozen all-positive step-1 gauge.

## Derived step2

The script solves the triangle-flux definition directly:

```text
tau_i = a_i a_(i+1) b_i,
b_i   = tau_i a_i a_(i+1).
```

This gives

```text
b = (-,-,+,+,+,+,-,-)^4.
```

The 32 by 32 integer adjacency matrix is then built directly from the
step-1 and step-2 edge definitions. It is symmetric, has zero diagonal,
has exactly four nonzero signs in every row, and has support exactly
`C_32(1,2)`.

## Flux checks

Recomputing all invariants from the new edge signs gives

```text
tau   = (+,+,-,+,-,-,+,-)^4
Q     = (+,-,-,-)^8
alpha = +1.
```

Thus the construction reproduces the specified mathematical data exactly.

## Frozen witness comparison

Only after the independent construction JSON was atomically written did the
script open `research/counterexamples/target_a_n32_period8.json`. Starting
with `d_0=+1`, the step-1 switching equations uniquely give

```text
d = (+,+,-,-,+,-,-,+)^4.
```

The vector closes after 32 edges. All 32 step-1 equations and all 32 step-2
equations hold exactly.

## Exact matrix relation

For `D=diag(d_0,...,d_31)`, direct integer matrix comparison proves

```text
A_independent = D A_frozen D.
```

No switching-equivalence helper from the existing Target A implementation is
called.

## Spectral consistency

SymPy exact integer characteristic polynomials independently satisfy

```text
charpoly(A_independent)   = charpoly(A_frozen),
charpoly(A_independent^2) = charpoly(A_frozen^2).
```

Their coefficient-sequence SHA-256 values are respectively
`cf05f3a37bcac92076176f8e3339acf2530f8c133902eb8f6109caa20af2ba0a`
and `04724c8677decd9bc79d0ac87ac4142d4344f0f1476717c9b52895a544de555c`.

## Counterexample check

The new implementation constructs

```text
M = 1561 I - 200 A_independent^2
```

and recomputes both fraction-free Bareiss leading principal minors and a
rational `LDL^T` decomposition. All 32 minors and all 32 pivots are positive,
and the cumulative LDL products equal the Bareiss minors. Hence

```text
rho(A_independent)^2 < 1561/200.
```

A fresh exact real-algebraic sign comparison proves

```text
1561/200 < rho_-(32)^2.
```

Therefore

```text
rho(A_independent)^2 < 1561/200 < rho_-(32)^2.
```

## Independence statement

The reconstruction script imports only the Python standard library and
SymPy. It does not import or call `target_a_period8_family`,
`target_a_flux_search`, `target_a_minimality_search`, `target_a_reproduce`,
`verify_target_a_n32_certificate`, any existing witness constructor, or any
Q/triangle-flux reconstruction helper. It uses no floating eigenvalues.

This audit establishes the concrete witness independently. It does not audit
the period-8 Floquet determinant or infinite-family proof; that remains Task
38.

## Evidence

```text
a1bbf6fb2e344a67b0fa910f94bd6da01c7672e66276c1076a874165cee0b92d  research/scripts/target_a_n32_independent_reconstruction.py
53b9b117b074427134e7e8f71838d5b2af85930492e988a8c1d17d9542fd7b7a  research/audit/target_a_n32_independent_reconstruction.json
35a28ffb95cb1ab1e15838997b7fc9a696d7f69caa70a4aeafd50f653bc5c543  research/audit/n32_witness_reconstruction_audit.json
c5ecd532da469092ef98fe2385dfb69b8da542595f942cd88b881d985b72bc10  research/counterexamples/target_a_n32_period8.json
```

## Conclusion

`INDEPENDENT_N32_RECONSTRUCTION_PASS`
