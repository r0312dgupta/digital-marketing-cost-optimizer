import pandas as pd


# Path of the raw input dataset
file_path = "data/raw/digital_marketing_dataset_30k.csv"


# Read CSV file into a Pandas DataFrame
df = pd.read_csv(file_path)

# If something cannot be converted, don't crash the whole conversion; turn that bad date into NaT
df["date"] = pd.to_datetime(
    df["date"],
    format="%d/%m/%Y",
    errors="coerce"
)


print("\n----- INVALID DATES AFTER CONVERSION -----")
print(df["date"].isnull().sum())



# 1. Display first 5 rows
print("\n----- FIRST 5 ROWS -----")
print(df.head())


# 2. Check number of rows and columns
print("\n----- DATASET SHAPE -----")
print(df.shape)


# 3. Display all column names
print("\n----- COLUMN NAMES -----")
print(df.columns.tolist())


# 4. Check data types
print("\n----- DATA TYPES -----")
print(df.dtypes)


# 5. Check missing values
print("\n----- MISSING VALUES -----")
print(df.isnull().sum())


# 6. Check duplicate rows
print("\n----- DUPLICATE ROWS -----")
print(df.duplicated().sum())



print("\n----- YEAR MISMATCHES -----")
print((df["year"] != df["date"].dt.year).sum())

print("\n----- MONTH MISMATCHES -----")
print((df["month"] != df["date"].dt.month).sum())