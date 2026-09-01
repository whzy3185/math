from verify_target_a_tail_compression import verify


def test_tail_compression_accounting() -> None:
    assert verify() == {"old_rows": 96, "removed_rows": 51, "remaining_rows": 45}
