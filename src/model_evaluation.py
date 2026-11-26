from sklearn.metrics import accuracy_score, precision_score

def evaluate_model(model, X_test, y_test):
    
    #generate predictions
    y_pred = model.predict(X_test)

    #Calculate accuracy
    accuracy = accuracy_score(y_test, y_pred)

    #Calculate precision
    precision = precision_score(
        y_pred,
        y_test,
        average = 'macro',
        zero_division = 0
    )

    #return evaluation results into a dictionary so other functions can use the outouts

    return {
        "accuracy": accuracy
        #"precision": precision
    }

if __name__ == "__main__":

    from sklearn.datasets import load_iris
    from sklearn.model_selection import train_test_split
    from src.model_training import train_model

    # Load sample data
    iris = load_iris()

    X = iris.data
    y = iris.target

    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Train the model
    model = train_model(X_train, y_train)

    # Evaluate the model
    results = evaluate_model(model, X_test, y_test)

    # Display the results
    print(f"Accuracy: {results['accuracy']:.2%}")
    #print(f"Precision: {results['precision']:.2%}")