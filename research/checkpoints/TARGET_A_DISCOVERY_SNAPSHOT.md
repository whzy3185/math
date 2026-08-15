# Target A Discovery Snapshot

Date: 2026-08-15

Snapshot purpose: freeze the discovery state before minimality work begins.
No mathematical claim is strengthened in this checkpoint.

## Git state before snapshot commit

- Repository: `https://github.com/whzy3185/math.git`
- Base branch: `main`
- Base commit: `fb4375f9588b558f162d7e3f6542c35b0056eea3`
- Base subject: `Initialize mathematical counterexample research`
- Snapshot branch: `agent/target-a-discovery-snapshot`
- Pre-snapshot worktree: modified research index/specification/reproduction files,
  modified reproduction script, and untracked proof, certificate, search, test,
  log, and checkpoint artifacts belonging to Target A.
- Push status: not pushed.

## Frozen mathematical state

### PROVED

1. Conjecture 3 of *Signed circulants at the Ramanujan bound* is false.
2. The period-8 triangle-flux pattern
   `tau=(+,+,-,+,-,-,+,-)` has quadrilateral-flux pattern
   `Q=(+,-,-,-)`.
3. For every `8|n` with `n>=32`, and for either `alpha=+1` or `alpha=-1`,
   this family satisfies
   `rho(A)^2 < 1561/200 < rho_-(n)^2`.
4. The uniform upper bound follows from the exact 8 by 8 Floquet
   characteristic polynomial and rational polynomial positivity.

### COMPUTATIONALLY VERIFIED

1. The explicit `n=32, alpha=+1` witness has the prescribed fluxes and
   satisfies the strict counterexample inequality.
2. `1561 I - 200 A^2` is positive definite by both fraction-free
   Bareiss/Sylvester leading minors and an independent rational `LDL^T`
   decomposition.
3. Full raw switching-class searches pass for `n=8,10,...,20`.
4. The `n=20` quotient search has 27,296 spectral states, represents all
   2,097,152 switching classes, and reproduces the raw minimum and smallest
   non-optimizer.
5. The `n=22` quotient search has 97,468 spectral states, represents all
   8,388,608 switching classes, certifies all 97,467 non-optimizer states by
   rational Rayleigh bounds, uses zero exact fallbacks, and finds no
   counterexample.
6. Five automated tests pass, all Python scripts compile, and
   `git diff --check` passes.

### OBSERVED

1. A numerical Floquet scan of 505 binary-bracelet patterns with Q-period at
   most 12 identifies `Q=(+,-,-,-)` as the smallest-band non-alternating
   pattern in that search.
2. The `n=20` and `n=22` near-minimizer atlases place the smallest
   non-optimizer in defect shell `d=4`, which motivated the periodic search.
3. A secondary period-10 infinite family also gives counterexamples from
   multiples of 10 with `n>=50`.

### UNRESOLVED

1. **`n=32 is the smallest counterexample`: UNRESOLVED.**
2. Complete exact searches at `n=24,26,28,30` have not been run.
3. The period-8 proof has not yet received a fully independent human or
   separately implemented Floquet audit.
4. No final novelty audit has been completed.
5. No claim is made that the period-8 family is globally optimal.
6. The failure mechanism has not yet been promoted to a structural theorem.

## Environment

- OS: `macOS-26.5.2-arm64-arm-64bit`
- Python: `3.12.13` (`Clang 22.1.3`)
- NumPy: `2.3.5`
- SymPy: `1.14.0`
- Virtual environment: repository-local `.venv`
- NumPy source: Codex bundled primary runtime via `PYTHONPATH`

## Reproduction commands

Set the bundled dependency path for each command:

```bash
export PYTHONPATH=/Users/muelsyse/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/lib/python3.12/site-packages
```

Run the frozen checks:

```bash
.venv/bin/python -m unittest discover -s research/scripts -p 'test_target_a_*.py'
.venv/bin/python -m py_compile research/scripts/*.py

.venv/bin/python research/scripts/target_a_period8_family.py \
  --output research/counterexamples/target_a_period8_family_certificate.json

.venv/bin/python research/scripts/target_a_rational_certificate.py \
  research/counterexamples/target_a_n32_period8.json \
  --bound 1561/200 \
  --output research/counterexamples/target_a_n32_period8_certificate.json

.venv/bin/python research/scripts/target_a_flux_search.py \
  --n 20 \
  --reference-log research/logs/target_a_search_n20.json \
  --output research/logs/target_a_flux_atlas_n20.json

.venv/bin/python research/scripts/target_a_flux_search.py \
  --n 22 \
  --output research/logs/target_a_flux_search_n22.json

.venv/bin/python research/scripts/target_a_structured_search.py \
  --max-n 100 --max-period 12 \
  --output research/logs/target_a_structured_search_n100_p12.json
```

