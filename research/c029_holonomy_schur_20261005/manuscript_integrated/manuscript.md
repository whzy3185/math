---
abstract: |
  We give a direct Schur-complement proof of spectral bounds for
  explicit signings of cycle squares. A rationally certified
  four-dimensional Riccati recurrence produces a common six-dimensional
  limiting boundary matrix. Concatenating any number of prescribed
  cells, with unequal lengths and either Hamilton holonomy, preserves a
  squared spectral-radius bound of $7.92$ when every cell has length at
  least $106$, and $7.90537$ when every cell has length at least $202$.
  A degree-two estimate keeps the error independent of the number of
  cells. The one-cell family satisfies the sharper bound at every
  admissible size, and its supremum lies in an interval of width
  $10^{-6}$. Exact finite bases complete explicit competitors to the
  twisted signing at orders $32,40$ and every even order at least $48$.
  This recovers the previously known witness range through a common
  analytic mechanism. We also present the exact period-eight holonomy
  calculation and its application to the revised global-optimality
  conjecture. Unrestricted minima and minimizing signings are not
  determined.
date: Integrated research manuscript October 2026
title: Uniform Schur bounds and holonomy in signed cycle squares
---

# Introduction and main results

For $N\ge8$, the cycle square $C_N(1,2)$ has vertex set
$\mathbb Z/N\mathbb Z$ and edges $\{i,i+1\}$ and $\{i,i+2\}$. A real
signing assigns $\pm1$ to each edge. For its symmetric adjacency matrix
$A$, write $$\rho(A)=\max\{|\lambda|:\lambda\in\operatorname{spec}(A)\},
 \qquad \mu_N=\min_\sigma\rho(A_\sigma).$$ The minimization controls
both spectral edges. The benchmark in the original twisted-optimality
question [@Suvagiya2026old] is
$$\rho_{\mathrm{tw}}(N)^2=4+2\cos\frac{2\pi}{N}+2\cos\frac{4\pi}{N}
 \qquad(N\text{ even},\ N\ge8).
 \label{eq:twisted}$$

Our main result is a uniform bound for a family whose local structure is
fixed but whose cell lengths and cell count are arbitrary. Set
$$t=(1,1,-1,1,-1,-1,1,-1),\qquad
 w_j=t^j\mathbin{\|}(1,-1),\qquad h_j=8j+2\quad(j\ge1).
 \label{eq:word}$$ Here $\|$ denotes concatenation. For a length-$N$
triangle-sign word $\tau$ and $\alpha\in\{\pm1\}$, define
$A_N(\tau,\alpha)$ by the edge signs
$$a_i=\begin{cases}1&i<N-1,\\\alpha&i=N-1,\end{cases}
 \quad
 \sigma\{i,i+1\}=a_i,\qquad
 \sigma\{i,i+2\}=\tau_i a_i a_{i+1},
 \label{eq:gauge-definition}$$ with cyclic indices. The triangle signs
are $\tau_i$, and the Hamilton-cycle sign product is $\alpha$. Define
the two rational caps $$c_0=\frac{198}{25}=7.92,\qquad
 c_1=\frac{790537}{100000}=7.90537.$$

