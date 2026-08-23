# Complete Classification at Every Even Order

Status: `COMPUTER_ASSISTED_PROVED`.

## Theorem

For an even integer `n>=8`, let

```text
m_n=min_sigma rho(A_sigma),
rho_-(n)^2=4+2 cos(2 pi/n)+2 cos(4 pi/n),
```

where `sigma` ranges over all signings of `C_n(1,2)`. Then

```text
m_n < rho_-(n)
```

if and only if

```text
n=32, n=40, or n is even and n>=48.                 (1)
```

Equivalently, the original conjectured lower bound holds exactly at

```text
n in {8,10,...,30,34,36,38,42,44,46},               (2)
```

and fails at every other admissible order.

## Proof

The admissible domain is precisely the set of even integers `n>=8`. Partition
that set into four disjoint parts.

1. For every even `8<=n<=30`, the inherited minimality certificate exhausts
   all switching classes and proves that no counterexample exists. Its exact
   endpoint decisions use rational Rayleigh certificates or optimizer
   equalities, not floating-point spectral comparisons.

2. At `n=32`, the period-eight signing has an exact positive-definiteness
   certificate for `1561 I-200 A^2`, while exact algebraic comparison gives
   `1561/200<rho_-(32)^2`. Thus `n=32` is a counterexample.

3. Task 55 independently classifies the remaining even orders below 48. Its
   exact local-window elimination and parity-lifted de Bruijn closure prove
   that no counterexample exists at

   ```text
   n=34,36,38,42,44,46.
   ```

   The complete terminal set has 84 `(Q,alpha)` records and zero unresolved
   records. At `n=40`, the separate exact rational LDL certificate proves
   `rho(A)^2<15541/2000<63/8`, so a counterexample exists.

4. For every even `48<=n<240`, one of 96 explicit structured signings has an
   exact rational full-matrix LDL certificate. For every even `n>=240`, the
   certified single-G6 edge and exact global tent IMS estimate construct a
   counterexample. Hence every even `n>=48` fails.

These four parts are exhaustive and disjoint, proving (1)--(2).

## Evidence Chain

The small-order inputs are:

- `../TARGET_A_SMALLEST_COUNTEREXAMPLE.md` for `8<=n<=32`;
- `TARGET_A_ORDERS_34_46_EXACT_CLASSIFICATION.md` for the exact `n=40` LDL
  witness and its preserved provenance;
- `TARGET_A_SMALL_ORDER_EXACT_THEOREM.md` and
  `lanes/small_order_exact/VERIFIER_HANDOFF.md` for
  `n=34,36,38,42,44,46`.

The eventual input is the independently checked Task 54 theorem combining
the 96-row finite LDL bridge with the global IMS tail. The Task 55 rank-two
correction does not affect it: the finite bridge controls the entire matrix,
and the IMS proof uses the local bound `sup sigma(H_6)=c6`, not the
multiplicity of `c6`.

The Task 55 small-order certificate is

```text
certificates/small_order_exact_classification.json
sha256 cb12d8502c6fcf31c5e8f1d23f3b9f1bb44b28b05a58f2e02067df08c04132b4
```

and its implementation-independent checker reports

```text
TARGET_A_TASK55_SMALL_ORDER_EXACT_VERIFY_PASS
terminal_unresolved=0.
```

## Scope

This is a complete classification of the truth value of the conjectured
inequality at every admissible order. It is not a classification of all
minimizing signings, all counterexample switching classes, or the exact value
of `m_n` at the failing orders. The number 48 is the beginning of a contiguous
explicit-witness tail, not the first counterexample order; the first failure
is 32, and the interval below 48 contains both true and false orders.
