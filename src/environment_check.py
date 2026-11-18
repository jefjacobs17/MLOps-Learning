import sys
import pandas as pd

# Python version
print("Python version:", sys.version)

# Interpreter path
print("Interpreter path:",sys.executable)

# Pandas version
print("Pandas version:", pd.__version__)

df = pd.DataFrame({"values": [10, 20, 30 ,40, 50]})
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
    if column not in df.columns:
        raise ValueError(f"Column '{column}' does not exist in the DataFrame.")
    
    if not pd.api.types.is_numeric_dtype(df[column]):
        raise TypeError(f"Column '{column}' is not numeric.")
    
    return True