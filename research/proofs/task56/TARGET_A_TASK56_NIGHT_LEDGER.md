# Target A Task 56 Night Ledger

Base: `c26c18f9077f184b8a62684baf2feb1e099edccc`.

| ID | Statement | Evidence | Boundary |
|---|---|---|---|
| T56-G1 | Every abnormal single gap `g!=4` has `sup sigma(H_g)>=c6`; equality holds at G6 and every other abnormal gap is strict | `PROVED` relative to the certified G6 edge | six exact small-gap witnesses and one uniform witness for all `g>=9`; reference gap 4 excluded |
| T56-D1 | On the standard residue-two one-G6 ring with `alpha=+1`, `K_n^2=-I` and `K_nA_n=-A_nK_n` for every `n=8k+2` | `PROVED` | global cyclic symmetry; not asserted for `alpha=-1` or arbitrary multi-interface rings |
| T56-D2 | For the same family and `n>=1042`, the near-`c6` cluster is one squared top level of multiplicity exactly two; the two unsquared partners are simple | `COMPUTER_ASSISTED_PROVED` | analytic symmetry plus independently checked Task 55 exact-`2r`; independent Task 56 checker and 14 tests PASS |
| T56-C1 | A gap 1 forces `sup sigma(A^2)>=44/5>c6` | `PROVED` | boundary-independent finite local witness |
| T56-C2 | Every adjacent pair over `{2,3,5}` forces a strict local witness above `c6` | `PROVED` | five new exact 32-case substitutions plus inherited `(3,3)` lemma |
| T56-C3 | Any gap `g>=45` forces `sup sigma(A^2)>=18061/2283>c6` | `PROVED` | one fixed 43-site vector |
| T56-C4 | A possible primitive competitor is reduced to gaps `{2,3,5,6,...,44}`, support at least 22, and no adjacent pair entirely in `{2,3,5}` | `PROVED` necessary condition | word length remains unbounded; universal `B0 -> B2` theorem OPEN |
| T56-F1 | Sequences eventually containing `(3,3)` obey liminf at least `419/53`; sequences containing a certified support-18 local copy obey at least `2930/369` | `PROVED` | local-occurrence subclasses only |
| T56-F2 | Large exact nonzero-residue minimizers eventually avoid every T56-F1 certified local class | `PROVED` | follows from strict local gap and inherited `limsup<=c6`; unrestricted liminf OPEN |
| T56-H1 | Period-25/26 read-only counts reproduce 337,594/58 and 649,532/95; all 153 survivors contain cyclic `---` | `EXACT_FINITE_READ_ONLY` | motif also occurs in period-eight equality phase; no spectral tail theorem |
| T56-E1 | Reference-relative 105/164 graph and 420/656 phase lift have exact `F4/F5` nonnegative reduced costs; zero cyclic SCCs are exactly the reference orbit | `EXACT_FINITE_PRODUCER` | deterministic certificate exists; independent checker and spectral bridge absent |

## Open After Task 56

- universal multi-gap `B0 -> B2` theorem for the remaining finite alphabet and
  unbounded word length;
- general multi-interface symmetry, splitting coefficients, simplicity, and
  genuine three-body interaction;
- reference-relative graph independent checker and graph-cost-to-spectrum bridge;
- unrestricted common liminf and common nonzero-residue limit;
- certified periodic frontier beyond `p=24` or a contextual survivor theorem.

## Rejected Promotions

The period-25/26 recomputation remains read-only. A local `---` motif is not a
strict spectral obstruction. The one-G6 global symmetry is not localized and
cannot be copied independently to an arbitrary multi-interface ring. The
finite-gap obstruction alphabet is not a finite classification because core
length is unbounded.
