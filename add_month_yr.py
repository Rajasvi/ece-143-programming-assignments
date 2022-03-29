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
