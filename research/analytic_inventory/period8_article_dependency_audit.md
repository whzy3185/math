# Dependency audit for the frozen analytic article

## Main theorem line

\[
\begin{array}{c}
\text{Hamilton-gauge realization}\\
\downarrow\\
\text{twisted Fourier benchmark}\qquad
\text{period-eight finite Bloch reduction}\\
\downarrow\qquad\qquad\downarrow\\
\rho_-(8L)^2>1561/200\qquad
\rho(A_{\tau_*})^2<1561/200\\
\qquad\qquad\downarrow\\
\text{infinite counterexample theorem.}
\end{array}
\]

Every arrow is a direct analytic proof.  The main theorem has no dependency
on the period-eight trichotomy, general-period moments, finite enumeration,
R2/R4/R6, G6, or Lean.

## Structural strengthening line

\[
\begin{array}{c}
\text{local square identity}\\
\downarrow\\
\text{general periodic moment obstruction}\\
\downarrow\\
\text{period-eight high-defect exclusion}\\
\qquad\searrow\quad\quad\swarrow\\
\text{two-defect finite integer lemma}\quad
\text{target Floquet edge}\\
\qquad\qquad\downarrow\\
\text{period-eight trichotomy.}
\end{array}
\]

The two-defect lemma is the sole finite component: its recurrence, values,
and trace implication are explicitly printed.  It is not a floating-point
or exhaustive-signing computation.

## Exclusion audit

| Material | Dependency of an article theorem? | Disposition |
|---|---:|---|
| finite exclusions through order 30 | no | exclude |
| order-32 witness | no | exclude, except optional illustrative sentence |
| low-period orbit frontier | no | exclude |
| R2 tail / local Riccati data | no | exclude |
| R4/R6 interface work | no | exclude |
| G6 programme | no | exclude |
| all-even truth pattern | no proof | exclude |
| Lean project | no | post-freeze supplementary verification only |

## Freeze verdict

The analytic proof line for the proposed article is dependency-closed.
Remaining work is manuscript construction, primary-source reference
verification, and a future Lean kernel; it is not a missing mathematical
premise of the theorem package.
