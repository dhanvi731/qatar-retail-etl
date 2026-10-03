from etl.extract import extract_data
from etl.transform import transform_data

df = extract_data()

print("\n--- BEFORE TRANSFORM ---")
print("Rows:", len(df))
print("Duplicates:", df.duplicated().sum())

df_transformed = transform_data(df)

print("\n--- AFTER TRANSFORM ---")
print("Rows:", len(df_transformed))
print("Duplicates:", df_transformed.duplicated().sum())

print("\n--- CITY VALUES ---")
print(df_transformed["City"].value_counts())

print("\n--- NULL VALUES ---")
print(df_transformed.isnull().sum())