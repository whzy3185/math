# Odd jumps: an exact quadratic-gap theorem with sharp constant

Date: 2026-09-06.

This note completes the missing parity in the `C_N(1,s)` workstream.  The
older Task 60 analysis already proved that the alternating-flux signing has a
continuous squared Bloch edge strictly below `8` when `s` is odd.  Here that
qualitative statement is upgraded to a quantitative theorem, a unique
critical-point description, and the sharp large-jump constant.

Throughout this note `s>=3` is odd.

## 1. Alternating-flux fiber

In Hamilton gauge take

\[
  \tau_i=(-1)^i.
\]

Let `T` denote the quasiperiodic unit shift.  Since `s` is odd,
`tau_i tau_(i+s)=-1`, and the mixed terms cancel exactly.  Hence

\[
 A_s^2=4I+T^2+T^{-2}-T^{2s}-T^{-2s}.
\tag{1}
\]

On a Fourier mode with `T=e^{i theta}` the squared dispersion is

\[
 F_s(\theta)=4+2\cos(2\theta)-2\cos(2s\theta).
\tag{2}
\]

Write

\[
 M_s=\max_{\theta\in\mathbb R}F_s(\theta),\qquad
 g_s^{\rm odd}=8-M_s.
\]

Then the gap has the exact variational form

\[
 \boxed{
 g_s^{\rm odd}=4\min_{\theta\in\mathbb R}
 \big(\sin^2\theta+\cos^2(s\theta)\big).}
\tag{3}
\]

In particular the gap is strictly positive: equality in (3) would require
simultaneously `theta in pi Z` and `s theta in pi/2+pi Z`, which is
impossible.

## 2. The unique minimizing phase

Because both terms in (3) are `pi`-periodic and even, restrict to
`0<=theta<=pi/2`.  The test point `theta=pi/(2s)` gives

\[
 \sin^2\theta+\cos^2(s\theta)=\sin^2\frac\pi{2s}.
\tag{4}
\]

If `theta>=pi/s`, then

\[
 \sin^2\theta\ge \sin^2\frac\pi s
 >\sin^2\frac\pi{2s},
\]

so every global minimizer lies in `[0,pi/s]`.  On
`[pi/(2s),pi/s]`, `sin(2 theta)>0` and `sin(2s theta)<=0`, hence the
derivative of the quantity in (3),

\[
 \sin(2\theta)-s\sin(2s\theta),
\tag{5}
\]

is strictly positive.  Thus the minimizer lies in `(0,pi/(2s))`.

On this interval, divide the critical equation by `sin(2 theta)>0`:

\[
 \frac{\sin(2s\theta)}{\sin(2\theta)}=\frac1s.
\tag{6}
\]

The function

\[
 x\longmapsto \frac{\sin(sx)}{\sin x}
\]

is strictly decreasing on `(0,pi/s)`.  Indeed, after multiplying its
derivative by `sin^2 x`, the negative of the numerator is

\[
 h(x)=\sin(sx)\cos x-s\cos(sx)\sin x,
\]

and

\[
 h'(x)=(s^2-1)\sin(sx)\sin x>0,
\]

with `h(0)=0`.  Therefore (6) has exactly one solution

\[
 \boxed{\theta_s\in(0,\pi/(2s)).}
\]

Equivalently,

\[
 \boxed{\sin(2\theta_s)=s\sin(2s\theta_s).}
\tag{7}
\]

Using `sin(sx)=sin x U_(s-1)(cos x)`, this is also the algebraic equation

\[
 \boxed{s\,U_{s-1}(\cos(2\theta_s))=1.}
\tag{8}
\]

Consequently `M_s` and `g_s^odd` are algebraic numbers for every fixed odd
`s`.

## 3. A sharp finite-`s` localization

The derivative in (5) is negative at `theta=pi/(4s)` because

\[
 \sin\frac\pi{2s}-s<0.
\]

By uniqueness of the zero,

\[
 \frac\pi{4s}<\theta_s<\frac\pi{2s}.
\tag{9}
\]

Set

