# Proof Overview

Put

$$
\theta_n=\rho_-(n)^2
=4+2\cos(2\pi/n)+2\cos(4\pi/n).
$$

Since $A$ is real symmetric,
$\rho(A)^2=\lambda_{\max}(A^2)$.  A no-counterexample certificate gives an
exact Rayleigh lower bound or an exact threshold equality.  A counterexample
certificate proves $tI-A^2\succ0$ for a rational $t<\theta_n$.

## Six proof regions

| region | conclusion | mathematical reduction | exact finite object |
|---|---|---|---|
| even $8\le n\le30$ | no failure | switching and dihedral reduction | completed class lists; integer Rayleigh witnesses or exact optimiser equalities |
| $n=32$ | failure | one period-eight signing | $1561I-200A^2\succ0$ and $1561/200<\theta_{32}$ |
| $n=34,36,38,42,44,46$ | no failure | local compression and a parity-lifted overlap graph | all local windows, all closed walks, and 64 terminal $(Q,\alpha)$ records |
| $n=40$ | failure | one explicit cyclic signing | $15541I-2000A^2\succ0$ and $15541/2000<63/8<\theta_{40}$ |
| even $48\le n<240$ | failure | one structured signing per order | 96 exact sparse rational LDL certificates |
| even $n\ge240$ | failure | residue constructions and tent IMS | four exact endpoints followed by monotonicity |

The terminal total in the third row is
$2+2+6+14+20+20=64$.  A historical handoff wrote 84, but the certificate and
independent reconstruction both give 64.  The incorrect sum is not evidence.

## Repeated rational threshold bound

For $x\ne0$, $\cos x>1-x^2/2$.  Therefore

$$
\theta_n>8-\frac{20\pi^2}{n^2}>8-\frac{200}{n^2},
$$

where $\pi<22/7<\sqrt{10}$ proves the last strict inequality.  The small-order
no-counterexample certificates use tighter exact algebraic intervals.

## Human and machine roles

The written proof supplies switching invariance, local compression, graph
soundness and completeness, the spectral consequences of positive
definiteness, the exhaustive order partition, and tail monotonicity.  Programs
perform only finite exact enumeration, integer quadratic forms, algebraic root
isolation, exact LDL or Bareiss elimination, and independent reconstruction.
