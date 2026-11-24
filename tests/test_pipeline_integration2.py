from src.train_pipeline import run_pipeline

def test_pipeline_reproducibility():

    first_run = run_pipeline(
        test_size=0.2,
        seed=42
    )

    second_run = run_pipeline(
        test_size=0.2,
        seed=42
    )

    assert first_run["accuracy"] == second_run["accuracy"]
    