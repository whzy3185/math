# Task 60.0-60.1 Handoff

> Historical Task 60 checkpoint; its formulas remain reusable foundations.
> The active extension is documented in
> [the current result index](../../../repository_guide/RESULTS_INDEX.md).
> “Next authorized task” below records the original stage, not the present
> task authorization.

```text
Branch: exp/circulant-1s-generalization
Frozen parent: target-a-task59-submission-v1
Task 60.0 checkpoint: e9a1754 (derive general switching algebra)
Current completed scope: Task 60.0 and Task 60.1

Universal theorem:
  Hamilton gauge + invariant tau/Q + complete path-sum A^2 formula.

Twisted theorem:
  Q=-1 exists iff N is even and gives
  A^2=4I+T^2+T^-2+(-1)^s(T^(2s)+T^(-2s)), T^N=alpha I.

Main obstruction:
  even s has endpoint threshold 8;
  odd s has an arithmetic-sensitive interior threshold M_s<8.

General verifier:
  research/scripts/verify_target_a_task60_general_model.py
General tests:
  research/scripts/test_target_a_task60_general_model.py
Twisted verifier:
  research/scripts/verify_target_a_task60_twisted.py
Symbolic verifier:
  research/scripts/verify_target_a_task60_twisted_symbolic.py
Twisted tests:
  research/scripts/test_target_a_task60_twisted.py

Task 59 frozen trees:
  manuscript: daf0bb5ab233e361e913abded481e26e7b68ebef
  supplement: 92de780d2621f4ab9b221fb27827564d2a459720
  control: b123397af26623d2051c3d21168d96e50a20f828

Next authorized task: Task 60.2 only after explicit continuation.
Pull request: none.
```
