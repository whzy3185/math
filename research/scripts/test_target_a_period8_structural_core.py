import unittest

from verify_target_a_period8_structural_core import (
    EXPECTED_D2,
    first_positive_excess,
    legal_q_words,
    separation,
    verify_core,
)


class Period8StructuralCoreTests(unittest.TestCase):
    def test_core_is_classification_independent(self):
        result = verify_core()
        self.assertFalse(result["classification_dependency_used"])
        self.assertEqual(result["categories"], {"below": 4, "equal": 1, "above": 123})

    def test_two_defect_hierarchy(self):
        observed = {}
        for q in legal_q_words():
            if sum(value == 1 for value in q) == 2 and separation(q) < 4:
                observed.setdefault(separation(q), first_positive_excess(q))
        self.assertEqual(observed, EXPECTED_D2)

    def test_target_negative_excess_not_used_as_upper_bound(self):
        target = (1, -1, -1, -1, 1, -1, -1, -1)
        self.assertIsNone(first_positive_excess(target))


if __name__ == "__main__":
    unittest.main()
