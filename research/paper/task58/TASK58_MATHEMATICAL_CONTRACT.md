# Mathematical Contract for the First-Submission Reframe

Status: `IMMUTABLE_EDITORIAL_CONTRACT`.

This document fixes the mathematical content that may enter the reconstructed
first-submission manuscript. It is a consolidation of the accepted canonical
proof package at checkpoint
`20eb153560df30980ff5ee842246579af40faae5`; it states no new theorem. Later
editorial work may shorten, reorder, or rephrase this material, but it may not
strengthen a conclusion, weaken a hypothesis, change a constant, or merge two
logically distinct inputs without a new proof and review.

## 1. Problem, Operators, and Types

For an even integer $n\ge 8$, let

$$
G_n=C_n(1,2)
$$

be the graph on $\mathbb Z/n\mathbb Z$ whose edges join vertices at cyclic
distance one or two. For an edge signing $\sigma$, let $A_\sigma$ be the real
symmetric signed adjacency matrix and define

$$
H_\sigma=A_\sigma^2,
\qquad
m_n=\min_\sigma \rho(A_\sigma).
$$

The comparison value and its squared form are

$$
\rho_-(n)^2
=4+2\cos\frac{2\pi}{n}+2\cos\frac{4\pi}{n},
\qquad
\theta_n:=\rho_-(n)^2.
$$

The type convention is immutable:

- $m_n$ and $\rho_-(n)$ are unsquared spectral radii;
- $\theta_n$ and every spectral value of $H_\sigma$ are squared quantities;
- $m_n$ is compared with $\rho_-(n)$;
- $m_n^2$ is compared with $\theta_n$.

Since all spectral radii are nonnegative,

$$
m_n<\rho_-(n)
\quad\Longleftrightarrow\quad
m_n^2<\theta_n.
$$

The phrase **failure at order $n$** means precisely this strict inequality.

## 2. Complete Classification and the Two Directions of Equality

The final classification is

$$
m_n<\rho_-(n)
\quad\Longleftrightarrow\quad
n=32,\quad n=40,\quad\text{or}\quad n\ge48,
$$

for every even $n\ge8$. Equivalently, equality holds exactly for

$$
\mathcal V=
\{8,10,12,14,16,18,20,22,24,26,28,30,34,36,38,42,44,46\}.
$$

Equality on $\mathcal V$ has two independent directions.

### 2.1 Candidate-attainment direction

For every even $n\ge8$, define an explicit signing $\sigma_n^-$ by

$$
a_i=1\ (0\le i\le n-2),\qquad a_{n-1}=-1,
$$

on the distance-one edges, and

$$
b_i=(-1)^i\ (0\le i\le n-3),\qquad
b_{n-2}=-1,\qquad b_{n-1}=1,
$$

on the distance-two edges. In Hamilton gauge this signing has

$$
Q_i=-1\quad\text{for every }i,
\qquad \alpha=-1.
$$

Its antiperiodic Fourier fibers are

$$
2\begin{pmatrix}
\cos\vartheta&\cos2\vartheta\\
\cos2\vartheta&-\cos\vartheta
\end{pmatrix},
\qquad
\vartheta=\frac{(2k+1)\pi}{n},
$$

and exact endpoint maximization gives

$$
\rho(A_{\sigma_n^-})^2
=4\cos^2\frac{\pi}{n}+4\cos^2\frac{2\pi}{n}
=\theta_n.
$$

Thus

$$
m_n\le\rho_-(n)
$$

for every even $n\ge8$. This is a purely analytic statement and has no
machine dependency.

### 2.2 Exhaustion direction

At each $n\in\mathcal V$, exact finite exhaustion proves

$$
\rho(A_\sigma)\ge\rho_-(n)
\quad\text{for every signing }\sigma,
$$

and hence $m_n\ge\rho_-(n)$. Only the conjunction of this universal lower
bound with the explicit candidate gives

$$
m_n=\rho_-(n)\qquad(n\in\mathcal V).
$$

At every failing order, a separate explicit signing proves the strict upper
inequality. The candidate $\sigma_n^-$ still exists there, but it is not a
minimizer.

## 3. Switching Coordinates and the Candidate/Reference Distinction

After switching to Hamilton gauge, the step-one cycle carries a residual
holonomy

$$
\alpha\in\{+1,-1\},
$$

