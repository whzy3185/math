# Positive-density multi-defect staircase and a uniform spectral gap

Date: 2026-09-15

Status: **Proved**.

This theorem marks a qualitative transition in Paper I.  The optimized two-defect phases have gaps of order `p^-2`; the multi-defect staircase has positive defect density and retains a nonzero limiting gap below the threshold `8`.

---

## 1. Full-period setting

Let the coefficient period `p` be divisible by four and take the half-period jump

\[
s=p/2.
\]

For a legal primitive period-`p` flux word `Q`, write

\[
R_p(Q)=\max_{|z|=1}\rho(H_Q(z))^2.
\]

Define

\[
\boxed{
d(p)=2\left\lfloor\frac{p-4}{8}\right\rfloor.}
\tag{1.1}
\]

The explicit staircase constructions below have exactly `d(p)` positive flux defects.

---

# Theorem A — explicit staircase at every large period divisible by four

There is an explicit primitive legal flux word `Q_p` for every sufficiently large `p` divisible by four such that

\[
\boxed{
\#\{j:Q_{p,j}=+1\}=d(p)
}
\tag{2.1}
\]

and

\[
\boxed{R_p(Q_p)<31/4.}
\tag{2.2}
\]

For the congruence class

\[
p\equiv4\pmod8,
\]

(2.2) holds for every `p>=20`, not merely eventually.

For the class

\[
p\equiv0\pmod8,
\]

it holds for every sufficiently large `p`; in addition it is already proved exactly for

\[
p=24,32,40,48,56,64.
\]

---

## 2. The `8r+4` branch: one `GGGG` dislocation

Let

\[
p=8r+4,
\qquad r\ge2.
\]

Take

\[
Q_j=+1
\iff
j\in\{0,2,\ldots,4r-2\}.
\tag{3.1}
\]

This word has `2r=d(p)` positive defects and primitive period `p`.  Its folded onsite word is

\[
\boxed{G(DDGG)^rG.}
\tag{3.2}
\]

`INFINITE_DDGG_FAMILY_P8R4_THEOREM.md` proves the non-asymptotic bound

\[
\boxed{R_p(Q_p)<31/4}
\]

for every `r>=2`.

Moreover `DDGG_DISLOCATION_ALGEBRAIC_LIMIT.md` proves

\[
\boxed{
R_{8r+4}(Q_{8r+4})\longrightarrow R_\infty,
}
\tag{3.3}
\]

where

\[
\boxed{
R_\infty
=7.70074090635371823740834037867\ldots
}
\tag{3.4}
\]

is the unique root in `(7.7007,7.7008)` of the degree-18 polynomial `P_18` displayed there.

The convergence is exponential in the number of `DDGG` bulk motifs.

---

## 3. The `8r` branch: a centered dual-dislocation pair

Let

\[
p=8r,
\qquad r\ge3.
\]

Put

\[
\ell_r=
\begin{cases}
r,&r\text{ odd},\\r-1,&r\text{ even},
\end{cases}
\]

and define

\[
Q_j=+1
\iff
j\in\{0,2,\ldots,4r-4\}\setminus\{2\ell_r\}.
\tag{4.1}
\]

This word has

\[
2r-2=d(p)
\]

positive defects and primitive period `p`.  Its folded onsite word is

\[
\boxed{
G(DDGG)^{a_r}DDDD\,GG(DDGG)^{b_r}G,
}
\tag{4.2}
\]

with

\[
a_r=\left\lceil\frac{r-2}{2}\right\rceil,
\qquad
b_r=\left\lfloor\frac{r-2}{2}\right\rfloor.
\]

Thus it contains a `GGGG` dislocation and its D/G-dual `DDDD` dislocation, separated by growing uniformly hyperbolic `DDGG` bulk segments.

`CENTERED_DOUBLE_DISLOCATION_P8R_LIMIT.md` proves

\[
\boxed{
R_{8r}(Q_{8r})\longrightarrow R_\infty
}
\tag{4.3}
\]

with exponential convergence.  Hence

\[
R_{8r}(Q_{8r})<31/4
\]

for every sufficiently large `r`.

Exact finite certificates already establish the same inequality for

\[
r=3,4,5,6,7,8.
\]

---

# Theorem B — a nonvanishing asymptotic gap

Along the complete explicit staircase, regardless of the period parity modulo eight,

\[
\boxed{
R_p(Q_p)\longrightarrow R_\infty
\qquad(p\to\infty,\ 4\mid p).
}
\tag{5.1}

Consequently

\[
\boxed{
8-R_p(Q_p)
\longrightarrow
\Delta_\infty:=8-R_\infty
}
\tag{5.2}
\]

with

\[
\boxed{
\Delta_\infty
=0.299259093646281762591659621329\ldots>0.
}
\tag{5.3}
\]

In particular there exists `p_0` such that

\[
\boxed{
8-R_p(Q_p)>1/4
}
\tag{5.4}
\]

for every `p>=p_0` divisible by four.  On the `p=8r+4` branch one may take `p_0=20` within that congruence class.

---

## 4. Positive defect density

From (1.1),

\[
\boxed{
\frac{d(p)}p\longrightarrow\frac14.
}
\tag{6.1}
\]

Thus the uniform gap is produced by a positive-density periodic flux phase, not by a bounded number of local defects.

In folded language, the limiting bulk is exactly the alternating four-site motif

\[
\boxed{DDGG.}
\]

The finite-period parity is encoded only by one `GGGG` dislocation or by a dual `GGGG/DDDD` pair.

---

# Theorem C — strict asymptotic separation from the complete two-defect family

Let

\[
R^{(2)}_p
\]

be the minimum edge over the complete reflection-chiral two-defect family of period `p`.

The optimized two-defect theory gives

\[
\boxed{
8-R^{(2)}_p=\Theta(p^{-2}),
}
\tag{7.1}
\]

so

\[
R^{(2)}_p\to8.
\]

By contrast, (5.1) gives

\[
R_p(Q_p)\to R_\infty<8.
\]

Therefore

\[
\boxed{
R^{(2)}_p-R_p(Q_p)
\longrightarrow
8-R_\infty
=\Delta_\infty>0.
}
\tag{7.2}
\]

Hence the multi-defect staircase beats the complete two-defect family by an **order-one spectral amount** in the large-period limit.

This is much stronger than the finite rational-separator comparisons at periods `20--64`.

---

## 5. Consequence for the full periodic variational problem

Let

\[
M_p=\min_{\text{all legal primitive period-}p\text{ flux words}}R_p(Q).
\]

Since `Q_p` is an admissible word,

\[
M_p\le R_p(Q_p).
\]

Thus

\[
\boxed{
\limsup_{\substack{p\to\infty\\4\mid p}}M_p
\le R_\infty<8.
}
\tag{8.1}
\]

The full-class optimum therefore stays uniformly below the threshold along all sufficiently large periods divisible by four.

This conclusion is independent of whether the staircase phases themselves are eventually globally optimal in the complete periodic class.

---

## 6. Structural interpretation

The paper now contains two genuinely different spectral regimes.

### Sparse-defect regime

A bounded number of defects produces

\[
8-R=\Theta(p^{-2}),
\]

with Robin/Dirichlet and phase-slip asymptotics.

### Positive-density regime

The `DDGG` bulk has defect density `1/4` and supports a uniform hyperbolic gap.  Local `GGGG/DDDD` dislocations create bound states at the algebraic edge `R_infty`, while the bulk itself remains uniformly hyperbolic at `31/4`.

Thus the defect-number staircase is a true **spectral phase transition from sparse scattering to periodic bulk order**.