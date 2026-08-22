"""Small exact-rational interval and automatic-differentiation kernel."""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import isqrt


SQRT_DECIMAL_DIGITS = 120


@dataclass(frozen=True)
class Interval:
    lo: Fraction
    hi: Fraction

    def __post_init__(self) -> None:
        if self.lo > self.hi:
            raise ValueError("reversed interval")

    @staticmethod
    def point(value: int | Fraction) -> "Interval":
        value = Fraction(value)
        return Interval(value, value)

    def __add__(self, other: object) -> "Interval":
        other = as_interval(other)
        return Interval(self.lo + other.lo, self.hi + other.hi)

    __radd__ = __add__

    def __neg__(self) -> "Interval":
        return Interval(-self.hi, -self.lo)

    def __sub__(self, other: object) -> "Interval":
        return self + (-as_interval(other))

    def __rsub__(self, other: object) -> "Interval":
        return as_interval(other) - self

    def __mul__(self, other: object) -> "Interval":
        other = as_interval(other)
        products = (self.lo * other.lo, self.lo * other.hi, self.hi * other.lo, self.hi * other.hi)
        return Interval(min(products), max(products))

    __rmul__ = __mul__

    def reciprocal(self) -> "Interval":
        if self.lo <= 0 <= self.hi:
            raise ZeroDivisionError("interval contains zero")
        return Interval(min(1 / self.lo, 1 / self.hi), max(1 / self.lo, 1 / self.hi))

    def __truediv__(self, other: object) -> "Interval":
        return self * as_interval(other).reciprocal()

    def __rtruediv__(self, other: object) -> "Interval":
        return as_interval(other) / self

    def __pow__(self, exponent: int) -> "Interval":
        if exponent < 0:
            return (self.reciprocal()) ** (-exponent)
        result = Interval.point(1)
        base = self
        power = exponent
        while power:
            if power & 1:
                result = result * base
            base = base * base
            power //= 2
        return result

    def excludes_zero(self) -> bool:
        return self.hi < 0 or self.lo > 0

    def sign(self) -> int:
        if self.lo > 0:
            return 1
        if self.hi < 0:
            return -1
        return 0


def as_interval(value: object) -> Interval:
    if isinstance(value, Interval):
        return value
    if isinstance(value, (int, Fraction)):
        return Interval.point(value)
    raise TypeError(f"cannot convert {type(value)!r} to Interval")


def sqrt_fraction_bounds(value: Fraction, digits: int = SQRT_DECIMAL_DIGITS) -> tuple[Fraction, Fraction]:
    if value < 0:
        raise ValueError("negative square root")
    scale = 10**digits
    numerator = value.numerator * scale * scale
    denominator = value.denominator
    lower_integer = isqrt(numerator // denominator)
    while (lower_integer + 1) ** 2 * denominator <= numerator:
        lower_integer += 1
    while lower_integer**2 * denominator > numerator:
        lower_integer -= 1
    lower = Fraction(lower_integer, scale)
    if lower_integer**2 * denominator == numerator:
        return lower, lower
    return lower, Fraction(lower_integer + 1, scale)


def interval_sqrt(value: Interval) -> Interval:
    if value.lo < 0:
        raise ValueError("interval square root crosses negative values")
    lower, _ = sqrt_fraction_bounds(value.lo)
    _, upper = sqrt_fraction_bounds(value.hi)
    return Interval(lower, upper)


@dataclass(frozen=True)
class Dual:
    value: Interval
    derivative: Interval

    @staticmethod
    def constant(value: int | Fraction | Interval) -> "Dual":
        return Dual(as_interval(value), Interval.point(0))

    @staticmethod
    def variable(value: Interval) -> "Dual":
        return Dual(value, Interval.point(1))

    def __add__(self, other: object) -> "Dual":
        other = as_dual(other)
        return Dual(self.value + other.value, self.derivative + other.derivative)

    __radd__ = __add__

    def __neg__(self) -> "Dual":
        return Dual(-self.value, -self.derivative)

    def __sub__(self, other: object) -> "Dual":
        return self + (-as_dual(other))

    def __rsub__(self, other: object) -> "Dual":
        return as_dual(other) - self

    def __mul__(self, other: object) -> "Dual":
        other = as_dual(other)
        return Dual(
            self.value * other.value,
            self.derivative * other.value + self.value * other.derivative,
        )

    __rmul__ = __mul__

    def reciprocal(self) -> "Dual":
        inverse = self.value.reciprocal()
        return Dual(inverse, -self.derivative * inverse * inverse)

    def __truediv__(self, other: object) -> "Dual":
        return self * as_dual(other).reciprocal()

    def __rtruediv__(self, other: object) -> "Dual":
        return as_dual(other) / self

    def __pow__(self, exponent: int) -> "Dual":
        if exponent < 0:
            return (self.reciprocal()) ** (-exponent)
        result = Dual.constant(1)
        for _ in range(exponent):
            result = result * self
        return result


def as_dual(value: object) -> Dual:
    if isinstance(value, Dual):
        return value
    if isinstance(value, Interval):
        return Dual.constant(value)
    if isinstance(value, (int, Fraction)):
        return Dual.constant(value)
    raise TypeError(f"cannot convert {type(value)!r} to Dual")


def dual_sqrt(value: Dual) -> Dual:
    root = interval_sqrt(value.value)
    return Dual(root, value.derivative / (2 * root))


def outward_decimal_fraction(value: Fraction, digits: int, upper: bool) -> Fraction:
    scale = 10**digits
    scaled_numerator = value.numerator * scale
    integer = -((-scaled_numerator) // value.denominator) if upper else scaled_numerator // value.denominator
    return Fraction(integer, scale)


def interval_record(value: Interval) -> dict[str, str]:
    lower = outward_decimal_fraction(value.lo, 30, upper=False)
    upper = outward_decimal_fraction(value.hi, 30, upper=True)
    return {
        "lower": str(lower),
        "upper": str(upper),
        "format": "30-decimal outward rational enclosure",
    }
