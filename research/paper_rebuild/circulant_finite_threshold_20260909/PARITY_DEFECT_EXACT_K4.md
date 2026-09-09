# Parity defect and the exact `N=4s` resonance family

This note is self-contained and belongs to the finite-global paper.  It makes no use of any continuous Bloch/Floquet result.

Throughout, `2 <= s < N/2`, `G=C_N(1,s)`, `A=A_sigma` is an arbitrary signed adjacency matrix, and

\[
B:=A^2-4I.
\]

Thus

\[
\rho(A)^2=4+\lambda_{\max}(B).
\]

The diagonal of `B` is zero and all entries of `B` are integers.

## 1. A fixed parity support for every signing

Let `A_0` be the ordinary unsigned adjacency matrix of `C_N(1,s)`.  Since every nonzero entry of `A` is `+-1`,

\[
A\equiv A_0 \pmod 2,
\qquad
B\equiv A_0^2 \pmod 2.
\]

Identify the group algebra of `Z_N` over `F_2` with

\[
\mathbb F_2[x,x^{-1}]/(x^N-1).
\]

The first row of `A_0` corresponds to

\[
p=x+x^{-1}+x^s+x^{-s}.
\]

In characteristic two, Frobenius squaring gives

\[
p^2=x^2+x^{-2}+x^{2s}+x^{-2s}. \tag{1}
\]

Because `2 <= s < N/2`, the only possible collisions among the four exponents in (1) are the following.

- `2 \equiv -2s (mod N)` (equivalently `-2 \equiv 2s`) iff `N=2s+2`;
- `2s \equiv -2s (mod N)` iff `N=4s`.

Indeed, the first congruence says `N | 2s+2`, while `N>2s`, so it forces `N=2s+2`; the second says `N | 4s`, and any proper divisor of `4s` is at most `2s`, so `N>2s` forces `N=4s`.  The congruences `2\equiv2s` and `-2\equiv-2s` are impossible because `0<2(s-1)<N`.

Therefore the support of `B` modulo two is completely independent of the signing:

\[
\operatorname{supp}(B\bmod2)=
\begin{cases}
\varnothing, & N=2s+2,\\[2mm]
\operatorname{Cay}(\mathbb Z_N,\{\pm2\}), & N=4s,\\[2mm]
\operatorname{Cay}(\mathbb Z_N,\{\pm2,\pm2s\}), & \text{otherwise}.
\end{cases} \tag{2}
\]

We call (2) the **parity-defect trichotomy**.  It is useful because any entry on the displayed support is odd, while every other off-diagonal entry is even.

The first line explains why the trace bound can be flat only on `N=2s+2`.  The second line is the key to a new exact resonance theorem.

## 2. Exact global extremum on `N=4s`

### Theorem

For every integer `s>=2`,

\[
\boxed{
 m(4s,s)^2=4+2\cos\frac{\pi}{2s}.
} \tag{3}
\]

Moreover, the minimizers form exactly two labelled switching classes.  In Hamilton gauge these are the two choices

\[
D=\varepsilon\,\operatorname{diag}(1,-1,1,-1,\ldots),
\qquad \varepsilon\in\{\pm1\},
\]

with anti-periodic step-one holonomy `alpha=-1`; one-step rotation exchanges the two classes.

### Proof: universal lower bound

Fix an arbitrary signing of `C_{4s}(1,s)` and put

\[
M:=\lambda_{\max}(B).
\]

Set

\[
c_s:=2\cos\frac{\pi}{2s}.
\]

Since `s>=2`,

\[
\sqrt2\le c_s<2.
\]

If `M>=2`, then certainly `M>=c_s`.  It remains to consider `M<2`.

For any off-diagonal entry `b_ij`, the principal submatrix on `{i,j}` is

\[
\begin{pmatrix}0&b_{ij}\\b_{ij}&0\end{pmatrix},
\]

whose largest eigenvalue is `|b_ij|`.  Interlacing therefore gives

\[
|b_{ij}|\le M<2.
\]

As `b_ij` is integral, every off-diagonal entry is in `{0,+-1}`.

On `N=4s`, (2) says that the entries at displacement `+-2` are odd and every other off-diagonal entry is even.  Hence, under `M<2`,

- every displacement-`+-2` entry is exactly `+-1`;
- every other off-diagonal entry is zero.

Thus the support of `B` is exactly

\[
\operatorname{Cay}(\mathbb Z_{4s},\{\pm2\}),
\]

which is the disjoint union of the even and odd cycles, each of length `2s`.

A signed cycle of length `L` is, up to switching, determined by its cycle sign.  If it is balanced, its largest eigenvalue is `2`.  If it is unbalanced, its eigenvalues are

\[
2\cos\frac{(2j+1)\pi}{L},\qquad j=0,\ldots,L-1,
\]

and hence its largest eigenvalue is

\[
2\cos\frac{\pi}{L}.
\]

With `L=2s`, every component of `B` therefore has largest eigenvalue at least `c_s`.  Consequently

\[
M\ge c_s,
\]

and for every signing