the step-two signs form a word $\tau=(\tau_i)$, and the gauge-invariant
quadrilateral flux word is

$$
Q_i=\tau_i\tau_{i+1}.
$$

On the line one may fix $\tau_0=1$ and lift $Q$ by
$\tau_{i+1}=Q_i\tau_i$; the other lift is $-\tau$ and gives a unitarily
equivalent squared operator. On a ring, $Q$ and $\alpha$ together retain the
cyclic parity and holonomy data required by the exact classifiers.

Two periodic objects must never be identified:

1. The **attaining candidate** has $Q_i=-1$ for every $i$ and
   $\alpha=-1$. It realizes $\rho_-(n)$ at every even order.
2. The **reference phase** is the period-eight word

   $$
   \tau_{\mathrm{ref}}=(+,+,-,+,-,-,+,-),
   \qquad
   Q_{\mathrm{ref}}=(+,-,-,-)\ \text{repeated}.
   $$

   It is the crystalline bulk from which phase-slip competitors are built.

For the bilateral operator

$$
(A_\tau u)_i
=u_{i-1}+u_{i+1}+\tau_{i-2}u_{i-2}+\tau_i u_{i+2},
\qquad H_\tau=A_\tau^2,
$$

the squared spectral edge of the reference phase is

$$
\eta=4+\sqrt{10+2\sqrt5}<8.
$$

The edge is attained only at Bloch multiplier $z=1$. The symbol $\eta$
always denotes a squared edge; the corresponding unsquared edge is
$\sqrt\eta$.

## 4. Gaps, Charge, and Two Different Congruence Laws

Let the positive sites of a cyclic $Q$-word be
$d_1,\ldots,d_d$ in cyclic order. Define the positive cyclic gaps and local
charges by

$$
g_j=d_{j+1}-d_j,
\qquad q_j=g_j-4.
$$

Then

$$
\sum_j g_j=n,
\qquad
\sum_j q_j=n-4d.
$$

If $n$ is even and the cyclic $Q$-word admits a $\tau$ lift, then $d$ is
even and

$$
\sum_j q_j\equiv n\pmod8.
$$

This is the **global ring-closure law**. It determines how many charge-two
defects are required in the nonzero even residue classes.

The four translated reference bulks are denoted by
$B_s$, $s\in\mathbb Z/4\mathbb Z$. An oriented interface of charge $q$
changes the translation sector by

$$
\sigma_{\mathrm{sec}}(q)=q\pmod4,
\qquad B_s\longrightarrow B_{s+q}.
$$

Sector shifts add modulo four. This **local sector-shift law** is not the
modulo-eight ring-closure law. In particular, the correct formula is
$q\pmod4$, not $q/2\pmod4$.

The reference gap is $g=4$. The elementary abnormal gap

$$
G6:\qquad g=6,\qquad q=+2,
$$

shifts the reference sector by two modulo four. One, two, and three G6 slips
supply total charges $2$, $4$, and $6$ modulo eight.

## 5. The Algebraic Constant $c_6$

Let

$$
\begin{aligned}
p_6(y)={}&16y^{10}-520y^9+6913y^8-48448y^7+191768y^6\\
&-423904y^5+484528y^4-270464y^3+137856y^2\\
&-19968y+256.
\end{aligned}
$$

The constant $c_6$ is the unique root of $p_6$ in the exact rational
isolating interval

$$
\frac{7905369311620327}{10^{15}}
<c_6<
\frac{7905369311620328}{10^{15}}.
$$

This polynomial and interval, rather than a decimal approximation, are the
definition contract. The constant is a squared spectral value and satisfies

$$
\eta<c_6<8.
$$

## 6. The G6 Essential-Spectrum and Edge Sequence

Let $H_6=A_6^2$ be the bilateral one-interface operator associated with a
single G6 gap. The accepted proof sequence is the following.

1. $H_6$ is a bounded self-adjoint finite-range operator.
2. Cutting beyond the interface core decouples two periodic half-line tails;
   the difference between $H_6$ and the decoupled operator has finite rank.
3. Bloch-Weyl sequences and a half-line Fredholm resolvent parametrix give

   $$
   \sigma_{\mathrm{ess}}(H_6)
   =\sigma(H_L)\cup\sigma(H_R)
   =\sigma(H_{\mathrm{ref}}),
   \qquad
   \sup\sigma_{\mathrm{ess}}(H_6)=\eta.
   $$