\[
 \varepsilon_s=\frac\pi{2s}-\theta_s.
\]

Then `0<2s epsilon_s<pi/2`, and (7) becomes

\[
 \sin(2\theta_s)=s\sin(2s\varepsilon_s).
\tag{10}
\]

Use `sin u>=2u/pi` on `[0,pi/2]` and
`sin(2 theta_s)<=2 theta_s<=pi/s`.  Equation (10) gives

\[
 \frac{4s^2}{\pi}\varepsilon_s
 \le s\sin(2s\varepsilon_s)
 =\sin(2\theta_s)
 \le\frac\pi s.
\]

Thus

\[
 \boxed{0<\varepsilon_s\le\frac{\pi^2}{4s^3}.}
\tag{11}
\]

This already pins the maximizing Bloch phase to an `O(s^-3)` window around
`pi/(2s)`.

## 4. Quadratic gap and the sharp constant

At the minimizing phase,

\[
 g_s^{\rm odd}=4\big(\sin^2\theta_s+\cos^2(s\theta_s)\big).
\]

The test point (4) gives the upper bound.  For the lower bound discard the
second nonnegative term and use (11).  Therefore

\[
 \boxed{
 4\sin^2\!\left(\frac\pi{2s}-\frac{\pi^2}{4s^3}\right)
 \le g_s^{\rm odd}
 \le 4\sin^2\frac\pi{2s}.}
\tag{12}
\]

Both sides have the same leading term, so

\[
 \boxed{s^2 g_s^{\rm odd}\longrightarrow\pi^2
 \qquad(s\to\infty,\ s\text{ odd}).}
\tag{13}
\]

In particular the old qualitative threshold `M_s<8` is quantitatively
strengthened to

\[
 8-M_s=\Theta(s^{-2}),
\]

with the exact leading constant `pi^2`.

A coarser parity-uniform estimate, useful when joining this result to the
even-jump theorem, is

\[
 \boxed{g_s^{\rm odd}\ge\frac4{1+s^2}.}
\tag{14}
\]

For completeness, (14) follows by reducing `theta` to `[-pi/2,pi/2]`,
choosing `delta in [-pi/2,pi/2]` with
`cos^2(s theta)=sin^2 delta`, and noting that
`|s theta-delta|>=pi/2`.  Cauchy--Schwarz and
`sin^2 u>=4u^2/pi^2` give

\[
 \theta^2+\delta^2\ge\frac{\pi^2}{4(1+s^2)},
\]

which proves (14).

## 5. Finite rings

For every admissible even order `N` with `2<=s<N/2`, the period-two word
lifts to `C_N(1,s)`.  In either Hamilton holonomy sector the exact Fourier
grid from Task 60 is a subset of the continuous phase circle, hence

\[
 \rho(A_{N,s,\alpha})^2\le M_s=8-g_s^{\rm odd}<8.
\tag{15}
\]

Thus for every odd jump, every admissible even order already has an explicit
signing with spectral radius strictly below `sqrt(8)`; no large-`N`
threshold is required.

This finite compatibility statement is stronger than the even-jump
antipodal construction, whose present explicit repetition theorem requires
`N` to be a multiple of `4s`.

## 6. Formal/asymptotic follow-up

The critical equation also supports the expansion

\[
 \theta_s=
 \frac\pi{2s}-\frac\pi{2s^3}
 +\left(\frac\pi2+\frac{\pi^3}{12}\right)s^{-5}
 +O(s^{-7}),
\]

and hence

\[
 g_s^{\rm odd}
 =\frac{\pi^2}{s^2}
 -\frac{\pi^2+\pi^4/12}{s^4}
 +O(s^{-6}).
\tag{16}
\]

Equation (16) is recorded as the next asymptotic refinement target; the
rigorous results needed for the all-`s` theorem are (12)--(15).

No publication-priority claim is made here.  The closest current signed
circulant paper located in the project literature audit treats the
special jump `s=2`; a broader periodic/magnetic-operator comparison remains
necessary before claiming novelty for the all-jump theorem.
