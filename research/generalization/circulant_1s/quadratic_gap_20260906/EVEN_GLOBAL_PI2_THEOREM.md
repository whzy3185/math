# Even jumps: global sharp `pi^2` Bloch-gap asymptotic

Date: 2026-09-06.

This note closes the main sharp problem left after
`ENDPOINT_PI2_ASYMPTOTIC.md`.  The exact `s=10` phase-slip certificate remains
valid: the maximizing phase need not be zero.  Nevertheless the phase drift
is too small to change the leading quadratic-gap constant.

Throughout `s=2r` and `r->infinity`.

## 1. Statement

Let

\[
 R_{2r}=\max_{|z|=1}\rho(H_{2r}(z))^2,
 \qquad
 g_{2r}=8-R_{2r}.
\]

**Theorem G (global sharp limit).**

\[
 \boxed{4r^2 g_{2r}\longrightarrow\pi^2.}
\tag{G1}
\]

Equivalently,

\[
 \boxed{s^2(8-R_s)\longrightarrow\pi^2
 \qquad(s\to\infty,\ s\text{ even}).}
\tag{G2}
\]

Consequently, after combining with `ODD_JUMP_SHARP_GAP.md`, the
parity-dependent all-jump family from `ALL_S_UNIFIED_THEOREM.md` satisfies

\[
 \boxed{s^2(8-\widehat R_s)\longrightarrow\pi^2}
 \qquad(s\to\infty)
\tag{G3}
\]

through **all** integer jumps.

A phase localization statement is obtained at the same time.  If `h_r` is a
square-root Bloch parameter attaining the global edge, chosen in `[0,2]` by
the symmetry `h -> -h`, then

\[
 \boxed{r^2(2-h_r)\longrightarrow0.}
\tag{G4}
\]

This is weaker than the numerically suggested second-order law
`2-h_r=Theta(r^-4)`, but it is sufficient for the sharp leading constant.

## 2. Global root and endpoint upper bound

Choose a maximizing phase and write

\[
 h_r\in[0,2],\qquad
 \mu_r=2-h_r,\qquad
 y_r=8-g_{2r}.
\]

The exact characteristic polynomial from
`../extension_20260905/EVEN_JUMP_THEOREM_AND_PROOF.md` satisfies

\[
 q_r(y_r,h_r)=0.
\tag{1}
\]

Because phase zero is an allowed phase,

\[
 g_{2r}\le e_r,
\]

where `e_r` is the endpoint gap from `ENDPOINT_PI2_ASYMPTOTIC.md`.  Hence

\[
 g_{2r}=O(r^{-2})
\tag{2}
\]

and, more sharply,

\[
 \limsup r^2g_{2r}\le\frac{\pi^2}{4}.
\tag{3}
\]

The continuant arguments at the global root are

\[
 d_-:=y_r-4-h_r=2+\mu_r-g_{2r},
 \qquad
 d_+:=y_r-4+h_r=6-\mu_r-g_{2r}.
\tag{4}
\]

Thus `d_-` is the soft channel and `d_+` the hard channel.

## 3. Root equation divided by the hard channel

Put

\[
 A_j=D_j(d_-),\qquad B_j=D_j(d_+),
\]

and

\[
 \beta_r=\frac{B_{r-1}}{B_r},\qquad
 \gamma_r=\frac{B_{r-2}}{B_r}.
\]

The compact determinant identity

\[
 q_r(y,h)=S_r(y,h)^2
 -4\big((2+h)a^2+(2-h)b^2+(4-h^2)ab\big)-h^2
\]

with `a=A_(r-1)`, `b=B_(r-1)` gives at the root

\[
\begin{split}
 &A_r-6\beta_rA_{r-1}+\gamma_rA_{r-2}\\
 &\qquad=\pm\frac2{B_r}
 \sqrt{(4-\mu_r)A_{r-1}^2
       +\mu_rB_{r-1}^2
       +(4\mu_r-\mu_r^2)A_{r-1}B_{r-1}
       +\frac{h_r^2}{4}}.
\end{split}
\tag{5}
\]

This equation contains the phase slip in one place: the new dominant
phase-dependent term is `mu_r B_(r-1)^2` under the square root.

## 4. First localization: `mu_r=O(r^-2)`

If `mu_r<=g_(2r)`, (2) already gives `mu_r=O(r^-2)`.  It remains to treat

