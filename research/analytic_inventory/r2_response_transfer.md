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

For row-response propagation one needs the dual orientation.  Define

\[
Q=10^{-4}
\begin{pmatrix}
11503&614&990&-1101\\
614&10470&15&113\\
990&15&12299&-2632\\
-1101&113&-2632&13260
\end{pmatrix}.
\]

Exact rational LDL checks also give

\[
\frac9{10}I\preceq Q\preceq2I,
\qquad LQL^{\mathsf T}\prec\frac25Q.
\]

This is the correctly oriented certificate for \(R\mapsto RL\) and
\(W\mapsto L^{\mathsf T}W\).  The earlier \(P\)-certificate controls the
column/linearized Riccati action; both metrics are needed.

## Uniform local transfer bound

On the Riccati ball \(\mathcal B\) from `r2_local_contraction.md`, write

\[
L(X)=X^{-1}E_+F_+(X)^{-1}E_-.
\]

The inverse perturbation identity and the lower bounds
\(X,F_+(X)\succeq I/3\) imply, in upper-triangular coordinate norm,

\[
\|L(X)-L(X_{12})\|_P<10^{-4}.
\]

For clarity, a deliberately loose derivation uses
\(\|E_\pm\|_F<4\), inverse norms at most \(3\), and
\(\|F_+(X)-F_+(X_{12})\|\le216\|X-X_{12}\|\).  The resulting raw
Lipschitz constant is below \(1.5\cdot141000\), which is still below
\(10^6\); multiplying by the radius \(10^{-10}\) gives the displayed
bound with substantial slack after the norm-equivalence factors are applied.

Since \(\sqrt{2/5}<2/3-10^{-4}\), it follows that

\[
\|L(X)\|_P<\frac23\qquad(X\in\mathcal B).
\]

Thus every response product that remains in the local bulk regime has a
geometric \((2/3)^j\) bound in the correctly oriented \(Q\)-norm.

## Exact entrance bound

Starting with the three fixed wrap couplings and carrying out 24 open-chain
block eliminations gives exact rational response matrices satisfying

\[
RQ R^{\mathsf T}\prec10^{-10}I_2,
\qquad
W^{\mathsf T}QW\prec10^{-10}I_4.
\]

This finite entrance calculation is checked by the same Fraction verifier.
Combined with the local two-cell \(Q\)-contraction, it supplies an explicit
geometric bound on all later propagated response terms.  The only remaining
work for the residue-two family is to insert these bounds into the fixed
terminal-coupling formula for the six-by-six core and derive one rational
tail inequality.

## Scope

This is not yet the cyclic boundary theorem.  The final core also contains
fixed wrap-around couplings, and their limiting six-by-six Schur complement
must still receive an exact positive-margin calculation.  The next proof
obligation is to form that limiting core and sum the now-controlled geometric
response tails.

The certificate is checked by

```text
python research/scripts/verify_target_a_r2_local_lyapunov.py
```
