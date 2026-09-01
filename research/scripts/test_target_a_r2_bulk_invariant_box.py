from verify_target_a_r2_bulk_invariant_box import verify


def test_r2_bulk_invariant_box() -> None:
    report = verify()
    assert report["status"] == "R2_BULK_INVARIANT_BOX_PASS"
    assert report["entry_steps"] == 4
