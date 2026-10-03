import pandas as pd


def transform_data(df):

    df = df.copy()

    # Clean column names
    df.columns = df.columns.str.strip()

    # Remove exact duplicate rows
    df = df.drop_duplicates()

    # Clean city names
    df["City"] = df["City"].str.strip().str.title()

    # Keep Order Date as it is
    # We are not converting or deleting dates
    df["Order Date"] = df["Order Date"].astype(str).str.strip()

    # Make numeric columns numeric
    numeric_columns = [
        "Quantity",
        "Unit Price",
        "Discount",
        "Revenue",
        "Cost",
        "Profit"
    ]

    for column in numeric_columns:
        df[column] = pd.to_numeric(df[column], errors="coerce")

    return df