## Core artifact SHA-256

```text
4ef3243e0e516aec934a84af7384c615b0d433527c2c052f5dfb165e63329b34  research/conjectures/TARGET_A_SPEC.md
bcfa939b6db8b29b410c6280f2892233637674699f53982c8f4b895565e5f221  research/experiments/TARGET_A_REPRODUCTION.md
11453ec1c17fd57dab036c92fe12909bb0d729f3ee6b0f8d83e71a9bee584806  research/proofs/TARGET_A_PERIOD8_FAMILY.md
5fcc0becd8cc7963d0bbd25521e14dc06f11b6ca245fb30bb3132588ed6bac2c  research/proofs/TARGET_A_PERIOD10_FAMILY.md
c5ecd532da469092ef98fe2385dfb69b8da542595f942cd88b881d985b72bc10  research/counterexamples/target_a_n32_period8.json
db1378c6a7e5ab8526890be41c929a60ee17675d920a5ca0c501f49d888e46b4  research/counterexamples/target_a_n32_period8_certificate.json
6421bb0400cbfda7063b86b3dfb9310543cc1c0800a9d49890f25d047624c023  research/counterexamples/target_a_period8_family_certificate.json
5220622e6863c6a8cee4c0762d994b99ecde358cf862b5aee3919f008804107f  research/counterexamples/target_a_n50_period10.json
947205eed4a43033a554a5b3b244e3c48a5cd7d71f102ac4ef09e6a668f02432  research/counterexamples/target_a_n50_period10_certificate.json
2f81432d28f61ee9196990e4f8663d6eab3f6b7195c005437ca262d3a1742b0d  research/counterexamples/target_a_period10_family_certificate.json
0c644b1242b4054c76a603d42897f6cbaf152ccfd2a934da67ddd90757f35694  research/scripts/target_a_verifier.py
caece358826ebb0325349fcb54422b1c220860d86d98509990fc65b19151b990  research/scripts/target_a_reproduce.py
cf32302864c90f995c377ea84969e3bdabd07c3a9a3f41c2a1defa68e02bb769  research/scripts/target_a_flux_search.py
f94183909a4075f1f8a015737f8f64e33e2fa287657b3c7a15d707866b9961c9  research/scripts/target_a_structured_search.py
9effc9681d020d76924f5e4ffebabad344e5945067551cd48e68ef3b19c1c63c  research/scripts/target_a_period8_family.py
e534db18965382d3e18919ea6b4e4f680fbc167e505ef55765ce9520b840de7e  research/scripts/target_a_period10_family.py
d08d420eaee6f8aefa6f1dbae90ab30bb666234495ffd8dfe75064dda434b838  research/scripts/target_a_rational_certificate.py
1173a444feb3217649213c8d334a575be9dd1da3e76ea3e66921c5d405608b99  research/scripts/test_target_a_flux_search.py
d2b632989fe5ee3d399ed01fe549a5f4496ddb3f7c96b8bce5795935cf62cd69  research/scripts/test_target_a_counterexample.py
141d0253159acde39473cf4f825f65d438cd56e8433e407c3302fe048ad3715e  research/logs/target_a_reproduction_n8_18.json
20a0d812a268d51c4c52188c63827732216815f20901ef83ad680816d82fbcc4  research/logs/target_a_search_n20.json
7fdf97370ae165bf513783936893652371741c74d8150031f8e70d816db2abc1  research/logs/target_a_flux_atlas_n20.json
588c5998a83d01c0db9cbc81d0551cbd04d66823c58ce7f506b259e8125264be  research/logs/target_a_flux_search_n22.json
1cfd9b91a686ee25f668e65281b994754fcdff95e87797758fd936516aebee19  research/logs/target_a_structured_search_n100_p12.json
```

The 23 per-shell JSON checkpoints under `research/logs/checkpoints/` have the
ordered SHA-256 manifest digest:

```text
642a2ffd3d88ef4131fae3e5719a81c306ae4983fe8813492b22998573f50243
```

The digest is reproduced by hashing the sorted `shasum -a 256` manifest,
not by concatenating checkpoint contents without filenames.
