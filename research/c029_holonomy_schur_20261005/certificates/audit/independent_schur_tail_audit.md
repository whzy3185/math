# Independent audit: normalized residue-two Schur tail

Date: 2026-10-05. Source snapshot: `analytic-proof-first@7b6a351cc5f8f83f5527b7fc547f0a865ea50cf2`.

## Result and scope

**Final audit status: PASS.** The final companion proof `../analytic/R2_ANALYTIC_TAIL_CLOSURE.md` was line-audited with no remaining gap in its stated explicit-family theorem. All finite premises were also independently replayed using the full signed graph and sparse scalar Schur elimination, without constructing the entrance by the four-site response recurrence. See `direct_graph_seed_replay.json` and `direct_graph_local_replay.json`, with their companion replay scripts. The second replay extracts X_24, R_24, W_24 after 96 scalar eliminations at n=106, then verifies all local P/Q, residual, and response inequalities by exact symbolic arithmetic. This is independent mathematical and exact-arithmetic audit, not external peer review or proof-assistant formalization.

The following is an analytic tail proof, conditional only on the finite exact entrance and local-certificate inequalities explicitly listed below. It does not use numerical convergence as proof. It repairs the boundary terms and norm conventions of the historical tail draft.

Under these finite premises, every even-length core with `m >= 26` is within `1/500` in spectral norm of one fixed limiting 6-by-6 core. At `m >= 102` the sharper bound is less than `10^-9`. Consequently a verified normalized 6-by-6 seed with margin `1/50` at any even `m >= 26` implies positivity of all even `m >= 26`, with lower margin `2/125`. Remaining orders are `n = 50, 58, 66, 74, 82, 90, 98`.

The historical 9/20 margin must not be copied: fresh testing found the normalized 6-by-6 n=410 core does not exceed even (1/20)I. The historical seed verifier does **not** supply the required seed: it retains a different 8-by-8 core of the unnormalized matrix `198 I - 25 A^2`. A fresh normalized 6-by-6 seed is necessary.

## 1. Exact indexing, dimensions, and boundary identity

Set `n=4m+2`, with `m=2k` even. Retain the two vertices in `V_0` and the four vertices in `V_m`. Eliminate `V_1,...,V_(m-1)` in that order. The normalized matrix is `M=(198/25)I-A^2`.

Use zero-based elimination index `t`: `t=0` refers to pivot `V_1`, and the terminal pivot is

`p=m-2`.

Thus `p` is even. Let `E_t=E_+` for even `t` and `E_t=E_-` for odd `t`. All quantities below belong to a single length-independent infinite open-chain recurrence, until its terminal correction is inserted.

Dimensions are `X_t,E_t,W_t: 4x4`, `R_t,C_t: 2x4`, `G_t:2x2`, and `H_t:4x4`. Initial data are

```
D = [[98/25,0,-1,0], [0,98/25,0,-1],
     [-1,0,98/25,0], [0,-1,0,98/25]]
E_+ = [[-1,0,0,0], [0,1,0,0], [-1,2,1,0], [2,-1,0,-1]]
E_- = [[-1,0,0,0], [0,1,0,0], [-1,-2,1,0], [-2,-1,0,-1]]
X_0=D
R_0=[[-1,-2,1,0], [-2,-1,0,-1]]
W_0=[[0,0,-1,0], [0,0,0,1], [0,0,0,0], [0,0,0,0]]
G_0=(98/25)I_2, H_0=D
C_0=[[-1,0,-1,0], [0,-1,0,-1]]
```

Define the open recurrence

```
X_(t+1)=D-E_t^T X_t^-1 E_t
R_(t+1)=-R_t X_t^-1 E_t
W_(t+1)=-E_t^T X_t^-1 W_t.
```

Set

```
g_t=R_t X_t^-1 R_t^T,
h_t=W_t^T X_t^-1 W_t,
c_t=R_t X_t^-1 W_t.
```

The exact terminal core is

```
G(m)=G_0 - sum_(t=0)^p g_t
H(m)=H_0 - sum_(t=0)^p h_t
     - W_p^T X_p^-1 E_+ - E_+^T X_p^-1 W_p
     - E_+^T X_p^-1 E_+
C(m)=C_0 - sum_(t=0)^p c_t - R_p X_p^-1 E_+
S_m=[[G(m),C(m)],[C(m)^T,H(m)]].
```

