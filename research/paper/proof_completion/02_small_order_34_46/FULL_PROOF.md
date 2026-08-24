# Full Proof

## 1. Switching normal form

Index vertices by $\mathbb Z/n\mathbb Z$.  Let $s_i$ be the sign on
$\{i,i+1\}$ and $t_i$ the sign on $\{i,i+2\}$.  Switching along a spanning
path gives

$$
s_0=\cdots=s_{n-2}=1,\qquad
s_{n-1}=\alpha\in\{\pm1\}.                             \tag{1}
$$

Define

$$
\tau_i=t_i s_i s_{i+1},\qquad
Q_i=\tau_i\tau_{i+1}.                                  \tag{2}
$$

The $\tau_i$ are triangle fluxes and are switching invariant.  Multiplying
(2) around the cycle gives

$$
\prod_{i=0}^{n-1}Q_i=1.                                \tag{3}
$$

Conversely, for any cyclic $Q$ satisfying (3), fix $\tau_0=1$ and set

$$
\tau_{i+1}=Q_i\tau_i.                                  \tag{4}
$$

Equation (3) makes this recursion cyclic.  Equations (1) and
$t_i=\tau_i s_i s_{i+1}$ reconstruct a signing for either $\alpha$.

Changing $\tau_0$ to $-1$ changes all distance-two signs.  With
$D=\operatorname{diag}(1,-1,1,-1,\ldots)$, evenness of $n$ gives

$$
A(-\tau,\alpha)=-D A(\tau,\alpha)D.                    \tag{5}
$$

Thus the two $\tau$-lifts are isospectral.  It suffices to enumerate $Q$ and
both holonomies, fixing $\tau_0=1$.

Encode $Q_i=+1$ by $b_i=1$ and $Q_i=-1$ by $b_i=0$.  Since $n$ is even, (3)
is equivalent to

$$
\sum_i b_i\equiv0\pmod2.                               \tag{6}
$$

## 2. Local compression and exclusion

Fix the consecutive support $S=\{0,\ldots,L-1\}$.  In a local tree gauge, for
a vector supported on $S$,

$$
(Av)_i=v_{i-1}+v_{i+1}
      +\tau_{i-2}v_{i-2}+\tau_i v_{i+2},               \tag{7}
$$

with terms outside $S$ omitted.  The output lies in
$\{-2,-1,\ldots,L,L+1\}$.  The needed values
$\tau_{-2},\ldots,\tau_{L-1}$ are determined up to common sign by

$$
Q_{-2},Q_{-1},\ldots,Q_{L-2},                           \tag{8}
$$

a window of length $L+1$.  The common-sign ambiguity is harmless by the local
analogue of (5).

Let $C_W:\mathbb R^L\to\mathbb R^{L+4}$ be the integer matrix in (7) for
window $W$, and set $M_W=C_W^{\mathsf T}C_W$.  Since $C_W$ is the restriction
of $A$ to vectors supported on $S$,

$$
M_W=P_SA^2P_S.                                         \tag{9}
$$

**Lemma 2.1 (local exclusion).**  Suppose
$a_n<\theta_n<b_n$ is a strict rational isolating interval.  If a nonzero
integral vector $v$ satisfies

$$
v^{\mathsf T}M_Wv>b_n v^{\mathsf T}v,                  \tag{10}
$$

then every cyclic signing containing $W$ has
$\rho(A)^2>\theta_n$.

**Proof.**  Extend $v$ by zero outside $S$.  Equation (9) and the Rayleigh
principle give

$$
\rho(A)^2=\lambda_{\max}(A^2)
\ge\frac{v^{\mathsf T}M_Wv}{v^{\mathsf T}v}
>b_n>\theta_n.
$$

This implication does not depend on how the window or vector was found.
$\square$

Use

$$
L_{34}=12,\qquad L_{36}=13,\qquad
L_{38}=L_{42}=L_{44}=L_{46}=14.                        \tag{11}
$$

The certificate evaluates all $2^{L_n+1}$ windows.  Independently, the checker
constructs $M_W$ from (7) and applies exact fraction-free Sylvester tests:

$$
\begin{array}{ll}
a_nI-M_W\succ0 &\Longrightarrow \lambda_{\max}(M_W)<a_n<\theta_n,\\
b_nI-M_W\not\succ0 &\Longrightarrow \lambda_{\max}(M_W)\ge b_n>\theta_n.
\end{array}                                             \tag{12}
$$

There is no unresolved window.  The excluded set in (12) is exactly the set
whose stored integral vectors satisfy (10).

## 3. Exact threshold selection

No decimal chooses the algebraic number $\theta_n$.  If
$c=\cos(2\pi k/n)$, each conjugate has the form

$$
f(c)=2+2c+4c^2.                                        \tag{13}
$$

The function $f$ is increasing on $[-1/4,1]$, while $f(c)\le4$ on
$[-1,-1/4]$.  For the six orders, the value at
$c=\cos(2\pi/n)$ is greater than 7.  Among the cyclotomic conjugates, the
smallest nonzero angular distance from an integer multiple of $2\pi$ is
$2\pi/n$, attained only by the pair $k=\pm1$ and giving the same cosine.
Consequently this value is the unique largest conjugate.
Hence $\theta_n$ is the rightmost real root of its exact minimal polynomial.
Sturm root counts supply strict rational endpoints
$a_n<\theta_n<b_n$ and verify all endpoint signs exactly.

## 4. Parity-lifted de Bruijn completeness

