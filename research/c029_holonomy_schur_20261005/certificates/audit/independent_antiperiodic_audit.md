# Independent audit of the antiperiodic counterexample

Date: 2026-10-05. Status: **PASS**.

The live primary statement was checked directly: [Conjecture 28, arXiv:2607.17343v2, Section 12.3](https://arxiv.org/html/2607.17343v2#S12.SS3) asserts that the unrestricted minimum on every `C_(8m)(1,2)`, `m>=4`, equals the period-eight value `r_*`, the largest real root of `f(x)=x^4-2x^3-6x^2+12x-4`.

The proposed antiperiodic modification disproves that statement for every `m>=4`. This does not identify the unrestricted minimum.

## 1. Construction and boundary conditions

Start with the period-eight signing whose step-one signs are positive and whose step-two pattern is

`(+,+,-,+,-,-,+,-)`.

For `n=8m`, reverse exactly the signs of the three edges crossing the cut between `n-1` and `0`:

`{n-1,0}`, `{n-2,0}`, and `{n-1,1}`.

Every triangle crossing the cut contains two reversed edges, and every other triangle contains zero, so every triangle sign is preserved. The step-one Hamilton cycle contains exactly one reversed edge, so its holonomy changes from positive to negative. These are genuine real signed adjacency matrices on the same graph.

Equivalently, lift the period-eight operator to the infinite chain and impose the boundary condition `v_(j+n)=-v_j`. The resulting finite operator is exactly the three-edge-modified matrix. Its cell shift has eigenvalues z satisfying `z^m=-1`, so the Floquet decomposition uses precisely those phases. There is no parity exception: `z=1` never occurs, while `z=-1` may occur and is harmless.

## 2. Block polynomial and largest root

The Bloch matrix and its characteristic polynomial were checked against [Theorem 26, Section 12.2](https://arxiv.org/html/2607.17343v2#S12.SS2). Independently constructing the Bloch matrix from the two signed edge types gives, for `s=z+z^-1`,

`P(x,s)=x^8-16x^6+80x^4-128x^2+38+s(-2x^4+16x^2-13)+s^2`.

Put `t=x^2-4`. Exact expansion gives

`P=t^4-(16+2s)t^2+s^2+19s+38`.

The two values of `t^2` are therefore

`U_+(s)=8+s+sqrt(26-3s)` and `U_-(s)=8+s-sqrt(26-3s)`.

For `-2<=s<=2`, both are positive. Indeed `8+s>=6`, and

`(8+s)^2-(26-3s)=s^2+19s+38>=4>0`.

Also `U_+(s)<16`: it is increasing, because

`U_+'(s)=1-3/(2sqrt(26-3s))>0`,

and its endpoint is `U_+(2)=10+sqrt20<16`. Consequently the four positive values of x² arising from the polynomial are `4 ± sqrt(U_+)` and `4 ± sqrt(U_-)`. The largest absolute eigenvalue of the Hermitian block is exactly

`R(s)=sqrt(4+sqrt(8+s+sqrt(26-3s)))`.

The preceding derivative proves that R is strictly increasing throughout `[-2,2]`.

At s=2, the exact factorization is `P(x,2)=f(x)f(-x)`. To verify which factor supplies the largest root, note that f is strictly increasing for `x>=sqrt6`, because `f''(x)>0` there and `f'(sqrt6)=12sqrt6-24>0`. Rational evaluations give `f(279/100)<0<f(14/5)`, so its largest root `r_*` lies in that interval. For `x>=r_*`,

`f(-x)=f(x)+4x(x^2-6)>0`.

Thus the largest absolute root of P(x,2) is `r_*`, and `R(2)=r_*`.

## 3. Strict improvement for every finite cell count

For `z^m=-1`, the maximum of `s=z+z^-1` is `2cos(pi/m)`, which is strictly below 2 for every finite positive m. The exact antiperiodic spectral radius is therefore

`rho(A_antiperiodic)=R(2cos(pi/m))<R(2)=r_*`.

In particular this holds for every `m>=4` covered by Conjecture 28. The change of Hamilton holonomy is essential; restricting to the original positive-holonomy gauge would omit these competitors.

## 4. Independent exact finite replay

The script `replay_antiperiodic.py` independently constructs the n=32 full signed graph and the symbolic eight-by-eight Bloch matrix from the edge rules. It does not execute the primary verifier or historical repository code.

The replay verifies:

- exactly the three claimed cut edges are reversed
- every triangle sign is unchanged and Hamilton holonomy is negative
- exact Fraction scalar LDL has 32 positive pivots for each of `279I-100A` and `279I+100A`
- the algorithmically generated Bloch determinant equals P exactly
- the endpoint factorization and nested-radical reduction hold exactly
- the two rational evaluations separating `279/100` from r_* have the stated signs

Hence the finite witness alone proves `rho(A_32)<279/100<r_*`. The all-m argument above is analytic and does not rely on numerical eigenvalues. Results and all 64 rational LDL pivots are in `antiperiodic_independent_replay.json`.

No gap was found in the proposed counterexample. No claim of global optimality for the antiperiodic signing has been established.