This follows directly by Schur elimination with `W_p+E_+` at the terminal step. In particular, replacing only the terminal H entry is incorrect: the off-diagonal C entry has its own linear correction.

After 24 eliminations the open pivot is `X_24=Phi^12(D)`, where `Phi=F_- o F_+`. At `m=102`, `p=100=24+2*38`. This proves the claimed 38 complete transfers without a parity ambiguity.

## 2. Finite certificate premises

Write `r=10^-10`, `q=2/3`, `theta=4/9`. Let `Z=X_24` and `Y=F_+(Z)`.

The necessary exact finite premises are:

1. All preceding pivots are positive, and `Z,Y > (1/2)I`.
2. Positive rational weights P and Q satisfy `(9/10)I <= P,Q <= 2I`.
3. For `L=Z^-1 E_+ Y^-1 E_-`, `L^T P L < (2/5)P` and `L Q L^T < (2/5)Q`.
4. `||Phi(Z)-Z||_F < r/40`.
5. `R_24 Q R_24^T < 10^-10 I_2` and `W_24^T Q W_24 < 10^-10 I_4`.

The old 10-coordinate Lyapunov derivative estimates are unnecessary. The order-unit P norm proves the local result directly, as follows.

## 3. Audit of the order-unit local proof

For symmetric H use `||H||_(P,ord)=||P^-1/2 H P^-1/2||_2`. On the ball of radius r about Z in this norm, `||X-Z||_2 <= 2r=:e`.

The inverse norm at the centers is at most 2. Since `e<1/6`, `X >= I/3` and `||X^-1||_2 <= 3`. The inverse identity gives `||X^-1-Z^-1||_2 <= 6e`. Both E matrices have squared Frobenius norm 14. Hence, with `Y(X)=F_+(X)`,

```
||Y(X)-Y||_2 <= 84e < 1/6
||Y(X)^-1||_2 <= 3
||Y(X)^-1-Y^-1||_2 <= 504e.
```

The two-cell transfer is `L(X)=X^-1 E_+ Y(X)^-1 E_-`. Expanding its difference in two terms gives

`||L(X)-L(Z)||_2 <= 14*(6*3+2*504)e = 14364e`.

For either the P column norm or the Q row norm, norm conversion costs at most `sqrt(20/9)<3/2`. Consequently the transfer perturbation is less than `21546e=43092r<10^-4`.

Since `sqrt(2/5)+10^-4<2/3`, throughout this ball

```
L(X)^T P L(X) < q^2 P,
L(X) Q L(X)^T < q^2 Q.
```

The exact derivative is `D Phi(X)[H]=L(X)^T H L(X)`. If `-aP<=H<=aP`, conjugation therefore yields `-a q^2 P <= D Phi(X)[H] <= a q^2 P`. This proves contraction by `theta=q^2=4/9` in the order-unit norm.

The center residual has order-unit norm less than `r/36`, so the ball is invariant because `1/36+4/9=17/36<1`. Banach's theorem supplies a fixed point `X_*` and, conservatively,

`||X_(24+2h)-X_*||_2 <= 4r theta^h`.

All even local and intermediate odd pivots have inverse norm at most 3, including `X_*`.

## 4. Correct response norm orientation

Avoid writing an undefined induced “Q norm.” Define explicitly

```
alpha(R)=||R Q^(1/2)||_2=sqrt(||R Q R^T||_2),
beta(W)=||Q^(1/2) W||_2=sqrt(||W^T Q W||_2).
```

Over two cells, `R -> R L(X)` and `W -> L(X)^T W`. The inequality `L Q L^T <= q^2 Q` proves contraction by q in both alpha and beta. The P inequality alone would not establish this orientation.

The entrance premises and `Q >= (9/10)I` give, for `h>=0`,

`||R_(24+2h)||_2, ||W_(24+2h)||_2 < a q^h`, with `a=1/30000`.

Indeed, the sharper common bound is `sqrt(10/9)*10^-5 q^h < a q^h`.

Each one-cell transfer has spectral norm at most `3*sqrt(14)<12`, so both intermediate responses satisfy

