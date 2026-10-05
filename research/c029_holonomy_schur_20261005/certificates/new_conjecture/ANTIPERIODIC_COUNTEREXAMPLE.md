# Antiperiodic period-eight signings strictly improve the conjectured value

## Recovery and verification status

This report and its verifier were reconstructed from the retained derivation and verification record after a workspace reset on 5 October 2026. The accompanying certificate and verification output are freshly recomputed in the replacement filesystem. They are not represented as the original pre-reset files or as a fresh independent audit.

Direct primary-source inspection and independent analytic and exact-computation checks were recorded before the reset. The arguments are fully restated below so that they can be reviewed without relying on those earlier checks. Their original files are not presumed to exist after the reset.

## Attribution and scope of this continuation

The antiperiodic finite-size formula is inherited from the existing mathematics repository and is freshly reverified here. It is not claimed as a newly discovered formula in this continuation. The contribution of this continuation is to apply that existing formula to Conjecture 28 in the 22 September 2026 v2 manuscript, giving an explicit contradiction to the conjecture as written and an exact 32-vertex certificate.

## Source and scope

The result below contradicts Conjecture 28 as written in Vaibhav Suvagiya, *Parity families and signed spectra: kernel averaging, near-Ramanujan bounds, and exact circulant models*, arXiv:2607.17343v2, 22 September 2026.

Primary source: https://arxiv.org/html/2607.17343v2#S12.SS3

The conjecture concerns all signings of `C_(8m)(1,2)`, for `m>=4`. Its proposed minimum is the largest real root `r_*` of

`f(x)=x^4-2x^3-6x^2+12x-4`,

approximately `2.793604493334841`. Theorem 26 supplies the positive-Hamilton-holonomy period-eight construction. Remark 27 explicitly says the supporting searches omit the opposite Hamilton-cycle holonomy.

This note gives a strict improvement in that omitted sector. It does not determine the true unrestricted minimum, establish literature-wide novelty, or report author contact.

## 1. Explicit signing

Let `n=8m`, for an integer `m>=1`. Label the vertices `0,...,n-1`, with edges `{i,i+1 mod n}` and `{i,i+2 mod n}`. Repeat the period-eight sequence

`b=(+1,+1,-1,+1,-1,-1,+1,-1)`.

Start with all step-one edges positive and sign `{i,i+2 mod n}` by `b_i`. Reverse precisely these three edges:

- `{n-1,0}`
- `{n-2,0}`
- `{n-1,1}`

Call the resulting signed adjacency matrix `A_m^-`. In other words, an edge whose forward lift crosses the cut between `n-1` and `0` receives an extra minus sign. All three edges are distinct, including for `n=8`.

Explicitly, the step-one signs are `a_i=+1` for `i<n-1` and `a_(n-1)=-1`. The step-two signs remain `b_i` for `i<n-2`; the final signs change from `b_(n-2)=+1` to `-1` and from `b_(n-1)=-1` to `+1`.

Every triangle retains sign `b_i`: each triangle crossing the cut contains exactly two reversed edges. The step-one Hamilton cycle has sign product `-1`. Thus the construction preserves the period-eight triangle data while changing the Hamilton holonomy.

## 2. Antiperiodic Floquet decomposition

Extend a vector to all integer indices using `u_(i+n)=-u_i`. Then the matrix action is the restriction of

`(Lu)_i=u_(i-1)+u_(i+1)+b_(i-2)u_(i-2)+b_i u_(i+2)`.

The sequence `b` has period eight. The ansatz `u_(8j+a)=z^j v_a`, for `a=0,...,7`, therefore gives the boundary condition `z^m=-1`. Its `m` roots

`z_k=exp((2k+1) pi i/m)`, for `0<=k<m`,

give an orthogonal direct sum of eight-dimensional fibers. None is `z=1`. The fiber matrix is

```
H(z) =
[ 0  1  1  0  0  0   z^-1   z^-1 ]
[ 1  0  1  1  0  0    0    -z^-1 ]
[ 1  1  0  1 -1  0    0      0   ]
[ 0  1  1  0  1  1    0      0   ]
[ 0  0 -1  1  0  1   -1      0   ]
[ 0  0  0  1  1  0    1     -1   ]
[ z  0  0  0 -1  1    0      1   ]
[ z -z  0  0  0 -1    1      0   ]
```

For an equivalent finite matrix identity, let `B` have only three nonzero entries: `B_(6,0)=B_(7,0)=1` and `B_(7,1)=-1`. Let `C0=H(1)-B-B^T`. Define `T_m` to have ones immediately above its main diagonal and entry `-1` in position `(m-1,0)`. Then

`A_m^-=I_m tensor C0+T_m tensor B+T_m^T tensor B^T`,

and `T_m^m=-I_m`. Its eigenvalues are the roots of `z^m=-1`. When `m=1`, this means `T_1=[-1]` and `A_1^-=C0-B-B^T`; there is no coincident-edge exception.

The verifier checks this identity directly for `m=1,...,5`. The displayed tensor identity also establishes it for arbitrary `m` from the edge construction.

Importantly, changing only the Hamilton edge would not give this decomposition. The two step-two cut edges must change as well.

## 3. Exact fiber radius

For a unit-modulus phase, put `s=z+z^-1`, so `-2<=s<=2`. Exact symbolic computation confirms

`det(xI-H(z))=P(x,s)`,

where

