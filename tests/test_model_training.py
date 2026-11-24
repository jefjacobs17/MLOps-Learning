import logging

from sklearn.datasets import load_iris

from src.model_training import train_model

def test_training_logs_success(caplog):

    iris = load_iris()

    X = iris.data
    y = iris.target

    caplog.set_level(
        logging.INFO,
        logger="src.model_training"
    )

    train_model(X, y)

    assert "Model training has started" in caplog.text
    assert "Model training completed" in caplog.text

def test_train_model_returns_predictor():
    iris = load_iris()

    X = iris.data
    y = iris.target

    model = train_model(X, y)

    predictions = model.predict(X[:5])

    assert len(predictions) == 5