# Lean formalization contract for the analytic article

## Standard for the manuscript statement

The article may say “the theorem kernel has been formally verified in Lean”
only after every item in the main-theorem line below builds with no proof
placeholder or author-added axiom.  A passing build of unrelated arithmetic
lemmas does not qualify.

## Required theorem kernel

| ID | Informal article content | Lean target | Current status |
|---|---|---|---|
| L1 | finite Hamilton-gauge realization | exact matrix equality for every \(n=8L\) and both holonomies | in progress: seam/sign closure checked |
| L2 | twisted benchmark | anti-periodic Fourier block and shifted-grid maximum | in progress: fiber block algebra checked |
| L3 | period-eight fiber | explicit \(8\times8\) fiber and chiral block reduction | open |
| L4 | polynomial certificate | \(P(y,c)>0\) for \(y\ge1561/200,\ c\le2\) | complete: kernel-checked |
| L5 | finite-ring spectral implication | every allowed fiber has squared eigenvalues below the bound | in progress: polynomial-root exclusion checked |
| L6 | trigonometric benchmark comparison | \(\rho_-(8L)^2>1561/200\) for \(L\ge4\) | complete: exact radical base plus cosine monotonicity |
| L7 | main theorem | explicit signing strictly beats the twisted signing for every \(L\ge4\) | open |
| L8 | period-eight trichotomy | optional structural strengthening, including exact finite recurrence | open |
| L9 | general moment obstruction | optional structural strengthening | open |

## Formalization order

1. Prove L4 with rational real arithmetic.
2. Formalize the finite matrix/gauge construction L1.
3. Formalize finite Fourier block algebra L2--L3.
4. Connect Hermitian-fiber eigenvalue roots to L4 for L5.
5. Formalize the trigonometric comparison L6.
6. Combine L1--L6 into L7.
7. Formalize L8--L9 only after the main theorem kernel is complete.

## Writing policy

The paper will retain human-readable proofs.  After L1--L7 are complete, one
sentence may state that the corresponding theorem kernel was independently
checked in Lean, with a repository revision and build command.  It will not
claim that Lean proves excluded R2/R4/R6/G6 or all-even classification
statements.
