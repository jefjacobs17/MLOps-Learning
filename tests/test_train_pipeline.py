import pytest
import subprocess
import sys

from src.train_pipeline import main


@pytest.mark.parametrize(
    "test_size",
    ["-0.1", "0", "1", "1.5"]
)
def test_invalid_test_sizes(test_size):

    with pytest.raises(ValueError, match="test_size"):
        main(["--test-size", test_size])

def test_pipeline_runs_with_valid_configuration():

    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "src.train_pipeline",
            "--test-size",
            "0.25",
            "--seed",
            "7"
        ],
        capture_output=True,
        text=True,
        check=False
    )

    assert result.returncode == 0
    assert "Model accuracy" in result.stderr

def test_pipeline_fails_with_invalid_configuration():

    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "src.train_pipeline",
            "--test-size",
            "1.5"
        ],
        capture_output=True,
        text=True,
        check=False
    )

    assert result.returncode == 1
    assert "test_size" in result.stderr