4. Consequently, every spectral point $y>\eta$ is an isolated eigenvalue of
   finite multiplicity.
5. Decomposing an $H_6$ eigenvector into the unsquared branches
   $\lambda=\pm\sqrt y$ reduces its tails to the stable and unstable planes
   of the period-eight transfer recurrence. Their intersection criterion is
   necessary and sufficient for a physical $\ell^2$ eigenvector, whose tails
   decay exponentially.
6. Exact stable/unstable matching realizes the algebraic candidate $c_6$;
   exact candidate completeness and physical matching exclude every spectral
   point above it.

Therefore, for either interface orientation and either $\tau$ lift,

$$
\sup\sigma(H_6)=c_6,
\qquad
\dim\ker(H_6-c_6)=2.
$$

In the forward tree gauge, the symmetry

$$
(Ku)_i=(-1)^iu_{9-i}
$$

satisfies

$$
K^2=-I,\qquad KA_6=-A_6K,\qquad KH_6=H_6K.
$$

The two squared modes arise from one simple eigenvalue of $A_6$ at each of
$+\sqrt{c_6}$ and $-\sqrt{c_6}$. Thus $c_6$ is not a simple eigenvalue of
$H_6$.

## 7. Complete Single-Gap Scope

For a positive gap $g$, let $H_g=A_g^2$ be the bilateral single-gap operator
with reference tails. The reference value $g=4$ is not an interface and has

$$
\sup\sigma(H_4)=\eta.
$$

For the unique least-cost abnormal single gap,

$$
\sup\sigma(H_6)=c_6,
\qquad
\dim\ker(H_6-c_6)=2.
$$

For every positive integer $g\notin\{4,6\}$, for both lifts and both
orientations,

$$
\sup\sigma(H_g)>c_6+\frac1{250}.
$$

Hence G6 is the unique minimizer among abnormal positive **single gaps**.
This conclusion does not compare G6 with arbitrary multi-gap or arbitrary
finite-core interfaces.

## 8. Separated G6 Interfaces: IMS and Exact-$2r$

Consider a legal finite ring obtained from the reference phase by inserting
$r\in\{1,2,3\}$ G6 interfaces. Let $D$ be the minimum cyclic site distance
between interface cores, using $D=n$ for one interface.

### 8.1 IMS cap used by the large-order classification

For an integer $R\ge4$ satisfying

$$
2(R+4)<D,
\qquad n>2R+4,
$$

every enlarged localization patch sees either pure reference bulk or one G6
interface. The exact discrete IMS identity and cyclic tent partition give

$$
\rho(A)^2
\le c_6+\frac{240R-342}{R(2R^2+1)}
\le c_6+\frac{120}{R^2}.
$$

This bound controls the full finite-ring spectral top. It uses the value of
the G6 edge, not its rank.

### 8.2 Correct exact-$2r$ strengthening

Under the additional hypothesis $D\ge1040$, set

$$
\ell=\left\lfloor
\frac{\lfloor D/4\rfloor-12}{8}
\right\rfloor.
$$

Then, counted with multiplicity,

$$
\operatorname{rank}
\mathbf 1_{[c_6-1/400,\,c_6+1/400]}(H)=2r,
$$

the complementary compression satisfies

$$
Q_\perp H Q_\perp\le c_6-\frac1{200},
$$

and every cluster level obeys

$$
|\lambda_j-c_6|
<3505r\left(\frac9{25}\right)^\ell,
\qquad 1\le j\le2r.
$$

The Gram, complement, and problem-specific Feshbach spaces have dimensions
$2r$, codimension $2r$, and $2r\times2r$, respectively. No individual
finite-ring simplicity is asserted. The certified scope is only
$r\in\{1,2,3\}$ and $D\ge1040$.

The exact-$2r$ theorem and its sufficient exponential onset
$N_{\mathrm{exp}}=3120$ are valid strengthening results, but neither is a
dependency of the sharp classification onset $48$.

## 9. Residue Words and the One-Sided Asymptotic Statement

For sufficiently large $k$, the nonzero even residue classes use the legal
gap words

