import pandas as pd
from pandas import DataFrame
from typing import Optional

def load(path: str) -> Optional[DataFrame]:
    try:
        df = pd.read_csv(path)
        print(f"Loading dataset of dimensions {df.shape}")
        return df
    except Exception:
        return None