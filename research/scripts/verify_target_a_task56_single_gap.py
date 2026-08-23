"""Independent exact checker for the Task 56 abnormal single-gap theorem."""

from __future__ import annotations

from pathlib import Path


REPO = Path(__file__).resolve().parents[2]
REPORT = REPO / "research" / "proofs" / "task56" / "TARGET_A_SINGLE_GAP_NIGHT_REPORT.md"
C6_UPPER_NUMERATOR = 7905369311620328
C6_UPPER_DENOMINATOR = 10**15


SMALL_CASES = {
    1: (-2, (2, 0, 4, 4, 6, 5), 97, 812),
    2: (-4, (1, -1, -2, -1, -4, -5, -6, -2, 1, 4, 2), 109, 866),
    3: (-5, (0, 1, -1, -3, 0, -6, -8, -6, -10, -6, -8, -6, 1, -3), 393, 3114),
    5: (-2, (2, 0, 4, 4, 4, 4, 1, 3, 3, 3), 96, 764),
    7: (-2, (2, 0, 3, 4, 4, 4, 1, 3, 2, 3, 2, 3), 97, 768),
    8: (-8, (4, 4, 4, 3, -3, 3, 9, 1, 19, 22, 21, 22, 4, 16, 8, 12, 5, 6, 0, -4, -1, 1, 0, 1, 0), 2487, 19672),
}

TAIL_VECTOR = (4, 0, 7, 8, 8, 9, 1, 7, 3, 6, 1, 4, 1, 2)
TAIL_EXPECTED = {9: 3102, 10: 3094, 11: 3094}


def q_value(index: int, gap: int) -> int:
    left = index <= 0 and index % 4 == 0
    right = index >= gap and (index - gap) % 4 == 0
    return 1 if left or right else -1


def tau_window(gap: int, low: int, high: int) -> dict[int, int]:
    tau = {0: 1}
    for index in range(high):
        tau[index + 1] = q_value(index, gap) * tau[index]
    for index in range(-1, low - 1, -1):
        tau[index] = q_value(index, gap) * tau[index + 1]
    return tau


def exact_image(gap: int, support_low: int, vector: tuple[int, ...]) -> tuple[int, ...]:
    values = {support_low + offset: value for offset, value in enumerate(vector)}
    output_low = support_low - 2
    output_high = support_low + len(vector) + 1
    tau = tau_window(gap, output_low - 2, output_high + 2)
    return tuple(
        values.get(index - 1, 0)
        + values.get(index + 1, 0)
        + tau[index - 2] * values.get(index - 2, 0)
        + tau[index] * values.get(index + 2, 0)
        for index in range(output_low, output_high + 1)
    )


def verify_case(
    gap: int,
    support_low: int,
    vector: tuple[int, ...],
    expected_denominator: int,
    expected_numerator: int,
) -> tuple[int, int]:
    denominator = sum(value * value for value in vector)
    numerator = sum(value * value for value in exact_image(gap, support_low, vector))
    if denominator != expected_denominator or numerator != expected_numerator:
        raise AssertionError((gap, denominator, numerator))
    if numerator * C6_UPPER_DENOMINATOR <= C6_UPPER_NUMERATOR * denominator:
        raise AssertionError(f"gap {gap} does not lie strictly above c6 upper endpoint")
    return numerator, denominator


def verify() -> dict[str, bool]:
    if not REPORT.is_file():
        raise AssertionError("Task 56 single-gap report missing")
    text = REPORT.read_text(encoding="utf-8")
    required = (
        "complete abnormal single-gap hierarchy",
        "sup sigma(H_6)=c6",
        "sup sigma(H_g)>c6  for every g not in {4,6}",
        "g=4` is not an interface",
        "rank two, not rank one",
        "3094/391=182/23",
    )
    if not all(fragment in text for fragment in required):
        raise AssertionError("report theorem contract mismatch")

    for gap, (support_low, vector, denominator, numerator) in SMALL_CASES.items():
        verify_case(gap, support_low, vector, denominator, numerator)

    for gap, expected in TAIL_EXPECTED.items():
        verify_case(gap, -2, TAIL_VECTOR, 391, expected)
    reference = exact_image(11, -2, TAIL_VECTOR)
    for gap in range(12, 257):
        if exact_image(gap, -2, TAIL_VECTOR) != reference:
            raise AssertionError(f"tail locality failed at gap {gap}")

    checks = {
        "six_small_abnormal_gaps_exact": len(SMALL_CASES) == 6,
        "tail_boundary_classes_exact": TAIL_EXPECTED == {9: 3102, 10: 3094, 11: 3094},
        "uniform_tail_quotient_exact": 3094 * 23 == 182 * 391,
        "all_strict_margins_positive": all(
            numerator * C6_UPPER_DENOMINATOR
            > C6_UPPER_NUMERATOR * denominator
            for _gap, (_low, _vector, denominator, numerator) in SMALL_CASES.items()
        ) and 3094 * C6_UPPER_DENOMINATOR > C6_UPPER_NUMERATOR * 391,
        "g6_dependency_stated": "computer-assisted global G6 edge theorem" in text,
        "scope_excludes_reference_gap": "g=4` is not an interface" in text,
    }
    if not all(checks.values()):
        raise AssertionError(checks)
    return checks


if __name__ == "__main__":
    verify()
    print("TARGET_A_TASK56_SINGLE_GAP_VERIFY_PASS")