`||R_(25+2h)||_2, ||W_(25+2h)||_2 < b q^h`, with `b=12a=1/2500`.

The weaker b bound also holds at the even member of the pair.

## 5. Exact limiting core and explicit tail estimate

The response bounds show absolute norm convergence of each series of g, h, c. Define

```
G_inf=G_0-sum_(t>=0) g_t,
H_inf=H_0-sum_(t>=0) h_t-E_+^T X_*^-1 E_+,
C_inf=C_0-sum_(t>=0) c_t,
S_inf=[[G_inf,C_inf],[C_inf^T,H_inf]].
```

These definitions use the actual infinite pivot trajectory. There are no pivot-inverse perturbations inside the series: comparing a finite core with this limit cancels the common initial terms exactly.

Take an even m with `p=m-2=24+2h`, `h>=0`. Each individual remaining quadratic or mixed increment has norm at most `3b^2 q^(2l)` in pair l. Counting **both** members of every pair gives the common series-tail majorant

`T_h = 6 b^2 q^(2h)/(1-q^2)`.

This also bounds the actual suffix starting just after p; it harmlessly includes one extra term at p.

Terminal linear and inverse-limit terms satisfy

```
||R_p X_p^-1 E_+||_2 <= 12a q^h,
||W_p^T X_p^-1 E_+ + E_+^T X_p^-1 W_p||_2 <= 24a q^h,
||E_+^T(X_p^-1-X_*^-1)E_+||_2 <= 16*9*(4r) theta^h
                                                =576r theta^h.
```

Here `||E_+||_2<4` and the inverse identity contributes the factor 9. Thus

```
||G(m)-G_inf||_2 <= T_h,
||C(m)-C_inf||_2 <= T_h+12a q^h,
||H(m)-H_inf||_2 <= T_h+24a q^h+576r theta^h.
```

Using the conservative block bound `||[[G,C],[C^T,H]]||_2 <= ||G||_2+2||C||_2+||H||_2`, we obtain the fully explicit analytic estimate

`||S_m-S_inf||_2 <= B_h := 4T_h+48a q^h+576r theta^h`.

At h=0 all constants are rational and

`B_0 = 0.0016069696 < 1/500`.

Every term decreases with h, proving the uniform bound for every even `m>=26`. At h=38, using even the weaker `theta<=q`, exact rational arithmetic gives

`B_38 < 3.256*10^-10 < 10^-9`.

Thus the historical intended `10^-6` bound follows with ample slack once the exact premises pass.

## 6. Seed transfer and finite completion

Let `S_(m0) > (1/50)I_6` be a freshly verified normalized 6-by-6 core with even `m0>=26`. Then for any even `m>=26`,

`||S_m-S_(m0)||_2 <= ||S_m-S_inf||_2+||S_(m0)-S_inf||_2 < 2/500=1/250`.

Therefore

`S_m > (1/50-1/250)I_6 = (2/125)I_6 > 0`.

This is the required **two-error** seed transfer. A single epsilon is not sufficient when both comparisons are only to the limit.

Together with positivity of all eliminated pivots, the block Schur identity implies `M>0`, hence `198I-25A^2>0`. To cover the complete requested range `k>=6`, one must separately certify `k=6,...,12`, corresponding to the seven orders listed in the first section. The companion analytic verifier has freshly certified all seven finite cases and the normalized seed at n=106, with margin 1/50. Those exact arithmetic results are recorded in `../analytic/r2_exact_certificate.json`; they are separate from the analytic argument above. An independent direct-graph replay is supplied separately by this audit.

## 7. Historical findings

- The retained cyclic core is 6-by-6; the old seed code really uses a different 8-by-8 core, so a notation-only edit would be invalid.
- The old seed also uses the unnormalized matrix, introducing a second mismatch.
- The terminal coupling is E_+ because the zero-based terminal index is m-2, always even.
- The terminal C correction must be included.
- Pairwise geometric summation must count two single-block increments per pair.
- Row and column response norms require the dual certificate `L Q L^T`, as above.
- The series need no pivot-limit replacement; only the terminal fixed quadratic form does.
- Seed-to-limit-to-core comparison costs two errors.
- The old coordinate derivative constants are not needed and have not been adopted.

