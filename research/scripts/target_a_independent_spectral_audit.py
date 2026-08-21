"""Independent exact spectral-decision audit for large Target A orders.

The representative stream is emitted by the independent C full-space scanner.
This module does not import the production signing, matrix, threshold, or
Rayleigh-certificate implementations. Floating eigenvectors only propose an
integer vector; every accepted exclusion is decided by an exact rational
comparison with a certified algebraic upper bound.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import mmap
import os
import platform
import shutil
import struct
import subprocess
import tempfile
import time
from fractions import Fraction
from pathlib import Path
from typing import Any, Iterator

import numpy as np
import sympy as sp
from sympy.polys.numberfields import to_number_field

from target_a_bracelets import enumerate_direct_q_orbits


SCRIPT_DIR = Path(__file__).resolve().parent
RESEARCH_DIR = SCRIPT_DIR.parent
C_SOURCE = SCRIPT_DIR / "target_a_independent_orbit_scan.c"
PRIMARY_SOURCE = SCRIPT_DIR / "target_a_bracelets.py"
DEFAULT_OUTPUT_DIR = (
    RESEARCH_DIR / "reproducibility" / "target_a_independent_spectral_audit"
)
RECORD = struct.Struct("<QB")


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    temporary.replace(path)


def _compile_scanner(binary: Path) -> dict[str, str]:
    compiler = shutil.which("cc")
    if compiler is None:
        raise RuntimeError("a C11 compiler named 'cc' is required")
    command = [
        compiler,
        "-O3",
        "-std=c11",
        "-Wall",
        "-Wextra",
        "-Werror",
        str(C_SOURCE),
        "-o",
        str(binary),
    ]
    subprocess.run(command, check=True)
    version = subprocess.run(
        [compiler, "--version"], check=True, capture_output=True, text=True
    ).stdout.splitlines()[0]
    return {
        "compiler": compiler,
        "compiler_version": version,
        "command": command,
        "c_source_sha256": _sha256(C_SOURCE),
    }


def _write_primary_comparison_table(n: int, path: Path) -> int:
    universe = 1 << n
    descriptor = os.open(path, os.O_RDWR | os.O_CREAT | os.O_TRUNC, 0o600)
    try:
        os.ftruncate(descriptor, universe)
        table = mmap.mmap(descriptor, universe, access=mmap.ACCESS_WRITE)
    finally:
        os.close(descriptor)
    count = 0
    try:
        for defects in range(0, n + 1, 2):
            for code, orbit_size in enumerate_direct_q_orbits(n, defects):
                if table[code] != 0:
                    raise AssertionError("duplicate primary representative")
                table[code] = orbit_size
                count += 1
        table.flush()
    finally:
        table.close()
    return count


def _emit_independent_records(
    n: int, binary: Path, table_path: Path, records_path: Path
) -> dict[str, Any]:
    process = subprocess.run(
        [str(binary), str(n), str(table_path), str(records_path)],
        check=False,
        capture_output=True,
        text=True,
    )
    if process.returncode != 0:
        raise RuntimeError(
            f"independent scanner failed for n={n}: {process.stderr.strip()}"
        )
    payload = json.loads(process.stdout)
    if payload.get("status") != "PASS":
        raise RuntimeError(f"independent scanner did not pass for n={n}")
    expected_size = payload["independent_representatives"] * RECORD.size
    if records_path.stat().st_size != expected_size:
        raise RuntimeError(f"independent record stream has wrong size for n={n}")
    return payload


def _exact_sign(value: sp.Expr) -> int:
    simplified = sp.simplify(value)
    if simplified == 0:
        return 0
    root = sp.simplify(to_number_field(simplified).to_root())
    if root.is_positive is True:
        return 1
    if root.is_negative is True:
        return -1
    if sp.simplify(root > 0) is sp.true:
        return 1
    if sp.simplify(root < 0) is sp.true:
        return -1
    raise ArithmeticError("could not determine exact algebraic sign")


def _threshold_interval(n: int, digits: int = 25) -> tuple[sp.Expr, Fraction, Fraction]:
    value = sp.simplify(
        4 * (sp.cos(sp.pi / n) ** 2 + sp.cos(2 * sp.pi / n) ** 2)
    )
    variable = sp.Symbol("x")
    polynomial = sp.Poly(sp.minimal_polynomial(value, variable), variable)
    approximation = float(sp.N(value, 18))
    epsilon = sp.Rational(1, 10**digits)
    for (left, right), _multiplicity in polynomial.intervals(eps=epsilon):
        if float(left) <= approximation <= float(right):
            if _exact_sign(value - left) >= 0 and _exact_sign(right - value) >= 0:
                return value, Fraction(left.p, left.q), Fraction(right.p, right.q)
    raise ArithmeticError(f"could not isolate threshold for n={n}")


def _independent_matrix(code: int, n: int, alpha: int) -> np.ndarray:
    if alpha not in (-1, 1):
        raise ValueError("alpha must be -1 or +1")
    q = [1 if (code >> index) & 1 else -1 for index in range(n)]
    tau = [1]
    for index in range(n - 1):
        tau.append(tau[-1] * q[index])
    if tau[-1] * q[-1] != tau[0]:
        raise ValueError("illegal Q parity")

    step_one = [1] * n
    step_one[-1] = alpha
    step_two = [
        tau[index] * step_one[index] * step_one[(index + 1) % n]
        for index in range(n)
    ]
    matrix = np.zeros((n, n), dtype=np.int64)
    for index in range(n):
        for offset, sign in ((1, step_one[index]), (2, step_two[index])):
            target = (index + offset) % n
            if matrix[index, target] != 0 or matrix[target, index] != 0:
                raise AssertionError("edge families collided")
            matrix[index, target] = sign
            matrix[target, index] = sign
    return matrix


def _integer_rayleigh(matrix: np.ndarray, eigenvector: np.ndarray) -> tuple[Fraction, list[int]]:
    vector = np.rint(eigenvector * 10**9).astype(np.int64)
    if not np.any(vector):
        vector[int(np.argmax(np.abs(eigenvector)))] = 1
    image = matrix @ vector
    numerator = sum(int(value) ** 2 for value in image)
    denominator = sum(int(value) ** 2 for value in vector)
    return Fraction(numerator, denominator), [int(value) for value in vector]


def _records(path: Path) -> Iterator[tuple[int, int]]:
    with path.open("rb") as stream:
        while data := stream.read(RECORD.size):
            if len(data) != RECORD.size:
                raise RuntimeError("truncated independent record stream")
            yield RECORD.unpack(data)


def _optimizer_divisibility(matrix: np.ndarray, threshold: sp.Expr) -> dict[str, Any]:
    variable = sp.Symbol("Y")
    square = sp.Matrix(matrix.tolist()) ** 2
    characteristic = sp.Poly(square.charpoly(variable).as_expr(), variable)
    minimal = sp.Poly(sp.minimal_polynomial(threshold, variable), variable)
    quotient, remainder = sp.div(characteristic, minimal)
    if not remainder.is_zero:
        raise AssertionError("distinguished threshold is not an exact squared eigenvalue")
    multiplicity = 1
    while True:
        next_quotient, next_remainder = sp.div(quotient, minimal)
        if not next_remainder.is_zero:
            break
        quotient = next_quotient
        multiplicity += 1
    return {
        "status": "EXACT_THRESHOLD_FACTOR_PASS",
        "threshold_minimal_polynomial": str(minimal.as_expr()),
        "characteristic_degree": characteristic.degree(),
        "threshold_factor_multiplicity": multiplicity,
    }


def audit_order(n: int, binary: Path, work_dir: Path) -> dict[str, Any]:
    if n < 8 or n > 30 or n % 2:
        raise ValueError("n must be an even integer in [8,30]")
    started = time.time()
    table_path = work_dir / f"n{n}-primary-table.bin"
    records_path = work_dir / f"n{n}-independent-records.bin"
    primary_count = _write_primary_comparison_table(n, table_path)
    scanner = _emit_independent_records(n, binary, table_path, records_path)
    table_path.unlink(missing_ok=True)

    threshold, threshold_lower, threshold_upper = _threshold_interval(n)
    certificate_digest = hashlib.sha256()
    completed_representatives = 0
    completed_states = 0
    represented_q_words = 0
    rayleigh_certified = 0
    uncertified: list[dict[str, Any]] = []
    optimizer: dict[str, Any] | None = None
    previous_code = -1

    for code, orbit_size in _records(records_path):
        if code <= previous_code:
            raise AssertionError("independent C records are not strictly increasing")
        previous_code = code
        completed_representatives += 1
        represented_q_words += orbit_size
        for alpha in (-1, 1):
            matrix = _independent_matrix(code, n, alpha)
            state = [code, orbit_size, alpha]
            if code == 0 and alpha == -1:
                optimizer = {
                    "state": state,
                    **_optimizer_divisibility(matrix, threshold),
                }
                decision: dict[str, Any] = {
                    "state": state,
                    "decision": "OPTIMIZER_EXACT_THRESHOLD_FACTOR",
                    "minimal_polynomial": optimizer["threshold_minimal_polynomial"],
                }
            else:
                values, vectors = np.linalg.eigh(matrix.astype(float))
                index = int(np.argmax(np.abs(values)))
                bound, vector = _integer_rayleigh(matrix, vectors[:, index])
                if bound >= threshold_upper:
                    rayleigh_certified += 1
                    decision = {
                        "state": state,
                        "decision": "EXACT_RAYLEIGH_EXCLUSION",
                        "numerator": bound.numerator,
                        "denominator": bound.denominator,
                    }
                else:
                    uncertified.append(
                        {
                            "state": state,
                            "rayleigh_numerator": bound.numerator,
                            "rayleigh_denominator": bound.denominator,
                            "integer_vector": vector,
                        }
                    )
                    decision = {
                        "state": state,
                        "decision": "UNCERTIFIED",
                        "numerator": bound.numerator,
                        "denominator": bound.denominator,
                    }
            certificate_digest.update(
                json.dumps(decision, sort_keys=True, separators=(",", ":")).encode()
            )
            completed_states += 1

    records_sha256 = _sha256(records_path)
    records_path.unlink(missing_ok=True)
    checks = {
        "independent_scanner_passed": scanner["status"] == "PASS",
        "primary_and_independent_record_counts_equal": primary_count
        == scanner["independent_representatives"],
        "all_independent_records_decided": completed_representatives
        == scanner["independent_representatives"],
        "all_legal_q_words_represented": represented_q_words == 1 << (n - 1),
        "both_holonomies_checked": completed_states == 2 * completed_representatives,
        "unique_optimizer_checked_exactly": optimizer is not None,
        "all_nonoptimizers_exactly_excluded": rayleigh_certified
        == completed_states - 1,
        "no_uncertified_state": not uncertified,
    }
    return {
        "schema_version": 1,
        "order": n,
        "status": "PASS" if all(checks.values()) else "FAIL",
        "purpose": "independent reconstruction and exact exclusion of every large-order spectral state",
        "representative_source": "independent C full-space orbit scan, emitted in increasing integer order",
        "matrix_route": "standalone Hamilton-gauge reconstruction in target_a_independent_spectral_audit.py",
        "decision_rule": "floating eigenvector proposal followed by exact integer Rayleigh quotient >= certified algebraic threshold upper endpoint",
        "threshold_squared": str(threshold),
        "threshold_interval": [str(threshold_lower), str(threshold_upper)],
        "canonical_representatives": completed_representatives,
        "spectral_states": completed_states,
        "represented_q_words": represented_q_words,
        "represented_switching_classes": 4 * represented_q_words,
        "holonomies": [-1, 1],
        "rayleigh_certified_nonoptimizers": rayleigh_certified,
        "uncertified_states": uncertified,
        "optimizer": optimizer,
        "ordered_independent_certificate_sha256": certificate_digest.hexdigest(),
        "independent_record_stream_sha256": records_sha256,
        "scanner_summary": scanner,
        "checks": checks,
        "elapsed_seconds": time.time() - started,
    }


def run(orders: list[int], output_dir: Path, work_dir: Path) -> dict[str, Any]:
    output_dir.mkdir(parents=True, exist_ok=True)
    work_dir.mkdir(parents=True, exist_ok=True)
    binary = work_dir / "target_a_independent_orbit_scan"
    build = _compile_scanner(binary)
    results = []
    for n in orders:
        result = audit_order(n, binary, work_dir)
        detail_path = output_dir / f"n{n}.json"
        _write_json(detail_path, result)
        results.append((result, detail_path))
    summary = {
        "schema_version": 1,
        "status": "PASS" if all(item[0]["status"] == "PASS" for item in results) else "FAIL",
        "orders": orders,
        "command": "python research/scripts/target_a_independent_spectral_audit.py --n "
        + " ".join(str(n) for n in orders),
        "environment": {
            "python": platform.python_version(),
            "numpy": np.__version__,
            "sympy": sp.__version__,
            "platform": platform.platform(),
        },
        "sources": {
            "driver": {
                "path": "research/scripts/target_a_independent_spectral_audit.py",
                "sha256": _sha256(Path(__file__)),
            },
            "independent_c_scanner": {
                "path": "research/scripts/target_a_independent_orbit_scan.c",
                "sha256": _sha256(C_SOURCE),
            },
            "primary_comparison_stream": {
                "path": "research/scripts/target_a_bracelets.py",
                "sha256": _sha256(PRIMARY_SOURCE),
                "role": "comparison table only; spectral records are emitted by the C full-space scan",
            },
        },
        "build": build,
        "results": [
            {
                "order": result["order"],
                "status": result["status"],
                "canonical_representatives": result["canonical_representatives"],
                "spectral_states": result["spectral_states"],
                "rayleigh_certified_nonoptimizers": result[
                    "rayleigh_certified_nonoptimizers"
                ],
                "ordered_independent_certificate_sha256": result[
                    "ordered_independent_certificate_sha256"
                ],
                "file": path.name,
                "file_sha256": _sha256(path),
                "elapsed_seconds": result["elapsed_seconds"],
            }
            for result, path in results
        ],
    }
    _write_json(output_dir / "summary.json", summary)
    return summary


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", nargs="+", type=int, default=[24, 26, 28, 30])
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--work-dir", type=Path)
    args = parser.parse_args()
    if args.work_dir is not None:
        args.work_dir.mkdir(parents=True, exist_ok=True)
        summary = run(args.n, args.output_dir, args.work_dir)
    else:
        with tempfile.TemporaryDirectory(prefix="target-a-spectral-audit-") as temporary:
            summary = run(args.n, args.output_dir, Path(temporary))
    print(json.dumps(summary, indent=2))
    raise SystemExit(0 if summary["status"] == "PASS" else 1)


if __name__ == "__main__":
    main()
