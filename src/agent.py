from analysis import (
    load_data,
    calculate_lfpr,
    calculate_unemployment_rate,
    calculate_employment_rate
)


def ask_agent(question):
    question = question.lower()

    # Labour Force Participation Rate
    if (
        "labour force participation rate" in question
        or "lfpr" in question
    ):
        df = load_data("Data/RW_LFS2024.dta")

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

        lfpr = calculate_lfpr(
            labour_force,
            working_age_population
        )

        return f"The Labour Force Participation Rate is {lfpr:.2f}%."

    # Unemployment Rate
    if "unemployment rate" in question:
        df = load_data("Data/RW_LFS2024.dta")

        employed = df.loc[
            df["status1"] == "Employed", "weight2"
        ].sum()

        unemployed = df.loc[
            df["status1"] == "Unemployed", "weight2"
        ].sum()

        labour_force = employed + unemployed 

        unemployment_rate = calculate_unemployment_rate(
            unemployed,
            labour_force
        )

        return f"The unemployment rate is {unemployment_rate:.2f}%."

    # Employment_to_Population Ratio
    if (

        "employment rate" in question

        or "employment-to-population ratio" in question

        or "employment to population ratio" in question

        or "epr" in question

    ):

        df = load_data("Data/RW_LFS2024.dta")

        working_age_population = df.loc[

            df["wap16"] == 1, "weight2"

        ].sum()

        employed = df.loc[

            df["status1"] == "Employed", "weight2"

        ].sum()

        employment_rate = calculate_employment_rate(

            employed,

            working_age_population

        )

        return (

            f"The Employment-to-Population Ratio is "

            f"{employment_rate:.2f}%."

        )

    return "I don't know how to answer that yet."



print(ask_agent("What is the employment-to-population ratio?"))
print(ask_agent("What is the LFPR?"))
print(ask_agent("What is the unemployment rate?"))
print(ask_agent("What is the employment rate?"))