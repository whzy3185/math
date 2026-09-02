# Rational Lyapunov certificate at the residue-two Riccati centre

## Exact checked statement

Let \(X_{10}=\Phi^{10}(D)\), where all Riccati operations are performed over
`Fraction`, and let \(J=D\Phi(X_{10})\) in the standard ten-coordinate basis
of symmetric four-by-four matrices.  Define \(W=10^{-4}W_0\), where

\[
W_0=\begin{pmatrix}
10125&118&156&-171&30&73&-78&64&-140&77\\
118&10141&107&-96&39&79&-79&24&-32&6\\
156&107&10436&-492&24&151&-163&228&-527&307\\
-171&-96&-492&10588&-18&-152&177&-266&639&-386\\
30&39&24&-18&10014&12&-6&13&-27&16\\
73&79&151&-152&12&10132&-150&-3&49&-54\\
-78&-79&-163&177&-6&-150&10184&12&-78&79\\
64&24&228&-266&13&-3&12&10268&-641&387\\
-140&-32&-527&639&-27&49&-78&-641&11592&-992\\
77&6&307&-386&16&-54&79&387&-992&10638
\end{pmatrix}.
\]

Exact rational LDL elimination verifies

\[
W\succ0,
\qquad
\frac14W-J^{\mathsf T}WJ\succ0.
\]

The matrices in this statement are rational: \(X_{10}\) is produced by a
finite rational recurrence and \(W\) has denominator \(10^4\).  No
floating-point inequality is used in this check.

## Interpretation

At the exact centre \(X_{10}\), the two-step Riccati map is a strict
contraction with factor at most \(1/2\) in the \(W\)-norm.  This is a local
algebraic fact, not yet a global theorem on the existing large Loewner boxes.

## What remains

To use this certificate in a proof, one must still provide:

1. a rational neighbourhood \(\mathcal N\) of \(X_{10}\) on which
   \(\frac14W-D\Phi(X)^{\mathsf T}WD\Phi(X)\succ0\) holds uniformly;
2. a rational proof that the original bulk orbit enters \(\mathcal N\);
3. a response-variable analogue that bounds the final cyclic six-by-six
   boundary core.

Thus this certificate is the first local component of the residue-two
analytic programme, not a proof of the residue-two family by itself.
