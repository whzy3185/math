"""Independent exact witness and completeness checker for Task 53 S2."""

from __future__ import annotations

import hashlib
import json
import csv
from pathlib import Path

import sympy as sp

from target_a_task53_p24 import canonical_key, exact_bloch_matrix, exact_rayleigh, q_from_bits
from target_a_low_period_spectral_frontier import tau_lift


RESEARCH = Path(__file__).resolve().parents[1]
CERTIFICATE = RESEARCH / "proofs" / "task53" / "certificates" / "p24_c6_frontier.json"
UPPER = sp.Rational(7905369311620328, 10**15)


def verify(path: Path = CERTIFICATE) -> dict[str, bool]:
    data = json.loads(path.read_text())
    rebuilt = []
    keys = set()
    for row in data["witnesses"]:
        key = (int(row["period"]), row["q_bits"])
        if key in keys:
            raise AssertionError("duplicate witness")
        keys.add(key)
        q = q_from_bits(row["q_bits"])
        tau = tau_lift(q)
        matrix = exact_bloch_matrix(tau, row["bloch_root"])
        vector = [(int(real), int(imag)) for real, imag in row["gaussian_integer_vector"]]
        numerator, denominator = exact_rayleigh(matrix, vector)
        rebuilt.append(
            numerator == int(row["numerator_A2"])
            and denominator == int(row["denominator"])
            and sp.Integer(numerator) * UPPER.q > UPPER.p * sp.Integer(denominator)
        )

    low_path = RESEARCH / "proofs" / "target_a_low_period_spectral_frontier.json"
    low = json.loads(low_path.read_text())
    low_complete = []
    for row in low["orbits"]:
        if row["target_infinite_phase"]:
            low_complete.append(True)
            continue
        certificate = row["exact_certificate"]
        low_complete.append(
            certificate["type"] == "TASK42A_MOMENT_EXCESS"
            or sp.Rational(certificate["quotient"]) > UPPER
            or (int(row["p"]), row["canonical_q_bits"]) in keys
        )

    high_complete = []
    for period in range(17, 25):
        closure = json.loads((RESEARCH / "experiments" / "exact_frontier" / f"p{period}_closure.json").read_text())
        high_complete.append(
            int(closure["moment_excluded_through_F16"]) + len(closure["survivors"])
            == int(closure["legal_dihedral_orbits"])
        )
        for row in closure["survivors"]:
            certificate = json.loads((RESEARCH.parent / row["certificate_file"]).read_text())
            high_complete.append(
                certificate["target_repetition"]
                or sp.Rational(certificate["certificate"]["rayleigh_lower_bound"]) > UPPER
            )

    csv_path = RESEARCH / "experiments" / "task51" / "subeight_periodic_phases.csv"
    residual = set()
    for row in csv.DictReader(csv_path.open(encoding="utf-8")):
        if row["band_at_8"] != "R_LT_8":
            continue
        period = int(row["primitive_Q_period"])
        key = canonical_key(q_from_bits(row["Q_bits"][:period]))
        if not (key[0] == 4 and int(row["primitive_tau_period"]) == 8):
            residual.add(key)
    checks = {
        "all_witnesses_rebuilt": len(rebuilt) == 16 and all(rebuilt),
        "low_orbits_complete": all(low_complete),
        "high_orbits_complete": all(high_complete),
        "source_csv_bound": hashlib.sha256(csv_path.read_bytes()).hexdigest() == data["source_hashes"]["task51_csv_sha256"],
        "source_low_bound": hashlib.sha256(low_path.read_bytes()).hexdigest() == data["source_hashes"]["low_frontier_sha256"],
        "target_scope_exact": data["theorem"].endswith("R(Q)<c6."),
        "c6_upper_bound": data["c6_upper"] == str(UPPER),
        "residual_orbits_bound": {tuple(row) for row in data["residual_subeight_keys"]} == residual,
        "artifact_checks_true": all(data["checks"].values()),
    }
    if not all(checks.values()):
        raise AssertionError(checks)
    return checks


def main() -> None:
    verify()
    print("TARGET_A_TASK53_P24_VERIFY_PASS")


if __name__ == "__main__":
    main()
