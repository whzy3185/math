"""Check order coverage supplied by the exact periodic Floquet families."""


FAMILIES = {
    8: 32,
    10: 50,
    12: 60,
    14: 112,
    18: 54,
    22: 66,
}


def covered_by_periodic_family(n: int) -> bool:
    return any(n >= first and n % period == 0 for period, first in FAMILIES.items())


def verify() -> dict[str, object]:
    remaining = []
    periodic = []
    ims = []
    for n in range(48, 240, 2):
        residue = n % 8
        if covered_by_periodic_family(n):
            periodic.append(n)
        elif (residue == 2 and n >= 92) or (residue == 4 and n >= 166):
            ims.append(n)
        else:
            remaining.append(n)
    expected = [
        52, 58, 62, 68, 74, 76, 78, 82, 86, 92, 94, 102, 116,
        118, 124, 134, 142, 148, 158, 164, 166, 174, 206, 214, 222,
    ]
    if remaining != expected:
        raise AssertionError((remaining, expected))
    if len(periodic) != 55 or len(ims) != 16 or len(remaining) != 25:
        raise AssertionError((len(periodic), len(ims), len(remaining)))
    return {
        "status": "PERIODIC_FAMILY_COVERAGE_PASS",
        "periodic_rows": len(periodic),
        "ims_rows": len(ims),
        "remaining_rows": len(remaining),
        "remaining": remaining,
    }


if __name__ == "__main__":
    print(verify())
