# Lane F Handoff

Status: `EXACT_ALGEBRA_PROVED_PHYSICAL_HIERARCHY_OPEN`.

Accepted exact results:

- quotient-ring involution `e6(lam,P)=P^3 e2(-lam,P^-1)`;
- common quotient norm and its complete factorization;
- exactly two gap-plus-eight transfer classes, odd and even;
- common four-term characteristic and exact generic order-five exterior
  recurrence;
- discriminant obstruction to a real Perron/invariant-cone tail at `c6`.

Independent hostile verification reconstructed the transfer and Evans
algebra without using the producer. The repository checker performs the same
independent reconstruction and compares the complete certificate exactly.

Not accepted:

- equality of physical gap-2 and gap-6 spectra;
- eventual physical-root ordering or monotonicity;
- an all-single-gap lower theorem.

The Task 53 negative duality search is superseded because it created a symbol
named `lambda` while the Evans core used `lam`; those were independent SymPy
variables. The old raw-core comparison is not evidence against the quotient
identity.