`P(x,s)=x^8-16x^6+80x^4-128x^2+38+s(-2x^4+16x^2-13)+s^2`.

Put `y=x^2` and `t=y-4`. The polynomial becomes

`P=t^4-(16+2s)t^2+s^2+19s+38`.

Its two roots as a quadratic in `t^2` are

`U_+(s)=8+s+sqrt(26-3s)` and `U_-(s)=8+s-sqrt(26-3s)`.

Both are positive: `8+s>0`, and

`(8+s)^2-(26-3s)=s^2+19s+38>=4`

on `[-2,2]`. Moreover, `U_+` is strictly increasing, because

`U_+'(s)=1-3/(2sqrt(26-3s))>0`,

using `sqrt(26-3s)>=sqrt(20)>3/2`. Consequently

`U_+(s)<=10+sqrt(20)<16`.

Thus all four numbers `y=4 +/- sqrt(U_+(s))` and `y=4 +/- sqrt(U_-(s))` are positive. Taking both signs of `sqrt(y)` gives all eight real eigenvalues. The largest modulus is therefore

`R(s)=sqrt(4+sqrt(8+s+sqrt(26-3s)))`.

It is strictly increasing on `[-2,2]`, because `U_+` and both outer square roots are strictly increasing.

## 4. Exact radius for every m

Among `z_k^m=-1`, the maximum of `s_k=z_k+z_k^-1` is `2cos(pi/m)`. Therefore

`rho(A_m^-)=R(2cos(pi/m))`

or explicitly,

`rho(A_m^-)=sqrt(4+sqrt(8+2cos(pi/m)+sqrt(26-6cos(pi/m))))`.

Since `cos(pi/m)<1` for every positive finite integer `m`, strict monotonicity gives

`rho(A_m^-)<R(2)=sqrt(4+sqrt(10+2sqrt(5)))`.

This endpoint equals `r_*`. Indeed, the verifier confirms

`P(x,2)=f(x)f(-x)`.

For completeness, `f(sqrt(6))=-4`, `f'(sqrt(6))=12sqrt(6)-24>0`, and

`f''(x)=12(x^2-x-1)>0` for `x>=sqrt(6)`.

Hence `f` has a unique root `r_*` in this interval, and no greater root. For `x>r_*`, both `f(x)>0` and

`f(-x)=f(x)+4x(x^2-6)>0`.

Thus the largest positive root of `P(x,2)` is `r_*`. The radical formula already identifies that root as `R(2)`.

In particular, for every `m>=4`,

`min_sigma rho(A_sigma)<=rho(A_m^-)<r_*`.

This contradicts Conjecture 28 as written, while leaving the actual unrestricted minimum undetermined.

There is no parity exception. For odd `m`, the phase `z=-1` occurs, but it has `s=-2`, whose radius is strictly smaller than the `s=2` endpoint. It does not restore the excluded extremum. The finite radii tend upward to `r_*` as `m` grows.

## 5. Standalone exact n=32 certificate

At `m=4`, the largest phase parameter is `s=sqrt(2)`, and

`rho(A_4^-)=sqrt[4+sqrt[8+sqrt(2)+sqrt(26-3sqrt(2))]]`

`=2.784269799307555...`.

The complete 32-by-32 signed integer matrix is saved in `exact_n32_certificate.json`. Its characteristic polynomial, computed directly from the matrix, is `Q(x)^2`, with

`Q(x)=x^16-32x^14+416x^12-2816x^10+10568x^8-21632x^6+22168x^4-9408x^2+1262`.

The verifier independently confirms `Q(x)=P(x,sqrt(2))P(x,-sqrt(2))`. Each phase parameter occurs twice.

A separate exact certificate does not depend on Floquet theory or numerical eigenvalues. Every leading principal minor of each of

`279I-100A_4^-` and `279I+100A_4^-`

is a strictly positive integer. All 64 values are recomputed using fraction-free integer Bareiss elimination and saved in the JSON certificate. Selected minors are also recomputed with a separate direct determinant implementation.

Sylvester's criterion implies both matrices are positive definite. Hence

`rho(A_4^-)<279/100=2.79`.

Exact rational evaluation gives

`f(279/100)=-6766519/100000000<0`,

`f(14/5)=76/625>0`.

Since `2.79>sqrt(6)` and `f` is increasing in that range, the exact separating chain is

`rho(A_4^-)<2.79<r_*<2.8`.

No floating-point result enters this certificate.

## 6. Reproduction and files

Run:

`python verify_antiperiodic_counterexample.py`

Python 3 and SymPy are required. NumPy is optional and used only for labeled numerical illustrations.

The script checks:

1. Graph support, symmetry, degree, triangle signs, and Hamilton holonomy
2. All 64 positive leading principal minors for the rational threshold
3. Exact symbolic eight-dimensional determinant and endpoint factorization
4. Exact tensor assembly for `m=1,2,3,4,5`
5. Exact nested-radical reduction
6. Direct 32-dimensional characteristic polynomial
7. Exact rational inequalities separating the example from `r_*`

Files in this directory:

- `ANTIPERIODIC_COUNTEREXAMPLE.md`: self-contained construction and proof
- `verify_antiperiodic_counterexample.py`: executable exact verifier
- `exact_n32_certificate.json`: freshly computed matrix and positive-minor certificate
- `verification_output.txt`: fresh run output after the workspace reset
- `RECOVERY.md`: recovery provenance and current verification status
