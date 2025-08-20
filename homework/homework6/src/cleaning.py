import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def fill_missing_median(df: pd.DataFrame, columns: list) -> pd.DataFrame:
    
    for col in columns:
        if col in df.columns and pd.api.types.is_numeric_dtype(df[col]):
            median_val = df[col].median()
            df[col].fillna(median_val, inplace=True)
    return df

def drop_missing(df: pd.DataFrame, threshold: float) -> pd.DataFrame:
    missing_ratio = df.isnull().sum() / len(df)
    cols_to_drop = missing_ratio[missing_ratio > threshold].index
    
    if not cols_to_drop.empty:
        df.drop(columns=cols_to_drop, inplace=True)
    return df

def normalize_data(df: pd.DataFrame, columns: list) -> pd.DataFrame:
    
    scaler = MinMaxScaler()
    for col in columns:
        if col in df.columns and pd.api.types.is_numeric_dtype(df[col]):
            df[col] = scaler.fit_transform(df[[col]])
    return df