# Phase-Slip and G6 Closure

## Charge formalization

Fix the reference sector `B_s` whose positive `Q` sites are `s mod 4`. A gap
of length `g` beginning at a positive site of `B_s` ends at a positive site
of `B_(s+g mod 4)`. Defining `q=g-4` therefore gives the translation-sector
change

```text
sigma(q)=q mod 4.
```

For concatenated gap words, endpoint displacement proves additivity. This is
a combinatorial endpoint invariant in the selected Hamilton gauge; it is not
asserted to be a gauge-invariant flux observable in arbitrary coordinates.
The terminology `phase-slip charge` in this project means exactly this sector
bookkeeping quantity. The proof is in
`research/proofs/task52/TARGET_A_TRANSLATION_CHARGE_THEOREM.md`.

## Exact G6 spectral theorem

The bilateral G6 operator is defined by positive `Q` positions

```text
(-4 Z_{>=0}) union {0,6} union (6+4 Z_{>=0}),
```

with `tau_0=1` and `tau_(i+1)=Q_i tau_i`. Its exact four-by-four defect
transfer is the integral polynomial matrix stored in
`research/proofs/task50/certificates/g6_defect_transfer.json`.

The squared physical level `c6` is the unique root in

```text
(7905369311620327/10^15,7905369311620328/10^15)
```

of

```text
16y^10-520y^9+6913y^8-48448y^7+191768y^6-423904y^5
+484528y^4-270464y^3+137856y^2-19968y+256.
```

Exact transfer multiplication, stable/unstable matching, and a rational
interval Evans determinant give existence, uniqueness, and simplicity of the
positive `A` root `+sqrt(c6)`. A distinct cofactor chart independently checks
the determinant signs, derivative, and nonzero pivots. The two stable
multipliers have modulus at most `9/25`, so matching the stable and unstable
subspaces supplies an exponentially localized eigenfunction.

The global edge theorem adds the missing spectral statement. Resultant roots
above the certified endpoint are merely candidates; every candidate is
rejected by an unsquared physical matching condition in two exact charts. The
norm bound `||A||<=4` closes the ambient interval through 16. The symmetry

```text
(Ku)_i=(-1)^i u_(9-i),  K^2=-I,  KA=-AK,  KA^2=A^2K
```

maps the simple positive root to a simple negative root. Thus `c6` has
multiplicity two for `A^2`, and

```text
sup sigma(A_G6^2)=c6.
```

This corrects the obsolete rank-one formulation. The exact proof bodies are
`task50/TARGET_A_EXACT_INTERFACE_THEOREM.md`,
`task51/TARGET_A_C6_ALGEBRAIC_THEOREM.md`, and
`task53/TARGET_A_G6_GLOBAL_EDGE_THEOREM.md`; the independent checks are
`verify_target_a_task50_interface.py`, `verify_target_a_task51.py`,
`verify_target_a_task53_a2.py`, and `verify_target_a_task53_a3.py`.

## Single-gap scope

The closed single-gap theorem is deliberately no stronger than warranted:

```text
for every positive abnormal gap g!=4, sup sigma(H_g)>=c6;
equality occurs exactly at g=6.
```

For `g=1,2,3,5,7,8`, explicit finite-support integer Rayleigh witnesses are
strictly above `c6`; one fixed witness handles all `g>=9`; `g=4` is reference
bulk and has edge `eta<c6`. The uniform refinement separates every
`g not in {4,6}` by at least `1/250`. It does not claim a theorem about all
multi-gap cores or all finite rings.
