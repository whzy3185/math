# Finite Structured Counterexample Tail

For every even `48<=n<240`, choose one deterministic structured signing:

```text
n=0 mod8: period-eight repetition,
n=2 mod8: one G6,
n=4 mod8: two balanced G6 interfaces,
n=6 mod8: three balanced G6 interfaces.
```

The holonomy is `-1` for `n=0 mod4` and `+1` for `n=2 mod4`. For every one
of the 96 orders, the producer chooses a rational `t_n` and reconstructs the
full signed adjacency. Exact positive definiteness of

```text
t_n I-A^2
```

proves the full spectral-top upper bound `rho(A)^2<t_n`. This is not a
Rayleigh certificate. The other half of the exact sandwich is

```text
t_n < 8-200/n^2 < rho_-(n)^2.
```

The compressed artifact is a deterministic recomputation package rather
than a self-contained list of all rational pivots. It stores the gap word,
holonomy, canonical Q code, rational bound, portable matrix hash, and
producer-pivot hash. Its independent checker reconstructs all 96 matrices
directly from the canonical Q bits, repeats exact rational LDL in a different
elimination order, and reproduces the producer-order pivot digest.

Combining these finite rows with the independent analytic tail proves that
every even `n>=48` has an explicit certified counterexample. The number 48
is a contiguous explicit-witness threshold, not a claim that no smaller
eventual threshold or counterexample exists.

Status: COMPUTER_ASSISTED_PROVED.
