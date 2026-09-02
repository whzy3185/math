# Residue-two cyclic response recurrence

## Exact block identity

Write the normalized block matrix as a two-site left boundary \(V_0\), a
chain of four-site blocks \(V_1,\ldots,V_m\), and the three fixed
wrap-around couplings \(V_0\! -\!V_1\), \(V_0\! -\!V_m\), and
\(V_1\! -\!V_m\).  Eliminating the current block gives

\[
\begin{aligned}
G'&=G-RX^{-1}R^{\mathsf T},\\
H'&=H-W^{\mathsf T}X^{-1}W,\\
C'&=C-RX^{-1}W,\\
R'&=-RX^{-1}E,\\
W'&=-E^{\mathsf T}X^{-1}W,\\
X'&=D-E^{\mathsf T}X^{-1}E.
\end{aligned}
\]

At the final elimination, the coupling into the retained last block is

\[
W_{m-1}^{\rm total}=W_{m-1}^{\rm propagated}+E_{m-1}.
\]

The added \(E_{m-1}\) is the physical nearest-neighbour coupling between
the penultimate and retained terminal block.  Omitting it produces a
different Schur complement, so it is a mathematical boundary condition, not
an implementation detail.

The final cyclic core is

\[
S_m=\begin{pmatrix}G_m&C_m\\C_m^{\mathsf T}&H_m\end{pmatrix}.
\]

Repeated application of the block Schur identity proves the recurrence for
every chain length.  The companion Fraction verifier reconstructs both this
recurrence and a direct full-matrix elimination at six residue-two orders;
their equality is an implementation cross-check rather than the proof of the
block identity itself.

## Role in the analytic closure

The response-transfer lemma now applies to exactly the matrices entering
\(S_m\).  It can therefore bound the propagated part geometrically; only
the fixed terminal addition must be retained explicitly in the limiting-core
calculation.

Verify with:

```text
python research/scripts/verify_target_a_r2_response_recurrence.py
```
