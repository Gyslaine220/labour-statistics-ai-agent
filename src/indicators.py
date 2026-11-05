def calculate_rate(
    numerator,
    denominator
):
    """
    Generic percentage calculator.
    """

    if denominator <= 0:
        return None

    return (
        numerator /
        denominator
    ) * 100


def get_labour_force_stats(df):
    """
    Calculate weighted employed,
    unemployed and labour force.
    """

    employed = df.loc[
        df["status1"] == "Employed",
        "weight2"
    ].sum()

    unemployed = df.loc[
        df["status1"] == "Unemployed",
        "weight2"
    ].sum()

    labour_force = (
        employed +
        unemployed
    )

    return (
        employed,
        unemployed,
        labour_force
    )


def calculate_lfpr(df):
    """
    Labour Force Participation Rate.
    """

    working_age_population = df.loc[
        df["wap16"] == 1,
        "weight2"
    ].sum()

    _, _, labour_force = (
        get_labour_force_stats(df)
    )

    return calculate_rate(
        labour_force,
        working_age_population
    )


def calculate_unemployment_rate(df):
    """
    Unemployment Rate.
    """

    _, unemployed, labour_force = (
        get_labour_force_stats(df)
    )

    return calculate_rate(
        unemployed,
        labour_force
    )


def calculate_employment_rate(df):
    """
    Employment-to-Population Ratio.
    """

    working_age_population = df.loc[
        df["wap16"] == 1,
        "weight2"
    ].sum()

    employed, _, _ = (
        get_labour_force_stats(df)
    )

    return calculate_rate(
        employed,
        working_age_population
    )


def calculate_neet_rate(df):
    """
    Youth NEET Rate.
    """

    youth_df = df[
        df["young"] == 1
    ]

    youth_population = (
        youth_df["weight2"]
        .sum()
    )

    youth_neet = (
        youth_df.loc[
            youth_df["neetyoung"] == 1,
            "weight2"
        ].sum()
    )

    return calculate_rate(
        youth_neet,
        youth_population
    )