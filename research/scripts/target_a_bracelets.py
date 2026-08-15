"""Constant-memory binary-bracelet stream for Target A spectral states.

The reference generator in target_a_flux_search scans all 2^n codes and
marks a visited bytearray.  This independent production generator uses the
Fredricksen-Kessler-Maiorana necklace recursion with a fixed-weight prune,
then keeps the lexicographically smaller orientation of each reflection pair.
Its working memory is O(n), independent of 2^n and of the number of outputs.
"""

from __future__ import annotations

from collections.abc import Iterator


def _rotate_left(code: int, shift: int, n: int) -> int:
    mask = (1 << n) - 1
    shift %= n
    if shift == 0:
        return code & mask
    return ((code << shift) | (code >> (n - shift))) & mask


def _reverse_n_bits(code: int, n: int) -> int:
    result = 0
    for _ in range(n):
        result = (result << 1) | (code & 1)
        code >>= 1
    return result


def _fixed_weight_necklaces(n: int, weight: int) -> Iterator[tuple[int, int]]:
    """Yield (lexicographically minimal code, minimal period) necklaces."""
    bits = [0] * (n + 1)

    def generate(position: int, period: int, ones: int) -> Iterator[tuple[int, int]]:
        remaining = n - position + 1
        if ones > weight or ones + remaining < weight:
            return
        if position > n:
            if n % period == 0 and ones == weight:
                code = 0
                for index in range(1, n + 1):
                    code = (code << 1) | bits[index]
                yield code, period
            return

        bits[position] = bits[position - period]
        yield from generate(position + 1, period, ones + bits[position])
        if bits[position - period] == 0:
            bits[position] = 1
            yield from generate(position + 1, position, ones + 1)

    yield from generate(1, 1, 0)


def enumerate_direct_q_orbits(
    n: int,
    defect_count: int | None = None,
) -> Iterator[tuple[int, int]]:
    """Yield (canonical Q code, dihedral orbit size) in stable shell order.

    Bit 1 denotes Q_i=+1, so admissible vectors have even Hamming weight.
    When defect_count is omitted, shells are emitted as 0,2,...,n.  Within a
    shell, canonical integer codes are strictly increasing.
    """
    if n < 1:
        raise ValueError("n must be positive")
    if defect_count is not None:
        if defect_count < 0 or defect_count > n or defect_count % 2:
            raise ValueError("defect_count must be an even integer in [0,n]")
        weights = (defect_count,)
    else:
        weights = range(0, n + 1, 2)

    for weight in weights:
        previous_code = -1
        for code, rotational_orbit_size in _fixed_weight_necklaces(n, weight):
            reflected = _reverse_n_bits(code, n)
            reflected_minimum = min(
                _rotate_left(reflected, shift, n)
                for shift in range(rotational_orbit_size)
            )
            if code > reflected_minimum:
                continue
            orbit_size = (
                rotational_orbit_size
                if code == reflected_minimum
                else 2 * rotational_orbit_size
            )
            if code <= previous_code:
                raise AssertionError("direct bracelet order is not strictly increasing")
            previous_code = code
            yield code, orbit_size
