import pandas as pd
from etl.database import get_connection


def extract_data():

    connection = get_connection()

    query = "SELECT * FROM qatarret"

    df = pd.read_sql(query, connection)
    print("Extraction successful!")
    print("Rows extracted:", len(df))
    print(df.head())

    connection.close()

    return df

extract_data()