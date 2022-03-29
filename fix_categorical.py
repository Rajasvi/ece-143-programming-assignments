import pandas as pd


def add_month_yr(x):
    """This function takes survey data frame and creates a dataframe with time stamp as re-formatted to month-year format with ID as index.

    Args:
        x (pd.DataFrame): survey data dataframe

    Returns:
        pd.DataFrame: Time dataframe with reformatted column
    """

    assert (
        "Timestamp" in x.columns
    ), "Checks whether Timestamp column is present or not."
    assert (
        x.Timestamp.isnull().sum() == 0
    ), "Check whether Timestamp column is null or not."

    x.Timestamp = pd.to_datetime(x.Timestamp, infer_datetime_format=True)
    x["month-yr"] = x.Timestamp.dt.strftime("%b-%Y")
    time_df = x[["month-yr", "ID"]]
    time_df = time_df.set_index("ID")

    return time_df


def fix_categorical(x):
    """ This function takes the month-yr dataframe column and then return the same dataframe with an updated column of CategoricalDtype that does the sorting based on month-yr index.

    Args:
        x (pd.DataFrame): survey-data dataframe

    Returns:
        pd.DataFrame: Dataframe with fixed updated column
    """

    assert isinstance(x, pd.DataFrame), "Check whether x is dataframe or not"

    month_df = x
    if "month-yr" not in x.columns:
        month_df = add_month_yr(x)
    month_df["Timestamp"] = pd.to_datetime(month_df["month-yr"])
    sorted_months_yrs = list(
        pd.to_datetime(month_df["Timestamp"].unique()).strftime("%b-%Y")
    )
    x["month-yr"] = pd.Categorical(
        x["month-yr"], categories=sorted_months_yrs, ordered=True
    )

    return x