\[
 \mu_r>g_{2r}.
\]

Define `kappa_r>0` by

\[
 2\cosh\kappa_r=d_-=2+\mu_r-g_{2r}.
\tag{6}
\]

Then

\[
 A_j=\frac{\sinh((j+1)\kappa_r)}{\sinh\kappa_r}.
\]

We claim

\[
 r\kappa_r=O(1).
\tag{7}
\]

Suppose instead that a subsequence has `r kappa_r -> infinity`.  Let
`eta_r>0` be defined by

\[
 2\cosh\eta_r=d_+.
\]

Because `h_r>=0`, one has `eta_r>=kappa_r`; moreover the hard channel stays
uniformly away from zero whenever `g_(2r)->0`.

For `r kappa_r -> infinity`, the left side of (5) has the standard
hyperbolic asymptotic

\[
 \frac{e^{r\kappa_r}}{2\sinh\kappa_r}
 \left(
 e^{\kappa_r}-6e^{-\eta_r}
 +e^{-\kappa_r-2\eta_r}+o(1)
 \right).
\tag{8}
\]

The coefficient in parentheses is positive away from the endpoint and has a
positive first-order limit at the endpoint.  To see the endpoint structure,
put `p=e^{kappa}` and `q=e^{-eta}`.  At `y=8` the numerator is

\[
 p^2-6pq+q^2.
\]

Its only zero with `p/q>1` is

\[
 \frac pq=3+2\sqrt2=\lambda,
\]

which occurs at `h=2`, `kappa=0`.  Near that point,

\[
 e^{\kappa}-6e^{-\eta}+e^{-\kappa-2\eta}
 =(1-\lambda^{-2})\kappa+O(\kappa^2+g_{2r}).
\tag{9}
\]

If `r kappa_r -> infinity`, (2) implies `g_(2r)=o(kappa_r^2)` whenever
`kappa_r->0`, so (8)--(9) still grow like `c e^(r kappa_r)` for some
`c>0` along the subsequence.

The right side of (5), however, stays bounded.  Indeed `eta_r>=kappa_r`
keeps `A_(r-1)/B_r` bounded, `B_(r-1)/B_r<=1`, and `0<=mu_r<=2`; taking the
square root gives an absolute `O(1)` bound.  This contradiction proves (7).

Since

\[
 \mu_r-g_{2r}=2\cosh\kappa_r-2
 =\kappa_r^2+O(\kappa_r^4),
\]

(2) and (7) imply

\[
 \boxed{\mu_r=O(r^{-2}).}
\tag{10}
\]

Thus every globally maximizing phase already lies in a shrinking endpoint
window.

## 5. Hard-channel ratios are endpoint-universal

From (2) and (10),

\[
 d_+=6+O(r^{-2}).
\]

Let `eta_0>0` satisfy `2 cosh eta_0=6` and

\[
 \lambda=e^{\eta_0}=3+2\sqrt2.
\]

Exactly as in the endpoint proof,

\[
 \boxed{
 \beta_r=\lambda^{-1}+O(r^{-2})+O(e^{-cr}),
 \qquad
 \gamma_r=\lambda^{-2}+O(r^{-2})+O(e^{-cr})}
\tag{11}
\]

for some absolute `c>0`.

The identity

\[
 6\lambda^{-1}=1+\lambda^{-2}
\tag{12}
\]

will again produce the limiting Robin equation.

## 6. The hyperbolic soft regime is impossible in the limit

Assume along a subsequence that

\[
 \mu_r>g_{2r}.
\]

By (7), after a further subsequence

\[
 r\kappa_r\to x\ge0.
\]

Multiply (5) by `sinh(kappa_r)` and divide by `kappa_r`.  Because
`kappa_r=O(r^-1)` and the hard channel grows exponentially,
all terms under the square root involving `A_(r-1)/B_r` vanish after this
normalization.  The only non-exponentially-small term is
`mu_r(B_(r-1)/B_r)^2`.  By (10), its contribution is

\[
 O(\sqrt{\mu_r})=O(r^{-1})\to0.
\tag{13}
\]

Using (11)--(12), the normalized left side tends to

\[
 (1-\lambda^{-2})\cosh x.
\tag{14}
\]

Equation (5) would therefore force

\[
 \cosh x=0,
\]

which is impossible for real `x>=0`.

