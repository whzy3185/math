# Universal phase slip in the macroscopic periodic-well regime

Date: 2026-09-10

Status: **Proved**. This extends the balanced phase-slip theorem to every macroscopic geometry whose complementary bulk arc is at least as long as the defect arc.

## 1. Setup

Write

\[
L=2(N+m),\qquad h=2m,
\]

and assume

\[
N,m\to\infty,
\qquad
\frac mN\to\gamma\in(0,1].
\tag{1.1}
\]

Let the compatible jump be

\[
s=L(2q+1),
\]

with arbitrary varying odd multiplier. Write

\[
z=e^{i\phi},
\qquad
\psi=(2q+1)\phi,
\qquad
d=2\cos\psi.
\]

Let

\[
\Gamma_{N,m,q}=8-\max_{|z|=1}\rho(H_{N,m,q}(z))^2
\]

and let

\[
e^+_{N,m}=8-\rho(H(1))^2.
\]

For `gamma<1`, the macroscopic full-Bloch theorem shows that the `d=2` well is the unique leading-order well. For `gamma=1`, it is tied with the antiperiodic well but the local statement below remains valid.

## Theorem A — local universal effective law

Let

\[
\psi=\frac\zeta{N^2},
\qquad \zeta=O(1),
\]

and let `g_{N,m}(psi)` be the squared gap of the lower top soft branch near the periodic endpoint. Then, locally uniformly for bounded `zeta`,

\[
\boxed{
N^4\bigl(g_{N,m}(\zeta/N^2)-e^+_{N,m}\bigr)
=
\zeta^2-
\frac{\pi}{2\sqrt2}|\zeta|
+o(1).
}
\tag{1.2}
\]

The limiting law is independent of `gamma` and of the odd multiplier.

## Theorem B — global phase slip for `0<gamma<1`

If

\[
0<\gamma<1,
\]

and `z_{N,m,q}` is any global maximizing Bloch phase, choose the representative with compressed phase `psi` closest to zero. Then

\[
\boxed{
N^2|\psi_{N,m,q}|
\longrightarrow
\frac{\pi}{4\sqrt2},
}
\tag{1.3}
\]

and

\[
\boxed{
N^4\bigl(e^+_{N,m}-\Gamma_{N,m,q}\bigr)
\longrightarrow
\frac{\pi^2}{32}.
}
\tag{1.4}
\]

Thus throughout the periodic-well macroscopic phase the global maximizer is shifted off the periodic endpoint by a universal compressed amount of order `N^-2`.

For `gamma=1`, the same local law holds at the periodic well; the balanced theorem describes the competition with the antiperiodic well.

---

## 2. Periodic soft coordinate

Put

\[
\mu:=2-d=2-2\cos\psi.
\]

For the soft generic arc write

\[
g-\mu=2-2\cos\theta,
\qquad
x=N\theta.
\]

At `psi=0`, let `x^0_{N,m}` be the periodic endpoint soft coordinate. The endpoint Dirichlet theorem and its cubic refinement give

\[
\boxed{
x^0_{N,m}\to\frac\pi2.}
\tag{2.1}
\]

The opposite defect arc is hyperbolic, and because `m->infinity`, its stable consecutive-transfer ratio converges to

\[
\Lambda^{-1}=3-2\sqrt2,
\qquad
\Lambda=3+2\sqrt2.
\tag{2.2}
\]

This limit is independent of the macroscopic ratio as long as `m->infinity`.

---

## 3. Boundary-layer bootstrap

The global macroscopic theorem gives

\[
\Gamma_{N,m,q}=O(N^{-2})
\]

when `gamma<=1`. Subtract the exact hard-divided transfer equation at `(g,mu,x)` from the periodic endpoint equation at `(e^+,0,x^0)`.

The derivative in the soft coordinate is bounded away from zero and converges to

\[
-(1-\Lambda^{-2}).
\]

The hard-ratio perturbation is

