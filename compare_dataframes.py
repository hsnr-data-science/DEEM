import pandas as pd
import numpy as np

import pandas as pd
import numpy as np

def compare_dataframes(df1: pd.DataFrame, df2: pd.DataFrame, decimal_places=2) -> bool:
    """
    Compares two DataFrames for equality, ignoring column order, case differences in column names, 
    and allowing rounding tolerance. Handles cases where a column has only NaN/None values.

    Args:
        df1 (pd.DataFrame): First DataFrame.
        df2 (pd.DataFrame): Second DataFrame (e.g., read from CSV).
        decimal_places (int): Number of decimal places for comparison (default is 2).

    Returns:
        bool: True if all columns match, False otherwise. Prints mismatched columns if any exist.
    """
    # Normalize column names to lowercase
    df1.columns = df1.columns.str.lower()
    df2.columns = df2.columns.str.lower()

    # Ensure both DataFrames have the same set of columns
    if set(df1.columns) != set(df2.columns):
        print("Mismatched columns:", set(df1.columns).symmetric_difference(set(df2.columns)))
        return False

    # Align columns by sorted column names (order irrelevant)
    common_columns = sorted(df1.columns)
    df1_aligned = df1[common_columns].reset_index(drop=True)
    df2_aligned = df2[common_columns].reset_index(drop=True)

    # Ensure same shape
    if df1_aligned.shape != df2_aligned.shape:
        print(f"Different shapes: {df1_aligned.shape} vs {df2_aligned.shape}")
        return False

    # Compare each column
    mismatched_columns = []
    for col in common_columns:
        col1 = df1_aligned[col]
        col2 = df2_aligned[col]

        if col1.isna().all() and col2.isna().all():
            continue

        try:
            if not np.allclose(col1.fillna(0), col2.fillna(0), atol=10**(-decimal_places), equal_nan=True):
                mismatched_columns.append(col)
        except TypeError:
            # For non-numeric columns, use string comparison with NA handling
            if not col1.fillna("").equals(col2.fillna("")):
                mismatched_columns.append(col)

    if mismatched_columns:
        print("Columns that don't match:", mismatched_columns)
        return False

    return True

