import pandas as pd

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