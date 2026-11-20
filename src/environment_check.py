import sys
import pandas as pd

# Python version
print("Python version:", sys.version)

# Interpreter path
print("Interpreter path:",sys.executable)

# Pandas version
print("Pandas version:", pd.__version__)

df = pd.DataFrame({"values": [10, 20, 30, 40, 50]})
mean_value = df["values"].mean()
print(mean_value)

min_value = df["values"].min()
print(min_value)

max_value = df["values"].max()
print(max_value)

median_value = df["values"].median()
print(median_value)

# Function to validate numeric data
def validate_numeric_data(df, column):
    # Check whether the column exists
    if column not in df.columns:
        raise ValueError(f"Column '{column}' does not exist in the DataFrame.")

    # Check whether the DataFrame is empty
    if df.empty:
        raise ValueError("The DataFrame is empty.")

    # Attempt to convert every value to a number
    numeric_values = pd.to_numeric(df[column], errors="coerce")

    # Identify values that could not be converted
    invalid_mask = numeric_values.isna()

    # Raise an error if any invalid values are found
    if invalid_mask.any():
        invalid_values = df.loc[invalid_mask, column]

        raise ValueError(
            f"Column '{column}' contains non-numeric or missing values: "
            f"{invalid_values.to_dict()}"
        )

    return True