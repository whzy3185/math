# A single non-complement defect cannot persist in a width-five sub-threshold strip

This note strengthens `N5S_WIDTH5_LOCAL_COMPLEMENT_RULE.md` by treating an isolated non-complement transition in an otherwise perfectly complement-alternating background.

Let a width-five open strip be described by pentagon edge-sign states `eta_j in {+-1}^5`, with identity matchings between adjacent columns. A transition is **complement** if `eta_(j+1)=-eta_j`.

## Theorem 1 (fifteen-column single-defect exclusion)

Suppose a fifteen-column open strip has exactly one non-complement transition, between columns `6` and `7`, while every other transition is complement. Then

\[
\boxed{\rho(M)^2>8.}
\]

Consequently, a sub-`sqrt(8)` width-five strip cannot contain a non-complement transition surrounded by six complement transitions on one side and seven on the other; by reversal the same holds with the sides interchanged. In particular, in a cyclic seam-free region, a non-complement transition cannot be arbitrarily isolated.

### Proof

Use a five-bit mask to record the negative edges of each signed pentagon. Under the spectral-radius-preserving operations used in the thirteen-column theorem, the state immediately before the exceptional transition may be normalized to the all-positive mask `0`. The XOR mask

\[
\delta=\eta_6\oplus\eta_7
\]

is unaffected by common row switching and global complementation, and is acted on only by the dihedral group of the pentagon. Excluding the complement mask `31`, the 31 possible bad masks therefore reduce to the seven dihedral orbit representatives

\[
\boxed{0,1,3,5,7,11,15.}
\]

For each representative, all remaining column states are then forced by complement alternation. Hence there are only seven canonical fifteen-column matrices to check.

For each one, the table below gives an explicit integral Rayleigh certificate for

\[
Q=M^2-8I.
\]

The vector itself is listed in the companion verifier; the table records its exact squared norm and exact excess.

\[
\begin{array}{c|c|c|c}
\delta&|\delta|&w^Tw&w^TQw\\ \hline
0&0&270&660\\
1&1&258&312\\
3&2&258&316\\
5&2&268&124\\
7&3&226&98\\
11&3&9346&15\\
15&4&270&8
\end{array}
\]

Every final entry is strictly positive. Therefore every one of the seven canonical matrices has a vector with Rayleigh quotient for `M^2` strictly larger than eight. Thus `rho(M)^2>8` in every case. `square`

No floating-point computation is needed to verify this theorem: `verify_n5s_width5_single_defect.py` contains the seven integer vectors and evaluates all seven quadratic forms in exact integer arithmetic.

---

## Relation to the thirteen-column local rule

The earlier theorem says that two adjacent non-complement transitions cannot occur in the interior of a sub-threshold strip. The present theorem says that a single bad transition cannot be surrounded for too long by complement transitions. Thus a putative sub-threshold cyclic word on `N=5s` must have non-complement defects that are

1. separated by at least one complement transition, but
2. recurrent within bounded distance.

This converts the next global problem into a finite-spacing defect system. The remaining task is to classify the allowed pairs of isolated defects and their separations, then impose cyclic/helical seam compatibility.