# Analytic claim registry

This registry controls the scope of the analytic-first manuscript route.
It records mathematical status, not the confidence labels of earlier
repository documents.

| ID | Claim | Evidence class | Permitted manuscript use |
|---|---|---|---|
| P8-1 | Hamilton-gauge realization of every \((\tau,\alpha)\) pair on \(C_n(1,2)\) | direct switching proof | main-text lemma |
| P8-2 | For the displayed period-eight word, the Floquet squared characteristic polynomial is \(P(y,c)\) | direct chiral block calculation; independently symbolically checked | main-text proposition |
| P8-3 | Its infinite-volume squared edge is \(4+\sqrt{10+2\sqrt5}\) | factorization and monotonicity in \(c\) | main-text proposition |
| P8-4 | For every \(8\mid n\), \(n\ge32\), both finite holonomies obey \(\rho(A)^2<1561/200<\rho_-(n)^2\) | direct rational positivity and Taylor bound | main theorem |
| P8-5 | The antipodal two-defect word is the unique period-eight local-flux phase below squared edge \(8\) | analytic moment barrier and Floquet proof, plus a visible finite integer recurrence for three two-defect cases | secondary theorem or appendix theorem |
| F-1 | No counterexample exists at each even order \(8\) through \(30\) | exhaustive exact computation | background only; never call analytic |
| F-2 | \(n=32\) is the smallest counterexample order | F-1 plus an exact \(n=32\) witness | computational corollary only |
| O-1 | Residue-two all-length family | local exact identities; tail closure not independently completed | exclude |
| O-2 | Residue-four/six all-length families | block templates and numerical screens | exclude |
| O-3 | All-even truth pattern or exact \(m_n\) classification | no complete analytic proof | exclude |
| O-4 | G6 physical-edge theorem | scalarization programme only | exclude |

## Main theorem wording currently authorized

For every integer \(L\ge4\), the signed circulant \(C_{8L}(1,2)\) has an
explicit signing with

\[
\rho(A)^2<\frac{1561}{200}<\rho_-(8L)^2.
\]

Thus the alternating twisted signing is not spectrally optimal for every
multiple of eight at least \(32\).

The statement asserts an explicit competing signing.  It does not identify
the minimum spectral radius, classify all minimizers, or infer anything about
orders outside \(0\bmod8\).

## Finite-combinatorial disclosure

Only one component of P8-5 is finite rather than symbolic: the integer
closed-walk recurrence through length twenty for the three non-antipodal
two-defect words.  It should be displayed in an appendix or a short
supplementary lemma, with its recurrence, intermediate moment values, and
the exact verifier path.  No floating-point eigenvalue, exhaustive signing
search, or certificate archive is required for P8-1 through P8-5.

## Pre-submission gates

Before manuscript drafting promotes P8-1 through P8-5 to theorem prose:

1. conduct a human line audit of the Floquet block and the \(2\times2\)
   determinant reduction;
2. verify direct predecessors and terminology with primary literature;
3. choose a journal only after the contribution and reference map are fixed;
4. keep every excluded claim out of the abstract, introduction, and
   conclusion.
