# Patch Identification Lemma

## 1. Finite-ring data and canonical line models

Write the finite ring as `Z/nZ` in Hamilton gauge. The step-one edge signs
are `+1` except at one movable seam carrying the Hamilton holonomy
`alpha in {+1,-1}`. The gauge-invariant flux word is

```text
Q_i=tau_i tau_(i+1).
```

The positive entries of `Q` have cyclic gaps four except at exactly
`r in {1,2,3}` marked gaps of length six. For interface `j`, let `p_j` be
the left positive-`Q` endpoint of its length-six gap, and order the `p_j`
cyclically. Put

```text
d_j=p_(j+1)-p_j mod n,   D=min_j d_j,                (1)
```

with `p_(r+1)=p_1`; when `r=1`, set `d_1=D=n`. Thus `d_j` measures the
site distance between consecutive marked G6 cores, not the number of
period-eight cells between them.

The canonical forward G6 flux word on `Z` is

```text
Q_i^(6)=+1  iff  (i<=0 and i=0 mod 4)
                     or (i>=6 and i=6 mod 4),         (2)
```

and is `-1` otherwise. Fix its lift by `tau_0^(6)=1` and
`tau_(i+1)^(6)=Q_i^(6)tau_i^(6)`. The other lift is `-tau^(6)`. The
reflected G6 model is obtained from (2) by reversing the integer coordinate.
After a translation of the reference sector, a reversal, and a diagonal
switching, these are the `A_6` and `H_6=A_6^2` used by the certified
single-interface theorem.

For a subset `E` of the ring, write

```text
E^[k]={i: dist(i,E)<=k}.                              (3)
```

Because `H=A^2` has propagation range four, `E^[4]` is the enlarged support
of a vector supported in `E`. To compare the principal compression of `H`
on `E^[4]`, it is enough to know the step-one/step-two coefficients on
`E^[6]`: every matrix entry of `H` is a sum over one intermediate vertex at
distance at most two from each endpoint.

## 2. The cutoff partition and its patches

Assume `D>=1040` and set

```text
S=floor(D/4),   a=S-8.                               (4)
```

On the oriented arc from `p_j` to `p_(j+1)`, use the coordinate
`t=0,...,d_j`. Define an interface cutoff at each endpoint and one bulk
cutoff `beta_j` on the arc as follows. All cutoffs not displayed in a row
are zero.

```text
0<=t<=a:
    chi_j=1;

a<t<a+S:
    theta=pi(t-a)/(2S),
    chi_j=cos(theta),  beta_j=sin(theta);

a+S<=t<=d_j-a-S:
    beta_j=1;

d_j-a-S<t<d_j-a:
    theta=pi(t-d_j+a+S)/(2S),
    beta_j=cos(theta),  chi_(j+1)=sin(theta);

d_j-a<=t<=d_j:
    chi_(j+1)=1.                                     (5)
```

Endpoint values in (5) agree, so this defines cyclic functions. For `r=1`,
the two endpoint copies of `chi_1` are the same cutoff; equivalently, if
`delta(i)` is cyclic distance from `p_1`, then

```text
chi_1(i)=1                         for delta(i)<=S-8,
        =cos(pi(delta(i)-S+8)/(2S)) for S-8<delta(i)<2S-8,
        =0                         for delta(i)>=2S-8,
beta_1=(1-chi_1^2)^(1/2).                          (6)
```

On every transition, (5) is a sine/cosine pair, and on every plateau one
cutoff equals one. Hence, pointwise on the ring,

```text
sum_j chi_j^2+sum_j beta_j^2=1.                      (7)
```

The cutoff vector follows a unit-circle quarter arc at angular speed
`pi/(2S)` and is constant off the transitions. If two sites have cyclic
distance `h<=4`, subdivision at transition endpoints and the chord bound
give

```text
sum_gamma |gamma(u)-gamma(v)|^2
 <=pi^2 h^2/(4S^2),                                  (8)
```

where `gamma` ranges over all `chi_j` and `beta_j`. Since `H` has range four
and absolute row sum at most 16, the exact double-commutator IMS identity,
together with `pi^2<10`, gives

```text
||E_IMS||
 <=(1/2)*16*(pi^2*4^2/(4S^2))
 <320/S^2.                                           (9)
```

