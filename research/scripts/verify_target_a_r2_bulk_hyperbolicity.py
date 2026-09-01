"""Exact stable-multiplier bound at the residue-two cap T2=198/25."""

from fractions import Fraction


def verify() -> dict[str, object]:
    y = Fraction(198, 25)
    h = 2 * y * y - 16 * y + 13
    discriminant = -12 * y * y + 96 * y + 17
    q = Fraction(1, 3)
    threshold = q + 1 / q
    base = h - 2 * threshold
    square_margin = base * base - discriminant
    checks = {
        "discriminant_positive": discriminant > 0,
        "base_positive": base > 0,
        "square_margin_positive": square_margin > 0,
        "slow_multiplier_bound": q < 1,
    }
    if not all(checks.values()):
        raise AssertionError(checks)
    return {
        "status": "R2_BULK_HYPERBOLICITY_PASS",
        "energy": str(y),
        "slow_multiplier_upper": str(q),
        "h": str(h),
        "discriminant": str(discriminant),
        "base": str(base),
        "square_margin": str(square_margin),
        "conclusion": "both slow stable multipliers are strictly below 1/3",
    }


if __name__ == "__main__":
    print(verify())
