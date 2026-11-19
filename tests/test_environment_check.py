import pandas as pd
import pytest

from src.environment_check import validate_numeric_data


#defines a test function to check the behavior of validate_numeric_data with valid numeric data
def test_valid_numeric_data():
    #create controlled test data with a DataFrame containing numeric values
    df = pd.DataFrame({"values": [10, 20, 30]})

    #call the validate_numeric_data function with the test DataFrame and the column name "values"
    result = validate_numeric_data(df, "values")

    #Checks that the function returns the expected result
    assert result is True

def test_missing_values():
    #create controlled test data with a DataFrame containing missing values
    df = pd.DataFrame({"values": [10, None, 30]})

    #expect the function to raise a ValueError due to the presence of missing values
    with pytest.raises(ValueError):
        validate_numeric_data(df, "values")


def test_empty_dataset():
    #create controlled test data with a DataFrame containing no values
    df = pd.DataFrame({"values": []})

    #expect the function to raise a ValueError due to the presence of no data
    with pytest.raises(ValueError):
        validate_numeric_data(df, "values")



def test_non_numeric_values():
    #create controlled test data with a DataFrame containing non-numeric values
    df = pd.DataFrame({"values": ["a", "b", "c"]})

    #expect the function to raise a ValueError due to the presence of non-numeric values
    with pytest.raises(ValueError):
        validate_numeric_data(df, "values")



def test_missing_column():
    #create controlled test data with a DataFrame missing the specified column
    df = pd.DataFrame({"other_column": [10, 20, 30]})

    #expect the function to raise a ValueError due to the presence of a missing column
    with pytest.raises(ValueError):
        validate_numeric_data(df, "values")

 