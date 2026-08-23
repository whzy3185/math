"""Produce the exact finite Task 56 reference-relative graph artifact."""

from __future__ import annotations

import hashlib
import itertools
import json
import math
from collections import defaultdict
from fractions import Fraction
from pathlib import Path

import numpy as np

from target_a_low_period_spectral_frontier import _candidate_vectors
from target_a_task51_crystallization import local_rayleigh_matrix


RESEARCH = Path(__file__).resolve().parents[1]
OUTPUT = RESEARCH / "proofs" / "task56" / "reference_graph"
CERTIFICATE = OUTPUT / "reference_graph_certificate.json"
MOMENTS = RESEARCH / "experiments" / "task52" / "c6_weighted_moments.json"
LO = Fraction(7905369311620327, 10**15)
HI = Fraction(7905369311620328, 10**15)
REFERENCE = (-1, -1, -1, 1)
EXPECTED = {
    "survivors": "1e5e9b94ad9de75260178d5198d2d685f658d1aa7ecacd0c692cbcb4a253d789",
    "nodes": "58027a627c037f951c2fbe217f8365b6fbf8359dad8418d84595e29164cf066d",
    "edges": "6384cd123c6271a2daf3e3924e43d61c57abc49ebf506e170e525ad28a918fb9",
    "F4": "db3f26e1792b3fb7ca19898512612a3530e8455991059d91ca81cf16b153e2a8",
    "F5": "ccc95e75d6c451bd3a3fa31e1c8140b27eb274cdf950073fc177a9bbaf5b99eb",
}

Pair = tuple[int, int]


def bits(word: tuple[int, ...]) -> str:
    return "".join("1" if value == 1 else "0" for value in word)


def digest(lines) -> str:
    return hashlib.sha256("\n".join(lines).encode("ascii")).hexdigest()


def add(left: Pair, right: Pair) -> Pair:
    return left[0] + right[0], left[1] + right[1]


def sub(left: Pair, right: Pair) -> Pair:
    return left[0] - right[0], left[1] - right[1]


def bounds(pair: Pair) -> tuple[Fraction, Fraction]:
    a_value, b_value = pair
    endpoints = (a_value + b_value * LO, a_value + b_value * HI)
    return min(endpoints), max(endpoints)


def less(left: Pair, right: Pair) -> bool:
    difference = sub(left, right)
    lower, upper = bounds(difference)
    if upper < 0:
        return True
    if lower > 0 or difference == (0, 0):
        return False
    raise ArithmeticError(f"undecided Q(c6) sign: {difference}")


def pair_json(pair: Pair) -> dict:
    lower, upper = bounds(pair)
    return {
        "A": pair[0],
        "B": pair[1],
        "meaning": "A+B*c6",
        "interval": [str(lower), str(upper)],
    }


def build_grammar() -> tuple[list[tuple[int, ...]], dict]:
    survivors = set()
    excluded_tau = 0
    for tau in itertools.product((-1, 1), repeat=12):
        square = local_rayleigh_matrix(tau, 10)
        excluded = False
        for vector in _candidate_vectors(square):
            column = np.asarray(vector, dtype=np.int64)
            quotient = Fraction(int(column @ square @ column), int(column @ column))
            if quotient > HI:
                excluded = True
                break
        q_word = tuple(tau[index] * tau[index + 1] for index in range(11))
        if excluded:
            excluded_tau += 1
        else:
            survivors.add(q_word)
    result = sorted(survivors)
    survivor_hash = digest(bits(word) for word in result)
    assert excluded_tau == 3768 and len(result) == 164
    assert survivor_hash == EXPECTED["survivors"]
    return result, {
        "tau_windows": 4096,
        "excluded_tau_windows": excluded_tau,
        "survivor_q_windows": len(result),
        "survivor_sha256": survivor_hash,
        "boundary": (
            "FP64 proposes integer vectors; exclusion accepts only an exact rational "
            "Rayleigh quotient above the rational c6 upper endpoint."
        ),
    }


