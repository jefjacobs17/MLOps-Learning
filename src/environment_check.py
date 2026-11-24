import sys
import pandas as pd
from src.data_validation import validate_numeric_data

def main():
    # Display Python environment information
    print("Python version:", sys.version)
    print("Interpreter path:", sys.executable)
    print("Pandas version:", pd.__version__)

    # Create a sample DataFrame for demonstration
    df = pd.DataFrame({"values": [10, 20, 30, 40, 50]})

    # Validate the sample dataset
    result = validate_numeric_data(df, "values")
    print("Validation result:", result)

    mean_value = df["values"].mean()
    print(mean_value)

    min_value = df["values"].min()
    print(min_value)

    max_value = df["values"].max()
    print(max_value)

    median_value = df["values"].median()
    print(median_value)

if __name__ == "__main__":
    main()