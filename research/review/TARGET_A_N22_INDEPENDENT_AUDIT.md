# Target A Order-22 Independent Audit

Date: 2026-08-22

Status: **PASS**

## Representative Audit

The primary route is the Python fixed-weight FKM necklace generator. The
independent route is the C11 full integer-space scanner: it visits every code
in `[0,2^22-1]`, filters legal parity, directly constructs every dihedral
image, determines the canonical representative and orbit size, and
destructively consumes the corresponding primary table record.

| check | result |
|:---|---:|
| legal `Q` words | 2,097,152 |
| canonical representatives | 48,734 |
| represented switching classes | 8,388,608 |
| missing primary records | 0 |
| duplicate primary records | 0 |
| unconsumed primary records | 0 |
| orbit-size mismatches | 0 |
| canonicality failures | 0 |
| record-level equality | PASS |

The implementations share the mathematical group-action specification and
binary `Q` semantics, but share neither code, traversal, shell decomposition,
data structure, nor implementation language.

## Independent Spectral Decisions

The independent C stream supplies all records to a standalone Hamilton-gauge
matrix reconstruction. For each representative, both `alpha=-1,+1` are
checked. Floating eigensolvers only propose integer vectors; every accepted
nonoptimizer is decided by an exact rational Rayleigh quotient against a
certified algebraic threshold endpoint.

| check | result |
|:---|---:|
| spectral states | 97,468 |
| holonomies | `-1,+1` |
| exact nonoptimizer exclusions | 97,467 |
| exact optimizer checks | 1 |
| uncertified states | 0 |
| final status | PASS |

The ordered independent certificate digest is
`04674adb0fb841e18099b8abf8f63d779a9ad075c964253458c0fe40e4c51bc3`.
Machine-readable details and all source hashes are stored under
`research/reproducibility/target_a_n22_independent_record_audit/` and
`research/reproducibility/target_a_n22_independent_spectral_audit/`.

## Scope

This closes the requested order-22 implementation-independence gap. It does
not alter the theorem, abstract, or manuscript narrative. Exact integer
vectors are deterministically regenerated rather than archived one per state;
the ordered digest binds the complete decision stream.
