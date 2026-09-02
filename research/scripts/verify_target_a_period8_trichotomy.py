"""Exact integer checks for the finite moment sublemma in the period-8 trichotomy."""

from __future__ import annotations


CASES = ((1, 4, 5504), (2, 6, 64336), (3, 9, 2872096))


def tau_from_q(q):
    tau = [1]
    for sign in q[:-1]:
        tau.append(tau[-1] * sign)
    if tau[-1] * q[-1] != 1:
        raise AssertionError("Q word does not close")
    return tau


def transitions(tau, position):
    return ((position - 1, 1), (position + 1, 1), (position - 2, tau[(position - 2) % 8]), (position + 2, tau[position % 8]))


def moments(q, maximum):
    tau = tau_from_q(q)
    states = [{start: 1} for start in range(8)]
    result = []
    for length in range(1, 2 * maximum + 1):
        next_states = []
        for state in states:
            updated = {}
            for position, amplitude in state.items():
                for endpoint, coefficient in transitions(tau, position):
                    updated[endpoint] = updated.get(endpoint, 0) + amplitude * coefficient
            next_states.append(updated)
        states = next_states
        if length % 2 == 0:
            result.append(sum(states[start].get(start, 0) for start in range(8)))
    return result


def verify():
    checks = {}
    for separation, index, expected in CASES:
        q = [-1] * 8
        q[0] = q[separation] = 1
        values = moments(q, 10)
        excess = values[index] - 8 * values[index - 1]
        checks[f"separation_{separation}"] = excess == expected and excess > 0
    if not all(checks.values()):
        raise AssertionError(checks)
    return {"status": "PERIOD8_TRICHOTOMY_MOMENT_SUBLEMMA_PASS", "checks": checks}


if __name__ == "__main__":
    print(verify())
