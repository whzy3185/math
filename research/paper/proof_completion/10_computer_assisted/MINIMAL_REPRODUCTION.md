# Minimal Referee Reproduction

## Runtime

From the repository root:

```bash
PY=/Users/muelsyse/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3
export PYTHONPATH=research/scripts
```

The commands below run checkers, not discovery scans. Producer commands are
unnecessary for a minimal review and may rewrite certificates.

## Unified proof-package command

The complete main-chain referee check is:

```bash
$PY research/scripts/verify_target_a_task575.py
```

It runs the 13 inherited independent checker entry points followed by the
focused proof-connection gate and finishes with
`TARGET_A_TASK575_VERIFY_PASS inherited_checkers=13 repair_gates=1`. The
family-by-family commands below are provided for diagnosis and selective
reproduction.

## One command group per certificate family

| Family | Minimal command | Expected terminal status |
|---|---|---|
| Reference phase | `$PY research/scripts/verify_target_a_period8_sharp_constant.py` | `TARGET_A_PERIOD8_SHARP_CONSTANT_PASS` |
| Small-order minimality and `n=32` | `$PY research/scripts/verify_target_a_minimality_certificate.py` | verifier PASS summary |
| G6 local/global edge | `$PY research/scripts/verify_target_a_task50_interface.py && $PY research/scripts/verify_target_a_task53_a3.py` | interface PASS and `TARGET_A_TASK53_A3_VERIFY_PASS` |
| IMS/residue arithmetic | `$PY research/scripts/verify_target_a_task53_global.py` | `TARGET_A_TASK53_GLOBAL_VERIFY_PASS` |
| Orders `34..46` | `$PY research/scripts/verify_target_a_task55_small_order_exact.py` | `TARGET_A_TASK55_SMALL_ORDER_EXACT_VERIFY_PASS` |
| Order 40 legacy LDL cross-check | `$PY research/scripts/verify_target_a_task55_orders_34_46.py` | `TARGET_A_TASK55_ORDERS_34_46_VERIFY_PASS` |
| Contiguous tail `n>=48` | `$PY research/scripts/verify_target_a_task54_threshold.py` | `TARGET_A_TASK54_THRESHOLD_VERIFY_PASS` |
| Exact `2r` and exponential constants | `$PY research/scripts/verify_target_a_task55_exact_2r.py` | `TARGET_A_TASK55_EXACT_2R_VERIFY_PASS` |
| Abnormal single-gap hierarchy | `$PY research/scripts/verify_target_a_task56_single_gap.py` | `TARGET_A_TASK56_SINGLE_GAP_VERIFY_PASS` |
| Uniform single-gap `1/250` | `$PY research/scripts/verify_target_a_task57_uniform_single_gap.py` | `TARGET_A_TASK57_UNIFORM_SINGLE_GAP_VERIFY_PASS` |
| General first moments | `$PY research/scripts/verify_target_a_general_period_moments.py` | `TARGET_A_GENERAL_PERIOD_MOMENTS_PASS` |
| Bounded `p<=24` frontier | `$PY research/scripts/verify_target_a_task53_p24.py` | `TARGET_A_TASK53_P24_VERIFY_PASS` |
| One-G6 protected double level | `$PY research/scripts/verify_target_a_task56_one_g6_degeneracy.py` | `TARGET_A_TASK56_ONE_G6_DEGENERACY_VERIFY_PASS` |
| Support-18 multi-gap appendix | `$PY research/scripts/verify_target_a_task55_multigap.py && $PY research/scripts/verify_target_a_task55_multigap_alt.py` | two multigap PASS lines |

## Focused fail-closed tests

```bash
$PY -m pytest -q \
  research/scripts/test_target_a_task55_exact_2r.py \
  research/scripts/test_target_a_task55_small_order_exact.py \
  research/scripts/test_target_a_task56_single_gap.py \
  research/scripts/test_target_a_task57_uniform_single_gap.py \
  research/scripts/test_target_a_general_period_moments.py
```

## Full research regression

This is optional for a referee because it includes historical and exploratory
modules:

```bash
$PY -m pytest -q research/scripts
```

The publication appendix should report the runtime and exact test summary from
the frozen submission commit. It should not require network access or GPU
software.

## Period-24 independence note

The implementation-disjoint orbit audit is

```bash
$PY research/scripts/target_a_task49_p24_independent.py
```

It regenerates and writes its summary, so it is not part of the read-only
minimal command list above. It independently verifies orbit completeness for
periods 17--24; its endpoint threshold is weaker than `c6`, as disclosed in
the proof boundary.