def load_forms() -> dict[str, dict[tuple[int, ...], Pair]]:
    raw = json.loads(MOMENTS.read_text(encoding="utf-8"))["forms"]
    forms = {}
    for name in ("F4", "F5"):
        forms[name] = {}
        for key, row in raw[name]["coefficients_a_plus_b_c6"].items():
            support = () if key == "const" else tuple(map(int, key.split(",")))
            forms[name][support] = (row["rational"], row["c6_coefficient"])
    return forms


def density(form: dict[tuple[int, ...], Pair], word: tuple[int, ...]) -> Pair:
    total = (0, 0)
    for support, coefficient in form.items():
        monomial = math.prod(word[index] for index in support)
        total = add(total, (monomial * coefficient[0], monomial * coefficient[1]))
    return total


def cyclic_sccs(adjacency: dict[int, list[int]], count: int) -> list[list[int]]:
    index = 0
    indices = {}
    low = {}
    stack = []
    on_stack = set()
    components = []

    def visit(vertex: int) -> None:
        nonlocal index
        indices[vertex] = low[vertex] = index
        index += 1
        stack.append(vertex)
        on_stack.add(vertex)
        for target in adjacency.get(vertex, []):
            if target not in indices:
                visit(target)
                low[vertex] = min(low[vertex], low[target])
            elif target in on_stack:
                low[vertex] = min(low[vertex], indices[target])
        if low[vertex] == indices[vertex]:
            component = []
            while True:
                member = stack.pop()
                on_stack.remove(member)
                component.append(member)
                if member == vertex:
                    break
            components.append(sorted(component))

    for vertex in range(count):
        if vertex not in indices:
            visit(vertex)
    return sorted(
        (
            component
            for component in components
            if len(component) > 1
            or any(vertex in adjacency.get(vertex, []) for vertex in component)
        ),
        key=lambda component: (len(component), component),
    )


def analyze(name: str, edges: list[dict], reference_vertices: set[int], count: int) -> dict:
    distance = [(0, 0)] * count
    for pass_index in range(count):
        changed = False
        for edge in edges:
            candidate = add(distance[edge["source"]], edge[name])
            if less(candidate, distance[edge["target"]]):
                distance[edge["target"]] = candidate
                changed = True
        if not changed:
            break
    else:
        raise AssertionError(f"{name}: negative cycle")

    slacks = [
        add(edge[name], sub(distance[edge["source"]], distance[edge["target"]]))
        for edge in edges
    ]
    assert all(not less(slack, (0, 0)) for slack in slacks)
    assert all(bounds(slack)[0] > 0 for slack in slacks if slack != (0, 0))
    potential_hash = digest(
        f"{vertex}:{pair[0]},{pair[1]}" for vertex, pair in enumerate(distance)
    )
    assert potential_hash == EXPECTED[name]
    zero_graph = defaultdict(list)
    zero_edges = []
    for edge_id, (edge, slack) in enumerate(zip(edges, slacks)):
        if slack == (0, 0):
            zero_graph[edge["source"]].append(edge["target"])
            zero_edges.append(edge_id)
    components = cyclic_sccs(zero_graph, count)
    assert len(components) == 4
    assert all(len(component) == 4 for component in components)
    assert all(set(component) <= reference_vertices for component in components)
    assert set().union(*map(set, components)) == reference_vertices
    minimum = min(
        (slack for slack in slacks if slack != (0, 0)),
        key=lambda pair: sum(bounds(pair)),
    )
    return {
        "status": "NO_NEGATIVE_CYCLE_EXACT",
        "bellman_ford_passes": pass_index + 1,
        "potential_sha256": potential_hash,
        "potential": [
            {"vertex": vertex, "A": pair[0], "B": pair[1]}
            for vertex, pair in enumerate(distance)
        ],
        "zero_reduced_edge_ids": zero_edges,
        "zero_cyclic_sccs": components,
        "minimum_positive_reduced_slack": pair_json(minimum),
        "conclusion": "Every directed cycle is nonnegative and every zero cycle is reference.",
    }