Hence the global root cannot remain in the hyperbolic soft regime.  After
passing to sufficiently large `r` (or, equivalently, for every asymptotic
subsequence relevant to the limit),

\[
 g_{2r}\ge\mu_r.
\tag{15}
\]

## 7. Oscillatory soft channel and the universal Robin limit

Define `theta_r>=0` by

\[
 g_{2r}-\mu_r=2-2\cos\theta_r.
\tag{16}
\]

From (2), `theta_r=O(r^-1)`.  The endpoint test bound gives
`r theta_r<=pi+o(1)`, so every subsequence has a further subsequence with

\[
 r\theta_r\to x\in[0,\pi].
\tag{17}
\]

Now

\[
 A_j=\frac{\sin((j+1)\theta_r)}{\sin\theta_r}.
\]

Multiply (5) by `sin(theta_r)` and divide by `theta_r`.  As in the
hyperbolic case, the `A/B_r` contributions on the right are exponentially
small.  The phase term contributes only

\[
 O(\sqrt{\mu_r})=O(r^{-1})\to0.
\tag{18}
\]

The coefficient errors in (11) also vanish after normalization.  Therefore
the left side has exactly the same limit as in the endpoint theorem:

\[
 (1-\lambda^{-2})\cos x.
\tag{19}
\]

The root equation forces `cos x=0`.  Since `x in [0,pi]`,

\[
 \boxed{r\theta_r\longrightarrow\frac\pi2.}
\tag{20}
\]

Consequently

\[
 r^2(g_{2r}-\mu_r)
 =r^2(2-2\cos\theta_r)
 \longrightarrow\frac{\pi^2}{4}.
\tag{21}
\]

## 8. Endpoint comparison kills the phase mass at leading order

Since `mu_r>=0`, (21) gives

\[
 r^2g_{2r}
 =r^2\mu_r+\frac{\pi^2}{4}+o(1).
\tag{22}
\]

But the phase-zero endpoint is available and
`ENDPOINT_PI2_ASYMPTOTIC.md` proves

\[
 r^2g_{2r}\le r^2e_r
 =\frac{\pi^2}{4}+o(1).
\tag{23}
\]

Comparing (22) and (23) forces

\[
 \boxed{r^2\mu_r\to0,}
\tag{24}
\]

which is (G4), and then

\[
 \boxed{r^2g_{2r}\to\frac{\pi^2}{4}.}
\]

This proves (G1)--(G2).

## 9. All-jump sharp limit

For odd `s`, `ODD_JUMP_SHARP_GAP.md` already proves

\[
 s^2(8-\widehat R_s)\to\pi^2.
\]

For even `s`, (G2) proves the same statement.  Therefore the
parity-dependent explicit family satisfies the parity-free limit (G3).

The project has thus progressed from

- an exponential even-jump gap;
- to a cubic inverse-polynomial gap;
- to a quadratic-order gap;
- to endpoint `pi^2`;
- and now to the **global sharp `pi^2` constant for every jump**.

## 10. Second-order phase-slip conjecture

The proof above deliberately stops once the leading constant is closed.
Numerical diagonalization of the exact reduced matrix suggests the stronger
laws

\[
 r^2\phi_r\to\frac\pi{4\sqrt2},
\tag{25}
\]

where `h_r=2 cos(phi_r)`, and

\[
 r^4(e_r-g_{2r})\to\frac{\pi^2}{32}.
\tag{26}
\]

These constants are consistent with an effective two-mode expansion

\[
 g_{2r}(\phi)
 =e_r+\phi^2
 -\frac{\pi}{2\sqrt2}\frac{|\phi|}{r^2}
 +o(r^{-4})
\]

in the boundary layer `phi=Theta(r^-2)`.  Equations (25)--(26) are recorded
as conjectural second-order targets, not used in Theorem G.

## 11. Proof-audit boundary

The new step relative to the endpoint proof is the phase-mass localization
argument in Sections 4--6.  A final manuscript version should expand the
uniform constants in the hyperbolic estimate (8)--(9) into explicit lemmas,
so that the contradiction `r kappa_r -> infinity` is fully epsilon-level
rather than asymptotic prose.  The determinant equation, channel formulas,
and endpoint ratio estimates used here are exact results already established
in the preceding notes.

No global optimality over all signings is claimed: Theorem G concerns the
explicit antipodal family and its Bloch phase maximum.
