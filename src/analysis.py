
import os
import pandas as pd
from pathlib import Path


def load_data(filepath):

    filepath = Path(filepath)

    if filepath.suffix == ".dta":
        return pd.read_stata(filepath)

    elif filepath.suffix == ".csv":
        return pd.read_csv(filepath)

    raise ValueError(
        f"Unsupported file format: {filepath.suffix}"
    )


def validate_data(df):

    required_columns = [
        "status1",
        "weight2",
        "wap16"
    ]

    missing_columns = [

        col

        for col in required_columns

        if col not in df.columns

    ]

    if missing_columns:

        raise ValueError(
            f"Missing columns: {missing_columns}"
        )

    return df


def get_working_age_population(df):

    return df[
        df["wap16"] == 1
    ]


def get_youth_population(df):

    return df[
        df["young"] == 1
    ]