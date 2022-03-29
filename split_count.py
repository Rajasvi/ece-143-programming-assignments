import pandas as pd
import numpy as np


def split_count(x):
    """Ths function splits the DataSeries column with multiple comma-separated values into dataframe with count of individual unique values. 

    Args:
        x (Pandas Series): Series column with multiple comma-separated values

    Returns:
        Pandas Dataframe: Dataframe with count for each value repeated in column
    """

    assert isinstance(x, pd.core.series.Series)

    t = x.str.split(",")
    df = pd.DataFrame({"survey_data": t, "count": t.apply(len)})

    exploded_df = df.explode("survey_data")
    exploded_df.survey_data = exploded_df.survey_data.str.strip()
    grp_df = (
        exploded_df.groupby(["survey_data"])["count"].count().sort_values().to_frame()
    )
    grp_df.index.name = None

    return grp_df
