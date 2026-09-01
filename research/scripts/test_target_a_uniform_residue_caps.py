from verify_target_a_uniform_residue_caps import verify


def test_uniform_residue_caps() -> None:
    report = verify()
    assert report["status"] == "UNIFORM_CAP_EXACT_FINITE_VERIFY_PASS"
    assert report["total"] == 72
