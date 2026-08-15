# Quotient Completeness Audit

Date: 2026-08-15

Final status: **PASS**

This audit checks the `(Q,alpha)/D_n` spectral-state reduction before any
minimality search at `n>=24`.  The machine-readable record is
`research/audit/quotient_completeness_audit.json`, SHA-256
`db89bc53edf0c5de6298b030dc304bf6499f151613800b674af5bbef134a6681`.

## A. Full `n=20` raw-versus-quotient comparison

The raw switching-class enumeration was rerun from scratch during this audit.
It completed all 2,097,152 classes in 70.7320 seconds.  The quotient search
completed all 27,296 spectral states in 1.1709 seconds.

| Check | Raw enumeration | Quotient enumeration | Result |
|---|---:|---:|---|
| switching classes represented | 2,097,152 | 2,097,152 | PASS |
| optimizer switching classes | 2 | 2 | PASS |
| counterexamples | 0 | 0 | PASS |
| exact fallbacks | 0 | 0 | PASS |
| smallest non-optimizer rho | 2.804361313158372 | 2.804361313158375 | PASS |
| smallest non-optimizer quotient state | `(17425,-1)` | `(17425,-1)` | PASS |

The tiny displayed difference in the two numeric radii is eigensolver roundoff
and is not used for the exact no-counterexample decision.  The raw run gave
rational Rayleigh exclusion certificates for all 2,097,150 non-optimizer
switching classes.  The quotient run gave such certificates for all 27,295
non-optimizer spectral representatives.

The following assertions all passed:

1. both searches completed with status `PASS`;
2. the exact optimizer state attains the same threshold;
3. the represented optimizer-class count is two in both descriptions;
4. all 20 raw class codes attaining the smallest non-optimizer radius map to
   the single quotient state `(canonical_Q_code=17425, alpha=-1)`;
5. both counterexample counts are zero;
6. the sum of quotient orbit sizes, including the two global-sign lifts,
   recovers exactly 2,097,152 switching classes;
7. the 13,648 Q-orbits agree with an independent Burnside calculation.

## B. Adversarial `n=22` orbit expansion

Sampling used Python's deterministic `random.Random` with seed `20260815`.
Thirty-two quotient states were sampled without replacement from the ordered
97,468-state list.

For every sampled state, the complete dihedral Q-orbit was expanded.  For
each orbit member the audit searched all 44 vertex maps

`i -> epsilon*i+s mod 22`, with `epsilon in {+1,-1}` and `0<=s<22`,

and explicitly solved the switching equations.  When the triangle-flux lift
changed sign, global edge negation was included and checked separately.

Results:

- sampled quotient states: 32;
- dihedral Q-members checked: 1,386;
- switching classes represented after global-sign expansion: 2,772;
- members lacking an exact dihedral/switching/global-negation relation: 0;
- global negations failing to preserve `(Q,alpha)`: 0;
- global negations failing the matrix identity `A_(-sigma)=-A_sigma`: 0;
- orbit-size mismatches: 0;
- Q-orbit count: 48,734, matching Burnside;
- spectral-state count: 97,468, matching the completed `n=22` search.

As a diagnostic only, every expanded member was also diagonalized numerically.
The maximum spectral-radius drift was `6.661338147750939e-15`.  Exact spectral
equality follows from the matrix relations below, not from this floating
check.

## C. Mathematical completeness proof

### 1. Switching equivalence

For a vertex sign vector `d in {±1}^n`, put `D=diag(d)`.  Switching sends

`A_sigma -> D A_sigma D`.

This is an exact similarity because `D^2=I`; it preserves the complete
spectrum and spectral radius.  In a connected graph, fixing the signs on a
spanning tree leaves one unique representative per switching class.

### 2. Complete cycle coordinates

Use the step-1 path edges `0-1,...,(n-2)-(n-1)` as the spanning tree and
switch them to `+1`.  The remaining step-1 edge has sign equal to the
Hamilton holonomy `alpha`.  The `n` step-2 edge signs are then uniquely
determined by the `n` triangle fluxes through

`tau_i = a_i*a_(i+1)*b_i`.

Conversely, any `(tau_0,...,tau_(n-1),alpha)` reconstructs exactly one
tree-gauge signing.  Thus these `n+1` signs are complete coordinates on all
`2^(n+1)` switching classes; no cycle information is omitted.

### 3. Global negation

Global edge negation sends `A_sigma` to `-A_sigma`, so it preserves spectral
radius.  Every triangle has odd length, hence every `tau_i` changes sign.
The Hamilton cycle has even length, hence `alpha` does not change.  Therefore

`Q_i=tau_i*tau_(i+1)`

also does not change.  Given Q with `product_i Q_i=1`, choosing `tau_0`
recursively determines all triangle fluxes; the two choices of `tau_0` are
exactly the two global-negation partners.  Consequently `(Q,alpha)` is a
complete coordinate system for spectral radius after quotienting global
negation.

There are `2^(n-1)` even-parity Q-vectors and two alpha values, giving exactly
`2^n` pre-dihedral spectral states.

### 4. Dihedral automorphisms

Every map `i -> epsilon*i+s mod n` preserves step distances 1 and 2, so it is
an automorphism of `C_n(1,2)`.  Relabeling vertices conjugates the signed
adjacency matrix by a permutation matrix.  It preserves `alpha` and acts on
Q by a rotation or a reflected rotation.  Combining this permutation with a
possible switching and global negation preserves spectral radius exactly.

The audit code does not merely compare canonical bit strings: for every
expanded sample member it constructs the transformed signing and solves for
the switching diagonal entry by entry.

### 5. Orbit decomposition and space recovery

Let `R` contain one binary-bracelet representative of each even-parity Q
orbit.  For fixed alpha, a representative Q with dihedral orbit size `s`
represents `2s` switching classes: `s` relabelings and two global-sign lifts.
Therefore the number of represented switching classes is

```text
sum_(alpha=±1) sum_(Q in R) 2*|D_n Q|
= 2 * 2 * 2^(n-1)
= 2^(n+1),
```

which is exactly the full switching-class count.  Distinct bracelet
representatives have disjoint Q-orbits, and the two alpha values cannot be
identified by switching, global negation, rotation, or reflection.  Hence no
spectral state is lost and none is counted twice at the quotient level.

## Audit limitations and next gate

This PASS validates the current visited-orbit canonicalizer and the
mathematical quotient used at `n=20,22`.  The constant-memory direct bracelet
stream proposed for large `n` in the minimality plan is a new implementation;
before production use it must match the validated generator for all even
`n<=22` and match independent Burnside totals at `n=24,26,28,30`.

Task 32 is complete.  Task 33 is now mathematically authorized, but no
`n=24` spectral search was started as part of this audit.
