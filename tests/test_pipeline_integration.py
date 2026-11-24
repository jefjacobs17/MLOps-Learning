from src.train_pipeline import run_pipeline


def test_complete_training_pipeline():

    results = run_pipeline(
        test_size=0.2,
        seed=42
    )

    assert isinstance(results, dict)

    assert "accuracy" in results

    assert 0 <= results["accuracy"] <= 1

    assert results["train_rows"] == 120

    assert results["test_rows"] == 30