Fix $n$ and write $L=L_n$.  Let $\mathcal W_n$ be the surviving binary words
of length $L+1$.  The directed overlap graph $G_n$ has as vertices all
length-$L$ prefixes and suffixes occurring in $\mathcal W_n$.  A word

$$
w=(b_0,b_1,\ldots,b_L)
$$

is the edge

$$
(b_0,\ldots,b_{L-1})\longrightarrow(b_1,\ldots,b_L),   \tag{14}
$$

labelled by the appended bit $b_L$.  Its parity lift has vertices
$(s,\varepsilon)$ with $\varepsilon\in\mathbb Z/2\mathbb Z$, and the lifted
edge is

$$
(s,\varepsilon)\longrightarrow
(s',\varepsilon+b_L).                                  \tag{15}
$$

**Lemma 4.1 (soundness).**  A length-$n$ closed walk in the parity lift
determines a cyclic $Q$-word satisfying (3), all of whose length-$(L+1)$
windows survive.

**Proof.**  Consecutive edges overlap in $L$ symbols, so their appended labels
form a length-$n$ cyclic word.  Closure of the base state enforces the
wrap-around overlaps.  Closure of the parity state says that the appended-bit
sum is even, which is (6), and hence (3).  $\square$

**Lemma 4.2 (completeness).**  Every cyclic $Q$ satisfying (3) and containing
no excluded window determines a length-$n$ closed walk in the parity lift.

**Proof.**  Read the cyclic word one symbol at a time.  Each consecutive
length-$(L+1)$ window is a surviving edge, consecutive windows overlap in
$L$ symbols, cyclicity closes the base state, and (6) closes parity.
$\square$

The two lemmas establish exact equality between the remaining global
candidates and the parity-even closed walks.  Rotation and reflection preserve
the signed spectrum, so taking one dihedral representative removes duplicates
without losing an orbit.  Holonomy is not a local datum and is not quotiented
away: both $\alpha=-1$ and $\alpha=+1$ remain for every canonical $Q$.
Equations (4)-(5) then show that all relevant signings are covered.

## 5. Terminal records

Independent reconstruction gives:

| $n$ | support | surviving windows | states | rooted even | rooted odd | canonical $Q$ | terminals |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 34 | 12 | 124 | 92 | 1 | 0 | 1 | 2 |
| 36 | 13 | 128 | 92 | 1 | 4 | 1 | 2 |
| 38 | 14 | 184 | 132 | 77 | 38 | 3 | 6 |
| 42 | 14 | 232 | 166 | 337 | 392 | 7 | 14 |
| 44 | 14 | 240 | 171 | 353 | 620 | 10 | 20 |
| 46 | 14 | 240 | 171 | 599 | 690 | 10 | 20 |

Rooted words can be different rotations of one cyclic word.  The canonical
column is the exact dihedral quotient.  Every canonical word has two holonomy
sectors, so the total is

$$
64=2(1+1+3+7+10+10).                                   \tag{16}
$$

Each terminal $(Q,\alpha)$ is discharged in one of two exact ways.

1. When the binary $Q$-code is zero, so $Q$ is the all-negative word, and
   $\alpha=-1$, the minimal polynomial of $\theta_n$ divides
   $\det(xI-A^2)$.  Exact root isolation proves that this factor supplies the
   largest squared eigenvalue with the stored multiplicity.  Hence
   $\rho(A)^2=\theta_n$.
2. Every other terminal has a primitive integral vector $v$ satisfying

   $$
   \frac{\|Av\|^2}{\|v\|^2}>b_n>\theta_n.
   $$

   The vector, numerator, denominator, and strict rational margin are all
   reconstructed.

There are six equality terminals and 58 strict Rayleigh terminals.  Thus all
64 terminal records are resolved and terminal_unresolved=0.  By
Lemma 2.1 and Lemmas 4.1-4.2, every signing is either locally excluded or
represented by a resolved terminal.  Therefore

$$
\rho(A)^2\ge\theta_n
\quad(n=34,36,38,42,44,46).                            \tag{17}
$$

The historical number 84 conflicts with (16), the certificate schema, and
the checker table.  It is a documentation typo, not an additional terminal
set.

## 6. Separate order-40 counterexample

Let

$$
Q=1000100010001000100010001000100010001000,\qquad
\alpha=-1.                                             \tag{18}
$$

The string is read in increasing cyclic index, with 1 meaning $Q_i=+1$.
Starting from $\tau_0=1$, equations (1), (4), and
$t_i=\tau_i s_i s_{i+1}$ construct the integer symmetric matrix $A_{40}$.
The canonical dihedral $Q$-code is 73300775185.

Form

$$
B=15541I_{40}-2000A_{40}^2.                            \tag{19}
$$

Exact rational LDL elimination gives forty strictly positive pivots.  Hence
$B\succ0$ and

$$
\rho(A_{40})^2<\frac{15541}{2000}.                     \tag{20}
$$

The elementary cosine bound gives

$$
\theta_{40}>8-\frac{200}{40^2}=\frac{63}{8},           \tag{21}
$$

and

$$
\frac{63}{8}-\frac{15541}{2000}
=\frac{209}{2000}>0.                                  \tag{22}
$$

Equations (20)-(22) prove $\rho(A_{40})^2<\theta_{40}$.  This full-matrix
upper certificate is logically separate from the six-order lower-certificate
argument.

Equations (17) and (20)-(22) classify every even order from 34 through 46.
