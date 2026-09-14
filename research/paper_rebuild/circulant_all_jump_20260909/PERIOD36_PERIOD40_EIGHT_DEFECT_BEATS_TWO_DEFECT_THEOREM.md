# Periods thirty-six and forty: eight-defect phases beat the complete two-defect family

Date: 2026-09-14

Status: **Proved**.

These two layers continue the multi-defect staircase:

\[
4,4,6,6,8,8
\]

explicit positive-flux defects at periods

\[
20,24,28,32,36,40.
\]

The theorem uses the same rational separator

\[
y_0=31/4.
\]

---

# Theorem A — period thirty-six

Take

\[
p=36,
\qquad s=18,
\]

and let `Q_36` have positive sites

\[
\boxed{\{0,2,4,6,8,10,12,14\}}.
\]

Then

\[
\boxed{
R(Q_{36})<31/4<R^{(36)}_{\rm 2def},
}
\tag{1.1}
\]

where `R_2def^(36)` is the minimum edge over the complete reflection-chiral two-defect family.

## Proof

At `y_0=31/4`, sparse determinant elimination gives

\[
\det(y_0I-H_{Q_{36}}(z)^2)
=
\frac{F_{36}(z)^2}{2^{72}z^{36}},
\]

with `F_36` palindromic of degree `36`.  Put `c=z+z^{-1}`. Then

\[
F_{36}(z)/z^{18}=f_{36}(c),
\]

where the coefficients of `f_36`, from `c^18` to the constant term, are

\[
\begin{aligned}
(&68719476736,-515396075520,-3603477561344,33243046871040,\\
&72092099805184,-934194578456576,-542738307088384,\\
&14938672101064704,-2988104027734016,-148669729384431616,\\
&98137395291881472,942868590013710336,-906289997598015488,\\
&-3721197956673904640,4364030009919411200,8355780413586619392,\\
&-11108675538316890224,-8172795949684775032,11855834411999146945).
\end{aligned}
\]

The exact Sturm count is

\[
\#\{c\in[-2,2]:f_{36}(c)=0\}=0.
\]

At `z=1`, every leading principal minor of

\[
31I-4H_{Q_{36}}(1)^2
\]

is positive. Hence the reference fiber lies below `31/4`; absence of test-energy crossings implies the whole Bloch family lies below it.

For period `36=8\cdot4+4`, the fixed-period two-defect theorem gives the unique two-defect optimum `(N,m)=(5,4)`. At its `z=1` fiber, the nineteenth leading principal minor of

\[
31I-4H^2
\]

is

\[
\boxed{-3024238794325721<0.}
\]

Thus its edge is above `31/4`, proving (1.1).

A corrected Hermitian computation gives the orientation value

\[
R(Q_{36})\approx7.70109,
\]

but this decimal is not used in the proof.

---

# Theorem B — period forty

Take

\[
p=40,
\qquad s=20,
\]

and let `Q_40` have positive sites

\[
\boxed{\{0,2,4,6,8,12,14,16\}}.
\]

Then

\[
\boxed{
R(Q_{40})<31/4<R^{(40)}_{\rm 2def}.
}
\tag{2.1}
\]

## Proof

Again

\[
\det(y_0I-H_{Q_{40}}(z)^2)
=
\frac{F_{40}(z)^2}{2^{80}z^{40}},
\]

with `F_40` palindromic.  Writing

\[
F_{40}(z)/z^{20}=f_{40}(c),
\]

the coefficients of `f_40`, from `c^20` to the constant term, are

\[
\begin{aligned}
(&1099511627776,0,-106240311033856,0,4463660726484992,\\
&4398046511104,-107600714007576576,-225674761601024,\\
&1652116975599484928,4961700839161856,-16919973680174333952,\\
&-60533291618402304,117259483996379807744,441876573063217152,\\
&-543690052838107873280,-1925242607286353920,\\
&1615543145385448058112,4619183128931205120,\\
&-2779596019692912386208,-4683480396175491072,\\
&2103606531822207433601).
\end{aligned}
\]

The exact Sturm count is zero on `[-2,2]`. At `z=1`, every leading principal minor of

\[
31I-4H_{Q_{40}}(1)^2
\]

is positive, so the whole Bloch family lies below `31/4`.

The unique best two-defect phase at period forty is balanced `(N,m)=(5,5)`. At `z=-1`, the thirteenth leading principal minor of

\[
31I-4H^2
\]

is

\[
\boxed{-31096761<0,}
\]

forcing its squared edge above `31/4`. This proves (2.1).

A corrected high-resolution Hermitian scan gives

\[
R(Q_{40})\approx7.69987,
\]

again only for orientation.

---

## 3. Consequence: a persistent defect-number staircase

We now have rigorous explicit improvements over the complete two-defect family at six consecutive layers:

\[
\begin{array}{c|c}
p&\text{defect count of the proved improving phase}\\ \hline
20&4\\
24&4\\
28&6\\
32&6\\
36&8\\
40&8.
\end{array}
\]

The counts fit exactly

\[
\boxed{
d(p)=2\left\lfloor\frac{p-4}{8}\right\rfloor.}
\]

At present this formula is a **proved description of the six explicit constructions above**, not yet a theorem that the same pattern continues or that these constructions are globally optimal.

The repeated two-layer plateaus strongly motivate an infinite multi-block scattering construction.