def build_certificate() -> dict:
    survivors, grammar = build_grammar()
    forms = load_forms()
    nodes = sorted({word[:-1] for word in survivors} | {word[1:] for word in survivors})
    base_edges = sorted((word[:-1], word[1:], word) for word in survivors)
    node_hash = digest(bits(node) for node in nodes)
    edge_hash = digest(
        f"{bits(source)}>{bits(target)}:{bits(word)}"
        for source, target, word in base_edges
    )
    assert len(nodes) == 105 and len(base_edges) == 164
    assert node_hash == EXPECTED["nodes"] and edge_hash == EXPECTED["edges"]

    reference_nodes = [
        tuple(REFERENCE[(phase + offset) % 4] for offset in range(10))
        for phase in range(4)
    ]
    reference_edges = [
        tuple(REFERENCE[(phase + offset) % 4] for offset in range(11))
        for phase in range(4)
    ]
    vertices = [(node, phase) for node in nodes for phase in range(4)]
    vertex_id = {vertex: index for index, vertex in enumerate(vertices)}
    lifted_edges = []
    for source, target, word in base_edges:
        for phase in range(4):
            lifted_edges.append({
                "source": vertex_id[(source, phase)],
                "target": vertex_id[(target, (phase + 1) % 4)],
                "phase": phase,
                "q_word": word,
                **{
                    name: sub(density(form, word), density(form, reference_edges[phase]))
                    for name, form in forms.items()
                },
            })
    assert len(vertices) == 420 and len(lifted_edges) == 656
    reference_vertices = {
        vertex_id[(node, phase)] for node in reference_nodes for phase in range(4)
    }
    analyses = {
        name: analyze(name, lifted_edges, reference_vertices, len(vertices))
        for name in ("F4", "F5")
    }
    return {
        "schema": "target-a-task56-reference-graph-v1",
        "status": "EXACT_FINITE_PRODUCER",
        "evidence_boundary": (
            "No independent checker and no spectral bridge from relative moment cost "
            "to the operator spectral edge."
        ),
        "inputs": {
            "c6_interval": [str(LO), str(HI)],
            "moment_file": str(MOMENTS.relative_to(RESEARCH)),
            "moment_file_sha256": hashlib.sha256(MOMENTS.read_bytes()).hexdigest(),
            "producer_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        },
        "grammar": {
            **grammar,
            "base_states": 105,
            "base_edges": 164,
            "state_sha256": node_hash,
            "edge_sha256": edge_hash,
            "survivors": [bits(word) for word in survivors],
        },
        "reference": {
            "q_period_bits": bits(REFERENCE),
            "state_windows": [bits(word) for word in reference_nodes],
            "edge_windows": [bits(word) for word in reference_edges],
            "calibration": "density_F(edge)-density_F(reference_edge_at_phase)",
            "reference_lifted_vertex_ids": sorted(reference_vertices),
        },
        "lifted_graph": {
            "states": [
                {"vertex": index, "q10_bits": bits(node), "phase": phase}
                for index, (node, phase) in enumerate(vertices)
            ],
            "edges": [
                {
                    "edge": index,
                    "source": edge["source"],
                    "target": edge["target"],
                    "phase": edge["phase"],
                    "q11_bits": bits(edge["q_word"]),
                    "F4": {"A": edge["F4"][0], "B": edge["F4"][1]},
                    "F5": {"A": edge["F5"][0], "B": edge["F5"][1]},
                }
                for index, edge in enumerate(lifted_edges)
            ],
        },
        "analyses": analyses,
        "checks": {
            "base_graph_105_164": True,
            "phase_lift_420_656": True,
            "F4_no_negative_cycle": True,
            "F5_no_negative_cycle": True,
            "F4_zero_cycles_reference_only": True,
            "F5_zero_cycles_reference_only": True,
        },
    }


def main() -> None:
    OUTPUT.mkdir(parents=True, exist_ok=True)
    payload = build_certificate()
    temporary = CERTIFICATE.with_suffix(".json.tmp")
    temporary.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    temporary.replace(CERTIFICATE)
    print(json.dumps({
        "status": payload["status"],
        "certificate": str(CERTIFICATE),
        "sha256": hashlib.sha256(CERTIFICATE.read_bytes()).hexdigest(),
        "base_graph": [105, 164],
        "phase_lift": [420, 656],
        "F4": payload["analyses"]["F4"]["status"],
        "F5": payload["analyses"]["F5"]["status"],
    }, indent=2))


if __name__ == "__main__":
    main()
