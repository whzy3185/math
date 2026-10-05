---
abstract: |
  We study the adjacency spectral radius of real signings of the cycle
  square $C_n(1,2)$. For the triangle-sign word $(+,+,-,+,-,-,+,-)$
  repeated on $8m$ vertices, we give a self-contained proof of the exact
  radii in the two Hamilton-cycle holonomy sectors. Negative holonomy
  has radius $\sqrt{4+\sqrt{8+2\cos(\pi/m)+\sqrt{26-6\cos(\pi/m)}}}$,
  strictly below the positive-holonomy value
  $\sqrt{4+\sqrt{10+2\sqrt5}}$ for every finite $m$. This disproves the
  unrestricted-minimum conjecture in Suvagiya's September 2026 revision.
  Separately, an explicit signing on every $n\equiv2\pmod8$, $n\ge50$,
  satisfies $\rho^2<198/25$. Its proof combines a rational finite
  entrance certificate with an analytic Riccati contraction and a
  uniform Schur-tail bound. Neither result determines the unrestricted
  minimum over all signings.
date: Research manuscript increment October 2026
title: Holonomy and spectral bounds for signed cycle squares
---

# Introduction

For $n\ge8$, the cycle square $C_n(1,2)$ has vertex set
$\mathbb Z/n\mathbb Z$ and edges $\{i,i+1\}$ and $\{i,i+2\}$. A signing
assigns a value in $\{\pm1\}$ to each edge. Its signed adjacency matrix
$A_\sigma$ is real symmetric, and we write
$$\rho(A_\sigma)=\max\{|\lambda|:\lambda\in\operatorname{spec}(A_\sigma)\},
 \qquad \mu_n=\min_\sigma\rho(A_\sigma).$$ Both spectral edges matter in
this minimization. An upper bound for $\lambda_{\max}$ alone does not
give the required upper bound for $\rho$.

The earlier twisted-optimality conjecture [@Suvagiya2026old] compared
$\mu_n$ with the benchmark
$$\rho_{\mathrm{tw}}(n)^2=4+2\cos\frac{2\pi}{n}+2\cos\frac{4\pi}{n}
 \qquad(n\text{ even},\ n\ge8).
 \label{eq:twisted}$$ That preprint has been withdrawn and incorporated
into [@Suvagiya2026]. The revised Theorem 26 gives a period-eight
signing with radius $$r_*=\sqrt{4+\sqrt{10+2\sqrt5}}
       =2.7936044933\ldots
 \label{eq:rstar}$$ on $8m$ vertices for $m\ge4$, and Conjecture 28
asserts $\mu_{8m}=r_*$ for $m\ge4$. The construction has positive
Hamilton-cycle holonomy; Remark 27 identifies the opposite holonomy as
absent from the reported search. Changing that holonomy while preserving
the triangle signs gives a strict improvement at every finite size.

Fix the word $$t=(1,1,-1,1,-1,-1,1,-1).
 \label{eq:word}$$ For $n=8m$, begin with positive step-one edges and
step-two signs $t_{i\bmod8}$. Let $A_m^+$ be this adjacency matrix. Let
$A_m^-$ be obtained by reversing the signs of exactly three edges:
$$\{n-1,0\},\qquad \{n-2,0\},\qquad \{n-1,1\}.
 \label{eq:seam}$$ These are distinct edges for every $n\ge8$.

