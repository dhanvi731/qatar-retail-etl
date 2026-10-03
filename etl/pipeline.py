from etl.extract import extract_data
from etl.transform import transform_data
from etl.load import load_data


def run_pipeline():

    print("Starting ETL pipeline...")

    # EXTRACT
    df = extract_data()
    print(f"Extracted {len(df)} rows")

    # TRANSFORM
    df = transform_data(df)
    print(f"Transformed data: {len(df)} rows")

    # LOAD
    load_data(df)

    print("ETL pipeline completed successfully!")


if __name__ == "__main__":
    run_pipeline()