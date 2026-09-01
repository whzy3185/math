from verify_target_a_r2_k_reduction import verify


def test_r2_k_reduction_comparison() -> None:
    report = verify()
    assert report["status"] == "R2_K_REDUCTION_COMPARISON_PASS"
