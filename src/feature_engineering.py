def create_features(df):

    df["Day"] = (
        df["Order Date"].dt.day
    )

    df["Month"] = (
        df["Order Date"].dt.month
    )

    df["Year"] = (
        df["Order Date"].dt.year
    )

    df["Quarter"] = (
        df["Order Date"].dt.quarter
    )

    df["Week"] = (
        df["Order Date"]
        .dt.isocalendar()
        .week
    )

    return df