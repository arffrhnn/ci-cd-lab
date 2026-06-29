import sys
import os
import pandas as pd
import pytest

# Add src folder to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from main import load_data

def test_load_data():
    # Correctly call load_data with a single filepath argument
    df = load_data("data/IBM_Churn.csv")
    # Ensure assertions are correctly indented within the function
    assert not df.empty, "DataFrame should not be empty"
    assert isinstance(df, pd.DataFrame), "Result should be a Pandas DataFrame"
    assert 'customerID' in df.columns, "DataFrame should contain 'customerID' column"
