import pandas as pd
from pandas import DataFrame
from typing import Optional


def load(path: str) -> Optional[DataFrame]:
    """Load a CSV file into a pandas DataFrame.
    Args:
        path (str): The file path to the CSV file.
    Returns:
        Optional[DataFrame]: The loaded DataFrame, or None if loading fails.
    """

    try:
        df = pd.read_csv(path)
        print(f"Loading dataset of dimensions {df.shape}")
        return df
    except Exception:
        return None
