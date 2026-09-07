# Exact repair certificates on the chord-cycle line `L=5`

Date: 2026-09-07.

This note corrects the overly broad heuristic that every short odd chord-cycle
length should behave like the proved `L=3` obstruction.  It does not.

Let

\[
 L=\frac{N}{\gcd(N,s)}.
\]

On the line `N=5s` with odd `s`, reorder vertices as

\[
 i=j+a s,\qquad 0\le j<s,\quad a\in\{0,1,2,3,4\}.
\]

Each column `j` contains the five `s`-chords, hence a signed pentagon block
`B_j`; ordinary neighboring columns are joined by `I_5`, while the last-to-first
matching is the helical signed permutation `S_alpha` carrying Hamilton
holonomy `alpha`.

A pentagon state is recorded by its five chord signs

\[
 (\tau_{j},\tau_{j+s},\tau_{j+2s},\tau_{j+3s},\tau_{j+4s})\in\{\pm1\}^5,
\]

in cyclic order.

## Theorem L5-short

The first three odd members of the `N=5s` line admit explicit signings with
spectral radius strictly below `sqrt(8)`:

\[
 \boxed{m(15,3)<\sqrt8,\qquad m(25,5)<\sqrt8,\qquad m(35,7)<\sqrt8.}
\]

The following block words are exact witnesses.

### `(N,s)=(15,3)`

Take `alpha=+1` and

```text
(-,+,-,+,-)
(+,-,+,-,+)
(-,+,-,+,-)
```

for the three pentagon columns.

### `(N,s)=(25,5)`

Take `alpha=-1` and

```text
(-,+,+,-,-)
(+,-,-,+,+)
(-,-,+,-,-)
(+,+,-,+,+)
(-,-,+,-,-)
```

### `(N,s)=(35,7)`

Take `alpha=-1` and

```text
(-,-,-,-,+)
(+,+,+,+,-)
(-,-,-,-,+)
(-,+,+,+,-)
(+,-,-,-,+)
(-,+,-,+,+)
(+,-,+,-,-)
```

For each displayed signing, form the exact integer matrix

\[
 C=8I-A^2.
\]

The verifier `verify_l5_repair_certificates.py` computes an exact rational
`LDL^T` decomposition of `C` and checks that every diagonal pivot is positive.
Therefore `C>0` by Sylvester/LDL positivity, so every eigenvalue of `A^2` is
strictly below `8`.

The final LDL pivots are, respectively,

\[
 \frac{2872}{1207},\qquad
 \frac{4809344936}{1946220357},\qquad
 \frac{280732937573368}{1166862995234035},
\]

and the script checks positivity of *all* preceding pivots as well.

Numerically, only for orientation,

\[
 \rho^2\approx6.7680958180,\quad
 7.5587325515,\quad
 7.9916366730,
\]

respectively.  These decimals are not used in the proof.

## Consequence

The `L=3` theorem

\[
 m(3s,s)^2\ge8+\frac1{70}\qquad(s\ge7\text{ odd})
\]

is **not** an instance of a blanket theorem saying that every odd chord-cycle
length forces a super-`sqrt(8)` obstruction.  In particular `L=5` remains
repairable through `s=7`.

Thus any correct general resonance theory must depend on more than the parity
of `L`.  The natural next question on this line is whether a new transition
occurs at `s=9` or later.  Current local-search evidence for `(45,9)` is above
`8`, but no all-signing theorem is asserted here.

## Structural difference from `L=3`

For `L=3`, a nine-column low-spectrum rule forces exact bulk alternation
`B_(j+1)=-B_j`, and the helical seam contradicts the signed-triangle invariant
`tr(B^3)=+/-6`.

For `L=5`, open low-spectrum windows admit many non-alternating pentagon-state
words.  The explicit certificates above exploit this extra local freedom and
show that a direct copy of the triangle argument cannot work.

Evidence status: exact finite positive certificates.