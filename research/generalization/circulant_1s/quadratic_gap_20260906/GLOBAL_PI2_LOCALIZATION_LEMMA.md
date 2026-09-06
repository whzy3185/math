# Explicit phase-mass localization lemma for the global `pi^2` proof

Date: 2026-09-06.

This note expands the only delicate asymptotic step in
`EVEN_GLOBAL_PI2_THEOREM.md`: ruling out a globally optimizing phase with a
soft hyperbolic exponent satisfying `r kappa_r -> infinity`.

It is written separately so the main theorem can cite a concrete inequality
rather than an informal "exponential beats bounded" sentence.

## 1. Setup

At the global root write

\[
 y=8-g,\qquad h=2-\mu\in[0,2],
\]

and suppose `mu>g`.  Then

\[
 d_-=2+\mu-g=2\cosh\kappa,
 \qquad
 d_+=6-\mu-g=2\cosh\eta,
\]

with `eta>=kappa>0` because `h>=0`.

Put

\[
 A_j=D_j(d_-)=\frac{\sinh((j+1)\kappa)}{\sinh\kappa},
\qquad
 B_j=D_j(d_+)=\frac{\sinh((j+1)\eta)}{\sinh\eta},
\]

and

\[
 \beta=\frac{B_{r-1}}{B_r},\qquad
 \gamma=\frac{B_{r-2}}{B_r}.
\]

The exact global root equation is

\[
 L_r=\pm R_r,
\tag{1}
\]

where

\[
 L_r=A_r-6\beta A_{r-1}+\gamma A_{r-2}
\tag{2}
\]

and

\[
 R_r=\frac2{B_r}
 \sqrt{(4-\mu)A_{r-1}^2+\mu B_{r-1}^2
 +(4\mu-\mu^2)A_{r-1}B_{r-1}+h^2/4}.
\tag{3}
\]

The already proved endpoint comparison gives `g=O(r^-2)`.

## 2. The right side is uniformly bounded

For `d_+>=d_->=2`, the continuant `D_j(d)` is nonnegative and increasing
both in `d` and in `j`.  Therefore

\[
 0\le \frac{A_{r-1}}{B_r}\le1,
 \qquad
 0\le\beta\le1.
\tag{4}
\]

Also

\[
 0\le4-\mu\le4,\quad
 0\le\mu\le2,\quad
 0\le4\mu-\mu^2\le4,\quad
 \frac{h^2}{4}\le1,\quad B_r\ge1.
\]

Dividing the radicand in (3) by `B_r^2` and using (4) gives the explicit
bound

\[
 \boxed{|R_r|\le2\sqrt{11}.}
\tag{5}
\]

No phase-independent constant hidden in `O(1)` is needed.

## 3. Exact leading coefficient on the left

The hyperbolic formulas give

\[
\begin{split}
 A_r&=\frac{e^{r\kappa}}{2\sinh\kappa}
     \left(e^\kappa-e^{-(2r+1)\kappa}\right),\\
 A_{r-1}&=\frac{e^{r\kappa}}{2\sinh\kappa}
     \left(1-e^{-2r\kappa}\right),\\
 A_{r-2}&=\frac{e^{r\kappa}}{2\sinh\kappa}
     \left(e^{-\kappa}-e^{-(2r-1)\kappa}\right).
\end{split}
\tag{6}
\]

Since `d_+>=4-g`, the hard exponent `eta` stays bounded below by a positive
absolute constant.  Hence

\[
 \beta=e^{-\eta}+O(e^{-2r\eta}),
 \qquad
 \gamma=e^{-2\eta}+O(e^{-2r\eta}).
\tag{7}
\]

If `r kappa -> infinity`, substituting (6)--(7) into (2) yields

\[
 L_r=\frac{e^{r\kappa}}{2\sinh\kappa}
 \left[B(\kappa,\eta)+o(\sinh\kappa)\right],
\tag{8}
\]

where

\[
 B(\kappa,\eta)
 =e^\kappa-6e^{-\eta}+e^{-\kappa-2\eta}.
\tag{9}
\]

Put

\[
 p=e^\kappa,\qquad q=e^{-\eta},
 \qquad \lambda=3+2\sqrt2=e^{\eta_0},
\]

