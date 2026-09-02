# Residue-two local response-transfer certificate

## Exact local statement

At the same rational centre \(X_{12}\) used for the Riccati contraction, put

\[
Y_{12}=F_+(X_{12}),
\qquad
L=X_{12}^{-1}E_+Y_{12}^{-1}E_-.
\]

The map \(H\mapsto L^{\mathsf T}HL\) is exactly the two-step derivative of
the Riccati map.  More importantly for boundary propagation, right
multiplication by \(L\) is the two-cell transport occurring in the response
updates.

Let

\[
P=10^{-4}
\begin{pmatrix}
10766&87&19&974\\
87&12664&148&-2418\\
19&148&10093&-25\\
974&-2418&-25&14009
\end{pmatrix}.
\]

Exact rational LDL checks establish

\[
\frac9{10}I\preceq P\preceq2I,
\qquad
L^{\mathsf T}PL\prec\frac25P.
\]

Therefore the centre two-cell response transfer contracts the \(P\)-norm by
strictly less than \(\sqrt{2/5}\).

## Scope

This is not yet the cyclic boundary theorem.  The actual response products
use \(X_j\), not the limiting centre at every step, and the final core also
contains fixed wrap-around couplings.  The next proof obligation is to extend
the \(P\)-contraction uniformly to the local Riccati neighbourhood and then
sum the resulting geometric response tails in the six-by-six Schur core.

The certificate is checked by

```text
python research/scripts/verify_target_a_r2_local_lyapunov.py
```