The transition width is exactly `S>=260`. The pure-bulk plateau on arc `j`
is

```text
P_j=[p_j+2S-8, p_(j+1)-2S+8],                      (10)
```

whose length is

```text
d_j-4S+16 >= D-4floor(D/4)+16 >=16.                (11)
```

Let

```text
I_j={i: chi_j(i)!=0},       J_j=I_j^[4],
B_j={i: beta_j(i)!=0},      C_j=B_j^[4].            (12)
```

The `J_j` are the interface patches and the `C_j` are the bulk patches.
The cutoff begins changing at distance `S-8` from `p_j`. Allowing the four
sites used by `H` leaves

```text
L_site=(S-8)-4=S-12,                                (13)
```

which is exactly the tail length used in the exact-`2r` proof.

## 3. Quantitative separation and the holonomy seam

On either side of `p_j`, the nonzero support of `chi_j` ends before distance
`2S-8`. Therefore `J_j` ends before distance `2S-4`, and the coefficient
collar `I_j^[6]` ends before distance `2S-2`. Its forward distance from the
next core's left endpoint and its backward distance from the preceding
core's right endpoint are bounded below by

```text
min(d_j-2S+2, d_(j-1)-2S-4)
 >=D-2floor(D/4)-4 >=516.                           (14)
```

Consequently, neither `J_j` nor `I_j^[6]` can meet a second G6 core. They
are proper arcs of the ring. Similarly, the active support of `beta_j` begins beyond
distance `S-8`. Accounting for the six-site extent of the adjacent abnormal
gap and for the six-site coefficient collar, `B_j^[6]` remains at distance
at least

```text
S-19 >=241                                           (15)
```

from either six-site core. Every coefficient seen by a bulk patch is
therefore a reference-bulk coefficient.

The holonomy sign can be moved by a diagonal switching to any prescribed
step-one edge. Choose arc `j=1`, let `L=p_1+2S-8` be the left endpoint of
`P_1`, and place the seam on the edge

```text
e_seam={L+7,L+8}.                                   (16)
```

By (10), this edge belongs to the plateau `beta_1=1`. The last site on which
the left adjacent interface cutoff is nonzero is at most `L-1`; the first
site on which the right adjacent interface cutoff is nonzero is at least
the right endpoint of `P_1` plus one. At the shortest possible plateau,
that right endpoint is `L+16`. Thus both endpoints of (16) have cyclic
distance at least eight from every interface support. In particular,

```text
e_seam cap I_j^[6]=empty   for every j.             (17)
```

Equation (17) is stronger than the range-four avoidance needed for the
localized quadratic forms. It applies unchanged for `r=1,2,3`. For
`alpha=+1`, (16) is a designated coordinate cut with sign `+1`; for
`alpha=-1`, it carries the unique negative step-one sign. Hence both
holonomies obey the same local identification.

## 4. Patch Identification Lemma

**Lemma (finite-ring patch identification).** For every ring above, every
`r in {1,2,3}`, every choice of forward or reflected orientation at each G6
interface, both tau lift choices (`tau` and `-tau`), and either Hamilton
holonomy, the following statements hold.

1. After cyclic translation, optional reflection, and diagonal switching,
   the principal compression of `H` to each `J_j` is exactly the
   corresponding principal finite section of the canonical infinite G6
   operator `H_6`.
2. Under the same identification, `H` maps vectors supported in `I_j` in
   exactly the same way as `H_6`; its image is supported in `J_j`.
3. Every bulk compression on `C_j`, and every map from vectors supported in
   `B_j` into `C_j`, is exactly a finite section of a translated
   period-eight reference-bulk operator.

**Proof.** Fix an interface `j`. By (14), the coefficient collar `I_j^[6]`
contains exactly one abnormal positive-`Q` gap. If the marked orientation is
forward, translate `p_j` to zero. The positive-`Q` sites in the collar are
then exactly those in (2): all gaps to the left and right are four and the
unique central gap is six. If the marked orientation is reflected, first
reverse the cyclic coordinate and then make the same translation. Thus in
both cases the finite `Q` word in the collar is the restriction of the
appropriate canonical G6 word.

