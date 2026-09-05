# C_N(1,s): conjectures recorded before the new tests

Date: 2026-09-05. Research branch: `research/circulant-1s-extension`.

## Frozen article

The bilingual period-eight article is frozen at commit
`6766ecbc20b084c648b29b0bf3813b8c1ecf86cb`, tag
`freeze/period8-jgt-2026-09-05`. Its source, figures, bibliography, PDFs,
strengthening package and Lean tree are not to be edited by this extension.
This work uses a separate worktree. Any later manuscript upgrade requires a
separate integration decision; the present task authorizes mathematical research.

## Model and prior local results

Write `C_N(1,s)` with `2 <= s < N/2`, so the underlying graph is simple
and four-regular. Put

`m(N,s) = min_{edge signings sigma} rho(A_sigma)`.

The Hamilton gauge has chord word `tau`, boundary condition
`x_(i+N)=alpha x_i`, and operator

`(A x)_i=x_(i-1)+x_(i+1)+tau_(i-s)x_(i-s)+tau_i x_(i+s)`.

Local Task 60 already established the switching coordinates, complete
collision-safe square formula, alternating-word dispersion and a flat
construction when `N=2s+2`. These are inputs, not new discoveries. Their
relevant calculations will be checked independently.

## C1: exact absolute-minimum classification

For all admissible `(N,s)`,

`m(N,s)=2 if and only if N=2s+2`.

Motivation: `tr(A^2)=4N` forces `rho(A)>=2`, with equality precisely when
`A^2=4I`. Task 60 supplies the forward construction; necessity should be
visible in the length-two displacement channels. Check `s=3` and `(5,2)`
separately rather than assuming the generic channels are distinct.

## C2: rigidity at the absolute minimum

When `N=2s+2` and `s!=3`, every equality signing has Hamilton coordinates

`tau_i=epsilon (-1)^i, alpha=(-1)^(s+1)`.

Thus there are two switching classes in the fixed Hamilton coordinate system,
and one class after allowing graph automorphisms. For `(N,s)=(8,3)`, the
graph is `K_(4,4)` and equality should instead be described by order-four
Hadamard matrices. Full arbitrary automorphisms and the dihedral subgroup
must not be conflated.

## C3: antipodal two-defect extension (deliberately falsifiable)

For every even `s>=2`, let `p=4s` and define the periodic flux word with
`Q_0=Q_(2s)=+1` and all other entries `-1`. Take its lift with `tau_0=1`.
Conjecture that its squared Bloch edge on the infinite step-`(1,s)` graph
is strictly below eight.

This specializes to the proved period-eight phase at `s=2`. It is NOT a
consequence of chirality. One exact fiber with squared radius above eight
refutes it. A phase-grid maximum below eight is numerical evidence only.

## C4: parity-correct half-cell mechanism

For `p=2m`, within the natural monomial class `D T_m`, where
`(Dx)_i=(-1)^i x_i`, the Laurent-fiber anticommutation identity holds for
all phases if and only if

`tau_(i+m)=(-1)^(s+1) tau_i`.

The normalization should still obey `gamma(z)^2=(-1)^m/z`.
Equivalently `Q` is `m`-periodic with half-cell product `(-1)^(s+1)`.
The all-phase quantifier is essential when short fibers merge channels.
For odd `s`, ordinary bipartite chirality must be distinguished from the
specified half-cell operator.

## Evidence discipline and stop for this first round

These are AI-proposed research hypotheses under the user's explicit request
to conjecture before proving. No novelty claim against the literature is made.
Record proof, counterexample and unresolved status separately, retaining this
initial file unchanged. Aim to close C1/C2/C4 analytically and resolve the
first meaningful test of C3. Computer checks support the analytic arguments.

ARS scoping challenge: a flat collision family alone does not settle
fixed-`s`, large-`N` minimization; finite and Bloch problems have different
quantifiers. The report must state this explicitly. No external model is used.
