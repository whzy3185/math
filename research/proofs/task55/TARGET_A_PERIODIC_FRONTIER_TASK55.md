# Periodic Frontier Beyond Period 24

Status through period 24: `COMPUTER_ASSISTED_PROVED` from the integrated Task
53 certificate. Task 55 periods 25 and 26: `EXACT_FINITE_READ_ONLY`.

## 1. Statement

The current integrated theorem remains:

```text
among primitive legal periodic phases of period p<=24,
the period-eight target is the unique phase with R(Q)<c6,
modulo the certified equivalences.                          (1)
```

Task 55 advanced the same complete frontier computation in a read-only run:

| period `p` | canonical orbits | post-filter survivors |
|---:|---:|---:|
| 25 | 337,594 | 58 |
| 26 | 649,532 | 95 |

Every one of the 153 survivors received an exact Rayleigh witness strictly
above the certified rational upper endpoint for `c6`. No below-`c6`
competitor was found at period 25 or 26.

Because no Task 55 producer, serialized closure, or independent checker was
created for these two periods, (1) is not enlarged. The complete integrated
frontier is still exactly `p<=24`.

## 2. Evidence

The read-only enumeration used the inherited legality, primitive-period,
symmetry, and exact moment filters. For each period it exhausted the reported
canonical orbit set, partitioned the orbits into filter exclusions and
survivors, and checked every survivor by exact rational Rayleigh comparison.
Floating eigenvectors, where used, served only to propose integer witness
vectors; acceptance used exact arithmetic.

Thus the correct evidence label is `EXACT_FINITE_READ_ONLY`, not numerical
or high precision. The missing issue is proof-artifact independence and
reproducibility, not the arithmetic type of the read-only calculation.

## 3. Exact limitation

The read-only tables do not establish a repository theorem for `p<=26`.
Without the full orbit stream and an independent reconstruction, one cannot
exclude a canonicalization omission, a primitive-period error, a missing
orbit, or a producer/checker shared bug.

Nothing here controls period `p>=27`, aperiodic phases, or finite interfaces.
Nor does a finite frontier imply a uniform gap above `c6`: survivor margins
may shrink with period. No structural tail theorem follows from the counts
`58` and `95`.

## 4. Dependencies

- Integrated Task 53 `p<=24` frontier and its exact `c6` upper endpoint.
- The established legal-orbit equivalences: dihedral action, tau negation,
  primitive normalization, and zone folding, exactly as implemented by the
  existing frontier certificate.
- Exact moment exclusions and exact Rayleigh witness comparison.
- The Task 55 `p=25,26` numbers currently have no bound certificate paths or
  digests and therefore remain read-only evidence.

## 5. Next lemma

Create a period-25/26 producer that records the complete canonical orbit
partition, filter reason, survivor witness, source hashes, and deterministic
stream digests. An independent checker must regenerate all legal orbits and
every exact comparison without importing producer helpers. Only after that
PASS may the integrated frontier be restated as `p<=26`.

The next mathematical step is survivor structure rather than an unbounded
enumeration promise: identify a finite family of local patterns shared by all
153 survivors and prove that each pattern supplies a uniform exact Rayleigh
witness. Such a lemma could replace period-by-period growth with a genuine
frontier tail argument.