\[
\rho(A)^2=4+M\ge4+2\cos\frac{\pi}{2s}. \tag{4}
\]

### Proof: finite construction attaining the bound

We now construct a finite signing attaining (4).

Switch the step-one Hamilton cycle into signed-shift form.  Let `T` be the signed cyclic shift satisfying

\[
T^{4s}=-I,
\]

and let

\[
D=\operatorname{diag}((-1)^j)_{j\in\mathbb Z_{4s}}.
\]

Since `4s` is even,

\[
DT=-TD.
\]

Define the signed adjacency matrix

\[
A=T+T^{-1}+DT^s+T^{-s}D. \tag{5}
\]

The first two terms give the signed step-one edges and the last two give one sign on every step-`s` edge, so (5) is a signing of `C_{4s}(1,s)`.

Put `P=T+T^{-1}` and `Q=DT^s+T^{-s}D`.  The anticommutation relation gives

\[
PQ+QP=0,
\]

and direct multiplication gives

\[
P^2=2I+T^2+T^{-2},
\]

\[
Q^2=2I+(-1)^s(T^{2s}+T^{-2s}).
\]

Because `T^{4s}=-I`,

\[
T^{-2s}=-T^{2s}.
\]

Therefore the last two terms cancel and

\[
A^2=4I+T^2+T^{-2}. \tag{6}
\]

The eigenvalues of `T` are the `4s` roots of `z^{4s}=-1`, namely

\[
z_k=e^{(2k+1)\pi i/(4s)},\qquad 0\le k<4s.
\]

By (6), the squared eigenvalues of `A` are

\[
4+z_k^2+z_k^{-2}
=4+2\cos\frac{(2k+1)\pi}{2s}.
\]

Their maximum is

\[
4+2\cos\frac{\pi}{2s}.
\]

Together with (4), this proves (3).

### Proof: switching rigidity of the minimizers

Suppose equality holds in (3).  Since `c_s<2`, the lower-bound argument shows that

\[
B=A^2-4I
\]

has no off-diagonal entries outside displacement `+-2`; its two parity components are unbalanced signed `2s`-cycles.

Normalize the step-one Hamilton path and write the signing in the signed-shift form

\[
A=T+T^{-1}+DT^s+T^{-s}D,
\qquad
D=\operatorname{diag}(d_0,\ldots,d_{4s-1}),\quad d_i\in\{\pm1\},
\]

where `T^{4s}=alpha I`, `alpha in {+-1}`.  The displacement `s+1` channel of `A^2` is the sum of the two mixed two-walks obtained in the orders `(1,s)` and `(s,1)`.  Since this displacement is not `+-2` for `s>=2`, equality forces that channel to vanish at every vertex.  After factoring the common signed step path, the condition is

\[
d_{i+1}+d_i=0\qquad(i\bmod4s).
\]

Hence

\[
d_i=\varepsilon(-1)^i
\]

for a unique `epsilon in {+-1}`, equivalently `DT=-TD`.

With this relation the same multiplication as above yields

\[
B=T^2+T^{-2}+(-1)^s(T^{2s}+T^{-2s}).
\]

Since `T^{4s}=alpha I`,

\[
T^{-2s}=\alpha T^{2s}.
\]

The equality support contains no displacement-`2s` term, so

\[
1+\alpha=0,
\]

that is,

\[
\alpha=-1.
\]

Thus Hamilton gauge leaves exactly the two possibilities `epsilon=+-1`.  A one-step rotation changes the alternating diagonal by a global sign and therefore exchanges the two labelled switching classes.  This completes the rigidity statement.

## 3. Consequences for the low-end hierarchy

Taking `s=2` in (3) gives

\[
m(8,2)^2=4+\sqrt2.
\]

More generally, the exact `N=4s` sequence is

\[
4+2\cos\frac{\pi}{2s},\qquad s=2,3,\ldots,
\]

which increases monotonically to `6`.

The first values are

\[
\begin{aligned}
m(8,2)^2&=4+\sqrt2,\\
m(12,3)^2&=4+\sqrt3,\\
m(16,4)^2&=4+\sqrt{2+\sqrt2}.
\end{aligned}
\]

This line is a genuine finite-global result: the lower bound quantifies over every signing, and the upper bound is supplied by a single finite anti-periodic construction.  No restriction to periodic signings and no continuous quasi-momentum maximization is involved.

## 4. Unified structural interpretation

The parity-defect trichotomy (2) explains three otherwise separate phenomena.

1. **Flat line `N=2s+2`.**  All mandatory parity defects cancel; this is the only place where `B=0` can occur.
2. **Exact resonance line `N=4s`.**  Half of the mandatory defect directions cancel, leaving two forced signed cycles that can be optimized exactly.
3. **Generic parameters.**  Four mandatory directions survive.  At the very bottom of the spectrum, the only way their signed support can collapse to negative cliques produces the exceptional `sqrt(5)` pairs `(5,2)` and `(10,3)`.

This should be elevated to the main structural engine of the low-end part of the manuscript rather than presented as a technical parity observation.
