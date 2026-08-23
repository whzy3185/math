# Task 53 Reproducibility

Use the locked project runtime and run:

```text
python -m pytest -q research/scripts/test_target_a_task53.py
python research/scripts/verify_target_a_task53_a1.py
python research/scripts/verify_target_a_task53_a2.py
python research/scripts/verify_target_a_task53_a3.py
python research/scripts/verify_target_a_task53_global.py
python research/scripts/verify_target_a_task53_p24.py
python research/scripts/verify_target_a_task53_s1.py
python research/scripts/verify_target_a_task53_s4.py
python -m pytest -q research/scripts
```

Producers are the corresponding `target_a_task53_*.py` scripts. Generated
certificates live in `research/proofs/task53/certificates/`. Acceptance never
uses a floating discovery eigenvalue. The formal manuscript directories are
frozen and outside every Task 53 write path.
