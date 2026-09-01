from verify_target_a_periodic_family_coverage import verify


def test_periodic_family_coverage() -> None:
    report = verify()
    assert report["status"] == "PERIODIC_FAMILY_COVERAGE_PASS"
    assert report["remaining_rows"] == 25
