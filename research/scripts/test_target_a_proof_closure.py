from verify_target_a_proof_closure import verify


def test_target_a_proof_closure_documents() -> None:
    report = verify()
    assert report == {"documents": 24, "verifiers": 0}