::: {#thm:main .theorem}
**Theorem 1**. *For every integer $m\ge1$, define
$$R(s)=\sqrt{4+\sqrt{8+s+\sqrt{26-3s}}}\qquad(-2\le s\le2).$$ Then
$$\rho(A_m^+)=R(2)=r_*,
 \qquad
 \rho(A_m^-)=R\!\left(2\cos\frac{\pi}{m}\right)<r_*.
 \label{eq:main}$$ Moreover, among all signings with the prescribed
labeled triangle signs $t_{i\bmod8}$, the negative-holonomy switching
class is the unique minimizing switching class. In particular,
$$\mu_{8m}\le R\!\left(2\cos\frac{\pi}{m}\right)<r_*
 \qquad(m\ge4),$$ so Conjecture 28 of [@Suvagiya2026] is false as
stated.*
:::

The uniqueness assertion is confined to the prescribed triangle signs.
The theorem supplies no matching lower bound for arbitrary triangle
words, and therefore no classification of unrestricted minimizers. The
dispersion relation and exact finite formula are recorded in the earlier
period-eight research manuscript [@EarlierPeriodEight]. The present
application concerns the revised conjecture and makes explicit why its
proposed endpoint is missed by every finite negative-holonomy grid.

A separate issue is to obtain a short proof for an explicit family
outside the $8$-divisible subsequence. The following statement is
independent of Theorem [1](#thm:main){reference-type="ref"
reference="thm:main"}.

::: {#thm:r2 .theorem}
**Theorem 2**. *Let $k\ge6$, $n=8k+2$, and let $B_n$ be the signed
adjacency matrix with all step-one signs positive and the step-two sign
word $$\tau=t^k\mathbin{\|}(1,-1).$$ Then
$$\frac{198}{25}I_n-B_n^2\succ0,
 \qquad
 \rho(B_n)^2<\frac{198}{25}<\rho_{\mathrm{tw}}(n)^2.
 \label{eq:r2}$$*
:::

Appendix [5](#app:r2){reference-type="ref" reference="app:r2"} gives the
full analytic argument and its finite rational premises. The latter have
been checked both through the block recurrence and independently from
the signed graph by scalar Schur elimination. The theorem is thus a
finite-certificate-assisted analytic result. The signing is inherited
from the earlier residue-two construction; the increment is the analytic
closure and its corrected exact certificates. The proof does not rely on
the historical all-even classification.

The character interpretation of twists is part of established spectral
methods. Luo and Roy [@LuoRoy2026], particularly their Theorems 3.6 and
3.13, study graph spectra over homology-character families and endpoint
attainment. Their setting provides context for holonomy, but does not
give an all-signing minimum for this fixed cycle-square support. The
parity-closed-walk identity of Chen, van Dam, and Bu [@ChenDamBu2024
Theorem 3.1] expresses signed moments averaged over all signings; an
average is likewise not a uniform lower bound for each signing. Our
proofs instead use the explicit fiber polynomial for one triangle word
and exact positive-definiteness certificates for another.

# Switching and finite holonomy

Write $a_i$ for the sign of $\{i,i+1\}$ and $d_i$ for the sign of
$\{i,i+2\}$, with cyclic indices. The triangle sign and Hamilton-cycle
holonomy are
$$\tau_i=a_i a_{i+1}d_i,\qquad \alpha=\prod_{i=0}^{n-1}a_i.$$ Switching
by vertex signs $g_i\in\{\pm1\}$ replaces $A$ by $GAG$, where
$G=\operatorname{diag}(g_i)$. It preserves the spectrum, every $\tau_i$,
and $\alpha$.

::: {#lem:gauge .lemma}
**Lemma 3**. *For prescribed triangle signs
$(\tau_i)_{i\in\mathbb Z/n\mathbb Z}$, there are exactly two switching
classes, indexed by $\alpha\in\{\pm1\}$. Each has a unique
representative with $$a_0=\cdots=a_{n-2}=1,\qquad a_{n-1}=\alpha,
 \qquad d_i=\tau_i a_i a_{i+1}.$$*
:::

::: proof
*Proof.* Set $g_0=1$ and recursively $g_{i+1}=g_i a_i$ for $0\le i<n-1$.
After switching, the first $n-1$ step-one signs are positive. Their
product with the remaining sign is $\alpha$, so that remaining sign is
$\alpha$. The triangle equations force every step-two sign. Conversely,
the displayed signs realize the prescribed data for either choice of
$\alpha$. A switch between two such representatives is constant along
the path $0,1,\ldots,n-1$, hence constant on all vertices and acts
trivially. Finally, distinct values of the switching invariant $\alpha$
cannot be switching equivalent. ◻
:::

For the repeated word [\[eq:word\]](#eq:word){reference-type="eqref"
reference="eq:word"}, this gauge yields exactly $A_m^+$ and $A_m^-$ in
[\[eq:seam\]](#eq:seam){reference-type="eqref" reference="eq:seam"}.
Reversing only the Hamilton edge would change two triangle signs. The
two additional step-two reversals are therefore essential.

Extend $u\in\mathbb C^{8m}$ to the integer line by
$$u_{i+8m}=\alpha u_i.
 \label{eq:extension}$$ Let $t_i=t_{i\bmod8}$. In either seam gauge the
adjacency action is the restriction of
$$(Lu)_i=u_{i-1}+u_{i+1}+t_{i-2}u_{i-2}+t_i u_{i+2}.
 \label{eq:infinite-action}$$ In particular, the signs of all
cut-crossing edges in the finite matrix agree with
[\[eq:extension\]](#eq:extension){reference-type="eqref"
reference="eq:extension"}, including for $m=1$.

::: {#lem:bloch .lemma}
**Lemma 4**. *The complexification of $A_m^\alpha$ is unitarily
equivalent to $$\bigoplus_{z^m=\alpha}H(z),$$ where, in the order
$0,1,\ldots,7$, $$H(z)=\begin{pmatrix}
0&1&1&0&0&0&z^{-1}&z^{-1}\\
1&0&1&1&0&0&0&-z^{-1}\\
1&1&0&1&-1&0&0&0\\
0&1&1&0&1&1&0&0\\
0&0&-1&1&0&1&-1&0\\
0&0&0&1&1&0&1&-1\\
z&0&0&0&-1&1&0&1\\
z&-z&0&0&0&-1&1&0
\end{pmatrix}.
\label{eq:fiber}$$*
:::

::: proof
*Proof.* For each root $z^m=\alpha$ and $v\in\mathbb C^8$, set
$u_{8j+a}=m^{-1/2}z^jv_a$ for $0\le j<m$ and $0\le a<8$. This satisfies
[\[eq:extension\]](#eq:extension){reference-type="eqref"
reference="eq:extension"}. Substitution into
[\[eq:infinite-action\]](#eq:infinite-action){reference-type="eqref"
reference="eq:infinite-action"} gives
[\[eq:fiber\]](#eq:fiber){reference-type="eqref" reference="eq:fiber"}.
For two different allowed phases $z,w$, the ratio $z\overline w$ is a
nontrivial $m$th root of unity, so
$$\sum_{j=0}^{m-1}(z\overline w)^j=0.$$ Thus the $m$ fiber spaces are
mutually orthogonal, each has dimension eight, and together they exhaust
dimension $8m$. The displayed map is unitary. Since $|z|=1$, the fiber
matrix is Hermitian. ◻
:::

# The exact antiperiodic spectrum

::: {#lem:poly .lemma}
**Lemma 5**. *For $|z|=1$ and $s=z+z^{-1}$, $$\begin{aligned}
 \det(xI_8-H(z))=P(x,s)
  &:=x^8-16x^6+80x^4-128x^2+38 \notag\\
  &\quad+s(-2x^4+16x^2-13)+s^2.
 \label{eq:poly}
\end{aligned}$$ Its eight roots, with all signs independently chosen,
are $$\pm\sqrt{4\pm\sqrt{8+s\pm\sqrt{26-3s}}}.
 \label{eq:all-roots}$$ They are all real, nonzero, and distinct for
every $-2\le s\le2$.*
:::

::: proof
*Proof.* Expanding the determinant of
[\[eq:fiber\]](#eq:fiber){reference-type="eqref" reference="eq:fiber"}
as a Laurent polynomial in $z$ gives $$x^8-16x^6+80x^4-128x^2+40
 +(z+z^{-1})(-2x^4+16x^2-13)+(z^2+z^{-2}).$$ Using $z^2+z^{-2}=s^2-2$
proves [\[eq:poly\]](#eq:poly){reference-type="eqref"
reference="eq:poly"}. This is a finite polynomial identity and can also
be checked by the exact symbolic determinant in the accompanying
verifier.

Put $y=x^2$. A translation gives
$$P(x,s)=(y-4)^4-(16+2s)(y-4)^2+s^2+19s+38.
 \label{eq:centered}$$ Solving this as a quadratic in $(y-4)^2$ gives
$$u_\pm(s)=8+s\pm\sqrt{26-3s}.$$ The function $s^2+19s+38$ is increasing
on $[-2,2]$ and has value $4$ at $-2$. Since $8+s>0$, the identity
$$(8+s)^2-(26-3s)=s^2+19s+38\ge4$$ proves $u_->0$. Also $u_+>u_-$, and
$$u_+'(s)=1-\frac3{2\sqrt{26-3s}}>0,
 \qquad u_+(s)\le10+2\sqrt5<16.$$ Consequently
$$0<4-\sqrt{u_+}<4-\sqrt{u_-}
   <4+\sqrt{u_-}<4+\sqrt{u_+}.$$ These are the four distinct positive
roots in $y$. Taking their positive and negative square roots gives
exactly [\[eq:all-roots\]](#eq:all-roots){reference-type="eqref"
reference="eq:all-roots"}. ◻
:::

::: proof
*Proof of Theorem [1](#thm:main){reference-type="ref"
reference="thm:main"}.* Lemma [5](#lem:poly){reference-type="ref"
reference="lem:poly"} implies $$\rho(H(z))=R(s),\qquad s=z+z^{-1}.$$ The
derivative computation in that lemma and strict monotonicity of the
outer square roots show that $R$ increases strictly on $[-2,2]$. For
positive holonomy, the grid $z^m=1$ contains $z=1$, so its maximal value
of $s$ is $2$. For negative holonomy, the grid is
$$z_j=\exp\!\left(\frac{(2j+1)\pi\mathrm i}{m}\right),
 \qquad 0\le j<m,$$ and its maximal value of $s$ is $2\cos(\pi/m)$.
Lemma [4](#lem:bloch){reference-type="ref" reference="lem:bloch"}
therefore proves both equalities in
[\[eq:main\]](#eq:main){reference-type="eqref" reference="eq:main"}. For
every finite $m\ge1$, $\cos(\pi/m)<1$, which proves the strict
inequality. Lemma [3](#lem:gauge){reference-type="ref"
reference="lem:gauge"} shows that these are exactly the two switching
classes for the prescribed triangle signs, so the strict comparison
proves the stated constrained uniqueness. Since $A_m^-$ is an admissible
real signing, the unrestricted upper bound follows. ◻
:::

To identify [\[eq:rstar\]](#eq:rstar){reference-type="eqref"
reference="eq:rstar"} with the algebraic number used in the revised
conjecture, put $$f(x)=x^4-2x^3-6x^2+12x-4.$$ An exact expansion gives
$P(x,2)=f(x)f(-x)$. On $x\ge\sqrt6$, $$f''(x)=12(x^2-x-1)>0,\qquad
 f'(\sqrt6)=12\sqrt6-24>0,\qquad f(\sqrt6)=-4.$$ Hence $f$ has exactly
one root on that ray. For $x>\sqrt6$, $f(-x)-f(x)=4x(x^2-6)>0$. The
largest positive root of $P(x,2)$ is $R(2)>\sqrt6$. It must be a root of
$f$, because $f(-R(2))=0$ would force $f(R(2))<0$ and then a still
larger positive root of $f$, contrary to maximality. Thus $R(2)$ is the
largest real root of $f$.

::: {#cor:asymptotic .corollary}
**Corollary 6**. *The negative-holonomy radii increase strictly to $r_*$
as $m$ increases, and $$r_*-\rho(A_m^-)
 =\frac{\pi^2}{4r_*\sqrt{10+2\sqrt5}}
   \left(1-\frac3{4\sqrt5}\right)m^{-2}+O(m^{-4}).
 \label{eq:asymptotic}$$*
:::

::: proof
*Proof.* The sequence $2\cos(\pi/m)$ increases strictly to $2$, and $R$
is strictly increasing and smooth near $2$. Since
$$2\cos(\pi/m)=2-\pi^2m^{-2}+O(m^{-4}),
 \qquad
 R'(2)=\frac{1-3/(4\sqrt5)}{4r_*\sqrt{10+2\sqrt5}},$$ Taylor's theorem
proves [\[eq:asymptotic\]](#eq:asymptotic){reference-type="eqref"
reference="eq:asymptotic"}. ◻
:::

There is no parity exception: when $m$ is odd, the allowed phase $z=-1$
has $s=-2$ and cannot recover the omitted maximum at $s=2$. At $m=1$ the
single fiber is $H(-1)$, with $\rho(A_1^-)=\sqrt{6+\sqrt2}$.

# An exact certificate at order 32

At $m=4$, Theorem [1](#thm:main){reference-type="ref"
reference="thm:main"} gives $$\rho(A_4^-)
 =\sqrt{4+\sqrt{8+\sqrt2+\sqrt{26-3\sqrt2}}}
 =2.7842697993\ldots.
 \label{eq:n32}$$ The characteristic polynomial computed directly from
the signed $32\times32$ integer matrix is $Q(x)^2$, where
$$\begin{aligned}
 Q(x)={}&x^{16}-32x^{14}+416x^{12}-2816x^{10}+10568x^8\\
       &-21632x^6+22168x^4-9408x^2+1262.
\end{aligned}$$ This agrees with $P(x,\sqrt2)P(x,-\sqrt2)$; each value
of $s$ occurs twice on the antiperiodic four-cell grid.

A separate rational certificate avoids both the fiber calculation and
numerical eigenvalues. Every leading principal minor of each integer
matrix $$279I_{32}-100A_4^-,\qquad 279I_{32}+100A_4^-$$ is strictly
positive. The certificate records all $64$ integer minors; fraction-free
elimination checks every division exactly. Sylvester's criterion yields
$\rho(A_4^-)<279/100$. Meanwhile,
$$f(279/100)=-\frac{6766519}{100000000}<0,
 \qquad f(14/5)=\frac{76}{625}>0.$$ The monotonicity proved above gives
the exact separation $$\rho(A_4^-)<2.79<r_*<2.8.$$ The direct graph
certificate and the all-$m$ analytic proof provide independent ways of
checking the failure at $n=32$.

The next extremal question remains to determine $\mu_{8m}$ and its
minimizing switching classes. The period-eight negative-holonomy family
is an explicit upper bound, not a proof of optimality. Establishing
optimality would require a lower bound over arbitrary triangle words,
including nonperiodic words. Similarly,
Theorem [2](#thm:r2){reference-type="ref" reference="thm:r2"} is an
existence theorem for one signing on each order $8k+2$. Combining such
witnesses does not certify a complete truth set for the twisted
benchmark without independent lower bounds at the complementary orders.

# A uniform residue-two Schur bound {#app:r2}

We prove Theorem [2](#thm:r2){reference-type="ref" reference="thm:r2"}.
In this appendix $n=8k+2=4\ell+2$, where $\ell=2k$ is even and $k\ge6$.
The letter $\ell$ counts four-vertex blocks and is distinct from the
cell count $m$ in the main text. Put $$M_n=\frac{198}{25}I_n-B_n^2.$$
All matrix inequalities in this appendix concern real symmetric
matrices; $X\succ0$ means positive definite. The norm
$\left\lVert\cdot\right\rVert_2$ is the Euclidean operator norm, and
$\left\lVert\cdot\right\rVert_F$ is the Frobenius norm.

## The exact block recurrence

Partition the vertices into $$V_0=\{0,1\},\qquad
 V_j=\{2+4(j-1),\ldots,5+4(j-1)\}\quad(1\le j\le\ell).$$ The diagonal
block on each $V_j$, $j\ge1$, is $$D=\begin{pmatrix}
 98/25&0&-1&0\\0&98/25&0&-1\\-1&0&98/25&0\\0&-1&0&98/25
 \end{pmatrix}.$$ The block $M_n[V_j,V_{j+1}]$ equals $E_+$ for odd $j$
and $E_-$ for even $j$, where
$$E_+=\begin{pmatrix}-1&0&0&0\\0&1&0&0\\-1&2&1&0\\2&-1&0&-1\end{pmatrix},
 \qquad
 E_-=\begin{pmatrix}-1&0&0&0\\0&1&0&0\\-1&-2&1&0\\-2&-1&0&-1\end{pmatrix}.$$
The exceptional blocks are $$\begin{gathered}
 G_0=M_n[V_0,V_0]=(98/25)I_2,\qquad H_0=D,\\
 R_0=M_n[V_0,V_1]=\begin{pmatrix}-1&-2&1&0\\-2&-1&0&-1\end{pmatrix},\\
 C_0=M_n[V_0,V_\ell]=\begin{pmatrix}-1&0&-1&0\\0&-1&0&-1\end{pmatrix},
 \qquad
 W_0=M_n[V_1,V_\ell]=\begin{pmatrix}0&0&-1&0\\0&0&0&1\\0&0&0&0\\0&0&0&0\end{pmatrix}.
\end{gathered}$$ All other nonadjacent bulk blocks vanish. To verify
these identities at all lengths, the only nonzero entries of $B_n^2$ on
the forward cyclic diagonals, apart from transposes, are
$$\begin{aligned}
 (B_n^2)_{i,i}&=4,&
 (B_n^2)_{i,i+1}&=\tau_{i-1}+\tau_i,&
 (B_n^2)_{i,i+2}&=1,\\
 (B_n^2)_{i,i+3}&=\tau_i+\tau_{i+1},&
 (B_n^2)_{i,i+4}&=\tau_i\tau_{i+2}.&&
\end{aligned}$$ They follow by enumerating the possible two-edge walks.
Since $n\ge50$, these cyclic offsets do not collide. Substitution of
$t^k\|(1,-1)$ gives the displayed blocks without a length-dependent
assumption.

Let $E_j=E_+$ for even $j$ and $E_j=E_-$ for odd $j$. Set $X_0=D$.
Before closing the right boundary, elimination of the current
four-vertex pivot gives the length-independent recurrence
$$\begin{aligned}
 X_{j+1}&=D-E_j^TX_j^{-1}E_j,&
 R_{j+1}&=-R_jX_j^{-1}E_j,\notag\\
 W_{j+1}&=-E_j^TX_j^{-1}W_j,&
 G_{j+1}&=G_j-R_jX_j^{-1}R_j^T,\label{eq:recurrence}\\
 H_{j+1}&=H_j-W_j^TX_j^{-1}W_j,&
 C_{j+1}&=C_j-R_jX_j^{-1}W_j.\notag
\end{aligned}$$ The terminal elimination index is $p=\ell-2$, which is
even. At that step only, the coupling to the retained last block becomes
$W_p+E_+$. Thus the normalized six-dimensional core is $$S_\ell=
 \begin{pmatrix}
 G_p-R_pX_p^{-1}R_p^T&C_p-R_pX_p^{-1}(W_p+E_+)\\
 *&H_p-(W_p+E_+)^TX_p^{-1}(W_p+E_+)
 \end{pmatrix}.
 \label{eq:core}$$ Here $*$ denotes the transpose block. Repeated Schur
congruence proves that $M_n\succ0$ if all eliminated pivots and $S_\ell$
are positive. The subscript of $S_\ell$ is a block count: in particular,
$S_{26}$ corresponds to graph order $106$.

## Finite exact premises

Define $F_\pm(X)=D-E_\pm^TX^{-1}E_\pm$ and $\Phi=F_-\circ F_+$. Put
$Z=\Phi^{12}(D)=X_{24}$, $Y=F_+(Z)$, and $L_Z=Z^{-1}E_+Y^{-1}E_-$. Use
the rational matrices $$\begin{aligned}
 P&=\frac1{10000}\begin{pmatrix}
10766&87&19&974\\87&12664&148&-2418\\19&148&10093&-25\\974&-2418&-25&14009
\end{pmatrix},\\
 Q&=\frac1{10000}\begin{pmatrix}
11503&614&990&-1101\\614&10470&15&113\\990&15&12299&-2632\\-1101&113&-2632&13260
\end{pmatrix}.
\end{aligned}$$ Set $r=10^{-10}$. The following finite inequalities are
the complete certificate premises used below:

1.  $X_0,\ldots,X_{24}\succ0$ and $Z,Y\succ I_4/2$;

2.  $(9/10)I_4\prec P,Q\prec2I_4$;

3.  $L_Z^TPL_Z\prec(2/5)P$ and $L_ZQL_Z^T\prec(2/5)Q$;

4.  $\left\lVert\Phi(Z)-Z\right\rVert_F<r/40$;

5.  $R_{24}QR_{24}^T\prec10^{-10}I_2$ and
    $W_{24}^TQW_{24}\prec10^{-10}I_4$;

6.  $S_{26}\succ(1/50)I_6$;

7.  $S_\ell\succ0$ for $\ell=12,14,16,18,20,22,24$.

They have been verified using exact rational arithmetic. For clarity,
their verification requires no limiting or approximate matrix: all
matrices are specified by the displayed rational initial data and a
finite number of recurrence steps. Positive definiteness is checked by
successive scalar Schur pivots. For a symmetric matrix $K$, start with
$K^{(0)}=K$; at each step require $d_j=K^{(j)}_{11}>0$ and replace the
remaining block by
$K^{(j+1)}=K^{(j)}_{22}-K^{(j)}_{21}(d_j)^{-1}K^{(j)}_{12}$. All
resulting scalars are rational, so each test is exact. The residual test
in item 4 is the rational inequality
$$\sum_{a,b}(\Phi(Z)-Z)_{ab}^2<(r/40)^2.$$ The accompanying certificate
records the matrices and the positive pivots. An independent replay
constructs $B_{106}$ from its edges, eliminates $96$ scalar vertices to
recover the entrance data, and verifies items 1--5 without generating
that entrance by the block recurrence. Direct scalar elimination from
the graphs also verifies the seven base orders $50,58,66,74,82,90,98$
and the normalized seed at $106$.

## A local Riccati contraction

For symmetric $U$, define the order-unit norm
$$|U|_P=\inf\{a\ge0:-aP\preceq U\preceq aP\}
      =\left\lVert P^{-1/2}UP^{-1/2}\right\rVert_2.$$ Consider the
closed ball $\mathcal K=\{X=X^T:|X-Z|_P\le r\}$. Since $P\prec2I$,
$$\left\lVert X-Z\right\rVert_2\le2r=:e.$$ The certified lower bound
$Z\succ I/2$ gives $X\succ I/3$ and
$\left\lVert X^{-1}\right\rVert_2\le3$. The inverse identity yields
$$\left\lVert X^{-1}-Z^{-1}\right\rVert_2\le6e.$$ Both $E_\pm$ have
squared Frobenius norm $14$. Writing $Y_X=F_+(X)$, we obtain
$$\left\lVert Y_X-Y\right\rVert_2\le84e<1/6,
 \qquad Y_X\succ I/3,
 \qquad \left\lVert Y_X^{-1}-Y^{-1}\right\rVert_2\le504e.$$ Define
$L(X)=X^{-1}E_+Y_X^{-1}E_-$. Splitting its difference from $L_Z$ into
two terms gives $$\left\lVert L(X)-L_Z\right\rVert_2
 \le14(6\cdot3+2\cdot504)e=14364e.
 \label{eq:Lperturb}$$ For the two transfer norms
$$\left\lVert L\right\rVert_{P,\mathrm{col}}=\left\lVert P^{1/2}LP^{-1/2}\right\rVert_2,
 \qquad
 \left\lVert L\right\rVert_{Q,\mathrm{row}}=\left\lVert Q^{-1/2}LQ^{1/2}\right\rVert_2,$$
conversion from the Euclidean norm costs at most $\sqrt{20/9}<3/2$.
Therefore the perturbation in either norm is less than
$21546e=43092r<10^{-4}$. The certified bounds at $Z$, together with
$\sqrt{2/5}+10^{-4}<2/3$, imply throughout $\mathcal K$ that
$$L(X)^TPL(X)\prec\frac49P,
 \qquad L(X)QL(X)^T\prec\frac49Q.
 \label{eq:dual-contractions}$$ Direct differentiation gives
$D\Phi_X[U]=L(X)^TUL(X)$. If $-aP\preceq U\preceq aP$, the first
inequality in
[\[eq:dual-contractions\]](#eq:dual-contractions){reference-type="eqref"
reference="eq:dual-contractions"} bounds this derivative in $|\cdot|_P$
by $4a/9$. Integrating along a line segment in the convex ball proves
that $\Phi$ is $4/9$-Lipschitz there.

The residual premise gives $|\Phi(Z)-Z|_P<(10/9)(r/40)=r/36$.
Consequently $$|\Phi(X)-Z|_P<r/36+(4/9)r=(17/36)r<r.$$ The ball is
invariant. Banach's fixed-point theorem supplies a unique
$X_*\in\mathcal K$ with $\Phi(X_*)=X_*$. The actual even trajectory
starts at $Z$, so, with $\theta=4/9$,
$$\left\lVert X_{24+2h}-X_*\right\rVert_2\le4r\theta^h
 \qquad(h\ge0).
 \label{eq:pivot-decay}$$ The constant $4r$ follows already from the
diameter of the ball. All these even pivots and their intermediate odd
partners exceed $I/3$. Together with the finite entrance this proves
positivity of every pivot needed at any length.

## Response decay

Two consecutive updates in
[\[eq:recurrence\]](#eq:recurrence){reference-type="eqref"
reference="eq:recurrence"} act by $R\mapsto RL(X)$ and
$W\mapsto L(X)^TW$. For these two orientations, respectively, use
$$\alpha(R)=\left\lVert RQ^{1/2}\right\rVert_2,
 \qquad \beta(W)=\left\lVert Q^{1/2}W\right\rVert_2.$$ The second
inequality in
[\[eq:dual-contractions\]](#eq:dual-contractions){reference-type="eqref"
reference="eq:dual-contractions"} contracts both quantities by $q=2/3$.
Hence the entrance premises imply $$\begin{aligned}
 R_{24+2h}QR_{24+2h}^T&\prec10^{-10}q^{2h}I_2,\\
 W_{24+2h}^TQW_{24+2h}&\prec10^{-10}q^{2h}I_4.
\end{aligned}$$ Since $Q\succ(9/10)I$, it follows that
$$\left\lVert R_{24+2h}\right\rVert_2,\ \left\lVert W_{24+2h}\right\rVert_2<a q^h,
 \qquad a=1/30000.
 \label{eq:even-response}$$ Each one-step transfer has norm at most
$3\sqrt{14}<12$. Thus both members of the $h$th pair obey
$$\left\lVert R_j\right\rVert_2,\ \left\lVert W_j\right\rVert_2\le bq^h,
 \qquad b=12a=1/2500,
 \quad j\in\{24+2h,25+2h\}.
 \label{eq:pair-response}$$ The row orientation $LQL^T$ is needed here.
A bound on $L^TQL$ alone would not justify these response estimates.

## The limiting core and its uniform tail

Use the actual infinite trajectory, not a trajectory with constant
pivots, to define the absolutely convergent series $$\begin{aligned}
 G_\infty&=G_0-\sum_{j\ge0}R_jX_j^{-1}R_j^T,\\
 H_\infty&=H_0-\sum_{j\ge0}W_j^TX_j^{-1}W_j,\\
 C_\infty&=C_0-\sum_{j\ge0}R_jX_j^{-1}W_j.
\end{aligned}$$ Convergence follows from
[\[eq:pair-response\]](#eq:pair-response){reference-type="eqref"
reference="eq:pair-response"} and
$\left\lVert X_j^{-1}\right\rVert_2\le3$ after $j=24$. Set
$$S_\infty=\begin{pmatrix}
 G_\infty&C_\infty\\
 C_\infty^T&H_\infty-E_+^TX_*^{-1}E_+
 \end{pmatrix}.$$ Take even $\ell\ge26$ and write its terminal index as
$p=\ell-2=24+2h$. Each of the three Schur-series suffixes after index
$p$ is bounded in norm by $$T_h=\frac{6b^2q^{2h}}{1-q^2}.
 \label{eq:Th}$$ Indeed, every increment in the $j$th pair has norm at
most $3b^2q^{2j}$, and there are two increments per pair. The bound in
[\[eq:Th\]](#eq:Th){reference-type="eqref" reference="eq:Th"} harmlessly
includes the term at $p$ as well.

The terminal linear terms from
[\[eq:core\]](#eq:core){reference-type="eqref" reference="eq:core"}
satisfy $$\begin{aligned}
 \left\lVert R_pX_p^{-1}E_+\right\rVert_2&\le12a q^h,\\
 \left\lVert W_p^TX_p^{-1}E_++E_+^TX_p^{-1}W_p\right\rVert_2&\le24a q^h.
\end{aligned}$$ The inverse identity and
[\[eq:pivot-decay\]](#eq:pivot-decay){reference-type="eqref"
reference="eq:pivot-decay"}, with $\delta=4r$, give
$$\left\lVert X_p^{-1}-X_*^{-1}\right\rVert_2\le9\delta\theta^h,
 \qquad
 \left\lVert E_+^T(X_p^{-1}-X_*^{-1})E_+\right\rVert_2
 \le144\delta\theta^h.$$ For the differences of the three blocks in
$S_\ell-S_\infty$ we therefore have $$\begin{aligned}
 \left\lVert\Delta G\right\rVert_2&\le T_h,\\
 \left\lVert\Delta C\right\rVert_2&\le T_h+12a q^h,\\
 \left\lVert\Delta H\right\rVert_2&\le T_h+24a q^h+144\delta\theta^h.
\end{aligned}$$ The block estimate
$$\left\lVert\begin{pmatrix}U&V\\V^T&Z\end{pmatrix}\right\rVert_2
 \le\left\lVert U\right\rVert_2+2\left\lVert V\right\rVert_2+\left\lVert Z\right\rVert_2$$
now gives the explicit uniform tail bound $$\begin{aligned}
 \left\lVert S_\ell-S_\infty\right\rVert_2
 &\le4T_h+48a q^h+144\delta\theta^h\notag\\
 &\le\frac{251089}{156250000}<\frac1{500}.
 \label{eq:tail}
\end{aligned}$$ The rational middle expression is the value of this
majorant at $h=0$; each geometric factor decreases for $h\ge0$. Because
the series were defined along the actual trajectory, the common initial
terms cancel exactly. Only the terminal pure-pivot term requires the
inverse-limit comparison above.

## Completion of the spectral estimate

The exact seed $S_{26}\succ I_6/50$ and two applications of
[\[eq:tail\]](#eq:tail){reference-type="eqref" reference="eq:tail"}
imply, for every even $\ell\ge26$,
$$\left\lVert S_\ell-S_{26}\right\rVert_2<2/500=1/250,
 \qquad S_\ell\succ\left(\frac1{50}-\frac1{250}\right)I_6
                  =\frac2{125}I_6.$$ Both tail errors are required: the
seed is a finite core, not the limiting core. The remaining even block
counts $12\le\ell<26$ are exactly the seven certified bases. Thus every
core and every eliminated pivot is positive. Schur congruence proves
$M_n\succ0$, and the spectral theorem then gives $\rho(B_n)^2<198/25$.

This use of Schur congruence asserts positivity only. The lower bound
$2/125$ for the reduced core is not a lower bound for the least
Euclidean eigenvalue of the original matrix $M_n$. Finally,
$\cos x>1-x^2/2$ for $x>0$ and $\pi^2<10$ yield
$$\rho_{\mathrm{tw}}(n)^2>8-\frac{20\pi^2}{n^2}
          >8-\frac{200}{n^2}\ge\frac{198}{25}
 \qquad(n\ge50).$$ This completes the proof of
Theorem [2](#thm:r2){reference-type="ref" reference="thm:r2"}.

#### Reproducibility.

The accompanying source package includes
`certificates/analytic/verify_r2_certificate.py` and
`r2_exact_certificate.json`, together with the independent
`replay_direct_graph_seed.py` and `replay_local_from_direct_graph.py`
under `certificates/audit/`. For the separate antiperiodic check, the
script `verify_antiperiodic_counterexample.py` under
`certificates/new_conjecture/` constructs the graph, checks the symbolic
identities, and verifies all recorded integer minors. The package README
lists the exact execution commands and dependencies.

::: thebibliography
9 V. Suvagiya, *Signed circulants at the Ramanujan bound*,
arXiv:2607.18334v1, 19 July 2026; withdrawn in version 2, 22 September
2026, and merged into [@Suvagiya2026].
<https://arxiv.org/abs/2607.18334>.

V. Suvagiya, *Parity families and signed spectra: kernel averaging,
near-Ramanujan bounds, and exact circulant models*, arXiv:2607.17343v2,
22 September 2026, Theorem 26, Remark 27, and Conjecture 28.
<https://arxiv.org/abs/2607.17343v2>.

Y. Luo and A. Roy, *Homological spectral graph theory and weighted cycle
counting*, arXiv:2403.01550v4, 4 August 2026.
<https://arxiv.org/abs/2403.01550v4>.

L. Chen, E. R. van Dam, and C. Bu, Spectra of power hypergraphs and
signed graphs via parity-closed walks, *Journal of Combinatorial Theory,
Series A* **207** (2024), 105909.
<https://doi.org/10.1016/j.jcta.2024.105909>.

*The exact period-eight phase*, Section 4 of the earlier period-eight
research manuscript, frozen repository source at commit
`085ea698475b7b32e0ae57457ec903a922248f69`. [Archived source
section](https://github.com/whzy3185/math/blob/085ea698475b7b32e0ae57457ec903a922248f69/research/paper_strengthening/manuscript_period8_jgt/sections_en/04_period8_exact.tex).
:::