::: {#thm:cells .theorem}
**Theorem 1** (Unequal-cell bound). *Let $r\ge1$,
$j_0,\ldots,j_{r-1}\ge1$, and $\tau=w_{j_0}\|\cdots\|w_{j_{r-1}}$, of
total length $N$. For either holonomy $\alpha$, $$\begin{aligned}
 \min_i h_{j_i}\ge106&\quad\Longrightarrow\quad
       \rho(A_N(\tau,\alpha))^2<c_0,\label{eq:cell-cap0}\\
 \min_i h_{j_i}\ge202&\quad\Longrightarrow\quad
       \rho(A_N(\tau,\alpha))^2<c_1.\label{eq:cell-cap1}
\end{aligned}$$ The constants do not depend on $r$, and the lengths need
not be equal.*
:::

The allowed cell words are part of the hypotheses. The theorem does not
cover arbitrary signings or arbitrary arrangements of local defects. Its
proof retains six coordinates at each cell boundary and eliminates the
four-site interior chains exactly. A common positive limiting core and a
quadratic-form estimate with two chain incidences per boundary control
the resulting $6r$-dimensional cyclic matrix. The error is independent
of $r$; no count of localized eigenmodes is assumed.

The single-cell family permits a sharper finite completion.

::: {#thm:one-cell .theorem}
**Theorem 2** (One-cell bound). *For every $k\ge1$,
$$\rho(A_{8k+2}(w_k,+1))^2<c_1.$$ Moreover, $$\frac{7905369}{1000000}
 <\sup_{k\ge1}\rho(A_{8k+2}(w_k,+1))^2
 \le\frac{790537}{100000}.
 \label{eq:supremum}$$*
:::

The interval in [\[eq:supremum\]](#eq:supremum){reference-type="eqref"
reference="eq:supremum"} has width $10^{-6}$. Its upper endpoint is
non-strict; no convergence, monotonicity, or exact supremum is asserted.

To cover each nonzero even residue modulo eight, put
$$W_{k,r}=\mathop{\|}_{a=0}^{r-1}w_{\lfloor(k+a)/r\rfloor},
 \qquad r\in\{1,2,3\},\ k\ge6.$$ The cell parameters sum to $k$, so the
word has length $8k+2r$.

::: {#thm:witnesses .theorem}
**Theorem 3** (Explicit finite competitors). *For $r\in\{1,2,3\}$ and
$k\ge6$, the matrix $$B_{k,r}=A_{8k+2r}(W_{k,r},(-1)^{r+1})$$ satisfies
$$\rho(B_{k,r})^2<c_0<\rho_{\mathrm{tw}}(8k+2r)^2.
 \label{eq:nonzero-witnesses}$$ For $r=1$ the stronger cap $c_1$ holds.
Together with the period-eight family, these constructions prove
$$\mu_N<\rho_{\mathrm{tw}}(N)
 \quad\text{for }N\in\{32,40\}\cup\{N\ge48:N\text{ even}\}.$$*
:::

This witness range already occurs in the earlier Target A project
[@EarlierTargetA]. The contribution here is a common transparent
analytic mechanism, sharper quantitative bounds, and a finite completion
with directly specified signings. For odd $k$ in residue four, and for
$3\nmid k$ in residue six, our placements need not be the older
balanced-gap placements. Their finite certificates are recomputed for
the words above. We do not reprove the universal lower bounds at
complementary smaller orders, determine $\mu_N$ when the twisted signing
fails, or classify minimizing signings.

The literature target has also changed. The original preprint
[@Suvagiya2026old] was withdrawn and merged into [@Suvagiya2026]. Its
revised Theorem 26 supplies the positive-holonomy period-eight value
$$\eta_*=4+\sqrt{10+2\sqrt5},\qquad r_*=\sqrt{\eta_*},
 \label{eq:rstar}$$ for $N=8m$, $m\ge4$, while Conjecture 28 proposes
$\mu_{8m}=r_*$ throughout that range. The exact negative-holonomy
formula from the earlier project manuscript [@EarlierPeriodEight] is
strictly smaller at every finite size. We provide its full proof and
apply it to that revised claim. This application is distinct from a
priority claim for the inherited formula.

The use of holonomy belongs to the established character approach to
spectral graph theory; Luo and Roy [@LuoRoy2026 Theorems 3.6 and 3.13]
study character families and endpoint attainment. Those results do not
supply the fixed-support minimum here. Likewise, signed moments averaged
over all signings, as in Chen, van Dam, and Bu [@ChenDamBu2024 Theorem
3.1], are not pointwise lower bounds for every signing. Our estimates
instead arise from an explicit fiber calculation and exact
positive-definiteness tests after a uniform analytic reduction. The
latter proofs are finite-certificate-assisted, with independent exact
replays; their finite checks are specified in
Section [7](#sec:finite){reference-type="ref" reference="sec:finite"}.

# Switching and finite holonomy

Write $a_i$ for the sign of $\{i,i+1\}$ and $d_i$ for the sign of
$\{i,i+2\}$, with cyclic indices. The triangle sign and Hamilton-cycle
holonomy are
$$\tau_i=a_i a_{i+1}d_i,\qquad \alpha=\prod_{i=0}^{n-1}a_i.$$ Switching
by vertex signs $g_i\in\{\pm1\}$ replaces $A$ by $GAG$, where
$G=\operatorname{diag}(g_i)$. It preserves the spectrum, every $\tau_i$,
and $\alpha$.

::: {#lem:gauge .lemma}
**Lemma 4**. *For prescribed triangle signs
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

For the repeated word $t^m$ on $N=8m$ vertices, write
$A_m^\pm=A_{8m}(t^m,\pm1)$. The positive representative has all step-one
signs positive and step-two signs $t_{i\bmod8}$. The negative
representative reverses exactly the three distinct edges
$$\{N-1,0\},\qquad\{N-2,0\},\qquad\{N-1,1\}.
 \label{eq:seam}$$ Reversing only the Hamilton edge would change two
triangle signs. The two additional step-two reversals are therefore
essential.

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
**Lemma 5**. *The complexification of $A_m^\alpha$ is unitarily
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

Let $A_m^\pm=A_{8m}(t^m,\pm1)$ and set
$$R(s)=\sqrt{4+\sqrt{8+s+\sqrt{26-3s}}}\qquad(-2\le s\le2).$$

::: {#thm:period8 .theorem}
**Theorem 6**. *For every $m\ge1$, $$\rho(A_m^+)^2=\eta_*,
 \qquad \rho(A_m^-)=R\!\left(2\cos\frac\pi m\right)<\sqrt{\eta_*}.
 \label{eq:main}$$ Among signings with the prescribed labeled triangle
signs $t^m$, the negative-holonomy class is the unique minimizing
switching class.*
:::

The exact formula is recorded in the earlier period-eight manuscript
[@EarlierPeriodEight]; we include its proof to keep the present argument
self-contained.

::: {#lem:poly .lemma}
**Lemma 7**. *For $|z|=1$ and $s=z+z^{-1}$, $$\begin{aligned}
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
*Proof of Theorem [6](#thm:period8){reference-type="ref"
reference="thm:period8"}.* Lemma [7](#lem:poly){reference-type="ref"
reference="lem:poly"} implies $$\rho(H(z))=R(s),\qquad s=z+z^{-1}.$$ The
derivative computation in that lemma and strict monotonicity of the
outer square roots show that $R$ increases strictly on $[-2,2]$. For
positive holonomy, the grid $z^m=1$ contains $z=1$, so its maximal value
of $s$ is $2$. For negative holonomy, the grid is
$$z_j=\exp\!\left(\frac{(2j+1)\pi\mathrm i}{m}\right),
 \qquad 0\le j<m,$$ and its maximal value of $s$ is $2\cos(\pi/m)$.
Lemma [5](#lem:bloch){reference-type="ref" reference="lem:bloch"}
therefore proves both equalities in
[\[eq:main\]](#eq:main){reference-type="eqref" reference="eq:main"}. For
every finite $m\ge1$, $\cos(\pi/m)<1$, which proves the strict
inequality. Lemma [4](#lem:gauge){reference-type="ref"
reference="lem:gauge"} shows that these are exactly the two switching
classes for the prescribed triangle signs, so the strict comparison
proves the stated constrained uniqueness. Since $A_m^-$ is an admissible
real signing, the same value is an upper bound for the unrestricted
minimum. ◻
:::

To identify $\sqrt{\eta_*}$ with the algebraic number used in the
revised conjecture, put $$f(x)=x^4-2x^3-6x^2+12x-4.$$ An exact expansion
gives $P(x,2)=f(x)f(-x)$. On $x\ge\sqrt6$, $$f''(x)=12(x^2-x-1)>0,\qquad
 f'(\sqrt6)=12\sqrt6-24>0,\qquad f(\sqrt6)=-4.$$ Hence $f$ has exactly
one root on that ray. For $x>\sqrt6$, $f(-x)-f(x)=4x(x^2-6)>0$. The
largest positive root of $P(x,2)$ is $R(2)>\sqrt6$. It must be a root of
$f$, because $f(-R(2))=0$ would force $f(R(2))<0$ and then a still
larger positive root of $f$, contrary to maximality. Thus $R(2)$ is the
largest real root of $f$.

::: {#cor:asymptotic .corollary}
**Corollary 8**. *The negative-holonomy radii increase strictly to $r_*$
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

::: {#cor:conjecture .corollary}
**Corollary 9**. *For every $m\ge4$, $\mu_{8m}<\sqrt{\eta_*}$. Thus
Conjecture 28 of [@Suvagiya2026] is false as stated.*
:::

::: proof
*Proof.* The matrix $A_m^-$ is a real signing of the same graph, and
Theorem [6](#thm:period8){reference-type="ref" reference="thm:period8"}
gives its strictly smaller radius. As shown above, $\sqrt{\eta_*}$ is
the largest real root of the quartic used in that conjecture. The
minimum in the conjecture ranges over both holonomies. ◻
:::

At $m=4$, the exact value is
$$\rho(A_4^-)=\sqrt{4+\sqrt{8+\sqrt2+\sqrt{26-3\sqrt2}}}
             =2.7842697993\ldots.$$ A separate full-graph integer
certificate checks that all leading principal minors of
$279I_{32}\pm100A_4^-$ are positive. Sylvester's criterion gives
$\rho(A_4^-)<2.79$. Exact evaluations
$$f(279/100)=-6766519/10^8<0,\qquad f(14/5)=76/625>0$$ and the
monotonicity of $f$ above show $2.79<\sqrt{\eta_*}<2.8$. This finite
check is independent of the all-$m$ fiber proof.

# A common four-site chain and six-coordinate boundary {#sec:chain}

The remaining proofs use squared adjacency matrices. For a cap $c$,
positive definiteness of $cI-A^2$ is equivalent to $\rho(A)^2<c$.
Throughout, $\left\lVert\cdot\right\rVert_2$ is the Euclidean operator
norm and $\left\lVert\cdot\right\rVert_F$ is the Frobenius norm. We
first derive one block system, then certify it at $c=c_0$ and $c=c_1$.
No estimate at the second energy is inferred by simply reusing a
certificate at the first.

For the one-cell word $w_j$, put $h=8j+2=4\ell+2$, where $\ell=2j$.
Initially take positive holonomy and $h\ge18$. Partition the vertices
into $$V_0=\{0,1\},\qquad
 V_s=\{2+4(s-1),\ldots,5+4(s-1)\}\quad(1\le s\le\ell).$$ The normalized
matrix $M_h(c)=cI-A_h(w_j,+1)^2$ has bulk diagonal and successive
coupling blocks $$\begin{gathered}
 D_c=\begin{pmatrix}
 c-4&0&-1&0\\0&c-4&0&-1\\-1&0&c-4&0\\0&-1&0&c-4
 \end{pmatrix},\label{eq:D}\\
 E_+=\begin{pmatrix}-1&0&0&0\\0&1&0&0\\-1&2&1&0\\2&-1&0&-1\end{pmatrix},
 \qquad
 E_-=\begin{pmatrix}-1&0&0&0\\0&1&0&0\\-1&-2&1&0\\-2&-1&0&-1\end{pmatrix}.
 \label{eq:E}
\end{gathered}$$ Here $M_h[V_s,V_{s+1}]=E_+$ for odd $s$ and $E_-$ for
even $s$. The boundary blocks are $$\begin{gathered}
 G_0=(c-4)I_2,\qquad H_0=D_c,\qquad
 R_0=\begin{pmatrix}-1&-2&1&0\\-2&-1&0&-1\end{pmatrix},\notag\\
 C_0=\begin{pmatrix}-1&0&-1&0\\0&-1&0&-1\end{pmatrix},\qquad
 W_0=\begin{pmatrix}0&0&-1&0\\0&0&0&1\\0&0&0&0\\0&0&0&0\end{pmatrix}.
 \label{eq:boundary-data}
\end{gathered}$$ Specifically, $R_0=M_h[V_0,V_1]$,
$C_0=M_h[V_0,V_\ell]$, and $W_0=M_h[V_1,V_\ell]$. All other nonadjacent
bulk blocks vanish. These identities follow from the complete two-walk
expansion $$\begin{aligned}
 (A^2)_{i,i}&=4,& (A^2)_{i,i+1}&=\tau_{i-1}+\tau_i,&
 (A^2)_{i,i+2}&=1,\notag\\
 (A^2)_{i,i+3}&=\tau_i+\tau_{i+1},&
 (A^2)_{i,i+4}&=\tau_i\tau_{i+2},&&
 \label{eq:two-walks}
\end{aligned}$$ their transposes, and zero entries at all other cyclic
offsets. At $h\ge18$ these offsets and the stated block locations do not
collide. The exceptional order $h=10$ will be checked directly.

Use zero-based elimination indices: let $X_0=D_c$, with $E_a=E_+$ for
even $a$ and $E_a=E_-$ for odd $a$. Eliminating the current four-site
pivot gives the length-independent open recurrence $$\begin{aligned}
 X_{a+1}&=D_c-E_a^TX_a^{-1}E_a,&
 R_{a+1}&=-R_aX_a^{-1}E_a,\notag\\
 W_{a+1}&=-E_a^TX_a^{-1}W_a,&
 G_{a+1}&=G_a-R_aX_a^{-1}R_a^T,\label{eq:recurrence}\\
 H_{a+1}&=H_a-W_a^TX_a^{-1}W_a,&
 C_{a+1}&=C_a-R_aX_a^{-1}W_a.\notag
\end{aligned}$$ The final pivot has index $p=\ell-2$, which is even. At
that step the right coupling is $W_p+E_+$, so the retained
six-coordinate core is $$S_\ell(c)=\begin{pmatrix}
 G_p-R_pX_p^{-1}R_p^T&C_p-R_pX_p^{-1}(W_p+E_+)\\
 *&H_p-(W_p+E_+)^TX_p^{-1}(W_p+E_+)
 \end{pmatrix}.
 \label{eq:single-core}$$ The lower-left block is the transpose of the
upper-right block. Repeated Schur congruence proves $M_h(c)\succ0$ once
every eliminated pivot and this core are positive. The subscript $\ell$
counts four-site blocks, not vertices.

## The two finite rational certificates

Write $F_\pm(X)=D_c-E_\pm^TX^{-1}E_\pm$ and $\Phi=F_-\circ F_+$. At the
even entrance $J$ set $$Z=X_J=\Phi^{J/2}(D_c),\qquad Y=F_+(Z),\qquad
 T_Z=Z^{-1}E_+Y^{-1}E_-.$$ Both energies use the fixed rational weights
$$\begin{aligned}
 P&=\frac1{10000}\begin{pmatrix}
10766&87&19&974\\87&12664&148&-2418\\19&148&10093&-25\\974&-2418&-25&14009
\end{pmatrix},\notag\\
 Q&=\frac1{10000}\begin{pmatrix}
11503&614&990&-1101\\614&10470&15&113\\990&15&12299&-2632\\-1101&113&-2632&13260
\end{pmatrix}.
\label{eq:weights}
\end{aligned}$$ The numerical constants are exact rational numbers:

::: center
  Quantity                             $c=c_0$        $c=c_1$
  ---------------------------------- ------------ ----------------
  Entrance $J$                           $24$           $48$
  Riccati radius $\delta$             $10^{-10}$     $10^{-18}$
  Response square bound $\zeta$       $10^{-10}$     $10^{-20}$
  Center transfer factor $\kappa$       $2/5$          $1/2$
  Response contraction $q$              $2/3$          $3/4$
  Riccati contraction $\theta=q^2$      $4/9$          $9/16$
  Even response bound $a$             $1/30000$    $1/9000000000$
  Pair response bound $b=12a$          $1/2500$    $1/750000000$
  Seed margin $\gamma$                  $1/50$       $10^{-6}$
  Tail tolerance $\epsilon$            $1/500$       $10^{-8}$
  Seed graph order $4(J+2)+2$           $106$          $202$
:::

::: {#lem:finite-premises .lemma}
**Lemma 10** (Exact finite premises). *For each column of the table, the
rational recurrence satisfies:*

1.  *$X_0,\ldots,X_J\succ0$ and $Z,Y\succ I_4/2$;*

2.  *$(9/10)I_4\prec P,Q\prec2I_4$;*

3.  *$T_Z^TPT_Z\prec\kappa P$ and $T_ZQT_Z^T\prec\kappa Q$;*

4.  *$\left\lVert\Phi(Z)-Z\right\rVert_F<\delta/40$;*

5.  *$R_JQR_J^T\prec\zeta I_2$ and $W_J^TQW_J\prec\zeta I_4$;*

6.  *$S_{J+2}(c)\succ\gamma I_6$.*
:::

::: proof
*Proof.* All the matrices are specified by the rational initial data and
at most $J+2$ recurrence steps. The accompanying exact verifiers
evaluate them over $\mathbb Q$. For each positive-definiteness assertion
they compute scalar Schur pivots: if a symmetric matrix is partitioned
as $\left(\begin{smallmatrix}d&v^T\\v&K\end{smallmatrix}\right)$, they
require $d>0$ and recurse on $K-vv^T/d$. Every pivot is a strictly
positive rational number. The residual check is the exact comparison
$$\sum_{u,v}(\Phi(Z)-Z)_{uv}^2<(\delta/40)^2.$$ The verifiers
reconstruct the responses, and the certificates store the exact centers,
seeds and positive pivots; the $c_1$ certificate also stores both
entrance responses. An independent implementation constructs the full
signed graph and uses scalar elimination, without generating the
entrance through the four-site recurrence. It recovers the entrance
after $4J$ scalar pivots, subtracts the physical terminal $E_+$ coupling
to isolate $W_J$, and checks the same inequalities. Both energies pass
these rational checks. The implementation and certificate locations are
given in Section [8](#sec:verification){reference-type="ref"
reference="sec:verification"}. ◻
:::

This lemma is the finite computational part of the uniform argument. No
floating eigenvalue or limiting-matrix approximation is used in its
acceptance tests. The seed margins refer to the normalized
six-coordinate cores in
[\[eq:single-core\]](#eq:single-core){reference-type="eqref"
reference="eq:single-core"}.

# Uniform Riccati and boundary estimates {#sec:uniform}

We give one analytic proof valid for either parameter column above. For
a real symmetric matrix $U$, use the order-unit norm
$$|U|_P=\inf\{d\ge0:-dP\preceq U\preceq dP\}
      =\left\lVert P^{-1/2}UP^{-1/2}\right\rVert_2.$$ On the closed ball
$\mathcal K=\{X=X^T:|X-Z|_P\le\delta\}$, $P\prec2I$ gives
$\left\lVert X-Z\right\rVert_2\le2\delta=:e$. The center bounds imply
$X\succ I/3$, $\left\lVert X^{-1}\right\rVert_2\le3$, and
$$\left\lVert X^{-1}-Z^{-1}\right\rVert_2\le6e.$$ Since
$\left\lVert E_\pm\right\rVert_F^2=14$, putting $Y_X=F_+(X)$ yields
$$\left\lVert Y_X-Y\right\rVert_2\le84e<1/6,\qquad
 Y_X\succ I/3,\qquad
 \left\lVert Y_X^{-1}-Y^{-1}\right\rVert_2\le504e.$$ For
$T(X)=X^{-1}E_+Y_X^{-1}E_-$, a two-term product difference gives
$$\left\lVert T(X)-T_Z\right\rVert_2\le14(6\cdot3+2\cdot504)e=14364e.
 \label{eq:Tperturb}$$ The norm conversion factor from the Euclidean
norm to either
$$\left\lVert T\right\rVert_{P,\mathrm{col}}=\left\lVert P^{1/2}TP^{-1/2}\right\rVert_2,
 \qquad
 \left\lVert T\right\rVert_{Q,\mathrm{row}}=\left\lVert Q^{-1/2}TQ^{1/2}\right\rVert_2$$
is at most $\sqrt{20/9}<3/2$. Thus the perturbation in either norm is
less than $43092\delta<10^{-4}$. Both parameter columns satisfy
$\sqrt\kappa+10^{-4}<q$, and hence throughout the ball
$$T(X)^TPT(X)\prec q^2P,\qquad T(X)QT(X)^T\prec q^2Q.
 \label{eq:dual-contractions}$$

The derivative is $D\Phi_X[U]=T(X)^TUT(X)$. The first inequality in
[\[eq:dual-contractions\]](#eq:dual-contractions){reference-type="eqref"
reference="eq:dual-contractions"} therefore bounds its order-unit norm
by $\theta|U|_P$, where $\theta=q^2$. Integration along a line segment
in $\mathcal K$ proves the same Lipschitz bound for $\Phi$. The center
residual has order-unit norm below $\delta/36$. Both columns satisfy
$1/36+\theta<1$, so $$|\Phi(X)-Z|_P<\delta/36+\theta\delta<\delta.$$
Banach's theorem gives a fixed point $X_*\in\mathcal K$. The actual even
orbit starts at $Z$, whence
$$\left\lVert X_{J+2s}-X_*\right\rVert_2\le4\delta\theta^s\qquad(s\ge0).
 \label{eq:pivot-decay}$$ All these pivots and their intermediate odd
partners exceed $I/3$. Together with
Lemma [10](#lem:finite-premises){reference-type="ref"
reference="lem:finite-premises"}, this proves positivity of every pivot
at either energy.

## Response decay and the limiting core

Two steps in [\[eq:recurrence\]](#eq:recurrence){reference-type="eqref"
reference="eq:recurrence"} send $R$ to $RT(X)$ and $W$ to $T(X)^TW$.
Their natural norms are
$$\left\lVert RQ^{1/2}\right\rVert_2,\qquad \left\lVert Q^{1/2}W\right\rVert_2.$$
The second inequality in
[\[eq:dual-contractions\]](#eq:dual-contractions){reference-type="eqref"
reference="eq:dual-contractions"} contracts both by $q$. The table
satisfies $a^2>(10/9)\zeta$; the response premises and $Q\succ(9/10)I$
give
$$\left\lVert R_{J+2s}\right\rVert_2,\ \left\lVert W_{J+2s}\right\rVert_2<a q^s.
 \label{eq:even-response}$$ A one-step transfer has norm at most
$3\sqrt{14}<12$. Consequently
$$\left\lVert R_a\right\rVert_2,\ \left\lVert W_a\right\rVert_2\le bq^s
 \quad\text{for }a\in\{J+2s,J+2s+1\}.
 \label{eq:pair-response}$$ The orientation $TQT^T$ is essential; a
column-only estimate would not establish these two response bounds.

Define absolutely convergent series along the actual open trajectory:
$$\begin{aligned}
 G_\infty&=G_0-\sum_{a\ge0}R_aX_a^{-1}R_a^T,\\
 H_\infty&=H_0-\sum_{a\ge0}W_a^TX_a^{-1}W_a,\\
 C_\infty&=C_0-\sum_{a\ge0}R_aX_a^{-1}W_a.
\end{aligned}$$ Convergence follows from
[\[eq:pair-response\]](#eq:pair-response){reference-type="eqref"
reference="eq:pair-response"} and
$\left\lVert X_a^{-1}\right\rVert_2\le3$ after the entrance. Set
$$S_\infty=\begin{pmatrix}
 G_\infty&C_\infty\\C_\infty^T&H_\infty-E_+^TX_*^{-1}E_+
 \end{pmatrix}.
 \label{eq:Sinfty}$$ There is no replacement of every pivot in the sums
by $X_*$. Common initial terms therefore cancel exactly when a finite
core is compared with this limit.

::: {#prop:tail .proposition}
**Proposition 11** (Complete one-cell tail). *For even $\ell\ge J+2$,
write $p=\ell-2=J+2s$. Then $$\begin{aligned}
 \left\lVert S_\ell(c)-S_\infty\right\rVert_2
 &\le B_s,\notag\\
 B_s&=\frac{24b^2q^{2s}}{1-q^2}+48aq^s+576\delta\theta^s
      <\epsilon.\label{eq:Btail}
\end{aligned}$$ Furthermore $S_\infty\succ(\gamma-\epsilon)I_6$ and
$S_\ell(c)\succ(\gamma-2\epsilon)I_6$.*
:::

::: proof
*Proof.* Each quadratic or mixed Schur suffix after $p$ is bounded by
$$T_s=\frac{6b^2q^{2s}}{1-q^2}.$$ There are two single-block increments
per pair, each at most $3b^2q^{2v}$; including the term at $p$ only
enlarges the bound. The terminal corrections in
[\[eq:single-core\]](#eq:single-core){reference-type="eqref"
reference="eq:single-core"} have norms at most
$$\left\lVert R_pX_p^{-1}E_+\right\rVert_2\le12a q^s,
 \qquad
 \left\lVert W_p^TX_p^{-1}E_++E_+^TX_p^{-1}W_p\right\rVert_2\le24a q^s.$$
The inverse identity and
[\[eq:pivot-decay\]](#eq:pivot-decay){reference-type="eqref"
reference="eq:pivot-decay"} give
$$\left\lVert X_p^{-1}-X_*^{-1}\right\rVert_2\le36\delta\theta^s,
 \qquad
 \left\lVert E_+^T(X_p^{-1}-X_*^{-1})E_+\right\rVert_2\le576\delta\theta^s.$$
Thus the errors in the $G,C,H$ blocks are bounded respectively by $T_s$,
$T_s+12aq^s$, and $T_s+24aq^s+576\delta\theta^s$. Using
$$\left\lVert\begin{pmatrix}U&V\\V^*&Z\end{pmatrix}\right\rVert_2
 \le\left\lVert U\right\rVert_2+2\left\lVert V\right\rVert_2+\left\lVert Z\right\rVert_2$$
proves [\[eq:Btail\]](#eq:Btail){reference-type="eqref"
reference="eq:Btail"}. Its right side decreases with $s$, and exact
rational arithmetic gives $$B_0=
 \begin{cases}
 251089/156250000<1/500,&c=c_0,\\
 583333407/109375000000000000<10^{-8},&c=c_1.
 \end{cases}
 \label{eq:B0}$$ Compare the certified seed $S_{J+2}(c)\succ\gamma I_6$
to the limit, and then the limit to any other finite core. These are two
separate errors, giving the two stated lower bounds. ◻
:::

The resulting core margins are $2/125$ and $49/50000000$, respectively.
Schur congruence transfers positivity to the full matrix; it does not
transfer these numbers as Euclidean eigenvalue gaps of the full matrix.

## Every unit complex phase {#sec:phase}

For $h=8j+2$ and $|z|=1$, let $A_h(z)$ be the Hermitian cell operator
induced by $$(Au)_i=u_{i-1}+u_{i+1}+\tau_{i-2}u_{i-2}+\tau_i u_{i+2},
 \qquad u_{i+h}=zu_i,\qquad \tau=w_j\text{ periodically extended}.$$ At
$h\ge18$, the two wrap blocks of $cI-A_h(z)^2$ are $C_0(z)=\bar z C_0$
and $W_0(z)=\bar z W_0$; all other initial blocks are unchanged. This
follows directly from the two-walk paths, each wrap path crossing the
cut once in the negative direction. The Hermitian Schur recurrence gives
$$X_p(z)=X_p,\ R_p(z)=R_p,\ G_p(z)=G_p,\ H_p(z)=H_p,
 \quad C_p(z)=\bar z C_p,\ W_p(z)=\bar z W_p.$$ Invariance of $H_p$ uses
conjugate transpose and $|z|=1$. The physical terminal coupling remains
$E=E_+$, so it is added to $\bar zW_p$, not multiplied by the phase. Put
$$\begin{aligned}
 g_p&=G_p-R_pX_p^{-1}R_p^T,&
 c_p&=C_p-R_pX_p^{-1}W_p,\\
 h_p&=H_p-W_p^TX_p^{-1}W_p-E^TX_p^{-1}E,&
 u_p&=R_pX_p^{-1}E,\qquad v_p=W_p^TX_p^{-1}E.
\end{aligned}$$ The exact terminal core and its unitary conjugate are
$$\begin{aligned}
 S_\ell(z)&=\begin{pmatrix}
 g_p&\bar z c_p-u_p\\ *&h_p-zv_p-\bar z v_p^T
 \end{pmatrix},\notag\\
 U_z^*S_\ell(z)U_z&=\begin{pmatrix}
 g_p&c_p-zu_p\\ *&h_p-zv_p-\bar z v_p^T
 \end{pmatrix},\quad U_z=\operatorname{diag}(I_2,zI_4).
 \label{eq:phase-core}
\end{aligned}$$ The lower-left blocks are conjugate transposes. The
limit of [\[eq:phase-core\]](#eq:phase-core){reference-type="eqref"
reference="eq:phase-core"} is the same $S_\infty$ for every phase.
Moreover, all the finite tail estimates in
Proposition [11](#prop:tail){reference-type="ref" reference="prop:tail"}
are unchanged by the factors $z$, giving a uniform bound before taking
any limit.

::: {#cor:phase .corollary}
**Corollary 12**. *For every $|z|=1$,
$$h\ge106\Longrightarrow\rho(A_h(z))^2<c_0,
 \qquad h\ge202\Longrightarrow\rho(A_h(z))^2<c_1,$$ where
$h\equiv2\pmod8$ and the word is $w_{(h-2)/8}$. For any number of
identical cells and either holonomy, the corresponding finite signing
obeys the same applicable bound.*
:::

::: proof
*Proof.* The uniformly positive pivots and phase core imply
$cI-A_h(z)^2\succ0$. For $r$ identical cells with total holonomy
$\alpha$, the maps $$(F_zv)_{ah+s}=r^{-1/2}z^a v_s\qquad(z^r=\alpha)$$
give an orthogonal decomposition of the full graph into the $A_h(z)$
fibers, by the same finite geometric-sum argument as
Lemma [5](#lem:bloch){reference-type="ref" reference="lem:bloch"}. The
seam identity is precisely $z^r=\alpha$. Every fiber is bounded, so the
full radius is bounded. ◻
:::

# Unequal cells and a bound independent of their number {#sec:cells}

The Fourier decomposition above requires identical cells. We now
eliminate the interiors of unequal cells directly, retaining every
boundary degree of freedom. This proves
Theorem [1](#thm:cells){reference-type="ref" reference="thm:cells"}.

Let the cell lengths be $h_i=8j_i+2$, $0\le i<r$, and write $b_0=0$,
$b_i=\sum_{a<i}h_a$, with all vertices interpreted modulo $N$. For each
cell retain the ordered six-tuple
$$K_i=(b_i,b_i+1,b_i-4,b_i-3,b_i-2,b_i-1)
 \label{eq:retained}$$ and eliminate its interior
$$I_i=\{b_i+2,\ldots,b_i+h_i-5\}.$$ Thus $K_i$ contains the head pair of
cell $i$ and the tail four vertices of cell $i-1$. The $K_i$ and $I_i$
partition the vertices for every legal $h_i\ge10$.

The range-four expansion
[\[eq:two-walks\]](#eq:two-walks){reference-type="eqref"
reference="eq:two-walks"} shows that different interiors do not couple:
adjacent interiors have closest separation seven. Distinct retained
intervals also have no direct coupling, since their closest separation
across cell $i$ is $h_i-5\ge5$. Each interior is a chain of $2j_i-1$
four-site blocks; it couples only to $K_i$ at its left and the tail-four
slot of $K_{i+1}$ at its right. The common initial and terminal triangle
signs make these endpoint coefficients independent of the cell length.

In terms of
[\[eq:boundary-data\]](#eq:boundary-data){reference-type="eqref"
reference="eq:boundary-data"}, the intrinsic retained block and left and
right chain couplings are
$$\mathcal B=\begin{pmatrix}G_0&C_0\\C_0^T&D_c\end{pmatrix},
 \qquad U_0=\begin{pmatrix}R_0\\W_0^T\end{pmatrix},
 \qquad V=\begin{pmatrix}0_{4\times2}&E_+\end{pmatrix}.
 \label{eq:assembly-data}$$ The global seam initially multiplies $C_0$
and the lower part of $U_0$ in $K_0$ by $\alpha$. Conjugating the
tail-four coordinates of $K_0$ by $\alpha$ restores
[\[eq:assembly-data\]](#eq:assembly-data){reference-type="eqref"
reference="eq:assembly-data"} and moves the seam sign to the last
chain's terminal coupling. Hence the canonical terminal factors are
$$\omega_i=1\quad(i<r-1),\qquad\omega_{r-1}=\alpha.$$ This is an
explicit permutation and diagonal sign conjugacy.

## The additive cyclic Schur identity

Use the same open pivot sequence as before and put
$$U_{a+1}=-U_aX_a^{-1}E_a.$$
Equation [\[eq:recurrence\]](#eq:recurrence){reference-type="eqref"
reference="eq:recurrence"} gives $U_a=(R_a^T,W_a)^T$, that is, the
vertical stack of $R_a$ and $W_a^T$. For the final interior index
$p_i=2j_i-2$, define $$\mathcal L_i=\sum_{a=0}^{p_i}U_aX_a^{-1}U_a^T,
 \qquad \mathcal P_i=V^TX_{p_i}^{-1}V,
 \qquad F_i=U_{p_i}X_{p_i}^{-1}V.
 \label{eq:endpoint-data}$$ Let $\iota_i:\mathbb R^6\to\mathbb R^{6r}$
be the coordinate embedding at $K_i$, with the index $i+1$ understood
cyclically.

::: {#lem:assembly .lemma}
**Lemma 13** (Exact cell assembly). *When the interior pivots are
positive, their elimination gives the retained matrix $$\begin{aligned}
 \mathcal S={}&I_r\otimes\mathcal B
 -\sum_i\iota_i\mathcal L_i\iota_i^T
 -\sum_i\iota_{i+1}\mathcal P_i\iota_{i+1}^T\notag\\
 &-\sum_i\omega_i\bigl(
 \iota_iF_i\iota_{i+1}^T+\iota_{i+1}F_i^T\iota_i^T\bigr).
 \label{eq:assembly}
\end{aligned}$$ Every contribution is added, including coincident block
locations when $r=1$ or $r=2$.*
:::

::: proof
*Proof.* At the current pivot of a chain, the left coupling is $U_a$, so
the Schur complement subtracts $U_aX_a^{-1}U_a^T$ from its retained left
endpoint and propagates the response as $-U_aX_a^{-1}E_a$. Only the
final pivot also sees the right endpoint, through $\omega_iV$. Its two
self-energy terms and cross term are precisely
[\[eq:endpoint-data\]](#eq:endpoint-data){reference-type="eqref"
reference="eq:endpoint-data"}. Distinct interiors do not couple, so
their Schur contributions add. For $r=2$, two different chains connect
the same pair of retained cores; both cross contributions remain in
[\[eq:assembly\]](#eq:assembly){reference-type="eqref"
reference="eq:assembly"}. For $r=1$, the combined coupling at the final
pivot is $U_{p_0}+\omega_0V^T$. Expanding its quadratic Schur correction
gives $\mathcal P_0$ and the loop contribution $\omega_0(F_0+F_0^T)$ in
addition to $\mathcal L_0$. Thus the same additive formula also covers
the one-cell case. ◻
:::

## The common limit and the degree-two estimate

At either certified cap, suppose $p_i=J+2s_i$ with $s_i\ge0$, and put
$s=\min_i s_i$. Define $$\mathcal L_\infty=\sum_{a\ge0}U_aX_a^{-1}U_a^T,
 \qquad \mathcal P_\infty=V^TX_*^{-1}V.$$ By the stacked form of $U_a$,
the matrix $\mathcal B-\mathcal L_\infty-\mathcal P_\infty$ equals
exactly $S_\infty$ from
[\[eq:Sinfty\]](#eq:Sinfty){reference-type="eqref"
reference="eq:Sinfty"}. Its positivity has already been proved; there is
no new limiting-core assumption.

The separate response bounds give
$$\left\lVert U_{J+2v}\right\rVert_2\le\sqrt2\,a q^v,
 \qquad \left\lVert U_{J+2v+1}\right\rVert_2\le\sqrt2\,b q^v.$$ Counting
both increments in every pair therefore yields
$$\left\lVert\mathcal L_\infty-\mathcal L_i\right\rVert_2
 \le\frac{12b^2q^{2s_i}}{1-q^2}.
 \label{eq:Ltail}$$ The right side harmlessly includes the final
included term as well as the actual suffix. The inverse identity and
$\left\lVert V\right\rVert_2\le\sqrt{14}$ give
$$\left\lVert\mathcal P_i-\mathcal P_\infty\right\rVert_2
 \le576\delta\theta^{s_i}.
 \label{eq:Ptail}$$ Finally,
$$\left\lVert F_i\right\rVert_2\le3\sqrt{28}\,a q^{s_i}<16a q^{s_i}.
 \label{eq:Ftail}$$

The diagonal part of
[\[eq:assembly\]](#eq:assembly){reference-type="eqref"
reference="eq:assembly"}, relative to $I_r\otimes S_\infty$, combines
one outgoing error from [\[eq:Ltail\]](#eq:Ltail){reference-type="eqref"
reference="eq:Ltail"} with one incoming error from
[\[eq:Ptail\]](#eq:Ptail){reference-type="eqref" reference="eq:Ptail"}.
For the cross terms, take arbitrary $v_i\in\mathbb R^6$. Their quadratic
form has absolute value at most $$\begin{aligned}
 \sum_i2\left\lVert F_i\right\rVert_2\left\lVert v_i\right\rVert_2\left\lVert v_{i+1}\right\rVert_2
 &\le\sum_i\left\lVert F_i\right\rVert_2(\left\lVert v_i\right\rVert_2^2+\left\lVert v_{i+1}\right\rVert_2^2)\\
 &\le2\max_i\left\lVert F_i\right\rVert_2\sum_i\left\lVert v_i\right\rVert_2^2.
\end{aligned}$$ Each retained core has exactly two chain-end incidences,
counting a loop twice and retaining both parallel contributions. This
proves the bound for every $r\ge1$, without summing an error $r$ times.
We obtain $$\left\lVert\mathcal S-I_r\otimes S_\infty\right\rVert_2
 \le E_s:=\frac{12b^2q^{2s}}{1-q^2}
              +576\delta\theta^s+32a q^s.
 \label{eq:assembly-error}$$

::: proof
*Proof of Theorem [1](#thm:cells){reference-type="ref"
reference="thm:cells"}.* Exact arithmetic with the two parameter columns
gives $$E_0=
 \begin{cases}
 501647/468750000<1/500,&c=c_0,\\
 700000123/196875000000000000<10^{-8},&c=c_1.
 \end{cases}$$ All terms in $E_s$ decrease with $s$.
Proposition [11](#prop:tail){reference-type="ref" reference="prop:tail"}
already supplies $S_\infty\succ(\gamma-\epsilon)I_6$, so
[\[eq:assembly-error\]](#eq:assembly-error){reference-type="eqref"
reference="eq:assembly-error"} gives
$$\mathcal S\succ(\gamma-2\epsilon)I_{6r}\succ0.$$ The condition
$p_i=2j_i-2\ge J$ is exactly $h_i\ge4(J+2)+2$, namely $106$ or $202$.
All eliminated pivots are positive by
Section [5](#sec:uniform){reference-type="ref" reference="sec:uniform"}.
Schur congruence now proves $cI-A_N(\tau,\alpha)^2\succ0$, as
required. ◻
:::

For each cell, the positive local quadrilateral fluxes
$Q_u=\tau_u\tau_{u+1}$ occur at positions $0,4,\ldots,8j-4$ relative to
its start. Successive positions have separation four within a cell and
six across a cell boundary. Thus the construction has $r$ gaps of length
six and all other gaps of length four. The proof uses the legal cell
words, not merely the number of such gaps. It is a full boundary-matrix
argument and does not depend on the historical localized-mode count,
physical interface-edge estimate, or IMS localization proof.

# Finite completion and explicit competitors {#sec:finite}

The preceding analysis reduces each remaining statement to an explicitly
bounded set of rational positive-definiteness tests. We give the
complete ranges and the separating inequalities, including the cases
where a stronger proposed cap is false.

## The one-cell family and its uniform ceiling

::: proof
*Proof of Theorem [2](#thm:one-cell){reference-type="ref"
reference="thm:one-cell"}.* For $k\ge25$, the single legal cell has
length $8k+2\ge202$, so Theorem [1](#thm:cells){reference-type="ref"
reference="thm:cells"} at $r=1$, $\alpha=+1$, and $c=c_1$ applies. The
remaining $k=1,\ldots,24$ are exactly the orders
$$10,18,26,\ldots,194.$$ For each full signed graph the rational
verifier proves $c_1I-A_{8k+2}(w_k,+1)^2\succ0$ by positive scalar Schur
pivots. The $10\times10$ matrix is constructed and checked directly,
without assuming disjoint ordinary and wrap block locations. The first
analytic order is $202$, so no admissible size is missing.

At $c_-=7905369/1000000$ and order $202$, independent exact elimination
of $c_-I-A_{202}(w_{25},+1)^2$ has $196$ positive scalar interior
pivots. The retained six-coordinate core then has a strictly negative
pivot after a positive scalar-pivot prefix. The recorded rational pivot
is strictly negative, not merely nonpositive or a failed numerical test.
Schur congruence gives a vector with negative quadratic form, and hence
$$\rho(A_{202}(w_{25},+1))^2>c_-.$$ This member supplies the lower
endpoint in [\[eq:supremum\]](#eq:supremum){reference-type="eqref"
reference="eq:supremum"}; the uniform strict upper bounds supply the
non-strict upper endpoint. ◻
:::

## Two and three nearly equal legal cells

For $r=2$ and $k\ge6$, the parameters
$\lfloor k/2\rfloor,\lceil k/2\rceil$ sum to $k$. When $k\ge26$, each is
at least $13$, so the cell bound $c_0$ applies. Exactly twenty finite
cases remain: $$k=6,\ldots,25,\qquad N=52,60,\ldots,204.
 \label{eq:R4finite}$$ All use negative holonomy. For even $k$ their
cell lengths are equal. For odd $k$ the two lengths are $N/2-4$ and
$N/2+4$, which changes the placement from the older equally spaced gap
construction. Each matrix in
[\[eq:R4finite\]](#eq:R4finite){reference-type="eqref"
reference="eq:R4finite"} is rebuilt from its own word and passes exact
rational LDL positivity at cap $c_0$. The first analytic order is $212$.

For $r=3$, write $k=3q+s$, $0\le s<3$. The three parameters
$$\left\lfloor\frac{k}{3}\right\rfloor,
 \left\lfloor\frac{k+1}{3}\right\rfloor,
 \left\lfloor\frac{k+2}{3}\right\rfloor$$ are $3-s$ copies of $q$
followed by $s$ copies of $q+1$. They sum to $k$, are at least two for
$k\ge6$, and differ by at most one. For $k\ge39$ they are all at least
thirteen, so Theorem [1](#thm:cells){reference-type="ref"
reference="thm:cells"} applies with positive holonomy. The remaining
thirty-three cases are $$k=6,\ldots,38,\qquad N=54,62,\ldots,310.
 \label{eq:R6finite}$$ Each full signed graph passes exact rational LDL
at cap $c_0$. The first analytic order is $318$, immediately after the
final admissible finite order. When $3\nmid k$, the cells are nearly
equal rather than identical, and no certificate for another gap
placement is substituted.

For both lists, the verification forms $(198/25)I-A^2$ or its
denominator-cleared equivalent $198I-25A^2$ directly from integer
two-edge walks. A separate implementation uses the normalized matrix and
a different scalar elimination order. For the three-cell list, it also
reconstructs the triangle signs independently from the quadrilateral-gap
word. Every required pivot in each list is strictly positive. These are
the only finite ranges left by the minimum-cell-length reduction for the
stated residue-four and residue-six families.

## The twisted comparison and the all-even witness range

::: proof
*Proof of Theorem [3](#thm:witnesses){reference-type="ref"
reference="thm:witnesses"}.* For residue two,
Theorem [2](#thm:one-cell){reference-type="ref"
reference="thm:one-cell"} gives the stronger cap $c_1<c_0$ at every
$k\ge6$. The two- and three-cell arguments above give the cap $c_0$ for
the other two residues. For $x>0$, $\cos x>1-x^2/2$, and $\pi^2<10$.
Therefore
$$\rho_{\mathrm{tw}}(N)^2>8-\frac{20\pi^2}{N^2}>8-\frac{200}{N^2}.
 \label{eq:benchmark-lower}$$ At $N\ge50$, the last expression is at
least $198/25$. Thus every nonzero residue witness satisfies
[\[eq:nonzero-witnesses\]](#eq:nonzero-witnesses){reference-type="eqref"
reference="eq:nonzero-witnesses"}. In particular, the exact endpoint
gaps for the other two residues are
$$\frac{2679}{338}-\frac{198}{25}=\frac{51}{8450}>0,
 \qquad
 \frac{5782}{729}-\frac{198}{25}=\frac{208}{18225}>0,$$ coming from
$N=52$ and $N=54$ respectively.

For $N=8m\ge32$, Theorem [6](#thm:period8){reference-type="ref"
reference="thm:period8"} gives a witness with squared radius at most
$\eta_*$. The rational comparison
$$\eta_*<\frac{999}{128}=8-\frac{200}{32^2}
 \label{eq:period8-separator}$$ follows by squaring positive quantities:
the intermediate bound is
$$\frac{(999/128-4)^2-10}{2}=\frac{73329}{32768}>\sqrt5,
 \quad 73329^2-5\cdot32768^2=8433121>0.$$
Equations [\[eq:benchmark-lower\]](#eq:benchmark-lower){reference-type="eqref"
reference="eq:benchmark-lower"} and
[\[eq:period8-separator\]](#eq:period8-separator){reference-type="eqref"
reference="eq:period8-separator"} prove the strict comparison at every
such order. The four residue classes now cover $32,40$ and every even
$N\ge48$. ◻
:::

## A stronger balanced subsequence and exact obstructions

Equal cells admit one additional small-order completion.

::: {#prop:balanced-sharp .proposition}
**Proposition 14**. *For every $j\ge1$,
$$\rho(A_{16j+4}(w_j\|w_j,-1))^2<c_1.$$ For $j\ge3$ this value is
strictly below the twisted benchmark.*
:::

::: proof
*Proof.* Corollary [12](#cor:phase){reference-type="ref"
reference="cor:phase"} applies for $j\ge25$, with the two finite phases
$z=\pm\mathrm i$. The remaining $j=1,\ldots,24$, at orders
$20,36,\ldots,388$, have exact full-graph positive-definiteness
certificates for $790537I-100000A^2$. Both primary and independent
rational replays cover the complete list. Their smallest case uses a
cell of length ten and is checked directly, including the coincident
couplings. The first analytic order is $404$. For $j\ge3$, $N\ge52$, so
[\[eq:benchmark-lower\]](#eq:benchmark-lower){reference-type="eqref"
reference="eq:benchmark-lower"} and $c_1<c_0$ give the comparison. ◻
:::

The sharper cap cannot replace $c_0$ in the full residue-four theorem.
For the negative-holonomy nearly balanced words, exact rational
elimination gives $$\begin{aligned}
 \rho(A_{60}(w_3\|w_4,-1))^2&>c_1,\\
 \rho(A_{76}(w_4\|w_5,-1))^2&>c_1.
\end{aligned}$$ In each case the certificate records a strictly negative
pivot with its complete positive predecessor prefix, proving a negative
direction for $c_1I-A^2$. Thus the obstruction is exact and applies to
the actual changed construction used here. There is also a distinct
obstruction for the older balanced $N=60$ gap word $[6,4^6,6,4^6]$ with
negative holonomy. Its half-length is thirty; its triangle signs change
sign under that half-shift rather than repeating a legal $w_j$. It
therefore lies outside
Proposition [14](#prop:balanced-sharp){reference-type="ref"
reference="prop:balanced-sharp"}, and its own exact negative pivot
confirms that dropping the even-$k$ condition would be false. None of
these obstructions contradicts the $c_0$ bound or gives an unrestricted
lower bound over all signings.

# Verification, provenance, and remaining questions {#sec:verification}

The proof has three exact computational inputs: the fixed rational
premises of Lemma [10](#lem:finite-premises){reference-type="ref"
reference="lem:finite-premises"}, the explicitly bounded finite graph
lists, and the strict lower obstructions. Everything that extends those
data to unbounded lengths, phases, or numbers of cells is proved in
Sections [5](#sec:uniform){reference-type="ref" reference="sec:uniform"}
and [6](#sec:cells){reference-type="ref" reference="sec:cells"}. The
finite lists are summarized below; a separate seed check supplies each
long-cell argument.

::: center
  Family                            Finite parameter range      Graph orders      Analytic from
  -------------------------------- ------------------------ -------------------- ---------------
  One cell ($c_1$)                      $1\le k\le24$        $10,18,\ldots,194$       $202$
  Two equal cells ($c_1$)               $1\le j\le24$        $20,36,\ldots,388$       $404$
  Two near-equal cells ($c_0$)          $6\le k\le25$        $52,60,\ldots,204$       $212$
  Three near-equal cells ($c_0$)        $6\le k\le38$        $54,62,\ldots,310$       $318$
:::

All acceptance comparisons use integers or rational numbers. Positive
pivots certify positive definiteness by exact Schur congruence; negative
pivots with positive predecessors certify the claimed strict
obstructions. The scripts store construction parameters, pivot counts,
exact certificate matrices or pivot data, and integrity digests. Digests
identify outputs; the mathematical tests are the rational computations
that generate them. Floating spectra used during exploration are
excluded from the proof.

Independent replays reconstruct the underlying graphs or isolated chain
responses separately, use different elimination orderings where
applicable, and match the exact statements rather than trusting stored
positivity flags. For example, the unequal-cell replay compares direct
full-graph elimination with independently eliminated chains embedded
additively into the cyclic boundary space, including loops and parallel
contributions. These finite comparisons test the implementations;
Lemma [13](#lem:assembly){reference-type="ref" reference="lem:assembly"}
proves the identity for every admissible length and number of cells.

The public supplement preserves the directories
`certificates/analytic/`, `certificates/strengthening/`,
`certificates/r4_pilot/`, `certificates/unequal_cells/`, and
`certificates/r6_completion/`. Their respective primary verifiers are
`verify_r2_certificate.py`, `verify_uniform_cap.py`,
`verify_r4_pilot.py`, `verify_unequal_cells.py`, and
`verify_r6_completion.py`. Each directory supplies its exact output. The
first package's independent replays are in `certificates/audit/`; the
later packages have their own `audit/` subdirectories. `assembly.py`
accompanies the unequal-cell verifier. The package README gives commands
and required dependencies.

A separate Lean development verifies the exact negative-holonomy finite
radius in Theorem [6](#thm:period8){reference-type="ref"
reference="thm:period8"}. For the explicit raw graph matrix and every
positive cell count, it proves that all Hermitian eigenvalue moduli are
at most the stated radical and that an eigenvalue equals its positive
value. The proof includes the seam and raw-operator bridges, maximal
antiperiodic phase, determinant root, and lower attainment. The verified
Lean 4.33.1 checkpoint audits $237$ declarations, with axiom union
exactly `propext`, `Classical.choice`, and `Quot.sound`. The separate
quartic identification used to name the conjectured constant, the
finite-size asymptotic, the integer principal-minor certificate, and the
Riccati/Schur and residue-completion arguments are not formalized by
that checkpoint. They retain their stated analytic and exact-certificate
evidence.

The exact period-eight formula and the witness range are inherited
project results; the present application to the revised conjecture and
the common unequal-cell proof have their scope distinguished in the
supplement's claim ledger. The new proof requires neither the older
physical interface-edge calculation nor an IMS localization estimate or
a count of localized modes. It does not change the status of historical
equality certificates at smaller orders.

The principal extremal problem remains to determine $\mu_N$ and its
minimizing switching classes. Even within the prescribed one-cell
family, the interval
[\[eq:supremum\]](#eq:supremum){reference-type="eqref"
reference="eq:supremum"} does not determine the exact supremum or prove
convergence. For broader cell arrangements, the two-cell obstructions at
orders $60$ and $76$ show that shortening cells can affect the sharper
cap. A structural lower bound over arbitrary triangle-sign words would
be needed to turn any of these explicit upper bounds into a global
minimization theorem.

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

*Earlier Target A finite structured counterexample package*, frozen
project source at commit `44ff33a89294056907d0b909d68a8db27371c4f0`.
[Archived construction and finite-tail
source](https://github.com/whzy3185/math/blob/44ff33a89294056907d0b909d68a8db27371c4f0/research/proofs/task54/TARGET_A_FINITE_STRUCTURED_COUNTEREXAMPLE_TAIL.md).
:::
