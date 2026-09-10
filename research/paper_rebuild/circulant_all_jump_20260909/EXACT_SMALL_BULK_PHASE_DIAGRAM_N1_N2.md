# Exact finite phase diagrams for complementary bulk lengths `N=1,2`

Date: 2026-09-10

Status: **Proved**. This note belongs only to Paper I.

We use the general even-separation two-defect family with

\[
L=2(N+m),\qquad h=2m,
\]

and the compact threshold formula

\[
P_{N,m,z}(8)=\mathcal F_{N,m}(d)-e,
\qquad d,e\in[-2,2].
\]

The purpose of this note is to close the first two finite complementary-bulk layers exactly.

## Theorem A — exact phase diagram for `N=1`

For `N=1`, the full Bloch spectrum is strictly below the squared threshold `8` if and only if

\[
\boxed{m=1.}
\]

Equivalently, in geometric variables, among the `N=1` family only

\[
(L,h)=(4,2)
\]

is globally sub-eight.

### Proof

For `m\ge2`, the exact antiperiodic formula gives

\[
P_{1,m,-1}(8)=4\bigl(T_1(3)^2-4m^2\bigr)
=4(9-4m^2)<0.
\]

Since the squared characteristic polynomial is

\[
P_{1,m,-1}(8)=\prod_j(8-y_j),\qquad y_j\ge0,
\]

at least one squared eigenvalue is larger than `8`.

For `m=1`, direct substitution into the compact threshold formula gives

\[
\mathcal F_{1,1}(d)-2
=d^4-20d^2+4d+88.
\]

Set

\[
t=\frac{d+2}{4}\in[0,1].
\]

Then

\[
\mathcal F_{1,1}(-2+4t)-2
=16\bigl(16t^4-32t^3+4t^2+13t+1\bigr).
\]

In the degree-four Bernstein basis

\[
B_{k,4}(t)=\binom4k t^k(1-t)^{4-k},
\]

this is

\[
16B_{0,4}+68B_{1,4}
+\frac{392}{3}B_{2,4}
+76B_{3,4}+32B_{4,4}.
\]

Every coefficient is positive, hence

\[
\mathcal F_{1,1}(d)>2
\qquad(-2\le d\le2).
\]

Since `e\le2`, we have `P_{1,1,z}(8)>0` for every Bloch phase. The endpoint fiber is already known to be strictly sub-eight. Continuous inertia on the unit circle therefore gives

\[
\rho(H_{1,1}(z))^2<8
\]

for every `z`. This proves the theorem.

---

## Theorem B — exact phase diagram for `N=2`

For `N=2`, the full Bloch spectrum is strictly below `8` if and only if

\[
\boxed{1\le m\le8.}
\]

Thus the exact transition is between `m=8` and `m=9`.

### Proof: obstruction for `m\ge9`

Since

\[
T_2(3)=17,
\]

the antiperiodic determinant is

\[
P_{2,m,-1}(8)
=4(17^2-4m^2).
\]

For `m\ge9`, this is negative. Hence a squared eigenvalue exceeds `8` at `z=-1`.

### Proof: safe range `1\le m\le4`

The exponential safe-region theorem gives

\[
m\le\frac23U_{N-1}(3).
\]

For `N=2`,

\[
U_1(3)=6,
\]

so every `m\le4` is globally sub-eight.

### Proof: exact Bernstein certificates for `m=5,6,7,8`

For the remaining four cases set again

\[
t=(d+2)/4.
\]

Let

\[
f_m(t)=\mathcal F_{2,m}(-2+4t)-2.
\]

Its degree is `2m+4`. Expanding in the Bernstein basis of that degree,

\[
f_m(t)=\sum_{k=0}^{2m+4}b_{m,k}B_{k,2m+4}(t),
\]

all coefficients are strictly positive. The exact coefficient vectors are as follows.

For `m=5` (degree 14):

\[
\begin{aligned}
(b_{5,k})={}&(752,9056,6012672/91,29804912/91,182044464/143,\\
&4133406720/1001,1045892384/91,11887810736/429,\\
&173092864400/3003,101777709216/1001,147395387072/1001,\\
&15207832880/91,13086142256/91,635287488/7,45239072).
\end{aligned}
\]

For `m=6` (degree 16):

\[
\begin{aligned}
(b_{6,k})={}&(576,10356,1414424/15,19609956/35,235623536/91,\\
&911419468/91,33643560248/1001,71236068052/715,\\
&1691242276384/6435,440766983196/715,1275716296136/1001,\\
&622625485676/273,312110652624/91,145579604364/35,\\
&58739078632/15,2753898844,1536796800).
\end{aligned}
\]

For `m=7` (degree 18):

\[
\begin{aligned}
(b_{7,k})={}&(368,101696/9,19301024/153,14885072/17,3573274576/765,\\
&22287285856/1071,124812340288/1547,184623784912/663,\\
&18958288087760/21879,2702130401536/1105,137023115833888/21879,\\
&3202476516944/221,139147826160208/4641,8339273726048/153,\\
&64821544096256/765,5535043853648/51,16842910722160/153,\\
&763702687936/9,52205852192).
\end{aligned}
\]

For `m=8` (degree 20):

\[
\begin{aligned}
(b_{8,k})={}&(128,59088/5,15271168/95,121721264/95,2205296128/285,\\
&2213986832/57,48335975296/285,12559524592/19,\\
&147129536289152/62985,158610450583472/20995,79838319815168/3553,\\
&1292232065103088/20995,9757485278996224/62985,1725637772583248/4845,\\
&3585671152116352/4845,1324374492789200/969,10602073280606336/4845,\\
&278874786311536/95,301328050413312/95,13231422563728/5,\\
&1773462177792).
\end{aligned}
\]

All listed rational numbers are positive. Therefore

\[
\mathcal F_{2,m}(d)-2>0
\]

for every `d\in[-2,2]` and `m=5,6,7,8`. Since `e\le2`,

\[
P_{2,m,z}(8)>0
\]

for every Bloch phase. Endpoint sub-eight positivity and connected-inertia propagation complete the proof.

---

## Corollary — the antiperiodic threshold is exact in the first two layers

For `N=1,2`,

\[
\boxed{
\text{global sub-eight}
\iff
2m<T_N(3).
}
\]

Indeed `T_1(3)=3` and `T_2(3)=17`, giving exactly `m\le1` and `m\le8`.

This is the first finite evidence, now fully proved rather than computationally observed, for the general exact criterion

\[
2m<T_N(3).
\]

No claim for arbitrary `N` is made in this note.