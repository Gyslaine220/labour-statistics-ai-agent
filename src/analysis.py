
import os

import pandas as pd

print(os.getcwd())


def load_data(filepath):
    if filepath.endswith(".dta"):
        return pd.read_stata(filepath)
    elif filepath.endswith(".csv"):
        return pd.read_csv(filepath)
    else:
        raise ValueError("Unsupported file format")


def prepare_data(df):
    return df[df["wap16"] == 1]


def calculate_rate(numerator, denominator):
    return (numerator / denominator) * 100


# Function to calculate the unemployment rate
def calculate_unemployment_rate(unemployed, labour_force):
    if labour_force <= 0:
        return None

    if unemployed < 0 or unemployed > labour_force:
        return None

    return calculate_rate(unemployed, labour_force)


# Function to calculate the labour force participation rate (LFPR)
def calculate_lfpr(labour_force, working_age_population):
    if working_age_population <= 0:
        return None

    if labour_force < 0 or labour_force > working_age_population:
        return None

    return calculate_rate(labour_force, working_age_population)


# Function to calculate the employment rate
def calculate_employment_rate(employed, working_age_population):
    if working_age_population <= 0:
        return None

    if employed < 0 or employed > working_age_population:
        return None

    return calculate_rate(employed, working_age_population)


# Data Validation Function
def validate_data(df):
    required_columns = ["status1", "wap16"]

    missing_columns = [
        column for column in required_columns
        if column not in df.columns
    ]

    if missing_columns:
        raise ValueError(f"Missing required columns: {missing_columns}")

    return df


if __name__ == "__main__":
    df = load_data("Data/RW_LFS2024.dta")
    print("STATUS1:")
    print(df["status1"].value_counts(dropna=False).to_string())
    df = prepare_data(df)
    df = validate_data(df)

    working_age_population = df.loc[
        df["wap16"] == 1, "weight2"
    ].sum()

    employed = df.loc[
        df["status1"] == "Employed", "weight2"
    ].sum()

    unemployed = df.loc[
        df["status1"] == "Unemployed", "weight2"
    ].sum()

    labour_force = employed + unemployed

    unemployment_rate = calculate_unemployment_rate(
        unemployed,
        labour_force,
    )

    lfpr = calculate_lfpr(
        labour_force,
        working_age_population,
    )

    employment_rate = calculate_employment_rate(
        employed,
        working_age_population,
    )

    print("Weighted Working Age Population:", working_age_population)
    print("Weighted Labour Force:", labour_force)
    print("Weighted Employed:", employed)
    print("Weighted Unemployed:", unemployed)
    print("Unemployment Rate:", unemployment_rate, "%")
    print("Labour Force Participation Rate:", lfpr, "%")
    print("Employment Rate:", employment_rate, "%")
    
        # Youth labour-market indicators

    youth_data = df[df["young"] == 1]

    youth_working_age_population = youth_data["weight2"].sum()

    youth_employed = youth_data.loc[
        youth_data["status1"] == "Employed", "weight2"
    ].sum()

    youth_unemployed = youth_data.loc[
        youth_data["status1"] == "Unemployed", "weight2"
    ].sum()

    youth_labour_force = youth_employed + youth_unemployed

    youth_lfpr = calculate_lfpr(
        youth_labour_force,
        youth_working_age_population
    )

    youth_unemployment_rate = calculate_unemployment_rate(
        youth_unemployed,
        youth_labour_force
    )

    youth_employment_rate = calculate_employment_rate(
        youth_employed,
        youth_working_age_population
    )

    # Youth NEET rate
    youth_neet = youth_data.loc[
        youth_data["neetyoung"] == 1, "weight2"
    ].sum()

    youth_neet_rate = calculate_rate(
        youth_neet,
        youth_working_age_population
    )

    print("\n--- Youth Labour-Market Indicators (Age 16–30) ---")
    print("Youth Working-Age Population:", youth_working_age_population)
    print("Youth Labour Force:", youth_labour_force)
    print("Youth Employed:", youth_employed)
    print("Youth Unemployed:", youth_unemployed)
    print("Youth LFPR:", youth_lfpr, "%")
    print("Youth Unemployment Rate:", youth_unemployment_rate, "%")
    print("Youth Employment Rate:", youth_employment_rate, "%")
    print("Youth NEET:", youth_neet)
    print("Youth NEET Rate:", youth_neet_rate, "%")
      
      
      
      
      
      
      