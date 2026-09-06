# Linear-scale finite comparison threshold

Date: 2026-09-06.

This note combines the new quadratic Bloch gap with the alternating-signing
lower estimate already proved in the previous workstream.

For even `s>=2`, let `N=4sL` and repeat the primitive period-`4s` antipodal
word.  For either target holonomy,

\[
 \rho(A_{s,L,\alpha})^2
 \le 8-\frac{1}{6s(s+2)}.
 \tag{1}
\]

For the alternating negative-holonomy signing the previous proof gives

\[
 \rho(A^{\rm alt}_{N,s,-})^2
 \ge 8-\frac{4\pi^2(1+s^2)}{N^2},
 \tag{2}
\]

while the positive alternating sector has squared radius exactly `8`.

Therefore the explicit antipodal signing is strictly better than both
alternating holonomies whenever

\[
 \frac{4\pi^2(1+s^2)}{N^2}
 <\frac{1}{6s(s+2)}.
\]

Equivalently,

\[
 \boxed{N>2\pi\sqrt{6s(s+2)(1+s^2)}.}
 \tag{3}
\]

Since `N=4sL`, a convenient period-count condition is

\[
 \boxed{
 L>\pi\sqrt{\frac{3(s+2)(1+s^2)}{2s}}.
 }
 \tag{4}
\]

Thus the sufficient repetition threshold is now linear in `s`:

\[
 L=O(s),
\]

instead of the previous `O(s^{3/2})` bound coming from the cubic gap lower
estimate.

The threshold remains a sufficient comparison bound, not a sharp transition
value.  At small jumps, especially `s=2`, the exact frozen formulas are much
stronger.
