
import os

import pandas as pd

import pandas as pd


def load_data(filepath):

    if filepath.endswith(".dta"):
        return pd.read_stata(filepath)

    elif filepath.endswith(".csv"):
        return pd.read_csv(filepath)

    raise ValueError(
        "Unsupported file format"
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