$$
\begin{array}{c|l}
n&\text{gap word}\\ \hline
8k+2&[6,4^{\,2k-1}],\\
8k+4&[6,4^{\,k-1},6,4^{\,k-1}],\\
8k+6&[6,4^a,6,4^b,6,4^c],
\end{array}
$$

where

$$
a=\left\lfloor\frac{2k-3}{3}\right\rfloor,
\qquad
b=\left\lfloor\frac{2k-2}{3}\right\rfloor,
\qquad
c=\left\lfloor\frac{2k-1}{3}\right\rfloor.
$$

Their minimum interface separations are

$$
D_2(n)=n,
\qquad
D_4(n)=\frac n2,
\qquad
D_6(n)=6+4\left\lfloor\frac{2k-3}{3}\right\rfloor
\quad(n=8k+6).
$$

The gap sums, parity of the positive-$Q$ count, cyclic $\tau$ lift, total
charge modulo eight, and sector closure modulo four are all part of the
legality proof. The one-, two-, and three-interface counts are fixed while
the separations tend to infinity. Therefore

$$
\limsup_{k\to\infty}m_{8k+s}^2\le c_6,
\qquad s\in\{2,4,6\}.
$$

This is an upper-construction theorem only. It gives no matching lower bound,
no `liminf`, no limit, and no classification of minimizers.

For residue zero, the classification uses the period-eight repetition. In
the deterministic finite and tail families, the Hamilton holonomy is chosen
as $-1$ for $n\equiv0\pmod4$ and $+1$ for $n\equiv2\pmod4$.

## 10. The Analytic Tail and the Sharp Finite Bridge

The universal strict threshold estimate

$$
\theta_n>8-\frac{200}{n^2}
$$

is used to compare the explicit competitors with the conjectured value.

### 10.1 Analytic tail: every even $n\ge240$

Use period-eight repetition in residue zero and the residue words above in
residues two, four, and six. Residue zero has the uniform squared upper bound
$1561/200$. In the other residues choose

$$
R=\left\lfloor\frac{D_s(n)-9}{2}\right\rfloor.
$$

The IMS error

$$
E(R)=\frac{240R-342}{R(2R^2+1)}
$$

is decreasing for $R\ge4$. Exact rational comparisons at the first four
residue endpoints $n=240,242,244,246$, followed by monotonicity in each
residue subsequence, prove a strict counterexample at every even
$n\ge240$. The infinite tail is therefore not established by sampling.

### 10.2 Exact finite bridge: every even $48\le n<240$

For the same deterministic residue families, 96 exact full-matrix rational
$LDL^{\mathsf T}$ certificates produce rational numbers $t_n$ with

$$
t_nI-A_n^2\succ0,
\qquad
t_n<8-\frac{200}{n^2}<\theta_n.
$$

Thus every even order from 48 through 238 fails. This finite bridge, not the
exact-$2r$ theorem, sharpens eventual analytic failure to the continuous
onset

$$
N_\star=48.
$$

Here $N_\star$ is the first order from which every subsequent even order
fails. It is not the first failure, which occurs at $n=32$.

## 11. Exact Role of the Small Orders

The finite classification has four logically different pieces.

1. For every even $8\le n\le30$, exact switching/dihedral exhaustion gives
   the universal lower bound. Together with candidate attainment, this gives
   $m_n=\rho_-(n)$.
2. At $n=32$, an exact positive-definiteness certificate gives a strict
   counterexample. This is the first failure.
3. At

   $$
   n\in\{34,36,38,42,44,46\},
   $$

   local compression and a parity-lifted de Bruijn closure exhaust all
   surviving cyclic $Q$-words and both holonomies. There are exactly 64
   terminal $(Q,\alpha)$ records, six equality terminals, 58 strict Rayleigh
   terminals, and zero unresolved terminals. The universal lower bound and
   candidate attainment again give equality.
4. At $n=40$, an explicit signing satisfies

   $$
   \rho(A_{40})^2<\frac{15541}{2000}
   <\frac{63}{8}<\theta_{40},
   $$

   by exact rational $LDL^{\mathsf T}$ elimination. This is a second isolated
   failure before continuous failure begins at 48.

The finite computations determine the irregular small-order truth pattern
exactly. They do not supply a separate structural mechanism explaining why
the isolated failing orders are numerically 32 and 40.

## 12. Exact Human/Machine Boundary

