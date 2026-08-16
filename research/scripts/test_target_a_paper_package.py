import copy
import json
import unittest

from verify_target_a_paper_package import (
    DEFAULT_GRAPH,
    DEFAULT_INVENTORY,
    PaperPackageVerificationError,
    verify_claim_inventory,
    verify_dependency_graph,
    verify_initial_files,
    verify_graph_markdown,
    verify_notation_and_compression,
    verify_claim_evidence_and_reproducibility,
)


class PaperPackageTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.inventory = json.loads(DEFAULT_INVENTORY.read_text(encoding="utf-8"))
        cls.graph = json.loads(DEFAULT_GRAPH.read_text(encoding="utf-8"))

    def test_positive_files(self):
        verify_initial_files()
        verify_notation_and_compression()
        verify_claim_evidence_and_reproducibility()

    def test_claim_gap_rejected(self):
        inventory = copy.deepcopy(self.inventory)
        del inventory["claims"][7]
        with self.assertRaises(PaperPackageVerificationError):
            verify_claim_inventory(inventory)

    def test_artifact_hash_tamper_rejected(self):
        inventory = copy.deepcopy(self.inventory)
        inventory["claims"][0]["sha256"]["main"] = "0" * 64
        with self.assertRaises(PaperPackageVerificationError):
            verify_claim_inventory(inventory)

    def test_dependency_cycle_rejected(self):
        inventory = copy.deepcopy(self.inventory)
        inventory["claims"][1]["dependencies"] = ["C3"]
        inventory["claims"][2]["dependencies"] = ["C2"]
        with self.assertRaises(PaperPackageVerificationError):
            verify_claim_inventory(inventory)

    def test_missing_deletion_effect_rejected(self):
        graph = copy.deepcopy(self.graph)
        del graph["theorems"][5]["deletion_tests"]["C25"]
        with self.assertRaises(PaperPackageVerificationError):
            verify_dependency_graph(graph, self.inventory)

    def test_independent_verification_as_premise_rejected(self):
        graph = copy.deepcopy(self.graph)
        graph["independent_verification_is_logical_dependency"] = True
        with self.assertRaises(PaperPackageVerificationError):
            verify_dependency_graph(graph, self.inventory)

    def test_human_graph_semantic_drift_rejected(self):
        markdown = "| THEOREM_A | wrong | C2 |\n"
        with self.assertRaises(PaperPackageVerificationError):
            verify_graph_markdown(self.graph, markdown)


if __name__ == "__main__":
    unittest.main()
