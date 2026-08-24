# Uniform Separation For Abnormal Single Gaps

Status: `PROVED` relative to the certified upper endpoint for `c6` and the
Task 56 exact single-gap witnesses.

## Corollary

For every positive integer `g` with `g not in {4,6}`, the bilateral
single-gap operator satisfies

```text
sup sigma(H_g)>c6+1/250.                              (1)
```

Thus G6 is not only the unique abnormal single gap attaining `c6`: every
other abnormal single gap is separated from it by the same explicit positive
constant `1/250`.

## Exact Proof

The certified isolating interval gives

```text
c6<7905369311620328/10^15.                            (2)
```

Consequently it is enough to compare each exact Rayleigh witness with

```text
7905369311620328/10^15+1/250
 =988671163952541/125000000000000.                    (3)
```

The complete abnormal single-gap theorem supplies the following lower bounds.

| gap class | exact lower bound | exact margin over (3) |
|---|---:|---:|
| `g=1` | `812/97` | `5598897096603523/12125000000000000` |
| `g=2` | `866/109` | `484843129173031/13625000000000000` |
| `g=3` | `3114/393` | `234077522217129/16375000000000000` |
| `g=5` | `764/96` | `18361508142377/375000000000000` |
| `g=7` | `768/97` | `98897096603523/12125000000000000` |
| `g=8` | `19672/2487` | `174815250030533/310875000000000000` |
| every `g>=9` | `182/23` | `10563229091557/2875000000000000` |

Every displayed numerator and denominator is positive. The smallest exact
margin is the `g=8` row. Therefore every listed quotient is strictly larger
than (3). These cases exhaust all positive `g not in {4,6}`, proving (1).

No floating-point comparison occurs in the proof. Gap 4 is excluded because
it is the unperturbed reference bulk with edge `eta<c6`; gap 6 is excluded
because its edge equals `c6`.

Certificate: `certificates/uniform_single_gap_separation.json`.