Every computer-assisted component has the form

$$
\text{mathematical reduction}
\longrightarrow
\text{explicitly finite exact object}
\longrightarrow
\text{independent verification}
\longrightarrow
\text{mathematical consequence}.
$$

The human proof supplies switching invariance, the candidate Fourier
calculation, local compression, soundness and completeness of the finite
state closure, the spectral consequences of positive definiteness, the
essential-spectrum bridge, patch classification, the IMS identity, the
exhaustive order partition, and tail monotonicity. Exact programs perform
finite enumeration, integer quadratic-form checks, algebraic root isolation,
rational Bareiss or $LDL^{\mathsf T}$ elimination, and independent
reconstruction. Floating-point experiments are not accepting proof paths.

The exact-$2r$ cluster, the G6 algebraic edge, the uniform single-gap
separation, and the finite order classifications retain their stated
computer-assisted evidence boundaries. Producer output alone is never
described as independent verification.

## 13. Prohibited Overclaims

The first-submission manuscript must not assert or imply any of the
following.

1. That $m_n$ is directly comparable with the squared quantity $\theta_n$.
2. That a no-counterexample exhaustion proves equality without the explicit
   candidate-attainment direction.
3. That the attaining all-negative-$Q$ candidate is the period-eight
   reference phase.
4. That the modulo-four sector law and modulo-eight ring-closure law are the
   same statement, or that the sector shift is $q/2\pmod4$.
5. That $c_6$ is defined by a decimal, is an unsquared value, or is a simple
   eigenvalue of $H_6$.
6. That one G6 interface contributes one squared mode; the correct local
   rank is two.
7. Any active exact-$r$, codimension-$r$, $r\times r$ problem-specific
   Feshbach, or one-mode-per-interface formulation.
8. That exact-$2r$ is proved beyond $r\in\{1,2,3\}$ or without $D\ge1040$,
   or that its finite-ring cluster levels are individually simple.
9. That single-gap optimality proves universal multi-gap or arbitrary
   finite-core optimality.
10. That the residue construction proves a lower bound, a common `liminf`, a
    limit, or a classification of minimizers.
11. That exact-$2r$ or $N_{\mathrm{exp}}=3120$ is needed for the sharp onset
    $N_\star=48$.
12. That the G6 mechanism alone proves the onset 48. It proves eventual
    failure through the IMS tail; exact finite certification supplies the
    bridge down to 48.
13. That every even $n\ge32$ fails, that 48 is the first failure, or that the
    small-order pattern is monotone.
14. That the classification determines all minimizing signings, computes
    $m_n$ at every failing order, or makes every signing at a failing order a
    counterexample.
15. That bounded periodic-frontier, finite multi-gap, reference-graph, or
    exploratory interaction results are dependencies of the complete
    classification.
16. That a finite producer, numerical eigensolve, plot, sampled scan, or
    unverified certificate is itself a proof.

## 14. Immutable Classification Partition

For editorial and logical checks, the complete domain is the disjoint union

$$
\begin{gathered}
\{8,10,\ldots,30\},\quad \{32\},\quad
\{34,36,38,42,44,46\},\quad \{40\},\\
\{48,50,\ldots,238\},\quad
\{240,242,244,\ldots\}.
\end{gathered}
$$

The first and third sets are equality orders. The other four sets are strict
failure orders. Any abstract, theorem statement, introduction summary,
figure caption, conclusion, or submission metadata that describes the final
classification must agree exactly with this partition.

## 15. Machine-Auditable Canonical Spellings

The following ASCII spellings are exact aliases of statements fixed above.
They are retained so editorial checks cannot silently change types,
multiplicities, scopes, or inequality directions:

```text
theta_n=rho_-(n)^2
failure iff m_n<rho_-(n) iff m_n^2<theta_n
candidate: Q_i=-1, alpha=-1
reference squared edge: eta
ring closure: sum q_j=n mod 8
sector shift: sigma_sec(q)=q mod 4
single-gap separation: sup sigma(H_g)>c6+1/250 for g not in {4,6}
sigma_ess(H_6)=sigma(H_ref)
dim ker(H_6-c_6)=2
separated cluster count: exact 2r
residue conclusion: limsup only
analytic tail: n>=240
finite bridge: 48<=n<240
small-order closure: 64 terminals, zero unresolved
```
