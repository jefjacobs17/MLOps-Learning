from src.model_evaluation import evaluate_model

class FakeModel:

    def predict(self, X):
        return [0, 1, 0, 0]


def test_evaluation_correctness():

    model = FakeModel()

    X_test = [[1], [2], [3], [4]]
    y_test = [0, 1, 1, 0]

    results = evaluate_model(model, X_test, y_test)

    assert results["accuracy"] == 0.75