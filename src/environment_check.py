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