\[
O(|g-e^+|+\mu),
\]

while the split soft-pair term is

\[
O(\sqrt\mu).
\]

Hence

\[
|x-x^0|
\le C\bigl(\sqrt\mu+|g-e^+|+\mu+e^{-cm}\bigr).
\tag{3.1}
\]

At a globally improving phase,

\[
g\le e^+,
\]

and the gap identity

\[
g-e^+
=
\mu+
\left(2-2\cos\frac xN\right)
-
\left(2-2\cos\frac{x^0}{N}\right)
\tag{3.2}
\]

implies

\[
\mu
\le \frac C{N^2}|x-x^0|.
\]

Combining this with (3.1) gives

\[
\boxed{
\mu=O(N^{-4}),
\qquad
|x-x^0|=O(N^{-2}),
\qquad
|g-e^+|=O(N^{-4}).
}
\tag{3.3}
\]

Therefore the natural compressed phase scale is

\[
\boxed{|\psi|=O(N^{-2}).}
\]

---

## 4. Universal cusp displacement

Take

\[
\psi=\frac\zeta{N^2}.
\]

Then

\[
N^2\sqrt\mu\to|\zeta|,
\qquad
N^4\mu\to\zeta^2.
\]

After hard-channel normalization, the split soft-pair term is

\[
2\Lambda^{-1}\sqrt\mu+o(N^{-2}).
\]

Linearizing the endpoint equation gives on the improving branch

\[
-(1-\Lambda^{-2})(x-x^0)
=2\Lambda^{-1}\sqrt\mu+o(N^{-2}).
\]

Since

\[
\frac{2\Lambda^{-1}}{1-\Lambda^{-2}}
=\frac1{2\sqrt2},
\]

we obtain

\[
\boxed{
N^2(x-x^0)
\longrightarrow
-\frac{|\zeta|}{2\sqrt2}.
}
\tag{4.1}
\]

---

## 5. Effective parabola

Use (3.2). Since `x^0->pi/2`,

\[
\begin{aligned}
N^4\left[
2-2\cos\frac xN
-\left(2-2\cos\frac{x^0}{N}\right)
\right]
&\longrightarrow
2\left(\frac\pi2\right)
\left(-\frac{|\zeta|}{2\sqrt2}\right)\\
&=-\frac\pi{2\sqrt2}|\zeta|.
\end{aligned}
\]

Together with the phase cost `N^4 mu -> zeta^2`, this proves (1.2).

The limiting potential

\[
V(\zeta)=\zeta^2-rac\pi{2\sqrt2}|\zeta|
\]

has minimizers

\[
\boxed{\zeta=\pm\frac\pi{4\sqrt2}}
\]

and minimum

\[
\boxed{-\frac{\pi^2}{32}.}
\]

---

## 6. Global identification when `gamma<1`

If `gamma<1`, the macroscopic two-well law separates the two endpoint wells at leading order:

\[
e^+_{N,m}
\sim\frac{\pi^2}{4N^2},
\qquad
 e^-_{N,m}
\sim\frac{\pi^2}{4m^2},
\]

and the second quantity is strictly larger by a fixed relative factor. Hence every global maximizer lies in the periodic well for all sufficiently large parameters.

The bootstrap in Section 3 then places it in the `N^-2` boundary layer. Testing the two minimizers of `V` and repeating the subsequence argument from the balanced phase-slip theorem forces every global optimizer to satisfy (1.3), and substitution into (1.2) gives (1.4).

## 7. Interpretation

The second-order behavior has a sharp asymmetry between the two macroscopic wells. Whenever the periodic well is the leading well, its endpoint develops the same avoided-crossing cusp regardless of the macroscopic defect ratio. Thus the phase-slip constants

\[
\frac\pi{4\sqrt2},
\qquad
\frac{\pi^2}{32}
\]

are universal scattering invariants of the hard defect wall, not special constants of the exactly balanced geometry.