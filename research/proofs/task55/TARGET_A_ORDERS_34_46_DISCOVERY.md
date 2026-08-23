# Target A orders 34--46: discovery record

> **Supersession notice.**  This document preserves the bounded-search
> provenance and the discovery route to the exact order-40 certificate.  Its
> six `OPEN_BOUNDED_SEARCH_ONLY` labels describe what this search lane proved,
> not the current project classification.  The later exact local-interlacing
> classifier in `TARGET_A_SMALL_ORDER_EXACT_THEOREM.md`, independently checked
> with final status `COMPUTER_ASSISTED_PROVED`, proves that no counterexample
> exists at \(n=34,36,38,42,44,46\).  The order-40 exact rational LDL
> certificate below remains valid and is not superseded.

## 1. Question and logical boundary

This lane studies the seven unresolved or diagnostic even orders

\[
 n\in\{34,36,38,40,42,44,46\}.
\]

The search objective was to find an admissible cyclic signing whose spectral
radius violates the conjectured lower bound.  A positive hit can subsequently
be upgraded to a proof by exact rational arithmetic.  Failure to find a hit in
a finite beam, annealing, language, or Hamming-neighborhood search is only
negative experimental evidence.  It is not a proof that no counterexample
exists.

This distinction is the principal contract of the lane.  Its historical lane
status was

```text
TASK55_ORDERS_34_46_PARTIAL_N40_ONLY
```

For current classification purposes this report has status
`SUPERSEDED_BY_TASK55_SMALL_ORDER_EXACT_CLASSIFICATION`.

## 2. Discovery outcome

The searches recovered one certifiable hit, at order 40.  The word and lift are

```text
Q bits = 1000100010001000100010001000100010001000
canonical Q code = 73300775185
alpha = -1
gap word = (4,4,4,4,4,4,4,4,4,4).
```

The exact certification of this hit is given in
`TARGET_A_ORDERS_34_46_EXACT_CLASSIFICATION.md`.  This bounded-search lane did
not settle the other six orders; the later exact classifier settled all six in
the affirmative for the conjectured lower bound.

| order | stored best lift | stored canonical Q code | stored positive margin | historical lane status |
|---:|---:|---:|---:|---|
| 34 | +1 | 286331153 | 0.07072256857384751 | `OPEN_BOUNDED_SEARCH_ONLY` |
| 36 | -1 | 1145311505 | 0.05197864446122491 | `OPEN_BOUNDED_SEARCH_ONLY` |
| 38 | +1 | 4567863569 | 0.0438583156 | `OPEN_BOUNDED_SEARCH_ONLY` |
| 40 | -1 | 73300775185 | exact certificate below threshold | `COMPUTER_ASSISTED_PROVED` |
| 42 | +1 | 73300775185 | 0.015267281028362056 | `OPEN_BOUNDED_SEARCH_ONLY` |
| 44 | -1 | 293199745297 | 0.011507122838066 | `OPEN_BOUNDED_SEARCH_ONLY` |
| 46 | +1 | 1169373073681 | 0.004990282450388 | `OPEN_BOUNDED_SEARCH_ONLY` |

The decimal margins in the open rows are search diagnostics, not interval
certificates.  In particular, their positivity records how narrowly the best
observed candidates missed the counterexample inequality; it cannot be used to
infer a positive minimum over all admissible words.

## 3. Bounded-search provenance

The frozen certificate records the following explored state counts:

- beam search: 1,145,182 canonical states;
- annealing search: 1,439,618 canonical states;
- order-46 Hamming-six search: 9,366,819 raw states and 3,987 canonical
  survivors;
- local-language search at orders 42, 44, and 46: respectively 1,740, 14,830,
  and 27,509 canonical classes.

The order-46 Hamming-six raw and survivor streams are bound by SHA-256 digests
in `TARGET_A_ORDERS_34_46_CERTIFICATES.json`.  These hashes establish the
identity of the recorded finite searches.  They do not enlarge the logical
scope of those searches.

## 4. Historical and current classification

Within this lane, only order 40 is `COMPUTER_ASSISTED_PROVED` to admit a
counterexample.  The status at orders 34, 36, 38, 42, 44, and 46 is exactly
`OPEN_BOUNDED_SEARCH_ONLY`: the searches recorded here did not exhaust those
orders.

Those historical labels have now been superseded by a different, exhaustive
exact certificate.  The independent checker for
`TARGET_A_SMALL_ORDER_EXACT_THEOREM.md` proves that no counterexample exists at
the six orders.  Combining that theorem with the inherited classification
through order 32, the still-valid order-40 LDL certificate, and the certified
tail gives the current exact classification

\[
 \boxed{\text{failure exactly at }n=32,\ n=40,\text{ and every even }n\ge48}
\]

for even \(n\ge8\).  In particular, neither this bounded search nor the current
classification says that every even \(n\ge32\) fails.

## 5. Reproducibility artifacts

- producer: `research/scripts/target_a_task55_orders_34_46.py`;
- independent checker:
  `research/scripts/verify_target_a_task55_orders_34_46.py`;
- certificate:
  `research/proofs/task55/TARGET_A_ORDERS_34_46_CERTIFICATES.json`;
- fail-closed tests:
  `research/scripts/test_target_a_task55_orders_34_46.py`.

The checker independently reconstructs the order-40 signing matrix and exact
LDL certificate.  The tests reject status promotion, missing or reordered
orders, modifications of the exact certificate and its hashes, duplicate JSON
keys, and the false claim that all even orders at least 32 fail.
The legacy checker intentionally continues to enforce the historical scope of
its own certificate; current nonexistence at the other six orders is verified
separately by `verify_target_a_task55_small_order_exact.py`.
