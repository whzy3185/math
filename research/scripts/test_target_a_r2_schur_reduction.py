from verify_target_a_r2_schur_reduction import verify


def test_r2_fixed_width_schur_reduction() -> None:
    report = verify()
    assert report["status"] == "R2_FIXED_WIDTH_SCHUR_REDUCTION_PASS"
    assert report["bulk_period_increment"] == 8
