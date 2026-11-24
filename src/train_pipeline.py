import logging
import argparse
from sys import argv
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from src.data_validation import validate_numeric_data
from src.model_training import train_model

logger = logging.getLogger(__name__)

#argparse for command line arguments
def parse_args(argv=None):

    parser = argparse.ArgumentParser(
        description="Train an Iris classification model"
    )

    parser.add_argument(
        "--test-size",
        type=float,
        default=0.2,
        help="Proportion of data used for testing"
    )

    parser.add_argument(
        "--seed",
        type=int,
        default=42,
        help="Random seed for reproducibility"
    )

    return parser.parse_args(argv)

def run_pipeline(test_size=0.2, seed=42):

    # Validate configuration
    if not 0 < test_size < 1:
        raise ValueError(
            "test_size must be greater than 0 and less than 1"
        )

    logger.info("Loading Iris dataset")

    iris = load_iris(as_frame=True)

    X = iris.data
    y = iris.target

    logger.info("Dataset loaded: %s rows", len(X))

    # Validate all feature columns
    for column in X.columns:
        validate_numeric_data(X, column)

    logger.info("Data validation successful")

    # Split the dataset
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=test_size,
        random_state=seed,
        stratify=y
    )

    # Train the model
    model = train_model(X_train, y_train)

    # Generate predictions
    predictions = model.predict(X_test)

    # Evaluate
    accuracy = accuracy_score(y_test, predictions)

    logger.info("Model accuracy: %.3f", accuracy)

    return {
        "accuracy": float(accuracy),
        "train_rows": len(X_train),
        "test_rows": len(X_test)
    }

def main(argv=None):

    args = parse_args(argv)

    logger.info("Training pipeline started")

    results = run_pipeline(
        test_size=args.test_size,
        seed=args.seed
    )

    logger.info("Training pipeline completed")

    return results


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )

    try:
        main()

    except ValueError as error:
        logger.error("Training pipeline failed: %s", error)
        raise SystemExit(1) from error