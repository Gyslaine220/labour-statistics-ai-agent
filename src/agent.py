from datetime import datetime

from src.analysis import (
    load_data,
    validate_data
)

from src.config import DATA_PATH

from src.indicators import (
    calculate_lfpr,
    calculate_unemployment_rate,
    calculate_employment_rate,
    calculate_neet_rate
)


# Load and validate data once at startup
DATA = validate_data(
    load_data(DATA_PATH)
)


def build_response(
    question,
    indicator,
    value,
    unit="%"
):
    """
    Standardize all API responses.
    """

    return {
        "question": question,
        "indicator": indicator,
        "value": round(float(value), 2),
        "unit": unit,
        "timestamp": datetime.now().isoformat()
    }


def ask_agent(question):

    original_question = question

    question = question.lower()

    try:

        # Labour Force Participation Rate
        if (
            "lfpr" in question
            or "labour force participation rate" in question
        ):

            return build_response(
                original_question,
                "LFPR",
                calculate_lfpr(DATA)
            )

        # Unemployment Rate
        elif (
            "unemployment rate" in question
            or "unemployment" in question
        ):

            return build_response(
                original_question,
                "Unemployment Rate",
                calculate_unemployment_rate(DATA)
            )

        # Employment-to-Population Ratio
        elif (
            "employment rate" in question
            or "employment-to-population ratio" in question
            or "employment to population ratio" in question
            or "epr" in question
        ):

            return build_response(
                original_question,
                "Employment-to-Population Ratio",
                calculate_employment_rate(DATA)
            )

        # Youth NEET Rate
        elif "neet" in question:

            return build_response(
                original_question,
                "Youth NEET Rate",
                calculate_neet_rate(DATA)
            )

        # Unsupported question
        else:

            return {
                "status": "unknown",
                "question": original_question,
                "message": (
                    "Supported indicators are: "
                    "LFPR, Unemployment Rate, "
                    "Employment-to-Population Ratio "
                    "and Youth NEET Rate."
                ),
                "timestamp": datetime.now().isoformat()
            }

    except Exception as e:

        return {
            "status": "error",
            "question": original_question,
            "message": str(e),
            "timestamp": datetime.now().isoformat()
        }


if __name__ == "__main__":

    questions = [
        "What is LFPR?",
        "What is unemployment rate?",
        "What is employment-to-population ratio?",
        "What is NEET?"
    ]

    for question in questions:

        print(
            ask_agent(question)
        )
