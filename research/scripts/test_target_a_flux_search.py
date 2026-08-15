import unittest
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))

from target_a_flux_search import (
    canonical_q_code,
    count_orbits,
    dihedral_orbit,
    enumerate_q_orbits,
    q_code_from_signing,
    signing_from_q,
)
from target_a_reproduce import numpy_matrix, signing_from_class_code
from target_a_quotient_audit import burnside_even_bracelets, dihedral_switching_relation


class FluxSearchTests(unittest.TestCase):
    def test_n8_raw_states_preserve_spectral_radius(self) -> None:
        n = 8
        observed_states = set()
        for code in range(1 << (n + 1)):
            signing = signing_from_class_code(n, code)
            q_code, alpha = q_code_from_signing(signing)
            observed_states.add((canonical_q_code(q_code, n), alpha))
            reconstructed = signing_from_q(q_code, n, alpha)
            original_rho = max(abs(np.linalg.eigvalsh(numpy_matrix(signing))))
            reconstructed_rho = max(abs(np.linalg.eigvalsh(numpy_matrix(reconstructed))))
            self.assertAlmostEqual(original_rho, reconstructed_rho, places=11)
        self.assertEqual(len(observed_states), count_orbits(n)["spectral_states_with_alpha"])

    def test_known_bracelet_counts(self) -> None:
        n20 = count_orbits(20)
        self.assertEqual(n20["q_orbits"], 13648)
        self.assertEqual(n20["spectral_states_with_alpha"], 27296)

        n22 = count_orbits(22)
        self.assertEqual(n22["q_orbits"], 48734)
        self.assertEqual(n22["spectral_states_with_alpha"], 97468)
        self.assertEqual(
            n22["q_orbits_by_defect"],
            {
                "0": 1,
                "2": 11,
                "4": 195,
                "6": 1782,
                "8": 7440,
                "10": 14938,
                "12": 14938,
                "14": 7440,
                "16": 1782,
                "18": 195,
                "20": 11,
                "22": 1,
            },
        )

    def test_n8_all_dihedral_members_have_exact_relations(self) -> None:
        n = 8
        q_orbits = list(enumerate_q_orbits(n))
        self.assertEqual(len(q_orbits), burnside_even_bracelets(n))
        for code, orbit_size in q_orbits:
            orbit = dihedral_orbit(code, n)
            self.assertEqual(len(orbit), orbit_size)
            for alpha in (-1, 1):
                reference = signing_from_q(code, n, alpha)
                for member in orbit:
                    target = signing_from_q(member, n, alpha)
                    self.assertIsNotNone(dihedral_switching_relation(reference, target))


if __name__ == "__main__":
    unittest.main()
