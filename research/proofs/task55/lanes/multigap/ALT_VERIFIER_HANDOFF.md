# Task 55 Multi-Gap Second-Organization Verification

## Verdict

```text
TARGET_A_TASK55_MULTIGAP_ALT_VERIFY_PASS
```

The 31,008-row finite certificate passes without qualification. The `(3,3)`
theorem and its lower bound also pass. The proof write-up and manifest were
corrected after this verifier found the second `a=1` numerator `902`; they now
record both possible values and the uniform lower bound `N>=874`.

The alternative verifier is
`research/scripts/verify_target_a_task55_multigap_alt.py`.  It uses only the
Python standard library and imports neither the producer nor either existing
checker.  It does not reuse their enumeration, defect, `Q`, `tau`, matrix, or
Rayleigh routines.

## Independent Finite Enumeration

For each

```text
S in {2,6,10,14,18},
```

the verifier traverses all `2^(S-1)` separator masks.  It retains words with
at least two positive parts, applies reflection canonicalization directly in
integer-tuple order, and detects zero-charge contiguous subwords by repeated
prefix charges.  Sorting by `(S,word)` gives

| `S` | canonical primitive words |
|---:|---:|
| 2 | 1 |
| 6 | 16 |
| 10 | 186 |
| 14 | 2,275 |
| 18 | 28,530 |
| **total** | **31,008** |

The independent word projection digest is

```text
1c635aa6c50d8dc2387508cf7ce63f67e6a2ced490a3ca6b4eacbe8b8c912bfb.
```

## Independent Operator Reconstruction

For every JSONL row, the verifier reconstructs the defect positions from the
gap word and uses exactly

```text
D=(-4 Z_{>=0}) union {x_0,...,x_m} union (S+4 Z_{>=0}),
Q_i=+1 on D and -1 off D,
tau_0=1,
tau_(i+1)=Q_i tau_i.
```

For a vector on `I_g=[-2,S+2]`, it evaluates

```text
(Av)_k=v_(k-1)+v_(k+1)+tau_(k-2)v_(k-2)+tau_k v_(k+2)
```

at every coordinate of `J_g=[-4,S+4]`.  In particular, it never substitutes
the truncated quantity `||(P_I A P_I)v||^2`.  Direct integer arithmetic gives

```text
N*10^15 > 7905369311620328*D
```

for all 31,008 rows.  It also reproduces

```text
stream SHA-256 = 9c8ef135fc11ca7b8c1761c3d45fb89c65790d97c12f2081787814f046c038bf
max |v_i|       = 11
max N           = 6226
max D           = 442
```

and the unique weakest row

```text
g=(3,3)
v=(3,0,5,7,6,9,7,8,6,2,4)
N/D=2930/369.
```

The Task 51 `c6` artifact is independently bound by its SHA-256.  A rational
Sturm chain implemented in this verifier counts exactly one degree-ten root
in

```text
(7905369311620327/10^15, 7905369311620328/10^15).
```

Thus every strict integer Rayleigh comparison is strictly above `c6`.

## Strict Format Audit

The manifest must be canonical two-space ASCII JSON with a terminal LF and
the exact declared schema.  Duplicate object keys, BOM, CR/CRLF, non-ASCII,
floating-point scalars, trailing JSON, reordered bytes, or changed fields are
rejected.  The JSONL stream must be compact ASCII JSON with one terminal LF;
each row must contain only bounded exact integers.  Missing, duplicate,
reordered, noncanonical, nonprimitive, sign-unnormalized, or gcd-reducible
records are rejected by reconstruction rather than trusted metadata.

The run includes explicit negative parser probes for duplicate keys, CRLF,
BOM, trailing JSON, floating-point values, booleans, oversized integers, and
noncompact rows.

## `(3,3)` Local Lemma

Translate the first motif defect to zero.  Only `tau` on `[-4,8]` can multiply
a nonzero vector coordinate for a vector supported on `[-2,8]` and its full
image on `[-4,10]`.  Equivalently, only `Q` on
`[-4,-1] union [0,7]` matters after fixing `tau_0=1`.  Therefore a complete
audit must inspect every earlier-defect subset compatible with each nearest
predecessor, not just the nearest predecessor itself.

The verifier uses the five exhaustive nearest-predecessor classes

```text
a=1,2,3,4, and the common case a>=5,
```

with every subset of still-earlier defects in `[-4,-1]`.  On the right it uses

```text
b=1 and the common case b>=2,
```

because only `Q_7` distinguishes the successor locally.  This gives 32 local
patterns.  Their exact squared numerators are:

| predecessor | possible `N` | certified lower quotient |
|---|---:|---:|
| `a=1` | `874, 902` | `874/106=437/53` |
| `a=2` | `258` | `258/32=129/16` |
| `a>=3` | `838` | `838/106=419/53` |

The extra `N=902` subcase occurs when `a=1` and the next defect to the left is
at `x-2`.  Thus the existing exact-coordinate sentence is false in that
subcase, but its recorded `874/106` is still a valid uniform lower bound.

The minimum has exact margin

```text
419/53 - 7905369311620328/10^15
= 1928310515327/6625000000000000 > 0.
```

For the other lift, let `(Dv)_i=(-1)^i v_i`.  Coefficientwise substitution
in the four operator terms gives

```text
A_(-tau) D v = -D A_tau v.
```

The verifier checks this identity coordinate by coordinate in all 32 finite
dependency cases.  Hence both lifts have the same squared norm, and arbitrary
more distant predecessor/successor defects cannot affect the calculation.
This closes the stated arbitrary-finite-core `(3,3)` subclass.

## Boundary

This second verification confirms the finite 31,008-class theorem and the
arbitrary-length `(3,3)` local lemma after weakening the `a=1` equality to the
uniform lower bound `N>=874`.  It does not prove the universal
`B0 -> B2` statement or motif-free primitive cores with `S>18`.
Reference-cell insertion/removal remains rejected as a spectral equivalence.

No existing certificate, producer, checker, test, proof document, formal
manuscript, Git branch, or remote state was changed by this verification.