On a proper arc there is no holonomy obstruction. Starting at its leftmost
vertex, choose a diagonal sign and determine successive diagonal signs so
that every step-one edge in the arc becomes positive. This recursion is
consistent because the arc contains no cycle. By (17), the interface collar
does not encounter the globally selected seam. Switching preserves each
triangular flux `Q`, so the transformed step-two signs form a lift of the
canonical word (2).

Two lifts of the same `Q` word on a connected arc differ by one global sign:
if `tau'` and `tau` are lifts, then

```text
(tau'_(i+1)/tau_(i+1))=(tau'_i/tau_i).
```

Hence the transformed coefficients are either `tau^(6)` or `-tau^(6)`.
For `D_0(i)=(-1)^i`, direct substitution gives

```text
A_(-tau)=-D_0 A_tau D_0,
H_(-tau)= D_0 H_tau D_0.                            (18)
```

Thus the remaining lift sign is removed by a diagonal unitary after
squaring. Translation and reflection are permutation unitaries. Their
composition with the two diagonal switchings gives a unitary `U_j` for which

```text
U_j (1_(J_j) H 1_(J_j)) U_j^*
   =1_(Jhat_j) H_6 1_(Jhat_j),                      (19)
```

where `Jhat_j` is the translated or reflected copy of `J_j` on `Z`.
Because `H` has range four, a vector supported in `I_j` has no image outside
`J_j`; the same coefficient comparison proves the corresponding map
identity. This proves statements 1 and 2 for both lifts, orientations, and
holonomies. Cyclic wraparound causes no extra case because `J_j` is a proper
arc and the translation is taken after unwrapping that arc.

For a bulk patch, (15) shows that its coefficient collar contains no
abnormal gap. Its positive-`Q` sites consequently form one congruence class
modulo four. Translation identifies this with one of the four bulk sectors
`B_s`; a diagonal switching fixes the local step-one gauge and (18) removes
the alternative lift. Although `C_1` may contain the selected holonomy seam,
it is still a proper arc, so the same recursive switching moves that sign
outside the compression. The resulting step-two word is a translate of
`tau_ref`. This proves statement 3. `square`

## 5. Transported modes and the complement identity

Choose the canonical normalized G6 modes so that

```text
A_6 psi_+= sqrt(c6) psi_+,
A_6 psi_-=-sqrt(c6) psi_-,
<psi_s,psi_t>=delta_(s,t).                           (20)
```

Extend the diagonal signs occurring in `U_j` from (19) arbitrarily by
`+1` outside the unwrapped collar. This gives a unitary on the full line,
which is used to transport the full pair before any truncation. Translation,
reflection, and diagonal switching preserve the inner product, so the
transported infinite modes `psi_(j,+)` and `psi_(j,-)` are normalized and
orthogonal. On the finite ring define

```text
phi_(j,+)=chi_j psi_(j,+),
phi_(j,-)=chi_j psi_(j,-),                           (21)
```

where the right side means the values of the transported infinite mode on
the unwrapped proper arc `I_j`, followed by multiplication by `chi_j` and
extension by zero to the ring. These are exactly the columns placed in
`Phi` in the Gram argument; no second choice of local gauge or local mode is
made there.

For any finite-ring vector `x`, transport `chi_j x` to the canonical line
and extend it by zero. Since `chi_j` is real and (21) uses the same unitary,

```text
<psi_(j,+/-), chi_j x>_line
   =<chi_j psi_(j,+/-),x>_ring
   =<phi_(j,+/-),x>_ring.                           (22)
```

Consequently, if `x` is orthogonal to all columns in (21), then the local
vector `chi_j x` is orthogonal to the entire rank-two eigenspace
`ker(H_6-c6)`. Equations (19) and (22) therefore apply the certified
single-G6 complement gap to exactly the same local model and exactly the
same pair of modes used in the Gram construction.

For a bulk vector, the same zero-extension argument and statement 3 give

```text
<beta_j x,H beta_j x>
 <=eta ||beta_j x||^2.                              (23)
```

Equations (19), (22), and (23) are the required bridge from the finite-ring
partition to the single-interface and pure-bulk spectral bounds. The lemma
is analytic: the cited producer supplies certified single-interface inputs
but does not independently verify this identification proof.