where `cosh eta_0=3`.  Then the coefficient factors exactly as

\[
 \boxed{
 B(\kappa,\eta)
 =\frac{(p-\lambda q)(p-\lambda^{-1}q)}{p}.}
\tag{10}
\]

Thus its relevant zero is precisely

\[
 \kappa+\eta=\eta_0.
\tag{11}
\]

## 4. The zero is only the endpoint at `g=0`

At `g=0`, the channel relation is

\[
 \cosh\kappa+\cosh\eta=4,
 \qquad \eta\ge\kappa.
\tag{12}
\]

Along this curve,

\[
 \frac{d\eta}{d\kappa}
 =-\frac{\sinh\kappa}{\sinh\eta},
\]

so

\[
 \frac d{d\kappa}(\kappa+\eta)
 =1-\frac{\sinh\kappa}{\sinh\eta}\ge0,
\tag{13}
\]

with strict inequality while `eta>kappa`.  At `kappa=0`,
`eta=eta_0`; hence

\[
 \kappa+\eta>\eta_0
\]

for every nonendpoint point of the curve.  By (10),

\[
 B(\kappa,\eta)>0\qquad(\kappa>0,g=0).
\tag{14}
\]

Consequently, on every compact region `kappa>=kappa_0>0`, continuity gives
an absolute positive lower bound for `B` once `g` is sufficiently small.

## 5. Endpoint expansion of the coefficient

It remains to control `kappa->0`.  The exact channel relations are

\[
 \cosh\kappa=1+\frac{\mu-g}{2},
 \qquad
 \cosh\eta=3-\frac{\mu+g}{2}.
\tag{15}
\]

Since

\[
 \mu-g=2\cosh\kappa-2=\kappa^2+O(\kappa^4),
\]

one gets

\[
 \eta=\eta_0+O(g+\kappa^2).
\tag{16}
\]

Expanding (9) at `(kappa,eta)=(0,eta_0)` and using
`1-6lambda^(-1)+lambda^(-2)=0` gives

\[
 \boxed{
 B(\kappa,\eta)
 =(1-\lambda^{-2})\kappa
 +O(\kappa^2+g).}
\tag{17}
\]

If a subsequence satisfies `r kappa -> infinity`, then
`g=O(r^-2)=o(kappa)`.  Hence for all sufficiently large indices on that
subsequence,

\[
 B(\kappa,\eta)\ge c\kappa
\tag{18}
\]

for some absolute `c>0`.  Since `sinh kappa~kappa` when `kappa->0`, (18)
also gives

\[
 \frac{B(\kappa,\eta)}{\sinh\kappa}\ge c'>0.
\tag{19}
\]

Together with the compact-region argument after (14), (19) is valid in the
only two possible regimes of a hypothetical `r kappa -> infinity`
subsequence.

## 6. Contradiction and localization

Equations (8) and (19) imply

\[
 |L_r|\ge c'' e^{r\kappa}
\]

for all sufficiently large indices of that subsequence.  This diverges,
whereas the exact bound (5) gives

\[
 |R_r|\le2\sqrt{11}.
\]

This contradicts the root equation (1).  Therefore

\[
 \boxed{r\kappa=O(1).}
\tag{20}
\]

Finally

\[
 \mu-g=2\cosh\kappa-2=O(r^{-2}),
\]

and `g=O(r^-2)`, so

\[
 \boxed{\mu=2-h=O(r^{-2}).}
\tag{21}
\]

This is the precise localization lemma used in Sections 5--8 of
`EVEN_GLOBAL_PI2_THEOREM.md`.

## 7. What this lemma does and does not prove

The lemma proves the scale needed for the leading constant.  The remainder
of the global theorem then rules out the hyperbolic soft regime after
rescaling, obtains the same limiting Robin equation `cos x=0` in the
oscillatory regime, and compares with the endpoint to strengthen (21) to

\[
 r^2(2-h_r)\to0.
\]

It does **not** prove the numerically sharper `2-h_r=Theta(r^-4)` law.  That
requires the second-order two-mode calculation recorded separately as the
next target.
