from verify_target_a_r2_bulk_hyperbolicity import verify


def test_r2_bulk_hyperbolicity() -> None:
    assert verify()["slow_multiplier_upper"] == "1/3"
