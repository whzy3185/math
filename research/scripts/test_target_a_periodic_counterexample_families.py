from verify_target_a_periodic_counterexample_families import verify


def test_periodic_counterexample_families() -> None:
    report = verify()
    assert report["status"] == "PERIODIC_FAMILY_FLOQUET_VERIFY_PASS"
    assert [row["period"] for row in report["families"]] == [10, 12, 14, 18, 22]
