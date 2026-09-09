# Period-two variational theory for signed step operators

Date: 2026-09-09

Status: **Proved**. This note belongs only to Paper I (`paper/circulant-periodic-gap-20260909`). It concerns optimization inside the period-two Hamilton-gauge sector and does not quantify over all finite signings.

Let

\[
(A_{s,\tau}x)_i=x_{i-1}+x_{i+1}+\tau_{i-s}x_{i-s}+\tau_i x_{i+s},
\]

where `tau` is periodic of period dividing two. Let `R_s^(2)(tau)` denote the continuous squared Bloch spectral radius of this periodic operator.

## Theorem 1 — complete period-two phase diagram

For every integer `s>=2`, among all words of period dividing two, the alternating words

\[
\tau_i=\pm(-1)^i
\]

are the unique minimizers up to translation. More precisely:

1. If `s` is odd, then
   \[
   \min_{\operatorname{per}(\tau)\mid2}R_s^{(2)}(\tau)
   =8-g_s<8,
   \]
   where
   \[
   g_s=4\min_{\theta\in\mathbb R}
   \bigl(\sin^2\theta+\cos^2(s\theta)\bigr).
   \]
2. If `s` is even, then
   \[
   \min_{\operatorname{per}(\tau)\mid2}R_s^{(2)}(\tau)=8,
   \]
   again attained exactly by the two alternating words.

Thus the parity split is already forced in the smallest nontrivial periodic sector: period two crosses below the squared edge `8` exactly for odd jumps.

### Proof

There are only four words of period dividing two. The two alternating words are translates and therefore have the same Bloch radius; the two constant words are treated separately.

For an alternating word, the mixed terms in `A^2` cancel because `tau_(i+1)=-tau_i`. The pure chord-square term has sign

\[
\tau_i\tau_{i+s}=(-1)^s.
\]

Hence on a scalar Fourier mode `T=e^{i theta}`,

\[
A^2=4I+T^2+T^{-2}+(-1)^s(T^{2s}+T^{-2s}).
\]

If `s` is odd, the squared dispersion is

\[
F_s(\theta)=4+2\cos(2\theta)-2\cos(2s\theta),
\]

so

\[
8-F_s(\theta)
=4\bigl(\sin^2\theta+\cos^2(s\theta)\bigr).
\]

The two terms on the right cannot vanish simultaneously, so the continuous maximum is strictly below `8`.

If `s` is even, instead

\[
F_s(\theta)=4+2\cos(2\theta)+2\cos(2s\theta)\le8,
\]

and equality holds at `theta=0`. Thus the alternating period-two radius is exactly `8`.

For a constant word `tau_i=epsilon`, the operator is translation invariant with symbol

\[
\lambda_\epsilon(\theta)=2\cos\theta+2\epsilon\cos(s\theta).
\]

For `epsilon=+1`, `lambda_+(0)=4`, hence the squared radius is `16`.

For `epsilon=-1` and even `s`, `lambda_-(pi)=-4`, so the squared radius is again `16`.

For `epsilon=-1` and odd `s`, take `theta=pi/(s+1)`. Since

\[
\cos(s\theta)=-\cos\theta,
\]

we obtain

\[
|\lambda_-(\theta)|=4\cos\frac\pi{s+1},
\]

and therefore

\[
R_s^{(2)}(\tau)\ge16\cos^2\frac\pi{s+1}\ge8.
\]

The alternating word has radius strictly below `8` for odd `s`, while for even `s` it has radius exactly `8` and both constant words have radius `16`. This proves the classification.

---

## Theorem 2 — unique odd optimizing phase

Assume now that `s>=3` is odd. There is a unique minimizer

\[
\theta_s\in(0,\pi/(2s))
\]

of

\[
\sin^2\theta+\cos^2(s\theta),
\]

and it is characterized by

\[
\boxed{\sin(2\theta_s)=s\sin(2s\theta_s).}
\]

Equivalently,

\[
sU_{s-1}(\cos(2\theta_s))=1.
\]

The uniqueness proof is the monotonic Chebyshev-ratio argument already present in `ODD_JUMP_SHARP_GAP.md`; it is retained here because the present note uses the minimizer as a variational object.

---

## Theorem 3 — strict monotonicity of the odd period-two gap

Along odd integers `s>=3`,

\[
\boxed{g_s\text{ is strictly decreasing},}
\]

while

\[
\boxed{s^2g_s\text{ is strictly increasing}.}
\]

Consequently

\[
0<s^2g_s<\pi^2
\]

for every odd `s>=3`, and the sequence approaches `pi^2` from below.

### Proof

The localization from Theorem 2 allows the change of variable

