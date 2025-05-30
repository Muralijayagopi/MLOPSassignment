import pandas as pd

def preprocess_data(df: pd.DataFrame):
    """
    Cleans and preprocesses input DataFrame.
    """
    df = df.copy()
    df = df.dropna()
    df = df[df['YearsExperience'] >= 0]
    return df

def preprocess_input(experience: float):
    """
    Prepares a single input instance for prediction.
    """
    return [[float(experience)]]
