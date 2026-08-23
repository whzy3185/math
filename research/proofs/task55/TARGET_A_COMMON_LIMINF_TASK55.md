# Common-Residue Liminf: Surviving Theorem and Open Cases

Status: restricted dilute-G6 liminf `PROVED`; unrestricted common-residue
liminf `OPEN`.

## 1. Statement

Let `A_j` be legal signed adjacency matrices on rings with orders tending to
infinity and let `H_j=A_j^2`. If one can root each ring at a G6 interface so
that the surrounding period-eight bulk radius tends to infinity, then

```text
liminf_j rho(A_j)^2 >=c6.                              (1)
```

This restricted dilute-G6 theorem survives the Task 55 rank correction. Its
proof uses one finitely supported approximation to a G6 `c6` eigenvector; it
does not use an exact-`r` or exact-`2r` cluster count.

For the minimizing values `m_n`, the unrestricted claims

```text
liminf_(k->infinity) m_(8k+r)^2 >=c6,
r in {2,4,6},                                         (2)
```

remain open.

## 2. Proof of the restricted statement

After rooting and passing to a diagonal subsequence, the local coefficient
words converge on every fixed window to a bounded bi-infinite operator
`A_infinity`; put `H_infinity=A_infinity^2`. Every finitely supported vector
embeds isometrically into all sufficiently large rings with exactly the same
quadratic form. Therefore

```text
||H_infinity|| <=liminf_j ||H_j||
                 =liminf_j rho(A_j)^2.                (3)
```

Under the dilute-G6 hypothesis the pointed limit is the single-G6 operator.
Its squared spectral top is `c6`. Equivalently, truncated G6 eigenvectors
already force the right side of (3) arbitrarily close to `c6`. This proves
(1).

## 3. Exact limitation

An arbitrary contradiction sequence for (2) need not contain a growing pure
bulk neighborhood around a G6 interface. Four independent cases remain
uncontrolled:

- `TIGHT_CLUSTER_BLOCKER`: bounded-diameter charge may converge to a
  non-elementary finite core not covered by the G6 theorem;
- `DICHOTOMY_BLOCKER`: separated components may have different signed charges
  and need not individually be G6;
- `VANISHING_BLOCKER`: charge may escape every fixed window while all ordinary
  pointed limits are pure bulk; and
- `APERIODIC_LIMIT_BLOCKER`: a pointed limit may have positive symbolic
  complexity and need not be periodic or finite-core.

The complete periodic frontier through `p<=24`, and the read-only extension
through `p=26`, do not control the last case. The finite support-18 multi-gap
certificate does not classify arbitrary tight clusters. Reference-relative
cost evidence has no proved spectral bridge and therefore does not close the
vanishing case.

## 4. Dependencies

- Pointed compactness and the lower-semicontinuity direction (3).
- The certified single-G6 global edge `sup sigma(H6)=c6`.
- Local convergence of increasingly large period-eight neighborhoods.
- No dependence on the withdrawn exact-`r` theorem, the independently proved
  exact-`2r` theorem, or high-precision interaction data.

## 5. Next lemma

A decisive next lemma should close one member of the charge trichotomy rather
than assume it away. Two viable targets are:

1. a tight-core theorem proving `sup sigma(H)>=c6` for every finite-core
   `B0 -> B2` interface; or
2. a coercive excursion theorem showing that every sufficiently separated
   nonzero charged excursion yields a uniform local Rayleigh witness above
   `c6-epsilon`.

The first would address tightness and feed the components of dichotomy. The
second would address vanishing. Neither is currently proved, so (2) must
remain `OPEN`.
