# Lean formalization contract for the analytic article

## Standard for the manuscript statement

The article may say “the theorem kernel has been formally verified in Lean”
only after every item in the main-theorem line below builds with no proof
placeholder or author-added axiom.  A passing build of unrelated arithmetic
lemmas does not qualify.

## Required theorem kernel

| ID | Informal article content | Lean target | Current status |
|---|---|---|---|
| L1 | finite Hamilton-gauge realization | exact matrix equality for the explicit \(\alpha=+1\) witness at every \(n=8L\) | complete: finite Hamilton matrix, cell reindexing, seams, and full cell action checked |
| L2 | twisted benchmark | shifted-grid lower bound used in the main comparison | complete: exact threshold comparison checked |
| L3 | period-eight fiber | explicit \(8\times8\) fiber and chiral block reduction | complete: fiber similarity, chiral block, and eigenvalue polynomial |
| L4 | polynomial certificate | \(P(y,c)>0\) for \(y\ge1561/200,\ c\le2\) | complete: kernel-checked |
| L5 | finite-ring spectral implication | every finite \(\alpha=+1\) witness eigenvalue has squared value below the bound | complete: finite matrix → cells → ZMod DFT → nonzero fiber → strict bound checked |
| L6 | trigonometric benchmark comparison | \(\rho_-(8L)^2>1561/200\) for \(L\ge4\) | complete: exact radical base plus cosine monotonicity |
| L7 | main theorem | every Hermitian eigenvalue of the explicit \(\alpha=+1\) signing strictly beats the twisted squared benchmark for every \(L\ge4\) | complete: exposed as `period8_alpha_plus_main_theorem` |
| L8 | period-eight trichotomy | optional structural strengthening, including exact finite recurrence | open |
| L9 | general moment obstruction | optional structural strengthening | open |

## Formalization order

1. Prove L4 with rational real arithmetic.
2. Formalize the finite matrix/gauge construction L1.
3. Formalize finite Fourier block algebra L2--L3.
4. Connect Hermitian-fiber eigenvalue roots to L4 for L5.
5. Formalize the trigonometric comparison L6.
6. Combine L1--L6 into L7 in Hermitian eigenvalue-radius form.
7. Freeze L1--L7. Do not formalize L8--L9 in the present manuscript pass.

## Writing policy

The paper will retain human-readable proofs.  After L1--L7 are complete, one
sentence may state that the corresponding alpha = +1 theorem kernel was
independently checked in Lean, with a repository revision and build command.
The statement must not imply formal coverage of alpha = -1, R2/R4/R6/G6, the
old enumerations, or any all-even classification statement.
