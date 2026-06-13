import pandas as pd

REQUIRED_COLUMNS = [
    "Order Date",
    "Product ID",
    "Product Name",
    "Category",
    "Region"
]


def load_dataset(uploaded_file):

    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)

    elif uploaded_file.name.endswith(".xlsx"):
        df = pd.read_excel(uploaded_file)

    else:
        raise ValueError("Unsupported file format")

    return df


def validate_dataset(df):

    missing = []

    for col in REQUIRED_COLUMNS:

        if col not in df.columns:
            missing.append(col)

    return missing