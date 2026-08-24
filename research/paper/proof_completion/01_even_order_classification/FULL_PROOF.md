# Full Proof

## 1. Certificate principles

Let $A$ be a signed adjacency matrix of $C_n(1,2)$ and set

$$
\theta_n=4+2\cos\frac{2\pi}{n}+2\cos\frac{4\pi}{n}.
$$

Switching conjugates $A$ by a diagonal $\{\pm1\}$-matrix and preserves its
spectrum.  Since $A$ is real symmetric,

$$
\rho(A)^2=\lambda_{\max}(A^2)
=\max_{v\ne0}\frac{\|Av\|^2}{\|v\|^2}.                 \tag{1}
$$

Thus an exact vector with quotient at least $\theta_n$ rules out a
counterexample.  Conversely, if $pI-qA^2\succ0$ for positive integers $p,q$,
then $\rho(A)^2<p/q$; if also $p/q<\theta_n$, the signing is a
counterexample.

We shall use

$$
\theta_n>8-\frac{200}{n^2}.                            \tag{2}
$$

Indeed, applying $\cos x>1-x^2/2$ at $2\pi/n$ and $4\pi/n$ gives
$\theta_n>8-20\pi^2/n^2$, and $\pi^2<10$.

## 2. Even orders from 8 through 30

For every even $8\le n\le30$, exact finite exhaustion proves

$$
\rho(A)^2\ge\theta_n                                  \tag{3}
$$

for every signing.  At $n=8,10,\ldots,20$, all $2^{n+1}$ switching classes
are represented.  At $n=22$, the equivalent $(Q,\alpha)$ quotient is
exhausted.  At $n=24,26,28,30$, fixed-weight necklace generation followed by
dihedral canonicalisation exhausts the same quotient; an independent replay
checks the terminal cursor, chunk completion, represented-space totals,
digests, and optimiser record.

Each non-optimising class has an integral vector whose exact quotient in (1)
is at least $\theta_n$.  Each remaining optimiser is closed by exact
characteristic-polynomial equality.  The exact completion data are:

| $n$ | represented switching classes | exact terminal decisions |
|---:|---:|---:|
| 8 | 512 | 510 Rayleigh certificates and 2 optimiser equalities |
| 10 | 2,048 | 2,046 Rayleigh certificates and 2 optimiser equalities |
| 12 | 8,192 | 8,190 Rayleigh certificates and 2 optimiser equalities |
| 14 | 32,768 | 32,766 Rayleigh certificates and 2 optimiser equalities |
| 16 | 131,072 | 131,070 Rayleigh certificates and 2 optimiser equalities |
| 18 | 524,288 | 524,286 Rayleigh certificates and 2 optimiser equalities |
| 20 | 2,097,152 | 2,097,150 Rayleigh certificates and 2 optimiser equalities |
| 22 | 8,388,608 | 97,467 quotient Rayleigh records and the threshold optimiser |
| 24 | 33,554,432 | 353,811 quotient Rayleigh records and the exact optimiser |
| 26 | 134,217,728 | 1,299,063 quotient Rayleigh records and the exact optimiser |
| 28 | 536,870,912 | 4,810,471 quotient Rayleigh records and the exact optimiser |
| 30 | 2,147,483,648 | 17,929,599 quotient Rayleigh records and the exact optimiser |

The quotient rows at orders 22 through 30 represent the full switching spaces
shown in the middle column.  Every completed order records zero
counterexamples.  Floating eigenvalues do not decide any row.  This proves
(3).

## 3. Order 32

Take all nearest-neighbour signs positive, holonomy $\alpha=+1$, and the
period-eight triangle-flux word

$$
(+,+,-,+,-,-,+,-)^4
$$

with its stated cyclic lift, and let $A_{32}$ be the reconstructed matrix.
Exact Bareiss minors and an independent rational LDL decomposition prove

$$
1561I_{32}-200A_{32}^2\succ0.                          \tag{4}
$$

Hence $\rho(A_{32})^2<1561/200$.  Exact root isolation gives

$$
\frac{1561}{200}
<\frac{11896117236720419}{1523321182060814}
<\theta_{32}.                                         \tag{5}
$$

All comparisons in (5) are integer cross-multiplications plus an exact
root-counting certificate.  Thus order 32 fails.

## 4. Orders 34 through 46

The local finite-state completeness theorem gives

$$
\rho(A)^2\ge\theta_n
\quad\text{for }n\in\{34,36,38,42,44,46\}.             \tag{6}
$$

Here is its logical content.  Every signing yields cyclic data $(Q,\alpha)$.
A length-$(L+1)$ local $Q$-window determines the compression
$M_Q=PA^2P=C_Q^{\mathsf T}C_Q$.  An exact local Rayleigh quotient above a
rational upper endpoint for $\theta_n$ excludes every signing containing that
window.