\[
x=s\theta\in[0,\pi/2].
\]

Thus

\[
g_s=4\min_{0\le x\le\pi/2}
\left(\sin^2\frac{x}{s}+\cos^2x\right).
\]

If `s_2>s_1`, then for every `x>0`,

\[
\sin^2(x/s_2)<\sin^2(x/s_1).
\]

The minimizer is in `(0,pi/2)`, so evaluating the `s_2` functional at the `s_1` minimizer gives `g_(s_2)<g_(s_1)`.

For the scaled gap, write

\[
s^2g_s
=4\min_{0\le x\le\pi/2}
\left([s\sin(x/s)]^2+s^2\cos^2x\right).
\]

For fixed `x>0`, the function `s sin(x/s)` is strictly increasing because, with `u=x/s`,

\[
\frac{d}{ds}\bigl[s\sin(x/s)\bigr]
=\sin u-u\cos u>0.
\]

At `x=0`, the second term `s^2 cos^2 x=s^2` is strictly increasing; at `x=pi/2`, the first term is strictly increasing. Hence the whole scaled integrand is pointwise strictly increasing on the compact interval. Its minimum is therefore strictly increasing. The limit `pi^2` follows from Theorem 4 below (or from the previously proved leading asymptotic).

---

## Theorem 4 — high-order sharp odd asymptotics

As `s->infinity` through odd integers,

\[
\boxed{
\begin{aligned}
\theta_s={}&\frac\pi{2s}-\frac\pi{2s^3}
+\frac{\pi(6+\pi^2)}{12s^5}\\
&-\frac{\pi(\pi^4+100\pi^2+120)}{240s^7}
+O(s^{-9}).
\end{aligned}}
\]

Moreover

\[
\boxed{
\begin{aligned}
g_s={}&\frac{\pi^2}{s^2}
-\frac{\pi^2(\pi^2+12)}{12s^4}\\
&+\frac{\pi^2(\pi^4+120\pi^2+360)}{360s^6}\\
&-\frac{\pi^2(\pi^6+896\pi^4+18480\pi^2+20160)}{20160s^8}
+O(s^{-10}).
\end{aligned}}
\]

This upgrades the former recorded target

\[
g_s=\pi^2s^{-2}-(\pi^2+\pi^4/12)s^{-4}+O(s^{-6})
\]

to a rigorous multi-term expansion.

### Proof

Put

\[
\varepsilon_s=\frac\pi{2s}-\theta_s,
\qquad
u_s=s^3\varepsilon_s,
\qquad t=s^{-1}.
\]

The previously proved localization `epsilon_s=O(s^-3)` makes `u_s` bounded. The critical equation becomes

\[
\sin(\pi t-2u_st^3)=t^{-1}\sin(2u_st^2).
\]

Equivalently,

\[
\Phi(t,u_s)=0,
\]

where

\[
\Phi(t,u):=
\frac{\sin(2ut^2)}{t^2}
-\frac{\sin(\pi t-2ut^3)}{t}.
\]

The apparent singularities are removable. The extension to `t=0` is real analytic and even in `t`, with

\[
\Phi(0,u)=2u-\pi,
\qquad
\partial_u\Phi(0,\pi/2)=2.
\]

Also the bounded critical equation itself gives `u_s->pi/2`. The analytic implicit-function theorem therefore gives a unique even analytic branch

\[
u(t)=u_0+u_2t^2+u_4t^4+O(t^6)
\]

containing all sufficiently large odd integer points. Expanding `Phi(t,u(t))=0` yields successively

\[
u_0=\frac\pi2,
\qquad
u_2=-\frac{\pi(6+\pi^2)}{12},
\qquad
u_4=\frac{\pi(\pi^4+100\pi^2+120)}{240}.
\]

Since

\[
\theta_s=\frac\pi{2s}-\frac{u(1/s)}{s^3},
\]

this proves the displayed expansion for `theta_s`.

Finally substitute that expansion into

\[
g_s=4\bigl(\sin^2\theta_s+\cos^2(s\theta_s)\bigr)
\]

and expand the analytic functions. The coefficients are exactly those displayed above; the `O(s^-9)` remainder in `theta_s` contributes only `O(s^-10)` to the gap because `theta_s=O(s^-1)` and `pi/2-s theta_s=O(s^-2)`.

---

## Paper-level significance

This theorem package changes the role of the odd-jump section. It is no longer merely one half of an existence proof. It gives a complete variational classification of the smallest periodic sector, proves that the parity bifurcation is already visible at period two, establishes monotone convergence to the sharp constant `pi^2`, and supplies a multi-term asymptotic expansion.
