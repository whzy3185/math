"""Exact structural reconnaissance for replacing recovered-order enumeration."""

from __future__ import annotations

import json
from pathlib import Path


REPO = Path(__file__).resolve().parents[2]
SOURCE = REPO / "research/proofs/task55/certificates/small_order_exact_classification.json"
OUTPUT = REPO / "research/proof_closure/equality_analytic_search.json"


def recurrent_components(adjacency: dict[int, list[tuple[int, int]]]) -> list[tuple[list[int], int]]:
    index: dict[int, int] = {}
    lowlink: dict[int, int] = {}
    stack: list[int] = []
    on_stack: set[int] = set()
    components: list[tuple[list[int], int]] = []

    def visit(vertex: int) -> None:
        index[vertex] = len(index)
        lowlink[vertex] = index[vertex]
        stack.append(vertex)
        on_stack.add(vertex)
        for neighbor, _bit in adjacency[vertex]:
            if neighbor not in index:
                visit(neighbor)
                lowlink[vertex] = min(lowlink[vertex], lowlink[neighbor])
            elif neighbor in on_stack:
                lowlink[vertex] = min(lowlink[vertex], index[neighbor])
        if lowlink[vertex] == index[vertex]:
            component: list[int] = []
            while True:
                member = stack.pop()
                on_stack.remove(member)
                component.append(member)
                if member == vertex:
                    break
            members = set(component)
            edges = sum(
                1 for member in members for neighbor, _bit in adjacency[member]
                if neighbor in members
            )
            if edges:
                components.append((sorted(component), edges))

    for vertex in adjacency:
        if vertex not in index:
            visit(vertex)
    return components


def cycle_word(component: list[int], adjacency: dict[int, list[tuple[int, int]]]) -> str:
    members = set(component)
    if not component or any(sum(neighbor in members for neighbor, _ in adjacency[vertex]) != 1 for vertex in members):
        return ""
    start = min(component)
    current = start
    bits: list[str] = []
    while not bits or current != start:
        next_vertex, bit = next((neighbor, bit) for neighbor, bit in adjacency[current] if neighbor in members)
        bits.append(str(bit))
        current = next_vertex
    return "".join(bits)


def analyze_order(row: dict[str, object]) -> dict[str, object]:
    support = int(row["support_length"])
    window_length = support + 1
    survivors = row["local_window_partition"]["surviving_window_codes"]
    mask = (1 << (window_length - 1)) - 1
    adjacency: dict[int, list[tuple[int, int]]] = {}
    for code in survivors:
        source = code & mask
        target = code >> 1
        bit = (code >> (window_length - 1)) & 1
        adjacency.setdefault(source, []).append((target, bit))
        adjacency.setdefault(target, [])
    components = []
    for members, edges in recurrent_components(adjacency):
        components.append({
            "states": len(members),
            "edges": edges,
            "contains_reference": members == [0],
            "cycle_word": cycle_word(members, adjacency),
        })
    return {
        "n": row["n"],
        "support_length": support,
        "all_windows": 1 << window_length,
        "surviving_windows": len(survivors),
        "automaton_states": row["overlap_automaton_state_count"],
        "rooted_even_closed_words": row["rooted_even_closed_walk_count"],
        "terminal_states": row["terminal_state_count"],
        "recurrent_components": sorted(components, key=lambda item: (item["states"], item["edges"])),
    }


def run() -> dict[str, object]:
    source = json.loads(SOURCE.read_text(encoding="utf-8"))
    records = [analyze_order(row) for row in source["orders"]]
    payload = {
        "status": "EXACT_STRUCTURAL_RECONNAISSANCE_ONLY",
        "scope": "Uses the already-certified local-window language; it does not promote the language classification to an analytic theorem.",
        "trace_fourth_moment": {
            "n_assumption": "n>=9, so step offsets do not collide",
            "identity": "tr(A^4)=20*n+16*d(Q)",
            "consequence": "rho(A)^2>=sqrt(20+16*d(Q)/n)<=6 by this moment alone",
            "obstruction": "The benchmark tends to 8, so fourth moments cannot prove equality optimality.",
        },
        "orders": records,
    }
    OUTPUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"status": payload["status"], "orders": len(records)}, sort_keys=True))
    return payload


if __name__ == "__main__":
    run()