The surviving windows are edges of a parity-lifted de Bruijn graph.
Length-$n$ closed walks are exactly the globally legal cyclic $Q$-words having
no excluded window.  Dihedral reduction gives respectively
$1,1,3,7,10,10$ canonical $Q$-classes.  Both holonomies are checked, so there
are 64 terminal records.  Exact terminal Rayleigh inequalities or exact
threshold-factor divisibility close every record, and the independently
reconstructed unresolved count is zero.  This proves (6).

At $n=40$, use instead

$$
Q=1000100010001000100010001000100010001000,\qquad
\alpha=-1.                                             \tag{7}
$$

The normal-form reconstruction gives a signed matrix $A_{40}$ for which exact
rational LDL elimination has forty positive pivots in

$$
15541I_{40}-2000A_{40}^2.                              \tag{8}
$$

Therefore $\rho(A_{40})^2<15541/2000$.  By (2),

$$
\frac{15541}{2000}<\frac{63}{8}
=8-\frac{200}{40^2}<\theta_{40},                       \tag{9}
$$

where the first difference is $209/2000$.  Hence order 40 fails, while (6)
closes every other even order from 34 through 46.

## 5. Finite bridge from 48 to 238

For every even $48\le n<240$, choose the deterministic family

$$
\begin{array}{c|c}
n\bmod8&\text{signing family}\\ \hline
0&\text{period-eight repetition}\\
2&\text{one G6 phase slip}\\
4&\text{two balanced G6 phase slips}\\
6&\text{three balanced G6 phase slips}.
\end{array}                                            \tag{10}
$$

The holonomy is $-1$ for $n\equiv0\pmod4$ and $+1$ for
$n\equiv2\pmod4$.  The interval contains exactly 96 even orders.  For each
one, a rational $t_n$ satisfies

$$
t_nI-A_n^2\succ0,\qquad
t_n<8-\frac{200}{n^2}.                                 \tag{11}
$$

An independent checker rebuilds every full matrix and repeats exact sparse
rational LDL in a different elimination order.  By (2) and (11),

$$
\rho(A_n)^2<t_n<8-\frac{200}{n^2}<\theta_n.
$$

Thus all even orders from 48 through 238 fail.

## 6. Analytic tail

Use the same residue families for $n\ge240$.  Residue zero has the uniform
period-eight upper bound $1561/200$.  In residues two, four, and six the
minimum interface separations are

$$
D_2(n)=n,\qquad D_4(n)=n/2,\qquad
D_6(n)=6+4\left\lfloor\frac{2k-3}{3}\right\rfloor
\quad(n=8k+6).                                         \tag{12}
$$

For

$$
R=\left\lfloor\frac{D_r(n)-9}{2}\right\rfloor,
$$

the cyclic tent IMS error is exactly

$$
E(R)=\frac{240R-342}{R(2R^2+1)}\le\frac{120}{R^2}.     \tag{13}
$$

The condition $2(R+4)<D_r(n)$ ensures that each enlarged range-four patch sees
at most one interface.  The local spectral input is the certified global G6
edge; its rank is not used.  Moreover,

$$
E(R)-E(R+1)=
\frac{6(160R^3-102R^2-262R-171)}
{R(R+1)(2R^2+1)(2R^2+4R+3)}>0                         \tag{14}
$$

for $R\ge4$.

At the first four residue endpoints, the exact comparisons are

| $n$ | certified squared spectral cap | $8-200/n^2$ |
|---:|---:|---:|
| 240 | $1561/200$ | $2303/288$ |
| 242 | $257368059342729114019/32519875000000000000$ | $117078/14641$ |
| 244 | $14532080076773342617/1829625000000000000$ | $59511/7442$ |
| 246 | $2591140328128938813/324125000000000000$ | $120982/15129$ |

In every row the middle entry is strictly smaller than the last entry by
integer cross-multiplication.  Along each residue
subsequence, $D_r$ and $R$ do not decrease, (14) makes the error nonincreasing,
and $8-200/n^2$ strictly increases.  The four exact checks therefore propagate
to all later orders.  Equation (2) proves a counterexample at every even
$n\ge240$.

## 7. Exhaustion

The even integers $n\ge8$ are the disjoint union

$$
\begin{gathered}
\{8,10,\ldots,30\},\quad\{32\},\quad
\{34,36,38,42,44,46\},\quad\{40\},\\
\{48,50,\ldots,238\},\quad\{240,242,244,\ldots\}.
\end{gathered}
$$

Sections 2 and 4 prove validity on the first and third sets.  Sections 3
through 6 prove failure on the other four sets.  This proves the theorem.
