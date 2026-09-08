import pandas as pd


# Load raw dataset
file_path = "data/raw/digital_marketing_dataset_30k.csv"

df = pd.read_csv(file_path)


# Convert date from text to datetime
df["date"] = pd.to_datetime(
    df["date"],
    format="%d/%m/%Y"
)


# Basic data quality checks
print("\n----- DATE TYPE AFTER CONVERSION -----")
print(df["date"].dtype)


print("\n----- DATE RANGE -----")
print("Minimum date:", df["date"].min())
print("Maximum date:", df["date"].max())


print("\n----- NEGATIVE SPEND -----")
print((df["spend"] < 0).sum())


print("\n----- ZERO SPEND -----")
print((df["spend"] == 0).sum())


print("\n----- NEGATIVE REVENUE -----")
print((df["revenue"] < 0).sum())


print("\n----- CLICKS GREATER THAN IMPRESSIONS -----")
print((df["clicks"] > df["impressions"]).sum())


print("\n----- CONVERSIONS GREATER THAN CLICKS -----")
print((df["conversions"] > df["clicks"]).sum())


print("\n----- REACH GREATER THAN IMPRESSIONS -----")
print((df["reach"] > df["impressions"]).sum())