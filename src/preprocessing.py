import pandas as pd


def standardize_columns(df):

    if "Sales" in df.columns:
        df["Revenue"] = df["Sales"]

    if "Quantity" in df.columns:
        df["Quantity Sold"] = df["Quantity"]

    if "Inventory Level" not in df.columns:
        df["Inventory Level"] = 500

    if "Promotion Flag" not in df.columns:
        df["Promotion Flag"] = 0

    if "Holiday Indicator" not in df.columns:
        df["Holiday Indicator"] = 0

    return df


def clean_data(df):

    df.drop_duplicates(inplace=True)

    df = df.ffill()

    df["Order Date"] = pd.to_datetime(
        df["Order Date"]
    )

    return df